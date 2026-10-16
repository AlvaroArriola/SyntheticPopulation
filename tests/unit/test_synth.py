"""Calibración, integerización, sobremuestreo y métricas de F4 (datos sintéticos de prueba)."""

from __future__ import annotations

import numpy as np
import polars as pl
import pytest
from scipy import sparse

from sinpop.synth import calibracion as C
from sinpop.synth import muestreo as S
from sinpop.validate import metrics as M


def _problema(seed: int = 0):
    """200 unidades, dos variables cruzadas (sexo × grupo) con objetivos coherentes."""
    rng = np.random.default_rng(seed)
    n = 200
    sexo = rng.integers(0, 2, n)
    grupo = rng.integers(0, 3, n)
    X = np.zeros((n, 5))
    X[np.arange(n), sexo] = 1
    X[np.arange(n), 2 + grupo] = 1
    d = np.full(n, 10.0)
    T = np.array([1100.0, 900.0, 700.0, 800.0, 500.0])  # ambos bloques suman 2.000
    return sparse.csr_matrix(X), d, T


@pytest.mark.parametrize("metodo", ["raking", "logit"])
def test_calibracion_reproduce_objetivos(metodo: str) -> None:
    X, d, T = _problema()
    r = C.calibrar(X, d, T, metodo)
    assert r.convergido
    assert np.allclose(X.T @ r.w, T, rtol=1e-6)
    assert np.all(r.w > 0)


def test_logit_respeta_los_limites() -> None:
    X, d, T = _problema()
    r = C.calibrar(X, d, T, "logit", limites=(0.5, 1.5))
    g = r.w / d
    assert r.convergido and g.min() >= 0.5 - 1e-9 and g.max() <= 1.5 + 1e-9


def test_logit_sin_solucion_no_converge() -> None:
    X, d, T = _problema()
    T = T.copy()
    T[0], T[1] = 1900.0, 100.0  # exige factores fuera de [0,9; 1,1]
    r = C.calibrar(X, d, T, "logit", limites=(0.9, 1.1))
    assert not r.convergido


def test_calibracion_rechaza_objetivos_no_positivos() -> None:
    X, d, T = _problema()
    T[0] = 0
    with pytest.raises(ValueError):
        C.calibrar(X, d, T)


def test_diagnostico() -> None:
    X, d, T = _problema()
    r = C.calibrar(X, d, T, "logit")
    dg = C.diagnostico(r, d)
    assert dg["proporcion_en_rango"] == 1.0 and dg["no_positivos"] == 0
    assert 0 < dg["kish_ratio"] <= 1


def test_trs_suma_y_reproducible() -> None:
    rng = np.random.default_rng(1)
    e = rng.random(1000) * 3
    a, b = S.trs(e, 7), S.trs(e, 7)
    assert np.array_equal(a, b)
    assert abs(a.sum() - e.sum()) < 1  # sistemático: difiere menos de una unidad
    assert np.all(a >= np.floor(e)) and np.all(a <= np.ceil(e))
    assert not np.array_equal(a, S.trs(e, 8))


def test_trs_es_insesgado() -> None:
    e = np.array([0.25, 0.5, 1.75, 0.3, 2.2])
    media = np.mean([S.trs(e, s) for s in range(4000)], axis=0)
    assert np.allclose(media, e, atol=0.03)


def test_sobremuestreo() -> None:
    e = np.array([1.0, 1.0, 1.0, 1.0])
    m = np.array([2.0, 2.0, 1.0, 1.0])
    g = np.array([1, 0, 0, 0])
    f, info = S.factores_sobremuestreo(e, m, g, 6, 2)
    assert info["beta"] == pytest.approx(2.0)
    ep = e * f
    assert np.dot(ep, g) == pytest.approx(2.0)  # mínimo pedido
    assert np.dot(ep, m) == pytest.approx(6.0)  # tamaño esperado sin cambios
    # Con peso = 1/f, el total ponderado esperado es el del modo representativo.
    assert np.dot(ep / f, m) == pytest.approx(6.0)
    with pytest.raises(ValueError):
        S.factores_sobremuestreo(e, m, g, 6, 100)


def test_parse_sobremuestreo() -> None:
    sm = S.parse_sobremuestreo("edad>=85:2000")
    assert sm.minimo == 2000
    df = pl.DataFrame({"edad": [80, 85, 90], "sexo": ["mujer", "hombre", "mujer"]})
    assert df.filter(sm.condicion(df.schema))["edad"].to_list() == [85, 90]
    sm2 = S.parse_sobremuestreo("sexo=='mujer':10")
    assert df.filter(sm2.condicion(df.schema)).height == 2
    assert S.parse_sobremuestreo(None) is None
    for malo in ("edad>=85", "edad~85:10", "zz>=1:10"):
        with pytest.raises(ValueError):
            sm = S.parse_sobremuestreo(malo)
            sm.condicion(df.schema)  # type: ignore[union-attr]


def test_metricas() -> None:
    assert M.tvd([1, 1], [1, 1]) == 0
    assert M.tvd([1, 0], [0, 1]) == 1
    assert M.hellinger([2, 2], [1, 1]) == pytest.approx(0, abs=1e-9)
    assert M.srmse([10, 10], [10, 10]) == 0
    assert M.kish([1, 1, 1, 1]) == 4
    assert M.cramer_v([[10, 0], [0, 10]]) == pytest.approx(1)
    assert M.cramer_v([[5, 5], [5, 5]]) == pytest.approx(0)
    r1 = M.tvd_ref([0.5, 0.3, 0.2], 1000, semilla=1)
    r2 = M.tvd_ref([0.5, 0.3, 0.2], 100_000, semilla=1)
    assert r2 < r1 and r1 == M.tvd_ref([0.5, 0.3, 0.2], 1000, semilla=1)
    assert np.allclose(M.sd_mas([0.5], 100), 0.05)
