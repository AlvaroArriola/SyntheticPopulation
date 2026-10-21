"""Indicadores mensuales de los barómetros del CIS (F8C; docs/03 §2.6) (D-068).

Cada indicador de `configs/temporal.yaml` se lee por la **etiqueta** de la respuesta:

- categorías: cada etiqueta va a una categoría; una etiqueta no prevista detiene el proceso;
- menciones (principales problemas, hasta tres respuestas): 1 si alguna de las respuestas es una
  de las etiquetas, 0 si no (también «N.S.», «Ninguno»: no mencionan el problema);
- `ideologia`: los bloques de la autoubicación de D-067; `cercania`: las familias de D-067.

Los encuestados son los de los estudios nacionales del CIS (`estudios_temporales`: los de
`valores.estudios_nacionales` más los barómetros mensuales con módulo postelectoral, 3410 y
3420, que son la muestra nacional de su mes), españoles de 18 y más años, con el mes de campo
del estudio y el peso normalizado por estudio. El grupo de voto es el recuerdo de las generales
de 2023, solo conocido desde agosto de 2023 (antes, «desconocido»).
"""

from __future__ import annotations

from functools import cache, lru_cache

import polars as pl
import yaml

from sinpop import CONFIGS_DIR, INTERIM_DIR
from sinpop.opinion.cis import CORTE
from sinpop.opinion.valores import _edad_grupo, estudios_nacionales
from sinpop.politics import recuerdo as RV
from sinpop.politics.ess_donantes import GRUPO

DESCONOCIDO = "desconocido"


@lru_cache(maxsize=1)
def estudios_temporales() -> list[str]:
    import json

    from sinpop.opinion.cis import SELECCION

    titulos = {e["estudio"]: e["titulo"] for e in json.loads(SELECCION.read_text("utf-8"))}
    varias = (
        pl.read_parquet(INTERIM_DIR / "cis_personas.parquet", columns=["estudio", "ccaa"])
        .group_by("estudio")
        .agg(pl.col("ccaa").n_unique())
        .filter(pl.col("ccaa") > 1)["estudio"]
        .to_list()
    )
    barometros = [e for e in varias if titulos.get(e, "").lower().startswith("barometro")]
    return sorted(set(estudios_nacionales()) | set(barometros))


@lru_cache(maxsize=1)
def config() -> dict:
    return yaml.safe_load((CONFIGS_DIR / "temporal.yaml").read_text("utf-8"))


def indicadores() -> list[str]:
    return list(config()["indicadores"])


def meses() -> list[str]:
    """Meses del periodo (AAAA-MM), en orden."""
    p = config()["periodo"]
    a, m = map(int, p["desde"].split("-"))
    b, n = map(int, p["hasta"].split("-"))
    out = []
    while (a, m) <= (b, n):
        out.append(f"{a:04d}-{m:02d}")
        a, m = (a + 1, 1) if m == 12 else (a, m + 1)
    return out


def _largo(variables: list[str]) -> pl.DataFrame:
    return (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter(pl.col("variable").is_in(variables))
        .select("estudio", "encuestado", "variable", "codigo", "etiqueta")
        .collect()
    )


def respuestas(indicador: str) -> pl.DataFrame:
    """(estudio, encuestado, valor) del indicador."""
    c = config()["indicadores"][indicador]
    if c.get("especial") == "ideologia":
        from sinpop.politics.ideologia import respuestas as ideol
        from sinpop.politics.rasgos_politicos import bloque_cis

        return ideol().select(
            "estudio", "encuestado", bloque_cis(pl.col("ideologia")).alias("valor")
        )
    if c.get("especial") == "cercania":
        from sinpop.politics.cercania import mapa

        lg = _largo(c["variables"]).with_columns(pl.col("etiqueta").str.strip_chars())
        m = mapa()
        sin = sorted(set(lg["etiqueta"].drop_nulls().unique()) - set(m))
        if sin:
            raise ValueError(f"{indicador}: etiquetas sin familia en partidos.yaml: {sin}")
        return lg.select(
            "estudio",
            "encuestado",
            pl.col("etiqueta")
            .replace_strict(m, default=None)
            .replace({"NS": "NS_NC", "NC": "NS_NC"})
            .alias("valor"),
        ).drop_nulls()
    lg = _largo(c["variables"]).with_columns(pl.col("etiqueta").str.strip_chars())
    if "menciones" in c:
        return (
            lg.group_by("estudio", "encuestado")
            .agg(pl.col("etiqueta").is_in(c["menciones"]).any().alias("m"))
            .select(
                "estudio",
                "encuestado",
                pl.when(pl.col("m")).then(pl.lit("si")).otherwise(pl.lit("no")).alias("valor"),
            )
        )
    mapa = {et: cat for cat, ets in c["categorias"].items() for et in ets}
    sin = sorted(set(lg["etiqueta"].drop_nulls().unique()) - set(mapa))
    if sin:
        raise ValueError(f"{indicador}: etiquetas no previstas en temporal.yaml: {sin}")
    return lg.select(
        "estudio",
        "encuestado",
        pl.col("etiqueta").replace_strict(mapa, default=None).alias("valor"),
    ).drop_nulls()


def _edad4(e: pl.Expr) -> pl.Expr:
    return (
        pl.when(e < 35)
        .then(pl.lit("18-34"))
        .when(e < 50)
        .then(pl.lit("35-49"))
        .when(e < 65)
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
        .alias("edad_4")
    )


def grupo_voto(recuerdo: pl.Expr, ns_nc: pl.Expr | None = None) -> pl.Expr:
    """Grupos de voto de 2023 (`ess_donantes.GRUPO`) más NS_NC."""
    g = (
        pl.when(recuerdo.is_in(["NS", "NC"]))
        .then(pl.lit("NS_NC"))
        .otherwise(recuerdo.replace_strict(GRUPO, default=None))
    )
    if ns_nc is not None:
        g = pl.when(ns_nc).then(pl.lit("NS_NC")).otherwise(g)
    return g.alias("grupo_voto")


@cache
def datos(indicador: str) -> pl.DataFrame:
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    r = RV.respuestas().select("estudio", "encuestado", "recuerdo")
    d = (
        p.join(respuestas(indicador), on=["estudio", "encuestado"])
        .with_columns(pl.col("fecha").str.slice(0, 7).alias("mes"))
        .filter(
            pl.col("estudio").is_in(estudios_temporales())
            & pl.col("mes").is_in(meses())
            & (pl.col("fecha").str.to_date() < CORTE)
            & (pl.col("edad") >= 18)
            & (
                pl.col("nacionalidad_esp_ext").is_null()
                | (pl.col("nacionalidad_esp_ext") == "espanola")
            )
            & ~pl.col("estudios_3").is_in(["NC", "NS"])
            & ~pl.col("actividad_3").is_in(["NC", "NS"])
        )
        .join(r, on=["estudio", "encuestado"], how="left")
        .with_columns(
            _edad4(pl.col("edad")),
            _edad_grupo(pl.col("edad")),
            pl.when(pl.col("recuerdo").is_null())
            .then(pl.lit(DESCONOCIDO))
            .otherwise(grupo_voto(pl.col("recuerdo")))
            .alias("grupo_voto"),
            (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
        )
        .filter(pl.col("grupo_voto").is_not_null())
    )
    return d.sort("estudio", "encuestado")


def serie(indicador: str) -> pl.DataFrame:
    """Proporción ponderada observada por mes y categoría (la que publica el CIS)."""
    d = datos(indicador)
    return (
        d.group_by("mes", "valor")
        .agg(pl.col("peso").sum())
        .with_columns((pl.col("peso") / pl.col("peso").sum().over("mes")).alias("p"))
        .join(
            d.group_by("mes").agg(
                pl.len().alias("n"),
                (pl.col("peso").sum() ** 2 / (pl.col("peso") ** 2).sum()).alias("n_efectivo"),
            ),
            on="mes",
        )
        .sort("mes", "valor")
        .select("mes", "valor", "p", "n", "n_efectivo")
    )
