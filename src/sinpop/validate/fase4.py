"""Validación de F4 (docs/04 F4, tareas 5 y 6; docs/05 §4 y §6).

Genera las poblaciones de prueba (5 tamaños × 5 semillas), valida cada una y guarda el resumen en
`reports/fase_04_validacion.json` (lo lee la puerta, `sinpop validate --phase 4`) y las tablas en
`reports/fase_04_validacion.md`. Comando: `python -m sinpop.validate.fase4`.
"""

from __future__ import annotations

import datetime as dt
import gc
import json
import shutil
import tempfile
from pathlib import Path

import polars as pl

from sinpop import REPORTS_DIR
from sinpop.repro import code_version
from sinpop.synth import donantes as D
from sinpop.synth import poblacion as PB
from sinpop.validate import metrics as M
from sinpop.validate import poblacion as V

TAMANOS = [10_000, 50_000, 100_000, 500_000, 1_000_000]
SEMILLAS = [1, 2, 3, 4, 5]
SOBREMUESTREO = "edad>=85:10000"  # unas 2,6 veces lo esperado en 100.000 personas
RESUMEN = REPORTS_DIR / "fase_04_validacion.json"
DETALLE = REPORTS_DIR / "fase_04"


def proporciones(p: pl.DataFrame, territorio: str) -> pl.DataFrame:
    """Proporción de cada categoría de las marginales calibradas del territorio."""
    from sinpop.targets import run

    obj = D.objetivos_calibrables(run.leer(territorio))
    r = D.recuentos(p, obj, "peso").join(
        obj.select("objetivo", "unidad", "universo").unique(), on="objetivo"
    )
    return r.with_columns(
        (pl.col("sintetico") / pl.col("sintetico").sum().over("objetivo")).alias("p"),
        (pl.col("valor") / pl.col("valor").sum().over("objetivo")).alias("p_obj"),
        pl.col("sintetico").sum().over("objetivo").alias("n_universo"),
    ).select("objetivo", "clave", "unidad", "p", "p_obj", "n_universo")


def _validar(rid: str, territorio: str, semilla: int, completa: bool) -> dict:
    p, lin, meta = V.cargar(rid)
    p = V.preparar(p)
    vm = V.v_marg(p, territorio, semilla)
    vc = V.v_cruce(p, territorio, semilla)
    duras = V.v_reglas_duras(p)
    blandas = V.v_reglas_blandas(p, meta["referencia_reglas_blandas"])
    DETALLE.mkdir(parents=True, exist_ok=True)
    vm.write_csv(DETALLE / f"{rid}_v_marg.csv")
    vc.write_csv(DETALLE / f"{rid}_v_cruce.csv")
    out = {
        "run_id": rid,
        "n": meta["tamano_solicitado"],
        "obtenido": meta["tamano_obtenido"],
        "semilla": semilla,
        "sha256": meta["sha256"],
        "v_marg": {
            "comprobaciones": vm.height,
            "fallos": vm.filter(~pl.col("ok"))
            .select("territorio", "objetivo", "tvd", "umbral")
            .to_dicts(),
            "tvd_media_espana": float(vm.filter(pl.col("nivel") == "espana")["tvd"].mean()),
            "tvd_max_espana": float(vm.filter(pl.col("nivel") == "espana")["tvd"].max()),
        },
        "v_cruce": {
            "comprobaciones": vc.height,
            "fallos": vc.filter(~pl.col("ok"))
            .select("nivel", "territorio", "objetivo", "tvd", "umbral")
            .to_dicts(),
            "espana": vc.filter(pl.col("nivel") == "espana")
            .select("objetivo", "tvd", "tvd_ref", "umbral", "ok")
            .to_dicts(),
            "tvd_media_espana": float(vc.filter(pl.col("nivel") == "espana")["tvd"].mean()),
            "fallos_propuesta": vc.filter(~pl.col("ok_propuesta"))
            .select("nivel", "territorio", "objetivo", "tvd", "umbral")
            .to_dicts(),
        },
        "v_reglas_duras": duras.to_dicts(),
        "v_reglas_blandas": blandas.to_dicts(),
        "proporciones": proporciones(p, territorio).to_dicts(),
    }
    if completa:
        out["v_cramer"] = V.v_cramer(p, territorio).to_dicts()
        out["minorias"] = V.v_minorias(p, lin, territorio).to_dicts()
        out["calidad_colectivos"] = float(
            (p["tipo_residencia"] == "establecimiento_colectivo").mean()
        )
    del p, lin
    gc.collect()
    return out


def v_semillas(pobs: list[dict], factor: float) -> list[dict]:
    """Por tamaño: sd entre semillas de cada proporción frente a 1,5 × sd de una muestra
    aleatoria simple del mismo tamaño (universo de la marginal)."""
    out = []
    for n in sorted({x["n"] for x in pobs}):
        filas = []
        for x in pobs:
            if x["n"] == n:
                filas += [r | {"semilla": x["semilla"]} for r in x["proporciones"]]
        df = pl.DataFrame(filas)
        g = df.group_by("objetivo", "clave").agg(
            pl.col("p").std().alias("sd"),
            pl.col("p_obj").first(),
            pl.col("n_universo").mean(),
            pl.len().alias("semillas"),
        )
        g = g.with_columns(
            (pl.col("p_obj") * (1 - pl.col("p_obj")) / pl.col("n_universo")).sqrt().alias("sd_mas")
        ).with_columns((pl.col("sd") <= factor * pl.col("sd_mas")).alias("ok"))
        malos = g.filter(~pl.col("ok") & (pl.col("p_obj") > 0))
        out.append(
            {
                "n": n,
                "proporciones": g.height,
                "fuera": malos.height,
                "razon_media": float(
                    g.filter(pl.col("sd_mas") > 0)
                    .select(pl.col("sd") / pl.col("sd_mas"))
                    .mean()
                    .item()
                ),
                "razon_max": float(
                    g.filter(pl.col("sd_mas") > 0)
                    .select(pl.col("sd") / pl.col("sd_mas"))
                    .max()
                    .item()
                ),
                "peores": malos.sort("sd", descending=True)
                .head(10)
                .select("objetivo", "clave", "sd", "sd_mas")
                .to_dicts(),
            }
        )
    return out


def v_repro(territorio: str, u: D.Unidades, referencia: dict) -> dict:
    """Misma configuración y semilla en otro directorio: mismos hashes (D-010)."""
    tmp = Path(tempfile.mkdtemp(prefix="sinpop_repro_"))
    try:
        m = PB.construir(territorio, referencia["n"], referencia["semilla"], u=u, destino=tmp)
        return {
            "run_id": referencia["run_id"],
            "hashes_iguales": m["sha256"] == referencia["sha256"],
            "sha256": m["sha256"],
        }
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def g47_sobremuestreo(territorio: str, u: D.Unidades, n: int = 100_000, semilla: int = 1) -> dict:
    """G4.7: las estimaciones ponderadas del modo de sobremuestreo reproducen las marginales
    calibradas dentro del error de muestreo de su tamaño efectivo (Kish de los pesos), igual que
    V-MARG, y el grupo alcanza el mínimo pedido."""
    from sinpop.targets import run

    c = V.umbrales()["V-MARG"]
    m = PB.construir(territorio, n, semilla, SOBREMUESTREO, u=u)
    p, _, _ = V.cargar(m["run_id"])
    p = V.preparar(p)
    sm = PB.S.parse_sobremuestreo(SOBREMUESTREO)
    miembros = int(p.filter(sm.condicion(p.schema)).height)  # type: ignore[union-attr]
    obj = D.objetivos_calibrables(run.leer(territorio))
    r = D.recuentos(p, obj, "peso")
    filas = []
    for (o,), g in r.group_by("objetivo", maintain_order=True):
        info = obj.filter(pl.col("objetivo") == o).row(0, named=True)
        sub = D.en_universo(p, info["universo"], info["unidad"], ["peso"])
        n_eff = M.kish(sub["peso"].to_numpy())
        ref = M.tvd_ref(
            g["valor"].to_numpy(),
            max(1, round(n_eff)),
            c["muestras_ref"],
            c["percentil_ref"],
            semilla,
        )
        tvd = M.tvd(g["sintetico"], g["valor"])
        umbral = c["factor_tvd_ref"] * ref + c["tolerancia"]
        filas.append(
            {"objetivo": o, "tvd": tvd, "n_efectivo": n_eff, "umbral": umbral, "ok": tvd <= umbral}
        )
    return {
        "run_id": m["run_id"],
        "spec": SOBREMUESTREO,
        "miembros": miembros,
        "minimo": sm.minimo,  # type: ignore[union-attr]
        "alfa_beta": {k: m["sobremuestreo"][k] for k in ("alfa", "beta")},
        "suma_pesos": float(p["peso"].sum()),
        "marginales": filas,
        "ok": all(f["ok"] for f in filas) and miembros >= 0.9 * sm.minimo,  # type: ignore[union-attr]
    }


def ejecutar(territorio: str = "ES", tamanos=TAMANOS, semillas=SEMILLAS) -> dict:
    u = PB.unidades_todas()
    pobs = []
    for n in tamanos:
        for s in semillas:
            meta = PB.construir(territorio, n, s, u=u)
            completa = n == max(tamanos) and s == semillas[0]
            pobs.append(_validar(meta["run_id"], territorio, s, completa))
            print(
                f"{meta['run_id']}: V-MARG {len(pobs[-1]['v_marg']['fallos'])} fallos, "
                f"V-CRUCE {len(pobs[-1]['v_cruce']['fallos'])} fallos",
                flush=True,
            )
    cal = json.loads((PB.CALIBRACION_DIR / f"{territorio}_{PB.METODO}.json").read_text("utf-8"))
    thr = V.umbrales()
    res = {
        "territorio": territorio,
        "fecha": dt.date.today().isoformat(),
        "version_codigo": code_version(),
        "comando": "python -m sinpop.validate.fase4",
        "calibracion": {
            "metodo": cal["metodo"],
            "sha256": cal["sha256"],
            "v_pesos": V.v_pesos(cal["diagnosticos"]).to_dicts(),
            "ampliaciones": cal["ampliaciones"],
            "fusiones": cal["fusiones"],
            "ceros": cal["ceros"],
        },
        "poblaciones": [{k: v for k, v in x.items() if k != "proporciones"} for x in pobs],
        "v_semillas": v_semillas(pobs, thr["V-SEMILLAS"]["factor_sd"]),
        "v_repro": v_repro(territorio, u, pobs[0]),
        "g47": g47_sobremuestreo(territorio, u),
    }
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")
    return res


def curva(res: dict) -> pl.DataFrame:
    df = pl.DataFrame(
        [
            {
                "n": x["n"],
                "semilla": x["semilla"],
                "marg": x["v_marg"]["tvd_media_espana"],
                "cruce": x["v_cruce"]["tvd_media_espana"],
            }
            for x in res["poblaciones"]
        ]
    )
    return (
        df.group_by("n")
        .agg(
            pl.col("marg").mean().alias("tvd_media_calibradas"),
            pl.col("marg").std().alias("sd_calibradas"),
            pl.col("cruce").mean().alias("tvd_media_reservadas"),
            pl.col("cruce").std().alias("sd_reservadas"),
        )
        .sort("n")
    )


if __name__ == "__main__":
    r = ejecutar()
    print(curva(r))
    print(json.dumps(r["v_semillas"], indent=1)[:2000])
    print(r["v_repro"]["hashes_iguales"], r["g47"]["ok"])
