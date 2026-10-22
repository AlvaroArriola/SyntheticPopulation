"""La fecha de corte de construcción es una sola (D-003, D-069; guía de actualización mensual).

Varias capas la llevan como constante. Este test falla si al mover el corte se olvida alguna:
todas tienen que coincidir con `fecha_corte_construccion` de `configs/llm.yaml`, que además es la
fecha con la que se comprueba la contaminación de los modelos de lenguaje.
"""

from __future__ import annotations

import datetime as dt

import yaml

from sinpop import CONFIGS_DIR
from sinpop.config import load_config


def test_todas_las_capas_usan_el_mismo_corte() -> None:
    from sinpop.opinion import cis
    from sinpop.opinion import run as opinion_run
    from sinpop.politics import derecho, recuerdo
    from sinpop.politics import run as politics_run

    fin = load_config("llm.yaml").fecha_corte_construccion  # último día con datos
    corte = fin + dt.timedelta(days=1)  # primer día excluido
    assert cis.CORTE == corte
    assert recuerdo.CORTE == corte
    assert derecho.FECHA_REFERENCIA == fin
    assert opinion_run.FECHA_REFERENCIA == fin.isoformat()
    assert politics_run.FECHA_REFERENCIA == fin.isoformat()
    periodo = yaml.safe_load((CONFIGS_DIR / "temporal.yaml").read_text("utf-8"))["periodo"]
    assert periodo["hasta"] == fin.isoformat()[:7]


def test_la_ventana_de_validacion_es_posterior_al_corte() -> None:
    from sinpop.evaluate import validacion as V

    fin = load_config("llm.yaml").fecha_corte_construccion
    fechas = list(V.VALIDACION.values()) + list(V.EVALUACION_FINAL.values())
    assert all(dt.date.fromisoformat(f) > fin for f in fechas)
