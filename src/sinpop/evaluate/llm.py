"""Evaluación de la capa de LLM (B2, preguntas nuevas, modo evento y G9.7) (D-071).

Se ejecuta una vez sobre la ventana de validación (`validacion.VALIDACION`) y, en F11, sobre la de
evaluación final, con las mismas métricas que el componente estadístico:

- **B2** en todas las preguntas evaluables: TVD en total, por subgrupo (edad, sexo, estudios) y por
  comunidad.
- **Pregunta nueva** (LLM anclado) en las preguntas sin análogas fiables (similitud < `UMBRAL` o
  ninguna alineable), frente al componente estadístico en las mismas preguntas cuando lo hay.
  Con la ventana de validación se calibran los intervalos y la confianza de esas salidas
  (`salida.CALIBRACION_LLM`), y se decide si el LLM se usa (`usar`: solo si mejora al
  componente estadístico donde ambos existen).
- **Modo evento** con LLM (`evento.backtest_llm`): contaminado, ver allí.
- **G9.7** (`docs/06` §5):
  - **prueba contrafactual** adaptada a distribuciones: la brecha entre grupos del LLM frente a
    la del modelo estadístico (V-LLM-ESTEREOTIPO);
  - **homogeneidad:** no aplica (no se simulan personas, D-069);
  - **auditoría de justificaciones:** todas se guardan para revisarlas
    (`reports/fase_09/llm_justificaciones.csv`).

Antes de gastar nada: `python -m sinpop.evaluate.llm --estimar`.
Comando: `python -m sinpop.evaluate.llm`.
"""

from __future__ import annotations

import json
import sys
from itertools import combinations

import numpy as np
import polars as pl

from sinpop import REPORTS_DIR
from sinpop.evaluate import validacion as V
from sinpop.llm import cliente as C
from sinpop.predict import asistido as A
from sinpop.predict import estimador as E
from sinpop.predict import opciones as O
from sinpop.predict import salida as S

DESTINO = REPORTS_DIR / "fase_09_llm.json"
DETALLE = REPORTS_DIR / "fase_09"
DIMENSIONES = ["edad_4", "sexo", "estudios_3"]


def casos(estudios: dict[str, str]) -> list[dict]:
    """Preguntas evaluables con su verdad (agregada) y la predicción estadística."""
    out = []
    for estudio, fecha in estudios.items():
        p, lg, banco = V._cargar(estudio, fecha)
        for q in V.preguntas(banco, estudio, fecha):
            d = V.verdad(p, lg, q["variable"], q["opciones"])
            if d.height < 200:
                continue
            escala = O.escala_probable(q["opciones"])
            pq = E.Pregunta(
                q["id"], q["enunciado"], q["opciones"], escala, q["mes"], A.SUBGRUPOS_LLM
            )
            r = E.predecir(pq)
            sim = r.analogas[0]["similitud"] if r.analogas else None
            out.append({"q": q, "pq": pq, "verdad": d, "r": r, "similitud": sim})
    return out


def peticiones(cs: list[dict]) -> list:
    claves = A.claves_subgrupo()
    pets = [A.peticion_b2(c["pq"], claves) for c in cs]
    pets += [
        A.peticion_nueva(c["pq"], claves)
        for c in cs
        if c["similitud"] is None or c["similitud"] < A.UMBRAL
    ]
    return pets


def _grupos(d: pl.DataFrame, g: str, opciones: list[str]) -> dict[str, np.ndarray]:
    return {
        f"{g}={lv[0]}": V._dist(dg, opciones)
        for lv, dg in d.group_by(g)
        if dg.height >= V.MIN_CASOS_GRUPO
    }


def _tvd_grupos(pred: dict[str, np.ndarray], d: pl.DataFrame, dims: list[str], ops) -> float | None:
    e = [V.tvd(pred[k], y) for g in dims for k, y in _grupos(d, g, ops).items() if k in pred]
    return float(np.mean(e)) if e else None


def brecha(dist: dict[str, np.ndarray], g: str) -> float | None:
    """TVD máxima entre los niveles de una dimensión."""
    v = [x for k, x in dist.items() if k.startswith(f"{g}=")]
    return max((V.tvd(a, b) for a, b in combinations(v, 2)), default=None)


def _conformal(res: np.ndarray, nivel: float) -> float:
    n = len(res)
    return float(np.quantile(res, min(1.0, np.ceil((n + 1) * nivel) / n)))


def ejecutar(
    estudios: dict[str, str] | None = None,
    backend=None,
    calibrar: bool = True,
    eventos: bool = True,
    destino=DESTINO,
) -> dict:
    from sinpop.config import load_config

    estudios = V.VALIDACION if estudios is None else estudios
    cs = casos(estudios)
    salidas = C.ejecutar(peticiones(cs), backend)
    filas, contra, justif, residuos = [], [], [], []
    for c in cs:
        q, d, r = c["q"], c["verdad"], c["r"]
        ops = q["opciones"]
        y = V._dist(d, ops)
        f = {
            "id": q["id"],
            "politica": q["politica"],
            "similitud_max": c["similitud"],
            "tvd_sistema_cis": V.tvd(r.sistema_cis["total"], y) if r.analogas else None,
        }
        b2 = salidas.get(f"b2:{q['id']}")
        if b2 is not None:
            dist = A.distribuciones(b2)
            f["tvd_b2"] = V.tvd(dist["total"], y)
            f["tvd_subgrupo_b2"] = _tvd_grupos(dist, d, DIMENSIONES, ops)
            f["tvd_ccaa_b2"] = _tvd_grupos(dist, d, ["ccaa"], ops)
            justif.append({"id": q["id"], "uso": "b2", "justificacion": b2["justificacion"]})
            for g in DIMENSIONES:
                bl = brecha(dist, g)
                bs = brecha(r.sistema_cis, g) if r.analogas else None
                br = brecha(_grupos(d, g, ops), g)
                contra.append({"id": q["id"], "dimension": g, "llm": bl, "sistema": bs, "real": br})
        nueva = salidas.get(f"nueva:{q['id']}")
        if nueva is not None:
            dist = A.distribuciones(nueva)
            f["tvd_nueva"] = V.tvd(dist["total"], y)
            f["tvd_subgrupo_nueva"] = _tvd_grupos(dist, d, DIMENSIONES, ops)
            mu = dist["total"]
            s = np.maximum(np.sqrt(mu * (1 - mu)), E.S_MIN)
            residuos += list(np.abs(y - mu) / s)
            justif.append({"id": q["id"], "uso": "nueva", "justificacion": nueva["justificacion"]})
        filas.append(f)
    d = pl.DataFrame(filas, infer_schema_length=None)
    DETALLE.mkdir(parents=True, exist_ok=True)
    d.write_csv(DETALLE / "llm_preguntas.csv")
    pl.DataFrame(justif).write_csv(DETALLE / "llm_justificaciones.csv")
    ct = pl.DataFrame(contra, infer_schema_length=None)
    ct.write_csv(DETALLE / "llm_contrafactual.csv")

    def media(col: str, df: pl.DataFrame = d) -> float | None:
        if col not in df.columns or not df[col].drop_nulls().len():
            return None
        return float(df[col].drop_nulls().mean())

    # G9.7: brecha del LLM / brecha del modelo estadístico (y frente a la observada, informativa)
    th = load_config("thresholds.yaml").v_llm_estereotipo  # type: ignore[attr-defined]
    cs_ok = ct.filter(pl.col("sistema").is_not_null() & (pl.col("sistema") >= th.brecha_minima))
    razon = (cs_ok["llm"] / cs_ok["sistema"]).drop_nulls()
    cr_ok = ct.filter(pl.col("real").is_not_null() & (pl.col("real") >= th.brecha_minima))
    razon_real = (cr_ok["llm"] / cr_ok["real"]).drop_nulls()
    # preguntas nuevas: LLM frente al estadístico donde existen ambos
    nuevas = d.filter(pl.col("tvd_nueva").is_not_null()) if "tvd_nueva" in d.columns else d.head(0)
    ambos = nuevas.filter(pl.col("tvd_sistema_cis").is_not_null())
    usar = bool(
        nuevas.height
        and (ambos.height == 0 or ambos["tvd_nueva"].mean() < ambos["tvd_sistema_cis"].mean())
    )
    res = {
        "estudios": sorted(estudios),
        "preguntas": d.height,
        "b2": {
            "total": media("tvd_b2"),
            "subgrupos": media("tvd_subgrupo_b2"),
            "ccaa": media("tvd_ccaa_b2"),
            "sistema_cis_mismas_preguntas": media(
                "tvd_sistema_cis", d.filter(pl.col("tvd_b2").is_not_null())
            )
            if "tvd_b2" in d.columns
            else None,
        },
        "nuevas": {
            "preguntas": nuevas.height,
            "tvd_llm": media("tvd_nueva", nuevas),
            "con_estadistico": ambos.height,
            "tvd_llm_en_ambas": media("tvd_nueva", ambos),
            "tvd_estadistico_en_ambas": media("tvd_sistema_cis", ambos),
            "usar": usar,
        },
        "g9_7": {
            "contrafactual_casos": razon.len(),
            "razon_brecha_mediana": float(razon.median()) if razon.len() else None,
            "razon_brecha_mediana_frente_real": float(razon_real.median())
            if razon_real.len()
            else None,
            "umbral": th.razon_brecha_mediana_max,
            "umbral_estado": th.estado,
            "homogeneidad": "no aplica: no se simulan personas (D-069)",
            "justificaciones": len(justif),
        },
        "coste": {"gastado_total_eur": round(C.gasto_total(), 4)},
    }
    if calibrar and nuevas.height and residuos:
        tasa = float((nuevas["tvd_nueva"] <= 0.10).mean())
        cal = {
            "q80": _conformal(np.array(residuos), 0.80),
            "q95": _conformal(np.array(residuos), 0.95),
            "acierto": tasa,
            "usar": usar,
            "preguntas": nuevas.height,
            "estudios": sorted(estudios),
        }
        S.CALIBRACION_LLM.parent.mkdir(parents=True, exist_ok=True)
        S.CALIBRACION_LLM.write_text(json.dumps(cal, indent=1), "utf-8")
        res["nuevas"]["calibracion"] = cal
    from sinpop.predict import evento as EV

    ev = EV.backtest_llm(backend) if eventos else pl.DataFrame()
    if ev.height:
        ev.drop("ic95_real").write_csv(DETALLE / "evento_backtest_llm.csv")
        por_evento = ev.group_by("evento").agg(pl.col("direccion_correcta").mean() > 0.5)
        res["g9_6_llm"] = {
            "pares": ev.height,
            "pares_correctos": int(ev["direccion_correcta"].sum()),
            "eventos": por_evento.height,
            "eventos_correctos": int(por_evento["direccion_correcta"].sum()),
            "error_magnitud_pp_medio": float(ev["error_magnitud_pp"].mean()),
            "contaminado": True,
        }
    res["coste"]["gastado_total_eur"] = round(C.gasto_total(), 4)
    destino.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    return res


def estimar(estudios: dict[str, str] | None = None) -> dict:
    from sinpop.config import load_config
    from sinpop.predict import evento as EV

    cs = casos(V.VALIDACION if estudios is None else estudios)
    pets = peticiones(cs)
    b = EV.banco()
    for e in load_config("eventos.yaml").eventos:  # type: ignore[attr-defined]
        for ind in e.indicadores_afectados:
            if not b.filter((pl.col("evento") == e.id) & (pl.col("indicador") == ind)).is_empty():
                pets.append(EV.peticion_llm(e, ind))
    return C.estimar(pets)


if __name__ == "__main__":
    if "--estimar" in sys.argv:
        print(json.dumps(estimar(), ensure_ascii=False, indent=1))
    else:
        print(json.dumps(ejecutar(), ensure_ascii=False, indent=1))
