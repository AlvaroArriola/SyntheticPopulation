"""Derecho a voto (F8B, tarea 1; `02_datos_y_variables.md` §3.5) (D-067).

En la fecha de referencia de la capa (30/06/2026):

- generales y autonómicas: nacionalidad española y 18 años o más;
- europeas: nacionalidad española o de otro país de la UE (los ciudadanos de la UE votan si se
  inscriben en el censo; la inscripción no se conoce, así que este es el derecho **potencial**);
- municipales: española, de la UE o de un país con acuerdo de reciprocidad identificable en la
  población (Colombia, Ecuador, Perú, Paraguay y Reino Unido entre las nacionalidades que se
  distinguen; Bolivia, Chile, Cabo Verde, Corea, Islandia, Noruega, Nueva Zelanda y Trinidad y
  Tobago no se distinguen). También es potencial: exige años de residencia e inscripción.

En una elección pasada (`elegible`), la edad se lleva a la fecha de esa elección. La población
tiene la edad cumplida a 1 de enero de 2026, no la fecha de nacimiento: quien tenía `a` años
nació entre el 2 de enero de `2025 − a` y el 1 de enero de `2026 − a`. Si la mayoría de edad en
la elección cae dentro de ese año, se sortea con la fracción de días (nacimientos uniformes en
el año). La nacionalidad es la actual: quien se nacionalizó después de la elección figura con
derecho a voto (no se conoce la fecha de nacionalización; limitación documentada en D-067).
"""

from __future__ import annotations

import datetime as dt

import numpy as np
import polars as pl

FECHA_POBLACION = dt.date(2026, 1, 1)
FECHA_REFERENCIA = dt.date(2026, 6, 30)
UE = {"ue"}  # nacionalidad_grupo
RECIPROCIDAD = {"colombia", "ecuador", "peru", "paraguay", "reino_unido"}  # nacionalidad_top


def fraccion_mayor_de_edad(edad_2026: int, fecha: dt.date) -> float:
    """Probabilidad de que una persona con `edad_2026` años a 1/1/2026 tuviera 18 o más en
    `fecha` (nacimientos uniformes dentro de su año de nacimiento)."""
    inicio = dt.date(2025 - edad_2026, 1, 2)
    fin = dt.date(2026 - edad_2026, 1, 1)
    limite = dt.date(fecha.year - 18, fecha.month, fecha.day)  # nacido como muy tarde ese día
    if limite >= fin:
        return 1.0
    if limite < inicio:
        return 0.0
    return ((limite - inicio).days + 1) / ((fin - inicio).days + 1)


def elegible(persons: pl.DataFrame, fecha: dt.date, rng: np.random.Generator) -> np.ndarray:
    """Derecho a voto en unas generales o autonómicas celebradas en `fecha`."""
    edad = persons["edad"].to_numpy()
    espanol = (persons["nacionalidad_esp_ext"] == "espanola").to_numpy()
    p = np.array([fraccion_mayor_de_edad(int(a), fecha) for a in range(0, 121)])
    prob = p[np.clip(edad, 0, 120)]
    u = rng.random(len(edad))
    return espanol & (u < prob)


def derechos_actuales(persons: pl.DataFrame) -> pl.DataFrame:
    mayor = pl.col("edad") >= 18
    esp = pl.col("nacionalidad_esp_ext") == "espanola"
    ue = pl.col("nacionalidad_grupo").is_in(sorted(UE))
    recip = pl.col("nacionalidad_top").is_in(sorted(RECIPROCIDAD))
    return persons.select(
        "person_id",
        (mayor & esp).alias("derecho_voto_generales"),
        (mayor & (esp | ue)).alias("derecho_voto_europeas"),
        (mayor & (esp | ue | recip)).alias("derecho_voto_municipales"),
    )
