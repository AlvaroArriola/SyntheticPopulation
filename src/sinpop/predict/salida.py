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

from sinpop import PROCESSED_DIR, REPORTS_DIR
from sinpop import paquete as PK
from sinpop.predict import estimador as E

PREDICCIONES_DIR = REPORTS_DIR / "fase_09" / "predicciones"
AVISO = (
    "Resultado simulado con una población sintética (docs/08): describe distribuciones de grupo, "
    "no a personas reales, y no sustituye a una encuesta."
)

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


def _confianza_provisional(r: E.Resultado) -> float:
    """Si no hay modelo de F10: la similitud de la mejor análoga, rebajada por el desacuerdo."""
    if not r.analogas:
        return 0.0
    desacuerdo = float(np.mean(r.sistema_sd["total"])) * 10
    return float(np.clip(r.analogas[0]["similitud"] * (1 - desacuerdo), 0, 1))


def confianza(r: E.Resultado) -> dict:
    """Probabilidad de que el error (TVD) sea ≤ 0,10, del modelo de confianza de F10 (D-070), por
    clave; si el modelo no está construido, la provisional de F9 para todas."""
    import polars as pl

    from sinpop.confidence import modelo as M
    from sinpop.confidence.senales import senales

    claves = [k for k in r.sistema if k in r.sistema_cis]
    d = M.confianza_final(pl.DataFrame([senales(r, k) | {"clave": k} for k in claves]))
    if d is None:
        c = _confianza_provisional(r)
        return {
            "total": c,
            "por_subgrupo": {k: c for k in r.sistema if k != "total"},
            "metodo": "provisional: similitud con el banco y desacuerdo entre análogas",
        }
    v = dict(zip(d["clave"], d["confianza"].round(4).to_list(), strict=True))
    err = float(d.filter(pl.col("clave") == "total")["error_predicho"][0])
    return {
        "total": v["total"],
        "por_subgrupo": {k: v.get(k, v["total"]) for k in r.sistema if k != "total"},
        "error_tvd_predicho": round(err, 4),
        "metodo": (
            f"P(TVD ≤ {M.UMBRAL_TVD}) según el modelo de confianza (F10, D-070), "
            "recalibrado en la ventana de validación"
            if M.recalibrador() is not None
            else f"P(TVD ≤ {M.UMBRAL_TVD}) según el modelo de confianza (F10, D-070)"
        ),
    }


def construir(r: E.Resultado, run_id: str) -> dict:
    q, cal = r.pregunta, E.calibracion()
    if not r.analogas:
        raise ValueError(f"{q.id}: sin preguntas parecidas alineables en el banco")
    sim = r.analogas[0]["similitud"]
    out = {
        "id": q.id,
        "run_id": run_id,
        "resultado_simulado": True,
        "aviso": AVISO,
        "total": _dist(q.opciones, r.sistema["total"], r.sistema_sd["total"], cal, sim),
        "medicion_cis": _dist(
            q.opciones, r.sistema_cis["total"], r.sistema_cis_sd["total"], cal, sim
        ),
        "por_subgrupo": {
            k: _dist(q.opciones, v, r.sistema_sd[k], cal, sim)
            for k, v in r.sistema.items()
            if k != "total"
        },
        "confianza": confianza(r),
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
        "evolucion": {
            "puntos": E.serie_temporal(q),
            "hoy": q.fecha_referencia,
            "vida_media_meses": E.VIDA_MEDIA_MESES,
        },
        "retratos": retratos(r, run_id),
    }
    validar(out, q.opciones)
    return out


# ---------------------------------------------------------------- retratos y cruces (D-083)
N_RETRATOS = 24
CAMPOS_RETRATO = [
    "sexo",
    "edad",
    "provincia",
    "ccaa",
    "estudios_3",
    "actividad_3",
    "tamano_municipio_cis",
    "religiosidad",
    "clase_subjetiva",
    "ideologia_bloque",
    "recuerdo_voto_generales_familia",
]


def retratos(r: E.Resultado, run_id: str, n: int = N_RETRATOS) -> list[dict]:
    """Personas sintéticas concretas, elegidas al azar (con su peso) con una semilla fija por
    pregunta, con su perfil y la probabilidad de cada respuesta para alguien con ese perfil."""
    import hashlib

    from sinpop.predict import poblacion as P

    if r.personas is None:
        return []
    try:
        m = P.marco(run_id)
    except FileNotFoundError:  # evaluación con un identificador sin población (F9, F11)
        return []
    w = m["peso"].to_numpy()
    semilla = int(hashlib.sha256(f"{r.pregunta.id}|{run_id}".encode()).hexdigest()[:8], 16)
    idx = np.random.default_rng(semilla).choice(
        m.height, size=min(n, m.height), replace=False, p=w / w.sum()
    )
    cols = [c for c in CAMPOS_RETRATO if c in m.columns]
    filas = m.select("person_id", *cols)[idx.tolist()].to_dicts()
    return [
        f
        | {
            "probabilidades": {
                o: round(float(p), 4)
                for o, p in zip(r.pregunta.opciones, r.personas[i], strict=True)
            }
        }
        for f, i in zip(filas, idx, strict=True)
    ]


def _llevar_tabla(t: np.ndarray, a: dict, b: dict, qa: E.Pregunta, qb: E.Pregunta) -> np.ndarray:
    """Tabla observada (opciones propias de las análogas) → opciones de las preguntas."""
    propias_a = list(E._b0_paquete()[a["id"]]["n_opcion"])
    propias_b = list(E._b0_paquete()[b["id"]]["n_opcion"])
    out = np.zeros((len(qa.opciones), len(qb.opciones)))
    for i, oa in enumerate(propias_a):
        for j, ob in enumerate(propias_b):
            if oa in a["mapeo"] and ob in b["mapeo"]:
                out[qa.opciones.index(a["mapeo"][oa]), qb.opciones.index(b["mapeo"][ob])] += t[i, j]
    return out / out.sum() if out.sum() > 0 else out


def _ipf(t: np.ndarray, filas: np.ndarray, cols: np.ndarray, vueltas: int = 200) -> np.ndarray:
    """Ajuste proporcional iterativo: conserva la asociación (razones de odds) de `t` y le pone
    los márgenes `filas` y `cols`."""
    x = t.copy() + 1e-9
    for _ in range(vueltas):
        x *= (filas / x.sum(1))[:, None]
        x *= (cols / x.sum(0))[None, :]
    return x / x.sum()


def _v_cramer(t: np.ndarray) -> float:
    ta, tb = t.sum(1), t.sum(0)
    indep = np.outer(ta, tb)
    chi = (((t - indep) ** 2) / np.where(indep > 0, indep, 1)).sum()
    return float(np.sqrt(chi / max(min(len(ta), len(tb)) - 1, 1)))


def cruce(qa: dict, qb: dict, run_id: str) -> dict:
    """Distribución conjunta de dos preguntas en la población (D-083).

    - **Márgenes:** las predicciones de cada pregunta para la población.
    - **Relación entre las dos:** la observada en el estudio del CIS más reciente y parecido que
      hizo las dos (tabla cruzada agregada), ajustada a esos márgenes con IPF, que conserva la
      asociación. Si ningún estudio las hizo juntas, la que pasa por el perfil de las personas
      (a igual perfil se suponen independientes), que subestima la asociación; se dice cuál es."""
    from sinpop.predict import opciones as O
    from sinpop.predict import poblacion as P

    m = P.marco(run_id)
    w = m["peso"].to_numpy()
    preg, res = [], []
    for q in (qa, qb):
        p = E.Pregunta(
            q["id"],
            q["enunciado"],
            q["opciones"],
            q.get("escala") or O.escala_probable(q["opciones"]),
            q.get("fecha_referencia", "2026-07"),
            [],
        )
        r = E.predecir(p, run_id=run_id)
        if r.personas is None:
            raise ValueError(
                f"«{q['enunciado']}» no tiene preguntas parecidas en el banco: hace falta "
                "el modelo de lenguaje y el cruce no lo usa"
            )
        preg.append(p)
        res.append(r)
    ra, rb = res
    ta = ra.sistema["total"] / ra.sistema["total"].sum()
    tb = rb.sistema["total"] / rb.sistema["total"].sum()
    perfil = (ra.personas * w[:, None]).T @ rb.personas / w.sum()
    mejor = None
    for a in ra.analogas:
        for b in rb.analogas:
            if a["estudio"] != b["estudio"] or a["id"] == b["id"]:
                continue
            t = E.tabla_conjunta(a["id"], b["id"])
            if t is None:
                continue
            puntos = a["peso_analoga"] * b["peso_analoga"]
            if mejor is None or puntos > mejor[0]:
                mejor = (puntos, a, b, t)
    if mejor is not None:
        _, a, b, (n, t) = mejor
        obs = _llevar_tabla(t, a, b, *preg)
        conj = _ipf(obs, ta, tb)
        fuente = {
            "tipo": "observada",
            "estudio": a["estudio"],
            "fecha": str(a["fecha"])[:7],
            "encuestados": n,
            "pregunta_a": a["enunciado"],
            "pregunta_b": b["enunciado"],
            "nota": (
                f"Relación observada entre las dos preguntas en el estudio {a['estudio']} del CIS "
                f"({str(a['fecha'])[:7]}, {n} encuestados), ajustada a las respuestas que se "
                "predicen hoy para la población."
            ),
        }
    else:
        conj = _ipf(perfil, ta, tb)
        fuente = {
            "tipo": "perfil",
            "nota": (
                "Ningún estudio del banco hizo las dos preguntas juntas: la relación es la que "
                "pasa por el perfil de las personas (edad, ideología, religiosidad…). A igual "
                "perfil se suponen independientes, así que la asociación real puede ser mayor."
            ),
        }
    ta2, tb2 = conj.sum(1), conj.sum(0)
    cond = conj / np.where(ta2[:, None] > 0, ta2[:, None], 1)
    return {
        "run_id": run_id,
        "a": {
            "enunciado": qa["enunciado"],
            "opciones": qa["opciones"],
            "total": ta2.round(4).tolist(),
        },
        "b": {
            "enunciado": qb["enunciado"],
            "opciones": qb["opciones"],
            "total": tb2.round(4).tolist(),
        },
        "conjunta": conj.round(5).tolist(),
        "b_segun_a": cond.round(4).tolist(),
        "v_cramer": round(_v_cramer(conj), 3),
        "v_cramer_solo_perfil": round(_v_cramer(perfil), 3),
        "fuente_relacion": fuente,
        "resultado_simulado": True,
        "aviso": AVISO,
    }


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


CALIBRACION_LLM = (
    PK.ruta("calibracion_llm.json")
    if PK.activo()
    else PROCESSED_DIR / "predict" / "calibracion_llm.json"
)


def calibracion_llm() -> dict | None:
    """Error de las preguntas nuevas con LLM medido en la ventana de validación
    (`evaluate/llm.py`): escala conformal de los intervalos y tasa de acierto (TVD ≤ 0,10)."""
    return json.loads(CALIBRACION_LLM.read_text("utf-8")) if CALIBRACION_LLM.exists() else None


def _dist_llm(opciones: list[str], mu: np.ndarray, cal: dict | None) -> dict:
    mu = mu / mu.sum()
    s = np.maximum(np.sqrt(np.clip(mu * (1 - mu), 0, None)), E.S_MIN)
    q80, q95 = (cal["q80"], cal["q95"]) if cal else (np.inf, np.inf)
    return {
        o: {
            "p": round(float(mu[j]), 6),
            "ic80": [
                round(float(max(mu[j] - q80 * s[j], 0)), 6),
                round(float(min(mu[j] + q80 * s[j], 1)), 6),
            ],
            "ic95": [
                round(float(max(mu[j] - q95 * s[j], 0)), 6),
                round(float(min(mu[j] + q95 * s[j], 1)), 6),
            ],
        }
        for j, o in enumerate(opciones)
    }


def construir_asistida(q: E.Pregunta, r: E.Resultado, run_id: str) -> dict:
    """Salida de una pregunta sin análogas fiables, con el LLM anclado en las más parecidas
    (`predict/asistido.py`). Sin calibración en validación, los intervalos son [0, 1] y la
    confianza 0: no se sabe cuánto se equivoca."""
    from sinpop.llm import cliente as C
    from sinpop.predict import asistido as A

    pet = A.peticion_nueva(q)
    salida = C.ejecutar([pet])[pet.id]
    if salida is None:
        raise ValueError(f"{q.id}: el modelo de lenguaje no devolvió una salida válida")
    dist = A.distribuciones(salida)
    cal = calibracion_llm()
    reg = C.registro(pet)
    conf = float(cal["acierto"]) if cal else 0.0
    out = {
        "id": q.id,
        "run_id": run_id,
        "resultado_simulado": True,
        "aviso": AVISO,
        "total": _dist_llm(q.opciones, dist["total"], cal),
        "medicion_cis": _dist_llm(q.opciones, dist["total"], cal),
        "por_subgrupo": {k: _dist_llm(q.opciones, v, cal) for k, v in dist.items() if k != "total"},
        "confianza": {
            "total": conf,
            "por_subgrupo": {k: conf for k in dist if k != "total"},
            "metodo": (
                "tasa de acierto (TVD ≤ 0,10) de las preguntas nuevas con LLM en la ventana de "
                "validación"
                if cal
                else "sin calibrar: aún no se ha medido el error del LLM en validación"
            ),
        },
        "parametros_llm": {
            "uso": "pregunta_nueva",
            "justificacion": salida["justificacion"],
            "similitud_mejor_analoga": round(r.analogas[0]["similitud"], 4) if r.analogas else None,
        },
        "parametros": {"estimador": "llm_anclado", "escala": q.escala},
        "preguntas_similares": [a["id"] for a in r.analogas],
        "coste": {
            "llamadas": reg["llamadas"],
            "tokens": reg["tokens"],
            "eur": reg["eur"],
            "segundos": round(r.segundos, 2),
        },
        "versiones": {"modelo_llm": reg["modelo"], "prompts": reg["prompt"], "poblacion": run_id},
    }
    validar(out, q.opciones)
    return out


def _clave_territorio(t: str) -> str | None:
    """Subgrupo del marco nacional que equivale a un territorio (`ccaa=XX`, `provincia=XX`)."""
    if t == "ES":
        return None
    nivel, cod = t.split(":")
    return f"{'ccaa' if nivel == 'CCAA' else 'provincia'}={cod}"


def ajustar_territorio(out: dict, r: E.Resultado, clave: str) -> dict:
    """D-075: en una población de un territorio, el total es un subgrupo del banco nacional. Su
    incertidumbre y su confianza son las de ese subgrupo (los encuestados del CIS del territorio),
    no las del total nacional."""
    if clave not in out["por_subgrupo"] or clave not in r.sistema_sd:
        return out
    cal, sim = E.calibracion(), r.analogas[0]["similitud"]
    q = r.pregunta
    out["total"] = _dist(q.opciones, r.sistema["total"], r.sistema_sd[clave], cal, sim)
    out["medicion_cis"] = _dist(q.opciones, r.sistema_cis["total"], r.sistema_sd[clave], cal, sim)
    c = out["confianza"]
    c["total"] = c["por_subgrupo"].get(clave, c["total"])
    c["metodo"] += f"; total con los datos del territorio ({clave})"
    out["por_subgrupo"].pop(clave, None)
    c["por_subgrupo"].pop(clave, None)
    return out


def predecir_dict(
    q: dict, run_id: str = "2026-01-01_ES_1000000_s1", permitir_llm: bool = True
) -> dict:
    """Predicción de una pregunta en formato `docs/03` §2.8 (la usan la CLI y el servicio).

    `permitir_llm=False` fuerza el estimador sin modelo de lenguaje (para comparaciones en lote,
    que si no harían una llamada por territorio)."""
    jsonschema.validate(q, ESQUEMA_ENTRADA)
    from sinpop.llm import cliente as C
    from sinpop.predict import asistido as A
    from sinpop.predict import opciones as O
    from sinpop.predict import poblacion as P

    clave = _clave_territorio(P.territorio(run_id))
    subgrupos = list(q.get("subgrupos", list(E.SUBGRUPOS)))
    if clave and clave.split("=")[0] not in subgrupos:
        subgrupos.append(clave.split("=")[0])
    p = E.Pregunta(
        q["id"],
        q["enunciado"],
        q["opciones"],
        q.get("escala") or O.escala_probable(q["opciones"]),
        q.get("fecha_referencia", "2026-07"),
        subgrupos,
    )
    r = E.predecir(p, run_id=run_id)
    sin_analogas = not r.analogas or r.analogas[0]["similitud"] < A.UMBRAL
    cal = calibracion_llm()
    usar = cal is None or cal.get("usar", True)
    if permitir_llm and sin_analogas and C.disponible() and usar:
        try:
            out = construir_asistida(p, r, run_id)
        except Exception as e:  # sin salida válida del LLM: estimador sin él, con aviso (D-085)
            fallo = f"{type(e).__name__}: {e}"
        else:
            # en una población de comunidad, el total es el subgrupo de esa comunidad
            if clave in out["por_subgrupo"]:
                out["total"] = out["medicion_cis"] = out["por_subgrupo"].pop(clave)
                out["confianza"]["por_subgrupo"].pop(clave, None)
            if clave:
                out["territorio"] = P.territorio(run_id)
            validar(out, q["opciones"])
            return out
    else:
        fallo = None
    out = construir(r, run_id)
    if fallo:
        out["aviso"] += (
            " El modelo de lenguaje no dio una respuesta válida; se muestra la estimación sin él."
        )
        out["parametros"]["llm_fallo"] = fallo[:300]
    if clave:
        out = ajustar_territorio(out, r, clave)
        out["territorio"] = P.territorio(run_id)
        validar(out, q["opciones"])
    return out


def predecir_fichero(entrada: Path, run_id: str = "2026-01-01_ES_1000000_s1") -> Path:
    """Lee `preguntas/<id>.json`, predice y escribe `predicciones/<id>_<run_id>.json`."""
    q = json.loads(entrada.read_text("utf-8"))
    out = predecir_dict(q, run_id)
    PREDICCIONES_DIR.mkdir(parents=True, exist_ok=True)
    destino = PREDICCIONES_DIR / f"{q['id']}_{run_id}.json"
    destino.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    return destino
