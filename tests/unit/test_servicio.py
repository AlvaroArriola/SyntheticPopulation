"""Servicio de consulta local (F13): rutas que no necesitan predecir."""

from __future__ import annotations

import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient  # noqa: E402

from sinpop.servicio import app as A  # noqa: E402


@pytest.fixture(scope="module")
def cliente() -> TestClient:
    return TestClient(A.crear_app())


def test_territorios_tiene_comunidades_y_provincias(cliente) -> None:
    g = cliente.get("/api/territorios").json()
    niveles = [f["properties"]["nivel"] for f in g["features"]]
    assert niveles.count("CCAA") == 19 and niveles.count("PROV") == 52


def test_etiquetas_salen_de_la_configuracion(cliente) -> None:
    e = cliente.get("/api/etiquetas").json()
    assert e["ccaa"]["13"].startswith("Madrid") and len(e["provincia"]) == 52
    assert "socialdemocrata" in e["recuerdo_voto_generales_familia"]


def test_poblaciones_y_tamanos(cliente) -> None:
    r = cliente.get("/api/poblaciones").json()
    assert r["tamanos"] == A.TAMANOS
    assert all({"run_id", "territorio", "lista", "capas"} <= set(p) for p in r["poblaciones"])


def test_validacion_de_entradas(cliente) -> None:
    r = cliente.post("/api/poblaciones", json={"territorio": "XX", "tamano": 10_000})
    assert r.status_code == 422
    r = cliente.post("/api/poblaciones", json={"territorio": "PROV:44", "tamano": 12_345})
    assert r.status_code == 422
    q = {"run_id": "no_existe", "enunciado": "¿Algo?", "opciones": ["Sí", "No"]}
    r = cliente.post("/api/preguntas", json=q)
    assert r.status_code == 404
    assert cliente.get("/api/trabajos/desconocido").status_code == 404


def test_run_id_sigue_la_convencion() -> None:
    assert A.run_id("CCAA:13", 100_000) == "2026-01-01_CCAA_13_100000_s1"


def test_la_interfaz_se_sirve(cliente) -> None:
    html = cliente.get("/").text
    assert "España sintética" in html and "vendor/leaflet/leaflet.js" in html
