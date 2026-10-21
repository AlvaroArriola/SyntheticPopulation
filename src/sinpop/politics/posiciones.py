"""Posición ideológica del partido votado (F8B, `rasgo_izquierda_derecha`) (D-067).

`02_datos_y_variables.md` §3.5 estima el eje izquierda-derecha «con autoubicación, recuerdo de
voto y actitudes». El recuerdo entra en el factorial como un ítem numérico: la **autoubicación
media (1-10) del electorado de esa familia en el CIS** (ponderada, todos los estudios con
recuerdo de las generales de 2023 y escala ideológica). La familia nacionalista y regionalista
reúne partidos de izquierda y de derecha según la comunidad (EH Bildu y PNV, ERC y Junts, BNG,
CC, UPN), así que su posición se calcula por comunidad cuando hay al menos `MIN_ENCUESTADOS`.
Blanco, nulo, otros y abstención no tienen posición de partido (ítem ausente).
"""

from __future__ import annotations

from functools import lru_cache

import polars as pl

FAMILIAS_CON_POSICION = [
    "izquierda_estatal",
    "socialdemocrata",
    "centro_derecha_estatal",
    "derecha_radical",
    "nacionalista_regionalista",
]
POR_COMUNIDAD = "nacionalista_regionalista"
MIN_ENCUESTADOS = 30


@lru_cache(maxsize=1)
def tabla() -> pl.DataFrame:
    """familia, ccaa (nulo = todas) y posición media 1-10."""
    from sinpop.politics import ideologia as I

    d = (
        I.datos()
        .filter(
            pl.col("recuerdo").is_in(FAMILIAS_CON_POSICION)
            & ~pl.col("ideologia").is_in(["NS", "NC"])
        )
        .with_columns(pl.col("ideologia").cast(pl.Float64))
    )

    def media(g: pl.DataFrame, claves: list[str]) -> pl.DataFrame:
        return (
            g.group_by(claves)
            .agg(
                ((pl.col("ideologia") * pl.col("peso")).sum() / pl.col("peso").sum()).alias(
                    "posicion"
                ),
                pl.len().alias("n"),
            )
            .sort(claves)
        )

    nacional = media(d, ["recuerdo"]).with_columns(pl.lit(None, pl.Utf8).alias("ccaa"))
    ccaa = media(d.filter(pl.col("recuerdo") == POR_COMUNIDAD), ["recuerdo", "ccaa"]).filter(
        pl.col("n") >= MIN_ENCUESTADOS
    )
    return pl.concat([nacional.select(ccaa.columns), ccaa]).rename({"recuerdo": "familia"})


def posicion(familia: pl.Series, ccaa: pl.Series) -> pl.Series:
    """Posición del partido votado para cada (familia, comunidad); nula sin posición."""
    t = tabla()
    nac = dict(t.filter(pl.col("ccaa").is_null()).select("familia", "posicion").iter_rows())
    reg = {
        (f, c): p
        for f, c, p in t.filter(pl.col("ccaa").is_not_null())
        .select("familia", "ccaa", "posicion")
        .iter_rows()
    }
    return pl.Series(
        "posicion_partido_votado",
        [reg.get((f, c), nac.get(f)) for f, c in zip(familia, ccaa, strict=True)],
        dtype=pl.Float64,
    )
