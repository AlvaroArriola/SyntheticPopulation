"""Piezas de la capa de predicción (F9) que no necesitan microdatos."""

from __future__ import annotations

import numpy as np
import pytest

from sinpop.predict import estimador as E
from sinpop.predict import opciones as O
from sinpop.predict.reformular import reformular


def test_tipos_de_respuesta() -> None:
    assert O.tipo("N.S.") == O.NS
    assert O.tipo("(NO LEER) No sabe") == O.NS
    assert O.tipo("N.C.") == O.NC
    assert O.tipo("No procede.") == "NP"
    assert O.tipo("Muy buena") is None


def test_alinear_por_etiqueta_y_ns_nc() -> None:
    m = O.alinear(
        ["Muy buena", "Buena", "(NO LEER) Regular", "Mala", "Muy mala", "N.S.", "N.C."],
        ["Muy buena", "Buena", "Regular", "Mala", "Muy mala", "No sabe", "No contesta"],
        ordinal=True,
    )
    assert m is not None
    assert m["(NO LEER) Regular"] == "Regular" and m["N.S."] == "No sabe"


def test_alinear_escala_numerica_por_posicion_relativa() -> None:
    origen = ["0 Nada", *[str(i) for i in range(1, 10)], "10 Mucho"]
    destino = ["1 Nada", *[str(i) for i in range(2, 10)], "10 Mucho"]
    m = O.alinear(origen, destino, ordinal=True)
    assert m is not None
    assert m["0 Nada"] == "1 Nada" and m["10 Mucho"] == "10 Mucho"


def test_alinear_nominal_distinta_se_descarta() -> None:
    assert O.alinear(["PP", "PSOE"], ["Sí", "No"], ordinal=False) is None


def test_escala_probable() -> None:
    assert O.escala_probable(["Mucho", "Bastante", "Poco", "Nada", "N.S."]) == "ordinal"
    assert O.escala_probable(["PP", "PSOE", "VOX", "Sumar"]) == "nominal"


def test_reformulacion_neutra_cambia_solo_la_redaccion() -> None:
    r = reformular("Grado de confianza en el Gobierno")
    assert r.startswith("¿") and r.endswith("?")
    assert "nivel de confianza en el Gobierno" in r


def test_intervalos_contienen_p_y_crecen_con_menos_similitud() -> None:
    cal = {
        "q80": 1.3,
        "q95": 2.0,
        "c_escala": 0.0025,
        "por_tramo": {"0.0-0.4": {"q80": 3.0, "q95": 5.0}, "0.7-1.0": {"q80": 1.0, "q95": 1.5}},
    }
    mu, sd = np.array([0.2, 0.8]), np.array([0.01, 0.01])
    a80, a95 = E.intervalos(mu, sd, cal, 0.9)
    b80, _ = E.intervalos(mu, sd, cal, 0.2)
    assert np.all(a80[:, 0] <= mu) and np.all(mu <= a80[:, 1])
    assert np.all(a95[:, 0] <= a80[:, 0])
    assert np.all((b80[:, 1] - b80[:, 0]) > (a80[:, 1] - a80[:, 0]))


def test_validar_detecta_distribucion_que_no_suma_uno() -> None:
    from sinpop.predict import salida as S

    d = {
        "Sí": {"p": 0.6, "ic80": [0.5, 0.7], "ic95": [0.4, 0.8]},
        "No": {"p": 0.3, "ic80": [0.2, 0.4], "ic95": [0.1, 0.5]},
    }
    out = {
        "id": "Q",
        "run_id": "r",
        "total": d,
        "por_subgrupo": {},
        "confianza": {"total": 0.5, "por_subgrupo": {}},
        "parametros_llm": None,
        "preguntas_similares": [],
        "coste": {"llamadas": 0, "tokens": 0, "eur": 0.0, "segundos": 1.0},
        "versiones": {"modelo_llm": None, "prompts": None, "poblacion": "r"},
    }
    with pytest.raises(ValueError, match="suma"):
        S.validar(out, ["Sí", "No"])
