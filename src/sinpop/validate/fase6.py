"""Validación de F6: enriquecimiento (docs/04 F6, docs/05 §5; D-044, D-045).

Sobre la población nacional de 1.000.000 de personas (semilla 1), enriquecida:

- V-ENRIQ-MARG, TVD nacional, V-ENRIQ-ASOC y V-ENRIQ-BLOQUE (G6.1-G6.3);
- V-ENRIQ-HOLDOUT: se repite el enriquecimiento sin los estudios como llave y se comprueba que
  se recupera su asociación con cada variable enriquecida (G6.4);
- G6.5: con y sin enriquecimiento, las columnas de los donantes censales son idénticas;
- G6.6: renta media por provincia frente al objetivo del Atlas (calibrada) y por municipio
  identificado (no calibrada, se informa).

Comando: `python -m sinpop.validate.fase6`. Resumen en `reports/fase_06_validacion.json` y
detalle en `reports/fase_06/`.
"""

from __future__ import annotations

import datetime as dt
import gc
import json
import tempfile
from pathlib import Path

import numpy as np
import polars as pl

from sinpop import POPULATIONS_DIR, REPORTS_DIR
from sinpop.enrich import run as ER
from sinpop.repro import code_version
from sinpop.synth import poblacion as PB
from sinpop.validate import enriquecimiento as VE
from sinpop.validate import poblacion as V

SEMILLA = 1
N = 1_000_000
N_PRUEBA = 10_000
RESUMEN = REPORTS_DIR / "fase_06_validacion.json"
DETALLE = REPORTS_DIR / "fase_06"


def _columnas_enriquecidas(df: pl.DataFrame, base: pl.DataFrame) -> list[str]:
    return [c for c in df.columns if c not in base.columns]


def g65_igualdad(u) -> dict:
    """Las columnas de la población sin enriquecer son idénticas en la enriquecida."""
    with tempfile.TemporaryDirectory() as t:
        a = PB.construir("ES", N_PRUEBA, SEMILLA, u=u, destino=Path(t) / "a", enriquecer=False)
        b = PB.construir("ES", N_PRUEBA, SEMILLA, u=u, destino=Path(t) / "b")
        out = {"run_id": a["run_id"], "ficheros": {}}
        for f in ("persons", "households", "lineage"):
            x = pl.read_parquet(Path(t) / "a" / a["run_id"] / f"{f}.parquet")
            y = pl.read_parquet(Path(t) / "b" / b["run_id"] / f"{f}.parquet")
            igual = y.select(x.columns).equals(x)
            out["ficheros"][f] = {
                "columnas_base": len(x.columns),
                "columnas_nuevas": _columnas_enriquecidas(y, x),
                "identicas": bool(igual),
            }
    out["ok"] = all(v["identicas"] for v in out["ficheros"].values())
    return out


LLAVES_RESERVADAS = ("sexo", "nacionalidad_esp_ext", "relacion_actividad", "estudios_3")


def holdout(personas: pl.DataFrame, hogares: pl.DataFrame, base_cols: list[str]) -> pl.DataFrame:
    """V-ENRIQ-HOLDOUT: enriquecimiento sin cada llave reservada (por turno) y asociación de
    cada variable enriquecida con ella, frente a la encuesta y frente a la independencia."""
    p0 = personas.select(base_cols)
    h0 = hogares.select([c for c in hogares.columns if not _es_enriquecida_hogar(c)])
    filas = []
    for llave in LLAVES_RESERVADAS:
        pe, _, _ = ER.enriquecer(p0, h0, "ES", SEMILLA, quitar=(llave,))
        for b in VE.BLOQUES:
            s = VE._universo(pe, b, sintetica=True)
            e = VE._encuesta(b)
            if llave not in s.columns or llave not in e.columns:
                continue
            for v in b.variables:
                ve = VE._cramer(e, v, llave, b.peso)
                vs = VE._cramer(s, v, llave, "peso")
                filas.append(
                    {
                        "llave": llave,
                        "bloque": b.nombre,
                        "variable": v,
                        "v_encuesta": ve,
                        "v_sintetica": vs,
                        "dif": abs(vs - ve),
                        "dif_independencia": ve,
                        "recuperada": vs / ve if ve > 0 else None,
                    }
                )
        del pe
        gc.collect()
    return pl.DataFrame(filas)


def _es_enriquecida_hogar(c: str) -> bool:
    from sinpop.enrich import fuentes as F

    return c.split("__")[0] in F.BLOQUE_HOGAR


def g66_renta(meta: dict, hogares: pl.DataFrame) -> dict:
    """Renta media (personas) por unidad de inclinación frente a su objetivo; y por municipio
    identificado frente a la renta relativa del Atlas (no calibrada)."""
    from sinpop.enrich import contexto as CTX

    h = hogares.filter(pl.col("renta_equivalente").is_not_null())
    w = pl.col("n_personas_hogar").cast(pl.Float64)
    m = h.group_by("provincia").agg(
        ((pl.col("renta_equivalente") * w).sum() / w.sum()).alias("media"),
        # error típico de la media ponderada por personas (hogares como conglomerados)
        (
            (w * (pl.col("renta_equivalente") - (pl.col("renta_equivalente") * w).sum() / w.sum()))
            .pow(2)
            .sum()
            .sqrt()
            / w.sum()
        ).alias("et"),
        pl.len().alias("hogares"),
    )
    inc = pl.DataFrame(meta["enriquecimiento"]["bloques"]["hogar"]["inclinacion"]).rename(
        {"unidad": "provincia"}
    )
    j = inc.join(m, on="provincia").with_columns(
        (pl.col("media") / pl.col("objetivo") - 1).alias("error_relativo"),
        pl.max_horizontal(pl.lit(0.02), 2 * pl.col("et") / pl.col("objetivo")).alias("tolerancia"),
    )
    j = j.with_columns((pl.col("error_relativo").abs() <= pl.col("tolerancia")).alias("ok"))
    # Municipios identificados: renta media sintética relativa a su provincia frente al Atlas
    am = CTX.atlas_municipios().select("municipio", "renta_uc_media")
    ap = (
        CTX.atlas_territorios()
        .filter(pl.col("nivel") == "provincia")
        .select(pl.col("codigo").alias("provincia"), pl.col("renta_uc_media").alias("a_prov"))
    )
    mm = (
        h.filter(pl.col("municipio").is_not_null())
        .group_by("municipio", "provincia")
        .agg(
            ((pl.col("renta_equivalente") * w).sum() / w.sum()).alias("media"), pl.len().alias("n")
        )
        .filter(pl.col("n") >= 200)
        .join(m.select("provincia", pl.col("media").alias("m_prov")), on="provincia")
        .join(am, on="municipio")
        .join(ap, on="provincia")
        .with_columns(
            (pl.col("media") / pl.col("m_prov")).alias("rel_sintetica"),
            (pl.col("renta_uc_media") / pl.col("a_prov")).alias("rel_atlas"),
        )
    )
    corr = float(np.corrcoef(mm["rel_sintetica"], mm["rel_atlas"])[0, 1]) if mm.height > 2 else None
    return {
        "provincias": j.sort("provincia").to_dicts(),
        "fuera": j.filter(~pl.col("ok"))["provincia"].to_list(),
        "error_max": float(j["error_relativo"].abs().max()),
        "municipios": {
            "n": mm.height,
            "correlacion_relativa": corr,
            "error_relativo_medio": float(
                ((pl.Series(mm["rel_sintetica"]) / mm["rel_atlas"]) - 1).abs().mean()
            )
            if mm.height
            else None,
        },
    }


def triangulacion_salud(personas: pl.DataFrame) -> list[dict]:
    """Salud autopercibida y limitación (GALI) frente a la ESdE 2023, por edad_4 (informativo)."""
    e = VE.encuesta("encuesta_salud").filter(pl.col("edad_4").is_in(VE.EDADES))
    s = personas.filter(
        (pl.col("tipo_residencia") == "vivienda_familiar") & pl.col("edad_4").is_in(VE.EDADES)
    )
    out = []
    for v in ("salud_autopercibida", "discapacidad_limitacion"):
        a = VE._props(e.filter(~pl.col(v).is_in(["NC", "NS"])), v, "peso", ["edad_4"])
        b = VE._props(s.filter(~pl.col(v).is_in(["NC", "NS"])), v, "peso", ["edad_4"])
        j = (
            a.select("edad_4", v, pl.col("p").alias("esde"))
            .join(
                b.select("edad_4", v, pl.col("p").alias("sintetica")),
                on=["edad_4", v],
                how="full",
                coalesce=True,
            )
            .fill_null(0.0)
        )
        for (g,), x in j.group_by("edad_4", maintain_order=True):
            out.append(
                {
                    "variable": v,
                    "edad_4": g,
                    "tvd": float(0.5 * (x["esde"] - x["sintetica"]).abs().sum()),
                }
            )
    return out


def ejecutar() -> dict:
    DETALLE.mkdir(parents=True, exist_ok=True)
    u = PB.unidades_todas()
    g65 = g65_igualdad(u)
    print(f"G6.5: {g65['ok']}", flush=True)
    del u
    gc.collect()
    meta = PB.construir("ES", N, SEMILLA)
    rid = meta["run_id"]
    p, _, _ = V.cargar(rid)
    h = pl.read_parquet(POPULATIONS_DIR / rid / "households.parquet")
    thr = V.umbrales()
    mg = VE.v_marg(p, 200, SEMILLA)
    mg.write_csv(DETALLE / "v_enriq_marg.csv")
    por_var = (
        mg.group_by("bloque", "variable")
        .agg(pl.col("en_ic").mean().alias("proporcion"), pl.len().alias("celdas"))
        .sort("bloque", "variable")
    )
    tv = VE.tvd_nacional(p)
    asoc = VE.v_asoc(p)
    asoc.write_csv(DETALLE / "v_enriq_asoc.csv")
    blo = VE.v_bloque(p)
    blo.write_csv(DETALLE / "v_enriq_bloque.csv")
    print("V-ENRIQ hechas", flush=True)
    base_cols = [c for c in p.columns if c not in set(VE_columnas(p))]
    ho = holdout(p, h, base_cols)
    ho.write_csv(DETALLE / "v_enriq_holdout.csv")
    g66 = g66_renta(meta, h)
    diag = diagnostico_composicion(p)
    calidad = {
        c.removesuffix("__calidad"): dict(p[c].value_counts().iter_rows())
        for c in p.columns
        if c.endswith("__calidad") and c.removesuffix("__calidad") in VE_columnas(p)
    }
    res = {
        "fecha": dt.date.today().isoformat(),
        "version_codigo": code_version(),
        "comando": "python -m sinpop.validate.fase6",
        "semilla": SEMILLA,
        "run_id": rid,
        "estrategia": meta["enriquecimiento"]["estrategia"],
        "niveles": {b: x.get("niveles") for b, x in meta["enriquecimiento"]["bloques"].items()},
        "v_enriq_marg": {
            "umbral": thr["V-ENRIQ-MARG"]["proporcion_celdas_ic95"],
            "por_variable": por_var.to_dicts(),
            "global": float(mg["en_ic"].mean()),
        },
        "tvd_nacional": {
            "umbral": thr["V-ENRIQ-MARG"]["tvd_nacional"],
            "por_variable": tv.to_dicts(),
        },
        "v_enriq_asoc": {
            "umbral": thr["V-ENRIQ-ASOC"]["max_abs_dif"],
            "comprobaciones": asoc.height,
            "fuera": asoc.filter(pl.col("dif") > thr["V-ENRIQ-ASOC"]["max_abs_dif"]).to_dicts(),
            "dif_max": float(asoc["dif"].max()),
        },
        "v_enriq_bloque": {
            "umbral_max": thr["V-ENRIQ-BLOQUE"]["max_abs_dif"],
            "umbral_media": thr["V-ENRIQ-BLOQUE"]["media_abs_dif"],
            "dif_max": float(blo["dif"].max()),
            "dif_media": float(blo["dif"].mean()),
            "pares": blo.to_dicts(),
        },
        "v_enriq_holdout": {
            "llaves": list(LLAVES_RESERVADAS),
            "umbral": thr["V-ENRIQ-HOLDOUT"]["max_abs_dif"],
            "filas": ho.to_dicts(),
        },
        "marg_ajustada": diag["marg_ajustada"],
        "tvd_ajustada": diag["tvd_ajustada"],
        "g65": g65,
        "g66": g66,
        "triangulacion_esde": triangulacion_salud(p),
        "calidad": calidad,
        "contexto": {
            c: {
                "media": float(p[c].mean()),
                "nulos": int(p[c].null_count()),
                "calidad": dict(p[f"{c}__calidad"].value_counts().iter_rows()),
            }
            for c in ("ctx_renta_municipio", "ctx_envejecimiento")
        },
    }
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")
    return res


def diagnostico_composicion(p: pl.DataFrame) -> dict:
    """D-048: V-ENRIQ-MARG y TVD nacional con la población reponderada, dentro de cada
    comunidad × edad_4, a la composición de cada encuesta (actividad y estudios)."""
    aj = VE.v_marg_ajustada(p, 200, SEMILLA)
    return {"marg_ajustada": aj.to_dicts(), "tvd_ajustada": VE.tvd_ajustada(p).to_dicts()}


def VE_columnas(p: pl.DataFrame) -> list[str]:
    """Columnas añadidas por el enriquecimiento (variables y su calidad)."""
    from sinpop.enrich import fuentes as F

    vs = [
        *F.BLOQUE_HOGAR,
        *F.BLOQUE_PERSONA_ECV,
        *F.BLOQUE_EMPLEO,
        *F.BLOQUE_DIGITAL,
        "ctx_renta_municipio",
        "ctx_envejecimiento",
    ]
    return [c for c in p.columns if c.split("__")[0] in vs]


if __name__ == "__main__":
    import sys

    if "--diagnostico" in sys.argv:  # recalcula solo el diagnóstico de composición
        r = json.loads(RESUMEN.read_text("utf-8"))
        r |= diagnostico_composicion(V.cargar(r["run_id"])[0])
        RESUMEN.write_text(json.dumps(r, ensure_ascii=False, indent=1, default=float), "utf-8")
        raise SystemExit
    r = ejecutar()
    print(
        json.dumps({k: r[k] for k in ("v_enriq_marg", "v_enriq_asoc", "g65")}, default=float)[:3000]
    )
