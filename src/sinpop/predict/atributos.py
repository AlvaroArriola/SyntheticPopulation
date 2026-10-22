"""Datos de la población que se responden directamente (D-077).

Algunas preguntas no necesitan el banco del CIS: la población sintética ya lleva el atributo,
calibrado o emparejado con una fuente oficial (salud autopercibida de la ECV, uso de internet de
la TIC-H, situación laboral del Censo y la EPA…). Para ellas basta con tabular la población
ponderada.

- `catalogo()`: los atributos de `configs/atributos.yaml`, con la descripción, las categorías y
  las fuentes de `configs/variables.yaml` y `configs/sources.yaml`.
- `buscar(enunciado, opciones)`: atributos parecidos a la pregunta (mismo TF-IDF que el banco).
- `distribucion(variable, run_id)`: distribución ponderada entre los adultos del universo, total y
  por subgrupos, con el margen de simulación y la procedencia de los valores (`__calidad`).

El margen es solo el de la simulación (cuántas personas sintéticas hay). El error de la propia
fuente oficial y el del emparejamiento no están en él; los mide la validación de F6 y F7.
"""

from __future__ import annotations

import json
from functools import cache

import numpy as np
import polars as pl
import yaml

from sinpop import CONFIGS_DIR, POPULATIONS_DIR
from sinpop import paquete as PK

SUBGRUPOS = ["edad_4", "sexo", "estudios_3", "ccaa"]
UMBRAL = 0.18  # similitud mínima para proponer un atributo
Z95 = 1.96


@cache
def catalogo() -> dict[str, dict]:
    cfg = yaml.safe_load((CONFIGS_DIR / "atributos.yaml").read_text("utf-8"))["atributos"]
    var = yaml.safe_load((CONFIGS_DIR / "variables.yaml").read_text("utf-8"))["variables"]
    src = {
        f["id"]: f
        for f in yaml.safe_load((CONFIGS_DIR / "sources.yaml").read_text("utf-8"))["fuentes"]
    }
    out = {}
    for v, c in cfg.items():
        d = var[v]
        cats = [str(x) for x in d["categorias"]]
        if "NC" in c["etiquetas"]:
            cats.append("NC")
        fuentes = [
            {
                "id": k,
                "nombre": src[k]["nombre"] if k in src else k,
                "organismo": src[k]["organismo"] if k in src else None,
                "variable_original": f.get("variable_original"),
            }
            for k, f in (d.get("fuentes") or {}).items()
        ]
        out[v] = {
            "variable": v,
            "descripcion": d["descripcion"],
            "categorias": cats,
            "etiquetas": {str(k): val for k, val in c["etiquetas"].items()},
            "universo": c.get("universo", "personas de 18 años o más"),
            "fuente_principal": d.get("fuente_principal"),
            "fuentes": fuentes,
            "busqueda": c.get("busqueda", []),
        }
    return out


@cache
def indice():
    from sinpop.predict.recuperar import Indice

    filas = [
        {
            "id": v,
            "enunciado": f"{c['descripcion']}. " + ". ".join(c["busqueda"]),
            "opciones": [e for k, e in c["etiquetas"].items() if k != "NC"],
        }
        for v, c in catalogo().items()
    ]
    return Indice(pl.DataFrame(filas))


def buscar(enunciado: str, opciones: list[str] | None = None, k: int = 3) -> list[dict]:
    d = indice().similares(enunciado, opciones or [], k=k)
    return [
        {
            "variable": r["id"],
            "descripcion": catalogo()[r["id"]]["descripcion"],
            "universo": catalogo()[r["id"]]["universo"],
            "fuente_principal": catalogo()[r["id"]]["fuente_principal"],
            "similitud": round(float(r["similitud"]), 3),
        }
        for r in d.iter_rows(named=True)
        if r["similitud"] >= UMBRAL
    ]


def _tabla(d: pl.DataFrame, v: str, cats: list[str]) -> dict:
    t = dict(d.group_by(v).agg(pl.col("peso").sum()).iter_rows())
    tot = sum(t.values()) or 1.0
    return {c: t.get(c, 0.0) / tot for c in cats}


def _con_margen(d: pl.DataFrame, v: str, cats: list[str]) -> dict:
    """Proporciones ponderadas con el margen de simulación del 95 % (tamaño efectivo de Kish)."""
    w = d["peso"].to_numpy()
    n_ef = float(w.sum() ** 2 / (w**2).sum()) if len(w) else 0.0
    out = {}
    for cat, p in _tabla(d, v, cats).items():
        m = Z95 * np.sqrt(p * (1 - p) / n_ef) if n_ef else 0.0
        out[cat] = {"p": round(p, 6), "ic95": [round(max(p - m, 0), 6), round(min(p + m, 1), 6)]}
    return out


def calcular(variable: str, persons: pl.DataFrame) -> dict:
    """Distribución ponderada de un atributo entre los adultos de su universo."""
    c = catalogo()[variable]
    cats = c["categorias"]
    adultos = persons.filter(pl.col("es_adulto"))
    d = adultos.filter(pl.col(variable).is_not_null() & (pl.col(variable) != "NP"))
    w = d["peso"].to_numpy()
    por = {}
    for g in SUBGRUPOS:
        if g == variable or g not in d.columns:
            continue
        for lv in d[g].drop_nulls().unique().sort().to_list():
            if lv != "NP":
                por[f"{g}={lv}"] = _con_margen(d.filter(pl.col(g) == lv), variable, cats)
    calidad = {}
    if f"{variable}__calidad" in d.columns:
        cal = d[f"{variable}__calidad"].unique().to_list()
        calidad = {k: round(x, 4) for k, x in _tabla(d, f"{variable}__calidad", cal).items()}
    return {
        "variable": variable,
        "descripcion": c["descripcion"],
        "universo": c["universo"],
        "cuota_universo": round(float(d["peso"].sum() / adultos["peso"].sum()), 4),
        "personas_universo": d.height,
        "n_efectivo": round(float(w.sum() ** 2 / (w**2).sum())) if len(w) else 0,
        "categorias": cats,
        "etiquetas": c["etiquetas"],
        "total": _con_margen(d, variable, cats),
        "por_subgrupo": por,
        "procedencia": calidad,
        "fuente_principal": c["fuente_principal"],
        "fuentes": c["fuentes"],
    }


def todas(run_id: str) -> dict[str, dict]:
    columnas = ["es_adulto", "peso", *SUBGRUPOS]
    for v in catalogo():
        columnas += [v, f"{v}__calidad"]
    ruta = POPULATIONS_DIR / run_id / "persons.parquet"
    disp = set(pl.read_parquet_schema(ruta))
    p = pl.read_parquet(ruta, columns=[x for x in dict.fromkeys(columnas) if x in disp])
    return {v: calcular(v, p) for v in catalogo() if v in disp}


def distribucion(variable: str, run_id: str) -> dict:
    if PK.activo():  # paquete portable (D-076): ya calculadas
        d = json.loads(PK.ruta("atributos", f"{run_id}.json").read_text("utf-8"))
        return d[variable]
    return _todas_cache(run_id)[variable]


@cache
def _todas_cache(run_id: str) -> dict[str, dict]:
    return todas(run_id)
