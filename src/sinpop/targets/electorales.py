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
    esp = res.select(
        "ccaa",
        "circunscripcion",
        pl.col("blancos").cast(pl.Float64).alias("blanco"),
        pl.col("nulos").cast(pl.Float64).alias("nulo"),
        (pl.col("electores") - pl.col("validos") - pl.col("nulos"))
        .cast(pl.Float64)
        .alias("abstencion"),
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
