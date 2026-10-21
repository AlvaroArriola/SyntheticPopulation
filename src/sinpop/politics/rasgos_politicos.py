"""Rasgos políticos latentes (F8B, tarea 6; `02_datos_y_variables.md` §3.5, docs/03 §2.5 punto 5).

`rasgo_izquierda_derecha`, `rasgo_desafeccion`, `rasgo_implicacion_politica` y
`rasgo_eje_territorial` se definen en `configs/rasgos.yaml` (`rasgos_politicos`) y se estiman
como los de F8A (`opinion/latentes.py`: factorial, puntuación de cada encuestado). La asignación
es la misma extracción condicionada (`opinion/rasgos.ModeloRasgo`: predicción ponderada + residuo
real de un encuestado de la celda edad × estudios × sexo), con predictores políticos además del
perfil (D-067):

- `grupo_voto`: el recuerdo de voto de 2023 ya calibrado de la persona (blanco, nulo y otros
  juntos; quienes no tenían edad o derecho, juntos). En los encuestados, su recuerdo declarado;
  los que no lo dicen (NS/NC) no entran en el modelo. El eje territorial (estudio 3409, anterior a
  las generales de 2023) no lo usa.
- `ideologia_bloque` (izquierda-derecha y eje territorial): la autoubicación ya asignada en
  tres bloques más NS/NC. La ESS usa 0-10 y el CIS 1-10: se cortan por la posición relativa en
  el recorrido de cada escala (izquierda ≤ 1/3, derecha > 0,6): ESS 0-3 / 4-6 / 7-10 y
  CIS 1-4 / 5-6 / 7-10.

Así cada rasgo es coherente con el voto y la ideología de la persona sin quedar fijado por ellos.
"""

from __future__ import annotations

import numpy as np
import polars as pl

from sinpop.opinion import latentes as L
from sinpop.opinion.rasgos import ModeloRasgo, columnas_rasgo
from sinpop.opinion.valores import perfil_sintetico
from sinpop.politics import ideologia as I
from sinpop.politics import recuerdo as RV
from sinpop.politics.ess_donantes import GRUPO


def bloque_ess(lr: pl.Expr) -> pl.Expr:
    return (
        pl.when(lr.is_null())
        .then(pl.lit("NS_NC"))
        .when(lr <= 3)
        .then(pl.lit("izquierda"))
        .when(lr <= 6)
        .then(pl.lit("centro"))
        .otherwise(pl.lit("derecha"))
    )


def bloque_cis(ideologia: pl.Expr) -> pl.Expr:
    n = ideologia.cast(pl.Int64, strict=False)
    return (
        pl.when(n.is_null())
        .then(pl.lit("NS_NC"))
        .when(n <= 4)
        .then(pl.lit("izquierda"))
        .when(n <= 6)
        .then(pl.lit("centro"))
        .otherwise(pl.lit("derecha"))
    )


def predictores(rasgo: str) -> list[str]:
    return columnas_rasgo(rasgo) + L.definicion(rasgo).get("predictores_extra", [])


def datos(rasgo: str) -> pl.DataFrame:
    """Encuestados con la puntuación del rasgo y los predictores políticos."""
    d = L.datos(rasgo)
    if L.universo(rasgo) == "todos":  # ESS
        d = d.with_columns(
            pl.col("voto_generales_2023").alias("_voto"),
            bloque_ess(pl.col("lrscale")).alias("ideologia_bloque"),
        )
    else:
        ideol = I.respuestas().select("estudio", "encuestado", "ideologia")
        d = d.join(ideol, on=["estudio", "encuestado"], how="left").with_columns(
            bloque_cis(pl.col("ideologia")).alias("ideologia_bloque")
        )
    d = d.sort("estudio", "encuestado")  # orden fijo: residuos sorteados por posición
    if "grupo_voto" not in predictores(rasgo):
        return d
    if L.universo(rasgo) != "todos":
        d = d.join(
            RV.respuestas().select("estudio", "encuestado", pl.col("recuerdo").alias("_voto")),
            on=["estudio", "encuestado"],
            how="left",
        )
    return (
        d.filter(pl.col("_voto").is_in(list(GRUPO)))
        .with_columns(pl.col("_voto").replace_strict(GRUPO).alias("grupo_voto"))
        .drop("_voto")
        .sort("estudio", "encuestado")
    )


def perfil(persons: pl.DataFrame, voto: pl.DataFrame, ideologia: pl.DataFrame) -> pl.DataFrame:
    return (
        perfil_sintetico(persons)
        .join(
            voto.select(
                "person_id",
                pl.col("recuerdo_voto_generales").replace_strict(GRUPO).alias("grupo_voto"),
            ),
            on="person_id",
        )
        .join(
            ideologia.select(
                "person_id",
                bloque_cis(pl.col("ideologia_autoubicacion")).alias("ideologia_bloque"),
            ),
            on="person_id",
        )
    )


def asignar(
    persons: pl.DataFrame,
    voto: pl.DataFrame,
    ideologia: pl.DataFrame,
    rng: np.random.Generator,
) -> tuple[pl.DataFrame, dict]:
    """Cada rasgo político con su `__calidad`: lo que viene de la ESS (residentes de cualquier
    nacionalidad) solo es `extrapolada` en colectivos; lo del CIS (españoles), también en los
    extranjeros."""
    p = perfil(persons, voto, ideologia)
    colectivo = (p["tipo_residencia"] != "vivienda_familiar").to_numpy()
    extranjero = (p["nacionalidad_esp_ext"] != "espanola").to_numpy()
    out = p.select("person_id")
    meta = {}
    for r in L.rasgos("politica"):
        d = datos(r)
        m = ModeloRasgo(r, predictores(r)).ajustar(d)
        fuera = colectivo if L.universo(r) == "todos" else (colectivo | extranjero)
        out = out.with_columns(
            pl.Series(r, m.extraer(p, rng)),
            pl.Series(f"{r}__calidad", np.where(fuera, "extrapolada", "modelada")),
        )
        meta[r] = {
            "encuestados": m.n,
            "estudios": sorted(d["estudio"].unique()),
            "predictores": predictores(r),
        }
    return out, meta
