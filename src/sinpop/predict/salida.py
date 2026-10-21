"""Formato de entrada y salida de una predicción (`03_arquitectura.md` §2.8) (D-069).

La salida se valida contra `ESQUEMA` (JSON Schema) y además se comprueba lo que un esquema no
expresa (V-FORMATO): cada distribución tiene todas las opciones de la pregunta, NS/NC incluido,
y suma 1; cada intervalo contiene su p y el del 95 % contiene al del 80 %.

Sin modelo de lenguaje, `parametros_llm` es nulo, el coste es cero y `versiones.modelo_llm` y
`versiones.prompts` son nulos. `medicion_cis` añade la distribución «como la mediría el CIS»
(misma predicción, población reponderada a la composición de voto de sus muestras): es la
comparable con un barómetro; `total` es la de la población.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import numpy as np

from sinpop import REPORTS_DIR
from sinpop.predict import estimador as E

PREDICCIONES_DIR = REPORTS_DIR / "fase_09" / "predicciones"

_DIST = {
    "type": "object",
    "additionalProperties": {
        "type": "object",
        "required": ["p", "ic80", "ic95"],
        "properties": {
            "p": {"type": "number", "minimum": 0, "maximum": 1},
            "ic80": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
            "ic95": {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2},
        },
        "additionalProperties": False,
    },
}
ESQUEMA_ENTRADA = {
    "type": "object",
    "required": ["id", "tipo", "enunciado", "opciones"],
    "properties": {
        "id": {"type": "string"},
        "tipo": {"enum": ["pregunta", "evento"]},
        "enunciado": {"type": "string", "minLength": 1},
        "opciones": {"type": "array", "items": {"type": "string"}, "minItems": 2},
        "escala": {"enum": ["ordinal", "nominal"]},
        "poblacion": {"type": "object"},
        "fecha_referencia": {"type": "string", "pattern": r"^\d{4}-\d{2}$"},
        "subgrupos": {"type": "array", "items": {"type": "string"}},
        "evento": {"type": "object"},
    },
}
ESQUEMA = {
    "type": "object",
    "required": [
        "id",
        "run_id",
        "total",
        "por_subgrupo",
        "confianza",
        "parametros_llm",
        "preguntas_similares",
        "coste",
        "versiones",
    ],
    "properties": {
        "id": {"type": "string"},
        "run_id": {"type": "string"},
        "total": _DIST,
        "medicion_cis": _DIST,
        "por_subgrupo": {"type": "object", "additionalProperties": _DIST},
        "confianza": {
            "type": "object",
            "required": ["total", "por_subgrupo"],
            "properties": {
                "total": {"type": "number", "minimum": 0, "maximum": 1},
                "por_subgrupo": {"type": "object"},
            },
        },
        "parametros_llm": {"type": ["object", "null"]},
        "preguntas_similares": {"type": "array", "items": {"type": "string"}},
        "coste": {
            "type": "object",
            "required": ["llamadas", "tokens", "eur", "segundos"],
        },
        "versiones": {"type": "object", "required": ["modelo_llm", "prompts", "poblacion"]},
    },
}


def _dist(opciones: list[str], mu: np.ndarray, sd: np.ndarray, cal: dict, similitud: float) -> dict:
    mu = mu / mu.sum()
    i80, i95 = E.intervalos(mu, sd, cal, similitud)
    return {
        o: {
            "p": round(float(mu[j]), 6),
            "ic80": [round(float(i80[j, 0]), 6), round(float(i80[j, 1]), 6)],
            "ic95": [round(float(i95[j, 0]), 6), round(float(i95[j, 1]), 6)],
        }
        for j, o in enumerate(opciones)
    }


def confianza(r: E.Resultado) -> float:
    """Provisional hasta F10 (modelo de confianza): la similitud de la mejor análoga, rebajada
    por el desacuerdo entre análogas."""
    if not r.analogas:
        return 0.0
    desacuerdo = float(np.mean(r.sistema_sd["total"])) * 10
    return float(np.clip(r.analogas[0]["similitud"] * (1 - desacuerdo), 0, 1))


def construir(r: E.Resultado, run_id: str) -> dict:
    q, cal = r.pregunta, E.calibracion()
    if not r.analogas:
        raise ValueError(f"{q.id}: sin preguntas parecidas alineables en el banco")
    c = confianza(r)
    sim = r.analogas[0]["similitud"]
    out = {
        "id": q.id,
        "run_id": run_id,
        "total": _dist(q.opciones, r.sistema["total"], r.sistema_sd["total"], cal, sim),
        "medicion_cis": _dist(
            q.opciones, r.sistema_cis["total"], r.sistema_cis_sd["total"], cal, sim
        ),
        "por_subgrupo": {
            k: _dist(q.opciones, v, r.sistema_sd[k], cal, sim)
            for k, v in r.sistema.items()
            if k != "total"
        },
        "confianza": {
            "total": c,
            "por_subgrupo": {k: c for k in r.sistema if k != "total"},
            "metodo": "provisional (F10): similitud con el banco y desacuerdo entre análogas",
        },
        "parametros_llm": None,
        "parametros": {
            "estimador": "estadistico_sin_llm",
            "escala": q.escala,
            "analogas": [
                {
                    "id": a["id"],
                    "similitud": round(a["similitud"], 4),
                    "peso": round(a["peso_analoga"], 4),
                    "encuestados": a.get("encuestados"),
                }
                for a in r.analogas
            ],
            "calibracion": {k: v for k, v in cal.items() if k != "combinacion"},
            "combinacion_medicion_cis": cal.get("combinacion"),
        },
        "preguntas_similares": [a["id"] for a in r.analogas],
        "coste": {"llamadas": 0, "tokens": 0, "eur": 0.0, "segundos": round(r.segundos, 2)},
        "versiones": {"modelo_llm": None, "prompts": None, "poblacion": run_id},
    }
    validar(out, q.opciones)
    return out


def validar(out: dict, opciones: list[str]) -> None:
    """V-FORMATO: esquema y coherencia de cada distribución."""
    jsonschema.validate(out, ESQUEMA)
    dists = {"total": out["total"], **out["por_subgrupo"]}
    if "medicion_cis" in out:
        dists["medicion_cis"] = out["medicion_cis"]
    for k, d in dists.items():
        if list(d) != list(opciones):
            raise ValueError(f"{out['id']} {k}: opciones distintas de las de la pregunta")
        s = sum(v["p"] for v in d.values())
        if abs(s - 1) > 1e-4:
            raise ValueError(f"{out['id']} {k}: la distribución suma {s}")
        for o, v in d.items():
            a80, b80 = v["ic80"]
            a95, b95 = v["ic95"]
            if not (a95 <= a80 <= v["p"] + 1e-9 and v["p"] - 1e-9 <= b80 <= b95):
                raise ValueError(f"{out['id']} {k} {o}: intervalos incoherentes")


def predecir_fichero(entrada: Path, run_id: str = "2026-01-01_ES_1000000_s1") -> Path:
    """Lee `preguntas/<id>.json`, predice y escribe `predicciones/<id>_<run_id>.json`."""
    q = json.loads(entrada.read_text("utf-8"))
    jsonschema.validate(q, ESQUEMA_ENTRADA)
    from sinpop.predict import opciones as O

    p = E.Pregunta(
        q["id"],
        q["enunciado"],
        q["opciones"],
        q.get("escala") or O.escala_probable(q["opciones"]),
        q.get("fecha_referencia", "2026-07"),
        q.get("subgrupos", list(E.SUBGRUPOS)),
    )
    out = construir(E.predecir(p, run_id=run_id), run_id)
    PREDICCIONES_DIR.mkdir(parents=True, exist_ok=True)
    destino = PREDICCIONES_DIR / f"{q['id']}_{run_id}.json"
    destino.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    return destino
