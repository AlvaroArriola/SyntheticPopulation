"""Tests de las transformaciones de F3 (objetivos) con datos pequeños construidos a mano."""

from __future__ import annotations

import polars as pl
import pytest

from sinpop.targets.build import reescalar
from sinpop.targets.edades import agrupar, etiquetas
from sinpop.targets.fuentes import etiqueta_edad
from sinpop.targets.municipios import TerritorioMunicipios, ajustar


def test_etiquetas_y_agrupacion() -> None:
    assert etiquetas([16, 35, 55, 75]) == ["00-15", "16-34", "35-54", "55-74", "75+"]
    df = pl.DataFrame({"e": [0, 15, 16, 34, 35, 74, 75, 100]})
    g = df.select(agrupar(pl.col("e"), [16, 35, 55, 75], "g"))["g"].to_list()
    assert g == ["00-15", "00-15", "16-34", "16-34", "35-54", "55-74", "75+", "75+"]


@pytest.mark.parametrize(
    ("texto", "etiqueta"),
    [("De 15 a 19 años", "15-19"), ("90 y más años", "90+"), ("Menos de 16 años", "00-15")],
)
def test_rotulos_de_edad(texto: str, etiqueta: str) -> None:
    assert etiqueta_edad(texto) == etiqueta


def test_rotulo_desconocido_detiene() -> None:
    with pytest.raises(ValueError, match="no reconocido"):
        etiqueta_edad("Todas las edades")


def test_reescalar_conserva_efectivos_y_usa_cuotas_nacionales_si_falta_celda() -> None:
    estr = pl.DataFrame(
        {
            "provincia": ["01", "01", "02", "02"],
            "sexo": ["mujer"] * 4,
            "grupo": ["16-34"] * 4,
            "categoria": ["a", "b", "a", "b"],
            "valor": [30.0, 70.0, 0.0, 0.0],  # la provincia 02 no tiene efectivos en la tabla
        }
    )
    base = pl.DataFrame(
        {
            "provincia": ["01", "02"],
            "sexo": ["mujer", "mujer"],
            "g": ["16-34", "16-34"],
            "n": [200.0, 50.0],
        }
    )
    out = reescalar(estr, base, "g").sort("provincia", "categoria")
    assert out["valor"].to_list() == pytest.approx([60.0, 140.0, 15.0, 35.0])
    assert out["valor"].sum() == pytest.approx(base["n"].sum())


def test_ajuste_ipf_respeta_ambos_margenes() -> None:
    celdas = pl.DataFrame(
        {
            "municipio": ["m1", "m1", "m2", "m2"],
            "provincia": ["01"] * 4,
            "k": ["x"] * 4,
            "v": ["esp", "ext", "esp", "ext"],
            "valor": [80.0, 30.0, 20.0, 10.0],  # provincia: esp 100, ext 40
        }
    )
    totales = pl.DataFrame({"municipio": ["m1", "m2"], "k": ["x", "x"], "t": [100.0, 40.0]})
    out = ajustar(celdas, totales, ["k"], "v")
    por_m = dict(out.group_by("municipio").agg(pl.col("valor").sum()).iter_rows())
    por_v = dict(out.group_by("v").agg(pl.col("valor").sum()).iter_rows())
    assert por_m == pytest.approx({"m1": 100.0, "m2": 40.0})
    assert por_v == pytest.approx({"esp": 100.0, "ext": 40.0})


def test_definicion_de_territorio() -> None:
    TerritorioMunicipios(nombre="x", municipios=["28079", "28005"])
    with pytest.raises(ValueError, match="no válidos"):
        TerritorioMunicipios(nombre="x", municipios=["2807"])
    with pytest.raises(ValueError, match="repetidos"):
        TerritorioMunicipios(nombre="x", municipios=["28079", "28079"])
