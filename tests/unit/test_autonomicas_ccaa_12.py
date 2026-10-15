"""Lector de los resultados autonómicos de Galicia 2024 (DOG n.º 47, 06-03-2024)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_12

pytestmark = pytest.mark.skipif(not ccaa_12.PDF.exists(), reason="falta el PDF del DOG")


@pytest.fixture(scope="module")
def res():
    return ccaa_12.leer()


def test_cuadra_salvo_discrepancia_del_dog(res):
    # El total publicado (sección I) da 100 votos a candidaturas y válidos de más respecto a
    # la suma de candidaturas y de provincias; es un error del propio documento y se conserva.
    assert res.errores() == [
        "Galicia: válidos publicados 1501857 ≠ 1501757",
        "Galicia: votos a candidaturas publicados ≠ suma de candidaturas",
    ]
    assert any("Discrepancia en el documento oficial" in n for n in res.notas)
    assert all(c.errores() == [] for c in res.circunscripciones)
    assert [c.codigo for c in res.circunscripciones] == ["15", "27", "32", "36"]


def test_cifras_publicadas(res):
    t = res.total
    assert (t.electores, t.votantes, t.nulos, t.blancos) == (2693816, 1515944, 14187, 13052)
    assert t.votos["BLOQUE NACIONALISTA GALEGO (BNG)"] == 470692
    ourense = res.circunscripciones[2]
    assert ourense.votantes == 178353
    assert ourense.votos["DEMOCRACIA OURENSANA (DO)"] == 15442
    assert ourense.escanos == {
        "PARTIDO POPULAR (PP)": 8,
        "BLOQUE NACIONALISTA GALEGO (BNG)": 4,
        "PARTIDO DOS SOCIALISTAS DE GALICIA-PSOE (PSdeG-PSOE)": 1,
        "DEMOCRACIA OURENSANA (DO)": 1,
    }
    assert sum(sum(c.escanos.values()) for c in res.circunscripciones) == 75
