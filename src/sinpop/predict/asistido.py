"""Predicciones asistidas por un modelo de lenguaje (F9; D-071).

Tres usos, cada uno solo donde el componente estadístico no llega o como referencia:

- **B2** (`peticion_b2`): el baseline de `docs/04` (F9, tarea 7). El LLM ve la pregunta y la
  composición de la población, sin preguntas del banco.
- **Pregunta nueva** (`peticion_nueva`): para preguntas sin análogas fiables (similitud < `UMBRAL`
  o ninguna alineable). El LLM ve además las preguntas más parecidas con sus resultados.
- **Evento** (`peticion_evento`): el LLM propone el cambio por categoría de un indicador.

A los modelos solo les llegan enunciados públicos, la composición agregada de la población
sintética y resultados ponderados agregados del CIS (regla 8).
"""

from __future__ import annotations

from functools import cache

import numpy as np
import polars as pl

from sinpop.llm.cliente import Peticion
from sinpop.predict import estimador as E

UMBRAL = 0.4  # similitud de la mejor análoga por debajo de la cual se usa el LLM (D-069)
SUBGRUPOS_LLM = ["edad_4", "sexo", "estudios_3", "ccaa"]
ETIQUETAS = {
    "edad_4": "edad",
    "sexo": "sexo",
    "estudios_3": "estudios",
    "ccaa": "comunidad autónoma",
}

ESQUEMA_DIST = {
    "type": "object",
    "properties": {
        "total": {"type": "array", "items": {"type": "number"}},
        "subgrupos": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "clave": {"type": "string"},
                    "distribucion": {"type": "array", "items": {"type": "number"}},
                },
                "required": ["clave", "distribucion"],
                "additionalProperties": False,
            },
        },
        "justificacion": {"type": "string"},
    },
    "required": ["total", "subgrupos", "justificacion"],
    "additionalProperties": False,
}

ESQUEMA_EVENTO = {
    "type": "object",
    "properties": {
        "categorias": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "categoria": {"type": "string"},
                    "cambio_pp": {"type": "number"},
                },
                "required": ["categoria", "cambio_pp"],
                "additionalProperties": False,
            },
        },
        "justificacion": {"type": "string"},
    },
    "required": ["categorias", "justificacion"],
    "additionalProperties": False,
}


@cache
def _nombres_ccaa() -> dict[str, str]:
    from sinpop.config import load_config

    return {c.codigo: c.nombre for c in load_config("territories.yaml").ccaa}  # type: ignore[attr-defined]


def _nombre(g: str, v: str) -> str:
    if g == "ccaa":
        return _nombres_ccaa().get(v, v)
    return v.replace("_", " ")


def claves_subgrupo(m: pl.DataFrame | None = None) -> list[str]:
    from sinpop.predict import poblacion as P

    m = P.marco() if m is None else m
    return [f"{g}={v}" for g in SUBGRUPOS_LLM for v in sorted(m[g].drop_nulls().unique())]


@cache
def poblacion_texto() -> str:
    """Composición de los españoles de 18+ de la población sintética (pesos `peso_es`)."""
    from sinpop.predict import poblacion as P

    m = P.marco().filter(pl.col("peso_es") > 0)
    lineas = []
    for g in SUBGRUPOS_LLM:
        t = m.group_by(g).agg(pl.col("peso_es").sum()).sort(g)
        tot = t["peso_es"].sum()
        partes = [f"{_nombre(g, v)} {100 * w / tot:.1f} %" for v, w in t.iter_rows()]
        lineas.append(f"- {ETIQUETAS[g]}: " + "; ".join(partes))
    return "\n".join(lineas)


def _lista_subgrupos(claves: list[str]) -> str:
    return "\n".join(
        f"- {k} ({ETIQUETAS[k.split('=')[0]]}: {_nombre(*k.split('=', 1))})" for k in claves
    )


def _opciones(opciones: list[str]) -> str:
    return "\n".join(f"{i + 1}. {o}" for i, o in enumerate(opciones))


def spec_distribucion(n: int, claves: list[str]) -> dict:
    return {"tipo": "distribucion", "n": n, "claves": list(claves)}


def distribuciones(salida: dict) -> dict[str, np.ndarray]:
    """Salida validada → {clave: distribución normalizada}."""
    out = {"total": np.asarray(salida["total"], float)}
    out |= {x["clave"]: np.asarray(x["distribucion"], float) for x in salida["subgrupos"]}
    return {k: v / v.sum() for k, v in out.items()}


def peticion_b2(q: E.Pregunta, claves: list[str] | None = None) -> Peticion:
    claves = claves_subgrupo() if claves is None else claves
    return Peticion(
        id=f"b2:{q.id}",
        tarea="b2",
        variables={
            "mes": q.fecha_referencia,
            "enunciado": q.enunciado,
            "opciones": _opciones(q.opciones),
            "n_opciones": str(len(q.opciones)),
            "poblacion": poblacion_texto(),
            "subgrupos": _lista_subgrupos(claves),
        },
        esquema=ESQUEMA_DIST,
        spec=spec_distribucion(len(q.opciones), claves),
    )


def parecidas_texto(q: E.Pregunta, k: int = 5) -> str:
    """Las `k` preguntas más parecidas del banco anteriores a la de referencia, con su resultado
    ponderado del CIS (agregado)."""
    from sinpop.predict import recuperar as R

    cand = R.indice().similares(
        q.enunciado, q.opciones, k, pl.col("fecha") >= f"{q.fecha_referencia}-01"
    )
    filas = []
    for a in cand.iter_rows(named=True):
        d = E.encuestados(a["estudio"], a["variable"], {o: o for o in a["opciones"]})
        if d.height < 50:
            continue
        p = E._observada(d, a["opciones"])
        dist = "; ".join(f"{o} {100 * x:.0f} %" for o, x in zip(a["opciones"], p, strict=True))
        filas.append(
            f"- ({a['fecha'][:7]}, similitud {a['similitud']:.2f}) {a['enunciado']}: {dist}"
        )
    return "\n".join(filas) or "(ninguna)"


def peticion_nueva(q: E.Pregunta, claves: list[str] | None = None) -> Peticion:
    claves = claves_subgrupo() if claves is None else claves
    p = peticion_b2(q, claves)
    return Peticion(
        id=f"nueva:{q.id}",
        tarea="pregunta_nueva",
        variables=p.variables | {"parecidas": parecidas_texto(q)},
        esquema=ESQUEMA_DIST,
        spec=p.spec,
    )


def peticion_evento(
    id_: str,
    fecha: str,
    descripcion: str,
    ambito: str,
    indicador: str,
    antes: dict[str, float],
    analogos: str,
) -> Peticion:
    cats = sorted(antes)
    return Peticion(
        id=f"evento:{id_}:{indicador}",
        tarea="evento",
        variables={
            "fecha": fecha,
            "descripcion": descripcion,
            "ambito": ambito,
            "indicador": indicador,
            "categorias": "\n".join(f"- {c}" for c in cats),
            "antes": "\n".join(f"- {c}: {antes[c]:.3f}" for c in cats),
            "analogos": analogos or "(ninguno)",
        },
        esquema=ESQUEMA_EVENTO,
        spec={"tipo": "evento", "categorias": cats},
    )
