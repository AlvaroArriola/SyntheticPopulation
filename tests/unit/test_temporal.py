"""Piezas de la dimensión temporal (F8C) que no necesitan los microdatos."""

from __future__ import annotations

import datetime as dt

import numpy as np

from sinpop.temporal import indicadores as T
from sinpop.temporal.eventos import ventanas
from sinpop.temporal.modelo import kalman
from sinpop.temporal.trayectorias import orden


def test_meses_del_periodo() -> None:
    m = T.meses()
    assert m[0] == T.config()["periodo"]["desde"]
    assert m[-1] == T.config()["periodo"]["hasta"]
    assert len(m) == len(set(m)) and m == sorted(m)


def test_kalman_sin_varianza_de_paseo_es_la_media() -> None:
    d = np.array([1.0, 2.0, 3.0, np.nan, 2.0])
    v = np.full(5, 1.0)
    s, _ = kalman(d, v, 0.0, suavizar=True)
    assert np.allclose(s, 2.0, atol=1e-3)


def test_kalman_con_paseo_grande_sigue_el_ultimo_dato() -> None:
    d = np.array([0.0, 0.0, 5.0])
    f, _ = kalman(d, np.full(3, 1e-6), 10.0, suavizar=False)
    assert abs(f[-1] - 5.0) < 1e-3


def test_kalman_mes_sin_dato_mantiene_el_nivel() -> None:
    d = np.array([1.0, np.nan])
    f, _ = kalman(d, np.full(2, 0.01), 0.1, suavizar=False)
    assert f[1] == f[0]


def test_ventanas_de_un_evento() -> None:
    meses = ["2024-08", "2024-09", "2024-10", "2024-11", "2024-12"]
    # campo del barómetro en la primera quincena: un evento del día 29 deja octubre «antes»
    a, d = ventanas(dt.date(2024, 10, 29), meses)
    assert a == ["2024-09", "2024-10"] and d == ["2024-11", "2024-12"]
    a, d = ventanas(dt.date(2024, 10, 5), meses)
    assert a == ["2024-08", "2024-09"] and d == ["2024-11", "2024-12"]


def test_orden_de_categorias() -> None:
    assert orden("economia_espana", ["NS_NC", "buena", "mala", "regular"]) == [
        "buena",
        "regular",
        "mala",
        "NS_NC",
    ]
    assert orden("problema_vivienda", ["si", "no"]) == ["no", "si"]
    assert orden("ideologia_bloque", ["NS_NC", "centro", "derecha", "izquierda"]) == [
        "izquierda",
        "centro",
        "derecha",
        "NS_NC",
    ]
