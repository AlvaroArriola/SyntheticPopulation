"""Asistente de tamaño de la población (D-079).

Quien usa la interfaz elige cuántas personas generar. El tamaño solo controla una parte del error,
el **de simulación** (cuántas personas sintéticas caen en cada grupo). La otra parte, la que pesa
de verdad en la confianza, sale de cuántos **encuestados del CIS** hay de ese territorio: ningún
tamaño de población la compensa. El asistente calcula las dos cosas:

- margen de simulación del 95 % en el peor caso (p = 0,5) para el grupo más pequeño del detalle
  pedido: 1,96·√(0,25 / (N·cuota)). Para las predicciones, N es como mucho la muestra de
  `predict.poblacion.TAMANO` (100 000) que usa el estimador; para los datos de la población, la
  población entera;
- mediana de encuestados del CIS de ese territorio por pregunta del banco (recuentos agregados del
  paquete, `n_sub`).
"""

from __future__ import annotations

import gzip
import json
import statistics
from functools import cache

import numpy as np
import polars as pl

from sinpop import paquete as PK

Z95 = 1.96
DETALLES = {
    "total": [],
    "grupos": ["edad_4", "sexo", "estudios_3"],
    "voto": ["recuerdo_voto_generales_familia"],
}
CUOTA_MINIMA = 0.01  # los grupos por debajo del 1 % no se usan como referencia


@cache
def _encuestados() -> dict[str, float]:
    from sinpop.paquete.exportar import DESTINO

    ruta = PK.ruta("modelos.jsonl.gz") if PK.activo() else DESTINO / "modelos.jsonl.gz"
    if not ruta.exists():
        return {}
    por: dict[str, list[int]] = {"ES": []}
    with gzip.open(ruta, "rt", encoding="utf-8") as f:
        for x in map(json.loads, f):
            por["ES"].append(x["n"])
            for k, v in x["n_sub"].items():
                if k.startswith(("ccaa=", "provincia=")):
                    por.setdefault(k, []).append(v)
    return {k: float(statistics.median(v)) for k, v in por.items()}


def encuestados(territorio: str) -> float | None:
    clave = "ES"
    if territorio.startswith("CCAA:"):
        clave = f"ccaa={territorio[5:]}"
    elif territorio.startswith("PROV:"):
        clave = f"provincia={territorio[5:]}"
    return _encuestados().get(clave)


def _cuota_minima(territorio: str, detalle: str) -> float:
    from sinpop.predict import poblacion as P

    m = P.marco(P.NACIONAL)
    if territorio.startswith("CCAA:"):
        m = m.filter(pl.col("ccaa") == territorio[5:])
    elif territorio.startswith("PROV:"):
        m = m.filter(pl.col("provincia") == territorio[5:])
    cuotas = [1.0]
    for g in DETALLES[detalle]:
        t = m.group_by(g).agg(pl.col("peso").sum())
        s = t["peso"] / t["peso"].sum()
        cuotas += [float(x) for x in s if x >= CUOTA_MINIMA]
    return min(cuotas)


def _margen(n: float, cuota: float) -> float:
    return float(Z95 * np.sqrt(0.25 / max(n * cuota, 1.0)))


def recomendar(territorio: str, margen: float, detalle: str, tamanos: list[int]) -> dict:
    from sinpop.predict.poblacion import TAMANO

    cuota = _cuota_minima(territorio, detalle)
    filas = [
        {
            "tamano": t,
            "margen_prediccion": round(_margen(min(t, TAMANO), cuota), 4),
            "margen_datos": round(_margen(t, cuota), 4),
        }
        for t in tamanos
    ]
    validos = [f["tamano"] for f in filas if f["margen_prediccion"] <= margen]
    rec = validos[0] if validos else min((t for t in tamanos if t >= TAMANO), default=tamanos[-1])
    n_cis = encuestados(territorio)
    if n_cis is None:
        techo = None
    elif n_cis >= 300:
        techo = "alta"
    elif n_cis >= 50:
        techo = "media"
    else:
        techo = "baja"
    return {
        "territorio": territorio,
        "detalle": detalle,
        "margen_objetivo": margen,
        "cuota_grupo_mas_pequeno": round(cuota, 4),
        "tamanos": filas,
        "recomendado": rec,
        "alcanzable": bool(validos),
        "muestra_prediccion": TAMANO,
        "encuestados_cis_mediana": n_cis,
        "techo_confianza": techo,
    }
