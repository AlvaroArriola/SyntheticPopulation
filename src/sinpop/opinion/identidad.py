"""`identidad_territorial` (escala Linz-Moreno) (F8A, D-066).

Los estudios del CIS que la preguntan («Sentimiento nacionalista …») la formulan con el
gentilicio de cada comunidad («Me siento más andaluz/a que español/a»). Se recodifica por la
etiqueta con patrones, independientes del gentilicio; una etiqueta que no encaje detiene el
proceso:

- «Me siento únicamente español/a» → `solo_espanol`
- «Me siento más español/a que X» → `mas_espanol`
- «Me siento tan español/a como X» → `igual`
- «Me siento más X que español/a» → `mas_comunidad`
- «Me siento únicamente X» → `solo_comunidad`
- «(NO LEER) Ninguna de las anteriores» → `ninguna`; «N.S.» y «N.C.» → NS y NC.

Fuentes: los postelectorales autonómicos (miles de encuestados en su comunidad) y el estudio
nacional 3409 (Identidades culturales, nacionales y europeas, mayo de 2023), que cubre todas.
"""

from __future__ import annotations

import re

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion.cis import CORTE, NS_NC
from sinpop.opinion.valores import Modelo, _edad_grupo, perfil_sintetico
from sinpop.repro import make_rng

PATRONES = [  # «Me siento …» en los autonómicos; sin ese prefijo y con mayúscula en el 3409
    (r"^(Me siento )?[úÚ]nicamente español/a$", "solo_espanol"),
    (r"^(Me siento )?[mM]ás español/a que .+$", "mas_espanol"),
    (r"^(Me siento )?[tT]an español/a como .+$", "igual"),
    (r"^(Me siento )?[mM]ás .+ que español/a$", "mas_comunidad"),
    (r"^(Me siento )?[úÚ]nicamente .+$", "solo_comunidad"),
    (r"^(\(NO LEER\) )?Ninguna de (las|ellas|las anteriores).*$", "ninguna"),
]
ENUNCIADO = r"(?i)^sentimiento nacionalista"
COLUMNAS = [
    "sexo",
    "edad_grupo",
    "estudios_3",
    "actividad_3",
    "tamano_municipio_cis",
    "ccaa",
    "ccaa_edad4",
]


def recodificar(etiqueta: str | None) -> str | None:
    if etiqueta is None:
        return None
    et = etiqueta.strip()
    if et in NS_NC:
        return NS_NC[et]
    for patron, valor in PATRONES:
        if re.match(patron, et):
            return valor
    if et in ("No procede", "N.P."):
        return None
    raise ValueError(f"identidad_territorial: etiqueta no prevista {et!r}")


def preguntas() -> pl.DataFrame:
    banco = pl.read_parquet(INTERIM_DIR / "cis_preguntas.parquet")
    return banco.filter(pl.col("enunciado").str.contains(ENUNCIADO)).explode("estudios")


def datos() -> pl.DataFrame:
    q = preguntas()
    claves = q.select(pl.col("estudios").alias("estudio"), "variable").unique()
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .join(claves.lazy(), on=["estudio", "variable"])
        .select("estudio", "encuestado", "etiqueta")
        .collect()
    )
    lg = lg.with_columns(
        pl.col("etiqueta")
        .map_elements(recodificar, return_dtype=pl.Utf8)
        .alias("identidad_territorial")
    ).drop_nulls("identidad_territorial")
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    return (
        p.join(lg.drop("etiqueta"), on=["estudio", "encuestado"])
        .filter(
            (pl.col("edad") >= 18)
            & (pl.col("fecha").str.to_date() < CORTE)
            & (
                pl.col("nacionalidad_esp_ext").is_null()
                | (pl.col("nacionalidad_esp_ext") == "espanola")
            )
            & ~pl.col("estudios_3").is_in(["NC", "NS"])
            & ~pl.col("actividad_3").is_in(["NC", "NS"])
        )
        .with_columns(
            (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
            _edad_grupo(pl.col("edad")),
        )
        .sort("estudio", "encuestado")
    )


def asignar(persons: pl.DataFrame, semilla: int) -> tuple[pl.DataFrame, dict]:
    """Un único modelo con la comunidad y su interacción con la edad, regularizado por
    validación cruzada (como en MRP): las comunidades con estudio autonómico propio (miles de
    encuestados) conservan su patrón y las que solo tienen la muestra del estudio nacional 3409
    (de 8 en Ceuta a 1.198 en Madrid) se encogen hacia el patrón general en vez de quedar vacías
    o copiar su ruido muestral (D-066)."""
    perfil = perfil_sintetico(persons)
    d = datos()
    m = Modelo("identidad_territorial", columnas=COLUMNAS).ajustar(d)
    pr = m.probabilidades(perfil)
    u = make_rng(semilla).random(len(pr))
    idx = (pr.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(m.clases) - 1)
    fuera = (perfil["nacionalidad_esp_ext"] != "espanola") | (
        perfil["tipo_residencia"] != "vivienda_familiar"
    )
    out = perfil.select("person_id").with_columns(
        pl.Series("identidad_territorial", np.array(m.clases)[idx]),
        pl.Series("identidad_territorial__calidad", np.where(fuera, "extrapolada", "modelada")),
    )
    n = dict(d.group_by("ccaa").len().iter_rows())
    return out, {
        "identidad_territorial": {
            "encuestados": d.height,
            "estudios": sorted(d["estudio"].unique()),
            "encuestados_por_ccaa": n,
            "c": m.c_elegido,
        }
    }
