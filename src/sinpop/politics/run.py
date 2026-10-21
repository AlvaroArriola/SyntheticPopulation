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
from sinpop.politics import ess_donantes as ED
from sinpop.politics import ideologia as ID
from sinpop.politics import rasgos_politicos as RP
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
    tabla = tabla.with_columns(pl.Series("derecho_voto_generales_2023", eleg))
    voto, info_voto = RV.asignar(persons, opinion, eleg, make_rng(semilla_capa(semilla, "voto")))
    ideol, info_ideol = ID.asignar(
        persons, opinion, voto, make_rng(semilla_capa(semilla, "ideologia"))
    )
    rasgos, info_rasgos = RP.asignar(
        persons, voto, ideol, make_rng(semilla_capa(semilla, "rasgos_politicos"))
    )
    actitudes, info_ess = ED.asignar(persons, voto, make_rng(semilla_capa(semilla, "ess")))
    tabla = (
        tabla.join(voto, on="person_id", how="left")
        .join(ideol, on="person_id", how="left")
        .join(rasgos, on="person_id", how="left")
        .join(actitudes, on="person_id", how="left")
        .with_columns(pl.lit(FECHA_REFERENCIA).alias("fecha_referencia"))
        .sort("person_id")
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
            "cis_3409": "CIS, estudio 3409, Identidades culturales, nacionales y europeas (2023)",
            "ess11": "European Social Survey European Research Infrastructure (ESS ERIC), "
            "ESS round 11 - 2023, fichero integrado, edición 4.2 (ESS11e04_2), distribuido "
            "por Sikt; submuestra de España",
        },
        "variables": {
            "recuerdo_voto_generales": info_voto,
            "ideologia_autoubicacion": info_ideol,
            "rasgos_politicos": info_rasgos,
            "actitudes_ess": info_ess,
        },
        "personas": tabla.height,
        "sha256": sha256_file(destino),
    }
    (d / "politics_metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1, default=str), "utf-8"
    )
    return meta
