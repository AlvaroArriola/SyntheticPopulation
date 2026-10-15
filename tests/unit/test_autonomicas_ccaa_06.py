"""Lector de resultados autonómicos de Cantabria 2023 (BOC)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_06

pytestmark = pytest.mark.skipif(not ccaa_06.PDF.exists(), reason="falta el PDF del BOC")


def test_cantabria_2023():
    r = ccaa_06.leer()
    assert r.errores() == []
    assert r.ccaa == "06" and r.eleccion == "autonomicas-06-2023"
    assert len(r.circunscripciones) == 1
    c = r.circunscripciones[0]
    assert c.codigo == "39"
    assert (c.electores, c.votantes, c.nulos, c.blancos) == (507_438, 331_413, 6_685, 5_809)
    assert (c.validos, c.a_candidaturas) == (324_728, 318_919)
    assert len(c.votos) == 12
    assert c.votos["PARTIDO POPULAR DE CANTABRIA"] == 116_198
    assert c.votos["PARTIDO REGIONALISTA DE CANTABRIA"] == 67_523
    assert c.votos["PARTIDO COMUNISTA DE LOS TRABAJADORES DE ESPAÑA"] == 757
    # el acta CERA no se suma al acta general
    assert any("CERA" in n and "no sumada" in n for n in r.notas)


def test_cifra_en_letra():
    assert ccaa_06._letra("Ciento dieciseis mil ciento noventa y ocho") == 116_198
    assert ccaa_06._letra("Mil ciento veinticinco") == 1_125
    assert ccaa_06._letra("Veintiuno") == 21
