"""Validación de F5: generador territorial (docs/04 F5, tareas 4 a 6).

Genera y valida las 19 comunidades, 10 provincias de perfiles distintos y 2 agrupaciones por
lista de municipios; la coherencia entre niveles (V-COHERENCIA) y la prueba del territorio
reservado. Resumen en `reports/fase_05_validacion.json` (lo lee la puerta) y detalle en
`reports/fase_05/`. Comando: `python -m sinpop.validate.fase5`.
"""

from __future__ import annotations

import datetime as dt
import gc
import json

import polars as pl

from sinpop import REPORTS_DIR
from sinpop.repro import code_version
from sinpop.synth import donantes as D
from sinpop.synth import poblacion as PB
from sinpop.validate import metrics as M
from sinpop.validate import poblacion as V

SEMILLA = 1
N_CCAA = 100_000
N_PROV = 50_000
N_MUNIS = 20_000
N_ES = 1_000_000
PROVINCIAS = ["28", "08", "42", "44", "04", "35", "20", "32", "51", "52"]
MUNIS = [
    "MUNIS:configs/territorios/ejemplo_valencia_urbano.yaml",
    "MUNIS:configs/territorios/ejemplo_teruel_rural.yaml",
]
# Prueba del territorio reservado: Galicia sin sus objetivos socioeconómicos.
RESERVADO = "CCAA:12"
SOCIOECONOMICOS = ("actividad_sexo", "estudios_edad")
RESUMEN = REPORTS_DIR / "fase_05_validacion.json"
DETALLE = REPORTS_DIR / "fase_05"


def territorios() -> list[tuple[str, int]]:
    from sinpop.harmonize.core import ccaa_de_provincia

    ccaa = sorted(set(ccaa_de_provincia().values()))
    return (
        [(f"CCAA:{c}", N_CCAA) for c in ccaa]
        + [(f"PROV:{p}", N_PROV) for p in PROVINCIAS]
        + [(m, N_MUNIS) for m in MUNIS]
    )


def _validar(meta: dict) -> dict:
    rid, t = meta["run_id"], meta["territorio"]["codigo"]
    p, _, _ = V.cargar(rid)
    pp = V.preparar(p)
    vm = V.v_marg(pp, t, SEMILLA)
    vc = V.v_cruce(pp, t, SEMILLA)
    duras = V.v_reglas_duras(pp)
    DETALLE.mkdir(parents=True, exist_ok=True)
    vm.write_csv(DETALLE / f"{rid}_v_marg.csv")
    vc.write_csv(DETALLE / f"{rid}_v_cruce.csv")
    fc = vc.filter(~pl.col("ok") & ~pl.col("excepcion"))
    out = {
        "territorio": t,
        "run_id": rid,
        "n": meta["tamano_solicitado"],
        "obtenido": meta["tamano_obtenido"],
        "donantes": meta["donantes"],
        "v_marg": {
            "comprobaciones": vm.height,
            "fallos": vm.filter(~pl.col("ok"))
            .select("territorio", "objetivo", "tvd", "umbral")
            .to_dicts(),
            "tvd_media": float(vm["tvd"].mean()),
        },
        "v_cruce": {
            "comprobaciones": vc.height,
            "fallos": fc.select("nivel", "territorio", "objetivo", "tvd", "umbral").to_dicts(),
            "excepciones": int((~vc["ok"] & vc["excepcion"]).sum()),
            "proporcion_fallos": fc.height / vc.height if vc.height else 0.0,
            "propio": vc.filter(pl.col("territorio") == t)
            .select("objetivo", "tvd", "tvd_ref", "umbral", "ok")
            .to_dicts(),
        },
        "v_reglas_duras": int(duras["violaciones"].sum()),
    }
    if t.startswith("CCAA:"):
        out["v_cramer"] = V.v_cramer(pp, t).to_dicts()
    del p, pp
    gc.collect()
    return out


def coherencia(ccaa: list[dict], nacional: str) -> dict:
    """V-COHERENCIA: las 19 poblaciones autonómicas, cada persona con peso = población oficial de
    su comunidad / tamaño obtenido, frente a la población nacional: TVD de las marginales
    calibradas ≤ 0,01 y de los cruces reservados ≤ 0,02 (nivel España)."""
    from sinpop.targets import run

    c = V.umbrales()["V-COHERENCIA"]
    partes = []
    for x in ccaa:
        p, _, _ = V.cargar(x["run_id"])
        pob = run.leer(x["territorio"]).filter(pl.col("objetivo") == "edad5_sexo")["valor"].sum()
        partes.append(p.with_columns(pl.lit(pob / p.height).alias("peso")))
    comb = V.preparar(pl.concat(partes, how="vertical_relaxed"))
    nac, _, _ = V.cargar(nacional)
    nac = V.preparar(nac)
    obj = run.leer("ES").filter(pl.col("universo").is_in(list(V.UNIVERSOS)))
    cal = D.objetivos_calibrables(obj)["objetivo"].unique().to_list()
    filas = []
    for uso, lim in (("calibrar", c["tvd_marginales"]), ("reservar", c["tvd_cruces"])):
        o = obj.filter(
            (pl.col("uso") == uso) & (pl.col("objetivo").is_in(cal) | (uso == "reservar"))
        )
        a = D.recuentos(comb, o, "peso")
        b = D.recuentos(nac, o, "peso")
        for (ob,), g in a.group_by("objetivo", maintain_order=True):
            h = b.filter(pl.col("objetivo") == ob).select("clave", pl.col("sintetico").alias("nac"))
            j = g.join(h, on="clave", how="full", coalesce=True).fill_null(0)
            if j["nac"].sum() <= 0 or j["sintetico"].sum() <= 0:
                continue
            d = M.tvd(j["sintetico"], j["nac"])
            filas.append({"uso": uso, "objetivo": ob, "tvd": d, "umbral": lim, "ok": d <= lim})
    return {"nacional": nacional, "comparaciones": filas}


def territorio_reservado(u: D.Unidades) -> dict:
    """F5, tarea 6: la comunidad calibrada sin sus objetivos socioeconómicos; estos se comprueban
    como reservados con el umbral de comunidad (máx(1,2 × TVD_ref + 0,002, 0,05))."""
    from sinpop.targets import run

    m = PB.construir(RESERVADO, N_CCAA, SEMILLA, u=u, excluir=SOCIOECONOMICOS)
    p, _, _ = V.cargar(m["run_id"])
    pp = V.preparar(p)
    obj = run.leer(RESERVADO).filter(pl.col("objetivo").is_in(list(SOCIOECONOMICOS)))
    r = D.recuentos(pp, obj, "peso")
    cfg = V.umbrales()
    filas = []
    for (ob,), g in r.group_by("objetivo", maintain_order=True):
        ref = M.tvd_ref(
            g["valor"].to_numpy(),
            m["tamano_obtenido"],
            cfg["V-MARG"]["muestras_ref"],
            cfg["V-MARG"]["percentil_ref"],
            SEMILLA,
        )
        um = max(
            cfg["V-CRUCE"]["factor_tvd_ref"] * ref + cfg["V-CRUCE"]["tolerancia"],
            cfg["V-CRUCE"]["ccaa"],
        )
        d = M.tvd(g["sintetico"], g["valor"])
        filas.append({"objetivo": ob, "tvd": d, "tvd_ref": ref, "umbral": um, "ok": d <= um})
    vm = V.v_marg(pp, RESERVADO, SEMILLA)
    return {
        "territorio": RESERVADO,
        "run_id": m["run_id"],
        "excluidos": list(SOCIOECONOMICOS),
        "socioeconomicos": filas,
        "v_marg_resto": {"comprobaciones": vm.height, "fallos": int((~vm["ok"]).sum())},
    }


def ejecutar() -> dict:
    u = PB.unidades_todas()
    res = {
        "fecha": dt.date.today().isoformat(),
        "version_codigo": code_version(),
        "comando": "python -m sinpop.validate.fase5",
        "semilla": SEMILLA,
        "territorios": [],
    }
    for t, n in territorios():
        meta = PB.construir(t, n, SEMILLA, u=u)
        x = _validar(meta)
        res["territorios"].append(x)
        print(
            f"{t}: V-MARG {len(x['v_marg']['fallos'])}/{x['v_marg']['comprobaciones']}, "
            f"V-CRUCE {len(x['v_cruce']['fallos'])}/{x['v_cruce']['comprobaciones']}, "
            f"local {x['donantes']['proporcion_local']:.3f}",
            flush=True,
        )
        RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")
    nac = PB.construir("ES", N_ES, SEMILLA, u=u)
    res["coherencia"] = coherencia(
        [x for x in res["territorios"] if x["territorio"].startswith("CCAA:")], nac["run_id"]
    )
    res["territorio_reservado"] = territorio_reservado(u)
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")
    return res


if __name__ == "__main__":
    r = ejecutar()
    print(json.dumps(r["coherencia"], indent=1)[:3000])
    print(json.dumps(r["territorio_reservado"], indent=1))
