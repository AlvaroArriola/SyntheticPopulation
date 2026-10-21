"""Construye el modelo de confianza (F10): backtest histórico, ajuste y métricas internas.

Comando: `python -m sinpop.confidence.run`
"""

from __future__ import annotations

import json

import numpy as np
import polars as pl

from sinpop import REPORTS_DIR
from sinpop.confidence import backtest as BT
from sinpop.confidence import modelo as M


def construir(rehacer_backtest: bool = False, paso: int = 2) -> dict:
    if rehacer_backtest or not BT.DESTINO.exists():
        d = BT.ejecutar(paso=paso)
    else:
        d = pl.read_csv(BT.DESTINO)
    # métrica interna honesta: validación cruzada por pregunta (5 pliegues)
    ids = np.array(sorted(d["id"].unique()))
    rng = np.random.default_rng(0)
    pliegue = dict(zip(ids, rng.integers(0, 5, len(ids)), strict=True))
    d = d.with_columns(pl.col("id").replace_strict(pliegue).alias("_pliegue"))
    partes = []
    for f in range(5):
        m = M.ModeloConfianza().ajustar(d.filter(pl.col("_pliegue") != f))
        partes.append(m.predecir(d.filter(pl.col("_pliegue") == f)))
    interna = M.metricas(pl.concat(partes))
    modelo = M.ModeloConfianza().ajustar(d)
    modelo.guardar()
    res = {"filas": d.height, "preguntas": len(ids), "validacion_cruzada_backtest": interna}
    M.guardar_metricas(res, REPORTS_DIR / "fase_10" / "backtest_metricas.json")
    return res


if __name__ == "__main__":
    print(json.dumps(construir(), ensure_ascii=False, indent=1))
