"""Ensayo de D-042 (propuesta): calibrar la nacionalidad española/extranjera por edad quinquenal.

Añade en memoria, sin tocar `configs/` ni `data/processed/targets/`, el objetivo calibrado
`nacionalidad_edad` (nacionalidad_esp_ext × edad_5; residentes; ECP 2026 tabla 60129 y colectivos
como en `targets.build.nacionalidad_celdas`), regenera algunas comunidades con la semilla de la
serie F5 y compara V-MARG, V-CRUCE y V de Cramér con la serie. Las poblaciones del ensayo van a
`data/processed/ensayos/d042/` y el resumen a `reports/fase_05/ensayo_d042.json`.
Uso: python tools/ensayo_d042.py [CCAA:09 CCAA:18 ...]
"""

from __future__ import annotations

import json
import sys

import polars as pl

from sinpop import PROCESSED_DIR, REPORTS_DIR
from sinpop.harmonize.core import ccaa_de_provincia
from sinpop.synth import donantes as D
from sinpop.synth import poblacion as PB
from sinpop.targets import build, run
from sinpop.validate import fase5
from sinpop.validate import poblacion as V

OBJETIVO = "nacionalidad_edad"
VARIABLES = ["nacionalidad_esp_ext", "edad_5"]
DESTINO = PROCESSED_DIR / "ensayos" / "d042"
TERRITORIOS = ["CCAA:09", "CCAA:13", "CCAA:18", "CCAA:19"]

_celdas = (
    build.nacionalidad_celdas()
    .filter(pl.col("variable") == "nacionalidad_grupo")
    .with_columns(
        pl.when(pl.col("categoria") == "espanola")
        .then(pl.lit("espanola"))
        .otherwise(pl.lit("extranjera"))
        .alias("nacionalidad_esp_ext"),
        pl.col("provincia").replace_strict(ccaa_de_provincia()).alias("ccaa"),
    )
)
_leer, _variables_de = run.leer, D.variables_de


def _filas(territorio: str) -> pl.DataFrame:
    tipo, cod = territorio.split(":", 1) if ":" in territorio else ("ES", "")
    c = _celdas
    if tipo == "CCAA":
        c = c.filter(pl.col("ccaa") == cod)
    elif tipo == "PROV":
        c = c.filter(pl.col("provincia") == cod)
    elif tipo != "ES":
        return pl.DataFrame()
    g = c.group_by(VARIABLES).agg(pl.col("valor").sum()).sort(VARIABLES)
    return g.select(
        pl.lit(territorio).alias("territorio"),
        pl.lit(OBJETIVO).alias("objetivo"),
        pl.lit("calibrar").alias("uso"),
        pl.lit("persona").alias("unidad"),
        pl.lit("residentes").alias("universo"),
        pl.concat_str(
            [pl.lit("nacionalidad_esp_ext="), "nacionalidad_esp_ext", pl.lit(";edad_5="), "edad_5"]
        ).alias("clave"),
        "valor",
        pl.lit("ecp: tabla 60129 + colectivos (ensayo D-042)").alias("fuente"),
        pl.lit("2026-01-01").alias("edicion"),
    )


def leer(territorio: str) -> pl.DataFrame:
    o = _leer(territorio)
    f = _filas(territorio)
    if f.is_empty():
        return o
    f = f.with_columns(
        pl.lit(o["fecha_referencia"][0]).alias("fecha_referencia"),
        pl.lit("suma de celdas provincia × sexo × edad_5").alias("metodo"),
    )
    return pl.concat([o, f.select(o.columns)], how="vertical_relaxed")


def variables_de(objetivo: str) -> list[str]:
    return list(VARIABLES) if objetivo == OBJETIVO else _variables_de(objetivo)


def main(ts: list[str]) -> None:
    run.leer, D.variables_de = leer, variables_de
    resumen = json.loads(fase5.RESUMEN.read_text("utf-8"))
    serie = {x["territorio"]: x for x in resumen["territorios"]}
    u = PB.unidades_todas()
    out = []
    for t in ts:
        # `excluir` con un nombre que no existe solo separa la caché de calibración del ensayo.
        m = PB.construir(t, fase5.N_CCAA, fase5.SEMILLA, u=u, destino=DESTINO, excluir=("d042",))
        p, _, _ = V.cargar(m["run_id"], DESTINO)
        pp = V.preparar(p)
        vm, vc, cr = V.v_marg(pp, t, 1), V.v_cruce(pp, t, 1), V.v_cramer(pp, t)
        nac = cr.filter(pl.col("objetivo") == "adultos_nacionalidad").to_dicts()[0]
        base = [c for c in serie[t]["v_cramer"] if c["objetivo"] == "adultos_nacionalidad"][0]
        x = {
            "territorio": t,
            "v_marg_fallos": int((~vm["ok"]).sum()),
            "v_marg": vm.height,
            "v_cruce_fallos": vc.filter(~pl.col("ok") & ~pl.col("excepcion"))
            .select("nivel", "territorio", "objetivo", "tvd", "umbral")
            .to_dicts(),
            "v_cruce": vc.height,
            "v_cruce_fallos_serie": len(serie[t]["v_cruce"]["fallos"]),
            "cramer_fuera": int((~cr["ok"]).sum()),
            "cramer_adultos_nacionalidad": {
                "oficial": nac["v_oficial"],
                "serie": base["v_sintetica"],
                "ensayo": nac["v_sintetica"],
            },
            "proporcion_local": m["donantes"]["proporcion_local"],
            "kish_hogares_donantes": m["donantes"]["kish_hogares_donantes"],
            "kish_serie": serie[t]["donantes"]["kish_hogares_donantes"],
        }
        print(json.dumps(x, ensure_ascii=False, default=float), flush=True)
        out.append(x)
    dest = REPORTS_DIR / "fase_05" / "ensayo_d042.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), "utf-8")


if __name__ == "__main__":
    main(sys.argv[1:] or TERRITORIOS)
