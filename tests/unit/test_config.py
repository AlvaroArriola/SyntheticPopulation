"""Esquemas de configuración (puerta G0.2)."""

from __future__ import annotations

import copy
from collections import Counter

import pytest
from pydantic import ValidationError

from sinpop import CONFIGS_DIR
from sinpop.config import load_config, load_yaml, validate_all
from sinpop.config.schemas import SCHEMAS


def test_all_configs_are_valid() -> None:
    assert validate_all() == {name: None for name in SCHEMAS}


def test_every_schema_has_a_config_file() -> None:
    for name in SCHEMAS:
        assert (CONFIGS_DIR / name).exists(), name


def _raw(name: str) -> dict:
    return copy.deepcopy(load_yaml(CONFIGS_DIR / name))  # type: ignore[arg-type]


def test_unknown_keys_are_rejected() -> None:
    raw = _raw("thresholds.yaml")
    raw["V-MARG"]["errata"] = 1
    with pytest.raises(ValidationError):
        SCHEMAS["thresholds.yaml"].model_validate(raw)


def test_targets_reject_reserved_in_calibration() -> None:
    raw = _raw("targets.yaml")
    raw["calibrar"].append(
        {"id": "x", "ambito": "provincia", "variables": ["edad_4", "tipo_hogar"]}
    )
    with pytest.raises(ValidationError, match="calibrados y reservados"):
        SCHEMAS["targets.yaml"].model_validate(raw)


def test_partidos_reject_unknown_family() -> None:
    raw = _raw("partidos.yaml")
    raw["elecciones"]["generales-2023"]["candidaturas"] = [
        {"codigo_oficial": "1", "nombre": "X", "familia": "inexistente"}
    ]
    with pytest.raises(ValidationError, match="familia desconocida"):
        SCHEMAS["partidos.yaml"].model_validate(raw)


def test_elecciones_require_a_reserved_election() -> None:
    raw = _raw("elecciones.yaml")
    raw.pop("validacion_reservada", None)
    for e in raw["elecciones"]:
        e["uso"] = "calibrar"
    with pytest.raises(ValidationError, match="reservarse"):
        SCHEMAS["elecciones.yaml"].model_validate(raw)


def test_variables_reject_categorical_without_domain() -> None:
    raw = _raw("variables.yaml")
    del raw["variables"]["sexo"]["categorias"]
    with pytest.raises(ValidationError):
        SCHEMAS["variables.yaml"].model_validate(raw)


def test_variables_reject_recode_out_of_domain() -> None:
    raw = _raw("variables.yaml")
    raw["variables"]["sexo"]["fuentes"] = {
        "censo": {"variable_original": "SEXO", "recodificacion": {"1": "hombre", "6": "otro"}}
    }
    with pytest.raises(ValidationError, match="fuera de dominio"):
        SCHEMAS["variables.yaml"].model_validate(raw)


def test_variables_accept_special_codes_in_recode() -> None:
    raw = _raw("variables.yaml")
    raw["variables"]["sexo"]["fuentes"] = {
        "censo": {"variable_original": "SEXO", "recodificacion": {"1": "hombre", "9": "NC"}}
    }
    SCHEMAS["variables.yaml"].model_validate(raw)


def test_llm_model_after_cutoff_is_rejected() -> None:
    raw = _raw("llm.yaml")
    raw["modelos"] = [
        {
            "id": "m",
            "proveedor": "p",
            "fecha_corte_conocimiento": "2026-09-01",
            "uso": ["traduccion"],
        }
    ]
    with pytest.raises(ValidationError, match="fecha de corte"):
        SCHEMAS["llm.yaml"].model_validate(raw)


def test_territories_structure() -> None:
    t = load_config("territories.yaml")
    assert len(t.ccaa) == 19
    assert len(t.provincias) == 52
    por_ccaa = Counter(p.ccaa for p in t.provincias)
    esperado = {
        "01": 8,
        "02": 3,
        "03": 1,
        "04": 1,
        "05": 2,
        "06": 1,
        "07": 9,
        "08": 5,
        "09": 4,
        "10": 3,
        "11": 2,
        "12": 4,
        "13": 1,
        "14": 1,
        "15": 1,
        "16": 3,
        "17": 1,
        "18": 1,
        "19": 1,
    }
    assert dict(por_ccaa) == esperado


def test_territory_codes_match_variable_domains() -> None:
    t = load_config("territories.yaml")
    v = load_config("variables.yaml")
    assert [c.codigo for c in t.ccaa] == v.variables["ccaa"].categorias
    assert sorted(p.codigo for p in t.provincias) == v.variables["provincia"].categorias


def test_watchlist_initial_groups_present() -> None:
    w = load_config("watchlist.yaml")
    ids = {g.id for g in w.grupos}
    for g in (
        "mayores_85",
        "mayores_solos",
        "ceuta_melilla",
        "abstencion_generales",
        "sin_ubicacion_ideologica",
        "monoparentales",
    ):
        assert g in ids


def test_thresholds_match_documentation() -> None:
    th = load_config("thresholds.yaml")
    assert th.v_marg.factor_tvd_ref == 1.2 and th.v_marg.tolerancia == 0.002
    assert (th.v_cruce.espana, th.v_cruce.ccaa, th.v_cruce.provincia) == (0.03, 0.05, 0.08)
    assert th.v_pesos.rango_factor == (0.2, 5.0)
    assert th.v_minorias.ratio == (0.9, 1.1)
    assert th.v_concentracion.top5_max == 0.20


def test_volatile_variables_not_in_dictionary() -> None:
    v = load_config("variables.yaml")
    assert "intencion_voto" not in v.variables
    assert "valoracion_lideres" not in v.variables
