"""Lector de las hojas municipales de resultados del Ministerio del Interior."""
# ruff: noqa: E501  (la página reproduce el ancho real del PDF)

from __future__ import annotations

from sinpop.ingest.elecciones_pdf import parse_page

PAGINA = """\
                                      #000000000000000000000b72                  00:00 - 24/07/2023 GMT+2

Barcelona       Alella                                                                     Congreso

2023                                                             Comparado con 10 N - 2019

                          Votos               %                    Votos                  %

Participación             120                 73,94 + 2,59%        3.002                  71,35

Abstención                30                  26,05 -2,59%         1.205                  28,64

Votos válidos             118                 98,19 -0,37%         2.959                  98,56

  A candidatura           116                 98,87 + 0,23%        2.919                  98,64
  En blanco               2                   1,12 -0,23%          40                     1,35

Votos nulos               2                   1,80 + 0,37%         43                     1,43


2023                                                          Comparado con 10 N - 2019

 Candidaturas     Votos           %                       Candidaturas       Votos             %

                  42              25,30       + 6,70        ERC-             32                18,60
    ERC
                                                            SOBIRANISTES
   JxCAT -        33              19,87       -20,82                         70                40,69
                                                             JxCAT-JUNTS
   JUNTS

    PSC           22              13,25       + 8,60         PSC-PSOE        8                 4,65
    VOX           1.019           4,21        + 1,89         VOX             4                 2,32

   RECORTES       0               0
   CERO
"""


def test_parse_page_columns_and_wrapped_names() -> None:
    m = parse_page(PAGINA.replace("1.019", "19"))
    assert (m.provincia, m.municipio) == ("Barcelona", "Alella")
    assert m.resumen == {
        "participacion": 120,
        "abstencion": 30,
        "validos": 118,
        "a_candidatura": 116,
        "blancos": 2,
        "nulos": 2,
    }
    assert m.candidaturas == {
        "ERC": 42,
        "JxCAT - JUNTS": 33,
        "PSC": 22,
        "VOX": 19,
        "RECORTES CERO": 0,
    }
    assert m.errores() == []


def test_thousands_separator_and_inconsistency_detected() -> None:
    m = parse_page(PAGINA)
    assert m.candidaturas["VOX"] == 1019
    assert any("suma de candidaturas" in e for e in m.errores())
