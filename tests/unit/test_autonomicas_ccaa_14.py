"""Lector de los resultados autonómicos de la Región de Murcia 2023 (BORM n.º 135)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_14

pytestmark = pytest.mark.skipif(not ccaa_14.PDF.exists(), reason="falta el PDF del BORM")


@pytest.fixture(scope="module")
def res():
    return ccaa_14.leer()


def test_cuadra_salvo_discrepancia_del_borm(res):
    # El edicto publica 694.906 votantes, 51 más que válidos + nulos (684.817 + 10.038); el
    # resto cuadra. Es un error del propio documento y se conserva la cifra publicada.
    assert res.errores() == ["Murcia: votantes 694906 ≠ candidaturas + blancos + nulos 694855"]
    assert any("Discrepancia en el documento oficial" in n for n in res.notas)
    assert len(res.circunscripciones) == 1 and res.total is None


def test_cifras_publicadas(res):
    (c,) = res.circunscripciones
    assert c.codigo == "30"
    assert (c.electores, c.votantes, c.validos, c.nulos) == (1098543, 694906, 684817, 10038)
    assert (c.a_candidaturas, c.blancos) == (676554, 8263)
    assert len(c.votos) == 15
    assert c.votos["VOX"] == 121321
    assert c.votos["PODEMOS-IZQUIERDA UNIDA VERDES-ALIANZA VERDE"] == 32173
    assert c.escanos == {
        "PARTIDO POPULAR": 21,
        "PARTIDO SOCIALISTA OBRERO ESPAÑOL": 13,
        "PODEMOS-IZQUIERDA UNIDA VERDES-ALIANZA VERDE": 2,
        "VOX": 9,
    }


def test_letra():
    assert ccaa_14._letra("Ciento veintiun mil trescientos veintiuno") == 121321
    assert ccaa_14._letra("Quinientos treinta") == 530
    assert ccaa_14._letra("Mil ciento cincuenta y dos") == 1152
