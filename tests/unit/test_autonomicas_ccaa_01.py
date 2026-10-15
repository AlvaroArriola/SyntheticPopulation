"""Lector de los resultados autonómicos de Andalucía 2026 (BOJA n.º 108, 08-06-2026)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_01

pytestmark = pytest.mark.skipif(not ccaa_01.PDF.exists(), reason="falta el PDF del BOJA")

POR_ANDALUCIA = (
    "POR ANDALUCIA-IZQUIERDA UNIDA-PODEMOS-MOVIMIENTO SUMAR-INICIATIVA DEL PUEBLO "
    "ANDALUZ-VERDES EQUO-ALTERNATIVA REPUBLICANA-ALIANZA VERDE"
)


@pytest.fixture(scope="module")
def res():
    return ccaa_01.leer()


def test_cuadra_salvo_discrepancia_del_boja(res):
    # En el cuadro I, Granada (y por arrastre el total) da 3 votos a candidaturas y válidos
    # menos que la suma de las formaciones de los cuadros II-III, que sí cuadra con los
    # votantes. Es un error del propio documento y se conservan las cifras publicadas.
    assert res.errores() == [
        "Granada: válidos publicados 480675 ≠ 480678",
        "Granada: votos a candidaturas publicados ≠ suma de candidaturas",
        "Andalucía: válidos publicados 4198230 ≠ 4198233",
        "Andalucía: votos a candidaturas publicados ≠ suma de candidaturas",
    ]
    assert sum("Discrepancia en el documento oficial" in n for n in res.notas) == 2
    assert [c.codigo for c in res.circunscripciones] == [
        "04", "11", "14", "18", "21", "23", "29", "41"
    ]  # fmt: skip


def test_cifras_publicadas(res):
    t = res.total
    assert (t.electores, t.votantes, t.nulos, t.blancos) == (6510871, 4244414, 46181, 40694)
    assert t.votos["PARTIDO POPULAR"] == 1744728
    assert t.votos[POR_ANDALUCIA] == 266213
    assert t.votos["PARITDO AUTÓNOMOS"] == 3752  # errata del BOJA, conservada
    assert len(t.votos) == 27
    assert sum(t.escanos.values()) == 109
    sevilla = res.circunscripciones[-1]
    assert sevilla.votantes == 1057960
    assert sevilla.votos["ADELANTE ANDALUCIA"] == 134654
    assert sevilla.escanos["PARTIDO SOCIALISTA OBRERO ESPAÑOL DE ANDALUCÍA"] == 5
    assert sum(sevilla.escanos.values()) == 18
    jaen = res.circunscripciones[5]
    assert jaen.votos["JAÉN MERECE MÁS"] == 7993
    assert "HUELVA EXISTE" not in jaen.votos  # «---»: no concurre
