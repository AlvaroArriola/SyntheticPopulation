"""Lector de las autonómicas de 2023 en Navarra (BON; acta escaneada, transcrita)."""

from __future__ import annotations

import pytest

from sinpop.harmonize.autonomicas import ccaa_15

pytestmark = pytest.mark.skipif(not ccaa_15.PDF.exists(), reason="falta el PDF del BON")


def test_navarra_2023():
    r = ccaa_15.leer()
    assert r.errores() == []
    assert len(r.circunscripciones) == 1
    c = r.circunscripciones[0]
    assert c.codigo == "31"
    assert (c.electores, c.votantes, c.nulos, c.blancos) == (518_998, 334_493, 4_632, 5_860)
    assert (c.validos, c.a_candidaturas) == (329_861, 324_001)
    assert len(c.votos) == 11
    assert c.votos["UNION DEL PUEBLO NAVARRO"] == 92_392
    assert c.votos["VOLUNTAD FORAL"] == 582
    assert sum(c.escanos.values()) == 50
    assert c.escanos["EUSKAL HERRIA BILDU"] == 9


def test_navarra_otro_fichero(tmp_path):
    otro = tmp_path / "otro.pdf"
    otro.write_bytes(b"%PDF-1.4\n")
    with pytest.raises(ValueError, match="no es el fichero transcrito"):
        ccaa_15.leer(otro)


@pytest.mark.skipif(not ccaa_15.PDF_WEB.exists(), reason="falta la página de resultados")
def test_contraste_con_la_web(monkeypatch):
    assert ccaa_15.contraste_web() == []
    # una cifra alterada se detecta
    monkeypatch.setitem(ccaa_15._RESUMEN, "electores", 518_999)
    assert ccaa_15.contraste_web() == ["electores: acta 518999 ≠ web 518998"]
