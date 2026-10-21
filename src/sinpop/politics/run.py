"""Capa política de una población (F8B): `politics.parquet` y su metadata.

Una fila por persona adulta, unida por `person_id`. La población base y la capa de opinión no
cambian (solo se añade). Orden (`03_arquitectura.md` §2.5): derecho a voto, recuerdo de voto
anclado en resultados oficiales y, después, lo que depende de él.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json

import polars as pl

from sinpop import POPULATIONS_DIR
from sinpop.politics import derecho as DV
from sinpop.politics import recuerdo as RV
from sinpop.repro import code_version, make_rng, sha256_file

FECHA_REFERENCIA = "2026-06-30"


def semilla_capa(semilla: int, capa: str) -> int:
    return int(hashlib.sha256(f"{semilla}:{capa}".encode()).hexdigest()[:8], 16)


def construir(run_id: str) -> dict:
    d = POPULATIONS_DIR / run_id
    meta_pob = json.loads((d / "metadata.json").read_text("utf-8"))
    persons = pl.read_parquet(d / "persons.parquet").filter(pl.col("edad") >= 18)
    opinion = pl.read_parquet(d / "opinion.parquet")
    semilla = semilla_capa(int(meta_pob["semilla"]), "politica")
    tabla = DV.derechos_actuales(persons)
    eleg = DV.elegible(persons, RV.ELECCION, make_rng(semilla_capa(semilla, "elegible_2023")))
    voto, info_voto = RV.asignar(persons, opinion, eleg, make_rng(semilla_capa(semilla, "voto")))
    tabla = tabla.join(voto, on="person_id", how="left").with_columns(
        pl.lit(FECHA_REFERENCIA).alias("fecha_referencia")
    )
    destino = d / "politics.parquet"
    tabla.write_parquet(destino)
    meta = {
        "run_id": run_id,
        "capa": "politica",
        "fecha_referencia": FECHA_REFERENCIA,
        "semilla_poblacion": meta_pob["semilla"],
        "semilla_capa": semilla,
        "version_codigo": code_version(),
        "fecha": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "fuentes": {
            "cis_barometros": "CIS, barómetros y estudios con recuerdo de voto de 2023 (citar "
            "el número de estudio y al CIS)",
            "infoelectoral_resultados": "Ministerio del Interior, generales del 23/07/2023 "
            "(escrutinio provisional por municipio, residentes)",
        },
        "variables": {"recuerdo_voto_generales": info_voto},
        "personas": tabla.height,
        "sha256": sha256_file(destino),
    }
    (d / "politics_metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1, default=str), "utf-8"
    )
    return meta
