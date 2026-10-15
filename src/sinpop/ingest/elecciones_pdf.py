"""Lector de las hojas de resultados municipales del Ministerio del Interior (PDF).

Cada página es un municipio con: participación, abstención, votos válidos, votos a
candidatura, en blanco, nulos y votos por candidatura en 2023 (columnas de la izquierda;
las de la derecha comparan con noviembre de 2019 y se ignoran).

Las cifras se comprueban por dentro en cada municipio:
  válidos = a candidatura + en blanco;  participación = válidos + nulos;
  suma de candidaturas = a candidatura.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import polars as pl

_NUM = r"(\d{1,3}(?:\.\d{3})*|\d+)"
_RESUMEN = {
    "Participación": "participacion",
    "Abstención": "abstencion",
    "Votos válidos": "validos",
    "A candidatura": "a_candidatura",
    "En blanco": "blancos",
    "Votos nulos": "nulos",
}


def _int(s: str) -> int:
    return int(s.replace(".", ""))


@dataclass
class Municipio:
    provincia: str
    municipio: str
    resumen: dict[str, int] = field(default_factory=dict)
    candidaturas: dict[str, int] = field(default_factory=dict)

    def errores(self) -> list[str]:
        r = self.resumen
        out = []
        if set(_RESUMEN.values()) - set(r):
            return [f"faltan campos: {sorted(set(_RESUMEN.values()) - set(r))}"]
        if r["validos"] != r["a_candidatura"] + r["blancos"]:
            out.append("válidos ≠ candidatura + blancos")
        if r["participacion"] != r["validos"] + r["nulos"]:
            out.append("participación ≠ válidos + nulos")
        if sum(self.candidaturas.values()) != r["a_candidatura"]:
            out.append(
                f"suma de candidaturas {sum(self.candidaturas.values())} ≠ {r['a_candidatura']}"
            )
        return out


def parse_page(text: str) -> Municipio:
    lines = text.splitlines()
    head = next(i for i, ln in enumerate(lines) if ln.rstrip().endswith("Congreso"))
    parts = re.split(r"\s{2,}", lines[head].strip())
    m = Municipio(provincia=parts[0], municipio=parts[1] if len(parts) > 2 else parts[0])
    i_cand = None
    for i, ln in enumerate(lines):
        s = ln.strip()
        for etiqueta, clave in _RESUMEN.items():
            if s.startswith(etiqueta) and clave not in m.resumen:
                mm = re.match(re.escape(etiqueta) + r"\s+" + _NUM, s)
                if mm:
                    m.resumen[clave] = _int(mm.group(1))
        if s.startswith("Candidaturas"):
            i_cand = i
    if i_cand is None:
        return m
    hdr = lines[i_cand]
    pos_votos = hdr.find("Votos")
    pos_right = hdr.find("Candidaturas", hdr.find("Candidaturas") + 5)
    if pos_right < 0:
        pos_right = len(hdr) + 200
    entradas: list[list] = []  # [nombre, votos]
    bloque_abierto = False
    for ln in lines[i_cand + 1 :]:
        seg = ln[: pos_right - 1]
        if not ln.strip():
            bloque_abierto = False
            continue
        if not seg.strip():
            continue  # solo texto en la columna de 2019
        mv = None
        for mm in re.finditer(r"(?<!\S)" + _NUM + r"(?=\s+\d)", seg):
            if pos_votos - 6 <= mm.start() <= pos_votos + 8:
                mv = mm
                break
        if mv is None:
            mv2 = re.search(r"(?<!\S)" + _NUM + r"\s*$", seg)
            if mv2 and pos_votos - 6 <= mv2.start() <= pos_votos + 8:
                mv = mv2
        if mv is not None:
            entradas.append([seg[: mv.start()].strip(), _int(mv.group(1))])
            bloque_abierto = True
        elif bloque_abierto and entradas:
            texto = seg.strip()
            e = entradas[-1]
            e[0] = f"{e[0]} {texto}".strip() if e[0] else texto
    for nombre, votos in entradas:
        nombre = re.sub(r"\s+", " ", nombre)
        m.candidaturas[nombre] = m.candidaturas.get(nombre, 0) + votos
    return m


def parse_pdf(path: Path) -> list[Municipio]:
    txt = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout
    return [parse_page(p) for p in txt.split("\f") if p.strip()]


def to_frames(
    municipios: list[Municipio], codigo_provincia: str
) -> tuple[pl.DataFrame, pl.DataFrame]:
    resumen = pl.DataFrame(
        [{"cpro": codigo_provincia, "municipio": m.municipio, **m.resumen} for m in municipios]
    )
    votos = pl.DataFrame(
        [
            {"cpro": codigo_provincia, "municipio": m.municipio, "candidatura": c, "votos": v}
            for m in municipios
            for c, v in m.candidaturas.items()
        ]
    )
    return resumen, votos
