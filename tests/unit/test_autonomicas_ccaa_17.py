"""Lector de las autonómicas de 2023 en La Rioja (BOR)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_17

pytestmark = pytest.mark.skipif(not ccaa_17.PDF.exists(), reason="falta el PDF del BOR")


def test_la_rioja_2023():
    r = ccaa_17.leer()
    assert r.errores() == []
    assert len(r.circunscripciones) == 1
    c = r.circunscripciones[0]
    assert c.codigo == "26"
    assert (c.electores, c.votantes, c.nulos, c.blancos) == (251_919, 170_779, 2_860, 2_360)
    assert len(c.votos) == 10
    assert c.votos["PARTIDO POPULAR"] == 76_205
    assert c.votos["PARTIDO SOCIALISTA OBRERO ESPAÑOL"] == 53_562
    # Nombre partido en dos líneas en el acta.
    assert c.votos["ESCAÑOS EN BLANCO PARA DEJAR ESCAÑOS VACÍOS"] == 619
    assert c.escanos == {}  # el acta publicada no trae escaños
    # El libro por municipio reproduce el acta y trae la fila de residentes ausentes.
    assert not any(n.startswith("Discrepancia") for n in r.notas)
    assert any(n.startswith("CERA incluido") for n in r.notas)
