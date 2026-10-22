"""Prueba de humo del servicio local (F13): una pregunta de ejemplo contra `sinpop serve`.

Uso: `python tools/prueba_servicio.py <run_id> [url]` (por defecto http://127.0.0.1:8000).
"""

from __future__ import annotations

import json
import sys
import time
import urllib.request


def main(run: str, base: str = "http://127.0.0.1:8000") -> dict:
    def post(ruta: str, cuerpo: dict) -> dict:
        q = urllib.request.Request(
            base + ruta, json.dumps(cuerpo).encode(), {"Content-Type": "application/json"}
        )
        return json.load(urllib.request.urlopen(q))

    def get(ruta: str) -> dict:
        return json.load(urllib.request.urlopen(base + ruta))

    t = post(
        "/api/preguntas",
        {
            "run_id": run,
            "enunciado": "¿Cómo calificaría usted la situación económica actual de España?",
            "opciones": ["Muy buena", "Buena", "Regular", "Mala", "Muy mala", "N.S.", "N.C."],
        },
    )["trabajo"]
    while (s := get(f"/api/trabajos/{t}"))["estado"] not in ("hecho", "error"):
        time.sleep(3)
    return s


if __name__ == "__main__":
    s = main(*sys.argv[1:])
    r = s.get("resultado") or {}
    print(s["estado"], s.get("mensaje"))
    print(r.get("territorio"), {k: round(v["p"], 3) for k, v in r.get("total", {}).items()})
    print(r.get("confianza", {}).get("total"), r.get("confianza", {}).get("metodo"))
    print(list(r.get("por_subgrupo", {}))[:8], r.get("coste"))
