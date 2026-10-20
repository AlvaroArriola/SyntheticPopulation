"""Análisis factorial confirmatorio de V-LATENTE con datos simulados."""

import numpy as np

from sinpop.opinion import factorial as F


def _simular(n: int, cargas: list[float], rho: float, semilla: int = 0):
    rng = np.random.default_rng(semilla)
    f = rng.multivariate_normal([0, 0], [[1, rho], [rho, 1]], size=n)
    asign = [0, 0, 0, 1, 1, 1]
    x = np.column_stack(
        [
            cargas[i] * f[:, asign[i]] + np.sqrt(1 - cargas[i] ** 2) * rng.normal(size=n)
            for i in range(6)
        ]
    )
    return np.corrcoef(x, rowvar=False), asign


def test_modelo_correcto_ajusta_bien_y_recupera_parametros():
    S, asign = _simular(5000, [0.8, 0.7, 0.6, 0.75, 0.65, 0.7], 0.3)
    a = F.ajustar(S, 5000, asign)
    assert a.cfi > 0.99 and a.rmsea < 0.03
    assert a.gl == 8
    np.testing.assert_allclose(
        np.abs(a.cargas[np.arange(6), asign]), [0.8, 0.7, 0.6, 0.75, 0.65, 0.7], atol=0.05
    )
    assert abs(abs(a.phi[0, 1]) - 0.3) < 0.05
    assert (a.omega > 0.6).all()


def test_modelo_mal_especificado_ajusta_peor():
    S, _ = _simular(5000, [0.8, 0.7, 0.6, 0.75, 0.65, 0.7], 0.0)
    mal = F.ajustar(S, 5000, [0, 1, 0, 1, 0, 1])  # ítems asignados al factor equivocado
    bien = F.ajustar(S, 5000, [0, 0, 0, 1, 1, 1])
    assert mal.cfi < bien.cfi and mal.rmsea > bien.rmsea
