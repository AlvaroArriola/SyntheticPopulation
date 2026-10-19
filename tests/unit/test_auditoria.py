"""Umbral del perfil de los grupos vigilados con referencia de encuesta (D-052)."""

import numpy as np
import polars as pl

from sinpop.audit import auditoria as A
from sinpop.audit import referencias as R
from sinpop.validate import metrics as M


def _encuesta(n: int, semilla: int = 1) -> pl.DataFrame:
    rng = np.random.default_rng(semilla)
    return pl.DataFrame(
        {
            "sexo": rng.choice(["hombre", "mujer"], n),
            "peso": rng.uniform(50, 150, n),
            "hogar": rng.integers(0, n // 2, n),
        }
    )


def test_replicas_suman_uno_y_categorias():
    cats, reps = R._replicas_perfil(_encuesta(200), "sexo", "peso", "hogar")
    assert cats == ["hombre", "mujer"]
    assert reps.shape == (200, 2)
    assert np.allclose(reps.sum(axis=1), 1.0)


def test_umbral_encuesta_crece_al_bajar_la_muestra():
    j = pl.DataFrame({"categoria": ["hombre", "mujer"], "p_ref": [0.5, 0.5]})
    pequena = A.tvd_ref_encuesta(
        j, R._replicas_perfil(_encuesta(60), "sexo", "peso", "hogar"), 5000, 95
    )
    grande = A.tvd_ref_encuesta(
        j, R._replicas_perfil(_encuesta(20000), "sexo", "peso", "hogar"), 5000, 95
    )
    # con una encuesta enorme, se acerca al de una sola muestra de la población
    assert grande < pequena
    assert grande >= M.tvd_ref([0.5, 0.5], 5000) * 0.8


def test_categoria_ausente_en_las_replicas():
    j = pl.DataFrame({"categoria": ["hombre", "mujer", "otra"], "p_ref": [0.5, 0.5, 0.0]})
    cats, reps = R._replicas_perfil(_encuesta(200), "sexo", "peso", "hogar")
    assert A.tvd_ref_encuesta(j, (cats, reps), 1000, 95) > 0
