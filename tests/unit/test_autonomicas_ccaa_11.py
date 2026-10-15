"""Lector de los resultados autonómicos de Extremadura 2025 (DOE n.º 8, 14-01-2026)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_11

pytestmark = pytest.mark.skipif(not ccaa_11.PDF.exists(), reason="falta el PDF del DOE")


@pytest.fixture(scope="module")
def res():
    return ccaa_11.leer()


def test_cuadra(res):
    assert res.errores() == []
    assert res.total is None
    assert [c.codigo for c in res.circunscripciones] == ["06", "10"]


def test_cifras_publicadas(res):
    badajoz, caceres = res.circunscripciones
    assert (badajoz.electores, badajoz.votantes, badajoz.nulos) == (551424, 337037, 6694)
    assert (caceres.electores, caceres.votantes, caceres.blancos) == (339614, 204689, 2082)
    assert badajoz.votos["PARTIDO POPULAR"] == 140811
    assert caceres.votos["EXTREMADURA UNIDA"] == 1548
    assert "EXTREMADURA UNIDA" not in badajoz.votos
    assert len(badajoz.votos) == 10 and len(caceres.votos) == 11
    assert sum(badajoz.escanos.values()) == 36 and sum(caceres.escanos.values()) == 29
    assert caceres.escanos["UNIDAS POR EXTREMADURA PODEMOS IZQUIERDA UNIDA ALIANZA VERDE"] == 3
