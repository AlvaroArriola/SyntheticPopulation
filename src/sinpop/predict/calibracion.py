"""*Backtest* de construcción y calibración de los intervalos (F9, tarea 5) (D-069).

Con datos anteriores al corte: cada pregunta cerrada de los estudios nacionales con campo en
`DESDE`–junio de 2026 se predice como si fuera nueva, con un banco limitado a las preguntas de
estudios **anteriores** a su fecha (ni el propio estudio ni los posteriores). La verdad es su
distribución ponderada entre los españoles de 18+ (el universo del CIS).

De ahí salen:

- la comparación del sistema (población y «como lo mediría el CIS») con B0 y B1;
- los cuantiles conformales q80 y q95 de |observada − predicha| / σ (σ = desacuerdo entre
  análogas y término de escala), que fijan la anchura de los intervalos. Es una calibración con
  datos de construcción: la cobertura se comprueba después en la ventana de validación (G9.5).

La población sintética se construyó con los barómetros de los 12 meses anteriores al corte, que
incluyen estos meses: el *backtest* es algo optimista (se dice en el informe).
"""

from __future__ import annotations

import json

import numpy as np
import polars as pl

from sinpop import REPORTS_DIR
from sinpop.predict import banco as B
from sinpop.predict import estimador as E
from sinpop.predict import opciones as O

DESDE = "2026-04-01"
DETALLE = REPORTS_DIR / "fase_09"


def verdad(estudio: str, variable: str, opciones: list[str]) -> tuple[np.ndarray, int]:
    m = {o: o for o in opciones}
    d = E.encuestados(estudio, variable, m)
    w = d.group_by("valor").agg(pl.col("peso").sum())
    dd = dict(w.iter_rows())
    v = np.array([dd.get(o, 0.0) for o in opciones])
    return v / v.sum(), d.height


def objetivos() -> pl.DataFrame:
    return B.preguntas().filter(pl.col("fecha") >= DESDE)


def ejecutar(limite: int | None = None) -> pl.DataFrame:
    obj = objetivos()
    if limite:
        obj = obj.head(limite)
    previas = {
        r["variable"] + "|" + r["enunciado"]
        for r in B.preguntas().filter(pl.col("fecha") < DESDE).iter_rows(named=True)
    }
    filas = []
    for row in obj.iter_rows(named=True):
        q = E.Pregunta(
            row["id"],
            row["enunciado"],
            row["opciones"],
            O.escala_probable(row["opciones"]),
            row["fecha"][:7],
            [],
        )
        r = E.predecir(q, excluir=pl.col("fecha") >= row["fecha"])
        if not r.analogas:
            continue
        y, n = verdad(row["estudio"], row["variable"], row["opciones"])
        if n < 200:
            continue
        mu, sd = r.sistema_cis["total"], r.sistema_cis_sd["total"]
        for j, o in enumerate(row["opciones"]):
            filas.append(
                {
                    "id": row["id"],
                    "opcion": o,
                    "observada": float(y[j]),
                    "sistema": float(r.sistema["total"][j]),
                    "sistema_cis": float(mu[j]),
                    "sd": float(sd[j]),
                    "b0": float(r.b0[j]),
                    "b1": float(r.b1["total"][j]),
                    "similitud_max": float(r.analogas[0]["similitud"]),
                    "analogas": len(r.analogas),
                    "recurrente": row["variable"] + "|" + row["enunciado"] in previas,
                    "n": n,
                }
            )
    return pl.DataFrame(filas)


def tvd(d: pl.DataFrame, col: str) -> pl.DataFrame:
    return d.group_by("id").agg((0.5 * (pl.col(col) - pl.col("observada")).abs().sum()).alias(col))


MIN_CASOS_TRAMO = 40


def calibrar(d: pl.DataFrame, columna: str = "sistema_cis") -> dict:
    """Cuantiles conformales de |observada − predicha| / σ, globales y por tramo de similitud
    de la mejor análoga (con al menos `MIN_CASOS_TRAMO` opciones)."""
    mu = d[columna].to_numpy()
    s = np.maximum(
        np.sqrt(d["sd"].to_numpy() ** 2 + E.C_ESCALA * np.clip(mu * (1 - mu), 0, None)), E.S_MIN
    )
    z = np.abs(d["observada"].to_numpy() - mu) / np.maximum(s, 1e-6)
    tr = np.array([E.tramo(x) for x in d["similitud_max"].to_numpy()])
    por_tramo = {}
    for t in sorted(set(tr)):
        zt = z[tr == t]
        if len(zt) >= MIN_CASOS_TRAMO:
            por_tramo[t] = {
                "q80": float(np.quantile(zt, 0.80)),
                "q95": float(np.quantile(zt, 0.95)),
                "casos": int(len(zt)),
            }
    return {
        "q80": float(np.quantile(z, 0.80)),
        "q95": float(np.quantile(z, 0.95)),
        "por_tramo": por_tramo,
        "c_escala": E.C_ESCALA,
        "calibrada": True,
        "casos": int(len(z)),
        "preguntas": int(d["id"].n_unique()),
        "desde": DESDE,
    }


def combinar(d: pl.DataFrame) -> dict:
    """Pesos convexos (rejilla de 0,1) de sistema «medición CIS», B0 y B1 que minimizan la TVD
    media del backtest de construcción (docs/03 §2.7: «pesos aprendidos»)."""
    ids = d["id"].to_numpy()
    g = np.unique(ids, return_inverse=True)[1]
    y = d["observada"].to_numpy()
    x = d.select("sistema_cis", "b0", "b1").to_numpy()
    mejor = None
    for a in np.arange(0, 1.0001, 0.1):
        for b in np.arange(0, 1.0001 - a, 0.1):
            w = np.array([a, b, max(0.0, 1 - a - b)])
            t = float(np.bincount(g, 0.5 * np.abs(x @ w - y)).mean())
            if mejor is None or t < mejor[0] - 1e-12:
                mejor = (t, w)
    assert mejor is not None
    return {
        "sistema_cis": float(mejor[1][0]),
        "b0": float(mejor[1][1]),
        "b1": float(mejor[1][2]),
        "tvd_backtest": mejor[0],
    }


def recalibrar() -> dict:
    """Calibración y combinación desde el CSV del backtest (sin volver a predecir)."""
    d = pl.read_csv(DETALLE / "backtest_construccion.csv")
    return _guardar(d)


def _guardar(d: pl.DataFrame) -> dict:
    w = combinar(d)
    d = d.with_columns(
        (
            w["sistema_cis"] * pl.col("sistema_cis")
            + w["b0"] * pl.col("b0")
            + w["b1"] * pl.col("b1")
        ).alias("combinada")
    )
    cal = calibrar(d, "combinada") | {"combinacion": w}
    E.CALIBRACION.parent.mkdir(parents=True, exist_ok=True)
    E.CALIBRACION.write_text(json.dumps(cal, indent=1), "utf-8")
    return cal


def construir() -> dict:
    DETALLE.mkdir(parents=True, exist_ok=True)
    d = ejecutar()
    d.write_csv(DETALLE / "backtest_construccion.csv")
    cal = _guardar(d)
    t = tvd(d, "sistema")
    for c in ["sistema_cis", "b0", "b1"]:
        t = t.join(tvd(d, c), on="id")
    rec = d.select("id", "recurrente").unique()
    t = t.join(rec, on="id")
    resumen = {
        c: {
            "todas": float(t[c].mean()),
            "recurrentes": float(t.filter(pl.col("recurrente"))[c].mean()),
            "nuevas": float(t.filter(~pl.col("recurrente"))[c].mean()),
        }
        for c in ["sistema", "sistema_cis", "b0", "b1"]
    }
    out = {"calibracion": cal, "tvd_media": resumen, "preguntas": t.height}
    (DETALLE / "backtest_construccion.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), "utf-8"
    )
    return out
