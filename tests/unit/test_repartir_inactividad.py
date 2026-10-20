"""Reparto de estudiante / otra_inactividad en los cruces fundidos (D-060)."""

import polars as pl

from sinpop.synth import poblacion as PB

RESTO = ";sexo=hombre;edad_tramo_epa=20-24"
EST = "relacion_actividad=estudiante"
OTRA = "relacion_actividad=otra_inactividad"


def _perfil(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.lit("espanola").alias("nacionalidad_grupo"),
        pl.lit("medios").alias("estudios_3"),
        pl.lit("soltero").alias("estado_civil"),
        pl.lit("hijo").alias("relacion_persona_ref"),
        pl.lit("pareja_con_hijos").alias("tipo_hogar"),
        pl.lit(3).alias("tamano_hogar"),
        pl.lit("vivienda_familiar").alias("tipo_residencia"),
    )


def _pers(actividades: list[str]) -> pl.DataFrame:
    n = len(actividades)
    return _perfil(
        pl.DataFrame(
            {
                "person_id": [f"P{i:03d}" for i in range(n)],
                "bloque": ["CCAA:13"] * n,
                "sexo": ["hombre"] * n,
                "edad": [22] * n,
                "relacion_actividad": actividades,
            }
        )
    )


def _fusiones() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "bloque": ["CCAA:13"],
            "objetivo": ["actividad_tramo"],
            "clave": [EST + RESTO],
            "fusionada_en": [OTRA + RESTO],
        }
    )


def _objetivos(monkeypatch, est: float, otra: float) -> None:
    from sinpop.targets import run as T

    obj = pl.DataFrame(
        {
            "objetivo": ["actividad_tramo"] * 2,
            "clave": [EST + RESTO, OTRA + RESTO],
            "valor": [est, otra],
        }
    )
    monkeypatch.setattr(T, "leer", lambda b: obj)


class _Todo(set):
    def __contains__(self, x):
        return True


def test_reparte_con_las_proporciones_del_objetivo(monkeypatch):
    _objetivos(monkeypatch, 80.0, 20.0)
    monkeypatch.setattr(PB, "_combinaciones_donantes", lambda: (_Todo(), _Todo()))
    pers = _pers(["estudiante"] * 40 + ["otra_inactividad"] * 50 + ["ocupado"] * 10)
    out = PB.repartir_inactividad(pers, _fusiones(), 1)
    cuenta = dict(out.group_by("relacion_actividad").len().iter_rows())
    assert cuenta == {"estudiante": 72, "otra_inactividad": 18, "ocupado": 10}
    assert out["_act_modelada"].sum() == 32
    assert out.equals(PB.repartir_inactividad(pers, _fusiones(), 1))  # misma semilla


def test_no_crea_perfiles_sin_donante(monkeypatch):
    _objetivos(monkeypatch, 90.0, 10.0)
    monkeypatch.setattr(PB, "_combinaciones_donantes", lambda: (set(), set()))
    out = PB.repartir_inactividad(_pers(["otra_inactividad"] * 2), _fusiones(), 1)
    assert out["relacion_actividad"].to_list() == ["otra_inactividad"] * 2


def test_sin_fusiones_no_cambia_nada():
    out = PB.repartir_inactividad(_pers(["otra_inactividad"]), pl.DataFrame(), 1)
    assert out["relacion_actividad"].to_list() == ["otra_inactividad"]
    assert out["_act_modelada"].to_list() == [False]
