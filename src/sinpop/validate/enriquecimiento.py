"""Validación del enriquecimiento (docs/05 §5; D-044.9).

Cada variable enriquecida se compara con su encuesta de origen, en el mismo universo a los dos
lados: personas de viviendas familiares (las encuestas no cubren los colectivos), de 18 o más
años (los grupos `edad_4`), con sus pesos oficiales.

- V-ENRIQ-MARG: proporción de cada categoría por comunidad × edad_4 dentro del IC del 95 % de la
  encuesta (bootstrap de Poisson por conglomerado: hogar en la ECV, persona en la EPA y la
  TIC-H) en ≥ 90 % de las celdas; TVD nacional ≤ 0,02.
- V-ENRIQ-ASOC: |Δ V de Cramér| ≤ 0,05 entre cada variable enriquecida y cada llave.
- V-ENRIQ-BLOQUE: |Δ V de Cramér| entre las variables de cada bloque: máximo ≤ 0,05, media ≤ 0,02.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.enrich import fuentes as F
from sinpop.repro import make_rng
from sinpop.validate import metrics as M

EDADES = ["18-34", "35-49", "50-64", "65+"]
CARENCIAS = (
    pl.when(pl.col("privacion_material_n") >= 7)
    .then(pl.lit("7+"))
    .otherwise(pl.col("privacion_material_n").cast(pl.Int64).cast(pl.Utf8))
)


@dataclass(frozen=True)
class Bloque:
    nombre: str
    fuente: str
    variables: tuple[str, ...]
    llaves: tuple[str, ...]
    peso: str
    conglomerado: str | None


BLOQUES = (
    Bloque(
        "hogar",
        "ecv",
        tuple(v for v in F.BLOQUE_HOGAR if v != "renta_equivalente"),
        ("estudios_3", "relacion_actividad", "nacionalidad_esp_ext", "sexo", "grado_urbanizacion"),
        "peso",
        "household_id",
    ),
    Bloque(
        "persona_ecv",
        "ecv",
        ("salud_autopercibida", "discapacidad_limitacion", "privacion_material", "carencias"),
        ("sexo", "relacion_actividad", "estudios_3", "renta_hogar_decil", "nacionalidad_esp_ext"),
        "peso_16",
        "household_id",
    ),
    Bloque(
        "empleo",
        "epa",
        tuple(F.BLOQUE_EMPLEO),
        ("sexo", "ocupacion", "situacion_3", "estudios_3", "nacionalidad_esp_ext"),
        "peso",
        None,
    ),
    Bloque(
        "digital",
        "tic_h",
        tuple(F.BLOQUE_DIGITAL),
        ("sexo", "relacion_actividad", "estudios_3", "nacionalidad_esp_ext"),
        "peso",
        None,
    ),
)


def _universo(df: pl.DataFrame, bloque: Bloque, sintetica: bool) -> pl.DataFrame:
    """Mismo universo a los dos lados (18+, viviendas familiares; ocupados en el empleo; 20+
    en la EPA, que no separa a los de 18 y 19)."""
    d = df
    if sintetica:
        d = d.filter(pl.col("tipo_residencia") == "vivienda_familiar")
    d = d.filter(pl.col("edad_4").is_in(EDADES))
    if bloque.nombre == "empleo":
        if sintetica:
            d = d.filter((pl.col("relacion_actividad") == "ocupado") & (pl.col("edad") >= 20))
        else:
            d = d.filter(pl.col("tipo_jornada").is_in(["completa", "parcial"]))
        d = d.with_columns(F.situacion_3())
    if bloque.nombre == "persona_ecv" or "privacion_material_n" in d.columns:
        d = d.with_columns(CARENCIAS.fill_null("NP").alias("carencias"))
    return d


@lru_cache(maxsize=4)
def encuesta(nombre: str) -> pl.DataFrame:
    return pl.read_parquet(INTERIM_DIR / f"{nombre}.parquet")


def _encuesta(bloque: Bloque) -> pl.DataFrame:
    e = encuesta(bloque.fuente)
    if bloque.nombre == "empleo":
        e = e.filter(pl.col("relacion_actividad_3") == "ocupado")
    if bloque.nombre == "persona_ecv":
        e = e.filter(pl.col("peso_16").is_not_null())
    return _universo(e, bloque, sintetica=False)


def _props(df: pl.DataFrame, var: str, peso: str, por: list[str]) -> pl.DataFrame:
    return (
        df.group_by([*por, var])
        .agg(pl.col(peso).sum().alias("w"))
        .with_columns((pl.col("w") / pl.col("w").sum().over(por)).alias("p"))
    )


def bootstrap_ic(
    df: pl.DataFrame,
    var: str,
    peso: str,
    por: list[str],
    conglomerado: str | None,
    replicas: int,
    semilla: int,
) -> pl.DataFrame:
    """IC del 95 % de cada proporción (por × var) con bootstrap de Poisson por conglomerado."""
    d = df.select([*por, var, peso, *([conglomerado] if conglomerado else [])])
    d = d.with_columns(
        pl.concat_str([pl.col(c).cast(pl.Utf8) for c in por], separator="|").alias("_g"),
        pl.col(var).cast(pl.Utf8).alias("_v"),
    )
    gi = d["_g"].rank("dense").cast(pl.Int64).to_numpy() - 1
    ci = d.select(pl.concat_str("_g", "_v", separator="#")).to_series()
    cidx = ci.rank("dense").cast(pl.Int64).to_numpy() - 1
    ng, nc = gi.max() + 1, cidx.max() + 1
    k = d[conglomerado].rank("dense").cast(pl.Int64).to_numpy() - 1 if conglomerado else None
    n_cong = (k.max() + 1) if k is not None else d.height
    w = d[peso].to_numpy().astype(float)
    rng = make_rng(semilla)
    reps = np.empty((replicas, nc))
    for b in range(replicas):
        m = rng.poisson(1.0, n_cong)
        wb = w * (m[k] if k is not None else m)
        num = np.bincount(cidx, weights=wb, minlength=nc)
        den = np.bincount(gi, weights=wb, minlength=ng)
        g_de_c = np.zeros(nc, dtype=np.int64)
        g_de_c[cidx] = gi
        with np.errstate(invalid="ignore", divide="ignore"):
            reps[b] = num / den[g_de_c]
    lo, hi = np.nanpercentile(reps, [2.5, 97.5], axis=0)
    claves = (
        pl.DataFrame({"_c": ci, "_i": cidx}).unique("_i").sort("_i")["_c"].str.split_exact("#", 1)
    )
    out = pl.DataFrame(
        {
            "_g": claves.struct.field("field_0"),
            var: claves.struct.field("field_1"),
            "lo": lo,
            "hi": hi,
        }
    )
    partes = out["_g"].str.split_exact("|", len(por) - 1)
    return out.with_columns(
        [partes.struct.field(f"field_{i}").alias(c) for i, c in enumerate(por)]
    ).drop("_g")


def v_marg(personas: pl.DataFrame, replicas: int = 200, semilla: int = 0) -> pl.DataFrame:
    """Una fila por bloque × variable × comunidad × edad_4 × categoría."""
    filas = []
    for b in BLOQUES:
        e = _encuesta(b)
        s = _universo(personas, b, sintetica=True)
        for v in b.variables:
            ic = bootstrap_ic(e, v, b.peso, ["ccaa", "edad_4"], b.conglomerado, replicas, semilla)
            ps = _props(s, v, "peso", ["ccaa", "edad_4"]).with_columns(pl.col(v).cast(pl.Utf8))
            pe = _props(e, v, b.peso, ["ccaa", "edad_4"]).with_columns(pl.col(v).cast(pl.Utf8))
            j = (
                ic.join(
                    pe.select("ccaa", "edad_4", v, pl.col("p").alias("p_encuesta")),
                    on=["ccaa", "edad_4", v],
                    how="left",
                )
                .join(
                    ps.select("ccaa", "edad_4", v, pl.col("p").alias("p_sintetica")),
                    on=["ccaa", "edad_4", v],
                    how="left",
                )
                .filter(pl.col("ccaa").is_in(s["ccaa"].unique()))
                .with_columns(pl.col("p_sintetica").fill_null(0.0))
            )
            filas.append(
                j.with_columns(
                    pl.lit(b.nombre).alias("bloque"),
                    pl.lit(v).alias("variable"),
                    (
                        (pl.col("p_sintetica") >= pl.col("lo") - 1e-12)
                        & (pl.col("p_sintetica") <= pl.col("hi") + 1e-12)
                    ).alias("en_ic"),
                ).rename({v: "categoria"})
            )
    return pl.concat(filas, how="diagonal_relaxed")


def tvd_nacional(personas: pl.DataFrame) -> pl.DataFrame:
    filas = []
    for b in BLOQUES:
        e = _encuesta(b)
        s = _universo(personas, b, sintetica=True)
        # La encuesta, restringida a las comunidades de la población y reponderada a su peso
        cc = s["ccaa"].unique()
        e = e.filter(pl.col("ccaa").is_in(cc))
        for v in b.variables:
            pe = _props(e.with_columns(pl.lit(1).alias("_t")), v, b.peso, ["_t"])
            ps = _props(s.with_columns(pl.lit(1).alias("_t")), v, "peso", ["_t"])
            j = (
                pe.select(v, pl.col("p").alias("a"))
                .join(ps.select(v, pl.col("p").alias("b")), on=v, how="full", coalesce=True)
                .fill_null(0.0)
            )
            filas.append({"bloque": b.nombre, "variable": v, "tvd": M.tvd(j["b"], j["a"])})
    return pl.DataFrame(filas)


def _cramer(df: pl.DataFrame, a: str, b: str, peso: str) -> float:
    t = df.group_by(a, b).agg(pl.col(peso).sum())
    pv = t.pivot(on=b, index=a, values=peso).fill_null(0).sort(a)
    return M.cramer_v(pv.drop(a).select(sorted(pv.columns[1:])).to_numpy())


def v_asoc(personas: pl.DataFrame) -> pl.DataFrame:
    filas = []
    for b in BLOQUES:
        s = _universo(personas, b, sintetica=True)
        e = _encuesta(b).filter(pl.col("ccaa").is_in(s["ccaa"].unique()))
        llaves = [*b.llaves, "edad_4"]
        for v in b.variables:
            for k in llaves:
                if k == v or k not in s.columns or k not in e.columns:
                    continue
                ve = _cramer(e, v, k, b.peso)
                vs = _cramer(s, v, k, "peso")
                filas.append(
                    {
                        "bloque": b.nombre,
                        "variable": v,
                        "llave": k,
                        "v_encuesta": ve,
                        "v_sintetica": vs,
                        "dif": abs(vs - ve),
                    }
                )
    return pl.DataFrame(filas)


def v_bloque(personas: pl.DataFrame) -> pl.DataFrame:
    filas = []
    for b in BLOQUES:
        s = _universo(personas, b, sintetica=True)
        e = _encuesta(b).filter(pl.col("ccaa").is_in(s["ccaa"].unique()))
        for x, y in combinations(b.variables, 2):
            if {x, y} <= {"renta_hogar_decil", "renta_hogar_decil_ccaa"}:
                continue  # dos versiones del mismo decil
            ve = _cramer(e, x, y, b.peso)
            vs = _cramer(s, x, y, "peso")
            filas.append(
                {
                    "bloque": b.nombre,
                    "par": f"{x} × {y}",
                    "v_encuesta": ve,
                    "v_sintetica": vs,
                    "dif": abs(vs - ve),
                }
            )
    return pl.DataFrame(filas)


def v_marg_ajustada(personas: pl.DataFrame, replicas: int = 200, semilla: int = 0) -> pl.DataFrame:
    """Diagnóstico (no es puerta): V-ENRIQ-MARG con la población reponderada, dentro de cada
    comunidad × edad_4, a la composición de la encuesta por relación con la actividad y estudios.
    Separa lo que se debe al emparejamiento de lo que se debe a la composición censal."""
    filas = []
    for b in BLOQUES:
        e = _encuesta(b)
        s = _universo(personas, b, sintetica=True)
        llaves = (
            ["estudios_3", "sexo"] if b.nombre == "empleo" else ["relacion_actividad", "estudios_3"]
        )
        por = ["ccaa", "edad_4", *llaves]
        qe = (
            e.group_by(por)
            .agg(pl.col(b.peso).sum().alias("we"))
            .with_columns((pl.col("we") / pl.col("we").sum().over(["ccaa", "edad_4"])).alias("qe"))
        )
        qs = (
            s.group_by(por)
            .agg(pl.col("peso").sum().alias("ws"))
            .with_columns((pl.col("ws") / pl.col("ws").sum().over(["ccaa", "edad_4"])).alias("qs"))
        )
        f = qe.join(qs, on=por).select(*por, (pl.col("qe") / pl.col("qs")).alias("_f"))
        sa = s.join(f, on=por, how="left").with_columns(
            (pl.col("peso") * pl.col("_f").fill_null(0.0)).alias("peso")
        )
        for v in b.variables:
            ic = bootstrap_ic(e, v, b.peso, ["ccaa", "edad_4"], b.conglomerado, replicas, semilla)
            ps = _props(sa, v, "peso", ["ccaa", "edad_4"]).with_columns(pl.col(v).cast(pl.Utf8))
            j = ic.join(
                ps.select("ccaa", "edad_4", v, pl.col("p").alias("p_sintetica")),
                on=["ccaa", "edad_4", v],
                how="left",
            ).with_columns(pl.col("p_sintetica").fill_null(0.0))
            filas.append(
                {
                    "bloque": b.nombre,
                    "variable": v,
                    "proporcion": float(
                        (
                            (j["p_sintetica"] >= j["lo"] - 1e-12)
                            & (j["p_sintetica"] <= j["hi"] + 1e-12)
                        ).mean()
                    ),
                }
            )
    return pl.DataFrame(filas)
