"""Variables observadas de valores (F8A, tarea 3; `02_datos_y_variables.md` §3.4).

Para cada variable, un modelo multinomial ponderado (pesos del CIS) de la respuesta según el
perfil y el territorio de la persona, ajustado con los barómetros de los 12 meses anteriores al
corte (la foto de junio de 2026). «No sabe» y «No contesta» son una categoría más (CLAUDE.md,
regla 10). A cada persona sintética se le asigna una **extracción aleatoria** de su
distribución predicha, con la semilla, no la categoría más probable (docs/03 §2.4).

El universo de los barómetros son las personas de nacionalidad española de 18 años y más en
viviendas familiares: los extranjeros y los residentes en colectivos reciben la predicción del
modelo con su perfil y se marcan `extrapolada`; el resto, `modelada` (D-063).
"""

from __future__ import annotations

import datetime as dt

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion.cis import CORTE, VALORES
from sinpop.repro import make_rng

VENTANA_MESES = 12
EDADES = [18, 25, 35, 45, 55, 65, 75]
PREDICTORES = ["sexo", "edad_grupo", "estudios_3", "actividad_3", "ccaa", "tamano_municipio_cis"]
# Interacción comunidad × edad (cuatro grupos), como en MRP: el modelo aditivo no recoge las
# diferencias de edad propias de cada comunidad, que es lo que compara G8A.4 (D-064)
INTERACCIONES = {"ccaa_edad4": ("ccaa", "edad")}
COLUMNAS = PREDICTORES + list(INTERACCIONES)


def _edad4_txt(edad: pl.Series) -> pl.Series:
    return pl.select(
        pl.when(edad < 35)
        .then(pl.lit("18-34"))
        .when(edad < 50)
        .then(pl.lit("35-49"))
        .when(edad < 65)
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
    ).to_series()


def columna(df: pl.DataFrame, v: str) -> list:
    """Valores (texto) de un predictor o de una interacción para la matriz del modelo."""
    if v in INTERACCIONES:
        a, e = INTERACCIONES[v]
        return (df[a].cast(pl.Utf8) + "|" + _edad4_txt(df[e])).to_list()
    return df[v].cast(pl.Utf8).to_list()


# Tamaño de municipio del Padrón (población) → clases comunes con el CIS (que corta en 400.000)
TAMANO_A_CIS = {
    "hasta_2000": "hasta_2000",
    "de_2001_a_10000": "de_2001_a_10000",
    "de_10001_a_50000": "de_10001_a_50000",
    "de_50001_a_100000": "de_50001_a_100000",
    "de_100001_a_500000": "mas_de_100000",
    "mas_de_500000": "mas_de_100000",
}


def _edad_grupo(edad: pl.Expr) -> pl.Expr:
    e = pl.lit(f"{EDADES[-1]}+")
    for lo, hi in reversed(list(zip(EDADES[:-1], EDADES[1:], strict=True))):
        e = pl.when(edad < hi).then(pl.lit(f"{lo}-{hi - 1}")).otherwise(e)
    return e.alias("edad_grupo")


def datos(variable: str) -> pl.DataFrame:
    """Encuestados del CIS con la variable, en la ventana anterior al corte, con el peso
    normalizado para que cada estudio cuente por su tamaño."""
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    desde = dt.date(CORTE.year - 1, CORTE.month, 1)
    p = p.filter(
        pl.col(variable).is_not_null()
        & (pl.col(variable) != "NP")
        & (pl.col("fecha").str.to_date() >= desde)
        & (pl.col("fecha").str.to_date() < CORTE)
        & (pl.col("edad") >= 18)
        # universo de los barómetros (D-063): el Barómetro Sanitario también entrevista a
        # extranjeros, que aquí no entran porque el modelo no tiene la nacionalidad
        & (
            pl.col("nacionalidad_esp_ext").is_null()
            | (pl.col("nacionalidad_esp_ext") == "espanola")
        )
    )
    return p.with_columns(
        _edad_grupo(pl.col("edad")),
        (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
    ).filter(~pl.col("estudios_3").is_in(["NC", "NS"]) & ~pl.col("actividad_3").is_in(["NC", "NS"]))


class Modelo:
    """Regresión logística multinomial ponderada con codificación one-hot de los predictores."""

    REJILLA_C = (0.01, 0.03, 0.1, 0.3, 1.0)

    def __init__(self, variable: str, c: float | None = None) -> None:
        """`c` = None: la regularización se elige por validación cruzada (3 particiones fijas,
        log-verosimilitud ponderada), así el modelo se encoge hacia efectos más simples cuando
        hay pocos encuestados por comunidad y edad, como en MRP (D-064)."""
        self.variable = variable
        self.c = c

    def _x(self, df: pl.DataFrame):
        import scipy.sparse as sp

        filas = []
        for v in COLUMNAS:
            col = columna(df, v)
            idx = np.array([self.cats[v].get(x, -1) for x in col])
            m = sp.csr_matrix(
                (np.ones((idx >= 0).sum()), (np.flatnonzero(idx >= 0), idx[idx >= 0])),
                shape=(df.height, len(self.cats[v])),
            )
            filas.append(m)
        return sp.hstack(filas).tocsr()

    def ajustar(self, df: pl.DataFrame) -> Modelo:
        from sklearn.linear_model import LogisticRegression

        self.cats = {
            v: {c: i for i, c in enumerate(sorted({x for x in columna(df, v) if x is not None}))}
            for v in COLUMNAS
        }
        self.clases = sorted(df[self.variable].unique().to_list())
        y = df[self.variable].to_numpy()
        x, w = self._x(df), df["peso"].to_numpy()
        self.c_elegido = self.c if self.c is not None else self._elegir_c(x, y, w)
        self.lr = LogisticRegression(C=self.c_elegido, max_iter=2000)
        self.lr.fit(x, y, sample_weight=w)
        self.n = df.height
        return self

    def _elegir_c(self, x, y: np.ndarray, w: np.ndarray) -> float:
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import log_loss
        from sklearn.model_selection import KFold

        clases = np.unique(y)
        perdida = {}
        for c in self.REJILLA_C:
            total = 0.0
            for tr, te in KFold(3, shuffle=True, random_state=0).split(y):
                lr = LogisticRegression(C=c, max_iter=2000).fit(x[tr], y[tr], sample_weight=w[tr])
                p = np.full((len(te), len(clases)), 1e-9)
                p[:, np.searchsorted(clases, lr.classes_)] = lr.predict_proba(x[te])
                total += log_loss(
                    y[te], p / p.sum(1, keepdims=True), sample_weight=w[te], labels=clases
                )
            perdida[c] = total
        return min(perdida, key=perdida.get)

    def probabilidades(self, df: pl.DataFrame) -> np.ndarray:
        return self.lr.predict_proba(self._x(df))


def perfil_sintetico(persons: pl.DataFrame) -> pl.DataFrame:
    """Adultos de la población con los predictores en la codificación del CIS."""
    return persons.filter(pl.col("edad") >= 18).select(
        "person_id",
        "sexo",
        "edad",
        _edad_grupo(pl.col("edad")),
        "estudios_3",
        pl.when(pl.col("relacion_actividad").is_in(["ocupado", "parado", "NC"]))
        .then(pl.col("relacion_actividad"))
        .otherwise(pl.lit("inactivo"))
        .alias("actividad_3"),
        "ccaa",
        pl.col("tamano_municipio")
        .replace_strict(TAMANO_A_CIS, default=None)
        .alias("tamano_municipio_cis"),
        "nacionalidad_esp_ext",
        "tipo_residencia",
    )


def asignar(
    persons: pl.DataFrame, semilla: int, variables: list[str] | None = None
) -> tuple[pl.DataFrame, dict]:
    """Una fila por adulto con cada variable de valores y su `__calidad`."""
    perfil = perfil_sintetico(persons)
    out = perfil.select("person_id")
    rng = make_rng(semilla)
    extrapolada = (perfil["nacionalidad_esp_ext"] != "espanola") | (
        perfil["tipo_residencia"] != "vivienda_familiar"
    )
    meta = {}
    for v in variables or list(VALORES):
        d = datos(v)
        m = Modelo(v).ajustar(d)
        pr = m.probabilidades(perfil)
        u = rng.random(len(pr))
        idx = (pr.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(m.clases) - 1)
        out = out.with_columns(
            pl.Series(v, np.array(m.clases)[idx]),
            pl.Series(f"{v}__calidad", np.where(extrapolada, "extrapolada", "modelada")),
        )
        meta[v] = {"encuestados": m.n, "estudios": sorted(d["estudio"].unique().to_list())}
    return out, meta
