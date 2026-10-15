"""Tests de integración sobre `data/interim/` (F2). Se omiten si no hay datos armonizados."""

from __future__ import annotations

import json

import polars as pl
import pytest

from sinpop import INTERIM_DIR
from sinpop.harmonize import checks
from sinpop.repro import sha256_file

pytestmark = pytest.mark.skipif(
    not (INTERIM_DIR / "metadata.json").exists(), reason="sin datos armonizados"
)


def test_g21_sin_valores_fuera_de_dominio() -> None:
    assert checks.g21_dominios() == {}


def test_g22_sin_codigos_especiales_numericos() -> None:
    assert checks.g22_especiales() == {}


def test_g23_totales_ponderados() -> None:
    malos = [(t.fichero, t.concepto) for t in checks.g23_totales() if not t.ok]
    assert malos == []


def test_metadatos_y_hashes() -> None:
    meta = json.loads((INTERIM_DIR / "metadata.json").read_text(encoding="utf-8"))
    for nombre, info in meta["salidas"].items():
        path = INTERIM_DIR / info["fichero"]
        assert sha256_file(path) == info["sha256"], nombre
        assert pl.scan_parquet(path).select(pl.len()).collect().item() == info["filas"]
        assert info["entradas"], f"{nombre} sin fuentes registradas"


@pytest.fixture(scope="module")
def c21() -> pl.DataFrame:
    return pl.read_parquet(
        INTERIM_DIR / "censo2021_personas.parquet",
        columns=[
            "household_id",
            "edad",
            "relacion_persona_ref",
            "tamano_hogar",
            "n_personas_hogar",
            "estado_civil",
            "relacion_actividad",
            "ocupacion",
            "n_mayores_65_hogar",
        ],
    )


def test_una_persona_de_referencia_por_hogar(c21: pl.DataFrame) -> None:
    n = c21.group_by("household_id").agg(
        (pl.col("relacion_persona_ref") == "persona_referencia").sum().alias("n"),
        pl.col("edad").max().alias("max"),
        pl.col("edad")
        .filter(pl.col("relacion_persona_ref") == "persona_referencia")
        .first()
        .alias("ref"),
    )
    assert n["n"].unique().to_list() == [1]
    assert (n["ref"] == n["max"]).all()  # la referencia es la persona de más edad (D-021)


def test_tamano_hogar_coherente(c21: pl.DataFrame) -> None:
    esperado = (
        pl.when(pl.col("n_personas_hogar") >= 5)
        .then(pl.lit("5+"))
        .otherwise(pl.col("n_personas_hogar").cast(pl.Utf8))
    )
    assert c21.select((pl.col("tamano_hogar") == esperado).all()).item()


def test_universos(c21: pl.DataFrame) -> None:
    assert c21.filter(pl.col("edad") < 16)["estado_civil"].unique().to_list() == ["NP"]
    assert c21.filter(pl.col("edad") < 15)["relacion_actividad"].unique().to_list() == ["NP"]
    no_ocup = c21.filter(pl.col("relacion_actividad") != "ocupado")
    assert no_ocup["ocupacion"].unique().to_list() == ["NP"]
    ocup = c21.filter(pl.col("relacion_actividad") == "ocupado")
    assert "NP" not in ocup["ocupacion"].unique().to_list()


def test_mayores_65_coherente(c21: pl.DataFrame) -> None:
    n = c21.group_by("household_id").agg(
        (pl.col("edad") >= 65).sum().alias("calc"), pl.col("n_mayores_65_hogar").first()
    )
    assert (n["calc"] == n["n_mayores_65_hogar"]).all()
