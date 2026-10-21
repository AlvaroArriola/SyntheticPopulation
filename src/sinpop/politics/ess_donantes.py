"""Implicación, participación, confianza y satisfacción desde la ESS (F8B, tarea 5) (D-067).

`02_datos_y_variables.md` §3.5 pone en la ESS el interés por la política, la participación no
electoral, la confianza en las instituciones y la satisfacción con la democracia. Para conservar
la relación entre ellas (quien se manifiesta suele estar interesado y desconfiar de los partidos),
se asignan **juntas** por emparejamiento (hot-deck, como en F6): cada persona sintética recibe el
vector de un encuestado de la ESS (España, ronda 11) sorteado con su peso dentro de su celda:

- grupo de voto en las generales de 2023 (el recuerdo calibrado; blanco, nulo y otros juntos;
  quienes no tenían edad o derecho, con los «Not eligible to vote» de la ESS);
- grupo de edad (cuatro) y estudios (tres).

Si la celda tiene menos de `MIN_DONANTES`, se relaja a voto × edad y después a voto. Los
encuestados de la ESS que no dicen su voto (rechazo, no sabe) no son donantes: su voto no se
conoce. Todo lo copiado se marca `emparejada`.
"""

from __future__ import annotations

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion.ess import CONFIANZA_INSTITUCIONES, PARTICIPACION

MIN_DONANTES = 10
GRUPO = {
    "izquierda_estatal": "izquierda_estatal",
    "socialdemocrata": "socialdemocrata",
    "centro_derecha_estatal": "centro_derecha_estatal",
    "derecha_radical": "derecha_radical",
    "nacionalista_regionalista": "nacionalista_regionalista",
    "otros": "otros_blanco_nulo",
    "blanco": "otros_blanco_nulo",
    "nulo": "otros_blanco_nulo",
    "abstencion": "abstencion",
    "no_tenia_edad": "sin_derecho",
    "sin_derecho_voto": "sin_derecho",
}
VARIABLES = (
    ["interes_politica", "satisfaccion_democracia"]
    + [f"confianza_{n}" for n in CONFIANZA_INSTITUCIONES.values()]
    + [f"participacion_{n}" for n in PARTICIPACION.values()]
)


def _edad4(e: pl.Expr) -> pl.Expr:
    return (
        pl.when(e < 35)
        .then(pl.lit("18-34"))
        .when(e < 50)
        .then(pl.lit("35-49"))
        .when(e < 65)
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
    )


def donantes() -> pl.DataFrame:
    d = pl.read_parquet(INTERIM_DIR / "ess_es.parquet")
    return (
        d.filter(pl.col("voto_generales_2023").is_in(list(GRUPO)))
        .with_columns(
            pl.col("voto_generales_2023").replace_strict(GRUPO).alias("grupo_voto"),
            _edad4(pl.col("edad")).alias("edad_4"),
        )
        .sort("encuestado")
    )


def asignar(
    persons: pl.DataFrame, voto: pl.DataFrame, rng: np.random.Generator
) -> tuple[pl.DataFrame, dict]:
    s = (
        persons.select("person_id", "edad", "estudios_3", "tipo_residencia")
        .join(voto.select("person_id", "recuerdo_voto_generales"), on="person_id")
        .with_columns(
            pl.col("recuerdo_voto_generales").replace_strict(GRUPO).alias("grupo_voto"),
            _edad4(pl.col("edad")).alias("edad_4"),
        )
    )
    d = donantes()
    niveles = [["grupo_voto", "edad_4", "estudios_3"], ["grupo_voto", "edad_4"], ["grupo_voto"]]
    idx_donante = np.full(s.height, -1)
    nivel_usado = np.full(s.height, -1)
    pendiente = np.ones(s.height, dtype=bool)
    w = d["peso"].to_numpy()
    for k, claves in enumerate(niveles):
        grupos_d = {
            key: np.asarray(g["_i"].to_numpy())
            for key, g in d.with_row_index("_i").group_by(claves)
        }
        s_pend = s.with_row_index("_j").filter(pl.Series(pendiente))
        for key, g in s_pend.group_by(claves):
            cand = grupos_d.get(key)
            if cand is None or len(cand) < MIN_DONANTES:
                continue
            j = g["_j"].to_numpy()
            p = w[cand] / w[cand].sum()
            idx_donante[j] = rng.choice(cand, size=len(j), p=p)
            nivel_usado[j] = k
            pendiente[j] = False
    if pendiente.any():
        raise ValueError(f"{pendiente.sum()} personas sin donante de la ESS")
    copia = d.select(VARIABLES)[idx_donante]
    out = s.select("person_id").hstack(copia)
    for v in VARIABLES:
        out = out.with_columns(pl.lit("emparejada").alias(f"{v}__calidad"))
    usados = np.bincount(nivel_usado, minlength=3)
    return out, {
        "donantes": d.height,
        "por_nivel": dict(
            zip(["voto_edad_estudios", "voto_edad", "voto"], usados.tolist(), strict=True)
        ),
        "donantes_distintos": int(len(np.unique(idx_donante))),
    }
