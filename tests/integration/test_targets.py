"""Tests de integración sobre `data/processed/targets/` (F3). Se omiten si no hay objetivos."""

from __future__ import annotations

import pytest

from sinpop.targets import checks, run

pytestmark = pytest.mark.skipif(
    not (run.DESTINO / "metadata.json").exists(), reason="sin objetivos construidos"
)


@pytest.fixture(scope="module")
def fs():
    return checks.ficheros()


def test_g31_totales(fs) -> None:
    assert checks.g31_totales(fs) == []


def test_g32_coherencia(fs) -> None:
    assert checks.g32_coherencia(fs) == []


def test_g33_ccaa_suman_espana(fs) -> None:
    assert checks.g33_ccaa_suman_espana(fs) == []


def test_g35_metadatos(fs) -> None:
    assert checks.g35_metadatos(fs) == []


def test_g36_electorales(fs) -> None:
    malos, difs = checks.g36_electorales(fs)
    assert malos == []
    assert abs(difs["ES"]) < checks.UMBRAL_DERECHO_VOTO


def test_sin_valores_negativos(fs) -> None:
    for t, df in fs.items():
        assert df.filter(df["valor"] < 0).height == 0, t
