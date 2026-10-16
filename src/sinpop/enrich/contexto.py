"""Variables de contexto y renta del Atlas (D-044.5 y D-044.6).

- Atlas de distribución de renta de los hogares 2023 (INE): renta neta media por persona y
  media de la renta por unidad de consumo, por municipio (tablas por provincia), provincia,
  comunidad y España (tabla 53689).
- Envejecimiento: proporción de 65+ del Censo Anual exhaustivo a 01/01/2025.

Los municipios que el Censo no identifica (menos de 10.000 habitantes) y las personas sin
municipio (colectivos, hogares trasladados) reciben la media de su provincia y clase de tamaño,
ponderada por población (`modelada`).
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.ingest.ine_tablas import leer

ATLAS = RAW_DIR / "atlas_renta/ultimo"
ANIO_ATLAS = "2023-01-01"
INDICADORES = {
    "Renta neta media por persona": "renta_neta_persona",
    "Media de la renta por unidad de consumo": "renta_uc_media",
}
TABLA_TERRITORIOS = "53689"


def _indicadores(path: Path) -> pl.DataFrame:
    t = leer(path)
    if "SALDOS CONTABLES" not in t.columns:  # tablas de otros indicadores del Atlas
        return pl.DataFrame()
    return t.filter(
        pl.col("SALDOS CONTABLES").is_in(list(INDICADORES)) & (pl.col("fecha") == ANIO_ATLAS)
    ).with_columns(pl.col("SALDOS CONTABLES").replace_strict(INDICADORES).alias("indicador"))


@lru_cache(maxsize=1)
def atlas_municipios() -> pl.DataFrame:
    """municipio, renta_neta_persona, renta_uc_media (2023)."""
    partes = []
    for f in sorted(ATLAS.glob("tabla_*_ultimo.json")):
        if TABLA_TERRITORIOS in f.name:
            continue
        t = _indicadores(f)
        if t.is_empty() or "Municipios" not in t.columns:
            continue
        partes.append(
            t.filter(pl.col("Municipios").is_not_null())
            .filter(
                pl.all_horizontal(
                    [pl.col(c).is_null() for c in ("Distritos", "Secciones") if c in t.columns]
                )
            )
            .select(pl.col("Municipios__cod").alias("municipio"), "indicador", "valor")
        )
    return (
        pl.concat(partes)
        .unique(["municipio", "indicador"], keep="first")
        .pivot(on="indicador", index="municipio", values="valor")
        .sort("municipio")
    )


@lru_cache(maxsize=1)
def atlas_territorios() -> pl.DataFrame:
    """nivel (espana, ccaa, provincia), codigo y los dos indicadores (2023)."""
    t = _indicadores(ATLAS / f"tabla_{TABLA_TERRITORIOS}_ultimo.json")
    if "Islas" in t.columns:
        t = t.filter(pl.col("Islas").is_null())
    niveles = (
        ("Provincias", "provincia"),
        ("Comunidades y Ciudades Autónomas", "ccaa"),
        ("Total Nacional", "espana"),
    )
    partes = []
    for col, nivel in niveles:
        x = t.filter(pl.col(col).is_not_null())
        for c, _ in niveles:
            if c != col:
                x = x.filter(pl.col(c).is_null())
        partes.append(
            x.select(
                pl.lit(nivel).alias("nivel"),
                pl.col(f"{col}__cod").alias("codigo"),
                "indicador",
                "valor",
            )
        )
    return (
        pl.concat(partes)
        .pivot(on="indicador", index=["nivel", "codigo"], values="valor")
        .sort("nivel", "codigo")
    )


@lru_cache(maxsize=1)
def renta_por_unidad() -> tuple[pl.DataFrame, pl.DataFrame]:
    """Renta neta media por persona por municipio y por provincia × clase de tamaño (media de
    los municipios con dato, ponderada por su población del Padrón 2025)."""
    from sinpop.targets.municipios import padron

    m = padron().join(atlas_municipios(), on="municipio", how="inner")
    clase = m.group_by("provincia", "tamano_municipio").agg(
        (
            (pl.col("renta_neta_persona") * pl.col("poblacion")).sum() / pl.col("poblacion").sum()
        ).alias("ctx_renta_municipio")
    )
    return m.select("municipio", pl.col("renta_neta_persona").alias("ctx_renta_municipio")), clase


@lru_cache(maxsize=1)
def envejecimiento_por_unidad() -> tuple[pl.DataFrame, pl.DataFrame]:
    """Proporción de 65+ por municipio identificado y por provincia × clase de tamaño (Censo
    Anual exhaustivo a 01/01/2025)."""
    c = pl.read_parquet(
        INTERIM_DIR / "censo_anual_exhaustivo_2025.parquet",
        columns=["edad", "provincia", "municipio", "tamano_municipio", "personas"],
    )
    p65 = (pl.col("personas").filter(pl.col("edad") >= 65).sum() / pl.col("personas").sum()).alias(
        "ctx_envejecimiento"
    )
    muni = c.filter(pl.col("municipio").is_not_null()).group_by("municipio").agg(p65)
    clase = c.group_by("provincia", "tamano_municipio").agg(p65)
    return muni, clase


def contexto(personas: pl.DataFrame) -> pl.DataFrame:
    """ctx_renta_municipio y ctx_envejecimiento (con su `__calidad`) para cada persona, en el
    mismo orden. Con municipio: el del municipio (`observada`; la calidad del municipio pasa si
    es `modelada`). Sin él o sin dato municipal: la media de su provincia y clase (`modelada`)."""
    out = personas.select(
        "municipio", "provincia", "tamano_municipio", "municipio__calidad"
    ).with_row_index("_i")
    for var, (muni, clase) in (
        ("ctx_renta_municipio", renta_por_unidad()),
        ("ctx_envejecimiento", envejecimiento_por_unidad()),
    ):
        # Último recurso: la media de la provincia (clase sin municipios en ella)
        prov = clase.group_by("provincia").agg(pl.col(var).mean().alias("_p"))
        out = (
            out.join(muni.rename({var: "_m"}), on="municipio", how="left")
            .join(clase.rename({var: "_c"}), on=["provincia", "tamano_municipio"], how="left")
            .join(prov, on="provincia", how="left")
            .with_columns(
                pl.coalesce("_m", "_c", "_p").alias(var),
                pl.when(pl.col("_m").is_not_null())
                .then(
                    pl.when(pl.col("municipio__calidad") == "modelada")
                    .then(pl.lit("modelada"))
                    .otherwise(pl.lit("observada"))
                )
                .otherwise(pl.lit("modelada"))
                .alias(f"{var}__calidad"),
            )
            .drop("_m", "_c", "_p")
        )
    return out.sort("_i").select(
        "ctx_renta_municipio",
        "ctx_renta_municipio__calidad",
        "ctx_envejecimiento",
        "ctx_envejecimiento__calidad",
    )
