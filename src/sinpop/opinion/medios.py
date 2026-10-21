"""`medio_informacion_principal` (F8A, D-066) desde el estudio 3511 del CIS (Estudio sobre
audiencias de medios de comunicación social II, mayo de 2025, 15.017 entrevistas).

El cuestionario no pregunta por un medio «principal»; se deriva de la frecuencia con que la
persona se informa por cada medio (escala común de las preguntas P.4, P.10, P.15 y P.20A):

- televisión: P.10 (informativos de su canal de referencia), si sigue informativos (P.8 = Sí);
- prensa: P.4 (lectura de su periódico de referencia), si lee periódicos (P.3 = Sí);
- radio: P.15 (escucha de su emisora de referencia), si escucha la radio (P.13 = Sí);
- redes sociales: P.20A, si se informa por redes (P.19 = Sí);
- otros digitales: podcasts, blogs y páginas de vídeos mencionados en P.2 (sin frecuencia).

Puntuación: «Todos o casi todos los días» 5, «Cuatro o cinco días por semana» 4, «Dos o tres
veces por semana» 3, «De vez en cuando» 2, «Nunca o casi nunca» 0. Un medio mencionado en P.2
(«¿A través de qué medios suele informarse?») sin frecuencia vale 1. El medio principal es el
de mayor puntuación; los **empates reparten el peso** del encuestado a partes iguales (no se
elige uno arbitrariamente). Sin ningún medio: «N.S.» o «N.C.» de P.2 → NS o NC; si no menciona
ninguno → `ninguno`.
"""

from __future__ import annotations

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion.valores import COLUMNAS, Modelo, _edad_grupo, perfil_sintetico
from sinpop.repro import make_rng

ESTUDIO = "3511"
FRECUENCIA = {
    "Todos o casi todos los días": 5,
    "Cuatro o cinco días por semana": 4,
    "Dos o tres veces por semana": 3,
    "De vez en cuando": 2,
    "Nunca o casi nunca": 0,
}
MEDIOS = {  # medio: (filtro, frecuencia, mención en P.2)
    "television": ("P8", "P10", "P2_1"),
    "prensa": ("P3", "P4", "P2_2"),
    "radio": ("P13", "P15", "P2_3"),
    "redes_sociales": ("P19", "P20A", "P2_4"),
}
OTROS_DIGITALES = ["P2_5", "P2_6", "P2_7"]  # podcasts, blogs, páginas de vídeos
SIN_DATO = {"N.S.", "N.C.", "No procede", "N.P."}


def _ancho() -> pl.DataFrame:
    vars_ = {v for t in MEDIOS.values() for v in t} | set(OTROS_DIGITALES) | {"P2_98", "P2_99"}
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter((pl.col("estudio") == ESTUDIO) & pl.col("variable").is_in(sorted(vars_)))
        .select("encuestado", "variable", "etiqueta")
        .collect()
    )
    return lg.pivot(on="variable", index="encuestado", values="etiqueta").sort("encuestado")


def puntuaciones(fila: dict) -> dict[str, float]:
    out = {}
    for medio, (filtro, frec, mencion) in MEDIOS.items():
        f = fila.get(frec)
        if fila.get(filtro) == "Sí" and f not in (None, *SIN_DATO):
            if f not in FRECUENCIA:
                raise ValueError(f"{frec}: etiqueta no prevista {f!r}")
            out[medio] = FRECUENCIA[f]
        elif fila.get(mencion) == "Menciona":
            out[medio] = 1
    if any(fila.get(v) == "Menciona" for v in OTROS_DIGITALES):
        out["otros_digitales"] = 1
    return {k: v for k, v in out.items() if v > 0}


def principal(fila: dict) -> list[str]:
    """Medio o medios (empatados) principales del encuestado."""
    p = puntuaciones(fila)
    if p:
        top = max(p.values())
        return sorted(k for k, v in p.items() if v == top)
    if fila.get("P2_98") == "Menciona":
        return ["NS"]
    if fila.get("P2_99") == "Menciona":
        return ["NC"]
    return ["ninguno"]


def datos() -> pl.DataFrame:
    """Encuestados de 3511 con una fila por medio principal y el peso repartido."""
    a = _ancho()
    filas = []
    for fila in a.iter_rows(named=True):
        ms = principal(fila)
        for m in ms:
            filas.append({"encuestado": fila["encuestado"], "medio": m, "fraccion": 1 / len(ms)})
    m = pl.DataFrame(filas)
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet").filter(pl.col("estudio") == ESTUDIO)
    return (
        p.join(m, on="encuestado")
        .filter(
            (pl.col("edad") >= 18)
            & ~pl.col("estudios_3").is_in(["NC", "NS"])
            & ~pl.col("actividad_3").is_in(["NC", "NS"])
        )
        .with_columns(
            (pl.col("peso") / pl.col("peso").mean() * pl.col("fraccion")).alias("peso"),
            pl.col("medio").alias("medio_informacion_principal"),
            _edad_grupo(pl.col("edad")),
        )
        .sort("encuestado", "medio")
    )


def asignar(persons: pl.DataFrame, semilla: int) -> tuple[pl.DataFrame, dict]:
    """El estudio 3511 entrevista a personas de nacionalidad española (ningún extranjero en la
    muestra): extranjeros y residentes en colectivos quedan `extrapolada`, como en D-063."""
    perfil = perfil_sintetico(persons)
    d = datos()
    m = Modelo("medio_informacion_principal", columnas=COLUMNAS).ajustar(d)
    pr = m.probabilidades(perfil)
    u = make_rng(semilla).random(len(pr))
    idx = (pr.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(m.clases) - 1)
    fuera = (perfil["nacionalidad_esp_ext"] != "espanola") | (
        perfil["tipo_residencia"] != "vivienda_familiar"
    )
    calidad = np.where(fuera, "extrapolada", "modelada")
    out = perfil.select("person_id").with_columns(
        pl.Series("medio_informacion_principal", np.array(m.clases)[idx]),
        pl.Series("medio_informacion_principal__calidad", calidad),
    )
    return out, {
        "medio_informacion_principal": {
            "encuestados": d["encuestado"].n_unique(),
            "estudios": [ESTUDIO],
        }
    }
