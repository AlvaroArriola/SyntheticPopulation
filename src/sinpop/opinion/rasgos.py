"""Rasgos latentes de opinión (F8A, tareas 4 y 5; `02_datos_y_variables.md` §3.4).

`estilo_ns_nc`: propensión a contestar «No sabe» o «No contesta». Para cada encuestado del CIS,
la proporción de sus respuestas NS/NC entre las preguntas que ofrecen esa opción (sin contar
las que no le proceden). Es un estilo de respuesta, no una opinión, y se puede medir en
cualquier estudio.

Asignación (docs/03 §2.4, extracción y no media): el valor de una persona sintética es la
predicción de un modelo lineal ponderado según su perfil y territorio más un **residuo real**
de un encuestado de su misma celda edad × estudios, sorteado con la semilla. Así se conservan
la variabilidad y la asimetría dentro de los grupos (G8A.3).
"""

from __future__ import annotations

import datetime as dt

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion import latentes as L
from sinpop.opinion.cis import CORTE
from sinpop.opinion.valores import PREDICTORES, VENTANA_MESES, _edad_grupo, perfil_sintetico
from sinpop.repro import make_rng

NS_NC_ETIQUETAS = ["N.S.", "N.C.", "No sabe, duda", "N.S./No recuerda", "No sabe", "No contesta"]
NO_PROCEDE = ["No procede", "N.P."]
MIN_PREGUNTAS = 10  # preguntas con opción NS/NC necesarias para medir el estilo


def estilo_ns_nc() -> pl.DataFrame:
    """(estudio, encuestado, estilo_ns_nc) desde el formato largo del CIS."""
    lg = pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
    banco = pl.read_parquet(INTERIM_DIR / "cis_preguntas.parquet")
    con_opcion = banco.filter(
        pl.col("opciones").str.contains("N.S.", literal=True)
        | pl.col("opciones").str.contains("N.C.", literal=True)
    )["variable"].unique()
    return (
        lg.filter(pl.col("variable").is_in(con_opcion.to_list()))
        .filter(~pl.col("etiqueta").is_in(NO_PROCEDE))
        .group_by("estudio", "encuestado")
        .agg(
            pl.len().alias("preguntas"),
            pl.col("etiqueta").is_in(NS_NC_ETIQUETAS).mean().alias("estilo_ns_nc"),
        )
        .filter(pl.col("preguntas") >= MIN_PREGUNTAS)
        .collect()
    )


def datos_rasgo(rasgo: str = "estilo_ns_nc") -> pl.DataFrame:
    if rasgo != "estilo_ns_nc":
        return L.datos(rasgo)
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    r = estilo_ns_nc()
    desde = dt.date(CORTE.year - (VENTANA_MESES // 12), CORTE.month, 1)
    d = p.join(r, on=["estudio", "encuestado"]).filter(
        (pl.col("fecha").str.to_date() >= desde)
        & (pl.col("fecha").str.to_date() < CORTE)
        & (pl.col("edad") >= 18)
        & ~pl.col("estudios_3").is_in(["NC", "NS"])
        & ~pl.col("actividad_3").is_in(["NC", "NS"])
    )
    return d.with_columns(
        _edad_grupo(pl.col("edad")),
        (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
    )


class ModeloRasgo:
    def __init__(self, rasgo: str) -> None:
        self.rasgo = rasgo

    def _x(self, df: pl.DataFrame) -> np.ndarray:
        cols = []
        for v in PREDICTORES:
            col = df[v].cast(pl.Utf8).to_list()
            m = np.zeros((df.height, len(self.cats[v])))
            for i, x in enumerate(col):
                j = self.cats[v].get(x)
                if j is not None:
                    m[i, j] = 1.0
            cols.append(m)
        return np.hstack(cols)

    def ajustar(self, d: pl.DataFrame) -> ModeloRasgo:
        from sklearn.linear_model import Ridge

        self.cats = {
            v: {
                c: i
                for i, c in enumerate(sorted(d[v].cast(pl.Utf8).drop_nulls().unique().to_list()))
            }
            for v in PREDICTORES
        }
        y = d[self.rasgo].to_numpy()
        w = d["peso"].to_numpy()
        self.lr = Ridge(alpha=1.0).fit(self._x(d), y, sample_weight=w)
        res = y - self.lr.predict(self._x(d))
        celda = (d["edad_grupo"] + "|" + d["estudios_3"]).to_numpy()
        self.residuos = {c: (res[celda == c], w[celda == c]) for c in np.unique(celda)}
        self.todos = (res, w)
        self.n = d.height
        return self

    def extraer(self, df: pl.DataFrame, rng: np.random.Generator) -> np.ndarray:
        pred = self.lr.predict(self._x(df))
        celda = (df["edad_grupo"] + "|" + df["estudios_3"].cast(pl.Utf8)).to_numpy()
        out = np.empty(len(pred))
        for c in np.unique(celda):
            idx = np.flatnonzero(celda == c)
            r, w = self.residuos.get(c, self.todos)
            out[idx] = pred[idx] + rng.choice(r, size=len(idx), p=w / w.sum())
        return out


def asignar(persons: pl.DataFrame, semilla: int) -> tuple[pl.DataFrame, dict]:
    """El estilo NS/NC y los rasgos latentes de `configs/rasgos.yaml`, con su `__calidad`."""
    perfil = perfil_sintetico(persons)
    rng = make_rng(semilla)
    extrapolada = (perfil["nacionalidad_esp_ext"] != "espanola") | (
        perfil["tipo_residencia"] != "vivienda_familiar"
    )
    calidad = np.where(extrapolada, "extrapolada", "modelada")
    out = perfil.select("person_id")
    meta = {}
    for r in ["estilo_ns_nc", *L.rasgos()]:
        d = datos_rasgo(r)
        m = ModeloRasgo(r).ajustar(d)
        valor = m.extraer(perfil, rng)
        if r == "estilo_ns_nc":  # proporción
            valor = np.clip(valor, 0.0, 1.0)
        out = out.with_columns(pl.Series(r, valor), pl.Series(f"{r}__calidad", calidad))
        meta[r] = {"encuestados": m.n, "estudios": sorted(d["estudio"].unique())}
    return out, meta
