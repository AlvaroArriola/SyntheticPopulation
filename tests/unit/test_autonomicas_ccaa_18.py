"""Lector de las elecciones a la Asamblea de Ceuta de 2023 (BOE, resumen de la JEC)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_18

pytestmark = pytest.mark.skipif(not ccaa_18.PDF.exists(), reason="falta el PDF del BOE")


def test_ceuta_2023():
    r = ccaa_18.leer()
    assert r.errores() == []
    assert len(r.circunscripciones) == 1
    c = r.circunscripciones[0]
    assert c.codigo == "51"
    assert (c.electores, c.votantes, c.nulos, c.blancos) == (63_301, 34_685, 403, 394)
    assert (c.validos, c.a_candidaturas) == (34_282, 33_888)
    assert len(c.votos) == 8
    assert c.votos["PARTIDO POPULAR (PP)"] == 11_774
    assert c.votos["LIBRES (LB)"] == 122
    assert sum(c.escanos.values()) == 25
    assert c.escanos["MOVIMIENTO POR LA DIGNIDAD Y LA CIUDADANÍA DE CEUTA (MDYC)"] == 3
