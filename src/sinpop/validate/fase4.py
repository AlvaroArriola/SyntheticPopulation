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

    obj = D.objetivos_calibrables(run.leer(territorio), municipios=territorio.startswith("MUNIS:"))
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
            # Criterio aprobado (D-038 A); `excepcion`: limitación aceptada (D-038 B).
            "fallos": vc.filter(~pl.col("ok"))
            .select("nivel", "territorio", "objetivo", "tvd", "umbral", "excepcion")
            .to_dicts(),
            "espana": vc.filter(pl.col("nivel") == "espana")
            .select("objetivo", "tvd", "tvd_ref", "umbral", "ok")
            .to_dicts(),
            "tvd_media_espana": float(vc.filter(pl.col("nivel") == "espana")["tvd"].mean()),
            "fallos_estricto": vc.filter(~pl.col("ok_estricto"))
            .select("nivel", "territorio", "objetivo", "tvd", "umbral_estricto")
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
    obj = D.objetivos_calibrables(run.leer(territorio), municipios=territorio.startswith("MUNIS:"))
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


def complementos(res: dict) -> dict:
    """V-DONANTES, V-RAREZA y validación externa (docs/05 §4 y §6) sobre la población más grande
    de la primera semilla; se añaden al resumen."""
    from sinpop.validate import externa as X

    x = [y for y in res["poblaciones"] if "minorias" in y][0]
    p, lin, _ = V.cargar(x["run_id"])
    res["complementos"] = {
        "run_id": x["run_id"],
        "v_donantes": V.v_donantes(p, lin, res["territorio"]).to_dicts(),
        "v_rareza": V.v_rareza(p).to_dicts(),
        "externa": {k: v.to_dicts() for k, v in X.ejecutar(p).items()},
    }
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")
    return res


def _complementos_md(cp: dict) -> list[str]:
    ex = cp["externa"]
    epa = pl.DataFrame(ex["epa"]).select(
        "ccaa",
        "sint_ocupado",
        "ref_ocupado",
        "sint_parado",
        "ref_parado",
        "paro_sint",
        "paro_epa",
        "tvd",
        "dentro",
    )
    pad = pl.DataFrame(ex["padron"]).select(
        "provincia", "sint_extranjera", "ref_extranjera", "tvd", "dentro"
    )
    return [
        f"## V-DONANTES ({cp['run_id']})",
        "",
        _tabla(pl.DataFrame(cp["v_donantes"]), 3),
        "",
        "## V-RAREZA",
        "",
        _tabla(pl.DataFrame(cp["v_rareza"])),
        "",
        "## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)",
        "",
        "### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)",
        "",
        _tabla(epa),
        "",
        "### ECV 2025: personas por tamaño del hogar",
        "",
        _tabla(pl.DataFrame(ex["ecv"])),
        "",
        "### Padrón 01/01/2022: proporción de extranjeros por provincia",
        "",
        _tabla(pad),
        "",
    ]


def _tabla(df: pl.DataFrame, decimales: int = 4) -> str:
    cols = df.columns
    filas = ["| " + " | ".join(cols) + " |", "| " + " | ".join("---" for _ in cols) + " |"]
    for r in df.iter_rows():
        filas.append(
            "| "
            + " | ".join(
                f"{v:.{decimales}f}"
                if isinstance(v, float)
                else ("✅" if v is True else "❌" if v is False else str(v))
                for v in r
            )
            + " |"
        )
    return "\n".join(filas)


def informe(res: dict) -> str:
    """Tablas de `reports/fase_04_validacion.md` a partir del resumen."""
    pobs = res["poblaciones"]
    t = [
        "# Fase 04 · Tablas de validación",
        "",
        f"Generado por `{res['comando']}` "
        f"({res['version_codigo']}, {res['fecha']}). Resumen en `fase_04_validacion.json`; "
        "detalle por población en `fase_04/`.",
        "",
    ]
    t += [
        "## Curva de error frente a tamaño (España; media de 5 semillas)",
        "",
        _tabla(curva(res)),
        "",
    ]
    det = pl.concat(
        [
            pl.read_csv(DETALLE / f"{x['run_id']}_v_marg.csv").with_columns(
                pl.lit(x["n"]).alias("N")
            )
            for x in pobs
        ]
    )
    t += [
        "## TVD por marginal calibrada (España; media de 5 semillas)",
        "",
        _tabla(
            det.filter(pl.col("nivel") == "espana")
            .group_by("objetivo", "N")
            .agg(pl.col("tvd").mean())
            .pivot(on="N", index="objetivo", values="tvd")
            .sort("objetivo")
        ),
        "",
    ]
    detc = pl.concat(
        [
            pl.read_csv(DETALLE / f"{x['run_id']}_v_cruce.csv").with_columns(
                pl.lit(x["n"]).alias("N")
            )
            for x in pobs
        ]
    )
    t += [
        "## TVD por cruce reservado (España; media de 5 semillas)",
        "",
        _tabla(
            detc.filter(pl.col("nivel") == "espana")
            .group_by("objetivo", "N")
            .agg(pl.col("tvd").mean())
            .pivot(on="N", index="objetivo", values="tvd")
            .sort("objetivo")
        ),
        "",
    ]
    t += [
        "## Fallos por tamaño",
        "",
        _tabla(
            pl.DataFrame(
                [
                    {
                        "N": x["n"],
                        "semilla": x["semilla"],
                        "v_marg": len(x["v_marg"]["fallos"]),
                        "v_cruce": sum(not y.get("excepcion") for y in x["v_cruce"]["fallos"]),
                        "v_cruce_excepciones": sum(
                            bool(y.get("excepcion")) for y in x["v_cruce"]["fallos"]
                        ),
                        "v_cruce_estricto": len(x["v_cruce"].get("fallos_estricto", [])),
                        "comprobaciones_cruce": x["v_cruce"]["comprobaciones"],
                    }
                    for x in pobs
                ]
            )
        ),
        "",
    ]
    fc = pl.DataFrame(
        [dict(y, N=x["n"], semilla=x["semilla"]) for x in pobs for y in x["v_cruce"]["fallos"]]
    )
    if fc.height:
        t += [
            "### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas",
            "",
            _tabla(fc.filter(pl.col("N") >= 500_000).sort("N", "semilla")),
            "",
        ]
    t += ["## V-SEMILLAS", "", _tabla(pl.DataFrame(res["v_semillas"]).drop("peores")), ""]
    t += [
        "## V-PESOS (calibración por comunidades)",
        "",
        _tabla(pl.DataFrame(res["calibracion"]["v_pesos"])),
        "",
    ]
    t += [
        "## Ampliación de donantes",
        "",
        _tabla(pl.DataFrame(res["calibracion"]["ampliaciones"])),
        "",
    ]
    if res["calibracion"]["fusiones"]:
        t += [
            "## Nacionalidades fusionadas con «otras extranjeras»",
            "",
            _tabla(pl.DataFrame(res["calibracion"]["fusiones"])),
            "",
        ]
    grande = [x for x in pobs if "minorias" in x][0]
    t += [f"## V de Cramér ({grande['run_id']})", "", _tabla(pl.DataFrame(grande["v_cramer"])), ""]
    t += [
        f"## Minorías, primera pasada ({grande['run_id']})",
        "",
        _tabla(pl.DataFrame(grande["minorias"]).drop("fuente")),
        "",
    ]
    bl = pl.DataFrame([dict(r, N=x["n"]) for x in pobs for r in x["v_reglas_blandas"]])
    t += [
        "## Reglas blandas (media de 5 semillas; nº de semillas dentro)",
        "",
        _tabla(
            bl.group_by("regla", "N")
            .agg(
                pl.col("frecuencia_donantes").first(),
                pl.col("exceso_relativo").mean(),
                pl.col("ok_estricto").sum(),
                pl.col("ok").sum(),
            )
            .sort("regla", "N"),
            6,
        ),
        "",
    ]
    g = res["g47"]
    t += [
        f"## G4.7 · Sobremuestreo ({g['spec']}, {g['run_id']})",
        "",
        f"Miembros del grupo: {g['miembros']} (mínimo pedido {g['minimo']}); "
        f"α = {g['alfa_beta']['alfa']:.4f}, "
        f"β = {g['alfa_beta']['beta']:.4f}; suma de pesos {g['suma_pesos']:.0f}.",
        "",
        _tabla(pl.DataFrame(g["marginales"])),
        "",
    ]
    if "complementos" in res:
        t += _complementos_md(res["complementos"])
    r = res["v_repro"]
    t += [
        "## V-REPRO",
        "",
        f"{r['run_id']} generado de nuevo en otro directorio: "
        f"{'mismos hashes' if r['hashes_iguales'] else 'hashes distintos'}.",
        "",
    ]
    for k, v in r["sha256"].items():
        t.append(f"- `{k}`: `{v}`")
    texto = "\n".join(t) + "\n"
    (REPORTS_DIR / "fase_04_validacion.md").write_text(texto, encoding="utf-8")
    return texto


def validar_poblacion(rid: str) -> bool:
    """`sinpop validate --run <run_id>`: V-MARG, V-CRUCE, Cramér, reglas, donantes, rareza y
    minorías de una población; escribe `reports/<run_id>/validacion.md` y actualiza el estado
    de validación en su `metadata.json`."""
    from sinpop import POPULATIONS_DIR

    p, lin, meta = V.cargar(rid)
    terr = meta["territorio"]["codigo"]
    semilla = meta["semilla"]
    pp = V.preparar(p)
    vm = V.v_marg(pp, terr, semilla)
    vc = V.v_cruce(pp, terr, semilla)
    cr = V.v_cramer(pp, terr)
    duras = V.v_reglas_duras(pp)
    blandas = V.v_reglas_blandas(pp, meta["referencia_reglas_blandas"])
    don = V.v_donantes(p, lin, terr)
    rar = V.v_rareza(p)
    mino = V.v_minorias(p, lin, terr)
    ok = bool(
        vm["ok"].all()
        and vc["ok"].all()
        and cr["ok"].all()
        and duras["ok"].all()
        and rar["ok"].all()
    )
    out = REPORTS_DIR / rid
    out.mkdir(parents=True, exist_ok=True)
    t = [
        f"# Validación de {rid}",
        "",
        f"**Estado:** {'superada' if ok else 'fallida'} · {meta['tamano_obtenido']} personas · "
        f"semilla {semilla} · {code_version()}",
        "",
        "## V-MARG",
        "",
        _tabla(vm.select("nivel", "territorio", "objetivo", "tvd", "umbral", "ok")),
        "",
        "## V-CRUCE",
        "",
        _tabla(
            vc.filter((pl.col("nivel") == "espana") | ~pl.col("ok")).select(
                "nivel", "territorio", "objetivo", "tvd", "umbral", "ok", "excepcion"
            )
        ),
        "",
        "## V de Cramér",
        "",
        _tabla(cr),
        "",
        "## Reglas duras",
        "",
        _tabla(duras),
        "",
        "## Reglas blandas",
        "",
        _tabla(blandas, 6),
        "",
        "## V-DONANTES",
        "",
        _tabla(don, 3),
        "",
        "## V-RAREZA",
        "",
        _tabla(rar),
        "",
        "## Minorías (primera pasada)",
        "",
        _tabla(mino.drop("fuente")),
        "",
    ]
    (out / "validacion.md").write_text("\n".join(t) + "\n", encoding="utf-8")
    meta["validacion"] = {
        "estado": "superada" if ok else "fallida",
        "informe": f"reports/{rid}/validacion.md",
    }
    (POPULATIONS_DIR / rid / "metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), "utf-8"
    )
    return ok


if __name__ == "__main__":
    r = complementos(ejecutar())
    informe(r)
    print(curva(r))
    print(json.dumps(r["v_semillas"], indent=1)[:2000])
    print(r["v_repro"]["hashes_iguales"], r["g47"]["ok"])
