"""Modo evento (F9, tarea 6; docs/03 §2.7) (D-069).

Ante un evento nuevo devuelve, para un indicador de `configs/temporal.yaml`, la distribución
**antes**, la de **después** y el **cambio**. Sin modelo de lenguaje, el tipo del evento
(`politico`, `economico`, `social`, `catastrofe`, `internacional`) y el indicador los da quien
pregunta; el LLM, cuando se incorpore, solo los propondría.

- Antes: el nivel del indicador en el último mes con barómetro anterior al evento (serie
  ponderada del CIS, `temporal.indicadores.serie`).
- Cambio: la media de los efectos observados de los eventos del banco del mismo tipo y del mismo
  ámbito (estatal o autonómico) sobre ese indicador (`temporal/eventos.py`), con un intervalo que
  suma la varianza muestral de cada efecto y la dispersión entre eventos.
- Después: antes + cambio, recortado a [0, 1] y renormalizado.

Es una predicción por analogía: con pocos eventos parecidos es muy incierta, y así se declara.
"""

from __future__ import annotations

import datetime as dt

import numpy as np
import polars as pl

from sinpop.temporal import eventos as EV
from sinpop.temporal import indicadores as T


def banco() -> pl.DataFrame:
    return pl.read_parquet(EV.DESTINO).filter(pl.col("grupo") == "nacional")


def tipos() -> dict[str, str]:
    from sinpop.config import load_config

    return {e.id: e.tipo for e in load_config("eventos.yaml").eventos}  # type: ignore[attr-defined]


def efecto_por_analogia(
    indicador: str, tipo: str, ambito: str, excluir: str | None = None
) -> pl.DataFrame | None:
    """Efecto medio por categoría de los eventos análogos (o None si no hay ninguno)."""
    t = tipos()
    autonomico = ambito.startswith("CCAA:")
    b = banco().filter(
        (pl.col("indicador") == indicador)
        & (pl.col("evento").replace_strict(t, default=None) == tipo)
        & (pl.col("ambito").str.starts_with("CCAA:") == autonomico)
    )
    if excluir:
        b = b.filter(pl.col("evento") != excluir)
    if b.is_empty():
        return None
    return (
        b.group_by("categoria")
        .agg(
            pl.col("efecto").mean().alias("cambio"),
            pl.col("efecto").std(ddof=1).fill_null(0.0).alias("sd_eventos"),
            (pl.col("error_tipico") ** 2).mean().sqrt().alias("ee_medio"),
            pl.col("evento").n_unique().alias("eventos_analogos"),
            pl.col("evento").unique().sort().alias("analogos"),
        )
        .with_columns(
            (pl.col("sd_eventos") ** 2 + pl.col("ee_medio") ** 2).sqrt().alias("incertidumbre")
        )
        .sort("categoria")
    )


def antes(indicador: str, fecha: dt.date, ccaa: str | None = None) -> pl.DataFrame:
    d = T.datos(indicador)
    if ccaa:
        d = d.filter(pl.col("ccaa") == ccaa)
    me = f"{fecha.year:04d}-{fecha.month:02d}"
    previos = sorted(m for m in d["mes"].unique() if m < me)
    if not previos:
        raise ValueError(f"{indicador}: no hay barómetros antes de {fecha}")
    x = d.filter(pl.col("mes") == previos[-1])
    return (
        x.group_by("valor")
        .agg(pl.col("peso").sum())
        .with_columns((pl.col("peso") / pl.col("peso").sum()).alias("antes"))
        .select(pl.col("valor").alias("categoria"), "antes", pl.lit(previos[-1]).alias("mes"))
        .sort("categoria")
    )


def predecir(indicador: str, fecha: dt.date, tipo: str, ambito: str = "ES") -> dict:
    ccaa = ambito.split(":")[1] if ambito.startswith("CCAA:") else None
    a = antes(indicador, fecha, ccaa)
    ef = efecto_por_analogia(indicador, tipo, ambito)
    if ef is None:
        return {
            "indicador": indicador,
            "antes": a.to_dicts(),
            "cambio": None,
            "motivo": f"sin eventos de tipo {tipo} en el banco",
        }
    x = a.join(ef, on="categoria", how="left").with_columns(
        pl.col("cambio").fill_null(0.0), pl.col("incertidumbre").fill_null(0.0)
    )
    despues = np.clip(x["antes"].to_numpy() + x["cambio"].to_numpy(), 0, 1)
    despues = despues / despues.sum()
    x = x.with_columns(pl.Series("despues", despues))
    return {
        "indicador": indicador,
        "mes_antes": a["mes"][0],
        "categorias": [
            {
                "categoria": r["categoria"],
                "antes": r["antes"],
                "despues": r["despues"],
                "cambio": r["despues"] - r["antes"],
                "ic80_cambio": [
                    r["cambio"] - 1.2816 * r["incertidumbre"],
                    r["cambio"] + 1.2816 * r["incertidumbre"],
                ],
            }
            for r in x.iter_rows(named=True)
        ],
        "eventos_analogos": sorted(set(sum((v or [] for v in ef["analogos"].to_list()), []))),
    }


def backtest() -> pl.DataFrame:
    """V-EVENTO: cada evento pasado se predice con los demás (dejando uno fuera). Para cada
    indicador que el evento afectaba según su ficha, la dirección es correcta si el cambio
    predicho en la categoría que más cambió de verdad tiene su mismo signo."""
    from sinpop.config import load_config

    filas = []
    b = banco()
    for e in load_config("eventos.yaml").eventos:  # type: ignore[attr-defined]
        for ind in e.indicadores_afectados:
            obs = b.filter((pl.col("evento") == e.id) & (pl.col("indicador") == ind))
            if obs.is_empty():
                continue
            pred = efecto_por_analogia(ind, e.tipo, e.ambito, excluir=e.id)
            if pred is None:
                continue
            top = obs.sort(pl.col("efecto").abs(), descending=True).row(0, named=True)
            p = pred.filter(pl.col("categoria") == top["categoria"])
            if p.is_empty():
                continue
            pc = p["cambio"][0]
            filas.append(
                {
                    "evento": e.id,
                    "tipo": e.tipo,
                    "indicador": ind,
                    "categoria": top["categoria"],
                    "cambio_real": top["efecto"],
                    "ic95_real": [top["ic95_inf"], top["ic95_sup"]],
                    "cambio_predicho": pc,
                    "eventos_analogos": p["eventos_analogos"][0],
                    "direccion_correcta": bool(np.sign(pc) == np.sign(top["efecto"]) and pc != 0),
                    "error_magnitud_pp": abs(pc - top["efecto"]) * 100,
                }
            )
    return pl.DataFrame(filas)
