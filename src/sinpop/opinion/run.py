"""Capa de opinión y valores de una población (F8A): `opinion.parquet` y su metadata.

Una fila por persona adulta, unida por `person_id`, con las variables de valores y los rasgos,
cada uno con su `__calidad`, y la fecha de referencia (docs/03, «opinion.parquet»). La
población base no cambia (D-005): la capa va en un fichero aparte.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json

import polars as pl

from sinpop import POPULATIONS_DIR
from sinpop.opinion import lengua as LG
from sinpop.opinion import medios as MD
from sinpop.opinion import rasgos as R
from sinpop.opinion import valores as V
from sinpop.repro import code_version, sha256_file

FECHA_REFERENCIA = "2026-06-30"


def semilla_capa(semilla: int, capa: str) -> int:
    return int(hashlib.sha256(f"{semilla}:{capa}".encode()).hexdigest()[:8], 16)


def construir(run_id: str) -> dict:
    d = POPULATIONS_DIR / run_id
    meta_pob = json.loads((d / "metadata.json").read_text("utf-8"))
    persons = pl.read_parquet(d / "persons.parquet")
    semilla = semilla_capa(int(meta_pob["semilla"]), "opinion")
    tabla, info = V.asignar(persons, semilla)
    tr, info_r = R.asignar(persons, semilla_capa(semilla, "rasgos"))
    tabla = tabla.join(tr, on="person_id", how="left")
    info |= info_r
    for nombre, modulo in [("lengua", LG), ("medios", MD)]:
        t_, i_ = modulo.asignar(persons, semilla_capa(semilla, nombre))
        tabla = tabla.join(t_, on="person_id", how="left")
        info |= i_
    tabla = tabla.with_columns(pl.lit(FECHA_REFERENCIA).alias("fecha_referencia"))
    destino = d / "opinion.parquet"
    tabla.write_parquet(destino)
    meta = {
        "run_id": run_id,
        "capa": "opinion",
        "fecha_referencia": FECHA_REFERENCIA,
        "semilla_poblacion": meta_pob["semilla"],
        "semilla_capa": semilla,
        "version_codigo": code_version(),
        "fecha": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "fuentes": {
            "cis_barometros": "CIS, barómetros mensuales y estudios temáticos (citar el número "
            "de estudio y al CIS)",
            "ecepov2021": "INE, Encuesta de Características Esenciales de la Población y las "
            "Viviendas 2021 (lengua habitual)",
        },
        "variables": info,
        "personas": tabla.height,
        "sha256": sha256_file(destino),
    }
    (d / "opinion_metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), "utf-8"
    )
    return meta
