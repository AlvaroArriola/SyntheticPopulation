"""Partido más cercano a sus ideas (F8B, tarea 5; `02_datos_y_variables.md` §3.5) (D-067).

`CERCANIA` de los estudios del CIS de los 12 meses anteriores al corte, por familia, con
«ninguno», N.S. y N.C. como opciones propias (regla 10: no tener partido cercano es una respuesta
real y frecuente). Cada etiqueta toma la familia que ya tiene en `configs/partidos.yaml` (códigos
del CIS y recuerdo autonómico) o en `cercania_cis_adicionales`; una etiqueta sin familia detiene
el proceso.

Modelo multinomial ponderado con el perfil, la religiosidad, la clase subjetiva y el recuerdo de
voto de 2023 ya calibrado (como la ideología). Quien no tenía edad para votar en 2023 entra con
esa categoría; quien no tiene la nacionalidad (fuera del universo del CIS) recibe el modelo sin
recuerdo y queda `extrapolada`.
"""

from __future__ import annotations

import datetime as dt
from functools import lru_cache

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.config import load_config
from sinpop.opinion.cis import CORTE, fechas
from sinpop.opinion.valores import COLUMNAS, VENTANA_MESES, Modelo, _edad_grupo, perfil_sintetico
from sinpop.politics import recuerdo as RV

FAMILIAS = [
    "izquierda_estatal",
    "socialdemocrata",
    "centro_derecha_estatal",
    "derecha_radical",
    "nacionalista_regionalista",
    "otros",
]
OPCIONES = FAMILIAS + ["ninguno", "NS", "NC"]
COLUMNAS_CERCANIA = COLUMNAS + ["religiosidad", "clase_subjetiva", "recuerdo"]
RECUERDOS = RV.OPCIONES + ["no_tenia_edad"]


@lru_cache(maxsize=1)
def mapa() -> dict[str, str]:
    cfg = load_config("partidos.yaml")
    m: dict[str, str] = {}
    for estudio in cfg.cis.values():  # type: ignore[attr-defined]
        for cod in estudio.codigos.values():
            if cod.etiqueta and cod.familia:
                for et in cod.etiqueta.split(" / "):
                    m[et] = cod.familia
    m |= {k: v for k, v in cfg.recuerdo_cis_autonomicas.items() if v in FAMILIAS}  # type: ignore[attr-defined]
    return m | cfg.cercania_cis_adicionales  # type: ignore[attr-defined]


def estudios() -> list[str]:
    desde = dt.date(CORTE.year - VENTANA_MESES // 12, CORTE.month, 1)
    banco = pl.read_parquet(INTERIM_DIR / "cis_preguntas.parquet")
    q = banco.filter(pl.col("variable") == "CERCANIA").explode("estudios")
    f = fechas()
    return sorted(
        e
        for e in q["estudios"].unique().to_list()
        if e in f and desde <= dt.date.fromisoformat(f[e]) < CORTE
    )


def respuestas() -> pl.DataFrame:
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter(pl.col("estudio").is_in(estudios()) & (pl.col("variable") == "CERCANIA"))
        .select("estudio", "encuestado", pl.col("etiqueta").str.strip_chars())
        .collect()
    )
    m = mapa()
    sin = sorted(set(lg["etiqueta"].drop_nulls().unique()) - set(m))
    if sin:
        raise ValueError(f"CERCANIA: etiquetas sin familia en partidos.yaml: {sin}")
    return lg.with_columns(
        pl.col("etiqueta").replace_strict(m, default=None).alias("cercania")
    ).drop("etiqueta")


def datos() -> pl.DataFrame:
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    return (
        p.join(respuestas(), on=["estudio", "encuestado"])
        .join(RV.respuestas(), on=["estudio", "encuestado"])
        .filter(
            (pl.col("edad") >= 18)
            & ~pl.col("estudios_3").is_in(["NC", "NS"])
            & ~pl.col("actividad_3").is_in(["NC", "NS"])
            & pl.col("recuerdo").is_in(RECUERDOS)
            & pl.col("cercania").is_in(OPCIONES)
        )
        .with_columns(
            (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
            _edad_grupo(pl.col("edad")),
        )
        .sort("estudio", "encuestado")
    )


def asignar(
    persons: pl.DataFrame, opinion: pl.DataFrame, voto: pl.DataFrame, rng: np.random.Generator
) -> tuple[pl.DataFrame, dict]:
    perfil = (
        perfil_sintetico(persons)
        .join(opinion.select("person_id", "religiosidad", "clase_subjetiva"), on="person_id")
        .join(
            voto.select("person_id", pl.col("recuerdo_voto_generales").alias("recuerdo")),
            on="person_id",
        )
    )
    d = datos()
    m = Modelo("cercania", columnas=COLUMNAS_CERCANIA).ajustar(d)
    m0 = Modelo("cercania", columnas=COLUMNAS + ["religiosidad", "clase_subjetiva"]).ajustar(d)
    if list(m.clases) != list(m0.clases):
        raise ValueError("cercanía: opciones distintas entre los dos modelos")
    con = perfil["recuerdo"].is_in(RECUERDOS).to_numpy()
    pr = np.where(con[:, None], m.probabilidades(perfil), m0.probabilidades(perfil))
    u = rng.random(len(pr))
    idx = (pr.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(m.clases) - 1)
    fuera = (perfil["nacionalidad_esp_ext"] != "espanola") | (
        perfil["tipo_residencia"] != "vivienda_familiar"
    )
    out = perfil.select("person_id").with_columns(
        pl.Series("cercania_partido", np.array(m.clases)[idx]),
        pl.Series("cercania_partido__calidad", np.where(fuera, "extrapolada", "modelada")),
    )
    return out, {
        "encuestados": d.height,
        "estudios": sorted(d["estudio"].unique()),
        "c": m.c_elegido,
        "opciones": list(m.clases),
    }
