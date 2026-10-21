"""Rasgos latentes de opinión (F8A, tareas 4 y 5; `02_datos_y_variables.md` §3.4).

`estilo_ns_nc`: propensión a contestar «No sabe» o «No contesta». Para cada encuestado del CIS,
la proporción de sus respuestas NS/NC entre las preguntas que ofrecen esa opción (sin contar
las que no le proceden). Es un estilo de respuesta, no una opinión, y se puede medir en
cualquier estudio.

Asignación (docs/03 §2.4, extracción y no media): el valor de una persona sintética es la
predicción de un modelo lineal ponderado según su perfil y territorio más un **residuo real**
de un encuestado de su misma celda edad × estudios × sexo, sorteado con la semilla. Así se conservan
la variabilidad y la asimetría dentro de los grupos (G8A.3).
"""

from __future__ import annotations

import datetime as dt

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion import latentes as L
from sinpop.opinion.cis import CORTE
from sinpop.opinion.valores import (
    COLUMNAS,
    VENTANA_MESES,
    _edad_grupo,
    columna,
    nacional,
    perfil_sintetico,
)
from sinpop.repro import make_rng

NS_NC_ETIQUETAS = [
    "N.S.",
    "N.C.",
    "No sabe, duda",
    "No sabe/duda",
    "N.S./No recuerda",
    "No sabe",
    "No contesta",
]
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
        .sort("estudio", "encuestado")  # group_by no conserva el orden: reproducibilidad
        .collect()
    )


COLUMNAS_ESS = ["sexo", "edad_grupo", "estudios_3", "actividad_3", "ccaa", "nacionalidad_esp_ext"]


def estilo_aquiescencia() -> pl.DataFrame:
    """Media de las 21 respuestas de la escala de valores de Schwartz de la ESS (6 = «Very much
    like me»), con al menos 16 respondidas: es la medida estándar de la tendencia a mostrarse de
    acuerdo con cualquier enunciado en esa escala (MRAT; Schwartz, guía de la ESS) (D-066)."""
    from sinpop.opinion import ess as E

    d = pl.read_parquet(E.SALIDA)
    pvq = list(E.PVQ)
    return (
        d.with_columns(
            pl.mean_horizontal(pvq).alias("estilo_aquiescencia"),
            pl.sum_horizontal([pl.col(v).is_not_null() for v in pvq]).alias("_n"),
        )
        .filter((pl.col("_n") >= 16) & (pl.col("edad") >= 18))
        .drop("_n")
    )


def columnas_rasgo(rasgo: str) -> list[str]:
    if rasgo == "estilo_aquiescencia":
        return COLUMNAS_ESS
    if rasgo == "estilo_ns_nc":
        return COLUMNAS
    return L.columnas(rasgo) or (COLUMNAS_ESS if L.universo(rasgo) == "todos" else COLUMNAS)


def datos_rasgo(rasgo: str = "estilo_ns_nc") -> pl.DataFrame:
    if rasgo == "estilo_aquiescencia":
        return (
            estilo_aquiescencia()
            .filter(
                ~pl.col("estudios_3").is_in(["NC", "NS"])
                & ~pl.col("actividad_3").is_in(["NC", "NS"])
            )
            .with_columns(_edad_grupo(pl.col("edad")))
        )
    if rasgo != "estilo_ns_nc":
        return L.datos(rasgo)
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    r = estilo_ns_nc()
    desde = dt.date(CORTE.year - (VENTANA_MESES // 12), CORTE.month, 1)
    d = p.join(r, on=["estudio", "encuestado"]).filter(
        (pl.col("fecha").str.to_date() >= desde)
        & (pl.col("fecha").str.to_date() < CORTE)
        & (pl.col("edad") >= 18)
        & (
            pl.col("nacionalidad_esp_ext").is_null()
            | (pl.col("nacionalidad_esp_ext") == "espanola")
        )
        & nacional()
        & ~pl.col("estudios_3").is_in(["NC", "NS"])
        & ~pl.col("actividad_3").is_in(["NC", "NS"])
    )
    return d.with_columns(
        _edad_grupo(pl.col("edad")),
        (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
    )


def _celda(df: pl.DataFrame) -> np.ndarray:
    """Celda de los residuos: edad × estudios × sexo (los grupos de G8A.3)."""
    return (
        df["edad_grupo"] + "|" + df["estudios_3"].cast(pl.Utf8) + "|" + df["sexo"].cast(pl.Utf8)
    ).to_numpy()


class ModeloRasgo:
    def __init__(self, rasgo: str, columnas: list[str] | None = None) -> None:
        self.rasgo = rasgo
        self.columnas = columnas or COLUMNAS

    def _x(self, df: pl.DataFrame) -> np.ndarray:
        cols = []
        for v in self.columnas:
            col = columna(df, v)
            m = np.zeros((df.height, len(self.cats[v])))
            for i, x in enumerate(col):
                j = self.cats[v].get(x)
                if j is not None:
                    m[i, j] = 1.0
            cols.append(m)
        return np.hstack(cols)

    def ajustar(self, d: pl.DataFrame) -> ModeloRasgo:
        from sklearn.linear_model import RidgeCV

        self.cats = {
            v: {c: i for i, c in enumerate(sorted({x for x in columna(d, v) if x is not None}))}
            for v in self.columnas
        }
        y = d[self.rasgo].to_numpy()
        w = d["peso"].to_numpy()
        # regularización elegida por validación cruzada (D-064)
        self.lr = RidgeCV(alphas=(0.1, 1.0, 10.0, 100.0, 1000.0)).fit(
            self._x(d), y, sample_weight=w
        )
        res = y - self.lr.predict(self._x(d))
        celda = _celda(d)
        self.residuos = {c: (res[celda == c], w[celda == c]) for c in np.unique(celda)}
        self.todos = (res, w)
        self.n = d.height
        return self

    def extraer(self, df: pl.DataFrame, rng: np.random.Generator) -> np.ndarray:
        pred = self.lr.predict(self._x(df))
        celda = _celda(df)
        out = np.empty(len(pred))
        for c in np.unique(celda):
            idx = np.flatnonzero(celda == c)
            r, w = self.residuos.get(c, self.todos)
            out[idx] = pred[idx] + rng.choice(r, size=len(idx), p=w / w.sum())
        return out


def asignar(persons: pl.DataFrame, semilla: int) -> tuple[pl.DataFrame, dict]:
    """Los estilos de respuesta y los rasgos latentes de `configs/rasgos.yaml`, con su
    `__calidad`. Lo que viene de la ESS (que entrevista a cualquier nacionalidad) solo es
    `extrapolada` en los residentes en establecimientos colectivos."""
    perfil = perfil_sintetico(persons)
    rng = make_rng(semilla)
    colectivo = perfil["tipo_residencia"] != "vivienda_familiar"
    extranjero = perfil["nacionalidad_esp_ext"] != "espanola"
    out = perfil.select("person_id")
    meta = {}
    for r in ["estilo_ns_nc", "estilo_aquiescencia", *L.rasgos()]:
        d = datos_rasgo(r)
        m = ModeloRasgo(r, columnas_rasgo(r)).ajustar(d)
        valor = m.extraer(perfil, rng)
        if r == "estilo_ns_nc":  # proporción
            valor = np.clip(valor, 0.0, 1.0)
        if r == "estilo_aquiescencia":  # media de una escala 1-6
            valor = np.clip(valor, 1.0, 6.0)
        todos = r == "estilo_aquiescencia" or (r in L.rasgos() and L.universo(r) == "todos")
        fuera = colectivo if todos else (colectivo | extranjero)
        calidad = np.where(fuera, "extrapolada", "modelada")
        out = out.with_columns(pl.Series(r, valor), pl.Series(f"{r}__calidad", calidad))
        meta[r] = {"encuestados": m.n, "estudios": sorted(d["estudio"].unique())}
    return out, meta
