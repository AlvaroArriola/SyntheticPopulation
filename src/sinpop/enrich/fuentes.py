"""Donantes de las encuestas y llaves comunes con la población (D-044.2).

Las llaves se construyen con la misma definición a los dos lados: en la población, a partir de
`persons.parquet`; en las encuestas, a partir de sus ficheros armonizados (`data/interim/`).
"""

from __future__ import annotations

from functools import lru_cache

import polars as pl

from sinpop import INTERIM_DIR

ORDEN_ESTUDIOS = {"hasta_obligatoria": 0, "secundaria_2a_etapa": 1, "superior": 2}
ESTUDIOS = list(ORDEN_ESTUDIOS)

# Tenencia del Censo frente a la detallada de la ECV (D-044.3; T_REGTE y TH021H). El 4
# («alquiler a precio inferior al de mercado») es compatible con «alquiler» y con «otro».
TENENCIA_COMPATIBLE = {
    "propiedad_sin_hipoteca": ["propiedad"],
    "propiedad_con_hipoteca": ["propiedad"],
    "alquiler_mercado": ["alquiler"],
    "alquiler_inferior": ["alquiler", "otro"],
    "cesion_gratuita": ["otro"],
}

# Bloques heredados del mismo donante (D-044.2)
BLOQUE_HOGAR = [
    "renta_equivalente",
    "renta_hogar_decil",
    "renta_hogar_decil_ccaa",
    "tenencia_vivienda",
    "dificultad_fin_mes",
    "vehiculo_hogar",
]
BLOQUE_PERSONA_ECV = [
    "salud_autopercibida",
    "discapacidad_limitacion",
    "privacion_material",
    "privacion_material_n",
]
BLOQUE_EMPLEO = ["tipo_jornada", "sector_publico"]
BLOQUE_DIGITAL = ["uso_internet", "compra_online", "teletrabajo"]


def grupo_edad(edad: pl.Expr, cortes: list[int], nombre: str) -> pl.Expr:
    """Etiqueta del grupo de edad por su límite inferior («16», «20», …); el último grupo es
    abierto; por debajo del primer corte, NP."""
    e = pl.lit(f"{cortes[-1]:02d}")
    for lo, hi in reversed(list(zip(cortes[:-1], cortes[1:], strict=True))):
        e = pl.when(edad < hi).then(pl.lit(f"{lo:02d}")).otherwise(e)
    return pl.when(edad < cortes[0]).then(pl.lit("NP")).otherwise(e).alias(nombre)


EDAD_PERSONA = [16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
EDAD_EPA = [16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]  # grupos de EDAD1 (65 = 65 y más)


def situacion_3(col: str = "situacion_profesional") -> pl.Expr:
    """Empresario / autónomo / asalariado / otra: la situación común al Censo y a la EPA."""
    return (
        pl.when(pl.col(col).str.starts_with("asalariado"))
        .then(pl.lit("asalariado"))
        .otherwise(pl.col(col))
        .alias("situacion_3")
    )


def rasgos_hogar(personas: pl.DataFrame, hogar: str = "household_id") -> pl.DataFrame:
    """Llaves de hogar a partir de sus miembros: ocupados (0, 1, 2+), estudios más altos de los
    de 16+, algún menor de 18, algún 65+ y algún adulto extranjero."""
    adulto = pl.col("edad") >= 16
    nivel = pl.col("estudios_3").replace_strict(ORDEN_ESTUDIOS, default=None, return_dtype=pl.Int32)
    return (
        personas.group_by(hogar)
        .agg(
            pl.len().alias("_n"),
            (pl.col("relacion_actividad") == "ocupado").sum().alias("_ocup"),
            nivel.filter(adulto).max().alias("_est"),
            (pl.col("edad") < 18).any().alias("menores"),
            (pl.col("edad") >= 65).any().alias("mayores_65"),
            ((pl.col("nacionalidad_esp_ext") == "extranjera") & (pl.col("edad") >= 18))
            .any()
            .alias("extranjero"),
        )
        .with_columns(
            pl.when(pl.col("_n") >= 4)
            .then(pl.lit("4+"))
            .otherwise(pl.col("_n").cast(pl.Utf8))
            .alias("tamano_hogar_4"),
            pl.when(pl.col("_ocup") >= 2)
            .then(pl.lit("2+"))
            .otherwise(pl.col("_ocup").cast(pl.Utf8))
            .alias("ocupados"),
            pl.col("_est")
            .replace_strict(dict(enumerate(ESTUDIOS)), default="NC", return_dtype=pl.Utf8)
            .alias("estudios_max"),
            pl.col("menores", "mayores_65", "extranjero").cast(pl.Utf8),
        )
        .drop("_n", "_ocup", "_est")
    )


@lru_cache(maxsize=1)
def _ecv() -> pl.DataFrame:
    return pl.read_parquet(INTERIM_DIR / "ecv.parquet")


def donantes_hogar() -> pl.DataFrame:
    """Hogares de la ECV: llaves, bloque de hogar y peso del hogar (DB090). Cada hogar aparece
    una vez por cada régimen del Censo compatible con su tenencia (columna `tenencia_censo`)."""
    e = _ecv()
    h = (
        e.group_by("household_id")
        .agg(
            pl.col(
                "ccaa", "grado_urbanizacion", "tenencia_ecv", "peso_hogar", *BLOQUE_HOGAR
            ).first()
        )
        .join(rasgos_hogar(e), on="household_id")
        .filter(pl.col("tenencia_ecv").is_in(list(TENENCIA_COMPATIBLE)))
    )
    compat = pl.DataFrame(
        [(k, v) for k, vs in TENENCIA_COMPATIBLE.items() for v in vs],
        schema=["tenencia_ecv", "tenencia_censo"],
        orient="row",
    )
    return h.join(compat, on="tenencia_ecv").sort("household_id", "tenencia_censo")


def donantes_persona_ecv() -> pl.DataFrame:
    """Personas de 16+ de la ECV (fichero de adultos, peso PB040) con el decil de su hogar."""
    return (
        _ecv()
        .filter(pl.col("peso_16").is_not_null() & (pl.col("edad") >= 16))
        .with_columns(grupo_edad(pl.col("edad"), EDAD_PERSONA, "edad_grupo"))
        .sort("person_id")
    )


def donantes_empleo() -> pl.DataFrame:
    """Ocupados de la EPA con jornada y sector conocidos."""
    e = pl.read_parquet(INTERIM_DIR / "epa.parquet")
    return (
        e.filter(
            (pl.col("relacion_actividad_3") == "ocupado")
            & pl.col("tipo_jornada").is_in(["completa", "parcial"])
            & pl.col("sector_publico").is_in(["si", "no"])
        )
        .with_columns(pl.col("edad_grupo_epa").alias("edad_grupo"), situacion_3())
        .with_row_index("_fila")
        .sort("_fila")
        .drop("_fila")
    )


def donantes_digital() -> pl.DataFrame:
    """Personas de 16+ de la TIC-H."""
    t = pl.read_parquet(INTERIM_DIR / "tic_h.parquet")
    return t.with_columns(
        grupo_edad(pl.col("edad"), EDAD_PERSONA, "edad_grupo"),
        (pl.col("relacion_actividad") == "ocupado").cast(pl.Utf8).alias("ocupado"),
    )
