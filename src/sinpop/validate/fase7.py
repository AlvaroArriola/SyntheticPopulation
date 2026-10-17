"""Validación de F7: auditoría de sesgos y minorías (docs/04 F7, docs/05 §6, docs/06).

Audita la población nacional de 1.000.000 de personas (semilla 1) y los 31 territorios de la
serie F5 (`sinpop audit`): representación, perfil interno, concentración de donantes y calidad
de cada grupo vigilado, con su semáforo; V-DIVERSIDAD frente a los donantes ponderados de la
calibración y V-RAREZA. Resumen en `reports/fase_07_validacion.json` y detalle por población en
`reports/fase_07/`. Comando: `python -m sinpop.validate.fase7`.
"""

from __future__ import annotations

import datetime as dt
import gc
import json

import polars as pl

from sinpop import REPORTS_DIR
from sinpop.audit import auditoria as A
from sinpop.repro import code_version
from sinpop.synth import pesos as P
from sinpop.synth import poblacion as PB
from sinpop.validate import fase5
from sinpop.validate import poblacion as V

RESUMEN = REPORTS_DIR / "fase_07_validacion.json"
DETALLE = REPORTS_DIR / "fase_07"
NACIONAL = "2026-01-01_ES_1000000_s1"


def poblaciones() -> list[tuple[str, str]]:
    """(territorio, run_id) de la población nacional y de la serie F5."""
    r = json.loads(fase5.RESUMEN.read_text("utf-8"))
    return [("ES", NACIONAL)] + [(x["territorio"], x["run_id"]) for x in r["territorios"]]


def _referencia_diversidad(u, territorio: str) -> pl.DataFrame:
    """Donantes con sus pesos calibrados (la población «ideal» antes de integerizar)."""
    cal, _ = PB.calibracion(u, territorio)
    p = P.personas_ponderadas(u, cal)
    return V.preparar(p)


def ejecutar(diversidad: bool = True) -> dict:
    DETALLE.mkdir(parents=True, exist_ok=True)
    u = PB.unidades_todas() if diversidad else None
    res = {
        "fecha": dt.date.today().isoformat(),
        "version_codigo": code_version(),
        "comando": "python -m sinpop.validate.fase7",
        "poblaciones": [],
    }
    for territorio, rid in poblaciones():
        p, lin, _ = V.cargar(rid)
        a = A.auditar(p, lin, territorio)
        a.write_json(DETALLE / f"{rid}_auditoria.json")
        x = {
            "territorio": territorio,
            "run_id": rid,
            "grupos": a.to_dicts(),
            "semaforo": dict(a["semaforo"].value_counts().iter_rows()),
        }
        if diversidad and (territorio == "ES" or territorio.startswith("CCAA:")):
            # España se calibra por comunidades (D-038.3): referencia bloque a bloque
            pp = V.preparar(p)
            bloques = P.bloques(territorio)
            gs = []
            for b in bloques:
                ref = _referencia_diversidad(u, b)
                sub = (
                    pp.filter(pl.col("ccaa") == b.removeprefix("CCAA:")) if len(bloques) > 1 else pp
                )
                gs.append(A.diversidad_grupos(sub, ref))
                del ref
                gc.collect()
            dv = A.v_diversidad(pl.concat(gs))
            dv.write_csv(DETALLE / f"{rid}_diversidad.csv")
            x["v_diversidad"] = dv.to_dicts()
        if territorio == "ES":
            x["v_rareza"] = V.v_rareza(V.preparar(p)).to_dicts()
        res["poblaciones"].append(x)
        rojos = [g["grupo"] for g in x["grupos"] if g["semaforo"] == "rojo"]
        print(f"{territorio}: {x['semaforo']} rojos {rojos}", flush=True)
        RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")
        del p, lin, a
        gc.collect()
    return res


if __name__ == "__main__":
    import sys

    ejecutar(diversidad="--sin-diversidad" not in sys.argv)
