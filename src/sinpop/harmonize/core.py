"""Utilidades comunes de armonización (F2).

Las tablas de recodificación viven solo en `configs/variables.yaml`
(`variables.<var>.fuentes.<fuente>.recodificacion`). Aquí se aplican y se comprueba que:

- ningún código queda sin traducir (un código no documentado detiene el proceso);
- los valores fuera del universo (vacíos) pasan a `NP` solo cuando la regla de universo lo
  justifica, y si no se marcan como error;
- el resultado está dentro del dominio declarado (más NS, NC, NP).
"""

from __future__ import annotations

from collections.abc import Iterable

import polars as pl

from sinpop.config import load_config
from sinpop.config.schemas import ESPECIALES, VariablesConfig


class CodigoNoDocumentado(ValueError):
    """Un valor del fichero no aparece en la tabla de recodificación (regla 2 de CLAUDE.md)."""


_VARS: VariablesConfig | None = None


def variables() -> VariablesConfig:
    global _VARS
    if _VARS is None:
        _VARS = load_config("variables.yaml")  # type: ignore[assignment]
    return _VARS


def tabla(var: str, fuente: str) -> dict[str, str]:
    f = variables().variables[var].fuentes.get(fuente)
    if f is None or not f.recodificacion:
        raise KeyError(f"no hay recodificación de {var} para {fuente}")
    return dict(f.recodificacion)


def dominio(var: str) -> set[str]:
    v = variables().variables[var]
    return set(v.categorias or []) | set(ESPECIALES)


def recode(
    df: pl.DataFrame,
    columna: str,
    var: str,
    fuente: str,
    *,
    np_si: pl.Expr | None = None,
    nc_si: pl.Expr | None = None,
    otros: dict[str, str] | None = None,
) -> pl.Series:
    """Recodifica `columna` a la variable armonizada `var`.

    - `np_si`: condición (expresión booleana) bajo la cual un valor vacío es «no procede».
    - `nc_si`: condición bajo la cual un valor vacío dentro del universo es «no consta»
      (casos no documentados registrados en DECISIONS.md).
    - `otros`: códigos adicionales resueltos fuera de la tabla (p. ej. municipios ≥10.000
      clasificados por su población), ya armonizados.
    Lanza `CodigoNoDocumentado` si queda algún valor sin traducir.
    """
    mapa = tabla(var, fuente) | (otros or {})
    s = df[columna].cast(pl.Utf8).fill_null("").str.strip_chars()
    out = s.replace_strict(mapa, default=None, return_dtype=pl.Utf8)
    vacio = s == ""
    if np_si is not None:
        cond = df.select(np_si.alias("_c"))["_c"]
        out = pl.select(pl.when(vacio & cond).then(pl.lit("NP")).otherwise(out)).to_series()
    if nc_si is not None:
        cond = df.select(nc_si.alias("_c"))["_c"]
        out = pl.select(pl.when(vacio & cond).then(pl.lit("NC")).otherwise(out)).to_series()
    sin = df.filter(out.is_null())[columna].cast(pl.Utf8).fill_null("").unique().to_list()
    if sin:
        raise CodigoNoDocumentado(
            f"{fuente}.{columna} → {var}: valores sin traducir {sorted(sin)[:20]}"
        )
    fuera = set(out.unique().to_list()) - dominio(var)
    if fuera:
        raise ValueError(f"{var}: valores fuera de dominio {sorted(fuera)}")
    return out.alias(var)


def edad_5(edad: pl.Expr) -> pl.Expr:
    cats = variables().variables["edad_5"].categorias or []
    expr = pl.lit(cats[-1])
    for c in reversed(cats[:-1]):
        hi = int(c.split("-")[1])
        expr = pl.when(edad <= hi).then(pl.lit(c)).otherwise(expr)
    return expr.alias("edad_5")


def edad_4(edad: pl.Expr) -> pl.Expr:
    return (
        pl.when(edad < 18)
        .then(pl.lit("NP"))
        .when(edad <= 34)
        .then(pl.lit("18-34"))
        .when(edad <= 49)
        .then(pl.lit("35-49"))
        .when(edad <= 64)
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
        .alias("edad_4")
    )


def ccaa_de_provincia() -> dict[str, str]:
    t = load_config("territories.yaml")
    return {p.codigo: p.ccaa for p in t.provincias}  # type: ignore[attr-defined]


def tamano_por_poblacion(poblacion: int) -> str:
    if poblacion <= 2000:
        return "hasta_2000"
    if poblacion <= 10000:
        return "de_2001_a_10000"
    if poblacion <= 50000:
        return "de_10001_a_50000"
    if poblacion <= 100000:
        return "de_50001_a_100000"
    if poblacion <= 500000:
        return "de_100001_a_500000"
    return "mas_de_500000"


def comprobar_dominio(df: pl.DataFrame, columnas: Iterable[str]) -> dict[str, list[str]]:
    """Valores fuera de dominio por columna armonizada (para G2.1)."""
    out = {}
    for c in columnas:
        v = variables().variables.get(c)
        if v is None or not v.categorias:
            continue
        fuera = sorted(set(df[c].drop_nulls().unique().to_list()) - dominio(c))
        if fuera:
            out[c] = fuera
    return out
