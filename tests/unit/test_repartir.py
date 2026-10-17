"""Reparto del valor de celdas diminutas sin donantes (D-049)."""

import numpy as np
import polars as pl

from sinpop.synth.donantes import _repartir


def test_repartir_conserva_totales_por_cruce():
    c = pl.DataFrame(
        {
            "objetivo": ["a"] * 4,
            "clave": ["x=1;t=1", "x=2;t=1", "x=3;t=1", "x=1;t=2"],
            "valor": [10.0, 30.0, 1.0, 5.0],
        }
    )
    sd = np.array([False, False, True, False])
    usadas = np.array([True, True, False, True])
    r = _repartir(c, sd, usadas)
    assert r.height == c.height
    v = r["valor"].to_list()
    assert np.isclose(v[0] + v[1], 41.0)
    assert np.isclose(v[0] / v[1], 10 / 30)
    assert v[2] == 1.0  # la celda excluida conserva su valor original para el registro
    assert v[3] == 5.0  # otro cruce, intacto
