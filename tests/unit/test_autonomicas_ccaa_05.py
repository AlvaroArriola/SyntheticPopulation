"""Lector de las autonómicas de Canarias 2023 (BOC núm. 121, 22-06-2023)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_05

pytestmark = pytest.mark.skipif(not ccaa_05.PDF.exists(), reason="falta el PDF del BOC")

PSOE = "PARTIDO SOCIALISTA OBRERO ESPAÑOL"


@pytest.fixture(scope="module")
def res():
    return ccaa_05.leer()


def test_cuadra_salvo_discrepancia_del_boc(res):
    # En El Hierro las formaciones de los anexos II y III suman 6.218 votos, y el anexo I
    # da 6.216 votos a candidaturas (con válidos y votantes coherentes con 6.216). Es una
    # discrepancia del propio documento; se conservan las cifras publicadas.
    assert res.errores() == [
        "El Hierro: votantes 6473 ≠ candidaturas + blancos + nulos 6475",
        "El Hierro: válidos publicados 6323 ≠ 6325",
        "El Hierro: votos a candidaturas publicados ≠ suma de candidaturas",
    ]
    assert any("Discrepancia" in n and "El Hierro" in n for n in res.notas)
    assert res.ccaa == "05" and res.eleccion == "autonomicas-05-2023"
    assert res.total is None


def test_columna_total_cuadra(res):
    # La columna TOTAL de los anexos II y III coincide con la suma de las 8 circunscripciones
    assert not any("TOTAL" in n for n in res.notas)


def test_circunscripciones(res):
    codigos = ["05-AUT", "38-EH", "35-FV", "35-GC", "38-GO", "35-LZ", "38-LP", "38-TF"]
    assert [c.codigo for c in res.circunscripciones] == codigos
    escanos = {c.codigo: sum(c.escanos.values()) for c in res.circunscripciones}
    assert escanos == {
        "05-AUT": 9, "38-EH": 3, "35-FV": 8, "35-GC": 15,
        "38-GO": 4, "35-LZ": 8, "38-LP": 8, "38-TF": 15,
    }  # fmt: skip
    assert [len(c.votos) for c in res.circunscripciones] == [17, 8, 9, 16, 6, 10, 9, 15]


def test_cifras_publicadas(res):
    c = {x.codigo: x for x in res.circunscripciones}
    aut = c["05-AUT"]
    assert (aut.electores, aut.votantes, aut.validos) == (1_788_706, 928_585, 912_645)
    assert (aut.a_candidaturas, aut.blancos, aut.nulos) == (897_991, 14_654, 15_940)
    assert aut.votos[PSOE] == 295_969 and aut.escanos[PSOE] == 4
    assert aut.votos["AHORA CANARIAS - PARTIDO COMUNISTA DEL PUEBLO CANARIO"] == 2_156
    assert c["38-GO"].votos["AGRUPACIÓN SOCIALISTA GOMERA"] == 6_765
    assert c["38-GO"].escanos["AGRUPACIÓN SOCIALISTA GOMERA"] == 3
    assert c["38-TF"].votos["COALICIÓN CANARIA"] == 123_240
    assert c["35-GC"].votos["HABLEMOS AHORA"] == 4_030
    assert c["35-GC"].escanos["HABLEMOS AHORA"] == 0  # anexo III: sin escaño
    # «―»: no concurre; no se guarda como 0
    assert "COALICIÓN CANARIA" not in c["38-EH"].votos
    assert "NUEVA CANARIAS" not in c["38-GO"].votos
