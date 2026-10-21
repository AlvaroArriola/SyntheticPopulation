"""Validación de F8A: capa de opinión y valores (docs/04 F8A, docs/05 §7).

- G8A.4: distribución de cada variable de valores por comunidad × edad_4 frente al CIS, como
  V-ENRIQ-MARG (≥ 90 % de las celdas en el IC 95 % bootstrap del CIS y TVD nacional ≤ 0,02).
  La comparación se hace en el universo del CIS: personas de nacionalidad española de 18 años
  y más en viviendas familiares.

Comando: `python -m sinpop.validate.fase8a`
"""

from __future__ import annotations

import datetime as dt
import json

import polars as pl

from sinpop import POPULATIONS_DIR, REPORTS_DIR
from sinpop.opinion import cv as CV
from sinpop.opinion import identidad as ID
from sinpop.opinion import latentes as L
from sinpop.opinion import lengua as LG
from sinpop.opinion import medios as MD
from sinpop.opinion import rasgos as R
from sinpop.opinion import run as OR
from sinpop.opinion import valores as V
from sinpop.opinion.cis import VALORES
from sinpop.repro import code_version
from sinpop.validate import metrics as M
from sinpop.validate import sanitario as SAN
from sinpop.validate.enriquecimiento import _props, bootstrap_ic

NACIONAL = "2026-01-01_ES_1000000_s1"
RESUMEN = REPORTS_DIR / "fase_08a_validacion.json"
DETALLE = REPORTS_DIR / "fase_08a"


def _edad_4(edad: pl.Expr) -> pl.Expr:
    return (
        pl.when(edad < 35)
        .then(pl.lit("18-34"))
        .when(edad < 50)
        .then(pl.lit("35-49"))
        .when(edad < 65)
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
        .alias("edad_4")
    )


def referencias() -> dict[str, tuple]:
    """Variable observada → (datos de referencia, universo de la comparación). Las del CIS se
    comparan en su universo (españoles en vivienda familiar); la lengua, con la ECEPOV, en todos
    los adultos en vivienda familiar (D-066)."""
    out = {v: ((lambda v=v: V.datos(v)), "espanoles") for v in VALORES}
    out["lengua_habitual"] = (LG.datos, "todos")
    out["medio_informacion_principal"] = (MD.datos, "espanoles")
    out["identidad_territorial"] = (ID.datos, "espanoles")
    return out


REPONDERAR = {
    "lengua_habitual": ["ccaa", "edad_4", "pais_nacimiento_grupo"],
    # la identidad junta postelectorales autonómicos (miles de entrevistas en su comunidad) con
    # el estudio nacional 3409: sin reponderar, la cifra «nacional» del CIS sobrerrepresenta
    # Andalucía, Cataluña, Galicia, País Vasco, Aragón y Castilla y León (D-066)
    "identidad_territorial": ["ccaa", "edad_4"],
}


def _reponderar(e: pl.DataFrame, s: pl.DataFrame, celdas: list[str]) -> pl.DataFrame:
    """Lleva la referencia a la composición de la población sintética en `celdas`. La ECEPOV es
    de 2021 y desde entonces creció la población nacida fuera de España (16 % → 21 % de los
    adultos): sin esto, el cambio demográfico real se leería como error del modelo (D-066)."""
    pe = e.group_by(celdas).agg(pl.col("peso").sum().alias("we"))
    ps = s.group_by(celdas).agg(pl.col("peso").sum().alias("ws"))
    f = pe.join(ps, on=celdas, how="inner").with_columns(
        (pl.col("ws") / pl.col("ws").sum() / (pl.col("we") / pl.col("we").sum())).alias("f")
    )
    return e.join(f.select(*celdas, "f"), on=celdas, how="inner").with_columns(
        pl.col("peso") * pl.col("f")
    )


def sintetica(run_id: str, universo: str = "espanoles") -> pl.DataFrame:
    d = POPULATIONS_DIR / run_id
    p = pl.read_parquet(
        d / "persons.parquet",
        columns=[
            "person_id",
            "edad",
            "ccaa",
            "peso",
            "nacionalidad_esp_ext",
            "tipo_residencia",
            "pais_nacimiento_grupo",
        ],
    )
    o = pl.read_parquet(d / "opinion.parquet")
    filtro = pl.col("tipo_residencia") == "vivienda_familiar"
    if universo == "espanoles":
        filtro = filtro & (pl.col("nacionalidad_esp_ext") == "espanola")
    return p.join(o, on="person_id").filter(filtro).with_columns(_edad_4(pl.col("edad")))


def v_marg_valores(run_id: str, replicas: int = 200, semilla: int = 0) -> pl.DataFrame:
    filas = []
    sint = {u: sintetica(run_id, u) for u in ("espanoles", "todos")}
    for v, (fuente, universo) in referencias().items():
        s = sint[universo]
        e = fuente().with_columns(_edad_4(pl.col("edad")))
        if v in REPONDERAR:
            e = _reponderar(e, s, REPONDERAR[v])
        ic = bootstrap_ic(e, v, "peso", ["ccaa", "edad_4"], None, replicas, semilla)
        ps = _props(s, v, "peso", ["ccaa", "edad_4"])
        pe = _props(e, v, "peso", ["ccaa", "edad_4"])
        j = (
            ic.join(
                pe.select("ccaa", "edad_4", v, pl.col("p").alias("p_cis")),
                on=["ccaa", "edad_4", v],
                how="left",
            )
            .join(
                ps.select("ccaa", "edad_4", v, pl.col("p").alias("p_sintetica")),
                on=["ccaa", "edad_4", v],
                how="left",
            )
            .filter(pl.col("ccaa").is_in(s["ccaa"].unique().to_list()))
            .with_columns(pl.col("p_sintetica").fill_null(0.0))
        )
        filas.append(
            j.with_columns(
                pl.lit(v).alias("variable"),
                (
                    (pl.col("p_sintetica") >= pl.col("lo") - 1e-12)
                    & (pl.col("p_sintetica") <= pl.col("hi") + 1e-12)
                ).alias("en_ic"),
            ).rename({v: "categoria"})
        )
    return pl.concat(filas, how="diagonal_relaxed")


def tvd_nacional(run_id: str) -> list[dict]:
    out = []
    sint = {u: sintetica(run_id, u) for u in ("espanoles", "todos")}
    for v, (fuente, universo) in referencias().items():
        s, e = sint[universo], fuente().with_columns(_edad_4(pl.col("edad")))
        # solo donde hay referencia (la identidad solo se pregunta en algunas comunidades)
        s = s.filter(pl.col(v).is_not_null() & pl.col("ccaa").is_in(e["ccaa"].unique().to_list()))
        if v in REPONDERAR:
            e = _reponderar(e, s, REPONDERAR[v])
        a = _props(s.with_columns(pl.lit(1).alias("_t")), v, "peso", ["_t"]).select(
            v, pl.col("p").alias("p_s")
        )
        b = _props(e.with_columns(pl.lit(1).alias("_t")), v, "peso", ["_t"]).select(
            v, pl.col("p").alias("p_c")
        )
        j = a.join(b, on=v, how="full", coalesce=True).fill_null(0.0)
        out.append({"variable": v, "tvd": M.tvd(j["p_s"], j["p_c"])})
    return out


MIN_GRUPO = 200  # encuestados del CIS por grupo para comparar varianzas


def v_diversidad_rasgos(run_id: str, s: pl.DataFrame) -> pl.DataFrame:
    """G8A.3: varianza de cada rasgo dentro de los grupos edad × estudios × sexo, sintética
    frente a la del CIS (ponderada), en los grupos con al menos `MIN_GRUPO` encuestados."""
    d = POPULATIONS_DIR / run_id
    extra = pl.read_parquet(d / "persons.parquet", columns=["person_id", "sexo", "estudios_3"])
    s = s.join(extra, on="person_id").with_columns(V._edad_grupo(pl.col("edad")))
    grupo = ["edad_grupo", "estudios_3", "sexo"]
    filas = []
    for r in ["estilo_ns_nc", *L.rasgos()]:
        e = R.datos_rasgo(r)

        def var_pond(df: pl.DataFrame, peso: str, r: str = r) -> pl.DataFrame:
            w, x = pl.col(peso), pl.col(r)
            media = (w * x).sum() / w.sum()
            return df.group_by(grupo).agg(
                pl.len().alias("n"), ((w * (x - media) ** 2).sum() / w.sum()).alias("var")
            )

        j = (
            var_pond(e, "peso")
            .filter(pl.col("n") >= MIN_GRUPO)
            .join(var_pond(s, "peso"), on=grupo, suffix="_sintetica")
        )
        filas.append(
            j.with_columns(
                pl.lit(r).alias("rasgo"), (pl.col("var_sintetica") / pl.col("var")).alias("ratio")
            )
        )
    return pl.concat(filas)


def v_latente() -> dict:
    """G8A.1: ajuste de cada rasgo. Un factor con tres ítems tiene 0 grados de libertad y su
    CFI y RMSEA no contrastan nada: para esos rasgos se usan los del factorial conjunto de
    todos los rasgos de su estudio (`latentes.ajuste_conjunto`)."""
    conjuntos = {}
    filas = []
    for r in L.rasgos():
        _, i = L.ajuste(r)
        i["ajuste_de"] = "propio"
        if i["gl"] == 0:
            e = i["estudios"][0]
            if e not in conjuntos:
                conjuntos[e] = L.ajuste_conjunto(e)
            c = conjuntos[e]
            if c is not None:
                i |= {"cfi": c["cfi"], "rmsea": c["rmsea"], "ajuste_de": f"conjunto {e}"}
        filas.append(i)
    for e in {x["estudios"][0] for x in filas}:
        if e not in conjuntos:
            conjuntos[e] = L.ajuste_conjunto(e)
    return {"rasgos": filas, "conjuntos": [c for c in conjuntos.values() if c]}


def ejecutar(run_id: str = NACIONAL) -> dict:
    DETALLE.mkdir(parents=True, exist_ok=True)
    if not (POPULATIONS_DIR / run_id / "opinion.parquet").exists():
        OR.construir(run_id)
    s = sintetica(run_id)
    m = v_marg_valores(run_id)
    m.write_csv(DETALLE / f"{run_id}_v_marg_valores.csv")
    por_var = (
        m.group_by("variable")
        .agg(pl.col("en_ic").mean().alias("proporcion"), pl.len().alias("celdas"))
        .sort("variable")
    )
    res = {
        "fecha": dt.date.today().isoformat(),
        "version_codigo": code_version(),
        "run_id": run_id,
        "g8a4": {
            "umbral_celdas": 0.90,
            "umbral_tvd": 0.02,
            "por_variable": por_var.to_dicts(),
            "global": float(m["en_ic"].mean()),
            "tvd_nacional": tvd_nacional(run_id),
        },
    }
    dv = v_diversidad_rasgos(run_id, s)
    dv.write_csv(DETALLE / f"{run_id}_v_diversidad_rasgos.csv")
    res["g8a3"] = {
        "umbral": [0.8, 1.2],
        "grupos": dv.height,
        "dentro": int(dv.filter(pl.col("ratio").is_between(0.8, 1.2)).height),
        "ratio_min": float(dv["ratio"].min()) if dv.height else None,
        "ratio_max": float(dv["ratio"].max()) if dv.height else None,
    }
    res["g8a1"] = v_latente()
    cv = CV.v_opinion_cv()
    pl.DataFrame(cv.pop("detalle")).with_columns(
        pl.col("estudios_entreno").list.join(",")
    ).write_csv(DETALLE / "v_opinion_cv.csv")
    res["g8a2"] = cv
    meta = json.loads((POPULATIONS_DIR / run_id / "metadata.json").read_text("utf-8"))
    persons = pl.read_parquet(POPULATIONS_DIR / run_id / "persons.parquet")
    t, g5 = SAN.g8a5(persons, OR.semilla_capa(int(meta["semilla"]), "g8a5"))
    if not t.is_empty():
        t.write_csv(DETALLE / f"{run_id}_g8a5_sanitario.csv")
        g5["resumen"] = (
            f"oleada {g5['oleada_contraste']} (ajuste con los 12 meses previos); "
            f"{len(g5['preguntas'])} preguntas, {g5['celdas']} celdas pregunta × CCAA; TVD media "
            f"simulada {g5['tvd_media_simulada']:.3f}, B0 nacional {g5['tvd_media_b0']:.3f}, "
            f"B1 directa {g5['tvd_media_b1']:.3f}, ruido muestral {g5['ruido_muestral_medio']:.3f}"
        )
    else:
        g5["resumen"] = g5.get("motivo", "")
    res["g8a5"] = g5
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    return res


if __name__ == "__main__":
    r = ejecutar()
    print(json.dumps(r["g8a4"], ensure_ascii=False, indent=1))
