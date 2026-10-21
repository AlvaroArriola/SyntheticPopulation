"""Objetivos electorales por territorio (F3, tarea 5; G3.6; D-036).

Generales del 23/07/2023: hojas municipales del Ministerio del Interior (escrutinio provisional,
solo residentes en España, sin CERA; D-029), que es el universo de la población sintética.
Opciones: las seis familias de `partidos.yaml`, blanco, nulo y abstención, sobre el censo
electoral de residentes (suman el 100 %). El detalle municipal se reserva para validar (D-022).

Autonómicas: resultados oficiales por circunscripción (D-023, D-031, D-032), con la familia de
cada candidatura (`tools/familias_autonomicas.py`). La abstención es electores − (válidos +
nulos): votantes = válidos + nulos por definición (en Castilla y León no se publican los
votantes). En Aragón no se publican los electores: su objetivo se da sobre los votantes, sin
abstención, y se indica en `metodo`.
"""

from __future__ import annotations

import polars as pl

from sinpop import INTERIM_DIR
from sinpop.config import load_config

ESPECIALES = ("blanco", "nulo", "abstencion")


def familias_generales() -> dict[str, str]:
    cfg = load_config("partidos.yaml")
    return {c.codigo_oficial: c.familia for c in cfg.elecciones["generales-2023"].candidaturas}  # type: ignore[attr-defined]


def generales_municipios() -> tuple[pl.DataFrame, pl.DataFrame]:
    """(opciones por municipio, votos por municipio y candidatura).

    Opciones: municipio, provincia, opcion (familia | blanco | nulo | abstencion), valor.
    """
    res = pl.read_parquet(INTERIM_DIR / "elecciones_generales_2023_municipios.parquet")
    vot = pl.read_parquet(INTERIM_DIR / "elecciones_generales_2023_votos.parquet")
    fam = familias_generales()
    sin = set(vot["candidatura"].unique().to_list()) - set(fam)
    if sin:
        raise ValueError(f"candidaturas sin familia en partidos.yaml: {sorted(sin)}")
    f = (
        vot.with_columns(pl.col("candidatura").replace_strict(fam).alias("opcion"))
        .group_by("municipio", "provincia", "opcion")
        .agg(pl.col("votos").sum().alias("valor"))
    )
    esp = res.select(
        "municipio",
        "provincia",
        pl.struct(
            blanco=pl.col("blancos"), nulo=pl.col("nulos"), abstencion=pl.col("abstencion")
        ).alias("s"),
    ).unnest("s")
    esp = esp.unpivot(index=["municipio", "provincia"], variable_name="opcion", value_name="valor")
    opciones = pl.concat(
        [f, esp.with_columns(pl.col("valor").cast(pl.Int64))], how="vertical_relaxed"
    )
    return opciones.with_columns(pl.col("valor").cast(pl.Float64)), vot


def comprobar_generales(opciones: pl.DataFrame) -> None:
    """Las opciones de cada municipio suman su censo de residentes (100 %)."""
    res = pl.read_parquet(INTERIM_DIR / "elecciones_generales_2023_municipios.parquet")
    s = opciones.group_by("municipio").agg(pl.col("valor").sum())
    j = s.join(res.select("municipio", "censo_residentes"), on="municipio")
    malos = j.filter(pl.col("valor") != pl.col("censo_residentes"))
    if malos.height:
        raise ValueError(f"{malos.height} municipios cuyas opciones no suman su censo")


UMBRAL_CERA = 0.9  # parte del censo CERA de 2023 que debe explicar el exceso de electores


def cera_autonomicas() -> pl.DataFrame:
    """Electores residentes en el extranjero (CERA) que se descuentan de cada circunscripción
    autonómica (D-067, reapertura de F3).

    Los boletines autonómicos dan el censo total, con el CERA, mientras que la población sintética
    y los objetivos de generales son de residentes (regla 2 de `docs/02`, §3.5). Sin descontarlo,
    la abstención de los residentes sale inflada (Galicia: 44 % frente a 33 %). El CERA de cada
    provincia es el de las generales de 2023: electores del BOE (con CERA) menos el censo de
    residentes de las hojas de Interior. Se descuenta en las comunidades cuyo censo autonómico
    supera al de residentes de 2023 en al menos el `UMBRAL_CERA` de ese CERA (el censo incluye
    el CERA); en Andalucía (2026) el exceso es el 41 %, explicable por el crecimiento del censo de
    residentes, y no se descuenta. Dentro de una provincia con varias islas, se reparte en
    proporción a los electores. Los votos del CERA (en torno al 1-5 % de su censo) no se publican
    aparte y quedan dentro de los votos: la abstención de residentes queda algo por debajo de la
    real.
    """
    res = pl.read_parquet(INTERIM_DIR / "elecciones_autonomicas_circunscripciones.parquet").filter(
        (pl.col("circunscripcion") != "05-AUT") & pl.col("electores").is_not_null()
    )
    residentes = (
        pl.read_parquet(INTERIM_DIR / "elecciones_generales_2023_municipios.parquet")
        .group_by("provincia")
        .agg(pl.col("censo_residentes").sum().alias("residentes"))
    )
    boe = pl.read_parquet(INTERIM_DIR / "elecciones_generales_2023_provincias.parquet").select(
        "provincia", pl.col("electores").alias("boe")
    )
    cera = residentes.join(boe, on="provincia").with_columns(
        (pl.col("boe") - pl.col("residentes")).alias("cera")
    )
    c = res.with_columns(pl.col("circunscripcion").str.slice(0, 2).alias("provincia")).join(
        cera, on="provincia"
    )
    por_ccaa = (
        c.group_by("ccaa")
        .agg(
            pl.col("electores").sum(),
            pl.col("residentes").unique().sum(),
            pl.col("cera").unique().sum(),
        )
        .with_columns(
            ((pl.col("electores") - pl.col("residentes")) / pl.col("cera")).alias("fraccion")
        )
    )
    incluye = por_ccaa.filter(pl.col("fraccion") >= UMBRAL_CERA)["ccaa"].to_list()
    return c.with_columns(
        pl.when(pl.col("ccaa").is_in(incluye))
        .then(pl.col("cera") * pl.col("electores") / pl.col("electores").sum().over("provincia"))
        .otherwise(0.0)
        .alias("cera_descontado")
    ).select("ccaa", "circunscripcion", "cera_descontado")


def autonomicas_circunscripciones() -> pl.DataFrame:
    """Opciones por circunscripción autonómica: ccaa, circunscripcion, provincia, opcion, valor.

    Canarias: se usan las 7 islas (la circunscripción autonómica «05-AUT» es una segunda papeleta
    de los mismos electores y no se suma).
    """
    import importlib.util

    from sinpop import REPO_ROOT

    spec = importlib.util.spec_from_file_location(
        "familias_autonomicas", REPO_ROOT / "tools/familias_autonomicas.py"
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    fam = {k: v[0] for k, v in mod.FAMILIAS_AUTONOMICAS.items()}
    res = pl.read_parquet(INTERIM_DIR / "elecciones_autonomicas_circunscripciones.parquet")
    vot = pl.read_parquet(INTERIM_DIR / "elecciones_autonomicas_votos.parquet")
    res = res.filter(pl.col("circunscripcion") != "05-AUT")
    vot = vot.filter(pl.col("circunscripcion") != "05-AUT")
    claves = [(c, n) for c, n in vot.select("ccaa", "candidatura").unique().iter_rows()]
    sin = [k for k in claves if k not in fam]
    if sin:
        raise ValueError(f"candidaturas autonómicas sin familia: {sin[:10]}")
    v = (
        vot.with_columns(
            pl.struct("ccaa", "candidatura")
            .map_elements(lambda r: fam[(r["ccaa"], r["candidatura"])], return_dtype=pl.Utf8)
            .alias("opcion")
        )
        .group_by("ccaa", "circunscripcion", "opcion")
        .agg(pl.col("votos").sum().cast(pl.Float64).alias("valor"))
    )
    res = res.join(cera_autonomicas(), on=["ccaa", "circunscripcion"], how="left")
    esp = res.select(
        "ccaa",
        "circunscripcion",
        pl.col("blancos").cast(pl.Float64).alias("blanco"),
        pl.col("nulos").cast(pl.Float64).alias("nulo"),
        (
            pl.col("electores").cast(pl.Float64)
            - pl.col("cera_descontado").fill_null(0.0)
            - pl.col("validos")
            - pl.col("nulos")
        ).alias("abstencion"),
    ).unpivot(index=["ccaa", "circunscripcion"], variable_name="opcion", value_name="valor")
    esp = esp.filter(pl.col("valor").is_not_null())
    out = pl.concat([v, esp])
    return out.with_columns(pl.col("circunscripcion").str.slice(0, 2).alias("provincia"))


def generales_candidaturas(opciones: pl.DataFrame, votos: pl.DataFrame) -> pl.DataFrame:
    """Votos por candidatura (siglas de Interior) más blanco, nulo y abstención, por municipio:
    suma el censo de residentes, como las familias."""
    esp = opciones.filter(pl.col("opcion").is_in(list(ESPECIALES))).rename(
        {"opcion": "candidatura_generales_2023"}
    )
    cand = votos.select(
        "municipio",
        "provincia",
        pl.col("candidatura").alias("candidatura_generales_2023"),
        pl.col("votos").cast(pl.Float64).alias("valor"),
    )
    return pl.concat([cand, esp.select(cand.columns)])
