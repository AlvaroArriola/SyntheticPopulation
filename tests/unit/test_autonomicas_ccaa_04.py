"""Lector de las autonómicas de Illes Balears 2023 (BOIB núm. 83): solo voto CERA."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_04

pytestmark = pytest.mark.skipif(not ccaa_04.PDF.exists(), reason="falta el PDF del BOIB")


@pytest.fixture(scope="module")
def res():
    return ccaa_04.leer()


def test_sin_errores(res):
    assert res.errores() == []
    assert res.ccaa == "04" and res.eleccion == "autonomicas-04-2023"
    assert res.total is None


def test_solo_cera_documentado(res):
    assert "SOLO el escrutinio del voto CERA" in res.notas[0]
    assert all(c.notas == "Solo voto CERA." for c in res.circunscripciones)


def test_circunscripciones(res):
    assert [c.codigo for c in res.circunscripciones] == ["07-MA", "07-ME", "07-EF", "07-FO"]
    assert [len(c.votos) for c in res.circunscripciones] == [12, 7, 9, 4]
    assert all(c.escanos == {} for c in res.circunscripciones)


def test_cifras_publicadas(res):
    ma, me, ef, fo = res.circunscripciones
    assert (ma.electores, ma.votantes, ma.blancos, ma.nulos) == (26_419, 1_301, 11, 30)
    assert ma.votos["Partit Socialista de les Illes Balears"] == 394
    assert ma.votos["Partido Popular"] == 354
    assert (me.electores, me.votantes, me.blancos, me.nulos) == (2_847, 132, 0, 5)
    assert me.votos["VOX"] == 12  # impreso «1.VOX», sin espacio
    assert (ef.electores, ef.votantes) == (3_075, 126)
    assert ef.votos["Ciudadanos-Partido de la Ciudadanía"] == 7
    assert (fo.electores, fo.votantes) == (303, 7)
    assert fo.votos["Gent per Formentera + Partit Socialista de les Illes Balears"] == 6
    assert fo.votos["VOX"] == 0


def test_anexo_por_consulado(res):
    # El anexo «Número de votos» por consulado no coincide con los votantes del acta en
    # Mallorca y Menorca (sumas comprobadas a mano); se deja constancia, no es un error.
    assert any("Mallorca: el anexo por consulado suma 1306" in n for n in res.notas)
    assert any("Menorca: el anexo por consulado suma 136" in n for n in res.notas)
    assert not any(n.startswith(("Eivissa", "Formentera")) for n in res.notas)
