"""Fusiones de nacionalidad × sexo (D-058), con la misma regla que nacionalidad × edad."""

import polars as pl

from sinpop.synth import pesos as P


def _obj(filas):
    return pl.DataFrame(
        [("nacionalidad_top_sexo", c, float(v)) for c, v in filas],
        schema=["objetivo", "clave", "valor"],
        orient="row",
    )


def test_nacionalidad_pequena_en_una_celda_y_fundida_a_otras():
    obj = _obj(
        [
            ("nacionalidad_top=marruecos;sexo=hombre", 3000),
            ("nacionalidad_top=marruecos;sexo=mujer", 2500),
            ("nacionalidad_top=paraguay;sexo=hombre", 300),
            ("nacionalidad_top=paraguay;sexo=mujer", 500),
            ("nacionalidad_top=china;sexo=hombre", 40),
            ("nacionalidad_top=china;sexo=mujer", 45),
            ("nacionalidad_top=otras_extranjeras;sexo=hombre", 900),
            ("nacionalidad_top=otras_extranjeras;sexo=mujer", 950),
        ]
    )
    mapa = {"nacionalidad_top=china": "nacionalidad_top=otras_extranjeras"}
    out, m = P._fundir_cruce_nacionalidad(
        obj, "nacionalidad_top_sexo", "sexo", mapa, frozenset(), minimo=2000
    )
    claves = dict(out.select("clave", "valor").iter_rows())
    # Marruecos (≥ 2000) conserva el sexo; Paraguay (< 2000) queda en una sola celda
    assert claves["nacionalidad_top=marruecos;sexo=mujer"] == 2500
    assert claves["nacionalidad_top=paraguay;sexo=todas"] == 800
    # China, fundida en nacionalidad_top, pasa a otras_extranjeras del mismo sexo
    assert claves["nacionalidad_top=otras_extranjeras;sexo=hombre"] == 940
    assert out["valor"].sum() == obj["valor"].sum()
    assert m["nacionalidad_top=china;sexo=mujer"] == "nacionalidad_top=otras_extranjeras;sexo=mujer"


def test_umbral_propio_del_sexo():
    obj = _obj(
        [
            ("nacionalidad_top=paraguay;sexo=hombre", 120),
            ("nacionalidad_top=paraguay;sexo=mujer", 180),
            ("nacionalidad_top=otras_extranjeras;sexo=hombre", 900),
            ("nacionalidad_top=otras_extranjeras;sexo=mujer", 950),
        ]
    )
    out, _ = P._fundir_cruce_nacionalidad(
        obj, "nacionalidad_top_sexo", "sexo", {}, frozenset(), minimo=P.MIN_NACIONALIDAD_SEXO
    )
    claves = dict(out.select("clave", "valor").iter_rows())
    assert claves["nacionalidad_top=paraguay;sexo=mujer"] == 180
    assert claves["nacionalidad_top=paraguay;sexo=hombre"] == 120
