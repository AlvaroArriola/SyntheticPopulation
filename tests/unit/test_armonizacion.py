"""Tests de las transformaciones de armonización con datos pequeños construidos a mano."""

from __future__ import annotations

import polars as pl
import pytest

from sinpop.harmonize.censos import _hogar_censo2021
from sinpop.harmonize.core import dominio, edad_4, edad_5, tamano_por_poblacion
from sinpop.harmonize.encuestas import con_deciles


@pytest.mark.parametrize(
    ("edad", "e5", "e4"),
    [
        (0, "00-04", "NP"),
        (17, "15-19", "NP"),
        (18, "15-19", "18-34"),
        (34, "30-34", "18-34"),
        (35, "35-39", "35-49"),
        (64, "60-64", "50-64"),
        (65, "65-69", "65+"),
        (89, "85-89", "65+"),
        (90, "90+", "65+"),
        (110, "90+", "65+"),
    ],
)
def test_grupos_de_edad(edad: int, e5: str, e4: str) -> None:
    df = pl.DataFrame({"edad": [edad]}).select(edad_5(pl.col("edad")), edad_4(pl.col("edad")))
    assert df.row(0) == (e5, e4)
    assert e5 in dominio("edad_5") and e4 in dominio("edad_4")


@pytest.mark.parametrize(
    ("n", "cat"),
    [
        (1, "hasta_2000"),
        (2000, "hasta_2000"),
        (2001, "de_2001_a_10000"),
        (10000, "de_2001_a_10000"),
        (10001, "de_10001_a_50000"),
        (50001, "de_50001_a_100000"),
        (100001, "de_100001_a_500000"),
        (500001, "mas_de_500000"),
    ],
)
def test_tamano_municipio(n: int, cat: str) -> None:
    assert tamano_por_poblacion(n) == cat
    assert cat in dominio("tamano_municipio")


def test_deciles_ponderados() -> None:
    df = pl.DataFrame({"v": list(range(100, 0, -1)), "peso": [2.0] * 100, "g": ["a", "b"] * 50})
    out = con_deciles(df, "v", "d")
    assert out.height == df.height
    assert out["peso"].sum() == df["peso"].sum()
    assert out["v"].to_list() == df["v"].to_list()  # el orden original se conserva
    assert out.group_by("d").len()["len"].to_list() == [10] * 10
    assert out.filter(pl.col("v") == 1)["d"].item() == "D01"
    assert out.filter(pl.col("v") == 100)["d"].item() == "D10"
    por = con_deciles(df, "v", "d", por="g")
    assert set(por["d"]) <= {f"D{i:02d}" for i in range(1, 11)}
    assert por.group_by("g", "d").len()["len"].max() == 5


def _hogares() -> pl.DataFrame:
    filas = [
        # NVIV, NORDEN, edad, CON, PAD, MAD, FAMILIA
        ("1", "01", 40, "02", "", "", "01"),
        ("1", "02", 38, "01", "", "", "01"),
        ("1", "03", 10, "", "01", "02", "01"),
        ("2", "01", 50, "", "", "03", "01"),  # hijo de la persona de más edad
        ("2", "02", 50, "", "", "", "NN"),  # sin familia
        ("2", "03", 80, "", "", "", "01"),  # la de más edad → referencia
        ("3", "01", 30, "", "", "", "NN"),  # empate de edad → menor NORDEN
        ("3", "02", 30, "", "", "", "NN"),
        ("4", "01", 30, "", "", "", "01"),
        ("4", "02", 60, "", "", "", "01"),  # padre/madre de 01 → referencia
        ("4", "03", 28, "", "", "", "01"),  # hermano/a de 01: otro familiar
    ]
    df = pl.DataFrame(
        filas,
        schema=["NVIV", "NORDEN", "VAREDAD", "NORDEN_CON", "NORDEN_PAD", "NORDEN_MAD", "FAMILIA"],
        orient="row",
    )
    return df.with_columns(
        pl.when((pl.col("NVIV") == "4") & pl.col("NORDEN").is_in(["01", "03"]))
        .then(pl.lit("02"))
        .otherwise(pl.col("NORDEN_PAD"))
        .alias("NORDEN_PAD")
    )


def test_persona_de_referencia_y_parentescos() -> None:
    df = _hogares()
    rel = _hogar_censo2021(df)["relacion_persona_ref"].to_list()
    assert len(rel) == df.height
    assert rel == [
        "persona_referencia",
        "pareja",
        "hijo",
        "hijo",
        "no_familiar",
        "persona_referencia",
        "persona_referencia",
        "no_familiar",
        "hijo",
        "persona_referencia",
        "hijo",
    ]
    assert set(rel) <= dominio("relacion_persona_ref")
    # una sola persona de referencia por hogar
    out = df.with_columns(pl.Series("r", rel))
    n = out.group_by("NVIV").agg((pl.col("r") == "persona_referencia").sum().alias("n"))
    assert n["n"].to_list() == [1] * 4


def test_descarte_d026_solo_con_ocupacion_publicada() -> None:
    from sinpop.harmonize.censos import descartados_d026

    con = pl.DataFrame(
        {
            "RELA": ["01", "01", "02"],
            "CNO": ["", "2", ""],
            "CNAE": ["", "C", ""],
            "SITU": ["", "07", ""],
        }
    )
    assert descartados_d026(con).to_list() == [True, False, False]
    # fichero que no publica ocupación (muestras 2024 y 2025): no se descarta a nadie
    sin = pl.DataFrame({"RELA": ["01", "01"], "CNO": ["", ""], "CNAE": ["", ""], "SITU": ["", ""]})
    assert descartados_d026(sin).to_list() == [False, False]
