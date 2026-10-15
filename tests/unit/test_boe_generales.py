"""Resultados oficiales de las generales de 2023 (Congreso) publicados en el BOE."""

from __future__ import annotations

import pytest

from sinpop.harmonize import boe_generales as bg

pytestmark = pytest.mark.skipif(not bg.PDF.exists(), reason="falta el PDF del BOE")


@pytest.fixture(scope="module")
def datos():
    return bg.leer()


def _celda(votos, provincia, siglas):
    f = votos.filter((votos["provincia"] == provincia) & (votos["siglas"] == siglas))
    assert f.height == 1
    return f.row(0, named=True)


def test_cuadra_por_dentro(datos):
    assert bg.errores(*datos) == []


def test_provincias_y_total_estatal(datos):
    prov, votos, totales = datos
    assert prov.height == 52
    assert prov["provincia"].n_unique() == 52
    assert set(votos["provincia"]) == set(prov["provincia"])
    assert totales["cuadro_i"]["electores"] == 37_469_458
    assert totales["cuadro_i"]["votantes"] == 24_952_447
    assert totales["total_escanos"] == 350
    assert prov["escanos"].sum() == 350
    # Errata tipográfica del BOE: «9.938.» en el total estatal de Geroa Bai
    assert totales["notas"] == [
        "Total estatal, Geroa Bai (GBAI).: cifra impresa '9.938.', leída '9.938'"
    ]


def test_candidaturas(datos):
    _, votos, totales = datos
    cands = votos.select("candidatura", "siglas").unique()
    assert cands.height == 59
    assert cands["siglas"].n_unique() == 59
    con_escano = set(votos.filter(votos["escanos"] > 0)["siglas"])
    assert con_escano == {
        "PP", "PSOE", "VOX", "SUMAR", "PSC", "ERC", "JUNTS",
        "EH Bildu", "EAJ-PNV", "BNG", "CCa", "UPN",
    }  # fmt: skip
    # Cuadro III: sin columna de escaños
    assert votos.filter(votos["siglas"] == "PACMA")["escanos"].null_count() == 51
    assert totales["candidaturas"]["Partido Popular (PP)"] == {"votos": 8_160_837, "escanos": 137}
    assert totales["candidaturas"]["Fuerza Cívica (FUERZA CÍVICA)"] == {
        "votos": 115,
        "escanos": None,
    }


def test_cifras_leidas_del_boe(datos):
    _, votos, _ = datos
    assert _celda(votos, "02", "PP") == {
        "provincia": "02",
        "candidatura": "Partido Popular (PP)",
        "siglas": "PP",
        "votos": 88_299,
        "escanos": 2,
    }
    assert (_celda(votos, "28", "PP")["votos"], _celda(votos, "28", "PP")["escanos"]) == (
        1_463_183,
        16,
    )
    psc = _celda(votos, "08", "PSC")
    assert psc["candidatura"] == "Partit dels Socialistes de Catalunya (PSC-PSOE) (PSC)"
    assert (psc["votos"], psc["escanos"]) == (952_347, 13)
    # Celda vacía: el PSOE no se presenta en Barcelona (allí concurre el PSC)
    assert votos.filter((votos["provincia"] == "08") & (votos["siglas"] == "PSOE")).height == 0
    # Santa Cruz de Tenerife: casilla de VOX vacía; Sumar 53.632 votos y 0 escaños
    assert votos.filter((votos["provincia"] == "38") & (votos["siglas"] == "VOX")).height == 0
    assert _celda(votos, "38", "SUMAR")["votos"] == 53_632
    assert _celda(votos, "02", "PACMA")["votos"] == 1_261
    assert _celda(votos, "02", "PACMA")["escanos"] is None
    nc = _celda(votos, "35", "NC-bc")
    assert nc["candidatura"] == "Nueva Canarias-Bloque Canarista (NC-bc)"
