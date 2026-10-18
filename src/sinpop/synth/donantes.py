"""Donantes y matriz de calibración (F4, tarea 1; docs/03 §2.1; D-021, D-036, D-038).

Unidades de calibración:

- **Hogares** completos de la muestra del Censo 2021 (viviendas familiares), con sus personas.
- **Colectivos** (D-021, opción B): la muestra del Censo 2021 no tiene establecimientos
  colectivos. Cada residente en colectivos se representa con una persona donante «parecida»
  (misma provincia, sexo y edad quinquenal) tomada como unidad individual. La selección es
  determinista y su peso inicial reparte el objetivo de colectivos de la celda. Sus atributos
  distintos de edad, sexo y territorio se marcan como `modelada`; los del hogar no proceden.

La matriz de calibración tiene una fila por unidad y una columna por celda de objetivo
(«objetivo|clave»): número de personas (u hogares) de la unidad que caen en esa celda.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import polars as pl
from scipy import sparse

from sinpop import INTERIM_DIR
from sinpop.targets.edades import agrupar, cortes

PERSONAS = INTERIM_DIR / "censo2021_personas.parquet"

# Atributos de persona de los donantes que pasan a la población (P0 y P1 del Censo 2021).
ATRIBUTOS_PERSONA = [
    "edad",
    "sexo",
    "nacionalidad_grupo",
    "nacionalidad_top",
    "pais_nacimiento_grupo",
    "anio_llegada_espana",
    "estado_civil",
    "nivel_estudios",
    "estudios_3",
    "relacion_actividad",
    "ocupacion",
    "sector_actividad",
    "situacion_profesional",
]
ATRIBUTOS_HOGAR = [
    "tamano_hogar",
    "tipo_hogar",
    "n_personas_hogar",
    "n_menores_hogar",
    "n_mayores_65_hogar",
    "n_mayores_80_hogar",
    "tenencia_censo",
]
ATRIBUTOS_TERRITORIO = ["provincia", "ccaa", "municipio", "tamano_municipio", "grado_urbanizacion"]

# D-038: la relación con la actividad se publica para 16 y más años (Censo Anual, tabla 67128;
# EPA), y nadie menor de 16 puede figurar como ocupado (V-REGLAS). Los microdatos del Censo 2021
# la dan desde los 15: a los de 15 años se les pone NP en estas variables.
EDAD_MIN_ACTIVIDAD = 16
VARIABLES_ACTIVIDAD = [
    "relacion_actividad",
    "ocupacion",
    "sector_actividad",
    "situacion_profesional",
]

# Universos de los objetivos que se calibran con estas unidades (los electorales son de F8B).
UNIVERSOS_PERSONA = {"residentes", "viviendas_familiares", "colectivos"}


def alinear_universos(p: pl.DataFrame) -> pl.DataFrame:
    """D-038: variables de actividad NP por debajo de 16 años."""
    return p.with_columns(
        [
            pl.when(pl.col("edad") < EDAD_MIN_ACTIVIDAD)
            .then(pl.lit("NP"))
            .otherwise(pl.col(v))
            .alias(v)
            for v in VARIABLES_ACTIVIDAD
        ]
    )


def derivadas(p: pl.DataFrame) -> pl.DataFrame:
    """Variables de los objetivos que no están en los donantes: grupos de edad de cada tabla,
    tamaño del hogar en 4 grupos, nacionalidad española o extranjera y mayoría de edad."""
    c = cortes()
    return p.with_columns(
        *[agrupar(pl.col("edad"), v, k) for k, v in sorted(c.items())],
        pl.when(pl.col("tamano_hogar").is_in(["4", "5+"]))
        .then(pl.lit("4+"))
        .otherwise(pl.col("tamano_hogar"))
        .alias("tamano_hogar_4"),
        pl.when(pl.col("nacionalidad_grupo") == "espanola")
        .then(pl.lit("espanola"))
        .otherwise(pl.lit("extranjera"))
        .alias("nacionalidad_esp_ext"),
        # D-049
        pl.when(pl.col("nivel_estudios").is_in(["analfabetos", "primaria_incompleta"]))
        .then(pl.lit("si"))
        .when(pl.col("nivel_estudios").is_in(["NP", "NC", "NS"]))
        .then(pl.col("nivel_estudios"))
        .otherwise(pl.lit("no"))
        .alias("sin_estudios"),
        # D-050: ocupado, parado o inactivo (16+), para la actividad por nacionalidad
        pl.when(pl.col("relacion_actividad").is_in(["NP", "ocupado", "parado"]))
        .then(pl.col("relacion_actividad"))
        .otherwise(pl.lit("inactivo"))
        .alias("actividad_3"),
        pl.when(pl.col("pais_nacimiento_grupo") == "espana")
        .then(pl.lit("no"))
        .when(pl.col("pais_nacimiento_grupo").is_in(["NC", "NS"]))
        .then(pl.lit("NC"))
        .otherwise(pl.lit("si"))
        .alias("nacido_fuera"),
    )


def hogares(provincias: list[str] | None = None) -> pl.DataFrame:
    """Personas de los hogares donantes (una fila por persona), ordenadas por hogar y orden."""
    cols = ["household_id", "norden", *ATRIBUTOS_PERSONA, "edad_5", "edad_4", "es_adulto"]
    cols += ["relacion_persona_ref", *ATRIBUTOS_HOGAR, *ATRIBUTOS_TERRITORIO, "peso"]
    lf = pl.scan_parquet(PERSONAS).select(cols)
    if provincias is not None:
        lf = lf.filter(pl.col("provincia").is_in(provincias))
    p = lf.sort("household_id", "norden").collect()
    p = derivadas(alinear_universos(p))
    return p.with_columns(pl.lit("vivienda_familiar").alias("tipo_residencia"))


def _orden_determinista(household_id: pl.Expr, norden: pl.Expr) -> pl.Expr:
    """Clave pseudoaleatoria fija (no depende de la versión de polars ni de la semilla)."""
    x = household_id.cast(pl.UInt64) * 2654435761 + norden.cast(pl.UInt64) * 40503
    return (x * 6364136223846793005 + 1442695040888963407) % (1 << 61)


def colectivos(objetivos: pl.DataFrame, personas: pl.DataFrame) -> pl.DataFrame:
    """Unidades del módulo de colectivos.

    `objetivos`: provincia, sexo, edad_5, valor (residentes en colectivos por celda).
    En cada celda con valor > 0 se toman n = máx(5, round(valor / 10)) personas donantes de la
    misma provincia, sexo y edad_5 (peso inicial parecido al de los hogares del Censo, 10), en
    un orden pseudoaleatorio fijo; si la provincia no tiene bastantes, se completan con donantes
    de la misma comunidad y luego de España. Peso inicial: valor / n.
    """
    obj = objetivos.filter(pl.col("valor") > 0).sort("provincia", "sexo", "edad_5")
    obj = obj.with_columns(
        pl.max_horizontal(pl.lit(5), (pl.col("valor") / 10).round(0).cast(pl.Int64)).alias("n")
    )
    from sinpop.harmonize.core import ccaa_de_provincia

    ccaa_de = ccaa_de_provincia()
    # Solo las columnas de la selección (memoria); las filas elegidas recuperan después el resto.
    claves = ["household_id", "norden", "sexo", "edad_5", "provincia", "ccaa"]
    cand = (
        personas.select(claves)
        .with_columns(_orden_determinista(pl.col("household_id"), pl.col("norden")).alias("_orden"))
        .sort("_orden", "household_id", "norden")
    )
    grupos = cand.partition_by("sexo", "edad_5", as_dict=True)
    elegidos = []
    for prov, sexo, edad5, valor, n in obj.select(
        "provincia", "sexo", "edad_5", "valor", "n"
    ).iter_rows():
        base = grupos[(sexo, edad5)]
        tomados = []
        for nivel, f in (
            ("provincia", pl.col("provincia") == prov),
            ("ccaa", pl.col("ccaa") == ccaa_de[prov]),
            ("espana", pl.lit(True)),
        ):
            faltan = n - sum(t.height for t in tomados)
            if faltan <= 0:
                break
            ya = pl.concat(tomados) if tomados else base.head(0)
            sel = base.filter(f).join(
                ya.select("household_id", "norden"), on=["household_id", "norden"], how="anti"
            )
            tomados.append(
                sel.head(faltan).with_columns(pl.lit(nivel).alias("colectivo_donante_nivel"))
            )
        t = pl.concat(tomados)
        if t.height < n:
            raise ValueError(f"colectivos {prov} {sexo} {edad5}: solo {t.height} donantes de {n}")
        elegidos.append(
            t.with_columns(
                pl.lit(prov).alias("provincia_destino"),
                pl.lit(valor / n).alias("peso_inicial"),
            )
        )
    out = (
        pl.concat(elegidos)
        .drop("_orden")
        .join(
            personas.drop("sexo", "edad_5", "provincia", "ccaa"),
            on=["household_id", "norden"],
            how="left",
            maintain_order="left",
        )
    )
    # El colectivo reside en la provincia de destino; los atributos del hogar no proceden.
    ccaa_dest = pl.col("provincia_destino").replace_strict(ccaa_de)
    nulos = {
        "relacion_persona_ref": "NP",
        "tamano_hogar": "NP",
        "tipo_hogar": "NP",
        "tamano_hogar_4": "NP",
        "tenencia_censo": "NP",
    }
    return out.with_columns(
        pl.col("provincia_destino").alias("provincia"),
        ccaa_dest.alias("ccaa"),
        *[pl.lit(v).alias(k) for k, v in nulos.items()],
        *[
            pl.lit(None, dtype=out.schema[c]).alias(c)
            for c in (
                "n_personas_hogar",
                "n_menores_hogar",
                "n_mayores_65_hogar",
                "n_mayores_80_hogar",
            )
        ],
        pl.lit("establecimiento_colectivo").alias("tipo_residencia"),
    ).drop("provincia_destino")


def objetivos_colectivos(provincias: list[str]) -> pl.DataFrame:
    """Residentes en colectivos por provincia, sexo y edad_5 (objetivo `edad5_sexo_colectivos`
    de cada provincia, F3)."""
    from sinpop.targets import run

    out = []
    for pr in provincias:
        o = run.leer(f"PROV:{pr}").filter(pl.col("objetivo") == "edad5_sexo_colectivos")
        out.append(o.select(pl.lit(pr).alias("provincia"), "clave", "valor"))
    o = pl.concat(out).with_columns(
        pl.col("clave").str.extract(r"edad_5=([^;]+)").alias("edad_5"),
        pl.col("clave").str.extract(r"sexo=([^;]+)").alias("sexo"),
    )
    return o.select("provincia", "sexo", "edad_5", "valor")


def _valor(var: str) -> pl.Expr:
    if var == "es_adulto":
        return pl.when(pl.col("es_adulto")).then(pl.lit("si")).otherwise(pl.lit("no"))
    return pl.col(var).cast(pl.Utf8)


def clave(variables: list[str]) -> pl.Expr:
    """Clave «var=val;var=val» igual a la de los ficheros de objetivos (F3)."""
    partes = []
    for i, v in enumerate(variables):
        if i:
            partes.append(pl.lit(";"))
        partes += [pl.lit(f"{v}="), _valor(v)]
    return pl.concat_str(partes)


@dataclass
class Unidades:
    """Unidades de calibración y sus personas."""

    personas: pl.DataFrame  # una fila por persona; `unidad` = índice de su unidad
    unidades: pl.DataFrame  # una fila por unidad: unidad, tipo, household_id, norden, d, n_personas


def _ordenado(df: pl.DataFrame) -> bool:
    u, n = df["unidad"], df["norden"].cast(pl.Int64)
    du = u.diff().fill_null(1)
    return bool((du >= 0).all() and ((du > 0) | (n.diff().fill_null(1) > 0)).all())


def unidades(personas_hogar: pl.DataFrame, personas_col: pl.DataFrame) -> Unidades:
    h = personas_hogar.with_columns(pl.lit("hogar").alias("tipo_unidad"))
    h = h.with_columns(pl.col("household_id").rank("dense").cast(pl.Int64).sub(1).alias("unidad"))
    nh = int(h["unidad"].max()) + 1 if h.height else 0
    c = personas_col.sort("provincia", "sexo", "edad_5", "household_id", "norden").with_columns(
        pl.lit("colectivo").alias("tipo_unidad"),
        (pl.int_range(pl.len()) + nh).cast(pl.Int64).alias("unidad"),
    )
    h = h.with_columns(
        pl.col("peso").alias("peso_inicial"),
        pl.lit(None, dtype=pl.Utf8).alias("colectivo_donante_nivel"),
    )
    cols = [c_ for c_ in h.columns if c_ in c.columns]
    # `h` ya viene ordenado por hogar y orden (`hogares`) y `unidad` sigue ese orden; `c`, por
    # unidad: la unión ya está ordenada y no hace falta otra copia ordenada (memoria, España).
    h = h.sort("unidad", "norden") if not _ordenado(h) else h
    p = pl.concat([h.select(cols), c.select(cols)], how="vertical_relaxed", rechunk=False)
    p = p.with_columns(pl.col("unidad").set_sorted())
    u = (
        p.group_by("unidad", maintain_order=True)
        .agg(
            pl.col("tipo_unidad").first(),
            pl.col("household_id").first(),
            pl.col("norden").first(),
            pl.col("peso_inicial").first().alias("d"),
            pl.len().alias("n_personas"),
            pl.col("provincia").first(),
        )
        .sort("unidad")
    )
    return Unidades(personas=p, unidades=u)


@dataclass
class Matriz:
    X: sparse.csr_matrix  # unidades × celdas
    celdas: pl.DataFrame  # j, objetivo, clave, unidad_obj, universo, valor
    d: np.ndarray
    ceros: pl.DataFrame  # celdas fuera de la calibración: objetivo 0 o sin donantes (motivo)


def objetivos_calibrables(obj: pl.DataFrame, municipios: bool = False) -> pl.DataFrame:
    """Objetivos `calibrar` de persona (residentes, viviendas familiares, colectivos) y de hogar.
    Los electorales se calibran en F8B, sobre el recuerdo de voto. `ambito: municipios` solo en
    territorios por municipios (y entonces sustituye a estudios_edad, D-036)."""
    from sinpop.config import load_config

    cfg = load_config("targets.yaml")
    ambito = {o.id: o.ambito for o in cfg.calibrar}  # type: ignore[attr-defined]
    if municipios:
        ids = [
            i
            for i in ambito
            if i
            not in (
                "estudios_edad",
                "actividad_tramo",
                "sin_estudios_edad",
                "actividad_nacionalidad",
            )
        ]
    else:
        ids = [i for i, a in ambito.items() if a != "municipios"]
    o = obj.filter(
        (pl.col("uso") == "calibrar")
        & pl.col("objetivo").is_in(ids)
        & pl.col("universo").is_in([*UNIVERSOS_PERSONA, "hogares"])
    )
    return o.sort("objetivo", "clave")


def variables_de(objetivo: str) -> list[str]:
    from sinpop.config import load_config

    cfg = load_config("targets.yaml")
    for o in [*cfg.calibrar, *cfg.reservar]:  # type: ignore[attr-defined]
        if o.id == objetivo:
            return list(o.variables)
    raise KeyError(objetivo)


def en_universo(
    personas: pl.DataFrame, universo: str, unidad_obj: str, columnas: list[str] | None = None
) -> pl.DataFrame:
    """Filas que cuentan para un objetivo: personas del universo o, si el objetivo es de hogar,
    una fila por hogar (su persona de referencia). Vale para donantes y para la población."""
    p = personas
    if columnas is not None:  # menos memoria: solo las columnas que se van a usar
        p = p.select(sorted({*columnas, "tipo_residencia", "relacion_persona_ref"}))
    if universo == "viviendas_familiares" or unidad_obj == "hogar":
        p = p.filter(pl.col("tipo_residencia") == "vivienda_familiar")
    elif universo == "colectivos":
        p = p.filter(pl.col("tipo_residencia") == "establecimiento_colectivo")
    elif universo != "residentes":
        raise ValueError(f"universo no admitido: {universo}")
    if unidad_obj == "hogar":
        p = p.filter(pl.col("relacion_persona_ref") == "persona_referencia")
    return p


def recuentos(
    personas: pl.DataFrame, objetivos: pl.DataFrame, peso: str | None = None
) -> pl.DataFrame:
    """Recuento (ponderado si se da `peso`) de la población en cada celda de los objetivos.
    Devuelve objetivo, clave, valor (objetivo oficial) y sintetico; las claves de la población
    que no están en los objetivos aparecen con valor 0 (y se detectan en la validación)."""
    out = []
    for (objetivo, unidad_obj, universo), g in objetivos.group_by(
        "objetivo", "unidad", "universo", maintain_order=True
    ):
        w = pl.col(peso) if peso else pl.lit(1.0)
        vs = variables_de(objetivo)
        s = (
            en_universo(personas, universo, unidad_obj, [*vs, *([peso] if peso else [])])
            .group_by(clave(vs).alias("clave"))
            .agg(w.sum().cast(pl.Float64).alias("sintetico"))
        )
        j = g.select("objetivo", "clave", "valor").join(s, on="clave", how="full", coalesce=True)
        out.append(
            j.with_columns(
                pl.lit(objetivo).alias("objetivo"),
                pl.col("valor").fill_null(0.0),
                pl.col("sintetico").fill_null(0.0),
            )
        )
    return pl.concat(out).sort("objetivo", "clave")


MAX_SIN_DONANTES = 0.001


def _repartir(celdas: pl.DataFrame, sd: np.ndarray, usadas: np.ndarray) -> pl.DataFrame:
    """Reparte el valor de las celdas `sd` entre las celdas con donantes de su mismo objetivo y
    resto de clave, en proporción a su valor."""
    resto = pl.col("clave").str.split(";").list.slice(1).list.join(";")
    c = celdas.with_columns(
        resto.alias("_resto"), pl.Series("_sd", sd), pl.Series("_usada", usadas)
    )
    g = ["objetivo", "_resto"]
    receptora = pl.col("_usada") & ~pl.col("_sd") & (pl.col("valor") > 0)
    c = c.with_columns(
        pl.when(pl.col("_sd")).then(pl.col("valor")).otherwise(0.0).sum().over(g).alias("_extra"),
        pl.when(receptora).then(pl.col("valor")).otherwise(0.0).sum().over(g).alias("_base"),
    )
    return c.with_columns(
        pl.when(receptora & (pl.col("_base") > 0))
        .then(pl.col("valor") * (1 + pl.col("_extra") / pl.col("_base")))
        .otherwise(pl.col("valor"))
        .alias("valor")
    ).drop("_resto", "_sd", "_usada", "_extra", "_base")


def matriz(
    u: Unidades, obj: pl.DataFrame, fusion: dict[str, dict[str, str]] | None = None
) -> Matriz:
    """Matriz dispersa unidades × celdas. Falla si una persona cae en una clave que no está en
    los objetivos (código fuera de dominio) o si una celda con valor > 0 no tiene donantes.
    `fusion`: objetivo → {clave original: clave fusionada} (celdas fusionadas del bloque)."""
    fusion = fusion or {}
    celdas = (
        obj.select("objetivo", "clave", "unidad", "universo", "valor")
        .rename({"unidad": "unidad_obj"})
        .sort("objetivo", "clave")
        .with_row_index("j")
    )
    trip = []
    for (objetivo, unidad_obj, universo), g in celdas.group_by(
        "objetivo", "unidad_obj", "universo", maintain_order=True
    ):
        k = (
            en_universo(u.personas, universo, unidad_obj, [*variables_de(objetivo), "unidad"])
            .select("unidad", clave(variables_de(objetivo)).alias("clave"))
            .with_columns(pl.col("clave").replace(fusion.get(objetivo, {})))
            .join(g.select("clave", "j"), on="clave", how="left")
        )
        fuera = k.filter(pl.col("j").is_null())
        if fuera.height:
            ej = fuera["clave"].value_counts().sort("count", descending=True).head(5).rows()
            raise ValueError(f"{objetivo}: {fuera.height} personas con claves sin objetivo: {ej}")
        trip.append(k.group_by("unidad", "j").agg(pl.len().alias("x")))
    t = pl.concat(trip).sort("unidad", "j")
    n, m = u.unidades.height, celdas.height
    X = sparse.csr_matrix(
        (t["x"].to_numpy().astype(float), (t["unidad"].to_numpy(), t["j"].to_numpy())),
        shape=(n, m),
    )
    d = u.unidades["d"].to_numpy().astype(float)
    vacias = celdas.filter((pl.col("valor") > 0) & ~pl.col("j").is_in(t["j"].unique().implode()))
    # Celdas sin ningún donante posible (ni tras la ampliación de donantes): si son muy pequeñas
    # (≤ 0,1 % de su objetivo), salen de la calibración, su valor se reparte entre las demás
    # categorías del mismo cruce (mismas claves salvo la primera variable) para conservar los
    # totales y quedan registradas (D-049; p. ej. jubilados de 25-34 años en Ceuta); si no, la
    # construcción se detiene.
    tot = celdas.group_by("objetivo").agg(pl.col("valor").sum().alias("_t"))
    vacias = vacias.join(tot, on="objetivo").with_columns(
        (pl.col("valor") <= MAX_SIN_DONANTES * pl.col("_t")).alias("_peq")
    )
    if vacias.filter(~pl.col("_peq")).height:
        raise ValueError(
            "celdas con objetivo > 0 sin donantes: "
            f"{vacias.filter(~pl.col('_peq')).select('objetivo', 'clave', 'valor').rows()}"
        )
    sin_donantes = vacias["j"].to_numpy()
    # Ceros estructurales (p. ej. estudios superiores a los 15-19 años): sin donantes, se quitan
    # de la calibración; con donantes, el objetivo es incompatible con los datos y se detiene.
    usadas = np.asarray((X != 0).sum(axis=0)).ravel() > 0
    ceros = celdas["valor"].to_numpy() <= 0
    if np.any(ceros & usadas):
        malas = celdas.filter(pl.Series(ceros & usadas)).select("objetivo", "clave").rows()
        raise ValueError(f"celdas con objetivo 0 y donantes: {malas}")
    sd = np.isin(np.arange(len(ceros)), sin_donantes)
    if sd.any():
        celdas = _repartir(celdas, sd, usadas)
    motivo = np.where(sd, "sin_donantes", "cero_estructural")
    ceros = ceros | sd
    keep = ~ceros
    celdas = celdas.with_columns(pl.Series("cero_estructural", ceros), pl.Series("motivo", motivo))
    return Matriz(
        X=sparse.csr_matrix(X[:, keep]),
        celdas=celdas.filter(~pl.col("cero_estructural")).drop("j").with_row_index("j"),
        d=d,
        ceros=celdas.filter(pl.col("cero_estructural")).select(
            "objetivo", "clave", "valor", "motivo"
        ),
    )
