"""Armonización de los resultados electorales (F2, G2.6).

Generales 2023 (Congreso): hojas municipales del escrutinio provisional del Ministerio del
Interior, sin voto CERA (D-021). Los PDF identifican el municipio solo por su nombre; aquí se
le asigna el código INE comparando con los nombres del Padrón 2025 (tabla 29005). Los
municipios que han cambiado de nombre entre 2023 y 2025 se resuelven con `RENOMBRADOS`
(D-029). Usansolo (48916) se segregó de Galdakao después de las elecciones: su voto de 2023
está dentro del de Galdakao (48036).
"""

from __future__ import annotations

import json
import re
import unicodedata

import polars as pl

from sinpop import RAW_DIR
from sinpop.harmonize.censos import PADRON_MUNI
from sinpop.ingest.elecciones_pdf import parse_pdf

GENERALES_2023 = RAW_DIR / "infoelectoral_resultados/generales-2023"
_ART = "el|la|los|las|l'|les|els|o|a|os|as|lo|sa|ses|es|s'"

# (provincia, nombre en la hoja de Interior 2023) → código INE (nombre en el Padrón 2025)
RENOMBRADOS = {
    ("03", "Alcocer de Planes"): "03007",  # Alcosser
    ("03", "Facheca"): "03067",  # Fageca
    ("03", "Vall de Gallinera"): "03136",  # Vall de Gallinera, la
    ("08", "Bigues i Riells"): "08023",  # Bigues i Riells del Fai
    ("09", "Santa María Rivarredonda"): "09353",  # Santa María Ribarredonda
    ("10", "Higuera"): "10097",  # Higuera de Albalat
    ("12", "Herbés"): "12068",  # Herbers
    ("17", "Castell-Platja d'Aro"): "17048",  # Castell d'Aro, Platja d'Aro i s'Agaró
    ("17", "Masarac"): "17100",  # Masarac i Vilarnadal
    ("21", "La Zarza-Perrunal"): "21902",  # Zarza-Perrunal, La
    ("24", "Candín"): "24036",  # Valle de Ancares
    ("26", "Lumbreras"): "26091",  # Lumbreras de Cameros
    ("32", "A Rúa de Valdeorras"): "32072",  # Rúa, A
    ("43", "La Bisbal de Falset"): "43027",  # Bisbal de Montsant, La
    ("46", "Alfarp"): "46026",  # Alfarb
    ("46", "Villanueva de Castellón"): "46257",  # Castelló
}


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.strip()).encode("ascii", "ignore").decode().lower()
    m = re.match(rf"^(.*), ({_ART})$", s)
    if m:
        s = f"{m.group(2)} {m.group(1)}"
    return re.sub(r"[^a-z0-9]", "", s)


def nombres_ine() -> dict[str, str]:
    """{código INE de 5 cifras: nombre} de la tabla 29005."""
    out = {}
    for s in json.loads(PADRON_MUNI.read_text(encoding="utf-8")):
        md = {m["T3_Variable"]: m for m in s["MetaData"]}
        if md["Sexo"]["Codigo"] == "0" and md["Tamaño de los municipios"]["Codigo"] == "0":
            out[md["Municipios"]["Codigo"]] = md["Municipios"]["Nombre"].strip()
    return out


def codigo_municipio(cpro: str, nombre: str, indice: dict[tuple[str, str], set[str]]) -> str:
    if (cpro, nombre) in RENOMBRADOS:
        return RENOMBRADOS[(cpro, nombre)]
    cands: set[str] = set()
    for k in [_norm(nombre), *(_norm(p) for p in nombre.split("/"))]:
        cands |= indice.get((cpro, k), set())
    if len(cands) != 1:
        raise ValueError(f"municipio sin código INE único: {cpro} {nombre!r} → {sorted(cands)}")
    return cands.pop()


def _indice() -> dict[tuple[str, str], set[str]]:
    idx: dict[tuple[str, str], set[str]] = {}
    for c, n in nombres_ine().items():
        for k in {_norm(n), *(_norm(p) for p in n.split("/"))}:
            idx.setdefault((c[:2], k), set()).add(c)
    return idx


def generales_2023() -> tuple[pl.DataFrame, pl.DataFrame]:
    """(resumen por municipio, votos por municipio y candidatura)."""
    idx = _indice()
    resumen, votos = [], []
    for f in sorted(GENERALES_2023.glob("congreso2023_prov*.pdf")):
        cpro = f.stem[-2:]
        for m in parse_pdf(f):
            err = m.errores()
            if err:
                raise ValueError(f"{cpro} {m.municipio}: {err}")
            cod = codigo_municipio(cpro, m.municipio, idx)
            r = m.resumen
            resumen.append(
                {
                    "provincia": cpro,
                    "municipio": cod,
                    "nombre_interior": m.municipio,
                    "censo_residentes": r["participacion"] + r["abstencion"],
                    "votantes": r["participacion"],
                    "abstencion": r["abstencion"],
                    "validos": r["validos"],
                    "a_candidatura": r["a_candidatura"],
                    "blancos": r["blancos"],
                    "nulos": r["nulos"],
                }
            )
            votos += [
                {"provincia": cpro, "municipio": cod, "candidatura": c, "votos": v}
                for c, v in m.candidaturas.items()
            ]
    res = pl.DataFrame(resumen).sort("municipio")
    dup = res.filter(pl.col("municipio").is_duplicated())
    if dup.height:
        raise ValueError(f"códigos INE repetidos: {dup['municipio'].unique().to_list()}")
    vot = pl.DataFrame(votos).sort("municipio", "candidatura")
    return res, vot
