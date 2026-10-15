"""Lector de las elecciones a la Asamblea de Melilla de 2023 (BOE, resumen de la JEC)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_19

pytestmark = pytest.mark.skipif(not ccaa_19.PDF.exists(), reason="falta el PDF del BOE")


def test_melilla_2023():
    r = ccaa_19.leer()
    assert r.errores() == []
    assert len(r.circunscripciones) == 1
    c = r.circunscripciones[0]
    assert c.codigo == "52"
    assert (c.electores, c.votantes, c.nulos, c.blancos) == (61_138, 30_239, 486, 394)
    assert (c.validos, c.a_candidaturas) == (29_753, 29_359)
    assert len(c.votos) == 8
    assert c.votos["COALICION POR MELILLA (CPM)"] == 5_590
    assert c.votos["CREANDO MELILLA (CREAME)"] == 74
    assert sum(c.escanos.values()) == 25
    assert c.escanos["PARTIDO POPULAR (PP)"] == 14
