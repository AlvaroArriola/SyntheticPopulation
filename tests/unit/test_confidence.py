"""Piezas del modelo de confianza (F10) que no necesitan microdatos."""

from __future__ import annotations

import numpy as np
import polars as pl

from sinpop.config import load_config
from sinpop.confidence import modelo as M


def test_umbral_de_acierto_coincide_con_thresholds() -> None:
    assert load_config("thresholds.yaml").v_conf_ece.tvd_acierto == M.UMBRAL_TVD


def test_ece_cero_si_perfecta_y_alta_si_sobreconfiada() -> None:
    conf = np.array([0.0] * 50 + [1.0] * 50)
    acierto = np.array([0.0] * 50 + [1.0] * 50)
    assert M.ece(conf, acierto) == 0.0
    assert M.ece(np.full(100, 0.9), np.zeros(100)) > 0.85


def _sintetico(n: int, seed: int) -> pl.DataFrame:
    rng = np.random.default_rng(seed)
    d = {s: rng.uniform(0, 1, n) for s in M.SENALES}
    d["log_n_datos"] = rng.uniform(3, 10, n)
    d["es_subgrupo"] = rng.integers(0, 2, n)
    # el error baja con los datos y sube con el desacuerdo
    tvd = 0.25 - 0.02 * d["log_n_datos"] + 0.1 * d["desacuerdo_analogas"]
    d["tvd"] = np.clip(tvd + rng.normal(0, 0.02, n), 0, 1)
    d["id"] = np.arange(n) // 3
    return pl.DataFrame(d)


def test_confianza_monotona_en_los_datos_del_subgrupo() -> None:
    m = M.ModeloConfianza().ajustar(_sintetico(600, 0))
    base = _sintetico(1, 1)
    rejilla = pl.concat([base.with_columns(pl.lit(v).alias("log_n_datos")) for v in range(3, 11)])
    c = m.predecir(rejilla)["confianza"].to_numpy()
    assert np.all(np.diff(c) >= -1e-12)
    assert c[-1] > c[0]
