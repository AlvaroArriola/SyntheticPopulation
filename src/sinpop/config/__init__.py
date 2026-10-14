"""Carga y validación de las configuraciones de `configs/`."""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel

from sinpop import CONFIGS_DIR
from sinpop.config.schemas import SCHEMAS


def load_yaml(path: Path) -> object:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_config(name: str, configs_dir: Path = CONFIGS_DIR) -> BaseModel:
    """Carga `configs/<name>` y lo valida contra su esquema."""
    if name not in SCHEMAS:
        raise KeyError(f"no hay esquema para {name!r}")
    return SCHEMAS[name].model_validate(load_yaml(configs_dir / name))


def validate_all(configs_dir: Path = CONFIGS_DIR) -> dict[str, str | None]:
    """Valida todas las configuraciones. Devuelve {fichero: None si es válido, o el error}."""
    out: dict[str, str | None] = {}
    for name in SCHEMAS:
        try:
            load_config(name, configs_dir)
            out[name] = None
        except Exception as exc:  # noqa: BLE001 - se informa cualquier error
            out[name] = f"{type(exc).__name__}: {exc}"
    return out
