"""Batería de validación para la interfaz «Validación» (D-091): previsto frente a real.

Para cada pregunta de los barómetros del CIS posteriores al corte (junio de 2026) — validación
(`validacion.VALIDACION`, julio y septiembre) y evaluación final (`validacion.EVALUACION_FINAL`,
octubre; F11 ya ejecutada) — guarda en `reports/validacion/bateria.json`:

- **Lo que midió el CIS** (agregado, nunca respuestas individuales): distribución ponderada de los
  españoles de 18+ con su margen de muestreo del 95 % (tamaño efectivo de Kish), en total y por
  ocho dimensiones del perfil (edad, sexo, estudios, situación laboral, tamaño del municipio,
  comunidad, religiosidad y clase social), cada grupo con su número de encuestados.
- **Lo que predijo el sistema** sin ver esa encuesta: como lo mediría el CIS, con sus intervalos
  del 80 % y del 95 % y su confianza; por grupos, la población posestratificada (igual que en F9).
  Donde no había análogas fiables y el LLM anclado respondió en la evaluación, su respuesta guardada
  en caché (no se hace ninguna llamada nueva); si no está en caché, el estimador estadístico.
- **Error:** TVD total y por grupo, y si la diferencia supera el margen de muestreo.
- **Importancia de las variables** (`predict/importancia.py`) prevista y observada.
- **De dónde sale:** preguntas del banco en que se apoyó la predicción (estudio, fecha, similitud)
  y las fuentes oficiales del estudio evaluado (cuestionario, ficha técnica y microdatos, con su
  URL del manifiesto de descarga).

Las predicciones se calculan con el paquete portable (D-076), que da los mismos resultados que el
modo completo (TVD máxima 0,0002 en `reports/fase_13/comparacion_paquete.json`) y es mucho más
rápido. Mostrar estos resultados no cambia nada del sistema: no se ajusta ningún parámetro con
ellos (regla 5).

Comando: `SINPOP_PAQUETE=dist/paquete python -m sinpop.evaluate.bateria`.
"""

from __future__ import annotations

import datetime as dt
import json

import numpy as np
import polars as pl
import yaml

from sinpop import REPORTS_DIR
from sinpop.evaluate import EVAL_DIR
from sinpop.evaluate import validacion as V
from sinpop.predict import asistido as A
from sinpop.predict import estimador as E
from sinpop.predict import importancia as IM
from sinpop.predict import opciones as O
from sinpop.predict import poblacion as P
from sinpop.predict import salida as S

DESTINO = REPORTS_DIR / "validacion" / "bateria.json"
DIMENSIONES = [
    "edad_4",
    "sexo",
    "estudios_3",
    "actividad_3",
    "tamano_municipio_cis",
    "ccaa",
    "religiosidad",
    "clase_subjetiva",
]
MIN_GRUPO = 50  # encuestados mínimos para enseñar un grupo observado
Z95 = 1.96


def _kish(w: np.ndarray) -> float:
    return float(w.sum() ** 2 / (w**2).sum()) if len(w) and (w**2).sum() > 0 else 0.0


def _observada(d: pl.DataFrame, opciones: list[str]) -> dict:
    """Distribución ponderada con margen de muestreo del 95 % (normal con n efectivo de Kish)."""
    p = V._dist(d, opciones)
    n_ef = _kish(d["peso"].to_numpy().astype(float))
    m = Z95 * np.sqrt(p * (1 - p) / max(n_ef, 1.0))
    return {
        "p": p,
        "n": d.height,
        "n_efectivo": n_ef,
        "ic95": np.stack([np.clip(p - m, 0, 1), np.clip(p + m, 0, 1)], 1),
    }


def _fuentes_estudio(estudio: str) -> list[dict]:
    m = yaml.safe_load((EVAL_DIR / "MANIFEST.yaml").read_text("utf-8"))
    nombres = {
        "cuestionario": "Cuestionario",
        "metodologia": "Ficha técnica",
        "datos": "Microdatos",
    }
    return [
        {
            "tipo": nombres.get(f["tipo"], f["tipo"]),
            "url": f["url_oficial"],
            "fecha_descarga": f.get("fecha_descarga"),
            "condiciones": f.get("condiciones"),
        }
        for f in m["ficheros"]
        if str(f.get("edicion")) == estudio
    ]


def _llm_en_cache(q: dict, escala: str) -> dict | None:
    """Respuesta del LLM anclado de la evaluación, solo si está en caché (sin llamadas)."""
    from sinpop.llm import cliente as C

    pq = E.Pregunta(q["id"], q["enunciado"], q["opciones"], escala, q["mes"], A.SUBGRUPOS_LLM)
    pet = A.peticion_nueva(pq, A.claves_subgrupo())
    clave = C._solicitud(pet)[1]
    f = C._rutas()[0] / f"{clave}.json"
    if not f.exists():
        return None
    salida = json.loads(f.read_text("utf-8"))["salida"]
    try:
        C._comprobar(salida, pet.esquema, pet.spec)
    except Exception:  # salida guardada que no pasa la validación: no se usa
        return None
    return {"dist": A.distribuciones(salida), "justificacion": salida["justificacion"]}


def _r(x: float, d: int = 4) -> float:
    return round(float(x), d)


def pregunta(q: dict, p: pl.DataFrame, lg: pl.DataFrame, pesos_marco: dict) -> dict | None:
    d = V.verdad(p, lg, q["variable"], q["opciones"])
    if d.height < 200:
        return None
    ops = q["opciones"]
    escala = O.escala_probable(ops)
    pq = E.Pregunta(q["id"], q["enunciado"], ops, escala, q["mes"], DIMENSIONES)
    r = E.predecir(pq)
    sim = r.analogas[0]["similitud"] if r.analogas else None
    obs = _observada(d, ops)
    out = {
        "id": q["id"],
        "enunciado": q["enunciado"],
        "opciones": ops,
        "politica": q["politica"],
        "mes": q["mes"],
        "similitud_max": _r(sim) if sim is not None else None,
        "observado": {
            "p": [_r(x) for x in obs["p"]],
            "ic95": [[_r(a), _r(b)] for a, b in obs["ic95"]],
            "n": obs["n"],
            "n_efectivo": round(obs["n_efectivo"]),
        },
    }
    llm = _llm_en_cache(q, escala) if (sim is None or sim < A.UMBRAL) else None
    if llm is None and not r.analogas:
        out["metodo"] = "sin predicción: ninguna pregunta anterior alineable y sin LLM en caché"
        return out
    if llm is not None:
        out["metodo"] = "llm_anclado"
        out["justificacion_llm"] = llm["justificacion"]
        pred_total = np.asarray(llm["dist"]["total"])
        pred_sub = {k: np.asarray(v) for k, v in llm["dist"].items() if k != "total"}
        intervalos = None
        confianza = (S.calibracion_llm() or {}).get("acierto")
        conf_sub = {}
    else:
        js = S.construir(r, "validacion")
        out["metodo"] = "analogas"
        pred_total = np.array([js["medicion_cis"][o]["p"] for o in ops])
        intervalos = js["medicion_cis"]
        pred_sub = {k: np.array([v[o]["p"] for o in ops]) for k, v in js["por_subgrupo"].items()}
        confianza = js["confianza"]["total"]
        conf_sub = js["confianza"]["por_subgrupo"]
    out["previsto"] = {
        "p": [_r(x) for x in pred_total],
        "ic80": [[_r(x) for x in intervalos[o]["ic80"]] for o in ops] if intervalos else None,
        "ic95": [[_r(x) for x in intervalos[o]["ic95"]] for o in ops] if intervalos else None,
        "confianza": _r(confianza, 3) if confianza is not None else None,
    }
    out["tvd"] = _r(V.tvd(pred_total, obs["p"]))
    out["dentro_margen"] = [
        bool(a - 1e-9 <= x <= b + 1e-9) for x, (a, b) in zip(pred_total, obs["ic95"], strict=True)
    ]
    out["analogas"] = [
        {
            "id": a["id"],
            "estudio": a["estudio"],
            "fecha": str(a["fecha"])[:7],
            "enunciado": a["enunciado"],
            "similitud": _r(a["similitud"], 3),
            "peso": _r(a.get("peso_analoga", 0.0), 4),
        }
        for a in r.analogas[:6]
    ]
    # grupos: previsto frente a observado en las dimensiones que tienen ambos
    grupos, obs_sub, pesos_obs, nef_obs = [], {}, {}, {}
    tot_w = float(d["peso"].sum())
    for dim in DIMENSIONES:
        if dim not in d.columns:
            continue
        for (lv,), dg in sorted(d.group_by(dim), key=lambda x: str(x[0][0])):
            if lv is None or str(lv) in IM.NO_SUSTANTIVOS:
                continue
            k = f"{dim}={lv}"
            og = _observada(dg, ops)
            obs_sub[k], pesos_obs[k], nef_obs[k] = (
                og["p"],
                float(dg["peso"].sum()) / tot_w,
                og["n_efectivo"],
            )
            if dg.height < MIN_GRUPO or k not in pred_sub:
                continue
            pg = pred_sub[k]
            grupos.append(
                {
                    "dimension": dim,
                    "nivel": str(lv),
                    "n": dg.height,
                    "previsto": [_r(x) for x in pg],
                    "observado": [_r(x) for x in og["p"]],
                    "ic95_observado": [[_r(a), _r(b)] for a, b in og["ic95"]],
                    "tvd": _r(V.tvd(pg, og["p"])),
                    "confianza": _r(conf_sub[k], 3) if k in conf_sub else None,
                }
            )
    out["grupos"] = grupos
    dims_pred = sorted({k.split("=", 1)[0] for k in pred_sub} & set(DIMENSIONES))
    out["importancia"] = {
        "prevista": IM.importancia(pred_sub, pesos_marco, pred_total, ops, dimensiones=dims_pred),
        "observada": IM.importancia(
            obs_sub, pesos_obs, obs["p"], ops, n_efectivo=nef_obs, dimensiones=dims_pred
        ),
    }
    return out


def _f11_oficial() -> dict | None:
    """Resultado oficial de la evaluación final (F11), ejecutada una sola vez con el código
    congelado antes de corregir las escalas (D-089): se enseña junto al del sistema corregido."""
    f = REPORTS_DIR / "fase_11_evaluacion.json"
    if not f.exists():
        return None
    d = json.loads(f.read_text("utf-8"))
    return {
        "estudio": next(iter(d["estudios"])),
        "tvd_media": d["todas"]["sistema_final"],
        "preguntas": d["todas"]["preguntas"],
        "etiqueta": d["git"]["tag"],
    }


def ejecutar() -> dict:
    estudios = V.VALIDACION | V.EVALUACION_FINAL
    pesos_marco = IM.pesos_marco(P.marco(), DIMENSIONES, "peso_cis")
    bloques = []
    for estudio, fecha in estudios.items():
        p, lg, banco = V._cargar(estudio, fecha)
        qs = []
        for q in V.preguntas(banco, estudio, fecha):
            x = pregunta(q, p, lg, pesos_marco)
            if x is not None:
                qs.append(x)
        esp = p.filter(
            (pl.col("edad") >= 18)
            & (
                pl.col("nacionalidad_esp_ext").is_null()
                | (pl.col("nacionalidad_esp_ext") == "espanola")
            )
        )
        bloques.append(
            {
                "estudio": estudio,
                "fecha": fecha[:7],
                "uso": "evaluación final (F11)"
                if estudio in V.EVALUACION_FINAL
                else "validación (F9-F10)",
                "encuestados": esp.height,
                "fuentes": _fuentes_estudio(estudio),
                "preguntas": qs,
            }
        )
    res = {
        "generado": dt.date.today().isoformat(),
        "corte_datos": "2026-06",
        "metodo": (
            "Predicción sin ver la encuesta: preguntas parecidas del banco del CIS anteriores a la "
            "fecha (y LLM anclado cuando no las hay), sobre la población sintética nacional. "
            "Observado: respuestas ponderadas de los españoles de 18 años o más del estudio."
        ),
        "dimensiones": DIMENSIONES,
        "escalas": (
            "Escalas 1-10 con solo los extremos etiquetados completadas en el banco (D-089), "
            "después de la evaluación final"
        ),
        "f11_oficial": _f11_oficial(),
        "estudios": bloques,
    }
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(json.dumps(res, ensure_ascii=False, separators=(",", ":")), "utf-8")
    return res


if __name__ == "__main__":
    r = ejecutar()
    for b in r["estudios"]:
        e = [q["tvd"] for q in b["preguntas"] if "tvd" in q]
        print(
            b["estudio"],
            b["fecha"],
            len(b["preguntas"]),
            "preguntas; TVD media",
            round(float(np.mean(e)), 3),
        )
