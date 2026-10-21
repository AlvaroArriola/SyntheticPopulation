"""Autoubicación ideológica (F8B, tarea 5; `03_arquitectura.md` §2.5, punto 4) (D-067).

`ESCIDEOL` de los mismos estudios del CIS que el recuerdo de voto: escala 1 (izquierda) a 10
(derecha) con N.S. y N.C. como opciones. El fichero solo etiqueta los extremos («1 Izquierda»,
«10 Derecha»); los códigos intermedios se aceptan entre los dos extremos etiquetados
(`latentes._intermedios_numericos`).

Modelo multinomial (las doce opciones) con el perfil, la religiosidad, la clase subjetiva y el
**recuerdo de voto** del encuestado (ya armonizado), y extracción para cada persona sintética
con su recuerdo asignado: así la ideología es coherente con el voto sin fijarla (no todos los
votantes de un partido se colocan igual, `06_sesgos_y_minorias.md` §6.2).
"""

from __future__ import annotations

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion.latentes import _intermedios_numericos
from sinpop.opinion.valores import COLUMNAS, Modelo, perfil_sintetico
from sinpop.politics import recuerdo as RV

OPCIONES = [str(i) for i in range(1, 11)] + ["NS", "NC"]
COLUMNAS_IDEOLOGIA = COLUMNAS + ["religiosidad", "clase_subjetiva", "recuerdo"]
NS_NC = {"N.S.": "NS", "N.C.": "NC"}


def respuestas() -> pl.DataFrame:
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter(pl.col("variable") == "ESCIDEOL")
        .select("estudio", "encuestado", "variable", "codigo", "etiqueta")
        .collect()
    )
    lg = _intermedios_numericos(lg, {"ESCIDEOL": "numerica"})

    def valor(et: str | None) -> str | None:
        if et is None:
            return None
        et = et.strip()
        if et in NS_NC:
            return NS_NC[et]
        n = et.split(" ")[0]
        if n.isdigit() and 1 <= int(n) <= 10:
            return n
        if et in ("No procede", "N.P."):
            return None
        raise ValueError(f"ESCIDEOL: etiqueta no prevista {et!r}")

    return (
        lg.with_columns(
            pl.col("etiqueta").map_elements(valor, return_dtype=pl.Utf8).alias("ideologia")
        )
        .select("estudio", "encuestado", "ideologia")
        .drop_nulls()
    )


def datos() -> pl.DataFrame:
    d = RV.datos().filter(pl.col("recuerdo").is_in(RV.OPCIONES))
    return d.join(respuestas(), on=["estudio", "encuestado"])


def asignar(
    persons: pl.DataFrame, opinion: pl.DataFrame, voto: pl.DataFrame, rng: np.random.Generator
) -> tuple[pl.DataFrame, dict]:
    """Quienes tienen un voto de 2023 (familia, blanco, nulo o abstención) reciben la ideología
    condicionada a ese voto. Quienes no tenían edad o derecho a voto no tienen recuerdo, y se
    les asigna con el mismo modelo ajustado sin el recuerdo (solo perfil y valores)."""
    perfil = (
        perfil_sintetico(persons)
        .join(opinion.select("person_id", "religiosidad", "clase_subjetiva"), on="person_id")
        .join(
            voto.select("person_id", pl.col("recuerdo_voto_generales").alias("recuerdo")),
            on="person_id",
        )
    )
    d = datos()
    m = Modelo("ideologia", columnas=COLUMNAS_IDEOLOGIA).ajustar(d)
    m0 = Modelo("ideologia", columnas=COLUMNAS + ["religiosidad", "clase_subjetiva"]).ajustar(d)
    con_voto = perfil["recuerdo"].is_in(RV.OPCIONES).to_numpy()
    pr = np.where(con_voto[:, None], m.probabilidades(perfil), m0.probabilidades(perfil))
    u = rng.random(len(pr))
    idx = (pr.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(m.clases) - 1)
    out = perfil.select("person_id").with_columns(
        pl.Series("ideologia_autoubicacion", np.array(m.clases)[idx])
    )
    return out, {
        "encuestados": d.height,
        "estudios": sorted(d["estudio"].unique()),
        "c": m.c_elegido,
    }
