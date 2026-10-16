"""Validación de una población sintética (docs/05 §4 y §6; puerta F4).

Cada función devuelve una tabla con una fila por comprobación y una columna `ok`.
"""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np
import polars as pl

from sinpop import POPULATIONS_DIR
from sinpop.synth import donantes as D
from sinpop.validate import metrics as M

UNIVERSOS = {*D.UNIVERSOS_PERSONA, "hogares"}


def umbrales() -> dict:
    import yaml

    from sinpop import CONFIGS_DIR

    return yaml.safe_load((CONFIGS_DIR / "thresholds.yaml").read_text(encoding="utf-8"))


def cargar(rid: str, raiz: Path = POPULATIONS_DIR) -> tuple[pl.DataFrame, pl.DataFrame, dict]:
    d = raiz / rid
    persons = pl.read_parquet(d / "persons.parquet")
    lineage = pl.read_parquet(d / "lineage.parquet")
    meta = json.loads((d / "metadata.json").read_text(encoding="utf-8"))
    return persons, lineage, meta


def preparar(persons: pl.DataFrame) -> pl.DataFrame:
    """Añade las variables derivadas que usan los objetivos (grupos de edad de cada tabla)."""
    return D.derivadas(persons)


def _territorios(territorio: str, nivel: str) -> list[str]:
    from sinpop.harmonize.core import ccaa_de_provincia
    from sinpop.targets.build import provincias_de

    if nivel == "espana":
        return [territorio]
    ps = provincias_de(territorio)
    if nivel == "ccaa":
        ccaa = ccaa_de_provincia()
        return [f"CCAA:{c}" for c in sorted({ccaa[p] for p in ps})]
    return [f"PROV:{p}" for p in ps]


def _subconjunto(p: pl.DataFrame, t: str) -> pl.DataFrame:
    if t.startswith("CCAA:"):
        return p.filter(pl.col("ccaa") == t[5:])
    if t.startswith("PROV:"):
        return p.filter(pl.col("provincia") == t[5:])
    return p


def _n_universo(p: pl.DataFrame, universo: str, unidad: str) -> float:
    return float(D.en_universo(p, universo, unidad, ["peso"])["peso"].sum())


def comparar(
    p: pl.DataFrame, territorio: str, uso: str, niveles: list[str], semilla: int = 0
) -> pl.DataFrame:
    """TVD y TVD_ref por objetivo y territorio. `p` ya preparada (con `peso`)."""
    from sinpop.targets import run

    cfg = umbrales()
    filas = []
    for nivel in niveles:
        for t in _territorios(territorio, nivel):
            obj = run.leer(t).filter(
                (pl.col("uso") == uso) & pl.col("universo").is_in(list(UNIVERSOS))
            )
            if uso == "calibrar":
                cal = D.objetivos_calibrables(obj, municipios=t.startswith("MUNIS:"))
                obj = obj.filter(pl.col("objetivo").is_in(cal["objetivo"].implode()))
            sub = _subconjunto(p, t)
            if sub.height == 0:
                continue
            r = D.recuentos(sub, obj, "peso")
            for (o,), g in r.group_by("objetivo", maintain_order=True):
                if g.height < 2 or g["valor"].sum() <= 0:
                    continue  # un objetivo de una sola celda no tiene distribución
                info = obj.filter(pl.col("objetivo") == o).row(0, named=True)
                n = _n_universo(sub, info["universo"], info["unidad"])
                if n <= 0:
                    continue
                ref = M.tvd_ref(
                    g["valor"].to_numpy(),
                    max(1, round(n)),
                    cfg["V-MARG"]["muestras_ref"],
                    cfg["V-MARG"]["percentil_ref"],
                    semilla,
                )
                filas.append(
                    {
                        "nivel": nivel,
                        "territorio": t,
                        "objetivo": o,
                        "celdas": g.height,
                        "n": n,
                        "tvd": M.tvd(g["sintetico"], g["valor"]),
                        "hellinger": M.hellinger(g["sintetico"], g["valor"]),
                        "tvd_ref": ref,
                        "fuera_dominio": float(g.filter(pl.col("valor") == 0)["sintetico"].sum()),
                    }
                )
    return pl.DataFrame(filas)


def _residencia(p: pl.DataFrame, territorio: str, niveles: list[str], semilla: int) -> pl.DataFrame:
    """Marginal implícita de los objetivos calibrados: residentes en viviendas familiares y en
    establecimientos colectivos (edad5_sexo_familiares y edad5_sexo_colectivos)."""
    from sinpop.targets import run

    cfg = umbrales()["V-MARG"]
    filas = []
    for nivel in niveles:
        for t in _territorios(territorio, nivel):
            o = run.leer(t)
            obj = [
                o.filter(pl.col("objetivo") == f"edad5_sexo_{k}")["valor"].sum()
                for k in ("familiares", "colectivos")
            ]
            sub = _subconjunto(p, t)
            if sub.height == 0 or min(obj) <= 0:
                continue
            col = pl.col("tipo_residencia") == "establecimiento_colectivo"
            sint = [float(sub.filter(~col)["peso"].sum()), float(sub.filter(col)["peso"].sum())]
            n = sum(sint)
            filas.append(
                {
                    "nivel": nivel,
                    "territorio": t,
                    "objetivo": "tipo_residencia (implícito)",
                    "celdas": 2,
                    "n": n,
                    "tvd": M.tvd(sint, obj),
                    "hellinger": M.hellinger(sint, obj),
                    "tvd_ref": M.tvd_ref(
                        obj, max(1, round(n)), cfg["muestras_ref"], cfg["percentil_ref"], semilla
                    ),
                    "fuera_dominio": 0.0,
                }
            )
    return pl.DataFrame(filas)


def v_marg(p: pl.DataFrame, territorio: str, semilla: int = 0) -> pl.DataFrame:
    """V-MARG: TVD ≤ 1,2 · TVD_ref(N) + 0,002 en cada marginal calibrada (territorio y, si se
    calibró por comunidades, cada comunidad)."""
    c = umbrales()["V-MARG"]
    niveles = ["espana", "ccaa"] if territorio == "ES" else ["espana"]
    partes = [comparar(p, territorio, "calibrar", niveles, semilla)]
    res = _residencia(p, territorio, niveles, semilla)
    if res.height:  # los territorios por municipios no tienen objetivos de colectivos
        partes.append(res)
    df = pl.concat(partes, how="vertical_relaxed")
    return df.with_columns(
        (c["factor_tvd_ref"] * pl.col("tvd_ref") + c["tolerancia"]).alias("umbral")
    ).with_columns(
        ((pl.col("tvd") <= pl.col("umbral")) & (pl.col("fuera_dominio") == 0)).alias("ok")
    )


def v_cruce(p: pl.DataFrame, territorio: str, semilla: int = 0) -> pl.DataFrame:
    """V-CRUCE: TVD de los objetivos reservados ≤ máx(1,2 · TVD_ref(N) + 0,002, umbral del nivel)
    (D-038 A, aprobada). `ok_estricto` es el criterio original, máx(TVD_ref, umbral del nivel).
    `excepcion` marca los fallos aceptados como limitación de los datos (D-038 B)."""
    c = umbrales()["V-CRUCE"]
    lim = {"espana": c["espana"], "ccaa": c["ccaa"], "provincia": c["provincia"]}
    exc = {(e["territorio"], e["objetivo"]) for e in c.get("excepciones", [])}
    niveles = {"ES": ["espana", "ccaa", "provincia"]}.get(
        territorio, ["espana", "provincia"] if territorio.startswith("CCAA:") else ["espana"]
    )
    df = comparar(p, territorio, "reservar", niveles, semilla)
    nivel = pl.col("nivel").replace_strict(lim, return_dtype=pl.Float64)
    return df.with_columns(
        pl.max_horizontal(
            c.get("factor_tvd_ref", 1.0) * pl.col("tvd_ref") + c.get("tolerancia", 0.0), nivel
        ).alias("umbral"),
        pl.max_horizontal(pl.col("tvd_ref"), nivel).alias("umbral_estricto"),
        pl.struct("territorio", "objetivo")
        .map_elements(lambda r: (r["territorio"], r["objetivo"]) in exc, return_dtype=pl.Boolean)
        .alias("excepcion"),
    ).with_columns(
        (pl.col("tvd") <= pl.col("umbral")).alias("ok"),
        (pl.col("tvd") <= pl.col("umbral_estricto")).alias("ok_estricto"),
    )


def v_cramer(p: pl.DataFrame, territorio: str) -> pl.DataFrame:
    """V de Cramér de cada par de variables de los cruces reservados, sintética frente a oficial
    (nivel del territorio; D-038)."""
    from sinpop.targets import run

    lim = umbrales()["V-CRUCE"]["cramer_v_max_dif"]
    obj = run.leer(territorio).filter(
        (pl.col("uso") == "reservar") & pl.col("universo").is_in(list(UNIVERSOS))
    )
    r = D.recuentos(p, obj, "peso")
    filas = []
    for (o,), g in r.group_by("objetivo", maintain_order=True):
        vs = D.variables_de(o)
        if len(vs) < 2:
            continue
        partes = g.with_columns(
            [pl.col("clave").str.extract(f"(?:^|;){v}=([^;]+)").alias(v) for v in vs]
        )
        for a, b in combinations(vs, 2):
            t = partes.group_by(a, b).agg(pl.col("valor", "sintetico").sum())
            tab = {}
            for col in ("valor", "sintetico"):
                pv = t.pivot(on=b, index=a, values=col).fill_null(0).sort(a)
                tab[col] = pv.drop(a).select(sorted(pv.columns[1:])).to_numpy()
            vo, vsint = M.cramer_v(tab["valor"]), M.cramer_v(tab["sintetico"])
            filas.append(
                {
                    "objetivo": o,
                    "par": f"{a} × {b}",
                    "v_oficial": vo,
                    "v_sintetica": vsint,
                    "dif": abs(vsint - vo),
                    "ok": abs(vsint - vo) <= lim,
                }
            )
    return pl.DataFrame(filas)


# --- V-REGLAS --------------------------------------------------------------------------------

REGLAS_BLANDAS = {
    "jubilado_menor_50": (pl.col("relacion_actividad") == "jubilado_pensionista")
    & (pl.col("edad") < 50),
    "estudiante_50_o_mas": (pl.col("relacion_actividad") == "estudiante") & (pl.col("edad") >= 50),
    "ocupado_75_o_mas": (pl.col("relacion_actividad") == "ocupado") & (pl.col("edad") >= 75),
    "incapacidad_menor_25": (pl.col("relacion_actividad") == "incapacidad_permanente")
    & (pl.col("edad") < 25),
    "viudo_menor_30": (pl.col("estado_civil") == "viudo") & (pl.col("edad") < 30),
    "casado_menor_20": (pl.col("estado_civil") == "casado") & (pl.col("edad") < 20),
    "superior_20_21": (pl.col("estudios_3") == "superior") & (pl.col("edad") <= 21),
    "hogar_8_o_mas": pl.col("n_personas_hogar").fill_null(0) >= 8,
}


def v_reglas_duras(p: pl.DataFrame) -> pl.DataFrame:
    """Reglas de coherencia duras (0 violaciones)."""
    fam = p.filter(pl.col("tipo_residencia") == "vivienda_familiar")
    h = fam.group_by("household_id").agg(
        (pl.col("relacion_persona_ref") == "persona_referencia").sum().alias("nref"),
        pl.len().alias("n"),
        pl.col("tamano_hogar").first(),
        pl.col("tipo_hogar").first(),
        (pl.col("relacion_persona_ref") == "pareja").sum().alias("npar"),
        (pl.col("relacion_persona_ref") == "hijo").sum().alias("nhij"),
        pl.col("relacion_persona_ref").is_in(["otro_familiar", "no_familiar"]).sum().alias("noth"),
        pl.col("edad")
        .filter(pl.col("relacion_persona_ref") == "persona_referencia")
        .first()
        .alias("eref"),
        pl.col("edad").filter(pl.col("relacion_persona_ref") == "hijo").max().alias("ehijo"),
    )
    tam = pl.when(pl.col("n") >= 5).then(pl.lit("5+")).otherwise(pl.col("n").cast(pl.Utf8))
    t = pl.col("tipo_hogar")
    incoherente = (
        ((t == "unipersonal") != (pl.col("n") == 1))
        | (
            (t == "pareja_sin_hijos")
            & ~((pl.col("npar") > 0) & (pl.col("nhij") == 0) & (pl.col("noth") == 0))
        )
        | (
            (t == "pareja_con_hijos")
            & ~((pl.col("npar") > 0) & (pl.col("nhij") > 0) & (pl.col("noth") == 0))
        )
        | (
            (t == "monoparental")
            & ~((pl.col("npar") == 0) & (pl.col("nhij") > 0) & (pl.col("noth") == 0))
        )
        | (t.is_in(["otros", "varias_familias_no_emparentadas"]) & (pl.col("n") < 2))
    )
    reglas = {
        "una_persona_de_referencia_por_hogar": h.filter(pl.col("nref") != 1).height,
        "tamano_hogar_igual_a_personas": h.filter(tam != pl.col("tamano_hogar")).height,
        "progenitor_al_menos_12_anos_mayor": h.filter(pl.col("eref") - pl.col("ehijo") < 12).height,
        "ningun_menor_de_16_ocupado": p.filter(
            (pl.col("edad") < 16) & (pl.col("relacion_actividad") == "ocupado")
        ).height,
        "ningun_menor_de_19_con_estudios_superiores": p.filter(
            (pl.col("edad") < 19) & (pl.col("estudios_3") == "superior")
        ).height,
        "es_adulto_igual_a_edad_18": p.filter(pl.col("es_adulto") != (pl.col("edad") >= 18)).height,
        "nadie_en_dos_hogares": p.height
        - p["person_id"].n_unique()
        + p.filter(
            pl.col("household_id").is_null() & (pl.col("tipo_residencia") == "vivienda_familiar")
        ).height
        + p.filter(
            pl.col("household_id").is_not_null()
            & (pl.col("tipo_residencia") != "vivienda_familiar")
        ).height,
        "tipo_hogar_coherente_con_parentesco": h.filter(incoherente).height,
    }
    return pl.DataFrame({"regla": list(reglas), "violaciones": list(reglas.values())}).with_columns(
        (pl.col("violaciones") == 0).alias("ok")
    )


def frecuencias_blandas(p: pl.DataFrame, peso: str) -> dict[str, float]:
    tot = float(p[peso].sum())
    return {k: float(p.filter(e)[peso].sum()) / tot for k, e in REGLAS_BLANDAS.items()}


def v_reglas_blandas(p: pl.DataFrame, referencia: dict[str, float]) -> pl.DataFrame:
    """Frecuencia en la población ≤ 1,10 × la de los donantes calibrados. Se informa también el
    margen de muestreo (2 errores típicos de una muestra aleatoria simple de tamaño N): con N
    pequeño, un caso raro puede superar el 10 % solo por azar (D-038, pendiente de aprobación)."""
    lim = umbrales()["V-REGLAS-BLANDAS"]["exceso_relativo_max"]
    n = float(p["peso"].sum())
    sint = frecuencias_blandas(p, "peso")
    filas = []
    for k, f in sint.items():
        r = referencia[k]
        margen = 2 * float(np.sqrt(r * (1 - r) / n))
        filas.append(
            {
                "regla": k,
                "frecuencia_donantes": r,
                "frecuencia_sintetica": f,
                "exceso_relativo": f / r - 1 if r > 0 else (np.inf if f > 0 else 0.0),
                "ok_estricto": f <= (1 + lim) * r,
                "ok": f <= (1 + lim) * r + margen,
            }
        )
    return pl.DataFrame(filas)


def v_pesos(diagnosticos: dict[str, dict]) -> pl.DataFrame:
    c = umbrales()["V-PESOS"]
    filas = []
    for b, d in diagnosticos.items():
        filas.append(
            {
                "bloque": b,
                "desviacion_max": d["desviacion_max"],
                "proporcion_en_rango": d["proporcion_en_rango"],
                "kish_ratio": d["kish_ratio"],
                "no_positivos": d["no_positivos"],
                "factor_min": d["factor_cuantiles"]["min"],
                "factor_max": d["factor_cuantiles"]["max"],
                "proporcion_local": d.get("proporcion_local", 1.0),
                "ok": d["desviacion_max"] <= c["convergencia_max"]
                and d["proporcion_en_rango"] >= c["proporcion_en_rango"]
                and d["kish_ratio"] >= c["kish_min_ratio"]
                and d["no_positivos"] == 0,
            }
        )
    return pl.DataFrame(filas)


# --- Minorías (primera pasada, docs/05 §6) ---------------------------------------------------


def _referencias(territorio: str) -> dict[str, tuple[pl.Expr, float, str, str]]:
    """Grupo → (condición, proporción oficial, unidad, fuente) para los grupos de la lista de
    vigilancia que tienen referencia en los objetivos de F3."""
    from sinpop.targets import run

    o = run.leer(territorio)

    def prop(objetivo: str, patron: str) -> float:
        g = o.filter(pl.col("objetivo") == objetivo)
        return float(
            g.filter(pl.col("clave").str.contains(patron))["valor"].sum() / g["valor"].sum()
        )

    refs = {
        "mayores_85": (
            pl.col("edad") >= 85,
            prop("edad5_sexo", r"edad_5=(85-89|90\+)"),
            "persona",
            "ECP 2026 (edad5_sexo)",
        ),
        "municipios_menos_2000": (
            pl.col("tamano_municipio") == "hasta_2000",
            prop("tamano_municipio", "hasta_2000"),
            "persona",
            "Padrón 2025 (tamano_municipio)",
        ),
        "parados": (
            pl.col("relacion_actividad") == "parado",
            prop("actividad_sexo", "relacion_actividad=parado"),
            "persona",
            "Censo Anual 2024 (actividad_sexo)",
        ),
        "monoparentales": (
            pl.col("tipo_hogar") == "monoparental",
            prop("tipo_hogar", "tipo_hogar=monoparental"),
            "hogar",
            "Censo 2021 sobre hogares ECP 2026 (tipo_hogar)",
        ),
        "mayores_solos": (
            (pl.col("edad") >= 65) & (pl.col("tipo_hogar") == "unipersonal"),
            float(
                o.filter(
                    (pl.col("objetivo") == "tipo_hogar_edad4_ref")
                    & (pl.col("clave") == "tipo_hogar=unipersonal;edad_4=65+")
                )["valor"].sum()
                / o.filter(pl.col("objetivo") == "edad5_sexo")["valor"].sum()
            ),
            "persona",
            "Censo 2021 (tipo_hogar_edad4_ref) sobre residentes ECP 2026",
        ),
    }
    if territorio == "ES":
        refs["ceuta_melilla"] = (
            pl.col("ccaa").is_in(["18", "19"]),
            prop("provincia_si_calibra_ccaa", "provincia=(51|52)"),
            "persona",
            "ECP 2026 (provincias)",
        )
    top = o.filter(pl.col("objetivo") == "nacionalidad_top")
    for clave, v in top.select("clave", "valor").iter_rows():
        nac = clave.split("=", 1)[1]
        if nac in ("espanola", "otras_extranjeras"):
            continue
        refs[f"nacionalidad_{nac}"] = (
            pl.col("nacionalidad_top") == nac,
            v / top["valor"].sum(),
            "persona",
            "Censo Anual exhaustivo 2025 sobre ECP 2026 (nacionalidad_top)",
        )
    return refs


def v_minorias(p: pl.DataFrame, lineage: pl.DataFrame, territorio: str) -> pl.DataFrame:
    """V-MINORIAS (representación) y V-CONCENTRACION (donantes) de los grupos con referencia."""
    cm = umbrales()["V-MINORIAS"]
    cc = umbrales()["V-CONCENTRACION"]
    pl_ = p.join(lineage.select("person_id", "donante_household_id"), on="person_id")
    hog = pl_.filter(pl.col("relacion_persona_ref") == "persona_referencia")
    filas = []
    for g, (cond, q, unidad, fuente) in _referencias(territorio).items():
        base = hog if unidad == "hogar" else pl_
        n = float(base["peso"].sum())
        miembros = base.filter(cond)
        obs = float(miembros["peso"].sum())
        esperado = q * n
        if esperado >= cm["recuento_esperado_min"]:
            ratio_ok = cm["ratio"][0] <= obs / esperado <= cm["ratio"][1]
        else:
            se = float(np.sqrt(n * q * (1 - q)))
            ratio_ok = abs(obs - esperado) <= 1.96 * se
        don = pl_.filter(cond).group_by("donante_household_id").agg(pl.col("peso").sum())
        tam = float(pl_.filter(cond)["peso"].sum())
        top5 = float(don.sort("peso", descending=True).head(5)["peso"].sum() / tam) if tam else 0.0
        distintos = don.height
        min_dist = min(cc["donantes_distintos_min"], tam / cc["divisor_tamano_grupo"])
        filas.append(
            {
                "grupo": g,
                "unidad": unidad,
                "esperado": esperado,
                "observado": obs,
                "ratio": obs / esperado if esperado else None,
                "ok_representacion": ratio_ok,
                "donantes_distintos": distintos,
                "top5": top5,
                "ok_concentracion": top5 <= cc["top5_max"] and distintos >= min_dist,
                "fuente": fuente,
            }
        )
    return pl.DataFrame(filas)


# --- V-DONANTES y V-RAREZA -------------------------------------------------------------------

P0_PERSONA = [
    "edad",
    "sexo",
    "nacionalidad_grupo",
    "estudios_3",
    "relacion_actividad",
    "estado_civil",
]
P0_HOGAR = ["relacion_persona_ref", "tipo_hogar", "tamano_hogar"]


def v_donantes(p: pl.DataFrame, lineage: pl.DataFrame, territorio: str) -> pl.DataFrame:
    """V-DONANTES: tamaño efectivo de Kish de los hogares donantes usados (copias por hogar
    donante) ≥ 200 y porcentaje de personas de donantes locales, por territorio y comunidad."""
    c = umbrales()["V-DONANTES"]
    x = p.select("person_id", "ccaa").join(
        lineage.select("person_id", "donante_household_id", "local"), on="person_id"
    )
    filas = []
    grupos = [("ES" if territorio == "ES" else territorio, x)]
    if territorio == "ES":
        grupos += [(f"CCAA:{k}", g) for (k,), g in x.group_by("ccaa", maintain_order=True)]
    for t, g in sorted(grupos, key=lambda z: z[0]):
        copias = g.group_by("donante_household_id").agg(pl.len().alias("c"))["c"].to_numpy()
        k = M.kish(copias)
        loc = float(g["local"].mean())
        filas.append(
            {
                "territorio": t,
                "personas": g.height,
                "hogares_donantes": len(copias),
                "kish": k,
                "proporcion_local": loc,
                "ok": k >= c["kish_min"],
                "confianza_reducida": loc < c["locales_alerta"],
            }
        )
    return pl.DataFrame(filas)


def v_rareza(p: pl.DataFrame) -> pl.DataFrame:
    """V-RAREZA: combinaciones de atributos P0 de la población que no existen en ningún donante
    (0 con el método base). Los atributos de persona se comprueban en todos; los del hogar, en
    las viviendas familiares (en los colectivos no proceden)."""
    don = pl.scan_parquet(D.PERSONAS).select(*P0_PERSONA, *P0_HOGAR).collect()
    don = don.with_columns(  # D-038: actividad NP por debajo de 16 años, como en la población
        pl.when(pl.col("edad") < D.EDAD_MIN_ACTIVIDAD)
        .then(pl.lit("NP"))
        .otherwise(pl.col("relacion_actividad"))
        .alias("relacion_actividad")
    )
    filas = []
    for nombre, cols, sub in (
        ("persona", P0_PERSONA, p),
        (
            "persona_y_hogar",
            [*P0_PERSONA, *P0_HOGAR],
            p.filter(pl.col("tipo_residencia") == "vivienda_familiar"),
        ),
    ):
        combos = sub.select(cols).unique()
        nuevas = combos.join(don.select(cols).unique(), on=cols, how="anti")
        filas.append(
            {
                "nivel": nombre,
                "combinaciones": combos.height,
                "sin_donante": nuevas.height,
                "personas_afectadas": sub.join(nuevas, on=cols).height,
                "ok": nuevas.height == 0,
            }
        )
    return pl.DataFrame(filas)
