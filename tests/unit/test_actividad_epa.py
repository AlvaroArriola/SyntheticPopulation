"""Situación de inactividad de la EPA y fusión de categorías casi vacías (D-049)."""

import polars as pl

from sinpop.harmonize.encuestas import _situacion_inactividad
from sinpop.synth.pesos import _fusionar_actividad


def test_prioridad_sidi():
    df = pl.DataFrame(
        {
            "SIDI1": ["01", "01", "01", "03", "01", "00", ""],
            "SIDI2": ["02", "", "", "05", "03", "", ""],
            "SIDI3": ["", "", "", "", "", "", ""],
            "CURSR": ["3", "1", "3", "3", "1", "3", "3"],
        }
    )
    out = _situacion_inactividad(df)["SIDI"].to_list()
    # jubilación antes que estudios; estudiante solo con enseñanza reglada
    assert out == ["02", "01", "01NR", "03", "01", "00", ""]


def test_fusion_conserva_totales():
    obj = pl.DataFrame(
        {
            "objetivo": ["actividad_tramo"] * 4 + ["otro"],
            "clave": [
                "relacion_actividad=ocupado;edad_tramo_epa=35-44",
                "relacion_actividad=otra_inactividad;edad_tramo_epa=35-44",
                "relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44",
                "relacion_actividad=estudiante;edad_tramo_epa=35-44",
                "x=1",
            ],
            "valor": [1000.0, 100.0, 1.0, 20.0, 5.0],
        }
    )
    nuevo, fusion = _fusionar_actividad(obj)
    assert list(fusion["actividad_tramo"]) == [
        "relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44"
    ]
    assert nuevo.height == obj.height - 1
    assert abs(nuevo["valor"].sum() - obj["valor"].sum()) < 1e-9
    otra = nuevo.filter(pl.col("clave").str.contains("otra_inactividad"))["valor"][0]
    assert otra == 101.0
