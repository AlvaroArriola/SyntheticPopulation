"""Lector de resultados autonómicos de Castilla-La Mancha 2023 (DOCM)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_08

pytestmark = pytest.mark.skipif(not ccaa_08.PDF.exists(), reason="falta el PDF del DOCM")


def test_castilla_la_mancha_2023():
    r = ccaa_08.leer()
    assert r.errores() == []
    assert r.ccaa == "08" and r.eleccion == "autonomicas-08-2023"
    assert [c.codigo for c in r.circunscripciones] == ["02", "13", "16", "19", "45"]
    assert r.total is not None
    assert (r.total.electores, r.total.votantes) == (1_591_262, 1_107_507)
    assert (r.total.nulos, r.total.blancos) == (19_054, 15_570)
    cu = r.circunscripciones[2]
    assert cu.nombre == "Cuenca"
    assert cu.votos["+CU-EV"] == 1_984
    assert "ESPAÑA VACIADA" not in cu.votos  # celda vacía en el DOCM
    to = r.circunscripciones[4]
    assert to.votos["PSOE"] == 167_292
    assert to.escanos == {"PSOE": 5, "PP": 3, "VOX": 1}
    assert sum(sum(c.escanos.values()) for c in r.circunscripciones) == 33
