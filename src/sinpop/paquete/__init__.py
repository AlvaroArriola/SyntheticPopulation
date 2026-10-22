"""Paquete portable de predicción (D-076).

Permite usar la capa de predicción y la interfaz en un equipo **sin microdatos**. Con la variable
de entorno `SINPOP_PAQUETE=<carpeta>`, el predictor:

- toma el banco de preguntas (enunciados públicos) de `banco.parquet`;
- aplica a la población sintética los modelos ya ajustados de cada pregunta del banco
  (`modelos.jsonl.gz`: coeficientes, codificación de los predictores, distribución observada y
  recuentos por grupo; todo agregados) en lugar de reajustarlos con los encuestados;
- lee los marcos de las poblaciones sintéticas (`marcos/`), las calibraciones y el modelo de
  confianza del paquete.

El paquete lo construye `python -m sinpop.paquete.exportar` donde están los datos. No contiene
microdatos de ninguna fuente ni atributos copiados de donantes de la ESS (regla 8).
"""

from __future__ import annotations

import gzip
import json
import os
from functools import cache
from pathlib import Path

import numpy as np
import polars as pl

VARIABLE = "SINPOP_PAQUETE"


def raiz() -> Path | None:
    v = os.environ.get(VARIABLE)
    return Path(v) if v else None


def activo() -> bool:
    return raiz() is not None


def ruta(*partes: str) -> Path:
    r = raiz()
    if r is None:
        raise RuntimeError(f"{VARIABLE} no está definida")
    return r.joinpath(*partes)


@cache
def modelos() -> dict[str, dict]:
    with gzip.open(ruta("modelos.jsonl.gz"), "rt", encoding="utf-8") as f:
        return {x["id"]: x for x in map(json.loads, f)}


def _matriz(marco: pl.DataFrame, m: dict):
    import scipy.sparse as sp

    from sinpop.opinion.valores import columna

    bloques = []
    for v in m["columnas"]:
        cats = {c: i for i, c in enumerate(m["cats"][v])}
        idx = np.array([cats.get(x, -1) for x in columna(marco, v)])
        ok = idx >= 0
        bloques.append(
            sp.csr_matrix(
                (np.ones(ok.sum()), (np.flatnonzero(ok), idx[ok])),
                shape=(marco.height, len(cats)),
            )
        )
    return sp.hstack(bloques).tocsr()


def probabilidades(m: dict, marco: pl.DataFrame) -> tuple[np.ndarray, list[str]]:
    """Probabilidades por persona sobre las clases propias de la pregunta del banco (la misma
    función que `LogisticRegression.predict_proba` con los coeficientes guardados)."""
    if "constante" in m:
        return np.ones((marco.height, 1)), [m["constante"]]
    z = _matriz(marco, m) @ np.asarray(m["coef"]).T + np.asarray(m["intercept"])
    if z.shape[1] == 1:  # binaria: sklearn guarda una sola fila de coeficientes
        p1 = 1 / (1 + np.exp(-z[:, 0]))
        return np.column_stack([1 - p1, p1]), m["clases"]
    z = z - z.max(1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(1, keepdims=True), m["clases"]
