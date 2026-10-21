"""Banco de efectos de eventos (F8C, tareas 3 y 4; docs/03 §2.6) (D-068).

Para cada evento de `configs/eventos.yaml` y cada indicador de `configs/temporal.yaml`, el cambio
en la proporción de cada categoría entre los barómetros de **antes** y de **después**, por grupo
(nacional, edad en cuatro grupos y grupo de voto de 2023; en un evento autonómico, dentro de su
comunidad):

- antes: los `VENTANA` meses con barómetro anteriores al mes del evento (incluido ese mes si el
  evento es del día 20 en adelante: el campo del barómetro es en la primera quincena);
- después: los `VENTANA` meses con barómetro posteriores al mes del evento;
- efecto = proporción después − antes (ponderadas), con su intervalo del 95 % por la varianza
  muestral de cada lado (tamaño efectivo de Kish).

Es el cambio **observado** en torno al evento: incluye la tendencia que ya hubiera y cualquier
otra cosa que pasara a la vez. La capa de predicción lo usa por analogía, no como efecto causal.
"""

from __future__ import annotations

import datetime as dt

import numpy as np
import polars as pl

from sinpop import PROCESSED_DIR, REPORTS_DIR
from sinpop.config import load_config
from sinpop.temporal import indicadores as T

VENTANA = 2
DIA_CORTE = 20
MIN_CASOS = 100  # encuestados mínimos por lado para informar el efecto de un grupo
GRUPOS = ["nacional", "edad_4", "grupo_voto"]
DESTINO = PROCESSED_DIR / "temporal" / "banco_efectos_eventos.parquet"


def ventanas(fecha: dt.date, meses_con_datos: list[str]) -> tuple[list[str], list[str]]:
    me = f"{fecha.year:04d}-{fecha.month:02d}"
    antes = [m for m in meses_con_datos if m < me or (m == me and fecha.day >= DIA_CORTE)]
    despues = [m for m in meses_con_datos if m > me]
    return antes[-VENTANA:], despues[:VENTANA]


def _lado(d: pl.DataFrame, cat: str) -> tuple[float, float, int]:
    w = d["peso"].to_numpy()
    y = (d["valor"] == cat).to_numpy()
    p = float(np.average(y, weights=w))
    n_ef = w.sum() ** 2 / (w**2).sum()
    return p, p * (1 - p) / n_ef, d.height


def efectos() -> pl.DataFrame:
    filas = []
    for ev in load_config("eventos.yaml").eventos:  # type: ignore[attr-defined]
        for ind in T.indicadores():
            d = T.datos(ind)
            if ev.ambito.startswith("CCAA:"):
                d = d.filter(pl.col("ccaa") == ev.ambito.split(":")[1])
            antes, despues = ventanas(ev.fecha, sorted(d["mes"].unique()))
            if not antes or not despues:
                continue
            for g in GRUPOS:
                niveles = ["total"] if g == "nacional" else sorted(d[g].unique())
                for lv in niveles:
                    if lv == T.DESCONOCIDO:
                        continue
                    sel = d if g == "nacional" else d.filter(pl.col(g) == lv)
                    a = sel.filter(pl.col("mes").is_in(antes))
                    b = sel.filter(pl.col("mes").is_in(despues))
                    if a.height < MIN_CASOS or b.height < MIN_CASOS:
                        continue
                    for cat in sorted(d["valor"].unique()):
                        pa, va, na = _lado(a, cat)
                        pb, vb, nb = _lado(b, cat)
                        ef, ee = pb - pa, float(np.sqrt(va + vb))
                        filas.append(
                            {
                                "evento": ev.id,
                                "fecha": ev.fecha.isoformat(),
                                "ambito": ev.ambito,
                                "indicador": ind,
                                "categoria": cat,
                                "grupo": g,
                                "nivel": lv,
                                "meses_antes": ",".join(antes),
                                "meses_despues": ",".join(despues),
                                "n_antes": na,
                                "n_despues": nb,
                                "p_antes": pa,
                                "p_despues": pb,
                                "efecto": ef,
                                "error_tipico": ee,
                                "ic95_inf": ef - 1.96 * ee,
                                "ic95_sup": ef + 1.96 * ee,
                                "fuente_evento": ev.fuente,
                                "afectado_previsto": ind in ev.indicadores_afectados,
                            }
                        )
    return pl.DataFrame(filas)


def construir() -> dict:
    b = efectos()
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    b.write_parquet(DESTINO)
    (REPORTS_DIR / "fase_08c").mkdir(parents=True, exist_ok=True)
    b.filter(pl.col("grupo") == "nacional").write_csv(
        REPORTS_DIR / "fase_08c" / "banco_efectos_nacional.csv"
    )
    return {"filas": b.height, "eventos": b["evento"].n_unique()}
