"""Lector de las autonómicas de Aragón de 2026 (informe de resultados definitivos)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_02

pytestmark = pytest.mark.skipif(not ccaa_02.RUTA.exists(), reason="falta el PDF de Aragón")


@pytest.fixture(scope="module")
def res():
    return ccaa_02.leer()


def test_sin_errores(res):
    assert res.errores() == []
    assert res.ccaa == "02" and res.eleccion == "autonomicas-02-2026"


def test_circunscripciones(res):
    assert [c.codigo for c in res.circunscripciones] == ["22", "44", "50"]
    assert all(c.electores is None for c in res.circunscripciones)  # no publicados


def test_cifras_publicadas(res):
    # Cifras leídas a mano en las páginas 5 a 10 del informe.
    t = res.total
    assert (t.votantes, t.nulos, t.blancos, t.validos) == (674_570, 6_271, 7_315, 668_299)
    assert t.votos["PP"] == 228_388 and t.escanos["PP"] == 26
    huesca, teruel, zaragoza = res.circunscripciones
    assert huesca.votantes == 108_309 and huesca.votos["PSOE"] == 28_808
    assert teruel.votos["EXISTE"] == 8_693 and teruel.escanos["EXISTE"] == 2
    assert zaragoza.votos["IU- MOVIMIENTO SUMAR"] == 15_847
    assert sum(sum(c.escanos.values()) for c in res.circunscripciones) == 67


def test_cera_incluido(res):
    assert any(n.startswith("Voto CERA incluido") for n in res.notas)
