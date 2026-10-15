"""Lector de las autonómicas de 2023 en la Comunidad de Madrid (BOCM)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_13

pytestmark = pytest.mark.skipif(not ccaa_13.PDF.exists(), reason="falta el PDF del BOCM")


def test_madrid_2023():
    r = ccaa_13.leer()
    assert r.errores() == []
    assert len(r.circunscripciones) == 1
    c = r.circunscripciones[0]
    assert c.codigo == "28"
    assert (c.electores, c.votantes, c.nulos, c.blancos) == (5_211_710, 3_413_819, 34_342, 35_107)
    assert (c.validos, c.a_candidaturas) == (3_379_477, 3_344_370)
    assert len(c.votos) == 13
    assert c.votos["PARTIDO POPULAR"] == 1_599_186
    assert c.votos["MÁS MADRID-VERDES EQUO"] == 620_631
    # Nombre partido en dos líneas en el acta.
    assert c.votos["PARTIDO COMUNISTA DE LOS TRABAJADORES DE ESPAÑA"] == 4_148
    assert c.escanos == {
        "PARTIDO POPULAR": 70,
        "PARTIDO SOCIALISTA OBRERO ESPAÑOL": 27,
        "MÁS MADRID-VERDES EQUO": 27,
        "VOX": 11,
    }
