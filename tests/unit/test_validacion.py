"""Importancia de las variables (D-090) y batería de validación en el servicio (D-091)."""

from __future__ import annotations

import numpy as np
import pytest

from sinpop.predict import importancia as IM


def test_fuerza_cero_si_todos_los_grupos_responden_igual() -> None:
    p = np.array([0.6, 0.4])
    assert IM.fuerza({"a": p, "b": p}, {"a": 0.5, "b": 0.5}, p) == pytest.approx(0.0)


def test_fuerza_uno_si_cada_grupo_da_una_sola_respuesta() -> None:
    g = {"a": np.array([1.0, 0.0]), "b": np.array([0.0, 1.0])}
    assert IM.fuerza(g, {"a": 0.5, "b": 0.5}, np.array([0.5, 0.5])) == pytest.approx(1.0)


def test_fuerza_binaria_es_la_eta_de_toda_la_vida() -> None:
    # η² = varianza entre grupos / varianza total de la respuesta 0/1
    g = {"a": np.array([0.7, 0.3]), "b": np.array([0.3, 0.7])}
    total = np.array([0.5, 0.5])
    eta2 = (0.5 * 0.2**2 + 0.5 * 0.2**2) / (0.5 * 0.5)
    assert IM.fuerza(g, {"a": 0.5, "b": 0.5}, total) == pytest.approx(np.sqrt(eta2))


def test_el_ruido_de_muestreo_se_descuenta() -> None:
    g = {"a": np.array([0.55, 0.45]), "b": np.array([0.45, 0.55])}
    total = np.array([0.5, 0.5])
    sin = IM.fuerza(g, {"a": 0.5, "b": 0.5}, total)
    con = IM.fuerza(g, {"a": 0.5, "b": 0.5}, total, {"a": 100, "b": 100})
    assert con < sin
    # con muy pocos casos, una diferencia así es compatible con el azar
    assert IM.fuerza(g, {"a": 0.5, "b": 0.5}, total, {"a": 20, "b": 20}) == 0.0


def test_importancia_ordena_y_da_la_mayor_diferencia() -> None:
    ops = ["Sí", "No", "N.S."]
    sub = {
        "sexo=hombre": np.array([0.5, 0.45, 0.05]),
        "sexo=mujer": np.array([0.48, 0.47, 0.05]),
        "edad_4=18-34": np.array([0.8, 0.15, 0.05]),
        "edad_4=65+": np.array([0.2, 0.75, 0.05]),
        "edad_4=NC": np.array([0.0, 0.0, 1.0]),  # «No contesta» no es un grupo
    }
    pesos = {"sexo=hombre": 0.5, "sexo=mujer": 0.5, "edad_4=18-34": 0.5, "edad_4=65+": 0.5}
    imp = IM.importancia(sub, pesos, np.array([0.49, 0.46, 0.05]), ops)
    assert [x["dimension"] for x in imp] == ["edad_4", "sexo"]
    assert imp[0]["opcion"] in ("Sí", "No") and imp[0]["diferencia"] == pytest.approx(0.6)
    assert {imp[0]["grupo_alto"], imp[0]["grupo_bajo"]} == {"18-34", "65+"}


def test_resumen_de_la_bateria() -> None:
    from sinpop.servicio import app as A

    q = {
        "id": "CIS-1-P1",
        "enunciado": "¿Algo?",
        "politica": False,
        "metodo": "analogas",
        "tvd": 0.04,
        "similitud_max": 0.9,
        "observado": {"n": 3000},
        "dentro_margen": [True, False],
        "grupos": [
            {"dimension": "sexo", "tvd": 0.06, "ic95_observado": [[0.4, 0.6], [0.4, 0.6]]},
            {"dimension": "sexo", "tvd": 0.08, "ic95_observado": [[0.4, 0.6], [0.4, 0.6]]},
        ],
    }
    q2 = q | {"id": "CIS-1-VALMINIS_3", "tvd": 0.5, "dentro_margen": [False, False]}
    b = {
        "generado": "2026-10-23",
        "estudios": [{"estudio": "1", "fecha": "2026-07", "preguntas": [q, q2]}],
    }
    r = A._resumen_bateria(b)
    assert r["total"]["preguntas"] == 2 and r["total"]["bajo_10_puntos"] == 0.5
    assert r["sin_escalas_dudosas"]["tvd_media"] == pytest.approx(0.04)
    assert r["total"]["opciones_dentro_margen"] == 0.25
    sexo = r["por_dimension"]["sexo"]
    assert sexo["error"] == pytest.approx(0.07) and sexo["grupos"] == 2
    # dos opciones con sd = 0,2/3,92: ruido esperado = 0,5·2·sd·√(2/π)
    assert sexo["ruido_muestreo"] == pytest.approx((0.2 / 3.92) * (2 / np.pi) ** 0.5, rel=1e-3)
    assert r["estudios"][0]["preguntas"][1]["duda"] == "D-089"
    assert "grupos" not in r["estudios"][0]["preguntas"][0]
    # con las escalas corregidas (D-089) ya no se marca ninguna
    r2 = A._resumen_bateria(b | {"escalas": "completadas"})
    assert r2["estudios"][0]["preguntas"][1]["duda"] is None


def test_escalas_con_solo_los_extremos_etiquetados() -> None:
    """D-089: «1 Muy mal» … «10 Muy bien» sin etiquetas intermedias da la escala completa, con la
    misma regla que las respuestas (enteros entre los extremos etiquetados con su número)."""
    import json

    from sinpop.predict import banco as B

    ext = {"0": "No procede", "1": "1 Muy mal", "10": "10 Muy bien", "98": "N.S.", "99": "N.C."}
    completa = {str(i): str(i) for i in range(2, 10)} | ext
    esperado = ["1 Muy mal", *map(str, range(2, 10)), "10 Muy bien", "N.S.", "N.C."]
    assert B._opciones(json.dumps(ext)) == esperado
    assert B._opciones(json.dumps(completa)) == esperado
    # una pregunta normal no cambia, y los códigos de NS/NC no cuentan como extremos
    normal = {"1": "Muy buena", "2": "Buena", "3": "Regular", "8": "N.S.", "9": "N.C."}
    assert B._opciones(json.dumps(normal)) == ["Muy buena", "Buena", "Regular", "N.S.", "N.C."]
