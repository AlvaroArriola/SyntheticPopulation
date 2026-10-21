"""*Backtest* histórico para el modelo de confianza (F10, tarea 1) (D-070).

Cada pregunta cerrada de los estudios nacionales del CIS con campo entre `DESDE` y el corte se
oculta y se predice con el componente estadístico (`predict.estimador`), con un banco limitado a
los estudios **anteriores** a su fecha. Se mide el error (TVD de la medición CIS) en total y en
cada subgrupo (edad en cuatro grupos, sexo, estudios, comunidad) con al menos `MIN_CASOS`
encuestados, junto con las señales de `03_arquitectura.md` §2.7 (`senales`).

La sensibilidad a reformulaciones no se usa como señal: en F9 fue prácticamente nula (TVD máxima
0,003), así que no discrimina.
"""

from __future__ import annotations

import numpy as np
import polars as pl

from sinpop import REPORTS_DIR
from sinpop.confidence.senales import senales
from sinpop.predict import banco as B
from sinpop.predict import estimador as E
from sinpop.predict import opciones as O

DESDE = "2025-07-01"
MIN_CASOS = 50
SUBGRUPOS = ["edad_4", "sexo", "estudios_3", "ccaa"]
DESTINO = REPORTS_DIR / "fase_10" / "backtest_confianza.csv"


def _dist(d: pl.DataFrame, opciones: list[str]) -> np.ndarray:
    t = dict(d.group_by("valor").agg(pl.col("peso").sum()).iter_rows())
    v = np.array([t.get(o, 0.0) for o in opciones])
    return v / v.sum() if v.sum() > 0 else v


def filas_pregunta(r: E.Resultado, verdad: pl.DataFrame, grupos: list[str]) -> list[dict]:
    """Error y señales del total y de cada subgrupo con datos suficientes."""
    q = r.pregunta
    out = []
    base = senales(r)
    y = _dist(verdad, q.opciones)
    out.append(
        base
        | {
            "id": q.id,
            "clave": "total",
            "grupo": "total",
            "n_verdad": verdad.height,
            "tvd": float(0.5 * np.abs(r.sistema_cis["total"] - y).sum()),
        }
    )
    for g in grupos:
        for (lv,), dg in verdad.group_by(g):
            k = f"{g}={lv}"
            if dg.height < MIN_CASOS or k not in r.sistema_cis:
                continue
            yg = _dist(dg, q.opciones)
            out.append(
                senales(r, k)
                | {
                    "id": q.id,
                    "clave": k,
                    "grupo": g,
                    "n_verdad": dg.height,
                    "tvd": float(0.5 * np.abs(r.sistema_cis[k] - yg).sum()),
                }
            )
    return out


def ejecutar(desde: str = DESDE, hasta: str = "2026-07-01", paso: int = 1) -> pl.DataFrame:
    obj = B.preguntas().filter((pl.col("fecha") >= desde) & (pl.col("fecha") < hasta))
    obj = obj.sort("id").gather_every(paso)
    filas = []
    for row in obj.iter_rows(named=True):
        q = E.Pregunta(
            row["id"],
            row["enunciado"],
            row["opciones"],
            O.escala_probable(row["opciones"]),
            row["fecha"][:7],
            SUBGRUPOS,
        )
        r = E.predecir(q, excluir=pl.col("fecha") >= row["fecha"])
        if not r.analogas:
            continue
        m = {o: o for o in row["opciones"]}
        v = E.encuestados(row["estudio"], row["variable"], m)
        if v.height < 200:
            continue
        filas += filas_pregunta(r, v, SUBGRUPOS)
    d = pl.DataFrame(filas)
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    d.write_csv(DESTINO)
    return d
