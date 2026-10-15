"""Lector de resultados autonómicos de la Comunitat Valenciana 2023 (DOGV)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_10

pytestmark = pytest.mark.skipif(not ccaa_10.PDF.exists(), reason="falta el PDF del DOGV")


def test_comunitat_valenciana_2023():
    r = ccaa_10.leer()
    assert r.errores() == []
    assert r.ccaa == "10" and r.eleccion == "autonomicas-10-2023"
    assert [c.codigo for c in r.circunscripciones] == ["03", "12", "46"]
    al, cs, va = r.circunscripciones
    assert (al.electores, al.votantes, al.nulos, al.blancos) == (1_304_381, 825_463, 10_887, 10_386)
    assert cs.electores == 430_308 and va.electores == 1_995_970
    assert va.votos["Partido Popular (PP)"] == 457_889
    assert al.votos["Compromís: Més-Iniciativa-Verdsequo (COMPROMÍS)"] == 82_878
    assert r.total is not None
    assert r.total.votantes == 2_498_090
    # errata del DOGV: total de electores publicado 2.426.278 ≠ suma de provincias
    assert r.total.electores is None
    assert any("2.426.278" in n for n in r.notas)
