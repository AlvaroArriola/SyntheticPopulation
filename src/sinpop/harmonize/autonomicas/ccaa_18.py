"""Ceuta: elecciones a la Asamblea de Ceuta del 28 de mayo de 2023.

La Asamblea de Ceuta se elige en las elecciones locales. Fuente: BOE núm. 261, de 1 de
noviembre de 2023, Sec. III, págs. 145194-146077 (BOE-A-2023-22387): resolución de 5 de julio
de 2023 de la Presidencia de la Junta Electoral Central que publica el resumen de resultados de
las elecciones locales (provincias de Santa Cruz de Tenerife a Zaragoza y ciudades autónomas de
Ceuta y Melilla). Ceuta está en la pág. 146076 del BOE (penúltima del PDF). Circunscripción
única (código 51).

Para cada municipio el BOE da electores, votantes, votos a candidaturas, en blanco, válidos y
nulos, y los votos y concejales por candidatura. Este módulo también sirve a Melilla
(`ccaa_19`): el PDF es el mismo y solo cambia el bloque.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa18-2023" / "autonomicas_ccaa18_2023-05-28.pdf"

_NUM = r"(\d{1,3}(?:\.\d{3})*)"
_CAB = re.compile(r"^\s*" + r"\s+".join([_NUM] * 6) + r"\s*$")
_CAND = re.compile(r"^\s+(\S.*?)\s{2,}" + _NUM + r"(?:\s+(\d+))?\s*$")
_PIE = ("Verificable en", "cve: BOE-", "https://www.boe.es", "BOLETÍN OFICIAL DEL ESTADO")


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _pagina(path: Path, n: int) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", "-f", str(n), "-l", str(n), str(path), "-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _num_paginas(path: Path) -> int:
    info = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))


def _bloque(path: Path, provincia: str) -> str:
    """Texto del bloque «Provincia: <provincia>», buscando desde el final del PDF.

    Ceuta y Melilla van al final (orden alfabético, ciudades autónomas al cierre); se leen solo
    las páginas necesarias para no convertir las 884 páginas.
    """
    marca = re.compile(r"^\s*Provincia:\s+" + re.escape(provincia) + r"\s", re.M)
    n = _num_paginas(path)
    for p in range(n, 0, -1):
        txt = _pagina(path, p)
        m = marca.search(txt)
        if m:
            # El bloque termina en el siguiente «Provincia:»; si no lo hay en la página, puede
            # seguir en la siguiente.
            resto = txt[m.end() :]
            if p < n and not re.search(r"^\s*Provincia:", resto, re.M):
                resto += "\n" + _pagina(path, p + 1)
            fin = re.search(r"^\s*Provincia:", resto, re.M)
            return txt[m.start() : m.end()] + (resto[: fin.start()] if fin else resto)
    raise ValueError(f"no se encuentra «Provincia: {provincia}» en {path}")


def leer_ciudad(path: Path, provincia: str, codigo: str, nombre: str) -> Circunscripcion:
    lineas = _bloque(path, provincia).splitlines()
    i_cab = next(i for i, ln in enumerate(lineas) if ln.strip().startswith("Nº. electores"))
    m = _CAB.match(lineas[i_cab + 1])
    if m is None:
        raise ValueError(f"{nombre}: no se leen las cifras de la cabecera")
    electores, votantes, a_cand, blancos, validos, nulos = (_int(x) for x in m.groups())
    i_tab = next(i for i, ln in enumerate(lineas) if ln.strip().startswith("Candidatura"))
    votos: dict[str, int] = {}
    escanos: dict[str, int] = {}
    pendiente = ""  # nombre partido en dos líneas: la primera no lleva cifras
    for ln in lineas[i_tab + 1 :]:
        s = ln.strip()
        if not s:
            continue
        if s.startswith(_PIE) or re.match(r"^Núm\. \d+ ", s):
            continue
        m = _CAND.match(ln)
        if m is None:
            pendiente = f"{pendiente} {s}".strip()
            continue
        cand = re.sub(r"\s+", " ", f"{pendiente} {m.group(1)}").strip()
        pendiente = ""
        if cand in votos:
            raise ValueError(f"{nombre}: candidatura repetida: {cand}")
        votos[cand] = _int(m.group(2))
        if m.group(3):
            escanos[cand] = int(m.group(3))
    if pendiente:
        raise ValueError(f"{nombre}: texto sin cifras al final del bloque: {pendiente}")
    return Circunscripcion(
        codigo=codigo,
        nombre=nombre,
        electores=electores,
        votantes=votantes,
        nulos=nulos,
        blancos=blancos,
        votos=votos,
        escanos=escanos,
        validos=validos,
        a_candidaturas=a_cand,
    )


def notas_boe(ciudad: str) -> list[str]:
    return [
        "Fuente: BOE núm. 261 de 1-11-2023 (BOE-A-2023-22387), resumen de resultados de las "
        "elecciones locales de 28-5-2023 publicado por la Junta Electoral Central según las "
        f"actas de proclamación; bloque «Provincia: {ciudad.upper()}».",
        f"La Asamblea de {ciudad} se elige en las elecciones locales; los «concejales» del BOE "
        "son los escaños de la Asamblea.",
        "Circunscripción única: el bloque es a la vez el total de la ciudad; no se repite en "
        "`total`.",
        "La publicación no dice si los electores y votantes incluyen el CERA.",
    ]


def leer(path: Path = PDF) -> Resultado:
    c = leer_ciudad(path, "CEUTA", "51", "Ceuta")
    return Resultado(
        ccaa="18",
        eleccion="autonomicas-18-2023",
        circunscripciones=[c],
        total=None,
        notas=notas_boe("Ceuta"),
    )
