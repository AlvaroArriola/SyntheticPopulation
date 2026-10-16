"""Agrupaciones de edad de las tablas oficiales (configs/targets.yaml, `agrupaciones_edad`).

Cada agrupación se define por sus límites inferiores. Por debajo del primero hay un grupo
«00-(min-1)», donde la variable de la tabla no procede (NP); el último grupo es «N+».
La misma función etiqueta las edades de los objetivos (F3) y las de los donantes (F4).
"""

from __future__ import annotations

import polars as pl


def etiquetas(cortes: list[int]) -> list[str]:
    """Etiquetas en orden: ['00-14', '15-19', …, '90+'] para cortes [15, 20, …, 90]."""
    out = [f"00-{cortes[0] - 1:02d}"] if cortes[0] > 0 else []
    out += [f"{a:02d}-{b - 1:02d}" for a, b in zip(cortes, cortes[1:], strict=False)]
    return [*out, f"{cortes[-1]}+"]


def agrupar(edad: pl.Expr, cortes: list[int], nombre: str) -> pl.Expr:
    """Etiqueta de grupo de cada edad (entera, años cumplidos)."""
    labs = etiquetas(cortes)
    expr = pl.lit(labs[-1])
    for corte, lab in zip(reversed(cortes), reversed(labs[:-1]), strict=True):
        expr = pl.when(edad < corte).then(pl.lit(lab)).otherwise(expr)
    return expr.alias(nombre)


def cortes() -> dict[str, list[int]]:
    from sinpop.config import load_config

    return dict(load_config("targets.yaml").agrupaciones_edad)  # type: ignore[attr-defined]
