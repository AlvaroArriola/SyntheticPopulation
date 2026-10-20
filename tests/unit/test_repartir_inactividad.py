"""Reparto de estudiante / otra_inactividad en los cruces fundidos (D-060)."""

import polars as pl

from sinpop.synth import poblacion as PB


def test_reparte_con_las_proporciones_del_objetivo(monkeypatch):
    from sinpop.targets import run as T

    resto = ";sexo=hombre;edad_tramo_epa=20-24"
    objetivos = pl.DataFrame(
        {
            "objetivo": ["actividad_tramo"] * 2,
            "clave": [
                "relacion_actividad=estudiante" + resto,
                "relacion_actividad=otra_inactividad" + resto,
            ],
            "valor": [80.0, 20.0],
        }
    )
    monkeypatch.setattr(T, "leer", lambda b: objetivos)
    n = 100
    pers = pl.DataFrame(
        {
            "person_id": [f"P{i:03d}" for i in range(n)],
            "bloque": ["CCAA:13"] * n,
            "sexo": ["hombre"] * n,
            "edad": [22] * n,
            "relacion_actividad": ["estudiante"] * 40
            + ["otra_inactividad"] * 50
            + ["ocupado"] * 10,
        }
    )
    fusiones = pl.DataFrame(
        {
            "bloque": ["CCAA:13"],
            "objetivo": ["actividad_tramo"],
            "clave": ["relacion_actividad=estudiante" + resto],
            "fusionada_en": ["relacion_actividad=otra_inactividad" + resto],
        }
    )
    out = PB.repartir_inactividad(pers, fusiones, 1)
    cuenta = dict(out.group_by("relacion_actividad").len().iter_rows())
    assert cuenta == {"estudiante": 72, "otra_inactividad": 18, "ocupado": 10}
    assert out["_act_modelada"].sum() == 32
    assert out.height == n
    # misma semilla, mismo resultado
    assert out.equals(PB.repartir_inactividad(pers, fusiones, 1))


def test_sin_fusiones_no_cambia_nada():
    pers = pl.DataFrame(
        {
            "person_id": ["P1"],
            "bloque": ["ES"],
            "sexo": ["mujer"],
            "edad": [30],
            "relacion_actividad": ["otra_inactividad"],
        }
    )
    vacio = pl.DataFrame(
        schema=dict.fromkeys(["bloque", "objetivo", "clave", "fusionada_en"], pl.Utf8)
    )
    out = PB.repartir_inactividad(pers, vacio, 1)
    assert out["relacion_actividad"].to_list() == ["otra_inactividad"]
    assert out["_act_modelada"].to_list() == [False]
