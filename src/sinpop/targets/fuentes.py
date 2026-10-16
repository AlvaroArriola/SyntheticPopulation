"""Lectura de las tablas oficiales que dan la estructura de los objetivos (F3, D-036).

Cada función devuelve recuentos por provincia (código INE), sexo, grupo de edad de su tabla y
categoría armonizada. Las etiquetas de las tablas se traducen con mapas explícitos: una
etiqueta que no esté en el mapa detiene el proceso (regla 2 de CLAUDE.md).
"""

from __future__ import annotations

import re

import polars as pl

from sinpop import RAW_DIR
from sinpop.ingest.ine_tablas import leer
from sinpop.targets.edades import etiquetas

TAB = RAW_DIR / "censo_anual_tablas/ultimo"
SEXO = {"Hombres": "hombre", "Mujeres": "mujer"}

ESTUDIOS = {  # tabla 66601 → estudios_3
    "Sin estudios": "hasta_obligatoria",
    "Educación primaria": "hasta_obligatoria",
    "Primera etapa de Educación Secundaria y similar": "hasta_obligatoria",
    "Segunda etapa de educación secundaria, con orientación general": "secundaria_2a_etapa",
    "Segunda etapa de educación secundaria con orientación profesional; Educación "
    "postsecundaria no superior": "secundaria_2a_etapa",
    "Enseñanzas de formación profesional, artes plásticas y diseño y deportivas de grado "
    "superior y equivalentes": "superior",
    "Grados universitarios de hasta 240 créditos ECTS, diplomados universitarios y "
    "equivalentes": "superior",
    "Grados universitarios de más de 240 créditos ECTS, licenciados y equivalentes": "superior",
    "Másteres, especialidades en Ciencias de la Salud por el sistema de residencia y "
    "similares": "superior",
    "Doctorado universitario": "superior",
}
ACTIVIDAD = {  # tabla 67128 → relacion_actividad
    "Ocupado/a": "ocupado",
    "Parado/a": "parado",
    "Perceptor/a pensión de jubilación, prejubilación": "jubilado_pensionista",
    "Perceptor/a pensión de incapacidad": "incapacidad_permanente",
    "Estudiante": "estudiante",
    "Otra situación de inactividad": "otra_inactividad",
}
ESTADO_CIVIL = {  # tabla 76291 → estado_civil
    "Soltero/a": "soltero",
    "Casado/a": "casado",
    "Viudo/a": "viudo",
    "Divorciado/a o separado/a": "separado_divorciado",
    "No consta": "NC",
}
URBANIZACION = {  # tabla 79341 → grado_urbanizacion
    "Área densamente poblada": "ciudad",
    "Área poblada nivel intermedio": "intermedio",
    "Área poco poblada": "rural",
}


def etiqueta_edad(texto: str | None) -> str | None:
    """«De 15 a 19 años» → «15-19»; «90 y más años» → «90+»; «Menos de 16 años» → «00-15»."""
    if texto is None:
        return None
    if m := re.fullmatch(r"De (\d+) a (\d+) años", texto):
        return f"{int(m.group(1)):02d}-{int(m.group(2)):02d}"
    if m := re.fullmatch(r"(\d+) y más años", texto):
        return f"{int(m.group(1))}+"
    if m := re.fullmatch(r"Menos de (\d+) años", texto):
        return f"00-{int(m.group(1)) - 1:02d}"
    raise ValueError(f"rótulo de edad no reconocido: {texto!r}")


def tabla_estructura(
    t: pl.DataFrame,
    nombre: str,
    dim: str,
    mapa: dict[str, str],
    cortes: list[int],
    *,
    con_grupo_inferior: bool = False,
) -> pl.DataFrame:
    """Recuentos (provincia, sexo, grupo, categoria, valor) de una tabla de estructura.

    Usa la nacionalidad «Total» si la tabla la desagrega, descarta los totales de sexo, de
    categoría y de edad, y comprueba que los grupos de edad son exactamente los de `cortes`.
    El grupo inferior («00-…») solo se espera si la variable se aplica a todas las edades
    (`con_grupo_inferior`); si no, en él la variable no procede y no está en la tabla.
    """
    if "Nacionalidad" in t.columns:
        t = t.filter(pl.col("Nacionalidad") == "Total")
    t = t.filter(
        pl.col("Provincias").is_not_null()
        & pl.col("Sexo").is_in(list(SEXO))
        & (pl.col(dim) != "Total")
    )
    cols_edad = [c for c in ("Grupos de edad", "Semiintervalos de edad") if c in t.columns]
    t = t.with_columns(pl.coalesce([pl.col(c) for c in cols_edad]).alias("_edad")).filter(
        pl.col("_edad").is_not_null()
    )
    labs = etiquetas(cortes)
    validas = set(labs if con_grupo_inferior else labs[1:])
    grupos = [etiqueta_edad(x) for x in t["_edad"].to_list()]
    t = t.with_columns(pl.Series("grupo", grupos, dtype=pl.Utf8)).filter(
        pl.col("grupo").is_in(list(validas))
    )
    faltan = validas - set(t["grupo"].unique().to_list())
    if faltan:
        raise ValueError(f"{nombre}: faltan grupos de edad {sorted(faltan)}")
    sin = set(t[dim].unique().to_list()) - set(mapa)
    if sin:
        raise ValueError(f"{nombre}: categorías sin traducir {sorted(sin)}")
    return (
        t.select(
            pl.col("Provincias__cod").alias("provincia"),
            pl.col("Sexo").replace_strict(SEXO).alias("sexo"),
            "grupo",
            pl.col(dim).replace_strict(mapa).alias("categoria"),
            "valor",
        )
        .group_by("provincia", "sexo", "grupo", "categoria")
        .agg(pl.col("valor").sum())
        .sort("provincia", "sexo", "grupo", "categoria")
    )


def _leer(nombre: str) -> tuple[pl.DataFrame, str]:
    path = TAB / nombre
    return leer(path), path.name


def estudios(cortes: list[int]) -> pl.DataFrame:
    t, n = _leer("tabla_66601_ultimo.json")
    return tabla_estructura(t, n, "Nivel de formación alcanzado", ESTUDIOS, cortes)


def actividad(cortes: list[int]) -> pl.DataFrame:
    t, n = _leer("tabla_67128_ultimo.json")
    return tabla_estructura(t, n, "Relación con la actividad", ACTIVIDAD, cortes)


def estado_civil(cortes: list[int]) -> pl.DataFrame:
    t, n = _leer("tabla_76291_ultimo.json")
    return tabla_estructura(t, n, "Estado civil", ESTADO_CIVIL, cortes)


def urbanizacion(cortes: list[int]) -> pl.DataFrame:
    path = RAW_DIR / "degurba/ultimo/tabla_79341_ultimo.json"
    t = leer(path).filter(pl.col("Totales de edad").is_null())
    return tabla_estructura(
        t, path.name, "Grado de urbanización", URBANIZACION, cortes, con_grupo_inferior=True
    )
