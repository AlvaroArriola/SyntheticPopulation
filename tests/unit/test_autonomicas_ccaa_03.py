"""Lector de las autonómicas de Asturias 2023 (BOPA núm. 119, 22-VI-2023).

Nota: el PDF no tiene texto extraíble y el lector hace OCR (pdftoppm + tesseract) en un
directorio temporal; este módulo tarda del orden de medio minuto.
"""

from __future__ import annotations

import shutil

import pytest

from sinpop.harmonize.autonomicas import ccaa_03

pytestmark = [
    pytest.mark.skipif(not ccaa_03.PDF.exists(), reason="falta el PDF del BOPA"),
    pytest.mark.skipif(
        not (shutil.which("tesseract") and shutil.which("pdftoppm")),
        reason="faltan tesseract o pdftoppm",
    ),
]

IU = "CONVOCATORIA POR ASTURIES IU-MÁS PAÍS-IAS"


@pytest.fixture(scope="module")
def res():
    return ccaa_03.leer()


def test_sin_errores(res):
    assert res.errores() == []
    assert res.ccaa == "03" and res.eleccion == "autonomicas-03-2023"
    assert res.total is None  # la publicación no trae total de la comunidad


def test_circunscripciones(res):
    assert [c.codigo for c in res.circunscripciones] == ["33-C", "33-OC", "33-OR"]
    assert [len(c.votos) for c in res.circunscripciones] == [15, 13, 12]
    # 45 diputados en total
    assert [sum(c.escanos.values()) for c in res.circunscripciones] == [34, 6, 5]


def test_cifras_publicadas(res):
    # Cifras comprobadas a mano en las imágenes de las actas (págs. 1 a 3)
    c, oc, orl = res.circunscripciones
    assert (c.electores, c.votantes, c.validos, c.nulos) == (757_249, 441_558, 435_475, 6_083)
    assert (c.a_candidaturas, c.blancos) == (427_896, 7_579)
    assert c.votos["PARTIDO SOCIALISTA OBRERO ESPAÑOL"] == 157_852
    assert c.escanos["PARTIDO SOCIALISTA OBRERO ESPAÑOL"] == 13
    assert c.votos[IU] == 35_588 and c.escanos[IU] == 3
    assert (oc.electores, oc.votantes, oc.nulos, oc.blancos) == (115_005, 61_652, 969, 1_113)
    assert oc.votos["SOS OCCIDENTE- ESPAÑA VACIADA"] == 2_574
    assert (orl.electores, orl.votantes, orl.nulos, orl.blancos) == (86_404, 41_792, 927, 831)
    assert orl.votos["POR UN MUNDO MAS JUSTO"] == 80
    assert orl.votos[IU] == 1_908 and orl.escanos["PARTIDO POPULAR"] == 2


@pytest.mark.parametrize(
    ("texto", "valor"),
    [
        ("Ciento cincuenta y siete mil ochocientos cincuenta y dos", 157_852),
        ("Veintiun mil doscientos treinta y seis", 21_236),
        ("Mil sesenta y seis", 1_066),
        ("Cien", 100),
        ("Cuatrocientos dieciséis", 416),
        ("Catorce mil veintidos", 14_022),
        ("treinta y", None),
        ("dos mil mil", None),
        ("cien dos", None),
    ],
)
def test_numero_en_letra(texto, valor):
    assert ccaa_03.numero_en_letra(texto) == valor
