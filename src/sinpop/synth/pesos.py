"""Calibración de las unidades donantes a los objetivos de un territorio (F4; D-038).

España se calibra como la unión de sus 19 comunidades: cada comunidad se calibra con sus propios
objetivos y con los donantes que residen en ella. Así la población nacional reproduce también
las cifras de cada comunidad (V-COHERENCIA) y el reparto por provincias queda como validación
(objetivo reservado `provincia_si_calibra_ccaa`). Una comunidad o una provincia se calibra
directamente con sus objetivos.

Ampliación de donantes (docs/02 §5). Una celda calibrada del bloque es deficitaria si:

- tiene menos de `MIN_DONANTES` unidades locales: se añaden las que faltan, con peso inicial
  objetivo / `MIN_DONANTES` (con el peso del Censo, un objetivo pequeño exigiría factores
  fuera del rango de V-PESOS); o
- su objetivo supera `RAZON_MAX` veces la masa inicial local (Σ personas × peso del Censo), lo
  que pasa con las nacionalidades que más han crecido desde 2021 (p. ej. Ucrania en Asturias):
  se añaden unidades, con su peso del Censo, hasta que la razón baje a `RAZON_OBJETIVO`.

Las unidades añadidas se toman de fuera del bloque (primero de la misma comunidad, si el bloque es
una provincia, y luego de toda España) entre las que caen en la celda, en un orden
pseudoaleatorio fijo, prefiriendo las del mismo contexto (grado de urbanización y tamaño de
municipio más frecuentes en el bloque) y excluyendo las que caen en celdas con objetivo 0 del
bloque. Se reparten entre las provincias del bloque en proporción al objetivo de la celda en cada
una, pierden su municipio y se marcan como no locales (V-DONANTES informa la proporción local).
"""

from __future__ import annotations

from dataclasses import dataclass

import polars as pl

from sinpop.synth import calibracion as C
from sinpop.synth import donantes as D

MIN_DONANTES = 5
RAZON_MAX = 3.5
RAZON_OBJETIVO = 2.5


def bloques(territorio: str) -> list[str]:
    if territorio == "ES":
        from sinpop.harmonize.core import ccaa_de_provincia

        return [f"CCAA:{c}" for c in sorted(set(ccaa_de_provincia().values()))]
    return [territorio]


@dataclass
class Calibrado:
    unidades: pl.DataFrame  # bloque, unidad (global), local, provincia, ccaa, d, w
    diagnosticos: dict[str, dict]
    ceros: pl.DataFrame
    ampliaciones: pl.DataFrame  # bloque, objetivo, clave, locales, añadidas
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


MIN_CELDA_NACIONALIDAD = 100


def fusionar(obj: pl.DataFrame) -> tuple[pl.DataFrame, dict[str, dict[str, str]]]:
    """Funde con «otras_extranjeras» las nacionalidades cuyo objetivo en el bloque es menor que
    `MIN_CELDA_NACIONALIDAD` personas (p. ej. 7,6 ecuatorianos en Melilla): con tan pocos casos,
    los pocos hogares donantes locales pueden pesar más que el objetivo y la calibración acotada
    no tiene solución. La nacionalidad sigue calibrada por grupos (`nacionalidad`)."""
    top = obj.filter(pl.col("objetivo") == "nacionalidad_top")
    otras = "nacionalidad_top=otras_extranjeras"
    peq = top.filter(
        (pl.col("valor") < MIN_CELDA_NACIONALIDAD)
        & (pl.col("clave") != otras)
        & (pl.col("clave") != "nacionalidad_top=espanola")
    )
    if peq.height == 0:
        return obj, {}
    mapa = {c: otras for c in peq["clave"]}
    nuevo = (
        top.with_columns(pl.col("clave").replace(mapa))
        .group_by("clave", maintain_order=True)
        .agg(pl.all().exclude("valor").first(), pl.col("valor").sum())
        .select(obj.columns)
    )
    return pl.concat([obj.filter(pl.col("objetivo") != "nacionalidad_top"), nuevo]).sort(
        "objetivo", "clave"
    ), {"nacionalidad_top": mapa}


def _ampliar(
    u: D.Unidades, b: str, ps: list[str], obj: pl.DataFrame, todas: pl.DataFrame
) -> tuple[pl.DataFrame, pl.DataFrame]:
    """Unidades del bloque (locales y añadidas, con `d_anadida`) y registro de ampliaciones."""
    from sinpop.harmonize.core import ccaa_de_provincia
    from sinpop.targets import run

    ccaa = ccaa_de_provincia()
    loc = u.unidades.filter(pl.col("provincia").is_in(ps)).select("unidad", "provincia")
    loc = loc.with_columns(
        pl.lit(True).alias("local"), pl.lit(None, dtype=pl.Float64).alias("d_anadida")
    )
    cel = todas.join(loc.select("unidad"), on="unidad").join(
        u.unidades.select("unidad", "d"), on="unidad"
    )
    n = cel.group_by("objetivo", "clave").agg(
        pl.len().alias("locales"), (pl.col("x") * pl.col("d")).sum().alias("masa")
    )
    pos = obj.filter(pl.col("valor") > 0).select("objetivo", "clave", "valor")
    def_ = pos.join(n, on=["objetivo", "clave"], how="left").fill_null(0)
    def_ = def_.filter(
        (pl.col("locales") < MIN_DONANTES) | (pl.col("valor") > RAZON_MAX * pl.col("masa"))
    ).sort("objetivo", "clave")
    cols = ["bloque", "objetivo", "clave", "locales", "razon_inicial", "anadidas"]
    if def_.height == 0:
        return loc, pl.DataFrame(schema=dict.fromkeys(cols, pl.Utf8)).cast(
            {"locales": pl.Int64, "razon_inicial": pl.Float64, "anadidas": pl.Int64}
        )
    # Orden de preferencia: mismo contexto que el más frecuente en el bloque, después el orden
    # pseudoaleatorio fijo. Se excluyen las unidades que caen en celdas con objetivo 0 del bloque.
    ctx = (
        u.personas.filter(pl.col("provincia").is_in(ps))
        .group_by("grado_urbanizacion", "tamano_municipio")
        .agg(pl.len())
        .sort("len", "grado_urbanizacion", "tamano_municipio", descending=True)
        .row(0)
    )
    contexto = (
        u.personas.filter(pl.col("relacion_persona_ref").is_in(["persona_referencia", "NP"]))
        .select(
            "unidad",
            (
                (pl.col("grado_urbanizacion") == ctx[0]) & (pl.col("tamano_municipio") == ctx[1])
            ).alias("_ctx"),
        )
        .unique("unidad")
    )
    cero = obj.filter(pl.col("valor") <= 0).select("objetivo", "clave")
    incompatibles = todas.join(cero, on=["objetivo", "clave"]).select("unidad").unique()
    orden = (
        u.unidades.select(
            "unidad",
            "provincia",
            "d",
            "tipo_unidad",
            D._orden_determinista(pl.col("household_id"), pl.col("norden")).alias("_o"),
        )
        .filter(~pl.col("provincia").is_in(ps))
        .join(contexto, on="unidad")
        .join(incompatibles, on="unidad", how="anti")
    )
    ccaa_b = {ccaa[p] for p in ps}
    niveles = [pl.col("provincia").replace_strict(ccaa).is_in(list(ccaa_b)), pl.lit(True)]
    prov_obj = {p: run.leer(f"PROV:{p}") for p in ps}
    anadidas, registro = [], []
    universo = dict(obj.select("objetivo", "universo").unique().iter_rows())
    for objetivo, clave_, valor, locales, masa in def_.select(
        "objetivo", "clave", "valor", "locales", "masa"
    ).iter_rows():
        # Solo unidades del tipo de la celda: los colectivos no se importan para celdas de
        # hogares o de residentes (caerían también en las celdas de colectivos del bloque).
        tipo = "colectivo" if universo[objetivo] == "colectivos" else "hogar"
        cand = (
            todas.filter((pl.col("objetivo") == objetivo) & (pl.col("clave") == clave_))
            .select("unidad", "x")
            .join(orden.filter(pl.col("tipo_unidad") == tipo), on="unidad")
            .sort(["_ctx", "_o", "unidad"], descending=[True, False, False])
        )
        if anadidas:
            cand = cand.join(pl.concat(anadidas).select("unidad"), on="unidad", how="anti")
        cand = pl.concat(
            [cand.filter(f).with_columns(pl.lit(i).alias("_nivel")) for i, f in enumerate(niveles)]
        )
        cand = cand.unique("unidad", keep="first", maintain_order=True)
        if locales < MIN_DONANTES:
            t = cand.head(MIN_DONANTES - locales).with_columns(
                pl.lit(valor / MIN_DONANTES).alias("d_anadida")
            )
        else:
            falta = valor / RAZON_OBJETIVO - masa
            acum = (pl.col("x") * pl.col("d")).cum_sum()
            t = cand.filter(acum.shift(1, fill_value=0) < falta).with_columns(
                pl.col("d").alias("d_anadida")
            )
        # Reparto entre las provincias del bloque en proporción al objetivo de la celda.
        cuota = [
            float(
                prov_obj[p]
                .filter((pl.col("objetivo") == objetivo) & (pl.col("clave") == clave_))["valor"]
                .sum()
            )
            for p in ps
        ]
        tot = sum(cuota) or 1.0
        lims = [sum(cuota[: i + 1]) / tot for i in range(len(ps))]
        k = t.height
        destino = [
            ps[next(i for i, x in enumerate(lims) if (j + 0.5) / k <= x + 1e-12)] for j in range(k)
        ]
        anadidas.append(
            t.select("unidad", "d_anadida").with_columns(
                pl.Series("provincia", destino, dtype=pl.Utf8)
            )
        )
        registro.append((b, objetivo, clave_, locales, valor / masa if masa else None, k))
    add = (
        pl.concat(anadidas)
        .unique("unidad", keep="first", maintain_order=True)
        .sort("unidad")
        .with_columns(pl.lit(False).alias("local"))
    )
    reg = pl.DataFrame(registro, schema=cols, orient="row")
    return pl.concat([loc, add.select(loc.columns)]), reg


def calibrar(u: D.Unidades, territorio: str, metodo: str = "logit") -> Calibrado:
    from sinpop.harmonize.core import ccaa_de_provincia
    from sinpop.targets import run
    from sinpop.targets.build import provincias_de

    ccaa = ccaa_de_provincia()
    filas, diags, ceros, ampl, fusiones = [], {}, [], [], []
    todas = None
    for b in bloques(territorio):
        ps = provincias_de(b)
        obj, fusion = fusionar(D.objetivos_calibrables(run.leer(b)))
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
        fusiones.append(
            pl.DataFrame(
                [(b, o, k, v) for o, m in fusion.items() for k, v in m.items()],
                schema=dict.fromkeys(["bloque", "objetivo", "clave", "fusionada_en"], pl.Utf8),
                orient="row",
            )
        )
        ampl.append(reg)
        # Personas del bloque con índice local de unidad y la provincia de destino.
        ub = ub.with_row_index("_l")
        pers = u.personas.drop("provincia", "ccaa").join(
            ub.select("unidad", "_l", "provincia"), on="unidad"
        )
        pers = pers.with_columns(pl.col("provincia").replace_strict(ccaa).alias("ccaa"))
        uni = u.unidades.drop("provincia").join(ub, on="unidad").sort("_l")
        uni = uni.with_columns(pl.coalesce("d_anadida", "d").alias("d")).drop("d_anadida")
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
        if not r.convergido:
            raise RuntimeError(
                f"{b}: la calibración ({metodo}) no converge: {r.desviacion_max:.2e}"
            )
        diags[b] = C.diagnostico(r, m.d)
        diags[b]["proporcion_local"] = float(uni["local"].mean())
        ceros.append(m.ceros.with_columns(pl.lit(b).alias("bloque")))
        filas.append(
            uni.select(
                pl.lit(b).alias("bloque"),
                "unidad",
                "local",
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
        ampliaciones=pl.concat(ampl, how="vertical_relaxed"),
        fusiones=pl.concat(fusiones),
    )


def personas_ponderadas(u: D.Unidades, cal: Calibrado) -> pl.DataFrame:
    """Personas de las unidades calibradas con su peso (`w`) y su territorio de destino; una
    unidad añadida a otro bloque aparece una vez por bloque."""
    un = cal.unidades.with_row_index("unidad_cal")
    return (
        u.personas.drop("provincia", "ccaa")
        .join(
            un.select("unidad", "unidad_cal", "bloque", "local", "provincia", "ccaa", "w"),
            on="unidad",
        )
        .sort("unidad_cal", "norden")
    )
