"""Lector de resultados autonómicos de Cataluña 2024 (DOGC)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_09

pytestmark = pytest.mark.skipif(not ccaa_09.PDF.exists(), reason="falta el PDF del DOGC")

PSC = "PARTIT DELS SOCIALISTES DE CATALUNYA (PSC-PSOE) (PSC)"


def test_cataluna_2024():
    r = ccaa_09.leer()
    assert r.errores() == []
    assert r.ccaa == "09" and r.eleccion == "autonomicas-09-2024"
    assert [c.codigo for c in r.circunscripciones] == ["08", "17", "25", "43"]
    assert r.total is not None
    assert (r.total.electores, r.total.votantes) == (5_754_952, 3_183_137)
    assert (r.total.nulos, r.total.blancos) == (26_667, 35_967)
    assert len(r.total.votos) == 18
    assert sum(r.total.escanos.values()) == 135
    bcn, gi, ll, ta = r.circunscripciones
    assert bcn.votos[PSC] == 707_234 and bcn.escanos[PSC] == 28
    assert gi.a_candidaturas == 297_164  # impreso «297164» en castellano
    assert ll.votos["FRONT NACIONAL DE CATALUNYA (F.N.C.)"] == 110
    assert "FRONT NACIONAL DE CATALUNYA (F.N.C.)" not in bcn.votos  # celda vacía
    assert ta.votos["CONVERGENTS (CNV)"] == 263
    assert sum(c.escanos.get("ALIANÇA CATALANA (ALIANÇA.CAT)", 0) for c in r.circunscripciones) == 2
