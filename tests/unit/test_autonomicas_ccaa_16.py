"""Lector de las autonómicas del País Vasco de 2024 (BOPV nº 90, 09/05/2024)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_16

pytestmark = pytest.mark.skipif(not ccaa_16.RUTA.exists(), reason="falta el PDF del País Vasco")


@pytest.fixture(scope="module")
def res():
    return ccaa_16.leer()


def test_sin_errores(res):
    assert res.errores() == []
    assert res.ccaa == "16" and res.eleccion == "autonomicas-16-2024"
    assert res.total is None  # el total publicado no trae votantes, nulos ni blancos


def test_circunscripciones(res):
    assert [c.codigo for c in res.circunscripciones] == ["01", "20", "48"]
    assert all(sum(c.escanos.values()) == 25 for c in res.circunscripciones)


def test_cifras_publicadas(res):
    # Cifras leídas a mano en el BOPV.
    alava, gipuzkoa, bizkaia = res.circunscripciones
    assert (alava.electores, alava.votantes) == (261_623, 155_379)
    assert alava.votos["Partido Popular"] == 24_429
    assert bizkaia.votantes == 575_365
    assert bizkaia.votos["Euzko Alderdi Jeltzalea-Partido Nacionalista Vasco (EAJ-PNV)"] == 223_118
    assert gipuzkoa.votos["Sumar"] == 10_617
    assert gipuzkoa.escanos["Euskal Herria Bildu (EH Bildu)"] == 11


def test_total_comunidad(res):
    votos, escanos = ccaa_16.total_comunidad()
    assert votos["Euskal Herria Bildu (EH Bildu)"] == 343_609
    assert escanos == {"EAJ-PNV": 27, "EH Bildu": 27, "PSE-EE": 12, "PP": 7, "Sumar": 1, "Vox": 1}
    assert not any("DISCREPANCIA" in n for n in res.notas)
