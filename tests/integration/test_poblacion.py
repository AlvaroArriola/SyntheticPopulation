"""Tests de integración de F4: población nacional pequeña desde la calibración guardada.

Se omiten si no hay calibración nacional en `data/processed/calibracion/` (se crea con
`python -m sinpop.validate.fase4` o `sinpop build`). Comprueban, para N = 5.000: reproducibilidad
por hash (V-REPRO), reglas duras (V-REGLAS), separación de capas, metadatos y que las marginales
calibradas están dentro de V-MARG.
"""

from __future__ import annotations

import json

import polars as pl
import pytest

from sinpop.synth import poblacion as PB
from sinpop.validate import poblacion as V
from sinpop.validate.layers import layer_violations

CAL = PB.CALIBRACION_DIR / f"ES_{PB.METODO}.json"
pytestmark = pytest.mark.skipif(not CAL.exists(), reason="sin calibración nacional")


@pytest.fixture(scope="module")
def construida(tmp_path_factory):
    u = PB.unidades_todas()
    a = tmp_path_factory.mktemp("a")
    b = tmp_path_factory.mktemp("b")
    ma = PB.construir("ES", 5000, 11, u=u, destino=a)
    mb = PB.construir("ES", 5000, 11, u=u, destino=b)
    mc = PB.construir("ES", 5000, 12, u=u, destino=b)
    return a, ma, mb, mc


def test_repro_mismo_hash(construida) -> None:
    _, ma, mb, mc = construida
    assert ma["sha256"] == mb["sha256"]
    assert ma["sha256"]["persons.parquet"] != mc["sha256"]["persons.parquet"]


def test_reglas_duras_y_capas(construida) -> None:
    a, ma, _, _ = construida
    p = pl.read_parquet(a / ma["run_id"] / "persons.parquet")
    assert V.v_reglas_duras(p)["violaciones"].sum() == 0
    assert layer_violations(p.columns) == []
    assert p["person_id"].n_unique() == p.height
    assert abs(p.height - 5000) < 50
    assert (p["peso"] == 1).all()


def test_metadatos(construida) -> None:
    a, ma, _, _ = construida
    meta = json.loads((a / ma["run_id"] / "metadata.json").read_text(encoding="utf-8"))
    for k in ("semilla", "fuentes", "version_codigo", "sha256", "objetivos_calibrados"):
        assert meta[k]
    assert "nacionalidad_top" in meta["objetivos_calibrados"]
    assert "voto_generales_2023" not in meta["objetivos_calibrados"]


def test_v_marg_espana(construida) -> None:
    a, ma, _, _ = construida
    p = V.preparar(pl.read_parquet(a / ma["run_id"] / "persons.parquet"))
    vm = V.v_marg(p, "ES")
    assert vm.filter(pl.col("nivel") == "espana")["ok"].all()
