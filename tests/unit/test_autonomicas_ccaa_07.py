"""Lector de las autonómicas de Castilla y León de 2026 (BOCyL nº 80, 29/04/2026)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_07

pytestmark = pytest.mark.skipif(not ccaa_07.RUTA.exists(), reason="falta el PDF de Castilla y León")


@pytest.fixture(scope="module")
def res():
    return ccaa_07.leer()


def test_sin_errores(res):
    assert res.errores() == []
    assert res.ccaa == "07" and res.eleccion == "autonomicas-07-2026"


def test_circunscripciones(res):
    assert [c.codigo for c in res.circunscripciones] == [
        "05", "09", "24", "34", "37", "40", "42", "47", "49"
    ]  # fmt: skip


def test_cifras_publicadas(res):
    # Cifras leídas a mano en los anexos I a III (páginas 240 a 244 del boletín).
    t = res.total
    assert (t.electores, t.validos, t.nulos, t.blancos) == (2_097_803, 1_255_323, 16_573, 18_570)
    assert t.votantes is None  # no publicada
    assert t.votos["PARTIDO POPULAR (PP)"] == 444_296
    assert t.escanos["PARTIDO POPULAR (PP)"] == 33
    por = {c.codigo: c for c in res.circunscripciones}
    assert por["24"].votos["UNIÓN DEL PUEBLO LEONÉS (UPL)"] == 48_931
    assert por["47"].votos["POR ÁVILA (XÁV)"] == 146
    assert por["42"].escanos["SORIA ¡YA! (SY)"] == 1
    assert por["09"].votos["VÍA BURGALESA MUNICIPALISTA (VBM)"] == 3_621
    assert sum(sum(c.escanos.values()) for c in res.circunscripciones) == 82
