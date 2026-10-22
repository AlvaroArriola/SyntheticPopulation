"""Datos de la población (D-077), informe PDF (D-078) y asistente de tamaño (D-079)."""

from __future__ import annotations

import polars as pl
import pytest
import yaml

from sinpop import CONFIGS_DIR
from sinpop.predict import atributos as A


def _personas() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "es_adulto": [True, True, True, True, False],
            "peso": [1.0, 1.0, 2.0, 1.0, 1.0],
            "salud_autopercibida": ["buena", "mala", "buena", "NC", "buena"],
            "salud_autopercibida__calidad": ["emparejada"] * 4 + ["emparejada"],
            "teletrabajo": ["NP", "nunca", "habitual", "NP", "NP"],
            "edad_4": ["18-34", "65+", "18-34", "35-49", "NP"],
            "sexo": ["mujer", "hombre", "mujer", "hombre", "mujer"],
            "estudios_3": ["superior"] * 5,
            "ccaa": ["13"] * 5,
        }
    )


def test_catalogo_coherente_con_variables() -> None:
    var = yaml.safe_load((CONFIGS_DIR / "variables.yaml").read_text("utf-8"))["variables"]
    for v, c in A.catalogo().items():
        assert v in var
        # cada categoría documentada tiene etiqueta legible
        assert set(map(str, var[v]["categorias"])) <= set(c["etiquetas"]), v
        assert c["fuentes"], v


def test_distribucion_ponderada_sin_menores_ni_np() -> None:
    d = A.calcular("salud_autopercibida", _personas())
    t = {k: v["p"] for k, v in d["total"].items()}
    # adultos: buena 1+2, mala 1, NC 1 → 3/5, 1/5, 1/5; el menor no cuenta
    assert t["buena"] == pytest.approx(0.6) and t["mala"] == pytest.approx(0.2)
    assert t["NC"] == pytest.approx(0.2)  # «No contesta» es una categoría legítima
    assert sum(t.values()) == pytest.approx(1.0)
    assert d["cuota_universo"] == 1.0 and d["procedencia"] == {"emparejada": 1.0}
    for v in d["total"].values():
        assert v["ic95"][0] <= v["p"] <= v["ic95"][1]


def test_universo_excluye_no_aplicable() -> None:
    d = A.calcular("teletrabajo", _personas())
    assert d["personas_universo"] == 2
    assert d["cuota_universo"] == pytest.approx(3 / 5)
    assert d["total"]["habitual"]["p"] == pytest.approx(2 / 3)


def test_buscar_encuentra_y_no_inventa() -> None:
    assert A.buscar("¿Cómo diría que es su estado de salud en general?")[0]["variable"] == (
        "salud_autopercibida"
    )
    assert A.buscar("¿Qué opinión tiene del presidente del Gobierno?") == []


def test_resumen_sale_de_las_cifras() -> None:
    from sinpop.servicio import informe as INF

    r = {
        "total": {
            "Sí": {"p": 0.55, "ic80": [0.5, 0.6], "ic95": [0.48, 0.62]},
            "No": {"p": 0.4, "ic80": [0.35, 0.45], "ic95": [0.33, 0.47]},
            "N.S.": {"p": 0.05, "ic80": [0.03, 0.07], "ic95": [0.02, 0.08]},
        },
        "por_subgrupo": {
            "sexo=hombre": {"Sí": {"p": 0.5}, "No": {"p": 0.45}, "N.S.": {"p": 0.05}},
            "sexo=mujer": {"Sí": {"p": 0.6}, "No": {"p": 0.35}, "N.S.": {"p": 0.05}},
        },
        "confianza": {"total": 0.8, "por_subgrupo": {"sexo=hombre": 0.7, "sexo=mujer": 0.7}},
    }
    f = INF.resumen(INF.normalizar("pregunta", r, {"sexo": {"hombre": "H", "mujer": "M"}}))
    assert f[0].startswith("La respuesta más frecuente es «Sí», con un 55 %")
    assert not any("se solapan" in x for x in f)  # 48-62 % frente a 33-47 %
    assert any("del 50 % (H) al 60 % (M)" in x for x in f)
    assert any(x.startswith("Confianza alta: 80 %") for x in f)


def test_informe_pdf_se_genera() -> None:
    pytest.importorskip("matplotlib")
    from sinpop.servicio import informe as INF

    d = A.calcular("salud_autopercibida", _personas())
    pdf = INF.generar("dato", {**d, "aviso": "Simulado."}, {"territorio": "CCAA:13"}, {})
    assert pdf.startswith(b"%PDF") and len(pdf) > 5000


def test_margen_de_simulacion() -> None:
    from sinpop.servicio import tamano as T

    # 1,96·√(0,25/n): con 10 000 personas y todo el grupo, ±0,98 puntos
    assert T._margen(10_000, 1.0) == pytest.approx(0.0098, abs=1e-4)
    assert T._margen(10_000, 0.25) == pytest.approx(2 * T._margen(10_000, 1.0))


@pytest.mark.parametrize(
    ("pregunta", "esperado"),
    [
        ("¿Cómo calificaría usted la situación económica actual de España?", None),
        ("¿Cuál es su situación económica personal?", None),
        ("¿Cómo valora la situación política?", None),
        ("¿Cómo valora la sanidad pública?", None),
        ("¿Le preocupa el paro?", None),
        ("¿Cuál es su situación laboral actual?", "relacion_actividad"),
        ("¿Está usted en paro?", "relacion_actividad"),
        ("¿Cuál es su nivel de estudios?", "nivel_estudios"),
        ("¿Cuál es su ocupación?", "ocupacion"),
        ("¿Vive usted de alquiler o en propiedad?", "tenencia_vivienda"),
        ("¿Ha comprado algo por internet en los últimos meses?", "compra_online"),
    ],
)
def test_dato_oficial_solo_cuando_corresponde(pregunta, esperado) -> None:
    """D-081: el parecido de texto no basta («situación económica» no es «situación laboral»)."""
    r = A.buscar(pregunta)
    assert (r[0]["variable"] if r else None) == esperado


def test_fallo_del_llm_cae_al_estimador_sin_llm(monkeypatch) -> None:
    """D-085: si el LLM no da una salida válida, la interfaz recibe la estimación sin LLM con un
    aviso, no un error."""
    from types import SimpleNamespace

    from sinpop.llm import cliente as C
    from sinpop.predict import estimador as E
    from sinpop.predict import poblacion as P
    from sinpop.predict import salida as S

    def falla(*a):
        raise ValueError("el modelo de lenguaje no devolvió una salida válida")

    monkeypatch.setattr(P, "territorio", lambda run_id: "ES")
    monkeypatch.setattr(E, "predecir", lambda p, run_id: SimpleNamespace(analogas=[]))
    monkeypatch.setattr(C, "disponible", lambda: True)
    monkeypatch.setattr(S, "calibracion_llm", lambda: None)
    monkeypatch.setattr(S, "construir_asistida", falla)
    monkeypatch.setattr(S, "construir", lambda r, run_id: {"aviso": "Simulado.", "parametros": {}})
    q = {"id": "x", "tipo": "pregunta", "enunciado": "¿Qué?", "opciones": ["Sí", "No"]}
    out = S.predecir_dict(q, "r")
    assert "no dio una respuesta válida" in out["aviso"]
    assert "ValueError" in out["parametros"]["llm_fallo"]


def test_historial_de_eventos_en_el_paquete(tmp_path, monkeypatch) -> None:
    """D-086: el resultado de un evento lleva su acierto medido; en el paquete sale de un JSON."""
    import json

    from sinpop import paquete as PK
    from sinpop.predict import evento as V

    h = {"con_llm": {"eventos": 16, "eventos_correctos": 8, "error_magnitud_pp": 3.9}}
    (tmp_path / "historial_eventos.json").write_text(json.dumps(h), "utf-8")
    monkeypatch.setattr(PK, "activo", lambda: True)
    monkeypatch.setattr(PK, "ruta", lambda *p: tmp_path.joinpath(*p))
    assert V.historial() == h
