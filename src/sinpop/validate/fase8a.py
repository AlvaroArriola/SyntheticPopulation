"""Validación de F8A: capa de opinión y valores (docs/04 F8A, docs/05 §7).

- G8A.4: distribución de cada variable de valores por comunidad × edad_4 frente al CIS, como
  V-ENRIQ-MARG (≥ 90 % de las celdas en el IC 95 % bootstrap del CIS y TVD nacional ≤ 0,02).
  La comparación se hace en el universo del CIS: personas de nacionalidad española de 18 años
  y más en viviendas familiares.

Comando: `python -m sinpop.validate.fase8a`
"""

from __future__ import annotations

import datetime as dt
import json

import polars as pl

from sinpop import POPULATIONS_DIR, REPORTS_DIR
from sinpop.opinion import run as OR
from sinpop.opinion import valores as V
from sinpop.opinion.cis import VALORES
from sinpop.repro import code_version
from sinpop.validate import metrics as M
from sinpop.validate.enriquecimiento import _props, bootstrap_ic

NACIONAL = "2026-01-01_ES_1000000_s1"
RESUMEN = REPORTS_DIR / "fase_08a_validacion.json"
DETALLE = REPORTS_DIR / "fase_08a"


def _edad_4(edad: pl.Expr) -> pl.Expr:
    return (
        pl.when(edad < 35)
        .then(pl.lit("18-34"))
        .when(edad < 50)
        .then(pl.lit("35-49"))
        .when(edad < 65)
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
        .alias("edad_4")
    )


def sintetica(run_id: str) -> pl.DataFrame:
    d = POPULATIONS_DIR / run_id
    p = pl.read_parquet(
        d / "persons.parquet",
        columns=["person_id", "edad", "ccaa", "peso", "nacionalidad_esp_ext", "tipo_residencia"],
    )
    o = pl.read_parquet(d / "opinion.parquet")
    return (
        p.join(o, on="person_id")
        .filter(
            (pl.col("nacionalidad_esp_ext") == "espanola")
            & (pl.col("tipo_residencia") == "vivienda_familiar")
        )
        .with_columns(_edad_4(pl.col("edad")))
    )


def v_marg_valores(s: pl.DataFrame, replicas: int = 200, semilla: int = 0) -> pl.DataFrame:
    filas = []
    for v in VALORES:
        e = V.datos(v).with_columns(_edad_4(pl.col("edad")))
        ic = bootstrap_ic(e, v, "peso", ["ccaa", "edad_4"], None, replicas, semilla)
        ps = _props(s, v, "peso", ["ccaa", "edad_4"])
        pe = _props(e, v, "peso", ["ccaa", "edad_4"])
        j = (
            ic.join(
                pe.select("ccaa", "edad_4", v, pl.col("p").alias("p_cis")),
                on=["ccaa", "edad_4", v],
                how="left",
            )
            .join(
                ps.select("ccaa", "edad_4", v, pl.col("p").alias("p_sintetica")),
                on=["ccaa", "edad_4", v],
                how="left",
            )
            .filter(pl.col("ccaa").is_in(s["ccaa"].unique().to_list()))
            .with_columns(pl.col("p_sintetica").fill_null(0.0))
        )
        filas.append(
            j.with_columns(
                pl.lit(v).alias("variable"),
                (
                    (pl.col("p_sintetica") >= pl.col("lo") - 1e-12)
                    & (pl.col("p_sintetica") <= pl.col("hi") + 1e-12)
                ).alias("en_ic"),
            ).rename({v: "categoria"})
        )
    return pl.concat(filas, how="diagonal_relaxed")


def tvd_nacional(s: pl.DataFrame) -> list[dict]:
    out = []
    for v in VALORES:
        e = V.datos(v)
        a = _props(s.with_columns(pl.lit(1).alias("_t")), v, "peso", ["_t"]).select(
            v, pl.col("p").alias("p_s")
        )
        b = _props(e.with_columns(pl.lit(1).alias("_t")), v, "peso", ["_t"]).select(
            v, pl.col("p").alias("p_c")
        )
        j = a.join(b, on=v, how="full", coalesce=True).fill_null(0.0)
        out.append({"variable": v, "tvd": M.tvd(j["p_s"], j["p_c"])})
    return out


def ejecutar(run_id: str = NACIONAL) -> dict:
    DETALLE.mkdir(parents=True, exist_ok=True)
    if not (POPULATIONS_DIR / run_id / "opinion.parquet").exists():
        OR.construir(run_id)
    s = sintetica(run_id)
    m = v_marg_valores(s)
    m.write_csv(DETALLE / f"{run_id}_v_marg_valores.csv")
    por_var = (
        m.group_by("variable")
        .agg(pl.col("en_ic").mean().alias("proporcion"), pl.len().alias("celdas"))
        .sort("variable")
    )
    res = {
        "fecha": dt.date.today().isoformat(),
        "version_codigo": code_version(),
        "run_id": run_id,
        "g8a4": {
            "umbral_celdas": 0.90,
            "umbral_tvd": 0.02,
            "por_variable": por_var.to_dicts(),
            "global": float(m["en_ic"].mean()),
            "tvd_nacional": tvd_nacional(s),
        },
    }
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    return res


if __name__ == "__main__":
    r = ejecutar()
    print(json.dumps(r["g8a4"], ensure_ascii=False, indent=1))
