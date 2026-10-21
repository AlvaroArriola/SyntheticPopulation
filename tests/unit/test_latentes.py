import numpy as np
import pytest

from sinpop.opinion import latentes as L


def test_puntuar_por_etiqueta():
    esc = {"Mucha": 4, "Bastante": 3, "Poca": 2, "Ninguna": 1}
    assert L._puntuar("Mucha", esc, "X") == 4.0
    assert L._puntuar("(NO LEER) Poca", esc, "X") == 2.0
    for nsnc in ["N.S.", "N.C.", "No procede", "N.P."]:
        assert L._puntuar(nsnc, esc, "X") is None
    with pytest.raises(ValueError):  # nunca se inventa un código
        L._puntuar("Regular", esc, "X")


def test_puntuar_numerica():
    assert L._puntuar("0 Ninguna confianza", "numerica", "X") == 0.0
    assert L._puntuar("7", "numerica", "X") == 7.0
    assert L._puntuar("10 Total confianza", "numerica", "X") == 10.0
    assert L._puntuar("N.S.", "numerica", "X") is None
    with pytest.raises(ValueError):
        L._puntuar("Mucha", "numerica", "X")


def test_corr_ponderada():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(2000, 3))
    s = L._corr_ponderada(x, np.ones(2000))
    np.testing.assert_allclose(s, np.corrcoef(x.T), atol=1e-12)
