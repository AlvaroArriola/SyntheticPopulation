"""Objetivos de calibración y de validación por provincia (F3, D-036).

Método común: los efectivos los da la ECP a 01/01/2026 (provincia × sexo × edad simple); la
estructura de cada variable la dan las tablas oficiales más recientes que la publican, como
cuotas dentro de la misma celda provincia × sexo × grupo de edad de su tabla. Así todos los
objetivos de persona suman lo mismo por provincia, sexo y edad (G3.1, G3.2), y las comunidades
y España se obtienen sumando provincias (G3.3).

Formato de salida (largo): una fila por provincia, objetivo y celda, con la fuente, la edición
y la fecha de referencia de la cifra (G3.5).
"""

from __future__ import annotations

import datetime as dt

import polars as pl

from sinpop import INTERIM_DIR
from sinpop.config import load_config
from sinpop.harmonize.core import edad_4, edad_5
from sinpop.targets import edades, fuentes
from sinpop.targets.edades import agrupar, etiquetas

FECHA = dt.date(2026, 1, 1)
COLUMNAS = [
    "provincia",
    "objetivo",
    "uso",
    "unidad",
    "universo",
    "clave",
    "valor",
    "fuente",
    "edicion",
    "fecha_referencia",
    "metodo",
]


# --------------------------------------------------------------------------- bases


def base_edad() -> pl.DataFrame:
    """Residentes a 01/01/2026 por provincia, sexo y edad simple (ECP 59589; 100 = 100+)."""
    return pl.read_parquet(INTERIM_DIR / "ecp_total.parquet").rename({"personas": "n"})


def base_grupo(cortes: list[int], nombre: str) -> pl.DataFrame:
    return (
        base_edad()
        .with_columns(agrupar(pl.col("edad"), cortes, nombre))
        .group_by("provincia", "sexo", nombre)
        .agg(pl.col("n").sum())
    )


def reescalar(estr: pl.DataFrame, base: pl.DataFrame, grupo: str) -> pl.DataFrame:
    """Reparte `base` (provincia, sexo, grupo, n) con las cuotas de `estr`.

    `estr` trae recuentos (provincia, sexo, grupo, categoria, valor). Si una celda de la tabla
    está vacía (sin efectivos), se usan las cuotas nacionales de su sexo y grupo.
    """
    e = estr.rename({"grupo": grupo})
    tot = pl.col("valor").sum().over("provincia", "sexo", grupo)
    cuota = e.with_columns((pl.col("valor") / tot).alias("cuota")).filter(tot > 0)
    nac = (
        e.group_by("sexo", grupo, "categoria")
        .agg(pl.col("valor").sum())
        .with_columns((pl.col("valor") / pl.col("valor").sum().over("sexo", grupo)).alias("c"))
    )
    celdas = base.join(
        cuota.select("provincia", "sexo", grupo).unique(),
        on=["provincia", "sexo", grupo],
        how="anti",
    )
    con = base.join(
        cuota.select("provincia", "sexo", grupo, "categoria", "cuota"),
        on=["provincia", "sexo", grupo],
    )
    sin = celdas.join(
        nac.select("sexo", grupo, "categoria", pl.col("c").alias("cuota")), on=["sexo", grupo]
    )
    return pl.concat([con, sin]).select(
        "provincia", "sexo", grupo, "categoria", (pl.col("n") * pl.col("cuota")).alias("valor")
    )


def _no_procede(base: pl.DataFrame, grupo: str, inferior: str) -> pl.DataFrame:
    """Personas por debajo de la edad mínima de la tabla: la variable no procede (NP)."""
    return base.filter(pl.col(grupo) == inferior).select(
        "provincia", "sexo", grupo, pl.lit("NP").alias("categoria"), pl.col("n").alias("valor")
    )


def estructura(fn, clave_cortes: str) -> pl.DataFrame:
    """Objetivo completo (todas las edades) de una variable con tabla de estructura."""
    cortes = load_config("targets.yaml").agrupaciones_edad[clave_cortes]  # type: ignore[attr-defined]
    base = base_grupo(cortes, clave_cortes)
    estr = fn(cortes)
    out = reescalar(estr, base, clave_cortes)
    inferior = etiquetas(cortes)[0]
    if inferior not in set(estr["grupo"].unique().to_list()):
        out = pl.concat([out, _no_procede(base, clave_cortes, inferior)])
    return out


# --------------------------------------------------------------------------- actividad (EPA)

# D-046 A2 y D-049: relación con la actividad (las 6 categorías) de la EPA del 2T 2026 por
# comunidad × sexo × tramo de edad (inactivos por su situación autopercibida, SIDI1); el reparto
# entre provincias y grupos quinquenales dentro de cada tramo es el del Censo Anual a 01/01/2024.
TRAMOS_EPA = [16, 25, 35, 45, 55, 65]
PESO_PREVIO = 200.0  # personas de la muestra que equivalen a la estimación previa


def _tramo(lo: pl.Expr) -> pl.Expr:
    e = pl.lit(f"{TRAMOS_EPA[-1]}")
    for a, b in reversed(list(zip(TRAMOS_EPA[:-1], TRAMOS_EPA[1:], strict=True))):
        e = pl.when(lo < b).then(pl.lit(f"{a}")).otherwise(e)
    return e.alias("tramo")


def tasas_epa() -> pl.DataFrame:
    """Proporción de cada relación con la actividad (16+, sin NC) por comunidad × sexo × tramo
    en la EPA del 2T 2026 (pesos FACTOREL), con su muestra (n) para la contracción."""
    e = pl.read_parquet(INTERIM_DIR / "epa.parquet").filter(
        (pl.col("edad_grupo_epa") >= "16") & ~pl.col("relacion_actividad").is_in(["NC", "NP"])
    )
    e = e.with_columns(_tramo(pl.col("edad_grupo_epa").cast(pl.Int32)))
    k = ["ccaa", "sexo", "tramo"]
    return (
        e.group_by([*k, "relacion_actividad"])
        .agg(pl.col("peso").sum().alias("w"))
        .with_columns(
            (pl.col("w") / pl.col("w").sum().over(k)).alias("e"),
        )
        .join(e.group_by(k).agg(pl.len().alias("n")), on=k)
        .rename({"relacion_actividad": "categoria"})
    )


def actividad_epa(cortes: list[int]) -> pl.DataFrame:
    """Estructura del Censo Anual reajustada a la EPA (D-046 A2, D-049).

    En cada comunidad × sexo × tramo, cada categoría se multiplica por el cociente entre su
    proporción objetivo y la del Censo, de modo que la estructura de la celda es la de la EPA y
    el reparto entre provincias y edades quinquenales dentro del tramo, el del Censo. El
    objetivo es la proporción de la EPA contraída hacia una previa con `PESO_PREVIO` personas:
    el Censo de la celda corregido con el cociente EPA / Censo nacional de su sexo y tramo (las
    celdas pequeñas de la EPA, como Ceuta o Melilla, no se toman al pie de la letra)."""
    from sinpop.harmonize.core import ccaa_de_provincia

    c = fuentes.actividad(cortes).with_columns(
        pl.col("provincia").replace_strict(ccaa_de_provincia()).alias("ccaa"),
        _tramo(pl.col("grupo").str.slice(0, 2).cast(pl.Int32)),
    )
    k = ["ccaa", "sexo", "tramo"]
    cen = c.group_by([*k, "categoria"]).agg(pl.col("valor").sum().alias("cv"))
    celdas = cen.select(k).unique().join(cen.select("categoria").unique(), how="cross")
    cen = (
        celdas.join(cen, on=[*k, "categoria"], how="left")
        .fill_null(0.0)
        .with_columns((pl.col("cv") / pl.col("cv").sum().over(k)).alias("c"))
    )
    nac_c = (
        cen.group_by("sexo", "tramo", "categoria")
        .agg(pl.col("cv").sum())
        .with_columns((pl.col("cv") / pl.col("cv").sum().over("sexo", "tramo")).alias("cn"))
    )
    epa = tasas_epa()
    nac_e = (
        epa.group_by("sexo", "tramo", "categoria")
        .agg(pl.col("w").sum())
        .with_columns((pl.col("w") / pl.col("w").sum().over("sexo", "tramo")).alias("en"))
    )
    t = (
        cen.join(epa.select(*k, "categoria", "e", "n"), on=[*k, "categoria"], how="left")
        .join(nac_c.select("sexo", "tramo", "categoria", "cn"), on=["sexo", "tramo", "categoria"])
        .join(
            nac_e.select("sexo", "tramo", "categoria", "en"),
            on=["sexo", "tramo", "categoria"],
            how="left",
        )
        .with_columns(
            pl.col("e").fill_null(0.0),
            pl.col("en").fill_null(0.0),
            pl.col("n").max().over(k).fill_null(0),
        )
        .with_columns(
            pl.when(pl.col("cn") > 0)
            .then(pl.col("c") * pl.col("en") / pl.col("cn"))
            .otherwise(pl.col("en"))
            .alias("previa")
        )
        .with_columns((pl.col("previa") / pl.col("previa").sum().over(k)).alias("previa"))
        .with_columns(
            (
                (pl.col("n") * pl.col("e") + PESO_PREVIO * pl.col("previa"))
                / (pl.col("n") + PESO_PREVIO)
            ).alias("objetivo")
        )
    )
    # Reparto dentro de la celda: cuotas del Censo por provincia × grupo quinquenal; si el Censo
    # no tiene a nadie de esa categoría en la celda, las de la propia celda en conjunto.
    dentro = c.with_columns(
        (pl.col("valor") / pl.col("valor").sum().over([*k, "categoria"])).alias("r"),
        (
            pl.col("valor").sum().over(["provincia", "sexo", "grupo"])
            / pl.col("valor").sum().over(k)
        ).alias("peso_celda"),
    )
    out = dentro.join(t.select(*k, "categoria", "objetivo"), on=[*k, "categoria"]).with_columns(
        pl.when(pl.col("r").is_not_nan() & pl.col("r").is_not_null())
        .then(pl.col("r"))
        .otherwise(pl.col("peso_celda"))
        .alias("r")
    )
    total = c.group_by(k).agg(pl.col("valor").sum().alias("tot"))
    return (
        out.join(total, on=k)
        .with_columns((pl.col("tot") * pl.col("objetivo") * pl.col("r")).alias("valor"))
        .select("provincia", "sexo", "grupo", "categoria", "valor")
    )


def a_tramos(e: pl.DataFrame) -> pl.DataFrame:
    """Agrupa `edad_actividad` (quinquenal) en los tramos de la EPA (`edad_tramo_epa`)."""
    cortes = load_config("targets.yaml").agrupaciones_edad["edad_tramo_epa"]  # type: ignore[attr-defined]
    labs = etiquetas(cortes)
    lo = pl.col("edad_actividad").str.slice(0, 2).cast(pl.Int32)
    g = pl.lit(labs[-1])
    for lim, lab in reversed(list(zip(cortes[1:], labs[1:-1], strict=True))):
        g = pl.when(lo < lim).then(pl.lit(lab)).otherwise(g)
    g = pl.when(lo < cortes[0]).then(pl.lit(labs[0])).otherwise(g)
    return e.with_columns(g.alias("edad_tramo_epa"))


def sin_estudios(cortes: list[int]) -> pl.DataFrame:
    """«Sin estudios» de la tabla 66601 (Censo Anual a 01/01/2024) frente al resto (D-049)."""
    t, n = fuentes._leer("tabla_66601_ultimo.json")
    mapa = {k: ("si" if k == "Sin estudios" else "no") for k in fuentes.ESTUDIOS}
    e = fuentes.tabla_estructura(t, n, "Nivel de formación alcanzado", mapa, cortes)
    return e.group_by("provincia", "sexo", "grupo", "categoria").agg(pl.col("valor").sum())


def nacimiento_nacionalidad() -> pl.DataFrame:
    """Residentes 2026 por provincia, nacionalidad española/extranjera y nacimiento fuera de
    España (D-049): las celdas provincia × sexo × edad_5 × nacionalidad de la ECP 2026, con la
    proporción de nacidos fuera de su celda en el Censo Anual exhaustivo a 01/01/2025 (si la
    celda está vacía, la de su provincia y nacionalidad)."""
    nac = esp_ext(nacionalidad_celdas().filter(pl.col("variable") == "nacionalidad_grupo"))
    k = ["provincia", "sexo", "edad_5", "nacionalidad_esp_ext"]
    cel = nac.group_by(k).agg(pl.col("valor").sum())
    ex = pl.read_parquet(INTERIM_DIR / "censo_anual_exhaustivo_2025.parquet")
    ex = esp_ext(ex, "nacionalidad_grupo").with_columns(
        (pl.col("pais_nacimiento_grupo") != "espana").alias("_fuera")
    )
    q1 = ex.group_by(k).agg(
        (pl.col("personas").filter(pl.col("_fuera")).sum() / pl.col("personas").sum()).alias("q1")
    )
    q2 = ex.group_by("provincia", "nacionalidad_esp_ext").agg(
        (pl.col("personas").filter(pl.col("_fuera")).sum() / pl.col("personas").sum()).alias("q2")
    )
    c = (
        cel.join(q1, on=k, how="left")
        .join(q2, on=["provincia", "nacionalidad_esp_ext"], how="left")
        .with_columns(pl.coalesce("q1", "q2").fill_null(0.0).alias("q"))
    )
    return pl.concat(
        [
            c.select(
                *k,
                pl.lit("si").alias("nacido_fuera"),
                (pl.col("valor") * pl.col("q")).alias("valor"),
            ),
            c.select(
                *k,
                pl.lit("no").alias("nacido_fuera"),
                (pl.col("valor") * (1 - pl.col("q"))).alias("valor"),
            ),
        ]
    )


# --------------------------------------------------------------------------- nacionalidad


def nacionalidad_celdas() -> pl.DataFrame:
    """Residentes 2026 por provincia, sexo, edad_5 y nacionalidad (grupo y top 15).

    Española/extranjera: viviendas familiares de la ECP 2026 (60129) + colectivos 2026 con la
    proporción de extranjeros de su celda en el Censo Anual exhaustivo 2025. Grupos y
    nacionalidades dentro de los extranjeros: cuotas del Censo Anual exhaustivo 2025 en la
    misma celda (si la celda no tenía extranjeros en 2025, las de su provincia y sexo).
    """
    fam = pl.read_parquet(INTERIM_DIR / "ecp_viviendas_familiares.parquet")
    col = pl.read_parquet(INTERIM_DIR / "ecp_colectivos.parquet").select(
        "provincia", "sexo", "edad_5", pl.col("personas").alias("col")
    )
    ex = pl.read_parquet(INTERIM_DIR / "censo_anual_exhaustivo_2025.parquet")
    k = ["provincia", "sexo", "edad_5"]
    p_ext = ex.group_by(k).agg(
        (
            pl.col("personas").filter(pl.col("nacionalidad_grupo") != "espanola").sum()
            / pl.col("personas").sum()
        ).alias("p_ext")
    )
    f = fam.pivot(on="nacionalidad_esp_ext", index=k, values="personas").fill_null(0)
    cel = (
        f.join(col, on=k, how="full", coalesce=True)
        .join(p_ext, on=k, how="left")
        .fill_null(0)
        .with_columns(
            (pl.col("extranjera") + pl.col("col") * pl.col("p_ext")).alias("ext"),
            (pl.col("espanola") + pl.col("col") * (1 - pl.col("p_ext"))).alias("esp"),
        )
    )
    ext = ex.filter(pl.col("nacionalidad_grupo") != "espanola")
    filas = []
    for var in ("nacionalidad_grupo", "nacionalidad_top"):
        c1 = (
            ext.group_by(*k, var)
            .agg(pl.col("personas").sum())
            .with_columns((pl.col("personas") / pl.col("personas").sum().over(k)).alias("q"))
        )
        c2 = (
            ext.group_by("provincia", "sexo", var)
            .agg(pl.col("personas").sum())
            .with_columns(
                (pl.col("personas") / pl.col("personas").sum().over("provincia", "sexo")).alias(
                    "q2"
                )
            )
        )
        sin = cel.join(c1.select(k).unique(), on=k, how="anti").filter(pl.col("ext") > 0)
        a = cel.join(c1.select(*k, var, "q"), on=k).select(
            *k, pl.col(var).alias("categoria"), (pl.col("ext") * pl.col("q")).alias("valor")
        )
        b = sin.join(c2.select("provincia", "sexo", var, "q2"), on=["provincia", "sexo"]).select(
            *k, pl.col(var).alias("categoria"), (pl.col("ext") * pl.col("q2")).alias("valor")
        )
        e = cel.select(*k, pl.lit("espanola").alias("categoria"), pl.col("esp").alias("valor"))
        filas.append(pl.concat([a, b, e]).with_columns(pl.lit(var).alias("variable")))
    return pl.concat(filas)


def esp_ext(nac: pl.DataFrame, columna: str = "categoria") -> pl.DataFrame:
    """Añade `nacionalidad_esp_ext` (española / extranjera) a celdas de `nacionalidad_grupo`."""
    return nac.with_columns(
        pl.when(pl.col(columna) == "espanola")
        .then(pl.lit("espanola"))
        .otherwise(pl.lit("extranjera"))
        .alias("nacionalidad_esp_ext")
    )


def adultos_nacionalidad(nac: pl.DataFrame, clave: str = "provincia") -> pl.DataFrame:
    """Residentes 2026 por provincia, nacionalidad española/extranjera y mayoría de edad.

    Las celdas de nacionalidad van por edad quinquenal; el grupo 15-19 se parte en 15-17 y
    18-19 con la proporción de edades simples de la ECP 2026 en su provincia y sexo.
    """
    b = base_edad().filter(pl.col("edad").is_between(15, 19))
    p18 = b.group_by("provincia", "sexo").agg(
        (pl.col("n").filter(pl.col("edad") >= 18).sum() / pl.col("n").sum()).alias("p18")
    )
    n = esp_ext(nac.filter(pl.col("variable") == "nacionalidad_grupo"))
    n = n.join(p18, on=["provincia", "sexo"], how="left")
    menores = ["00-04", "05-09", "10-14"]
    adul = (
        pl.when(pl.col("edad_5").is_in(menores))
        .then(0.0)
        .when(pl.col("edad_5") == "15-19")
        .then(pl.col("p18"))
        .otherwise(1.0)
    )
    return pl.concat(
        [
            n.select(
                clave,
                "nacionalidad_esp_ext",
                pl.lit("si").alias("es_adulto"),
                (pl.col("valor") * adul).alias("valor"),
            ),
            n.select(
                clave,
                "nacionalidad_esp_ext",
                pl.lit("no").alias("es_adulto"),
                (pl.col("valor") * (1 - adul)).alias("valor"),
            ),
        ]
    )


# --------------------------------------------------------------------------- hogares


def hogares_censo2021() -> pl.DataFrame:
    """Hogares del Censo 2021 (muestra del 10 %): provincia, tipo, tamaño y edad de la persona
    de referencia (la de más edad, D-021), con su factor de elevación."""
    p = pl.read_parquet(
        INTERIM_DIR / "censo2021_personas.parquet",
        columns=["provincia", "relacion_persona_ref", "tipo_hogar", "tamano_hogar", "edad", "peso"],
    ).filter(pl.col("relacion_persona_ref") == "persona_referencia")
    return p.select(
        "provincia",
        "tipo_hogar",
        pl.col("tamano_hogar").replace({"4": "4+", "5+": "4+"}).alias("tamano_hogar_4"),
        edad_4(pl.col("edad")),
        "peso",
    )


def tipo_hogar() -> tuple[pl.DataFrame, pl.DataFrame]:
    """(tipo × tamaño, tipo × tamaño × edad_4 de la referencia) sobre los hogares ECP 2026.

    Tipo × tamaño (calibrado): cuotas del Censo 2021 dentro de cada provincia y tamaño (1, 2, 3,
    4+), aplicadas a los hogares por tamaño de la ECP 2026; así el número de hogares
    unipersonales coincide con el de tamaño 1 y el resto de tipos con su tamaño.

    Con la edad de la referencia (reservado; D-050): la estructura del Censo 2021 se ajusta (IPF)
    a ese tipo × tamaño y a los hogares de 2026 por edad de la referencia, que salen del método de
    las tasas de jefatura: la proporción de personas de cada provincia, sexo y edad que son
    referencia de su hogar en 2021, aplicada a la población en viviendas familiares de la ECP
    2026. Sin ello, la edad de la referencia era la de 2021, sin el envejecimiento posterior.
    """
    h = hogares_censo2021()
    ecp = pl.read_parquet(INTERIM_DIR / "ecp_hogares.parquet")
    k = ["provincia", "tamano_hogar_4"]
    c = (
        h.group_by(*k, "tipo_hogar", "edad_4")
        .agg(pl.col("peso").sum())
        .with_columns((pl.col("peso") / pl.col("peso").sum().over(k)).alias("q"))
    )
    semilla = c.join(ecp, on=k).select(
        *k, "tipo_hogar", "edad_4", (pl.col("hogares") * pl.col("q")).alias("valor")
    )
    tipo = semilla.group_by(*k, "tipo_hogar").agg(pl.col("valor").sum())
    jef = jefatura_2026()
    det = _ipf_hogares(semilla, tipo, jef)
    return tipo, det


def jefatura_2026() -> pl.DataFrame:
    """Hogares de 2026 por provincia y edad_4 de la referencia: tasas de jefatura del Censo 2021
    (referencias / personas en viviendas familiares por provincia × sexo × edad_5, partidas por
    la edad_4 de la referencia, que corta el grupo 15-19) × población ECP 2026 en viviendas
    familiares por provincia × sexo × edad_5. Se escalan al total de hogares ECP 2026."""
    p = pl.read_parquet(
        INTERIM_DIR / "censo2021_personas.parquet",
        columns=["provincia", "sexo", "edad", "edad_5", "relacion_persona_ref", "peso"],
    )
    k = ["provincia", "sexo", "edad_5"]
    personas = p.group_by(k).agg(pl.col("peso").sum().alias("personas"))
    refs = (
        p.filter(pl.col("relacion_persona_ref") == "persona_referencia")
        .with_columns(edad_4(pl.col("edad")))
        .group_by(*k, "edad_4")
        .agg(pl.col("peso").sum().alias("refs"))
    )
    tasa = refs.join(personas, on=k).with_columns((pl.col("refs") / pl.col("personas")).alias("t"))
    pob = (
        pl.read_parquet(INTERIM_DIR / "ecp_viviendas_familiares.parquet")
        .group_by(k)
        .agg(pl.col("personas").sum().alias("p26"))
    )
    j = (
        tasa.join(pob, on=k)
        .group_by("provincia", "edad_4")
        .agg((pl.col("t") * pl.col("p26")).sum().alias("hogares"))
    )
    tot = (
        pl.read_parquet(INTERIM_DIR / "ecp_hogares.parquet")
        .group_by("provincia")
        .agg(pl.col("hogares").sum().alias("_t"))
    )
    return j.join(tot, on="provincia").select(
        "provincia",
        "edad_4",
        (pl.col("hogares") * pl.col("_t") / pl.col("hogares").sum().over("provincia")).alias(
            "hogares"
        ),
    )


def _ipf_hogares(
    semilla: pl.DataFrame, tipo: pl.DataFrame, jef: pl.DataFrame, iteraciones: int = 200
) -> pl.DataFrame:
    """IPF de tipo × tamaño × edad_4 por provincia a dos márgenes: tipo × tamaño (`tipo`) y
    edad_4 (`jef`), que suman lo mismo en cada provincia."""
    k = ["provincia", "tamano_hogar_4", "tipo_hogar"]
    d = semilla
    for _ in range(iteraciones):
        d = (
            d.join(jef.rename({"hogares": "_m"}), on=["provincia", "edad_4"], how="left")
            .with_columns(
                (pl.col("valor") * pl.col("_m") / pl.col("valor").sum().over("provincia", "edad_4"))
                .fill_nan(0.0)
                .alias("valor")
            )
            .drop("_m")
        )
        d = (
            d.join(tipo.rename({"valor": "_m"}), on=k, how="left")
            .with_columns(
                (pl.col("valor") * pl.col("_m") / pl.col("valor").sum().over(k))
                .fill_nan(0.0)
                .alias("valor")
            )
            .drop("_m")
        )
    return d.sort(*k, "edad_4")


# --------------------------------------------------------------------------- municipio


def tamano_municipio() -> pl.DataFrame:
    """Residentes 2026 por tamaño de municipio: cuotas del Padrón 2025 (tabla 29005) dentro de
    cada provincia aplicadas al total de la ECP 2026."""
    from sinpop.harmonize.censos import poblacion_municipal
    from sinpop.harmonize.core import tamano_por_poblacion

    pm = poblacion_municipal()
    pm = pm.with_columns(
        pl.Series("tamano_municipio", [tamano_por_poblacion(int(x)) for x in pm["poblacion"]])
    )
    c = (
        pm.group_by(pl.col("CPRO").alias("provincia"), "tamano_municipio")
        .agg(pl.col("poblacion").sum())
        .with_columns(
            (pl.col("poblacion") / pl.col("poblacion").sum().over("provincia")).alias("q")
        )
    )
    tot = base_edad().group_by("provincia").agg(pl.col("n").sum())
    return c.join(tot, on="provincia").select(
        "provincia", "tamano_municipio", (pl.col("n") * pl.col("q")).alias("valor")
    )


# --------------------------------------------------------------------------- ensamblado


def _largo(
    df: pl.DataFrame,
    variables: list[str],
    objetivo: str,
    meta: dict[str, str],
) -> pl.DataFrame:
    """Suma `valor` por provincia y `variables` y lo pasa al formato largo con su `clave`."""
    cfg = load_config("targets.yaml")
    obj = next(o for o in cfg.calibrar + cfg.reservar if o.id == objetivo)  # type: ignore[attr-defined]
    uso = "calibrar" if obj in cfg.calibrar else "reservar"  # type: ignore[attr-defined]
    # Orden fijo y redondeo a la millonésima: las sumas en coma flotante en paralelo cambian
    # en el último bit según el orden, y el fichero debe tener siempre el mismo hash
    g = (
        df.sort("provincia", *variables)
        .group_by("provincia", *variables, maintain_order=True)
        .agg(pl.col("valor").sum())
    )
    clave = pl.concat_str(
        [pl.concat_str([pl.lit(f"{v}="), pl.col(v).cast(pl.Utf8)]) for v in variables],
        separator=";",
    )
    return g.select(
        "provincia",
        pl.lit(objetivo).alias("objetivo"),
        pl.lit(uso).alias("uso"),
        pl.lit(obj.unidad).alias("unidad"),
        pl.lit(obj.universo).alias("universo"),
        clave.alias("clave"),
        pl.col("valor").cast(pl.Float64).round(6),
        pl.lit(meta["fuente"]).alias("fuente"),
        pl.lit(meta["edicion"]).alias("edicion"),
        pl.lit(FECHA).alias("fecha_referencia"),
        pl.lit(meta["metodo"]).alias("metodo"),
    )


def provincias() -> pl.DataFrame:
    """Todos los objetivos de targets.yaml para las 52 provincias, en formato largo."""
    out = []
    base = base_edad().with_columns(edad_5(pl.col("edad")))
    out.append(
        _largo(
            base.rename({"n": "valor"}),
            ["edad_5", "sexo"],
            "edad5_sexo",
            {"fuente": "ecp: tabla 59589", "edicion": "2026-01-01", "metodo": "exacto"},
        )
    )
    fam = pl.read_parquet(INTERIM_DIR / "ecp_viviendas_familiares.parquet").rename(
        {"personas": "valor"}
    )
    out.append(
        _largo(
            fam,
            ["edad_5", "sexo"],
            "edad5_sexo_familiares",
            {"fuente": "ecp: tabla 60129", "edicion": "2026-01-01", "metodo": "exacto"},
        )
    )
    col = pl.read_parquet(INTERIM_DIR / "ecp_colectivos.parquet").drop("total", "familiares")
    out.append(
        _largo(
            col.rename({"personas": "valor"}),
            ["edad_5", "sexo"],
            "edad5_sexo_colectivos",
            {
                "fuente": "ecp: tablas 59589 − 60129",
                "edicion": "2026-01-01",
                "metodo": "diferencia de dos tablas exactas (D-021)",
            },
        )
    )
    nac = nacionalidad_celdas()
    meta_nac = {
        "fuente": "ecp: tabla 60129 + censo_anual_micro_demograficas (exhaustivo)",
        "edicion": "2026-01-01 (española/extranjera); 2025-01-01 (grupos)",
        "metodo": "extranjeros 2026 repartidos con cuotas de 2025 por provincia × sexo × edad_5",
    }
    for var, obj in (
        ("nacionalidad_grupo", "nacionalidad"),
        ("nacionalidad_top", "nacionalidad_top"),
    ):
        out.append(
            _largo(
                nac.filter(pl.col("variable") == var).rename({"categoria": var}),
                [var],
                obj,
                meta_nac,
            )
        )
    top = nac.filter(pl.col("variable") == "nacionalidad_top").rename(
        {"categoria": "nacionalidad_top"}
    )
    out.append(
        _largo(
            top.with_columns(
                edades.agrupar(
                    pl.col("edad_5").str.slice(0, 2).cast(pl.Int64),
                    edades.cortes()["edad_nacionalidad"],
                    "edad_nacionalidad",
                )
            ),
            ["nacionalidad_top", "sexo", "edad_nacionalidad"],
            "nacionalidad_top_sexo_edad",
            meta_nac,
        )
    )
    out.append(
        _largo(
            top.with_columns(
                edades.agrupar(
                    pl.col("edad_5").str.slice(0, 2).cast(pl.Int64),
                    edades.cortes()["edad_nacionalidad"],
                    "edad_nacionalidad",
                )
            ),
            ["nacionalidad_top", "edad_nacionalidad"],
            "nacionalidad_top_edad",
            meta_nac,
        )
    )
    out.append(
        _largo(
            adultos_nacionalidad(nac),
            ["nacionalidad_esp_ext", "es_adulto"],
            "adultos_nacionalidad",
            meta_nac | {"metodo": meta_nac["metodo"] + "; 15-19 partido en 18 con la ECP 2026"},
        )
    )
    out.append(
        _largo(
            esp_ext(nac.filter(pl.col("variable") == "nacionalidad_grupo")),
            ["nacionalidad_esp_ext", "edad_5"],
            "nacionalidad_edad",
            meta_nac,
        )
    )
    out.append(
        _largo(
            nacimiento_nacionalidad(),
            ["nacido_fuera", "nacionalidad_esp_ext"],
            "nacimiento_nacionalidad",
            {
                "fuente": "ecp: tabla 60129 + colectivos + censo_anual_micro_demograficas "
                "(exhaustivo)",
                "edicion": "2026-01-01 (nacionalidad); 2025-01-01 (nacidos fuera)",
                "metodo": "proporción de nacidos fuera de 2025 por provincia × sexo × edad_5 × "
                "nacionalidad sobre las celdas de la ECP 2026 (D-049)",
            },
        )
    )
    out += electorales_provincia()
    estructuras = [
        (
            fuentes.estudios,
            "edad_estudios",
            "estudios_3",
            "66601",
            "2024-01-01",
            [
                ("estudios_edad", ["estudios_3", "edad_estudios"]),
                ("estudios_sexo_edad", ["estudios_3", "sexo", "edad_estudios"]),
            ],
        ),
        (
            actividad_epa,
            "edad_actividad",
            "relacion_actividad",
            "67128",
            "2024-01-01",
            [
                ("actividad_sexo", ["relacion_actividad", "sexo"]),
                ("actividad_edad", ["relacion_actividad", "edad_actividad"]),
            ],
        ),
        (
            sin_estudios,
            "edad_estudios",
            "sin_estudios",
            "66601",
            "2024-01-01",
            [("sin_estudios_edad", ["sin_estudios", "edad_estudios"])],
        ),
        (
            fuentes.estado_civil,
            "edad_estado_civil",
            "estado_civil",
            "76291",
            "2024-01-01",
            [("estado_civil_edad", ["estado_civil", "edad_estado_civil"])],
        ),
        (
            fuentes.urbanizacion,
            "edad_urbanizacion",
            "grado_urbanizacion",
            "79341",
            "2025-01-01",
            [("urbanizacion", ["grado_urbanizacion"])],
        ),
    ]
    for fn, gk, var, tabla, ed, objetivos in estructuras:
        e = estructura(fn, gk).rename({"categoria": var})
        meta = {
            "fuente": f"censo_anual_tablas: tabla {tabla} (estructura) + ecp: tabla 59589",
            "edicion": f"{ed} (estructura); 2026-01-01 (efectivos)",
            "metodo": f"cuotas de {ed[:4]} por provincia × sexo × {gk} sobre la ECP 2026",
        }
        if fn is actividad_epa:
            meta = {
                "fuente": "censo_anual_tablas: tabla 67128 (reparto) + epa: 2T 2026, microdatos "
                "(ocupados, parados, inactivos) + ecp: tabla 59589",
                "edicion": "2024-01-01 (reparto); 2026-T2 (EPA); 2026-01-01 (efectivos)",
                "metodo": "estados de la EPA por CCAA × sexo × tramo (contraídos a una previa "
                "de 200 personas); dentro de cada estado, cuotas del Censo Anual 2024 por "
                "provincia × sexo × edad_actividad; sobre la ECP 2026 (D-046 A2)",
            }
        for obj, variables in objetivos:
            out.append(_largo(e, variables, obj, meta))
        if fn is actividad_epa:
            # Calibrado por tramos de la EPA: suma de los grupos quinquenales ya reescalados, así
            # que es coherente con actividad_edad y actividad_sexo (G3.2)
            out.append(
                _largo(
                    a_tramos(e),
                    ["relacion_actividad", "sexo", "edad_tramo_epa"],
                    "actividad_tramo",
                    meta,
                )
            )
    hog = pl.read_parquet(INTERIM_DIR / "ecp_hogares.parquet").rename({"hogares": "valor"})
    out.append(
        _largo(
            hog,
            ["tamano_hogar_4"],
            "tamano_hogar",
            {"fuente": "ecp: tabla 60133", "edicion": "2026-01-01", "metodo": "exacto"},
        )
    )
    tipo, det = tipo_hogar()
    meta_h = {
        "fuente": "censo2021_micro_hogares (estructura) + ecp: tabla 60133",
        "edicion": "2021 (estructura); 2026-01-01 (hogares por tamaño)",
        "metodo": "cuotas del Censo 2021 por provincia × tamaño sobre los hogares ECP 2026",
    }
    out.append(_largo(tipo, ["tipo_hogar", "tamano_hogar_4"], "tipo_hogar", meta_h))
    out.append(_largo(det, ["tipo_hogar", "edad_4"], "tipo_hogar_edad4_ref", meta_h))
    out.append(
        _largo(
            tamano_municipio(),
            ["tamano_municipio"],
            "tamano_municipio",
            {
                "fuente": "padron_continuo: tabla 29005 + ecp: tabla 59589",
                "edicion": "2025-01-01 (municipios); 2026-01-01 (efectivos)",
                "metodo": "cuotas de 2025 por provincia sobre la ECP 2026",
            },
        )
    )
    prov = (
        base.group_by("provincia")
        .agg(pl.col("n").sum().alias("valor"))
        .with_columns(pl.col("provincia").alias("p"))
    )
    out.append(
        _largo(
            prov.select("provincia", pl.col("p").alias("provincia_obj"), "valor").rename(
                {"provincia_obj": "provincia_x"}
            ),
            ["provincia_x"],
            "provincia_si_calibra_ccaa",
            {"fuente": "ecp: tabla 59589", "edicion": "2026-01-01", "metodo": "exacto"},
        ).with_columns(pl.col("clave").str.replace("provincia_x=", "provincia="))
    )
    res = pl.concat(out)
    out.append(
        _largo(
            trabajo_nacionalidad(res),
            ["trabaja", "nacionalidad_esp_ext", "edad_tramo_epa"],
            "trabajo_nacionalidad",
            {
                "fuente": "epa: 2T 2026, microdatos + objetivos actividad_tramo y "
                "nacionalidad_edad + ecp: tablas 59589 y 60129",
                "edicion": "2026-T2 (EPA); 2026-01-01 (efectivos)",
                "metodo": "ocupados de actividad_tramo repartidos entre españoles y extranjeros "
                "de nacionalidad_edad con las tasas de empleo de la EPA por comunidad × "
                "nacionalidad × tramo, contraídas a la nacional (D-050)",
            },
        )
    )
    return pl.concat(out).select(COLUMNAS).sort("provincia", "objetivo", "clave")


def tasas_empleo_nacionalidad() -> pl.DataFrame:
    """Tasa de empleo (ocupados / 16+ sin NC) de la EPA 2T 2026 por comunidad × nacionalidad
    española o extranjera × tramo, contraída hacia la nacional de su nacionalidad y tramo con
    `PESO_PREVIO` personas (D-050)."""
    e = pl.read_parquet(INTERIM_DIR / "epa.parquet").filter(
        (pl.col("edad_grupo_epa") >= "16") & ~pl.col("relacion_actividad").is_in(["NC", "NP"])
    )
    e = e.with_columns(
        _tramo(pl.col("edad_grupo_epa").cast(pl.Int32)),
        (pl.col("relacion_actividad") == "ocupado").cast(pl.Float64).alias("_o"),
    )
    k = ["nacionalidad_esp_ext", "tramo"]
    nac = e.group_by(k).agg(
        ((pl.col("_o") * pl.col("peso")).sum() / pl.col("peso").sum()).alias("rn")
    )
    cc = e.group_by("ccaa", *k).agg(
        ((pl.col("_o") * pl.col("peso")).sum() / pl.col("peso").sum()).alias("r"),
        pl.len().alias("n"),
    )
    # Todas las comunidades × nacionalidad × tramo: sin muestra en la EPA (n = 0), la nacional
    from sinpop.harmonize.core import ccaa_de_provincia

    todas = pl.DataFrame({"ccaa": sorted(set(ccaa_de_provincia().values()))}).join(nac, how="cross")
    return (
        todas.join(cc, on=["ccaa", *k], how="left")
        .with_columns(pl.col("n").fill_null(0), pl.col("r").fill_null(0.0))
        .select(
            "ccaa",
            *k,
            (
                (pl.col("n") * pl.col("r") + PESO_PREVIO * pl.col("rn"))
                / (pl.col("n") + PESO_PREVIO)
            ).alias("tasa"),
        )
    )


def trabajo_nacionalidad(res: pl.DataFrame) -> pl.DataFrame:
    """Ocupados y no ocupados por nacionalidad española/extranjera y tramo de la EPA (D-050).

    Coherente por construcción con los objetivos calibrados: los ocupados de cada provincia y
    tramo son los de `actividad_tramo`; los extranjeros, los de `nacionalidad_edad` (el grupo
    15-19 se parte con la proporción de 16-19 de la ECP por edad simple); el reparto de los
    ocupados entre españoles y extranjeros sigue sus tasas de empleo de la EPA. Menores de 16:
    no procede (NP)."""
    from sinpop.harmonize.core import ccaa_de_provincia

    etiqueta = dict(zip([str(t) for t in TRAMOS_EPA], etiquetas(TRAMOS_EPA)[1:], strict=True))
    np_tramo = etiquetas(TRAMOS_EPA)[0]
    a = res.filter(pl.col("objetivo") == "actividad_tramo").with_columns(
        pl.col("clave").str.extract(r"relacion_actividad=([^;]+)").alias("c"),
        pl.col("clave").str.extract(r"edad_tramo_epa=([^;]+)").alias("t"),
    )
    tot = a.group_by("provincia", "t").agg(
        pl.col("valor").sum().alias("total"),
        pl.col("valor").filter(pl.col("c") == "ocupado").sum().alias("ocupados"),
    )
    ecp = pl.read_parquet(INTERIM_DIR / "ecp_total.parquet")
    p16 = (
        ecp.filter(pl.col("edad").is_between(15, 19))
        .group_by("provincia")
        .agg(
            (
                pl.col("personas").filter(pl.col("edad") >= 16).sum() / pl.col("personas").sum()
            ).alias("p16")
        )
    )
    n = (
        res.filter(pl.col("objetivo") == "nacionalidad_edad")
        .with_columns(
            pl.col("clave")
            .str.extract(r"nacionalidad_esp_ext=([^;]+)")
            .alias("nacionalidad_esp_ext"),
            pl.col("clave").str.extract(r"edad_5=(\d+)").cast(pl.Int32).alias("lo"),
        )
        .filter(pl.col("nacionalidad_esp_ext") == "extranjera")
        .join(p16, on="provincia")
    )
    adultos = n.filter(pl.col("lo") >= 15).with_columns(
        pl.when(pl.col("lo") == 15)
        .then(pl.col("valor") * pl.col("p16"))
        .otherwise(pl.col("valor"))
        .alias("valor"),
        _tramo(pl.col("lo").clip(16)),
    )
    ext = (
        adultos.with_columns(pl.col("tramo").replace_strict(etiqueta).alias("t"))
        .group_by("provincia", "t")
        .agg(pl.col("valor").sum().alias("ext"))
    )
    ext_np = (
        n.group_by("provincia")
        .agg(pl.col("valor").sum().alias("_tot"))
        .join(ext.group_by("provincia").agg(pl.col("ext").sum().alias("_ad")), on="provincia")
        .select(
            "provincia", pl.lit(np_tramo).alias("t"), (pl.col("_tot") - pl.col("_ad")).alias("ext")
        )
    )
    tasas = tasas_empleo_nacionalidad().with_columns(
        pl.col("tramo").replace_strict(etiqueta).alias("t")
    )
    cc = ccaa_de_provincia()
    d = (
        tot.join(pl.concat([ext, ext_np]), on=["provincia", "t"], how="left")
        .with_columns(
            pl.col("ext").fill_null(0.0), pl.col("provincia").replace_strict(cc).alias("ccaa")
        )
        .with_columns((pl.col("total") - pl.col("ext")).alias("esp"))
        .join(
            tasas.filter(pl.col("nacionalidad_esp_ext") == "extranjera").select(
                "ccaa", "t", pl.col("tasa").alias("re")
            ),
            on=["ccaa", "t"],
            how="left",
        )
        .join(
            tasas.filter(pl.col("nacionalidad_esp_ext") == "espanola").select(
                "ccaa", "t", pl.col("tasa").alias("rs")
            ),
            on=["ccaa", "t"],
            how="left",
        )
        .with_columns(
            pl.when(pl.col("re").is_null())
            .then(0.0)
            .otherwise(
                pl.col("ocupados")
                * pl.col("re")
                * pl.col("ext")
                / (pl.col("re") * pl.col("ext") + pl.col("rs") * pl.col("esp"))
            )
            .clip(0.0, pl.col("ext"))
            .fill_nan(0.0)
            .alias("oe")
        )
        .with_columns((pl.col("ocupados") - pl.col("oe")).alias("os"))
    )
    filas = []
    for nac, total, ocup in (("extranjera", "ext", "oe"), ("espanola", "esp", "os")):
        si = d.select(
            "provincia", "t", pl.lit(nac).alias("nacionalidad_esp_ext"), pl.col(ocup).alias("valor")
        )
        no = d.select(
            "provincia",
            "t",
            pl.lit(nac).alias("nacionalidad_esp_ext"),
            (pl.col(total) - pl.col(ocup)).alias("valor"),
        )
        filas += [
            si.filter(pl.col("t") != np_tramo).with_columns(pl.lit("si").alias("trabaja")),
            no.with_columns(
                pl.when(pl.col("t") == np_tramo)
                .then(pl.lit("NP"))
                .otherwise(pl.lit("no"))
                .alias("trabaja")
            ),
        ]
    return (
        pl.concat(filas, how="diagonal_relaxed")
        .rename({"t": "edad_tramo_epa"})
        .select("provincia", "trabaja", "nacionalidad_esp_ext", "edad_tramo_epa", "valor")
    )


def electorales_provincia() -> list[pl.DataFrame]:
    """Objetivos electorales por provincia (generales y autonómicas)."""
    from sinpop.targets import electorales as el

    opc, vot = el.generales_municipios()
    el.comprobar_generales(opc)
    meta = {
        "fuente": "infoelectoral_resultados: hojas municipales del Congreso 2023 (Interior)",
        "edicion": "2023-07-23 (escrutinio provisional, residentes)",
        "metodo": "suma de municipios; familias de partidos.yaml (D-030, D-032)",
    }
    out = [
        _largo(
            opc.rename({"opcion": "recuerdo_voto_generales"}),
            ["recuerdo_voto_generales"],
            "voto_generales_2023",
            meta,
        ),
        _largo(
            opc.rename({"opcion": "recuerdo_voto_generales"}),
            ["recuerdo_voto_generales", "municipio"],
            "voto_generales_2023_municipio",
            meta,
        ),
        _largo(
            el.generales_candidaturas(opc, vot),
            ["candidatura_generales_2023"],
            "voto_generales_2023_candidatura",
            meta,
        ),
    ]
    aut = el.autonomicas_circunscripciones()
    out.append(
        _largo(
            aut.rename({"opcion": "recuerdo_voto_autonomicas"}),
            ["recuerdo_voto_autonomicas"],
            "voto_autonomicas",
            {
                "fuente": "resultados_autonomicas: boletines oficiales de cada comunidad",
                "edicion": "última elección de cada comunidad (2023–2026; elecciones.yaml)",
                "metodo": "suma de circunscripciones; abstención = electores − válidos − nulos; "
                "Aragón sin electores publicados (sin abstención); familias D-030",
            },
        )
    )
    return out


# --------------------------------------------------------------------------- territorios


def provincias_de(territorio: str) -> list[str]:
    """Provincias de ES, CCAA:XX o PROV:XX (códigos INE)."""
    from sinpop.harmonize.core import ccaa_de_provincia

    ccaa = ccaa_de_provincia()
    if territorio == "ES":
        return sorted(ccaa)
    tipo, _, cod = territorio.partition(":")
    if tipo == "CCAA":
        out = sorted(p for p, c in ccaa.items() if c == cod)
    elif tipo == "PROV":
        out = [cod] if cod in ccaa else []
    else:
        raise ValueError(f"territorio no admitido aquí: {territorio}")
    if not out:
        raise ValueError(f"territorio sin provincias: {territorio}")
    return out


def agregar(prov: pl.DataFrame, territorio: str) -> pl.DataFrame:
    """Suma los objetivos de las provincias del territorio (los metadatos son comunes)."""
    ps = provincias_de(territorio)
    meta = [c for c in COLUMNAS if c not in ("provincia", "valor")]
    return (
        prov.filter(pl.col("provincia").is_in(ps))
        .sort("objetivo", "clave", "provincia")
        .group_by(meta, maintain_order=True)
        .agg(pl.col("valor").sum().round(6))
        .with_columns(pl.lit(territorio).alias("territorio"))
        .select("territorio", *meta[:5], "valor", *meta[5:])
        .sort("objetivo", "clave")
    )
