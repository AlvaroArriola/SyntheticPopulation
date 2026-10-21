"""Validación de F8C: dimensión temporal (docs/04 F8C, docs/05 V-TEMPORAL*).

- G8C.1 V-TEMPORAL (*backtest*): para cada mes de origen t (cada `PASO` meses desde
  `PRIMER_ORIGEN`), el modelo se ajusta solo con los barómetros hasta t (niveles filtrados, sin
  ver el futuro) y predice la proporción nacional de cada categoría en los meses con barómetro de
  t + 1 a t + 3, con el perfil de los encuestados de ese mes (solo sus covariables). La
  referencia es la persistencia: repetir la proporción observada en el último barómetro hasta t.
  Pasa si el error absoluto medio del modelo es menor que el de la persistencia.
- G8C.2 V-TEMPORAL-SERIES: la serie mensual de cada categoría en la población sintética
  (españoles en viviendas familiares, el universo del CIS) frente a la serie del CIS (proporción
  ponderada de los barómetros, la que se publica); diferencia absoluta media ≤ 2 puntos.
- G8C.3: cada evento del banco tiene fecha, fuente y efecto con su intervalo.

Comando: `python -m sinpop.validate.fase8c`
"""

from __future__ import annotations

import datetime as dt
import json

import polars as pl

from sinpop import REPORTS_DIR
from sinpop.config import load_config
from sinpop.repro import code_version
from sinpop.temporal import eventos as EV
from sinpop.temporal import indicadores as T
from sinpop.temporal.modelo import ModeloTemporal

NACIONAL = "2026-01-01_ES_1000000_s1"
RESUMEN = REPORTS_DIR / "fase_08c_validacion.json"
DETALLE = REPORTS_DIR / "fase_08c"
PRIMER_ORIGEN = "2024-06"
PASO = 2
HORIZONTE = 3


def _sumar_meses(m: str, h: int) -> str:
    a, b = map(int, m.split("-"))
    b += h
    a += (b - 1) // 12
    b = (b - 1) % 12 + 1
    return f"{a:04d}-{b:02d}"


def _reparto(d: pl.DataFrame) -> dict:
    t = d.group_by("valor").agg(pl.col("peso").sum())
    s = t["peso"].sum()
    return {k: v / s for k, v in t.iter_rows()}


def backtest(indicador: str) -> pl.DataFrame:
    d = T.datos(indicador)
    con_datos = sorted(d["mes"].unique())
    meses = T.meses()
    origenes = [m for m in con_datos if m >= PRIMER_ORIGEN and _sumar_meses(m, 1) <= meses[-1]]
    origenes = origenes[::PASO]
    filas = []
    for t in origenes:
        hasta = [m for m in meses if m <= t]
        m = ModeloTemporal(indicador).ajustar(d.filter(pl.col("mes") <= t), hasta, suavizar=False)
        ultimo = max(x for x in con_datos if x <= t)
        persist = _reparto(d.filter(pl.col("mes") == ultimo))
        for h in range(1, HORIZONTE + 1):
            objetivo = _sumar_meses(t, h)
            x = d.filter(pl.col("mes") == objetivo)
            if x.is_empty():
                continue
            obs = _reparto(x)
            p = m.probabilidades(x, objetivo)
            w = x["peso"].to_numpy()
            pred = dict(zip(m.clases, (p * w[:, None]).sum(0) / w.sum(), strict=True))
            for cat in sorted(set(obs) | set(pred)):
                filas.append(
                    {
                        "indicador": indicador,
                        "origen": t,
                        "horizonte": h,
                        "mes": objetivo,
                        "categoria": cat,
                        "observada": obs.get(cat, 0.0),
                        "modelo": pred.get(cat, 0.0),
                        "persistencia": persist.get(cat, 0.0),
                    }
                )
    return pl.DataFrame(filas).with_columns(
        ((pl.col("modelo") - pl.col("observada")).abs() * 100).alias("error_modelo_pp"),
        ((pl.col("persistencia") - pl.col("observada")).abs() * 100).alias("error_persistencia_pp"),
    )


def series(run_id: str) -> pl.DataFrame:
    sint = pl.read_csv(DETALLE / f"{run_id}_series_sinteticas.csv")
    filas = []
    for ind in T.indicadores():
        s = T.serie(ind).select("mes", "valor", pl.col("p").alias("p_cis"), "n")
        filas.append(
            s.with_columns(pl.lit(ind).alias("indicador")).join(
                sint.filter(pl.col("indicador") == ind).drop("indicador"),
                on=["mes", "valor"],
                how="left",
            )
        )
    return (
        pl.concat(filas)
        .with_columns(pl.col("p_sintetica").fill_null(0.0))
        .with_columns(((pl.col("p_sintetica") - pl.col("p_cis")).abs() * 100).alias("dif_pp"))
        .select("indicador", "mes", "valor", "n", "p_cis", "p_sintetica", "dif_pp")
    )


def banco() -> dict:
    b = pl.read_parquet(EV.DESTINO)
    eventos = load_config("eventos.yaml").eventos  # type: ignore[attr-defined]
    nac = b.filter(pl.col("grupo") == "nacional")
    sin_efecto = [e.id for e in eventos if e.id not in set(nac["evento"].unique())]
    sin_fuente = [e.id for e in eventos if not e.fuente.strip()]
    incompletos = nac.filter(
        pl.col("efecto").is_null() | pl.col("ic95_inf").is_null() | pl.col("ic95_sup").is_null()
    ).height
    return {
        "eventos": len(eventos),
        "con_efecto": len(eventos) - len(sin_efecto),
        "sin_efecto": sin_efecto,
        "sin_fuente": sin_fuente,
        "filas_sin_intervalo": incompletos,
        "filas": b.height,
        "ok": not sin_efecto and not sin_fuente and incompletos == 0,
    }


def ejecutar(run_id: str = NACIONAL) -> dict:
    DETALLE.mkdir(parents=True, exist_ok=True)
    bt = pl.concat([backtest(i) for i in T.indicadores()])
    bt.write_csv(DETALLE / "backtest.csv")
    por_ind = (
        bt.group_by("indicador")
        .agg(pl.col("error_modelo_pp").mean(), pl.col("error_persistencia_pp").mean())
        .sort("indicador")
    )
    se = series(run_id)
    se.write_csv(DETALLE / f"{run_id}_series_frente_cis.csv")
    umbral = load_config("thresholds.yaml").v_temporal_series.error_medio_max_pp  # type: ignore[attr-defined]
    se_ind = (
        se.group_by("indicador")
        .agg(pl.col("dif_pp").mean(), pl.col("dif_pp").max().alias("max"))
        .sort("indicador")
    )
    res = {
        "fecha": dt.date.today().isoformat(),
        "version_codigo": code_version(),
        "run_id": run_id,
        "g8c1": {
            "origenes": bt["origen"].n_unique(),
            "predicciones": bt.height,
            "error_modelo_pp": float(bt["error_modelo_pp"].mean()),
            "error_persistencia_pp": float(bt["error_persistencia_pp"].mean()),
            "por_indicador": por_ind.to_dicts(),
        },
        "g8c2": {
            "umbral_pp": umbral,
            "comparaciones": se.height,
            "dif_media_pp": float(se["dif_pp"].mean()),
            "por_indicador": se_ind.to_dicts(),
        },
        "g8c3": banco(),
    }
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    return res


if __name__ == "__main__":
    print(json.dumps(ejecutar(), ensure_ascii=False, indent=1))
