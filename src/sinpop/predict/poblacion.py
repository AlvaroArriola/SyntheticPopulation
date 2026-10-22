"""Marco de población para predecir (F9) (D-069).

Una muestra fija (semilla) de `TAMANO` adultos de la población sintética nacional, con lo que
usan los modelos: perfil (F4-F6), valores (F8A: religiosidad, clase subjetiva), grupo de voto de
2023 con NS/NC (F8B) y autoubicación en bloques (F8B), más las columnas de los subgrupos de
salida.

Pesos: `peso` (todos los adultos), `peso_es` (españoles, el universo del CIS) y `peso_cis`
(españoles ajustados por *raking* a la composición de las muestras del CIS de los 12 meses
anteriores al corte en recuerdo de voto de 2023 —más voto al PSOE y menos abstención que el
resultado oficial, D-068—, edad × sexo, estudios y comunidad). `peso_cis` predice lo que
**mediría el CIS**, que es con lo que se valida; `peso`, lo que piensa la población.

Con 100.000 personas el error de muestreo de una proporción es ≤ 0,3 puntos, muy por
debajo del error del modelo, y la predicción tarda segundos en vez de minutos.
"""

from __future__ import annotations

from functools import cache

import numpy as np
import polars as pl

from sinpop import POPULATIONS_DIR
from sinpop.opinion.valores import perfil_sintetico
from sinpop.politics.rasgos_politicos import bloque_cis
from sinpop.temporal.indicadores import _edad4, grupo_voto

NACIONAL = "2026-01-01_ES_1000000_s1"
TAMANO = 100_000
SEMILLA = 20260630


def territorio(run_id: str) -> str:
    """Código del territorio de una población (`ES`, `CCAA:XX`, `PROV:XX`)."""
    import json

    meta = json.loads((POPULATIONS_DIR / run_id / "metadata.json").read_text("utf-8"))
    t = meta.get("territorio")
    return t["codigo"] if isinstance(t, dict) else str(t or "ES")


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
        .join(persons.select("person_id", "peso", "provincia"), on="person_id")
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
    m = m.with_columns(
        pl.when(es).then(pl.col("peso")).otherwise(0.0).alias("peso_es"),
        (pl.col("edad_4") + "|" + pl.col("sexo")).alias("_edad_sexo"),
    )
    t = territorio(run_id)
    if t == "ES":
        w = rastrillo(m, "peso_es")
    else:  # D-075: composición de los encuestados del CIS de ese territorio, sin la comunidad
        w = rastrillo(m, "peso_es", composicion_cis(t), [k for k in DIMENSIONES_CIS if k != "ccaa"])
    return m.with_columns(pl.Series("peso_cis", w)).drop("_edad_sexo")


DIMENSIONES_CIS = {
    "grupo_voto": "grupo_voto",
    "_edad_sexo": "_edad_sexo",
    "estudios_3": "estudios_3",
    "ccaa": "ccaa",
}


def rastrillo(
    m: pl.DataFrame,
    peso: str,
    obj: dict | None = None,
    dimensiones: list[str] | None = None,
    iteraciones: int = 30,
) -> np.ndarray:
    """Raking del peso de los españoles a la composición de las muestras del CIS en grupo de voto,
    edad × sexo, estudios y comunidad (`composicion_cis`)."""
    w = m[peso].to_numpy().copy()
    obj = composicion_cis() if obj is None else obj
    dims = list(DIMENSIONES_CIS) if dimensiones is None else dimensiones
    cols = {d: m[DIMENSIONES_CIS[d]].cast(pl.Utf8).to_numpy() for d in dims}
    for _ in range(iteraciones):
        for d, col in cols.items():
            tot = w.sum()
            for lv, p in obj[d].items():
                s = col == lv
                a = w[s].sum()
                if a > 0:
                    w[s] *= p * tot / a
    return w


@cache
def composicion_cis(territorio: str = "ES") -> dict[str, dict[str, float]]:
    """Composición de los encuestados españoles de 18+ de los estudios nacionales del CIS de los
    12 meses anteriores al corte (ponderada): grupo de voto de 2023, edad × sexo, estudios y
    comunidad. Con un territorio (`CCAA:XX`, `PROV:XX`), solo sus encuestados."""
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
    if territorio != "ES":
        nivel, cod = territorio.split(":")
        p = p.filter(pl.col("ccaa" if nivel == "CCAA" else "provincia") == cod)
    d = p.join(RV.respuestas(), on=["estudio", "encuestado"]).with_columns(
        grupo_voto(pl.col("recuerdo")),
        (_edad4(pl.col("edad")) + "|" + pl.col("sexo")).alias("_edad_sexo"),
        (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
    )
    out = {}
    for dim in DIMENSIONES_CIS:
        t = d.filter(pl.col(dim).is_not_null()).group_by(dim).agg(pl.col("peso").sum())
        tot = t["peso"].sum()
        out[dim] = {g: w / tot for g, w in t.iter_rows()}
    return out
