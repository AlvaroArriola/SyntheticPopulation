"""Separación de capas (regla 9) y reproducibilidad (regla 6)."""

from __future__ import annotations

import numpy as np
import pytest

from sinpop.repro import make_rng, sha256_file
from sinpop.validate.layers import forbidden_base_columns, layer_violations


def test_opinion_and_politics_are_forbidden_in_base() -> None:
    prohibidas = forbidden_base_columns()
    assert {
        "religiosidad",
        "recuerdo_voto_generales",
        "ideologia_autoubicacion",
        "intencion_voto",
        "valoracion_lideres",
    } <= prohibidas
    assert not {"edad", "sexo", "ccaa", "tipo_hogar", "renta_hogar_decil"} & prohibidas


def test_layer_violations_detects_derived_columns() -> None:
    cols = [
        "person_id",
        "edad",
        "sexo",
        "renta_hogar_decil__calidad",
        "religiosidad",
        "recuerdo_voto_generales_familia",
        "ideologia_autoubicacion__calidad",
    ]
    assert layer_violations(cols) == [
        "ideologia_autoubicacion__calidad",
        "recuerdo_voto_generales_familia",
        "religiosidad",
    ]


def test_layer_violations_clean_base() -> None:
    assert layer_violations(["person_id", "household_id", "peso", "es_adulto", "edad"]) == []


def test_rng_requires_int_seed_and_is_deterministic() -> None:
    with pytest.raises(TypeError):
        make_rng(None)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        make_rng(1.5)  # type: ignore[arg-type]
    a = make_rng(42).integers(0, 1000, 10)
    b = make_rng(42).integers(0, 1000, 10)
    assert np.array_equal(a, b)


def test_sha256_file(tmp_path) -> None:
    p = tmp_path / "x.txt"
    p.write_bytes(b"abc")
    assert sha256_file(p) == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
