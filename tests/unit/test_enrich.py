"""Tests del hot-deck del enriquecimiento (D-044, D-045)."""

from __future__ import annotations

import numpy as np
import polars as pl

from sinpop.enrich import fuentes as F
from sinpop.enrich import hotdeck as HD
from sinpop.repro import make_rng


def _donantes() -> pl.DataFrame:
    # dos celdas (a, b); en «a», el valor 1 pesa 3 veces más que el 0
    return pl.DataFrame(
        {
            "k": ["a"] * 20 + ["b"] * 20,
            "g": ["x"] * 40,
            "v": [1] * 10 + [0] * 10 + [5] * 20,
            "w": [3.0] * 10 + [1.0] * 10 + [1.0] * 20,
        }
    )


def test_reproduce_la_distribucion_ponderada_de_la_celda() -> None:
    r = pl.DataFrame({"k": ["a"] * 20_000, "g": ["x"] * 20_000})
    a = HD.emparejar(r, _donantes(), [["k"], []], "w", make_rng(1), k_min=5)
    v = _donantes()["v"].to_numpy()[a.donante]
    assert set(v) <= {0, 1}
    assert abs(v.mean() - 0.75) < 0.02
    assert (a.nivel == 0).all()


def test_colapsa_si_la_celda_no_tiene_donantes_suficientes() -> None:
    r = pl.DataFrame({"k": ["c", "a"], "g": ["x", "x"]})
    a = HD.emparejar(r, _donantes(), [["k"], []], "w", make_rng(1), k_min=5)
    assert list(a.nivel) == [1, 0]


def test_llave_desconocida_no_se_usa() -> None:
    r = pl.DataFrame({"k": ["NC"] * 1000, "g": ["x"] * 1000})
    a = HD.emparejar(r, _donantes(), [["k"], []], "w", make_rng(1), k_min=5)
    assert (a.nivel == 0).all()  # celda sin la llave k, no colapso
    assert set(_donantes()["k"].to_numpy()[a.donante]) == {"a", "b"}


def test_llave_fija_no_se_quita_nunca() -> None:
    r = pl.DataFrame({"k": ["b"] * 50, "g": ["x"] * 50})
    a = HD.emparejar(r, _donantes(), [["g"], []], "w", make_rng(1), fijas=["k"], k_min=5)
    assert set(_donantes()["k"].to_numpy()[a.donante]) == {"b"}


def test_determinista_con_la_semilla() -> None:
    r = pl.DataFrame({"k": ["a", "b"] * 500, "g": ["x"] * 1000})
    a1 = HD.emparejar(r, _donantes(), [["k"]], "w", make_rng(7), k_min=5)
    a2 = HD.emparejar(r, _donantes(), [["k"]], "w", make_rng(7), k_min=5)
    assert np.array_equal(a1.donante, a2.donante)


def test_niveles_nucleo_conserva_la_geografia_con_el_nucleo() -> None:
    nv = HD.niveles_nucleo(["a", "b", "c"], ["ccaa", None], 2)
    assert nv == [
        ["ccaa", "a", "b", "c"],
        ["ccaa", "a", "b"],
        ["a", "b", "c"],
        ["a", "b"],
        ["ccaa", "a"],
        ["a"],
        ["ccaa"],
        [],
    ]


def test_grupos_de_edad_y_quintil() -> None:
    d = pl.DataFrame(
        {"edad": [15, 16, 24, 25, 90], "renta_hogar_decil": ["D01", "D02", "D03", "D10", "NP"]}
    )
    g = d.select(F.grupo_edad(pl.col("edad"), F.EDAD_10, "e"), F.quintil())
    assert g["e"].to_list() == ["NP", "16", "16", "25", "75"]
    assert g["renta_quintil"].to_list() == ["Q1", "Q1", "Q2", "Q5", "NP"]


def test_tenencia_compatible_con_el_censo() -> None:
    # el 4 de la ECV (alquiler inferior al de mercado) cabe en «alquiler» y en «otro»
    assert F.TENENCIA_COMPATIBLE["alquiler_inferior"] == ["alquiler", "otro"]
    assert all(v for v in F.TENENCIA_COMPATIBLE.values())
