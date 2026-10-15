"""Armonización de las tablas de la Estadística Continua de Población a 01/01/2026 (F2).

Salidas (formato largo, códigos armonizados):
- `ecp_viviendas_familiares`: provincia × sexo × edad_5 × nacionalidad_esp_ext (tabla 60129).
- `ecp_total`: provincia × sexo × edad (simple) (tabla 59589).
- `ecp_colectivos`: provincia × sexo × edad_5 = total − viviendas familiares (D-021).
- `ecp_hogares`: provincia × tamaño del hogar (1, 2, 3, 4+) (tabla 60133).
"""

from __future__ import annotations

import re

import polars as pl

from sinpop import RAW_DIR
from sinpop.harmonize.core import edad_5
from sinpop.ingest.ine_tablas import leer

ECP = RAW_DIR / "ecp/2026-01-01"
SEXO = {"Hombres": "hombre", "Mujeres": "mujer"}
NACIO = {"Española": "espanola", "Extranjera": "extranjera"}


def _grupo(nombre: str | None, semi: str | None) -> str | None:
    if semi == "90 y más años":
        return "90+"
    if nombre is None:
        return None
    m = re.match(r"De (\d+) a (\d+) años", nombre)
    if not m:
        return None
    a, b = int(m.group(1)), int(m.group(2))
    return f"{a:02d}-{b:02d}"


def viviendas_familiares() -> pl.DataFrame:
    df = leer(ECP / "tabla_60129_20260101.json")
    df = df.filter(
        pl.col("Provincias").is_not_null()
        & pl.col("Sexo").is_in(list(SEXO))
        & pl.col("Nacionalidad").is_in(list(NACIO))
    )
    grupos = [
        _grupo(g, s) for g, s in df.select("Grupos de edad", "Semiintervalos de edad").iter_rows()
    ]
    df = df.with_columns(pl.Series("edad_5", grupos, dtype=pl.Utf8)).filter(
        pl.col("edad_5").is_not_null()
    )
    return df.select(
        pl.col("Provincias__cod").alias("provincia"),
        pl.col("Sexo").replace_strict(SEXO).alias("sexo"),
        "edad_5",
        pl.col("Nacionalidad").replace_strict(NACIO).alias("nacionalidad_esp_ext"),
        pl.col("valor").alias("personas"),
    ).sort("provincia", "sexo", "edad_5", "nacionalidad_esp_ext")


def total() -> pl.DataFrame:
    df = leer(ECP / "tabla_59589_20260101.json")
    df = df.filter(pl.col("Provincias").is_not_null() & pl.col("Sexo").is_in(list(SEXO)))
    df = df.filter(
        pl.col("Valores simples de edad").is_not_null()
        | pl.col("Semiintervalos de edad").is_not_null()
    )
    edad = (
        pl.when(pl.col("Semiintervalos de edad").is_not_null())
        .then(pl.col("Semiintervalos de edad").str.extract(r"(\d+)").cast(pl.Int32))
        .otherwise(pl.col("Valores simples de edad").str.extract(r"(\d+)").cast(pl.Int32))
    )
    return df.select(
        pl.col("Provincias__cod").alias("provincia"),
        pl.col("Sexo").replace_strict(SEXO).alias("sexo"),
        edad.alias("edad"),
        pl.col("valor").alias("personas"),
    ).sort("provincia", "sexo", "edad")


def colectivos(tot: pl.DataFrame, vf: pl.DataFrame) -> pl.DataFrame:
    t = (
        tot.with_columns(edad_5(pl.col("edad")))
        .group_by("provincia", "sexo", "edad_5")
        .agg(pl.col("personas").sum().alias("total"))
    )
    v = vf.group_by("provincia", "sexo", "edad_5").agg(pl.col("personas").sum().alias("familiares"))
    out = t.join(v, on=["provincia", "sexo", "edad_5"], how="full", coalesce=True).with_columns(
        (pl.col("total") - pl.col("familiares")).alias("personas")
    )
    return out.sort("provincia", "sexo", "edad_5")


def hogares() -> pl.DataFrame:
    df = leer(ECP / "tabla_60133_20260101.json")
    df = df.filter(
        pl.col("Provincias").is_not_null() & (pl.col("Composición del hogar") != "Total")
    )
    return df.select(
        pl.col("Provincias__cod").alias("provincia"),
        pl.col("Composición del hogar").replace({"4 y más": "4+"}).alias("tamano_hogar_4"),
        pl.col("valor").alias("hogares"),
    ).sort("provincia", "tamano_hogar_4")
