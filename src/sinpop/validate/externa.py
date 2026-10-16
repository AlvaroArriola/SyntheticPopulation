"""Validación externa o triangulación (docs/05 §4): indicadores de la población frente a fuentes
**no usadas para construirla**. No es puerta: se informa y se explica; si una diferencia supera el
doble del umbral de V-CRUCE del nivel (comunidad 0,10; provincia 0,16), se investiga.

- EPA (2T 2026, microdatos ponderados): ocupados, parados e inactivos de 16 y más años en
  viviendas familiares, por comunidad. El Censo usa la relación con la actividad declarada y la
  EPA la definición de la OIT, así que se espera más paro censal (docs/05 §4).
- ECV (2025, ponderada): personas por tamaño de su hogar, por comunidad. Sustituye al tipo de
  hogar que pide docs/05, porque la ECV armonizada no lo trae (se deriva en F6).
- Padrón (tabla 36778, 01/01/2022, el último que publica la nacionalidad por provincia):
  proporción de extranjeros por provincia. La población es de 2026: se espera más extranjeros.
"""

from __future__ import annotations

from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.validate import metrics as M

LIMITE = {"ccaa": 0.10, "provincia": 0.16}  # 2 × V-CRUCE


def _comparar(
    sint: pl.DataFrame, ref: pl.DataFrame, clave: str, cat: str, nivel: str
) -> pl.DataFrame:
    """TVD por territorio entre dos distribuciones (columnas clave, cat, n)."""
    j = sint.join(ref, on=[clave, cat], how="full", coalesce=True, suffix="_ref").fill_null(0)
    filas = []
    for (t,), g in j.group_by(clave, maintain_order=True):
        g = g.sort(cat)
        filas.append(
            {
                nivel: t,
                **{f"sint_{c}": v / g["n"].sum() for c, v in zip(g[cat], g["n"], strict=True)},
                **{
                    f"ref_{c}": v / g["n_ref"].sum()
                    for c, v in zip(g[cat], g["n_ref"], strict=True)
                },
                "tvd": M.tvd(g["n"], g["n_ref"]),
            }
        )
    df = pl.DataFrame(filas).sort(nivel)
    return df.with_columns((pl.col("tvd") <= LIMITE[nivel]).alias("dentro"))


def epa(p: pl.DataFrame) -> pl.DataFrame:
    e = pl.read_parquet(INTERIM_DIR / "epa.parquet").filter(pl.col("relacion_actividad_3") != "NP")
    ref = e.group_by("ccaa", pl.col("relacion_actividad_3").alias("rel")).agg(
        pl.col("peso").sum().alias("n")
    )
    s = p.filter((pl.col("tipo_residencia") == "vivienda_familiar") & (pl.col("edad") >= 16))
    rel = (
        pl.when(pl.col("relacion_actividad").is_in(["ocupado", "parado"]))
        .then(pl.col("relacion_actividad"))
        .otherwise(pl.lit("inactivo"))
    )
    sint = s.group_by("ccaa", rel.alias("rel")).agg(pl.col("peso").sum().alias("n"))
    out = _comparar(sint, ref, "ccaa", "rel", "ccaa")
    return out.with_columns(
        (pl.col("sint_parado") / (pl.col("sint_parado") + pl.col("sint_ocupado"))).alias(
            "paro_sint"
        ),
        (pl.col("ref_parado") / (pl.col("ref_parado") + pl.col("ref_ocupado"))).alias("paro_epa"),
    )


def _tam(x: pl.Expr) -> pl.Expr:
    return pl.when(x >= 5).then(pl.lit("5+")).otherwise(x.cast(pl.Int64).cast(pl.Utf8))


def ecv(p: pl.DataFrame) -> pl.DataFrame:
    v = pl.read_parquet(INTERIM_DIR / "ecv.parquet")
    ref = v.group_by("ccaa", _tam(pl.col("n_personas_hogar")).alias("tam")).agg(
        pl.col("peso").sum().alias("n")
    )
    s = p.filter(pl.col("tipo_residencia") == "vivienda_familiar")
    sint = s.group_by("ccaa", _tam(pl.col("n_personas_hogar")).alias("tam")).agg(
        pl.col("peso").sum().alias("n")
    )
    return _comparar(sint, ref, "ccaa", "tam", "ccaa")


def padron(p: pl.DataFrame, path: Path | None = None) -> pl.DataFrame:
    from sinpop.ingest.ine_tablas import leer

    d = leer(path or RAW_DIR / "padron_continuo/ultimo/tabla_36778_ultimo.json")
    d = d.filter(
        (pl.col("Tamaño del municipio de residencia") == "Total")
        & (pl.col("Sexo") == "Total")
        & pl.col("Provincias__cod").is_not_null()
        & (pl.col("Nacionalidad") != "Total")
    )
    ref = d.select(
        pl.col("Provincias__cod").alias("provincia"),
        pl.when(pl.col("Nacionalidad") == "Española")
        .then(pl.lit("espanola"))
        .otherwise(pl.lit("extranjera"))
        .alias("nac"),
        pl.col("valor").alias("n"),
    )
    sint = p.group_by("provincia", pl.col("nacionalidad_esp_ext").alias("nac")).agg(
        pl.col("peso").sum().alias("n")
    )
    return _comparar(sint, ref, "provincia", "nac", "provincia")


def ejecutar(persons: pl.DataFrame) -> dict[str, pl.DataFrame]:
    return {"epa": epa(persons), "ecv": ecv(persons), "padron": padron(persons)}
