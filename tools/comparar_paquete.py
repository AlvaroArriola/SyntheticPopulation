"""Compara las predicciones del modo paquete (D-076) con las del modo completo.

Toma una muestra fija de preguntas del banco y les cambia el identificador para tratarlas como
preguntas nuevas. Predice cada una dos veces sobre la misma población, en procesos separados:
una con los microdatos y otra con `SINPOP_PAQUETE`. Mide la distancia de variación total (TVD)
entre los totales y la diferencia de confianza. Guarda `reports/fase_13/comparacion_paquete.json`.

Uso: `python tools/comparar_paquete.py [n] [run_id]`.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PAQUETE = RAIZ / "dist" / "paquete"
DESTINO = RAIZ / "reports" / "fase_13" / "comparacion_paquete.json"


def _hijo(preguntas: Path, run: str, salida: Path) -> None:
    from sinpop.predict import salida as S

    out = {}
    for q in json.loads(preguntas.read_text("utf-8")):
        r = S.predecir_dict(q, run)
        out[q["id"]] = {
            "total": {k: v["p"] for k, v in r["total"].items()},
            "confianza": r["confianza"]["total"],
        }
    salida.write_text(json.dumps(out), "utf-8")


def main(n: int = 40, run: str = "2026-01-01_ES_1000000_s1") -> dict:
    import polars as pl

    from sinpop.predict import banco as B

    # enunciados con contenido (el banco tiene algunos residuales como «Otros»)
    b = B.preguntas().filter(pl.col("enunciado").str.len_chars() >= 25).sample(n, seed=1)
    qs = [
        {
            "id": f"CMP-{i:03d}",
            "tipo": "pregunta",
            "enunciado": f["enunciado"],
            "opciones": f["opciones"],
        }
        for i, f in enumerate(b.select("enunciado", "opciones").to_dicts())
    ]
    tmp = Path(tempfile.mkdtemp())
    (tmp / "q.json").write_text(json.dumps(qs, ensure_ascii=False), "utf-8")
    res = {}
    for modo in ("completo", "paquete"):
        env = {
            k: v
            for k, v in os.environ.items()
            if k not in ("SINPOP_PAQUETE", "SINPOP_ANTHROPIC_API_KEY")
        }
        if modo == "paquete":
            env["SINPOP_PAQUETE"] = str(PAQUETE)
        subprocess.run(
            [
                sys.executable,
                "-W",
                "ignore",
                __file__,
                "--hijo",
                str(tmp / "q.json"),
                run,
                str(tmp / f"{modo}.json"),
            ],
            check=True,
            env=env,
            cwd=RAIZ,
        )
        res[modo] = json.loads((tmp / f"{modo}.json").read_text("utf-8"))
    filas = []
    for q in qs:
        a, p = res["completo"][q["id"]], res["paquete"][q["id"]]
        tvd = 0.5 * sum(abs(a["total"][o] - p["total"][o]) for o in a["total"])
        filas.append({"id": q["id"], "tvd": tvd, "dif_confianza": p["confianza"] - a["confianza"]})
    d = pl.DataFrame(filas)
    out = {
        "run_id": run,
        "preguntas": n,
        "tvd_media": round(d["tvd"].mean(), 4),
        "tvd_p90": round(d["tvd"].quantile(0.9), 4),
        "tvd_max": round(d["tvd"].max(), 4),
        "dif_confianza_media_abs": round(d["dif_confianza"].abs().mean(), 4),
        "filas": filas,
    }
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    return out


if __name__ == "__main__":
    if sys.argv[1:2] == ["--hijo"]:
        _hijo(Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4]))
    else:
        r = main(*[int(sys.argv[1])] if sys.argv[1:] else [], *sys.argv[2:3])
        print({k: v for k, v in r.items() if k != "filas"})
