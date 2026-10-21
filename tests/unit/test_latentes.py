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


def test_intermedios_numericos_solo_entre_extremos():
    import polars as pl

    lg = pl.DataFrame(
        {
            "estudio": ["1"] * 5,
            "encuestado": [0, 1, 2, 3, 4],
            "variable": ["X"] * 5,
            "codigo": [1.0, 5.0, 10.0, 98.0, 7.0],
            "etiqueta": ["1 Nada", None, "10 Mucho", "N.S.", None],
        }
    )
    out = L._intermedios_numericos(lg, {"X": "numerica"})
    assert out["etiqueta"].to_list() == ["1 Nada", "5", "10 Mucho", "N.S.", "7"]
    lg2 = lg.with_columns(pl.Series("codigo", [1.0, 5.0, 10.0, 12.0, 7.0]))
    lg2 = lg2.with_columns(pl.Series("etiqueta", ["1 Nada", None, "10 Mucho", None, None]))
    out2 = L._intermedios_numericos(lg2, {"X": "numerica"})
    assert out2["etiqueta"][3] is None  # fuera de los extremos: sigue sin etiqueta
