"""Referencias oficiales de los grupos vigilados (F7; docs/06 §2-3).

Para cada grupo y territorio: la proporción oficial del grupo dentro de su universo, su
intervalo (las encuestas tienen error de muestreo; las fuentes exhaustivas, no) y, si existe,
el perfil interno oficial (sexo, edad, estudios, actividad) para V-MINORIAS-PERFIL.

Fuentes, con el mismo universo que mide la población:
- objetivos de F3 (`data/processed/targets/`): ECP 2026, Padrón 2025, EPA 2T 2026 (actividad),
  Censo 2021 sobre hogares ECP 2026, nacionalidades (Censo Anual exhaustivo 2025);
- Censo Anual exhaustivo a 01/01/2025 (microdatos): nacidos fuera con nacionalidad española,
  perfil de los municipios de menos de 2.000 habitantes;
- Censo Anual a 01/01/2024, tabla 66601: «Sin estudios» (CNED-A nivel 0);
- ECV 2025 y TIC-H 2025: grupos del enriquecimiento, con IC 95 % por bootstrap (solo
  comunidades y España: las encuestas no son representativas por provincia).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.repro import make_rng

EDAD_4 = ["18-34", "35-49", "50-64", "65+"]


@dataclass
class Referencia:
    proporcion: float
    fuente: str
    ic: tuple[float, float] | None = None  # solo las encuestas
    perfiles: dict[str, pl.DataFrame] = field(default_factory=dict)  # variable → (categoria, p)
    nota: str = ""


def _provincias(territorio: str) -> list[str] | None:
    """Provincias del territorio (None = España). En las listas de municipios, sus provincias."""
    from sinpop.synth.pesos import provincias_bloque

    if territorio == "ES":
        return None
    return provincias_bloque(territorio)


def _ccaa(territorio: str) -> list[str] | None:
    from sinpop.harmonize.core import ccaa_de_provincia

    ps = _provincias(territorio)
    return None if ps is None else sorted({ccaa_de_provincia()[p] for p in ps})


def _perfil(df: pl.DataFrame, var: str, peso: str) -> pl.DataFrame:
    g = df.group_by(var).agg(pl.col(peso).sum().alias("w"))
    return g.select(
        pl.col(var).cast(pl.Utf8).alias("categoria"), (pl.col("w") / pl.col("w").sum()).alias("p")
    )


# --------------------------------------------------------------------------- objetivos de F3


def _objetivos(territorio: str) -> pl.DataFrame:
    from sinpop.targets import run

    return run.leer(territorio)


def _prop_objetivo(
    o: pl.DataFrame, objetivo: str, patron: str, excluir: str | None = None
) -> float | None:
    """Proporción de las celdas `patron` en el objetivo; None si el territorio no lo tiene."""
    g = o.filter(pl.col("objetivo") == objetivo)
    if excluir:
        g = g.filter(~pl.col("clave").str.contains(excluir))
    den = float(g["valor"].sum())
    if not den:
        return None
    return float(g.filter(pl.col("clave").str.contains(patron))["valor"].sum()) / den


def _perfil_objetivo(o: pl.DataFrame, objetivo: str, filtro: str, var: str) -> pl.DataFrame:
    g = o.filter((pl.col("objetivo") == objetivo) & pl.col("clave").str.contains(filtro))
    g = g.with_columns(pl.col("clave").str.extract(f"(?:^|;){var}=([^;]+)").alias("categoria"))
    g = g.group_by("categoria").agg(pl.col("valor").sum())
    return g.select("categoria", (pl.col("valor") / pl.col("valor").sum()).alias("p"))


# --------------------------------------------------------------------------- Censo Anual 2025


@lru_cache(maxsize=1)
def _exhaustivo() -> pl.DataFrame:
    from sinpop.harmonize.core import ccaa_de_provincia

    d = pl.read_parquet(
        INTERIM_DIR / "censo_anual_exhaustivo_2025.parquet",
        columns=[
            "edad",
            "sexo",
            "provincia",
            "tamano_municipio",
            "nacionalidad_grupo",
            "pais_nacimiento_grupo",
            "personas",
        ],
    )
    return d.with_columns(pl.col("provincia").replace_strict(ccaa_de_provincia()).alias("ccaa"))


def _edad_grupos(edad: pl.Expr) -> pl.Expr:
    return (
        pl.when(edad < 18)
        .then(pl.lit("00-17"))
        .when(edad < 35)
        .then(pl.lit("18-34"))
        .when(edad < 50)
        .then(pl.lit("35-49"))
        .when(edad < 65)
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
        .alias("edad_grupo")
    )


# --------------------------------------------------------------------------- encuestas


@lru_cache(maxsize=4)
def _encuesta(nombre: str) -> pl.DataFrame:
    return pl.read_parquet(INTERIM_DIR / f"{nombre}.parquet")


def _ic_bootstrap(
    d: pl.DataFrame, en_grupo: pl.Expr, peso: str, conglomerado: str | None, semilla: int = 0
) -> tuple[float, float, float]:
    x = d.select(en_grupo.cast(pl.Float64).alias("g"), pl.col(peso).alias("w"))
    g, w = x["g"].to_numpy(), x["w"].to_numpy().astype(float)
    p = float((g * w).sum() / w.sum())
    if conglomerado:
        k = d[conglomerado].rank("dense").cast(pl.Int64).to_numpy() - 1
        n = int(k.max()) + 1
    else:
        k, n = None, len(g)
    rng = make_rng(semilla)
    reps = np.empty(400)
    for b in range(len(reps)):
        m = rng.poisson(1.0, n)
        wb = w * (m[k] if k is not None else m)
        reps[b] = (g * wb).sum() / wb.sum()
    lo, hi = np.percentile(reps, [2.5, 97.5])
    return p, float(lo), float(hi)


def _ref_encuesta(
    nombre: str,
    universo: pl.Expr,
    en_grupo: pl.Expr,
    peso: str,
    conglomerado: str | None,
    territorio: str,
    fuente: str,
) -> Referencia | None:
    cc = _ccaa(territorio)
    d = _encuesta(nombre).filter(universo)
    nota = ""
    if cc is not None:
        d = d.filter(pl.col("ccaa").is_in(cc))
        if not territorio.startswith("CCAA:"):
            nota = "referencia de la comunidad: la encuesta no es representativa por provincia"
    if d.height < 30:
        return None
    p, lo, hi = _ic_bootstrap(d, en_grupo, peso, conglomerado)
    sub = d.filter(en_grupo)
    perfiles = {}
    for v in ("sexo", "edad_4", "estudios_3", "relacion_actividad"):
        if v in sub.columns and sub.height >= 30:
            s = sub.filter(~pl.col(v).is_in(["NC", "NS"]))
            if v == "edad_4":
                s = s.filter(pl.col(v).is_in(EDAD_4))
            if s.height >= 30:
                perfiles[v] = _perfil(s, v, peso)
    return Referencia(p, fuente, (lo, hi), perfiles, nota)


# --------------------------------------------------------------------------- referencia por grupo


def referencia(grupo: str, territorio: str) -> Referencia | None:
    """Referencia oficial del grupo en el territorio, o None si no existe (también si el
    territorio no tiene el objetivo del que sale, p. ej. una lista de municipios)."""
    r = _referencia(grupo, territorio)
    return None if r is None or r.proporcion is None else r


def _referencia(grupo: str, territorio: str) -> Referencia | None:
    o = _objetivos(territorio)
    if grupo == "mayores_85":
        return Referencia(
            _prop_objetivo(o, "edad5_sexo", r"edad_5=(85-89|90\+)"),
            "ECP 2026 (residentes por edad y sexo)",
            perfiles={"sexo": _perfil_objetivo(o, "edad5_sexo", r"edad_5=(85-89|90\+)", "sexo")},
        )
    if grupo == "mayores_solos":
        num = o.filter(
            (pl.col("objetivo") == "tipo_hogar_edad4_ref")
            & (pl.col("clave") == "tipo_hogar=unipersonal;edad_4=65+")
        )["valor"].sum()
        den = o.filter(pl.col("objetivo") == "edad5_sexo_familiares")["valor"].sum()
        if not den:
            return None
        return Referencia(
            float(num / den),
            "Censo 2021 (hogares unipersonales de 65+) sobre residentes en viviendas familiares "
            "ECP 2026",
        )
    if grupo == "ceuta_melilla":
        if territorio != "ES":
            return None
        return Referencia(
            _prop_objetivo(o, "provincia_si_calibra_ccaa", "provincia=(51|52)"),
            "ECP 2026 (residentes por provincia)",
        )
    if grupo == "municipios_menos_2000":
        q = _prop_objetivo(o, "tamano_municipio", "hasta_2000")
        perf = {}
        ps = _provincias(territorio)
        e = _exhaustivo().filter(pl.col("tamano_municipio") == "hasta_2000")
        if ps is not None:
            e = e.filter(pl.col("provincia").is_in(ps))
        if e.height and not territorio.startswith("MUNIS:"):
            perf = {
                "sexo": _perfil(e, "sexo", "personas"),
                "edad_grupo": _perfil(
                    e.with_columns(_edad_grupos(pl.col("edad"))), "edad_grupo", "personas"
                ),
            }
        return Referencia(q, "Padrón 2025 (población por tamaño de municipio)", perfiles=perf)
    if grupo == "nacidos_fuera_espanoles":
        if territorio.startswith("MUNIS:"):
            return None
        ps = _provincias(territorio)
        e = _exhaustivo()
        if ps is not None:
            e = e.filter(pl.col("provincia").is_in(ps))
        cond = (pl.col("pais_nacimiento_grupo") != "espana") & (
            pl.col("nacionalidad_grupo") == "espanola"
        )
        sub = e.filter(cond)
        return Referencia(
            float(sub["personas"].sum() / e["personas"].sum()),
            "Censo Anual exhaustivo a 01/01/2025 (microdatos)",
            perfiles={
                "sexo": _perfil(sub, "sexo", "personas"),
                "edad_grupo": _perfil(
                    sub.with_columns(_edad_grupos(pl.col("edad"))), "edad_grupo", "personas"
                ),
            },
        )
    if grupo == "monoparentales":
        return Referencia(
            _prop_objetivo(o, "tipo_hogar", "tipo_hogar=monoparental"),
            "Censo 2021 (tipo de hogar por tamaño) sobre hogares ECP 2026",
        )
    if grupo == "parados":
        return Referencia(
            _prop_objetivo(
                o, "actividad_sexo", "relacion_actividad=parado", excluir="relacion_actividad=NP"
            ),
            "EPA 2T 2026 con el reparto del Censo Anual 2024 (objetivo actividad_sexo, D-046)",
            perfiles={
                "sexo": _perfil_objetivo(o, "actividad_sexo", "relacion_actividad=parado", "sexo"),
                "edad_actividad": _perfil_objetivo(
                    o, "actividad_edad", "relacion_actividad=parado", "edad_actividad"
                ),
            },
        )
    if grupo == "sin_estudios":
        return _ref_sin_estudios(territorio)
    if grupo.startswith("nacionalidad_"):
        nac = grupo.removeprefix("nacionalidad_")
        top = o.filter(pl.col("objetivo") == "nacionalidad_top")
        q = float(
            top.filter(pl.col("clave") == f"nacionalidad_top={nac}")["valor"].sum()
            / top["valor"].sum()
        )
        perf = {}
        se = o.filter(pl.col("objetivo") == "nacionalidad_top_sexo_edad")
        if se.height:
            perf = {
                "sexo": _perfil_objetivo(
                    o, "nacionalidad_top_sexo_edad", f"nacionalidad_top={nac};", "sexo"
                ),
                "edad_nacionalidad": _perfil_objetivo(
                    o, "nacionalidad_top_sexo_edad", f"nacionalidad_top={nac};", "edad_nacionalidad"
                ),
            }
        return Referencia(
            q,
            "Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top)",
            perfiles=perf,
        )
    fam16 = (pl.col("edad") >= 16) & pl.col("peso_16").is_not_null()
    if grupo == "limitacion_grave":
        return _ref_encuesta(
            "ecv",
            fam16 & ~pl.col("discapacidad_limitacion").is_in(["NP"]),
            pl.col("discapacidad_limitacion") == "limitacion_grave",
            "peso_16",
            "household_id",
            territorio,
            "ECV 2025 (16+, viviendas familiares)",
        )
    if grupo == "privacion_severa":
        return _ref_encuesta(
            "ecv",
            fam16 & ~pl.col("privacion_material").is_in(["NP"]),
            pl.col("privacion_material") == "si",
            "peso_16",
            "household_id",
            territorio,
            "ECV 2025 (16+, viviendas familiares; vrMATSOCDEP)",
        )
    if grupo == "jovenes_ni_ni":
        return _ref_encuesta(
            "ecv",
            fam16 & pl.col("edad").is_between(18, 24) & ~pl.col("relacion_actividad").is_in(["NP"]),
            ~pl.col("relacion_actividad").is_in(["ocupado", "estudiante"]),
            "peso_16",
            "household_id",
            territorio,
            "ECV 2025 (18-24, viviendas familiares)",
        )
    if grupo == "nunca_internet":
        return _ref_encuesta(
            "tic_h",
            pl.col("edad") >= 16,
            pl.col("uso_internet") == "nunca",
            "peso",
            None,
            territorio,
            "TIC-H 2025 (16+, viviendas familiares)",
        )
    return None


def _ref_sin_estudios(territorio: str) -> Referencia | None:
    """«Sin estudios» de la tabla 66601 (Censo Anual a 01/01/2024) sobre la población de 15+."""
    from sinpop.targets import fuentes

    if territorio.startswith("MUNIS:"):
        return None
    cortes = [15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90]
    t, n = fuentes._leer("tabla_66601_ultimo.json")
    e = fuentes.tabla_estructura(
        t, n, "Nivel de formación alcanzado", {k: k for k in fuentes.ESTUDIOS}, cortes
    )
    ps = _provincias(territorio)
    if ps is not None:
        e = e.filter(pl.col("provincia").is_in(ps))
    sub = e.filter(pl.col("categoria") == "Sin estudios")
    return Referencia(
        float(sub["valor"].sum() / e["valor"].sum()),
        "Censo Anual a 01/01/2024, tabla 66601 («Sin estudios», 15+)",
        perfiles={"sexo": _perfil(sub, "sexo", "valor")},
    )
