"""Inclinación de la ECV por comunidad en el bloque personal (D-053)."""

import numpy as np

from sinpop.enrich import run as ER


def _datos(semilla: int = 0):
    rng = np.random.default_rng(semilla)
    n = 400
    k = rng.integers(0, 4, n)  # celda de cada donante
    w = rng.uniform(0.5, 2.0, n)
    xs = {
        "discapacidad_limitacion": (rng.random(n) < 0.05).astype(float),
        "privacion_material": (rng.random(n) < 0.08).astype(float),
    }
    conocida = {v: np.ones(n) for v in xs}
    n_c = np.array([100.0, 50.0, 30.0, 20.0])  # receptores por celda
    return w, xs, conocida, k, n_c


def test_sin_inclinacion_es_la_media_por_celdas():
    w, xs, con, k, n_c = _datos()
    lam = dict.fromkeys(ER.INDICADORES_ECV, 0.0)
    v = "discapacidad_limitacion"
    tasa = np.array([(w * xs[v])[k == c].sum() / w[k == c].sum() for c in range(4)])
    esperada = (tasa * n_c).sum() / n_c.sum()
    assert np.isclose(ER.esperada_ecv(v, lam, w, xs, con, k, n_c), esperada)


def test_lambdas_alcanzan_las_dos_prevalencias():
    w, xs, con, k, n_c = _datos(1)
    objetivo = {"discapacidad_limitacion": 0.07, "privacion_material": 0.06}
    lam = ER.lambdas_celdas(objetivo, w, xs, con, k, n_c)
    for v, o in objetivo.items():
        assert np.isclose(ER.esperada_ecv(v, lam, w, xs, con, k, n_c), o, atol=1e-6)


def test_desconocidos_fuera_del_denominador():
    w, xs, con, k, n_c = _datos(2)
    v = "discapacidad_limitacion"
    con[v] = np.where(np.arange(len(w)) % 2 == 0, 1.0, 0.0)
    xs[v] = xs[v] * con[v]
    lam = dict.fromkeys(ER.INDICADORES_ECV, 0.0)
    assert ER.esperada_ecv(v, lam, w, xs, con, k, n_c) > ER.esperada_ecv(
        v, lam, w, xs, {**con, v: np.ones(len(w))}, k, n_c
    )
