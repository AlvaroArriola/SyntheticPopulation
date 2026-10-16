"""Métricas de validación de la población (docs/05 §4).

Todas reciben recuentos (o pesos sumados) por celda en el mismo orden y los normalizan.
"""

from __future__ import annotations

import numpy as np


def _prop(x) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    s = x.sum()
    if s <= 0:
        raise ValueError("distribución vacía")
    return x / s


def tvd(sintetica, objetivo) -> float:
    """Distancia de variación total: ½ Σ |p − q|."""
    return float(0.5 * np.abs(_prop(sintetica) - _prop(objetivo)).sum())


def hellinger(sintetica, objetivo) -> float:
    p, q = _prop(sintetica), _prop(objetivo)
    return float(np.sqrt(max(0.0, 1.0 - np.sqrt(p * q).sum())))


def srmse(sintetica, objetivo) -> float:
    """Error cuadrático medio estandarizado sobre totales: RMSE / media del objetivo."""
    x, t = np.asarray(sintetica, float), np.asarray(objetivo, float)
    return float(np.sqrt(np.mean((x - t) ** 2)) / np.mean(t))


def cramer_v(tabla) -> float:
    """V de Cramér de una tabla de contingencia (filas y columnas vacías se ignoran)."""
    t = np.asarray(tabla, dtype=float)
    t = t[t.sum(axis=1) > 0][:, t.sum(axis=0) > 0]
    r, c = t.shape
    if min(r, c) < 2:
        return 0.0
    n = t.sum()
    e = np.outer(t.sum(axis=1), t.sum(axis=0)) / n
    chi2 = float(((t - e) ** 2 / e).sum())
    return float(np.sqrt(chi2 / (n * (min(r, c) - 1))))


def kish(w) -> float:
    w = np.asarray(w, dtype=float)
    return float(w.sum() ** 2 / np.square(w).sum())


def tvd_ref(
    objetivo, n: int, muestras: int = 200, percentil: float = 95, semilla: int = 0
) -> float:
    """TVD_ref(N): percentil de la TVD entre la distribución objetivo y muestras aleatorias
    simples (multinomiales) de tamaño N de esa misma distribución."""
    q = _prop(objetivo)
    rng = np.random.default_rng(semilla)
    x = rng.multinomial(n, q, size=muestras)
    d = 0.5 * np.abs(x / n - q).sum(axis=1)
    return float(np.percentile(d, percentil))


def sd_mas(p, n: int) -> np.ndarray:
    """Desviación típica teórica de una proporción en una muestra aleatoria simple de tamaño N."""
    p = np.asarray(p, dtype=float)
    return np.sqrt(p * (1 - p) / n)
