"""Separación de capas (regla 9 de CLAUDE.md, decisión D-005).

Ninguna variable de opinión (P3) ni política (P3-POL) puede aparecer en
`persons.parquet` ni en `households.parquet`. Tampoco las variables volátiles que,
por D-005, nunca son atributos de la persona.
"""

from __future__ import annotations

from collections.abc import Iterable

from sinpop.config import load_config
from sinpop.config.schemas import VariablesConfig

# Volátiles: se predicen como preguntas, nunca se guardan como atributo (D-005).
VOLATILES = frozenset({"intencion_voto", "valoracion_lideres"})


def forbidden_base_columns(variables: VariablesConfig | None = None) -> set[str]:
    if variables is None:
        variables = load_config("variables.yaml")  # type: ignore[assignment]
    assert isinstance(variables, VariablesConfig)
    return variables.por_capa("P3", "P3-POL") | set(VOLATILES)


def layer_violations(columns: Iterable[str], variables: VariablesConfig | None = None) -> list[str]:
    """Columnas de la población base que pertenecen a las capas de opinión o política.

    También detecta columnas derivadas (`<variable>__calidad`, `<variable>_familia`…).
    """
    prohibidas = forbidden_base_columns(variables)
    out = []
    for c in columns:
        base = c.split("__", 1)[0]
        if base in prohibidas or any(base.startswith(p + "_") for p in prohibidas):
            out.append(c)
    return sorted(out)
