"""Calibración de las unidades donantes a los objetivos de un territorio (F4 y F5; D-038, D-041).

**Bloques.** España se calibra como la unión de sus 19 comunidades: cada comunidad con sus
objetivos y sus donantes, de modo que la población nacional reproduce también cada comunidad y
el reparto por provincias queda como validación. Una comunidad, una provincia o una lista de
municipios es un único bloque.

**Donantes base del bloque** (`base_bloque`):

- comunidad o provincia: las unidades (hogares y colectivos) de sus provincias, locales;
- lista de municipios: los hogares de los municipios de la lista que el Censo 2021 identifica
  (los de más de 10.000 habitantes), locales; para los no identificados, los hogares sin
  municipio identificado de su provincia y clase de tamaño, con el peso inicial escalado por la
  parte de la población de esa clase y provincia que son los municipios de la lista (Padrón
  2025), no locales (nivel «misma provincia»); y los colectivos de esas provincias, con el peso
  escalado por la parte de la población de la provincia que es el territorio.

**Ampliación de celdas deficitarias** (docs/02 §5; `territories.yaml`). Una celda calibrada es
deficitaria si tiene menos de `min_donantes_celda` unidades base, o si su objetivo supera
`razon_max` veces su masa inicial (Σ personas × peso). Se añaden unidades de fuera de la base que
caen en la celda, recorriendo la jerarquía (misma provincia, misma comunidad con el mismo grado de
urbanización, comunidades parecidas, España), en un orden pseudoaleatorio fijo y excluyendo las
que caen en celdas con objetivo 0 del bloque. Si faltan unidades, se añaden con peso inicial
objetivo / `min_donantes_celda`; si falta masa, con su peso hasta que la razón baje a
`razon_objetivo`. Se reparten entre las provincias del bloque, pierden el municipio y no son
locales (V-DONANTES informa la proporción local).
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np
import polars as pl

from sinpop.synth import calibracion as C
from sinpop.synth import donantes as D

MIN_CELDA_NACIONALIDAD = 100


def _cfg():
    from sinpop.config import load_config

    return load_config("territories.yaml")


def bloques(territorio: str) -> list[str]:
    if territorio == "ES":
        from sinpop.harmonize.core import ccaa_de_provincia

        return [f"CCAA:{c}" for c in sorted(set(ccaa_de_provincia().values()))]
    return [territorio]


def provincias_bloque(b: str) -> list[str]:
    if b.startswith("MUNIS:"):
        from sinpop.targets import municipios as M

        ms = M.definicion(Path(b.split(":", 1)[1])).municipios
        return sorted({m[:2] for m in ms})
    from sinpop.targets.build import provincias_de

    return provincias_de(b)


@lru_cache(maxsize=32)
def ccaa_parecidas(ccaa: str) -> tuple[str, ...]:
    """Las comunidades más próximas a `ccaa` por la TVD media de sus objetivos de estructura."""
    from sinpop.harmonize.core import ccaa_de_provincia
    from sinpop.targets import run
    from sinpop.validate.metrics import tvd

    cfg = _cfg().ccaa_parecidas  # type: ignore[attr-defined]
    todas = sorted(set(ccaa_de_provincia().values()))

    def perfil(c: str) -> pl.DataFrame:
        o = run.leer(f"CCAA:{c}").filter(pl.col("objetivo").is_in(cfg.objetivos))
        return o.select("objetivo", "clave", "valor")

    ref = perfil(ccaa)
    dist = []
    for c in todas:
        if c == ccaa:
            continue
        j = ref.join(perfil(c), on=["objetivo", "clave"], how="full", coalesce=True).fill_null(0)
        d = [tvd(g["valor_right"], g["valor"]) for _, g in j.group_by("objetivo")]
        dist.append((sum(d) / len(d), c))
    return tuple(c for _, c in sorted(dist)[: cfg.numero])


@dataclass
class Calibrado:
    unidades: pl.DataFrame  # bloque, unidad (global), local, nivel, provincia, ccaa, d, w
    diagnosticos: dict[str, dict]
    ceros: pl.DataFrame
    ampliaciones: pl.DataFrame  # bloque, objetivo, clave, locales, razon_inicial, anadidas
    fusiones: pl.DataFrame  # bloque, objetivo, clave, fusionada_en


def _celdas_por_unidad(personas: pl.DataFrame, obj: pl.DataFrame) -> pl.DataFrame:
    """unidad, objetivo, clave y x (personas u hogares de la unidad en la celda)."""
    out = []
    for (objetivo, unidad_obj, universo), _ in obj.group_by(
        "objetivo", "unidad", "universo", maintain_order=True
    ):
        vs = [*D.variables_de(objetivo), "unidad"]
        k = D.en_universo(personas, universo, unidad_obj, vs).select(
            "unidad",
            pl.lit(objetivo).alias("objetivo"),
            D.clave(D.variables_de(objetivo)).alias("clave"),
        )
        out.append(k.group_by("unidad", "objetivo", "clave").agg(pl.len().alias("x")))
    return pl.concat(out)


MIN_INACTIVIDAD = 0.02
FACTOR_MAX = 5.0  # cotas de los factores de la calibración logit
FACTOR_MIN = 0.2
MARGEN = 1.25  # margen sobre las cotas: otras restricciones también tiran de las mismas unidades
OBJETIVOS_SOBRECOBERTURA = ("estado_civil_edad", "nacionalidad_top_edad")
MIN_NACIONALIDAD_EDAD = 2000  # por debajo, la nacionalidad se calibra sin la edad (D-050)
MAX_SIN_EDAD = 5  # intentos del último recurso de nacionalidad sin edad (D-050)


def fusionar(
    obj: pl.DataFrame,
    cobertura: pl.DataFrame | None = None,
    sin_edad: frozenset[str] = frozenset(),
    cobertura_nac: pl.DataFrame | None = None,
) -> tuple[pl.DataFrame, dict[str, dict[str, str]]]:
    """Funde con «otras_extranjeras» las nacionalidades cuyo objetivo en el bloque es menor que
    `MIN_CELDA_NACIONALIDAD` personas (p. ej. 7,6 ecuatorianos en Melilla): con tan pocos casos,
    los pocos hogares donantes locales pueden pesar más que el objetivo y la calibración acotada
    no tiene solución. La nacionalidad sigue calibrada por grupos (`nacionalidad`)."""
    obj, fusion = _fusionar_actividad(obj, cobertura)
    top = obj.filter(pl.col("objetivo") == "nacionalidad_top")
    otras = "nacionalidad_top=otras_extranjeras"
    pequena = pl.col("valor") < MIN_CELDA_NACIONALIDAD
    if cobertura_nac is not None:
        # Exceso de cobertura (D-050): los donantes del bloque, con el factor mínimo, pesan más
        # que el objetivo (p. ej. 9 hogares chinos para 123 chinos en Teruel)
        top = top.join(cobertura_nac, on="clave", how="left").with_columns(
            (pl.col("valor") / pl.col("valor").sum()).alias("_cuota")
        )
        pequena = pequena | (
            pl.col("cuota_local").fill_null(0.0) * FACTOR_MIN * MARGEN > pl.col("_cuota")
        )
    peq = top.filter(
        pequena & (pl.col("clave") != otras) & (pl.col("clave") != "nacionalidad_top=espanola")
    )
    top = top.select(obj.columns)
    mapa = {c: otras for c in peq["clave"]}
    if mapa:
        nuevo = (
            top.with_columns(pl.col("clave").replace(mapa))
            .group_by("clave", maintain_order=True)
            .agg(pl.all().exclude("valor").first(), pl.col("valor").sum())
            .select(obj.columns)
        )
        obj = pl.concat([obj.filter(pl.col("objetivo") != "nacionalidad_top"), nuevo]).sort(
            "objetivo", "clave"
        )
        fusion = fusion | {"nacionalidad_top": mapa}
    # Nacionalidad por edad (D-050): las nacionalidades fundidas y las celdas pequeñas de cada
    # nacionalidad × edad van a otras_extranjeras de la misma edad.
    te = obj.filter(pl.col("objetivo") == "nacionalidad_top_edad")
    if te.height:
        nac = pl.col("clave").str.extract(r"^(nacionalidad_top=[^;]+)")
        resto = pl.col("clave").str.extract(r"^nacionalidad_top=[^;]+(;.*)$")
        te = te.with_columns(nac.alias("_n"), resto.alias("_r"))
        te = te.with_columns(pl.col("valor").sum().over("_n").alias("_tn"))
        propia = ~pl.col("_n").is_in([otras, "nacionalidad_top=espanola"])
        # Nacionalidad pequeña en el bloque: sin edad (todas sus edades en una celda, igual a
        # su total de nacionalidad_top), porque con pocos donantes no se pueden cumplir a la vez
        # el total y la edad dentro de las cotas
        entera = te.filter(propia & ~pl.col("_n").is_in(list(mapa)))
        entera = entera.filter(
            (pl.col("_tn") < MIN_NACIONALIDAD_EDAD) | pl.col("_n").is_in(list(sin_edad))
        )
        pares_e = entera.select("clave", "_n").iter_rows()
        mapa_e = {c: n + ";edad_nacionalidad=todas" for c, n in pares_e}
        fundir = te.filter(
            propia
            & ~pl.col("clave").is_in(list(mapa_e))
            & (pl.col("_n").is_in(list(mapa)) | (pl.col("valor") < MIN_CELDA_NACIONALIDAD))
        )
        mapa_e |= {c: otras + r for c, r in fundir.select("clave", "_r").iter_rows()}
        if mapa_e:
            nuevo = (
                te.with_columns(pl.col("clave").replace(mapa_e))
                .group_by("clave", maintain_order=True)
                .agg(pl.all().exclude("valor", "_n", "_r", "_tn").first(), pl.col("valor").sum())
                .select(obj.columns)
            )
            obj = pl.concat(
                [obj.filter(pl.col("objetivo") != "nacionalidad_top_edad"), nuevo]
            ).sort("objetivo", "clave")
            fusion = fusion | {"nacionalidad_top_edad": mapa_e}
    return obj, fusion


def cobertura_actividad(u: D.Unidades, provincias: list[str] | None = None) -> pl.DataFrame:
    """Proporción de cada clave de `actividad_tramo` en los donantes (peso inicial) dentro de su
    cruce (sexo × tramo): en todos (`cuota_donantes`) y, con `provincias`, en los del bloque
    (`cuota_local`). Es la cobertura que los donantes pueden dar a cada celda."""
    vs = D.variables_de("actividad_tramo")

    def cuota(lf: pl.LazyFrame, nombre: str) -> pl.LazyFrame:
        return (
            lf.filter(~pl.col("relacion_actividad").is_in(["NP"]))
            .group_by(D.clave(vs).alias("clave"))
            .agg(pl.col("peso_inicial").sum().alias("w"))
            .with_columns(
                pl.col("clave").str.extract(r"^relacion_actividad=[^;]+(;.*)$").alias("_r")
            )
            .with_columns((pl.col("w") / pl.col("w").sum().over("_r")).alias(nombre))
            .select("clave", nombre)
        )

    lf = u.personas.lazy()
    out = cuota(lf, "cuota_donantes")
    if provincias is not None:
        loc = cuota(lf.filter(pl.col("provincia").is_in(provincias)), "cuota_local")
        out = out.join(loc, on="clave", how="left")
    return out.collect()


def _fusionar_actividad(
    obj: pl.DataFrame, cobertura: pl.DataFrame | None = None
) -> tuple[pl.DataFrame, dict[str, dict[str, str]]]:
    """Funde con «otra_inactividad» del mismo cruce (sexo × tramo) (D-049, D-050):

    - las categorías de inactividad que pesan menos de `MIN_INACTIVIDAD` de los inactivos del
      cruce (p. ej. jubilados de 16-44 años o estudiantes de 65 y más);
    - las categorías no ocupadas con objetivo 0 (p. ej. paradas de 65 y más en Ceuta);
    - con `cobertura`, las categorías no ocupadas cuya proporción en todos los donantes,
      multiplicada por el factor máximo de la calibración (5), no llega a la del objetivo con
      un margen de `MARGEN` (p. ej. incapacitados de 65 y más, que el Censo, de registros
      administrativos, cuenta como jubilados, y la EPA, por lo que declaran, no);
    - con `cobertura`, si una categoría de inactividad tiene en los donantes del bloque, por
      el factor mínimo (0,2), más de lo que pide el objetivo (con el mismo margen), todas las
      categorías de inactividad del cruce: se calibra su total (p. ej. varones de 35-44 en
      «otra inactividad» en el País Vasco).

    Solo afecta a la calibración: la persona conserva su categoría y el total del cruce se
    calibra."""
    otra = "relacion_actividad=otra_inactividad"
    inactivas = ["estudiante", "jubilado_pensionista", "incapacidad_permanente"]
    no_ocupadas = ["parado", *inactivas]
    fusion, partes = {}, []
    for o in ("actividad_tramo",):
        a = obj.filter(pl.col("objetivo") == o).with_columns(
            pl.col("clave").str.extract(r"^relacion_actividad=([^;]+)").alias("_c"),
            pl.col("clave").str.extract(r"^relacion_actividad=[^;]+(;.*)$").alias("_resto"),
        )
        if a.is_empty():
            continue
        a = a.with_columns(
            pl.when(pl.col("_c").is_in([*inactivas, "otra_inactividad"]))
            .then(pl.col("valor"))
            .otherwise(0.0)
            .sum()
            .over("_resto")
            .alias("_ina")
        )
        a = a.with_columns((pl.col("valor") / pl.col("valor").sum().over("_resto")).alias("_cuota"))
        pequena = pl.col("valor") < MIN_INACTIVIDAD * pl.col("_ina")
        fundir = (pl.col("_c").is_in(inactivas) & pequena) | (
            pl.col("_c").is_in(no_ocupadas) & (pl.col("valor") <= 0)
        )
        if cobertura is not None:
            a = a.join(cobertura, on="clave", how="left").with_columns(
                pl.col("cuota_donantes").fill_null(0.0)
            )
            fundir = fundir | (
                pl.col("_c").is_in(no_ocupadas)
                & (pl.col("cuota_donantes") * FACTOR_MAX < MARGEN * pl.col("_cuota"))
            )
            if "cuota_local" in a.columns:
                sobra = pl.col("_c").is_in([*inactivas, "otra_inactividad"]) & (
                    pl.col("cuota_local").fill_null(0.0) * FACTOR_MIN * MARGEN > pl.col("_cuota")
                )
                cruce = a.filter(sobra)["_resto"].unique().implode()
                fundir = fundir | (pl.col("_c").is_in(inactivas) & pl.col("_resto").is_in(cruce))
        peq = a.filter(fundir)
        destino = set(a.filter(pl.col("_c") == "otra_inactividad")["clave"])
        pares = peq.select("clave", "_resto").iter_rows()
        mapa = {c: otra + r for c, r in pares if otra + r in destino}
        if not mapa:
            continue
        fusion[o] = mapa
        extra = (
            a.filter(pl.col("clave").is_in(list(mapa)))
            .with_columns(pl.col("clave").replace(mapa))
            .group_by("clave")
            .agg(pl.col("valor").sum().alias("_extra"))
        )
        partes.append(
            a.filter(~pl.col("clave").is_in(list(mapa)))
            .join(extra, on="clave", how="left")
            .with_columns(pl.col("valor") + pl.col("_extra").fill_null(0.0))
            .select(obj.columns)
        )
    if not fusion:
        return obj, {}
    return pl.concat([obj.filter(~pl.col("objetivo").is_in(list(fusion))), *partes]).sort(
        "objetivo", "clave"
    ), fusion


def _cruce(objetivo: str) -> pl.Expr:
    """Parte de la clave que define el cruce dentro del que se comparan las celdas: el resto de
    la clave salvo en nacionalidad × edad, donde es la nacionalidad (se funden edades); con una
    sola variable, todo el objetivo."""
    if objetivo == "nacionalidad_top":
        return pl.lit("")
    if objetivo == "nacionalidad_top_edad":
        return pl.col("clave").str.extract(r"^([^;]+);")
    return pl.col("clave").str.extract(r"^[^;]+(;.*)$")


def cobertura_local(u: D.Unidades, provincias: list[str], objetivo: str) -> pl.DataFrame:
    """Proporción de cada clave de `objetivo` en los donantes del bloque (peso inicial) dentro
    de su cruce (`_cruce`)."""
    vs = D.variables_de(objetivo)
    return (
        u.personas.lazy()
        .filter(pl.col("provincia").is_in(provincias))
        .group_by(D.clave(vs).alias("clave"))
        .agg(pl.col("peso_inicial").sum().alias("w"))
        .with_columns(_cruce(objetivo).alias("_r"))
        .with_columns((pl.col("w") / pl.col("w").sum().over("_r")).alias("cuota_local"))
        .select("clave", "cuota_local")
        .collect()
    )


def fusionar_sobrecobertura(
    obj: pl.DataFrame, objetivo: str, cobertura: pl.DataFrame
) -> tuple[pl.DataFrame, dict[str, str]]:
    """Celdas de `objetivo` que los donantes del bloque cubren de más (su proporción por el
    factor mínimo, 0,2, y con `MARGEN`, supera la del objetivo): se calibran junto con la
    categoría más numerosa de su cruce (D-050; p. ej. estado civil «no consta» de 35-54 años en
    Ceuta, mucho más frecuente en los donantes de 2021 que en el Censo Anual, o marroquíes de
    0-19 años en Ceuta, que van con la edad más numerosa de los marroquíes)."""
    a = obj.filter(pl.col("objetivo") == objetivo)
    if a.is_empty():
        return obj, {}
    a = (
        a.with_columns(_cruce(objetivo).alias("_r"))
        .with_columns((pl.col("valor") / pl.col("valor").sum().over("_r")).alias("_cuota"))
        .join(cobertura, on="clave", how="left")
    )
    mayor = (
        a.sort("valor", "clave", descending=True)
        .unique("_r", keep="first")
        .select("_r", pl.col("clave").alias("_mayor"))
    )
    a = a.join(mayor, on="_r", how="left")
    sobra = a.filter(
        (pl.col("cuota_local").fill_null(0.0) * FACTOR_MIN * MARGEN > pl.col("_cuota"))
        & (pl.col("clave") != pl.col("_mayor"))
    )
    mapa = dict(sobra.select("clave", "_mayor").iter_rows())
    if not mapa:
        return obj, {}
    nuevo = (
        a.with_columns(pl.col("clave").replace(mapa))
        .group_by("clave", maintain_order=True)
        .agg(
            pl.all().exclude("valor", "_r", "_cuota", "cuota_local", "_mayor").first(),
            pl.col("valor").sum(),
        )
        .select(obj.columns)
    )
    return pl.concat([obj.filter(pl.col("objetivo") != objetivo), nuevo]).sort(
        "objetivo", "clave"
    ), mapa


def _contexto_unidades(u: D.Unidades) -> pl.DataFrame:
    """Una fila por unidad: municipio, tamaño de municipio y grado de urbanización del donante."""
    ref = u.personas.filter(pl.col("relacion_persona_ref").is_in(["persona_referencia", "NP"]))
    return ref.select("unidad", "municipio", "tamano_municipio", "grado_urbanizacion").unique(
        "unidad", keep="first"
    )


def base_bloque(u: D.Unidades, b: str, ps: list[str]) -> pl.DataFrame:
    """Donantes base del bloque: unidad, provincia, local, nivel y factor del peso inicial."""
    uni = u.unidades.filter(pl.col("provincia").is_in(ps)).select(
        "unidad", "provincia", "tipo_unidad"
    )
    if not b.startswith("MUNIS:"):
        return uni.select(
            "unidad",
            "provincia",
            pl.lit(True).alias("local"),
            pl.lit("mismo_territorio").alias("nivel"),
            pl.lit(1.0).alias("factor"),
        )
    from sinpop.targets import municipios as M

    lista = M.definicion(Path(b.split(":", 1)[1])).municipios
    ctx = _contexto_unidades(u)
    ident = set(ctx["municipio"].drop_nulls().unique().to_list())
    pad = M.padron()
    # Clase del Censo 2021 para los no identificados: solo existen «hasta_2000» y
    # «de_2001_a_10000»; un municipio que ha crecido desde 2021 sigue en la segunda.
    pad = pad.with_columns(
        pl.when(pl.col("tamano_municipio") == "hasta_2000")
        .then(pl.lit("hasta_2000"))
        .otherwise(pl.lit("de_2001_a_10000"))
        .alias("clase_censo"),
        pl.col("municipio").is_in(list(ident)).alias("ident"),
    )
    no_id = pad.filter(~pl.col("ident"))
    escala = (
        no_id.group_by("provincia", "clase_censo")
        .agg(
            pl.col("poblacion").filter(pl.col("municipio").is_in(lista)).sum().alias("lista"),
            pl.col("poblacion").sum().alias("todos"),
        )
        .filter(pl.col("lista") > 0)
        .select(
            "provincia",
            pl.col("clase_censo").alias("tamano_municipio"),
            (pl.col("lista") / pl.col("todos")).alias("factor"),
        )
    )
    x = uni.join(ctx, on="unidad", how="left")
    locales = x.filter(
        (pl.col("tipo_unidad") == "hogar") & pl.col("municipio").is_in(lista)
    ).select(
        "unidad",
        "provincia",
        pl.lit(True).alias("local"),
        pl.lit("mismo_territorio").alias("nivel"),
        pl.lit(1.0).alias("factor"),
    )
    clase = (
        x.filter((pl.col("tipo_unidad") == "hogar") & pl.col("municipio").is_null())
        .join(escala, on=["provincia", "tamano_municipio"])
        .select(
            "unidad",
            "provincia",
            pl.lit(False).alias("local"),
            pl.lit("misma_provincia").alias("nivel"),
            "factor",
        )
    )
    prov_pob = pad.group_by("provincia").agg(
        pl.col("poblacion").filter(pl.col("municipio").is_in(lista)).sum().alias("lista"),
        pl.col("poblacion").sum().alias("todos"),
    )
    col = (
        x.filter(pl.col("tipo_unidad") == "colectivo")
        .join(prov_pob, on="provincia")
        .select(
            "unidad",
            "provincia",
            pl.lit(False).alias("local"),
            pl.lit("misma_provincia").alias("nivel"),
            (pl.col("lista") / pl.col("todos")).alias("factor"),
        )
    )
    return pl.concat([locales, clase, col]).filter(pl.col("factor") > 0).sort("unidad")


def _pesos_provincias(
    b: str, ps: list[str], objetivo: str, clave_: str, prov_obj: dict
) -> list[float]:
    """Reparto de las unidades añadidas entre las provincias del bloque: el objetivo de la celda
    en cada provincia (comunidades) o su población en la lista (municipios)."""
    if b.startswith("MUNIS:"):
        from sinpop.targets import municipios as M

        lista = M.definicion(Path(b.split(":", 1)[1])).municipios
        pad = M.padron().filter(pl.col("municipio").is_in(lista))
        return [float(pad.filter(pl.col("provincia") == p)["poblacion"].sum()) for p in ps]
    cuota = [
        float(
            prov_obj[p]
            .filter((pl.col("objetivo") == objetivo) & (pl.col("clave") == clave_))["valor"]
            .sum()
        )
        for p in ps
    ]
    if sum(cuota) > 0:
        return cuota
    # Celda fundida en el bloque (p. ej. una nacionalidad sin edad): no existe en las
    # provincias; el reparto es el del total del objetivo
    tot = [float(prov_obj[p].filter(pl.col("objetivo") == objetivo)["valor"].sum()) for p in ps]
    return tot if sum(tot) > 0 else [1.0] * len(ps)


def _tiene_grado(prov_obj: dict, p: str, grado: str, b: str) -> bool:
    """La provincia tiene residentes con ese grado de urbanización (objetivo `urbanizacion`).
    En las listas de municipios el reparto es por población y no se restringe."""
    if b.startswith("MUNIS:"):
        return True
    o = prov_obj[p].filter(
        (pl.col("objetivo") == "urbanizacion") & (pl.col("clave") == f"grado_urbanizacion={grado}")
    )
    return bool(o.height) and float(o["valor"].sum()) > 0


def _ampliar(
    u: D.Unidades,
    b: str,
    ps: list[str],
    obj: pl.DataFrame,
    todas: pl.DataFrame,
    reparar: pl.DataFrame | None = None,
    previas: pl.DataFrame | None = None,
    evitar_celdas: pl.DataFrame | None = None,
) -> tuple[pl.DataFrame, pl.DataFrame]:
    """Unidades del bloque (base y añadidas, con `d_anadida`) y registro de ampliaciones.

    Con `reparar` (objetivo, clave, falta) se añade a `previas` la masa `falta` en esas celdas,
    sin tomar unidades que caigan en `evitar_celdas` (objetivo, clave; véase `calibrar`)."""
    from sinpop.harmonize.core import ccaa_de_provincia
    from sinpop.targets import run

    cfg = _cfg()
    amp = cfg.ampliacion  # type: ignore[attr-defined]
    ccaa = ccaa_de_provincia()
    base = base_bloque(u, b, ps) if previas is None else previas.drop("d_anadida")
    if previas is None and b.startswith("MUNIS:"):
        # Los hogares de la provincia y clase que caerían en una celda sin objetivo en la lista
        # (p. ej. zona intermedia en un territorio rural) no representan a esos municipios.
        validas = obj.filter(pl.col("valor") > 0).select("objetivo", "clave")
        fuera = todas.join(validas, on=["objetivo", "clave"], how="anti").select("unidad")
        base = base.join(
            fuera.unique().join(
                base.filter(pl.col("nivel") != "mismo_territorio").select("unidad"), on="unidad"
            ),
            on="unidad",
            how="anti",
        )
    loc = (
        base.with_columns(pl.lit(None, dtype=pl.Float64).alias("d_anadida"))
        if previas is None
        else previas
    )
    cel = todas.join(base.select("unidad", "factor"), on="unidad").join(
        u.unidades.select("unidad", "d"), on="unidad"
    )
    n = cel.group_by("objetivo", "clave").agg(
        pl.len().alias("locales"),
        (pl.col("x") * pl.col("d") * pl.col("factor")).sum().alias("masa"),
    )
    pos = obj.filter(pl.col("valor") > 0).select("objetivo", "clave", "valor")
    def_ = pos.join(n, on=["objetivo", "clave"], how="left").fill_null(0)
    if reparar is None:
        def_ = def_.filter(
            (pl.col("locales") < amp.min_donantes_celda)
            | (pl.col("valor") > amp.razon_max * pl.col("masa"))
        ).sort("objetivo", "clave")
        def_ = def_.with_columns(pl.lit(None, dtype=pl.Float64).alias("falta"))
        evitar = pl.DataFrame(schema={"unidad": pl.Int64})
    else:
        def_ = def_.join(reparar.select("objetivo", "clave", "falta"), on=["objetivo", "clave"])
        evitar = (
            todas.join(evitar_celdas, on=["objetivo", "clave"]).select("unidad").unique()
            if evitar_celdas is not None and evitar_celdas.height
            else pl.DataFrame(schema={"unidad": pl.Int64})
        )
    cols = ["bloque", "objetivo", "clave", "locales", "razon_inicial", "anadidas"]
    if def_.height == 0:
        return loc, pl.DataFrame(schema=dict.fromkeys(cols, pl.Utf8)).cast(
            {"locales": pl.Int64, "razon_inicial": pl.Float64, "anadidas": pl.Int64}
        )
    ctx = _contexto_unidades(u)
    grado = (
        ctx.join(base.select("unidad"), on="unidad")
        .group_by("grado_urbanizacion")
        .agg(pl.len())
        .sort("len", "grado_urbanizacion", descending=True)
        .row(0)[0]
    )
    # Incompatibles: unidades con alguna celda sin objetivo positivo en el bloque (objetivo 0 o,
    # en las listas de municipios, categoría ausente).
    positivas = obj.filter(pl.col("valor") > 0).select("objetivo", "clave")
    incompatibles = (
        todas.join(positivas, on=["objetivo", "clave"], how="anti").select("unidad").unique()
    )
    orden = (
        u.unidades.select(
            "unidad",
            "provincia",
            "d",
            "tipo_unidad",
            D._orden_determinista(pl.col("household_id"), pl.col("norden")).alias("_o"),
        )
        .join(base.select("unidad"), on="unidad", how="anti")
        .join(incompatibles, on="unidad", how="anti")
        .join(evitar, on="unidad", how="anti")
        .join(ctx.select("unidad", "grado_urbanizacion"), on="unidad", how="left")
        .with_columns(pl.col("provincia").replace_strict(ccaa).alias("_ccaa"))
    )
    ccaa_b = sorted({ccaa[p] for p in ps})
    parecidas = sorted({c for cb in ccaa_b for c in ccaa_parecidas(cb)} - set(ccaa_b))
    filtros = {
        "misma_provincia": pl.col("provincia").is_in(ps),
        "misma_ccaa_mismo_grado_urbanizacion": pl.col("_ccaa").is_in(ccaa_b)
        & (pl.col("grado_urbanizacion") == grado),
        "ccaa_parecidas": pl.col("_ccaa").is_in(parecidas),
        "espana": pl.lit(True),
    }
    niveles = [n for n in cfg.jerarquia_donantes if n in filtros]  # type: ignore[attr-defined]
    prov_obj = {p: run.leer(f"PROV:{p}") for p in ps}
    anadidas, registro = [], []
    universo = dict(obj.select("objetivo", "universo").unique().iter_rows())
    for objetivo, clave_, valor, locales, masa, falta_r in def_.select(
        "objetivo", "clave", "valor", "locales", "masa", "falta"
    ).iter_rows():
        # Solo unidades del tipo de la celda: los colectivos no se importan para celdas de
        # hogares o de residentes (caerían también en las celdas de colectivos del bloque).
        tipo = "colectivo" if universo[objetivo] == "colectivos" else "hogar"
        cand = (
            todas.filter((pl.col("objetivo") == objetivo) & (pl.col("clave") == clave_))
            .select("unidad", "x")
            .join(orden.filter(pl.col("tipo_unidad") == tipo), on="unidad")
            .sort("_o", "unidad")
        )
        if anadidas:
            cand = cand.join(pl.concat(anadidas).select("unidad"), on="unidad", how="anti")
        cand = pl.concat(
            [cand.filter(filtros[nv]).with_columns(pl.lit(nv).alias("nivel")) for nv in niveles]
        ).unique("unidad", keep="first", maintain_order=True)
        if falta_r is not None or locales >= amp.min_donantes_celda:
            falta = falta_r if falta_r is not None else valor / amp.razon_objetivo - masa
            acum = (pl.col("x") * pl.col("d")).cum_sum()
            t = cand.filter(acum.shift(1, fill_value=0) < falta).with_columns(
                pl.col("d").alias("d_anadida")
            )
        elif locales < amp.min_donantes_celda:
            # Peso inicial para que las unidades añadidas sumen el objetivo de la celda contando
            # las personas de la celda que trae cada una (`x`): un hogar con 4 chinos cuenta 4
            t = cand.head(amp.min_donantes_celda - locales)
            t = t.with_columns(pl.lit(valor / max(float(t["x"].sum()), 1.0)).alias("d_anadida"))
        cuota = _pesos_provincias(b, ps, objetivo, clave_, prov_obj)
        # Cada unidad va a una provincia que tenga su grado de urbanización (p. ej. un hogar de
        # ciudad no puede ir a una provincia sin ciudades); reparto sistemático por grado.
        grados = t["grado_urbanizacion"].to_list()
        destino = [""] * t.height
        for g in sorted({x for x in grados if x is not None}) + [None]:
            pos_g = [j for j, x in enumerate(grados) if x == g]
            if not pos_g:
                continue
            c = [
                q * (1.0 if g is None or _tiene_grado(prov_obj, p, g, b) else 0.0)
                for q, p in zip(cuota, ps, strict=True)
            ]
            if not sum(c):
                c = cuota
            tot = sum(c) or 1.0
            lims = [sum(c[: i + 1]) / tot for i in range(len(ps))]
            k = len(pos_g)
            for jj, j in enumerate(pos_g):
                destino[j] = ps[next(i for i, x in enumerate(lims) if (jj + 0.5) / k <= x + 1e-12)]
        anadidas.append(
            t.select("unidad", "d_anadida", "nivel").with_columns(
                pl.Series("provincia", destino, dtype=pl.Utf8)
            )
        )
        registro.append((b, objetivo, clave_, locales, valor / masa if masa else None, t.height))
    add = (
        pl.concat(anadidas)
        .unique("unidad", keep="first", maintain_order=True)
        .sort("unidad")
        .with_columns(pl.lit(False).alias("local"), pl.lit(1.0).alias("factor"))
    )
    reg = pl.DataFrame(registro, schema=cols, orient="row")
    return pl.concat([loc, add.select(loc.columns)]), reg


RONDAS_REPARACION = 3


def _calibrar_unidades(u: D.Unidades, ub: pl.DataFrame, obj, fusion, metodo, ccaa):
    """Matriz y calibración de las unidades `ub` del bloque (índice local y provincia de
    destino)."""
    ubl = ub.with_row_index("_l")
    pers = u.personas.drop("provincia", "ccaa").join(
        ubl.select("unidad", "_l", "provincia"), on="unidad"
    )
    pers = pers.with_columns(pl.col("provincia").replace_strict(ccaa).alias("ccaa"))
    uni = u.unidades.drop("provincia").join(ubl, on="unidad").sort("_l")
    uni = uni.with_columns(
        pl.coalesce("d_anadida", pl.col("d") * pl.col("factor")).alias("d")
    ).drop("d_anadida")
    sub = D.Unidades(
        personas=pers.drop("unidad")
        .rename({"_l": "unidad"})
        .with_columns(pl.col("unidad").cast(pl.Int64)),
        unidades=uni.drop("unidad")
        .rename({"_l": "unidad"})
        .with_columns(pl.col("unidad").cast(pl.Int64)),
    )
    m = D.matriz(sub, obj, fusion)
    r = C.calibrar(m.X, m.d, m.celdas["valor"].to_numpy(), metodo)
    return uni, m, r


def calibrar(
    u: D.Unidades, territorio: str, metodo: str = "logit", excluir: tuple[str, ...] = ()
) -> Calibrado:
    """`excluir`: objetivos calibrables que no se usan (prueba del territorio reservado, F5)."""
    from sinpop.harmonize.core import ccaa_de_provincia
    from sinpop.targets import run

    ccaa = ccaa_de_provincia()
    filas, diags, ceros, ampl, fusiones = [], {}, [], [], []
    todas = None
    for b in bloques(territorio):
        ps = provincias_bloque(b)
        cob = cobertura_actividad(u, ps)
        from sinpop.config import load_config

        # Se busca 1e-7, pero el criterio de aceptación es el de V-PESOS (desviación relativa
        # máxima ≤ 0,1 %); la desviación alcanzada queda en el diagnóstico.
        tol = load_config("thresholds.yaml").v_pesos.convergencia_max  # type: ignore[attr-defined]
        # Último recurso (D-050): si no converge y entre las celdas fuera de tolerancia hay de
        # nacionalidad × edad, esas nacionalidades se calibran en el bloque sin la edad (solo su
        # total) y se repite; queda en las fusiones (`edad_nacionalidad=todas`).
        sin_edad: frozenset[str] = frozenset()
        for _intento in range(MAX_SIN_EDAD + 1):
            ampl_b = []
            obj, fusion = fusionar(
                D.objetivos_calibrables(run.leer(b), municipios=b.startswith("MUNIS:")).filter(
                    ~pl.col("objetivo").is_in(list(excluir))
                ),
                cob,
                sin_edad,
                cobertura_local(u, ps, "nacionalidad_top"),
            )
            for o in OBJETIVOS_SOBRECOBERTURA:
                obj, mapa_o = fusionar_sobrecobertura(obj, o, cobertura_local(u, ps, o))
                if mapa_o:
                    fusion[o] = fusion.get(o, {}) | mapa_o
            if todas is None or set(obj["objetivo"].unique()) != set(todas["objetivo"].unique()):
                todas = _celdas_por_unidad(u.personas, obj)
            todas_b = todas
            if fusion:  # solo se rehacen las filas de los objetivos con celdas fusionadas
                afectados = list(fusion)
                resto = todas.filter(~pl.col("objetivo").is_in(afectados))
                fus = todas.filter(pl.col("objetivo").is_in(afectados))
                for o, mapa in fusion.items():
                    fus = fus.with_columns(
                        pl.when(pl.col("objetivo") == o)
                        .then(pl.col("clave").replace(mapa))
                        .otherwise(pl.col("clave"))
                        .alias("clave")
                    )
                fus = fus.group_by("unidad", "objetivo", "clave").agg(pl.col("x").sum())
                todas_b = pl.concat([resto, fus.select(resto.columns)])
            ub, reg = _ampliar(u, b, ps, obj, todas_b)
            ampl_b.append(reg)
            uni, m, r = _calibrar_unidades(u, ub, obj, fusion, metodo, ccaa)
            # Reparación (D-041): con pocos donantes, la calibración acotada puede no tener
            # solución aunque ninguna celda sea deficitaria por sí sola (p. ej. faltan africanos
            # que no sean marroquíes). Se añaden donantes a las celdas que no llegan, sin tomar
            # unidades de las celdas que se pasan, y se recalibra (hasta RONDAS_REPARACION veces).
            ronda = 0
            while r.desviacion_max > tol and ronda < RONDAS_REPARACION:
                ronda += 1
                T = m.celdas["valor"].to_numpy()
                dev = (m.X.T @ r.w) / T - 1
                c = m.celdas.with_columns(pl.Series("dev", dev))
                cortas = c.filter(pl.col("dev") < -tol)
                sobran = c.filter(pl.col("dev") > tol).select("objetivo", "clave")
                reparar = cortas.select(
                    "objetivo",
                    "clave",
                    (2 * (-pl.col("dev")) * pl.col("valor")).alias("falta"),
                )
                ub, reg = _ampliar(
                    u, b, ps, obj, todas_b, reparar=reparar, previas=ub, evitar_celdas=sobran
                )
                ampl_b.append(reg.with_columns(pl.lit(f"reparacion {ronda}").alias("motivo")))
                uni, m, r = _calibrar_unidades(u, ub, obj, fusion, metodo, ccaa)
            if r.desviacion_max <= tol:
                break
            T = m.celdas["valor"].to_numpy()
            dev = np.abs((m.X.T @ r.w) / T - 1)
            nuevas = (
                set(
                    m.celdas.filter(
                        pl.Series(dev > tol) & (pl.col("objetivo") == "nacionalidad_top_edad")
                    )["clave"]
                    .str.extract(r"^(nacionalidad_top=[^;]+);")
                    .drop_nulls()
                    .to_list()
                )
                - set(sin_edad)
                - {"nacionalidad_top=otras_extranjeras", "nacionalidad_top=espanola"}
            )
            if not nuevas:
                break
            sin_edad = sin_edad | nuevas
        if r.desviacion_max > tol:
            raise RuntimeError(
                f"{b}: la calibración ({metodo}) no converge: {r.desviacion_max:.2e}"
            )
        ampl.extend(ampl_b)
        fusiones.append(
            pl.DataFrame(
                [(b, o, k, v) for o, mp in fusion.items() for k, v in mp.items()],
                schema=dict.fromkeys(["bloque", "objetivo", "clave", "fusionada_en"], pl.Utf8),
                orient="row",
            )
        )
        diags[b] = C.diagnostico(r, m.d)
        diags[b]["proporcion_local"] = float(uni["local"].mean())
        diags[b]["niveles"] = dict(uni.group_by("nivel").agg(pl.len()).iter_rows())
        ceros.append(m.ceros.with_columns(pl.lit(b).alias("bloque")))
        filas.append(
            uni.select(
                pl.lit(b).alias("bloque"),
                "unidad",
                "local",
                "nivel",
                "provincia",
                pl.col("provincia").replace_strict(ccaa).alias("ccaa"),
                "d",
                pl.Series("w", r.w),
            )
        )
    return Calibrado(
        unidades=pl.concat(filas),
        diagnosticos=diags,
        ceros=pl.concat(ceros),
        ampliaciones=pl.concat(ampl, how="diagonal_relaxed"),
        fusiones=pl.concat(fusiones),
    )


def personas_ponderadas(u: D.Unidades, cal: Calibrado) -> pl.DataFrame:
    """Personas de las unidades calibradas con su peso (`w`) y su territorio de destino; una
    unidad añadida a otro bloque aparece una vez por bloque."""
    un = cal.unidades.with_row_index("unidad_cal")
    return (
        u.personas.drop("provincia", "ccaa")
        .join(
            un.select("unidad", "unidad_cal", "bloque", "local", "nivel", "provincia", "ccaa", "w"),
            on="unidad",
        )
        .sort("unidad_cal", "norden")
    )
