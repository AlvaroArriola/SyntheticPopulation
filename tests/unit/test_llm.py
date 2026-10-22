"""Capa de LLM (D-071) con un backend simulado: sin red, sin coste."""

from __future__ import annotations

import json

import pytest

from sinpop.llm import cliente as C
from sinpop.llm import prompts as P
from sinpop.predict import asistido as A
from sinpop.predict import estimador as E


@pytest.fixture
def rutas(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "_rutas", lambda: (tmp_path / "cache", tmp_path / "gasto.jsonl"))
    return tmp_path


CLAVES = ["sexo=hombre", "sexo=mujer"]
Q = E.Pregunta("Q1", "¿Está usted de acuerdo?", ["Sí", "No", "N.S."], "nominal", "2026-07", [])


def _ok(_s: dict) -> str:
    d = [0.5, 0.4, 0.1]
    return json.dumps(
        {
            "total": d,
            "subgrupos": [{"clave": k, "distribucion": d} for k in CLAVES],
            "justificacion": "x",
        }
    )


@pytest.fixture(autouse=True)
def poblacion_falsa(monkeypatch):
    monkeypatch.setattr(A, "poblacion_texto", lambda: "- sexo: hombre 48 %; mujer 52 %")


def test_prompts_versionados_cargan_y_renderizan() -> None:
    for id_ in ["b2@v1", "pregunta_nueva@v1", "evento@v1"]:
        p = P.cargar(id_)
        assert p.sistema and p.usuario and len(p.sha256) == 64


def test_cache_evita_pagar_dos_veces(rutas) -> None:
    b = C.SimuladoBackend(_ok)
    p = A.peticion_b2(Q, CLAVES)
    s1 = C.ejecutar([p], b)
    s2 = C.ejecutar([p], b)
    assert s1 == s2 and b.llamadas == 1
    lineas = (rutas / "gasto.jsonl").read_text().splitlines()
    assert len(lineas) == 1 and json.loads(lineas[0])["eur"] > 0


def test_salida_invalida_se_reintenta_y_acaba_en_none(rutas) -> None:
    malo = json.dumps({"total": [0.9, 0.9, 0.9], "subgrupos": [], "justificacion": "x"})
    b = C.SimuladoBackend(lambda s: malo)
    out = C.ejecutar([A.peticion_b2(Q, CLAVES)], b)
    assert out["b2:Q1"] is None
    assert b.llamadas == 1 + C._cfg().reintentos_salida_invalida


def test_presupuesto_bloquea_antes_de_enviar(rutas, monkeypatch) -> None:
    base = C._cfg()
    pres = base.presupuesto.model_copy(update={"eur_max_por_ejecucion": 1e-6})
    cfg = base.model_copy(update={"presupuesto": pres})
    monkeypatch.setattr(C, "_cfg", lambda: cfg)
    b = C.SimuladoBackend(_ok)
    with pytest.raises(C.PresupuestoExcedido):
        C.ejecutar([A.peticion_b2(Q, CLAVES)], b)
    assert b.llamadas == 0


def test_sin_activar_no_hay_llm(monkeypatch) -> None:
    monkeypatch.setenv("SINPOP_ANTHROPIC_API_KEY", "x")
    assert C._cfg().activo is False
    assert not C.disponible()
    with pytest.raises(C.LLMNoDisponible):
        C.ejecutar([A.peticion_b2(Q, CLAVES)])


def test_distribuciones_normalizadas() -> None:
    d = A.distribuciones(json.loads(_ok({})))
    assert set(d) == {"total", *CLAVES}
    assert all(abs(v.sum() - 1) < 1e-12 for v in d.values())


def test_coste_con_descuento_de_lotes() -> None:
    lleno = C.coste_eur("claude-opus-5-5", 1_000_000, 1_000_000, lote=False)
    lote = C.coste_eur("claude-opus-5-5", 1_000_000, 1_000_000, lote=True)
    assert lleno == pytest.approx(24.0) and lote == pytest.approx(12.0)


def test_exportar_y_enviar_desde_otra_sesion(rutas, monkeypatch) -> None:
    monkeypatch.setattr(C, "PENDIENTES_DIR", rutas / "pendientes")
    p = A.peticion_b2(Q, CLAVES)
    info = C.exportar([p], "prueba")
    assert info["peticiones"] == 1
    # la «otra sesión» envía el fichero y deja la respuesta en la caché
    r = C.enviar_pendientes("prueba", C.SimuladoBackend(_ok))
    assert r["validas"] == 1
    # aquí, sin backend ni credenciales, la respuesta sale de la caché y vuelve a validarse
    monkeypatch.delenv("SINPOP_ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    assert C.ejecutar([p])["b2:Q1"]["total"] == [0.5, 0.4, 0.1]
    assert C.exportar([p], "prueba")["peticiones"] == 0
