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
    return [
        float(
            prov_obj[p]
            .filter((pl.col("objetivo") == objetivo) & (pl.col("clave") == clave_))["valor"]
            .sum()
        )
        for p in ps
    ]


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
            t = cand.head(amp.min_donantes_celda - locales).with_columns(
                pl.lit(valor / amp.min_donantes_celda).alias("d_anadida")
            )
        cuota = _pesos_provincias(b, ps, objetivo, clave_, prov_obj)
        tot = sum(cuota) or 1.0
        lims = [sum(cuota[: i + 1]) / tot for i in range(len(ps))]
        k = t.height
        destino = [
            ps[next(i for i, x in enumerate(lims) if (j + 0.5) / k <= x + 1e-12)] for j in range(k)
        ]
        anadidas.append(
            t.select("unidad", "d_anadida", "nivel").with_columns(
                pl.Series("provincia", destino, dtype=pl.Utf8)
            )
        )
        registro.append((b, objetivo, clave_, locales, valor / masa if masa else None, k))
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


def calibrar(u: D.Unidades, territorio: str, metodo: str = "logit") -> Calibrado:
    from sinpop.harmonize.core import ccaa_de_provincia
    from sinpop.targets import run

    ccaa = ccaa_de_provincia()
    filas, diags, ceros, ampl, fusiones = [], {}, [], [], []
    todas = None
    for b in bloques(territorio):
        ps = provincias_bloque(b)
        obj, fusion = fusionar(
            D.objetivos_calibrables(run.leer(b), municipios=b.startswith("MUNIS:"))
        )
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
        from sinpop.config import load_config

        # Se busca 1e-7, pero el criterio de aceptación es el de V-PESOS (desviación relativa
        # máxima ≤ 0,1 %); la desviación alcanzada queda en el diagnóstico.
        tol = load_config("thresholds.yaml").v_pesos.convergencia_max  # type: ignore[attr-defined]
        uni, m, r = _calibrar_unidades(u, ub, obj, fusion, metodo, ccaa)
        # Reparación (D-041): con pocos donantes, la calibración acotada puede no tener solución
        # aunque ninguna celda sea deficitaria por sí sola (p. ej. faltan africanos que no sean
        # marroquíes). Se añaden donantes a las celdas que no llegan, sin tomar unidades de las
        # celdas que se pasan, y se recalibra (hasta RONDAS_REPARACION veces).
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
            ampl.append(reg.with_columns(pl.lit(f"reparacion {ronda}").alias("motivo")))
            uni, m, r = _calibrar_unidades(u, ub, obj, fusion, metodo, ccaa)
        if r.desviacion_max > tol:
            raise RuntimeError(
                f"{b}: la calibración ({metodo}) no converge: {r.desviacion_max:.2e}"
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
