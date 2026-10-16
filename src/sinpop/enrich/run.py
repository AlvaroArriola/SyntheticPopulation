"""Etapa 5: enriquecimiento de una población (D-044).

Bloques, en este orden (cada uno hereda todas sus variables del mismo donante):

1. Hogar (ECV): renta, deciles, tenencia detallada, fin de mes y vehículo, para cada hogar
   familiar, con la tenencia compatible con la del Censo y la inclinación al Atlas por provincia.
2. Persona (ECV): salud, limitación (GALI) y carencia material y social, 16+, con el decil del
   hogar como llave.
3. Empleo (EPA): jornada y sector público, ocupados de 16+.
4. Digital (TIC-H): uso de internet, compra en línea y teletrabajo, 16+.
5. Contexto: renta media del municipio (Atlas) y envejecimiento (Censo Anual).

Los residentes en colectivos están fuera del universo de las encuestas (viviendas familiares):
reciben los bloques personales por extrapolación (mismas llaves, sin las del hogar) y se marcan
`extrapolada`; las variables del hogar son NP.
"""

from __future__ import annotations

import hashlib

import numpy as np
import polars as pl

from sinpop.enrich import contexto as CTX
from sinpop.enrich import fuentes as F
from sinpop.enrich import hotdeck as HD
from sinpop.repro import make_rng

K_MIN = 5

# Llaves de cada bloque por orden de importancia (asociación con las variables del bloque en
# la propia encuesta, D-044) y geografía de colapso: comunidad → zona NUTS-1 → España. Con todas
# las llaves se prueba antes una geografía más amplia que quitar una llave (`claves_primero`).
ESTRATEGIA: dict[str, dict] = {
    "modo": "nucleo",
    # Tenencia del Censo 2021 como llave fija (D-044.3): True, False o "salvo_extranjeros" (D-045)
    "tenencia_fija": "salvo_extranjeros",
    "nucleo": 2,
    "hogar": [
        "ocupados",
        "estudios_max",
        "extranjero",
        "mayores_65",
        "menores",
        "tamano_hogar_4",
        "grado_urbanizacion",
    ],
    "persona_ecv": [
        "edad_grupo",
        "relacion_actividad",
        "estudios_3",
        "renta_quintil",
        "nacionalidad_esp_ext",
        "sexo",
    ],
    # situacion_3 es llave fija: un autónomo o un empresario no puede ser del sector público
    # y la nacionalidad va pronto: el empleo público exige en general la nacionalidad española
    "empleo": ["ocupacion", "nacionalidad_esp_ext", "sexo", "edad_grupo_epa", "estudios_3"],
    "digital": ["edad_grupo", "relacion_actividad", "estudios_3", "nacionalidad_esp_ext", "sexo"],
}
GEOGRAFIA: list[str | None] = ["ccaa", "nuts1", None]


def niveles(bloque: str, quitar: tuple[str, ...] = ()) -> list[list[str]]:
    llaves = [k for k in ESTRATEGIA[bloque] if k not in quitar]
    if ESTRATEGIA["modo"] == "claves_primero":
        return HD.niveles_colapso(llaves, GEOGRAFIA)
    if ESTRATEGIA["modo"] == "nucleo":
        return HD.niveles_nucleo(llaves, GEOGRAFIA, min(ESTRATEGIA["nucleo"], len(llaves)))
    # geografía primero: comunidad con todas las llaves y quitando llaves; al final, España
    return [["ccaa", *llaves[:k]] for k in range(len(llaves), -1, -1)] + [[]]


VARIABLES_HOGAR = [v for v in F.BLOQUE_HOGAR if v != "renta_equivalente"]


def semilla_bloque(semilla: int, bloque: str) -> int:
    h = hashlib.sha256(f"{semilla}|enriquecimiento|{bloque}".encode()).hexdigest()
    return int(h[:8], 16)


# --------------------------------------------------------------------------- renta y Atlas


def media_ecv_ccaa() -> dict[str, float]:
    """Media ponderada (personas, RB050) de la renta equivalente por comunidad."""
    e = F._ecv()
    g = e.group_by("ccaa").agg(
        ((pl.col("renta_equivalente") * pl.col("peso")).sum() / pl.col("peso").sum()).alias("m")
    )
    return dict(g.iter_rows())


def objetivos_renta(unidades: pl.DataFrame) -> pl.DataFrame:
    """Media objetivo de la renta equivalente de cada unidad de inclinación (D-044.5):
    media ECV de su comunidad × (Atlas de la unidad / Atlas de la comunidad), con la media de la
    renta por unidad de consumo del Atlas 2023. `unidades`: unidad, ccaa, atlas."""
    at = CTX.atlas_territorios()
    a_cc = dict(at.filter(pl.col("nivel") == "ccaa").select("codigo", "renta_uc_media").iter_rows())
    m = media_ecv_ccaa()
    return unidades.with_columns(
        pl.struct("ccaa", "atlas")
        .map_elements(
            lambda r: m[r["ccaa"]] * r["atlas"] / a_cc[r["ccaa"]], return_dtype=pl.Float64
        )
        .alias("objetivo")
    )


def unidades_inclinacion(hogares: pl.DataFrame, territorio: str) -> pl.DataFrame:
    """Unidad de inclinación de cada hogar y su valor del Atlas (renta por unidad de consumo).
    Provincia en España, comunidades y provincias; en una lista de municipios, la parte de cada
    comunidad (Atlas: media de sus municipios ponderada por población del Padrón 2025)."""
    at = CTX.atlas_territorios()
    if territorio.startswith("MUNIS:"):
        from sinpop.targets.municipios import padron

        m = (
            padron()
            .join(CTX.atlas_municipios(), on="municipio")
            .filter(pl.col("municipio").is_in(hogares["municipio"].drop_nulls().unique()))
        )
        a = (
            m.with_columns(pl.col("provincia").alias("_p"))
            .join(hogares.select("provincia", "ccaa").unique(), on="provincia")
            .group_by("ccaa")
            .agg(
                (
                    (pl.col("renta_uc_media") * pl.col("poblacion")).sum()
                    / pl.col("poblacion").sum()
                ).alias("atlas")
            )
        )
        return (
            hogares.select("ccaa")
            .with_row_index("_i")
            .join(a, on="ccaa", how="left")
            .sort("_i")
            .select(pl.col("ccaa").alias("unidad"), "ccaa", "atlas")
        )
    a_p = at.filter(pl.col("nivel") == "provincia").select(
        pl.col("codigo").alias("provincia"), pl.col("renta_uc_media").alias("atlas")
    )
    return (
        hogares.select("provincia", "ccaa")
        .with_row_index("_i")
        .join(a_p, on="provincia", how="left")
        .sort("_i")
        .select(pl.col("provincia").alias("unidad"), "ccaa", "atlas")
    )


def _lambda(medias_celdas, objetivo: float) -> float:
    """λ tal que la media esperada (ponderada por personas) de las celdas inclinadas sea el
    objetivo; bisección en la escala de la renta relativa (renta / media de los donantes)."""
    lo, hi = -8.0, 8.0
    f = medias_celdas
    if not f(lo) <= objetivo <= f(hi):
        return lo if objetivo < f(lo) else hi
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(mid) < objetivo:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def bloque_hogar(
    hogares: pl.DataFrame,
    personas_fam: pl.DataFrame,
    territorio: str,
    semilla: int,
    quitar: tuple[str, ...] = (),
) -> tuple[pl.DataFrame, dict]:
    don = F.donantes_hogar().with_columns(F.nuts1())
    tenencias = set(hogares["tenencia_censo"].unique())
    if not tenencias <= {"propiedad", "alquiler", "otro"}:
        raise ValueError(f"tenencia del Censo no prevista: {tenencias}")
    rec = hogares.join(F.rasgos_hogar(personas_fam), on="household_id", how="left").with_columns(
        F.nuts1()
    )
    nv = niveles("hogar", quitar)
    # Tenencia (D-045): fija con la del Censo 2021 salvo, según la estrategia, en los hogares con
    # algún adulto extranjero, cuyo régimen ha cambiado mucho desde 2021 (la ECV decide).
    modo = ESTRATEGIA["tenencia_fija"]
    libre = (
        pl.lit(False)
        if modo is True
        else (pl.col("extranjero") == "true")
        if modo == "salvo_extranjeros"
        else pl.lit(True)
    )
    marca = rec.select(libre.alias("_l"))["_l"].to_numpy()
    celda = np.empty(rec.height, dtype=np.int64)
    nivel = np.empty(rec.height, dtype=np.int64)
    tablas = []
    base = 0
    unico = don.with_row_index("_fila").unique("household_id", keep="first")
    for libre_g in (False, True):
        idx = np.flatnonzero(marca == libre_g)
        if not len(idx):
            continue
        r_g = rec[idx]
        if libre_g:
            c, n, t = HD.celdas(r_g, unico, nv, [], K_MIN)
            filas = unico["_fila"].to_numpy()
            t = t.with_columns(pl.Series("_d", filas[t["_d"].to_numpy()].astype(np.int64)))
        else:
            c, n, t = HD.celdas(r_g, don, nv, ["tenencia_censo"], K_MIN)
        celda[idx] = c + base
        nivel[idx] = n
        tablas.append(t.with_columns(pl.col("_c") + base))
        base += int(t["_c"].max()) + 1
    tabla = pl.concat(tablas)
    x = don["renta_equivalente"].to_numpy().astype(float)
    escala = float(np.average(x, weights=don["peso_hogar"].to_numpy()))
    xr = x / escala
    w = don["peso_hogar"].to_numpy().astype(float)
    uni = unidades_inclinacion(rec, territorio)
    obj = objetivos_renta(uni.unique(["unidad", "ccaa"]).drop_nulls("atlas"))
    n_pers = rec["n_personas_hogar"].to_numpy().astype(float)
    t = tabla.sort("_c", "_d")
    tc, td = t["_c"].to_numpy(), t["_d"].to_numpy()
    rng = make_rng(semilla_bloque(semilla, "hogar"))
    donante = np.empty(len(celda), dtype=np.int64)
    informe = []
    unidad_r = uni["unidad"].to_numpy()
    for u in sorted(set(unidad_r)):
        idx = np.flatnonzero(unidad_r == u)
        fila = obj.filter(pl.col("unidad") == u)
        cel_u = celda[idx]
        usadas = np.unique(cel_u)
        en = np.isin(tc, usadas)
        cc, dd = tc[en], td[en]
        pesos_c = np.bincount(
            np.searchsorted(usadas, cel_u), weights=n_pers[idx], minlength=len(usadas)
        )

        def media(lam: float, cc=cc, dd=dd, pesos_c=pesos_c, usadas=usadas) -> float:
            ww = w[dd] * np.exp(lam * (xr[dd] - 1))
            k = np.searchsorted(usadas, cc)
            m = np.bincount(k, weights=ww * x[dd], minlength=len(usadas)) / np.bincount(
                k, weights=ww, minlength=len(usadas)
            )
            return float((m * pesos_c).sum() / pesos_c.sum())

        lam = 0.0
        objetivo = None
        if fila.height:
            objetivo = float(fila["objetivo"][0])
            lam = _lambda(media, objetivo)
        pesos = w * np.exp(lam * (xr - 1))
        donante[idx] = HD.muestrear(cel_u, tabla.filter(pl.col("_c").is_in(usadas)), pesos, rng)
        informe.append(
            {
                "unidad": u,
                "lambda": lam,
                "objetivo": objetivo,
                "esperada_sin_inclinar": media(0.0),
                "esperada": media(lam),
                "hogares": int(len(idx)),
            }
        )
    dsel = don[donante]
    out = pl.concat([rec.select("household_id"), dsel.select(F.BLOQUE_HOGAR)], how="horizontal")
    return out, {"inclinacion": informe, "niveles": _niveles(nivel, nv)}


def _niveles(nivel: np.ndarray, nv: list[list[str]]) -> dict[str, int]:
    v, c = np.unique(nivel, return_counts=True)
    return {"+".join(nv[int(a)]) or "españa": int(b) for a, b in zip(v, c, strict=True)}


# --------------------------------------------------------------------------- bloques personales


def _personales(
    rec: pl.DataFrame,
    don: pl.DataFrame,
    nv: list[list[str]],
    peso: str,
    variables: list[str],
    semilla: int,
    bloque: str,
    fijas: list[str] | None = None,
) -> tuple[pl.DataFrame, dict]:
    if rec.is_empty():
        return rec.select("_i").with_columns(
            [pl.lit(None, dtype=don.schema[v]).alias(v) for v in variables]
        ), {}
    a = HD.emparejar(rec, don, nv, peso, make_rng(semilla_bloque(semilla, bloque)), fijas, K_MIN)
    out = pl.concat([rec.select("_i"), don[a.donante].select(variables)], how="horizontal")
    return out, {"niveles": _niveles(a.nivel, nv)}


def _llaves_persona(df: pl.DataFrame) -> pl.DataFrame:
    """Llaves derivadas, con la misma definición en la población y en las encuestas."""
    out = df.with_columns(
        F.nuts1(),
        F.grupo_edad(pl.col("edad"), F.EDAD_10, "edad_grupo"),
        (pl.col("relacion_actividad") == "ocupado").cast(pl.Utf8).alias("ocupado"),
    )
    if "situacion_profesional" in out.columns:
        out = out.with_columns(F.situacion_3())
    if "renta_hogar_decil" in out.columns:
        # Sin hogar (colectivos): el decil no se conoce y no se usa como llave
        out = out.with_columns(F.quintil()).with_columns(pl.col("renta_quintil").fill_null("NC"))
    return out


def enriquecer(
    personas: pl.DataFrame,
    hogares: pl.DataFrame,
    territorio: str,
    semilla: int,
    quitar: tuple[str, ...] = (),
) -> tuple[pl.DataFrame, pl.DataFrame, dict]:
    """Devuelve personas y hogares con las variables enriquecidas y su `__calidad`, y la
    metadata del enriquecimiento. No modifica ninguna columna existente. `quitar`: llaves que
    no se usan (prueba V-ENRIQ-HOLDOUT)."""
    p = personas.with_row_index("_i")
    fam = pl.col("tipo_residencia") == "vivienda_familiar"
    meta: dict = {"k_min": K_MIN, "estrategia": ESTRATEGIA, "geografia": GEOGRAFIA, "bloques": {}}
    if quitar:
        meta["llaves_quitadas"] = list(quitar)

    # 1. Hogar (ECV)
    q_hogar = tuple("estudios_max" if k == "estudios_3" else k for k in quitar)
    hb, info = bloque_hogar(hogares, p.filter(fam), territorio, semilla, q_hogar)
    meta["bloques"]["hogar"] = {"fuente": "ecv", **info}
    hog = hogares.join(hb, on="household_id", how="left")
    p = p.join(hb, on="household_id", how="left").sort("_i")
    p = _llaves_persona(p).with_columns(F.grupo_edad(pl.col("edad"), F.EDAD_EPA, "edad_grupo_epa"))

    adulto = pl.col("edad") >= 16
    colect = ~fam
    especs = [
        (
            "persona_ecv",
            "ecv",
            _llaves_persona(F.donantes_persona_ecv()),
            "peso_16",
            F.BLOQUE_PERSONA_ECV,
            adulto,
            None,
        ),
        (
            "empleo",
            "epa",
            F.donantes_empleo().with_columns(F.nuts1()),
            "peso",
            F.BLOQUE_EMPLEO,
            adulto & (pl.col("relacion_actividad") == "ocupado"),
            ["situacion_3"],
        ),
        (
            "digital",
            "tic_h",
            _llaves_persona(F.donantes_digital()),
            "peso",
            F.BLOQUE_DIGITAL,
            adulto,
            ["ocupado"],
        ),
    ]
    for bloque, fuente, don, peso, variables, universo, fijas in especs:
        rec = p.filter(universo)
        nv = niveles(bloque, quitar)
        sal, info = _personales(rec, don, nv, peso, variables, semilla, bloque, fijas)
        meta["bloques"][bloque] = {"fuente": fuente, **info}
        p = p.join(sal, on="_i", how="left").sort("_i")
        calidad = (
            pl.when(~universo)
            .then(pl.lit("observada"))
            .when(colect)
            .then(pl.lit("extrapolada"))
            .otherwise(pl.lit("emparejada"))
        )
        p = p.with_columns(
            [
                pl.when(universo).then(pl.col(v)).otherwise(_np(don.schema[v])).alias(v)
                for v in variables
            ]
            + [calidad.alias(f"{v}__calidad") for v in variables]
        )

    # Variables del hogar: NP en colectivos (fuera del universo de la ECV)
    p = p.with_columns(
        [pl.col(v).fill_null(_np(p.schema[v])) for v in VARIABLES_HOGAR]
        + [
            pl.when(fam)
            .then(pl.lit("emparejada"))
            .otherwise(pl.lit("observada"))
            .alias(f"{v}__calidad")
            for v in VARIABLES_HOGAR
        ]
    ).drop("renta_equivalente")
    hog = hog.with_columns([pl.lit("emparejada").alias(f"{v}__calidad") for v in F.BLOQUE_HOGAR])

    # 5. Contexto
    p = pl.concat([p, CTX.contexto(p)], how="horizontal")
    p = p.drop(
        "_i", "nuts1", "edad_grupo", "edad_grupo_epa", "situacion_3", "ocupado", "renta_quintil"
    )
    meta["fuentes"] = {
        "ecv": "ECV 2025 (INE)",
        "epa": "EPA 2T 2026 (INE)",
        "tic_h": "TIC-H 2025 (INE)",
        "atlas_renta": "Atlas de distribución de renta de los hogares 2023 (INE)",
        "censo_anual": "Censo Anual exhaustivo 2025 (INE)",
    }
    return p, hog, meta


def _np(dtype: pl.DataType) -> pl.Expr:
    """NP en variables categóricas; nulo en las numéricas (fuera de universo)."""
    return pl.lit("NP") if dtype == pl.Utf8 else pl.lit(None, dtype=dtype)
