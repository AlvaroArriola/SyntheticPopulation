"""Prueba de la puerta F13: el servicio devuelve lo mismo que la CLI y con el formato de §2.8.

Para las preguntas y eventos de ejemplo de `preguntas/` (sobre España y, si está lista, una
comunidad), lanza la consulta por el servicio (en proceso, con el cliente de pruebas de FastAPI) y
por la CLI (`sinpop predict`, en un proceso aparte) y compara los JSON salvo los tiempos y el
identificador que el servicio asigna a la pregunta (G13.1). Comprueba en cada respuesta del
servicio el esquema y la coherencia (`salida.validar`), la marca `resultado_simulado`, el aviso,
los intervalos y la confianza (G13.2). Guarda `reports/fase_13/prueba_servicio.json`.

Uso: `python tools/prueba_f13.py [run_id ...]`.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "reports" / "fase_13"
POR_DEFECTO = ["2026-01-01_ES_1000000_s1", "2026-01-01_CCAA_13_100000_s1"]
IGNORAR = {"segundos"}


def _limpio(x):
    if isinstance(x, dict):
        return {k: _limpio(v) for k, v in x.items() if k not in IGNORAR}
    if isinstance(x, list):
        return [_limpio(v) for v in x]
    return x


def _diferencias(a, b, ruta="") -> list[str]:
    if isinstance(a, dict) and isinstance(b, dict):
        out = [f"{ruta}/{k}: solo en uno" for k in set(a) ^ set(b)]
        for k in set(a) & set(b):
            out += _diferencias(a[k], b[k], f"{ruta}/{k}")
        return out
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        return [
            d
            for i, (u, v) in enumerate(zip(a, b, strict=True))
            for d in _diferencias(u, v, f"{ruta}[{i}]")
        ]
    return [] if a == b else [ruta or "/"]


def _formato(out: dict, opciones: list[str]) -> list[str]:
    from sinpop.predict import salida as S

    fallos = []
    try:
        S.validar(out, opciones)
    except Exception as e:  # noqa: BLE001
        fallos.append(f"esquema: {str(e)[:200]}")
    if out.get("resultado_simulado") is not True:
        fallos.append("sin resultado_simulado")
    if "simulado" not in (out.get("aviso") or ""):
        fallos.append("sin aviso")
    for o, v in out.get("total", {}).items():
        if not (v.get("ic80") and v.get("ic95")):
            fallos.append(f"sin intervalo: {o}")
    if (out.get("confianza") or {}).get("total") is None:
        fallos.append("sin confianza total")
    return fallos


def _cli(args: list[str], fichero: str, carpeta: Path) -> dict:
    subprocess.run(["sinpop", "predict", *args], check=True, cwd=RAIZ, capture_output=True)
    return json.loads((carpeta / fichero).read_text("utf-8"))


def _servicio(cliente, ruta: str, cuerpo: dict) -> dict:
    t = cliente.post(ruta, json=cuerpo).json()["trabajo"]
    while (s := cliente.get(f"/api/trabajos/{t}").json())["estado"] not in ("hecho", "error"):
        time.sleep(2)
    if s["estado"] == "error":
        raise RuntimeError(s.get("mensaje"))
    return s["resultado"]


def main(runs: list[str]) -> dict:
    from fastapi.testclient import TestClient

    from sinpop.predict.salida import PREDICCIONES_DIR
    from sinpop.servicio import app as A

    cliente = TestClient(A.crear_app())
    listas = {p["run_id"] for p in A.poblaciones() if p["lista"]}
    q = json.loads((RAIZ / "preguntas" / "Q001_ejemplo.json").read_text("utf-8"))
    e = json.loads((RAIZ / "preguntas" / "E002_ejemplo.json").read_text("utf-8"))
    casos = []
    # la CLI escribe en reports/fase_09/predicciones; se guarda y se restaura lo que hubiera
    copia = Path(tempfile.mkdtemp())
    if PREDICCIONES_DIR.exists():
        shutil.copytree(PREDICCIONES_DIR, copia / "p")
    try:
        for rid in runs:
            if rid not in listas:
                casos.append({"run_id": rid, "omitido": "población no lista"})
                continue
            cuerpo = {k: q[k] for k in ("enunciado", "opciones")}
            sv = _servicio(
                cliente, "/api/preguntas", {"run_id": rid, **cuerpo, "escala": q.get("escala")}
            )
            cli = _cli(
                ["--question", "preguntas/Q001_ejemplo.json", "--run", rid],
                f"Q001_{rid}.json",
                PREDICCIONES_DIR,
            )
            sv_c = _limpio({**sv, "id": cli["id"]})
            casos.append(
                {
                    "run_id": rid,
                    "tipo": "pregunta",
                    "diferencias": _diferencias(sv_c, _limpio(cli))[:20],
                    "formato": _formato(sv, q["opciones"]),
                }
            )
            ev = e["evento"]
            sv = _servicio(
                cliente,
                "/api/eventos",
                {
                    "run_id": rid,
                    "enunciado": e["enunciado"],
                    "opciones": e["opciones"],
                    "escala": e["escala"],
                    **ev,
                },
            )
            cli = _cli(
                ["--event", "preguntas/E002_ejemplo.json", "--run", rid],
                "E002_evento.json",
                PREDICCIONES_DIR,
            )
            casos.append(
                {
                    "run_id": rid,
                    "tipo": "evento",
                    "diferencias": _diferencias(_limpio({**sv, "id": cli["id"]}), _limpio(cli))[
                        :20
                    ],
                    "formato": []
                    if sv.get("resultado_simulado") and "simulado" in sv.get("aviso", "")
                    else ["sin marca o aviso"],
                }
            )
    finally:
        shutil.rmtree(PREDICCIONES_DIR, ignore_errors=True)
        if (copia / "p").exists():
            shutil.copytree(copia / "p", PREDICCIONES_DIR)
        shutil.rmtree(copia, ignore_errors=True)

    hechos = [c for c in casos if "omitido" not in c]
    res = {
        "casos": casos,
        "g13_1": bool(hechos) and all(not c["diferencias"] for c in hechos),
        "g13_2": bool(hechos) and all(not c["formato"] for c in hechos),
    }
    DESTINO.mkdir(parents=True, exist_ok=True)
    (DESTINO / "prueba_servicio.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), "utf-8"
    )
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1:] or POR_DEFECTO), ensure_ascii=False, indent=1))
