"""Marco de población para predecir (F9) (D-069).

Una muestra fija (semilla) de `TAMANO` adultos de la población sintética nacional, con lo que
usan los modelos: perfil (F4-F6), valores (F8A: religiosidad, clase subjetiva), grupo de voto de
2023 con NS/NC (F8B) y autoubicación en bloques (F8B), más las columnas de los subgrupos de
salida.

Pesos: `peso` (todos los adultos), `peso_es` (españoles, el universo del CIS) y `peso_cis`
(españoles reponderados para que su recuerdo de voto de 2023 tenga la composición que tiene en las
muestras del CIS de los 12 meses anteriores al corte: más voto al PSOE y menos abstención que el
resultado oficial, D-068). `peso_cis` predice lo que **mediría el CIS**, que es con lo que se
valida; `peso`, lo que piensa la población.

Con 100.000 personas el error de muestreo de una proporción es ≤ 0,3 puntos, muy por
debajo del error del modelo, y la predicción tarda segundos en vez de minutos.
"""

from __future__ import annotations

from functools import cache

import polars as pl

from sinpop import POPULATIONS_DIR
from sinpop.opinion.valores import perfil_sintetico
from sinpop.politics.rasgos_politicos import bloque_cis
from sinpop.temporal.indicadores import _edad4, grupo_voto

NACIONAL = "2026-01-01_ES_1000000_s1"
TAMANO = 100_000
SEMILLA = 20260630


@cache
def marco(run_id: str = NACIONAL) -> pl.DataFrame:
    d = POPULATIONS_DIR / run_id
    persons = pl.read_parquet(d / "persons.parquet")
    op = pl.read_parquet(
        d / "opinion.parquet", columns=["person_id", "religiosidad", "clase_subjetiva"]
    )
    pol = pl.read_parquet(
        d / "politics.parquet",
        columns=[
            "person_id",
            "recuerdo_voto_generales",
            "recuerdo_voto_generales_ns_nc",
            "ideologia_autoubicacion",
        ],
    )
    m = (
        perfil_sintetico(persons)
        .join(persons.select("person_id", "peso"), on="person_id")
        .join(op, on="person_id")
        .join(pol, on="person_id")
        .sort("person_id")
    )
    m = m.sample(min(TAMANO, m.height), seed=SEMILLA).sort("person_id")
    m = m.with_columns(
        _edad4(pl.col("edad")),
        grupo_voto(pl.col("recuerdo_voto_generales"), pl.col("recuerdo_voto_generales_ns_nc")),
        bloque_cis(pl.col("ideologia_autoubicacion")).alias("ideologia_bloque"),
        pl.col("recuerdo_voto_generales").alias("recuerdo_voto_generales_familia"),
        (pl.col("peso") / pl.col("peso").mean()).alias("peso"),
    )
    es = m["nacionalidad_esp_ext"] == "espanola"
    m = m.with_columns(pl.when(es).then(pl.col("peso")).otherwise(0.0).alias("peso_es"))
    obj = composicion_cis()
    actual = (
        m.filter(es)
        .group_by("grupo_voto")
        .agg(pl.col("peso_es").sum())
        .with_columns(pl.col("peso_es") / pl.col("peso_es").sum())
    )
    razon = {g: obj.get(g, 0.0) / a for g, a in actual.iter_rows() if a > 0}
    return m.with_columns(
        (pl.col("peso_es") * pl.col("grupo_voto").replace_strict(razon, default=0.0)).alias(
            "peso_cis"
        )
    )


@cache
def composicion_cis() -> dict[str, float]:
    """Reparto del grupo de voto de 2023 entre los encuestados españoles de 18+ de los estudios
    nacionales del CIS de los 12 meses anteriores al corte (ponderado)."""
    import datetime as dt

    from sinpop import INTERIM_DIR
    from sinpop.opinion.cis import CORTE
    from sinpop.politics import recuerdo as RV
    from sinpop.temporal.indicadores import estudios_temporales

    desde = dt.date(CORTE.year - 1, CORTE.month, 1).isoformat()
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet").filter(
        pl.col("estudio").is_in(estudios_temporales())
        & (pl.col("fecha") >= desde)
        & (pl.col("edad") >= 18)
        & (
            pl.col("nacionalidad_esp_ext").is_null()
            | (pl.col("nacionalidad_esp_ext") == "espanola")
        )
    )
    d = p.join(RV.respuestas(), on=["estudio", "encuestado"]).with_columns(
        grupo_voto(pl.col("recuerdo")),
        (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
    )
    t = (
        d.filter(pl.col("grupo_voto").is_not_null())
        .group_by("grupo_voto")
        .agg(pl.col("peso").sum())
    )
    tot = t["peso"].sum()
    return {g: w / tot for g, w in t.iter_rows()}
