"""Evaluación de F9 en la ventana de validación (G9.1-G9.6) (D-069).

Único módulo, con el resto de `sinpop.evaluate`, que lee `data/eval/` (regla 5). La ventana de
datos posteriores al corte se reparte (D-069):

- **validación** (`VALIDACION`): barómetros de julio (3571) y septiembre (3577) de 2026. Se
  usan aquí, en F9 y F10;
- **evaluación final** (`EVALUACION_FINAL`): octubre de 2026 (3582) y los que se añadan. No se
  leen hasta F11.

Para cada pregunta cerrada de los estudios de validación (mismos filtros que el banco), el
predictor recibe **solo** el enunciado (la etiqueta de la variable), las opciones y el mes: nunca
las respuestas. Se compara con la distribución ponderada de los españoles de 18+ (el universo del
CIS), en total, por subgrupo y por comunidad:

- sistema «como lo mediría el CIS» (`medicion_cis`, comparable con un barómetro), sistema
  «población», B0 (histórico de análogas) y B1 (modelo demográfico clásico). B2 necesita un
  modelo de lenguaje y no se ejecuta (D-069);
- V-FORMATO: cada salida validada por esquema; V-COBERTURA: proporción de opciones cuyo valor
  real cae en el intervalo del 80 % y del 95 %; V-REFORMULACION: TVD entre la predicción de la
  pregunta y la de su reformulación neutra; V-EVENTO: *backtest* del modo evento.

Comando: `python -m sinpop.evaluate.validacion`.
"""

from __future__ import annotations

import datetime as dt
import json

import numpy as np
import polars as pl

from sinpop import REPORTS_DIR
from sinpop.evaluate import EVAL_DIR
from sinpop.opinion import cis
from sinpop.opinion.valores import _edad_grupo
from sinpop.predict import banco as B
from sinpop.predict import estimador as E
from sinpop.predict import opciones as O
from sinpop.predict import salida as S
from sinpop.predict.reformular import reformular
from sinpop.temporal.indicadores import _edad4

VALIDACION = {"3571": "2026-07-01", "3577": "2026-09-01"}
EVALUACION_FINAL = {"3582": "2026-10-01"}
CARPETA = EVAL_DIR / "cis"
DETALLE = REPORTS_DIR / "fase_09"
SUBGRUPOS = ["edad_4", "sexo", "estudios_3"]
MIN_CASOS_GRUPO = 150
POLITICAS = (
    r"^(RECUERDO|RECUVOTO|INTENCION|CERCANIA|SIMPATIA|VOTOSIM|PROBVOTO|ESCIDEOL|VALORALIDERES|"
    r"CONFIANZAPTE|CONFIANZAOPOSIC|PREFPTE|LIDERES|PARTICIPACION)"
)


def _cargar(estudio: str, fecha: str) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
    p = cis.personas(estudio, CARPETA, fecha)
    lg, banco = cis.largo(estudio, CARPETA)
    return p, lg, banco


def preguntas(banco: pl.DataFrame, estudio: str, fecha: str) -> list[dict]:
    out = []
    for var, enun, ops in banco.select("variable", "enunciado", "opciones").iter_rows():
        if B.EXCLUIDAS.search(var) or not (enun or "").strip():
            continue
        op = B._opciones(ops)
        k = len(O.sustantivas(op))
        if k < 2 or k > B.MAX_OPCIONES:
            continue
        out.append(
            {
                "id": f"CIS-{estudio}-{var}",
                "variable": var,
                "enunciado": enun.strip(),
                "opciones": op,
                "mes": fecha[:7],
                "politica": bool(__import__("re").match(POLITICAS, var)),
            }
        )
    return out


def verdad(p: pl.DataFrame, lg: pl.DataFrame, variable: str, opciones: list[str]) -> pl.DataFrame:
    """Respuestas ponderadas de los españoles de 18+ con su perfil (para total y grupos)."""
    from sinpop.opinion.latentes import _intermedios_numericos

    x = _intermedios_numericos(lg.filter(pl.col("variable") == variable), {variable: "numerica"})
    x = x.filter(pl.col("etiqueta").is_in(opciones))
    return (
        p.join(x.select("encuestado", "etiqueta"), on="encuestado")
        .filter(
            (pl.col("edad") >= 18)
            & (
                pl.col("nacionalidad_esp_ext").is_null()
                | (pl.col("nacionalidad_esp_ext") == "espanola")
            )
        )
        .with_columns(_edad4(pl.col("edad")), _edad_grupo(pl.col("edad")))
    )


def _dist(d: pl.DataFrame, opciones: list[str]) -> np.ndarray:
    t = dict(d.group_by("etiqueta").agg(pl.col("peso").sum()).iter_rows())
    v = np.array([t.get(o, 0.0) for o in opciones])
    return v / v.sum() if v.sum() > 0 else v


def tvd(a: np.ndarray, b: np.ndarray) -> float:
    return float(0.5 * np.abs(a - b).sum())


def evaluar_pregunta(q: dict, p: pl.DataFrame, lg: pl.DataFrame) -> dict | None:
    d = verdad(p, lg, q["variable"], q["opciones"])
    if d.height < 200:
        return None
    escala = O.escala_probable(q["opciones"])
    pq = E.Pregunta(q["id"], q["enunciado"], q["opciones"], escala, q["mes"], SUBGRUPOS + ["ccaa"])
    r = E.predecir(pq)
    if not r.analogas:
        return {"id": q["id"], "sin_analogas": True}
    out_json = S.construir(r, "validacion")
    y = _dist(d, q["opciones"])
    fila = {
        "id": q["id"],
        "politica": q["politica"],
        "n": d.height,
        "similitud_max": r.analogas[0]["similitud"],
        "recurrente": any(
            a["variable"] == q["variable"]
            and O.normalizar(a["enunciado"]) == O.normalizar(q["enunciado"])
            for a in r.analogas
        ),
        "tvd_sistema_cis": tvd(r.sistema_cis["total"], y),
        "tvd_sistema": tvd(r.sistema["total"], y),
        "tvd_b0": tvd(r.b0, y),
        "tvd_b1": tvd(r.b1["total"], y),
        "formato_ok": True,
    }
    # cobertura (total, medición CIS)
    dist = out_json["medicion_cis"]
    c80 = [dist[o]["ic80"][0] <= y[j] <= dist[o]["ic80"][1] for j, o in enumerate(q["opciones"])]
    c95 = [dist[o]["ic95"][0] <= y[j] <= dist[o]["ic95"][1] for j, o in enumerate(q["opciones"])]
    fila["cubre80"], fila["cubre95"], fila["opciones"] = sum(c80), sum(c95), len(c80)
    # subgrupos y comunidades (sistema población posestratificado a españoles ≈ medición CIS)
    for g, clave in [(s, "subgrupo") for s in SUBGRUPOS] + [("ccaa", "ccaa")]:
        errs = {k: [] for k in ["sistema", "b1"]}
        for lv, dg in d.group_by(g):
            lv = lv[0]
            k = f"{g}={lv}"
            if dg.height < MIN_CASOS_GRUPO or k not in r.sistema:
                continue
            yg = _dist(dg, q["opciones"])
            errs["sistema"].append(tvd(r.sistema[k], yg))
            errs["b1"].append(tvd(r.b1[k], yg))
        for est, v in errs.items():
            fila.setdefault(f"tvd_{clave}_{est}", [])
            fila[f"tvd_{clave}_{est}"] += v
    for c in list(fila):
        if isinstance(fila[c], list):
            fila[c] = float(np.mean(fila[c])) if fila[c] else None
    # reformulación neutra
    rq = E.Pregunta(q["id"] + "_R", reformular(q["enunciado"]), q["opciones"], escala, q["mes"], [])
    rr = E.predecir(rq)
    fila["reformulacion"] = rq.enunciado
    fila["tvd_reformulacion"] = (
        tvd(rr.sistema_cis["total"], r.sistema_cis["total"]) if rr.analogas else None
    )
    return fila


def ejecutar(limite: int | None = None) -> dict:
    DETALLE.mkdir(parents=True, exist_ok=True)
    filas, sin = [], []
    for estudio, fecha in VALIDACION.items():
        p, lg, banco = _cargar(estudio, fecha)
        qs = preguntas(banco, estudio, fecha)
        if limite:
            qs = qs[:limite]
        for q in qs:
            try:
                f = evaluar_pregunta(q, p, lg)
            except ValueError as exc:  # salida que no pasa V-FORMATO
                f = {"id": q["id"], "formato_ok": False, "error": str(exc)}
            if f is None:
                continue
            if f.get("sin_analogas"):
                sin.append(q["id"])
                continue
            filas.append(f)
    d = pl.DataFrame(filas, infer_schema_length=None)
    d.write_csv(DETALLE / "validacion_preguntas.csv")
    from sinpop.predict import evento as V

    ev = V.backtest()
    ev.with_columns(
        pl.col("ic95_real").list.eval(pl.element().round(4).cast(pl.Utf8)).list.join(" a ")
    ).write_csv(DETALLE / "evento_backtest.csv")
    ok = d.filter(pl.col("formato_ok"))

    def media(df: pl.DataFrame, c: str) -> float | None:
        v = df[c].drop_nulls()
        return float(v.mean()) if len(v) else None

    por_evento = ev.group_by("evento").agg(pl.col("direccion_correcta").mean())
    res = {
        "fecha": dt.date.today().isoformat(),
        "estudios_validacion": VALIDACION,
        "estudios_reservados_f11": EVALUACION_FINAL,
        "preguntas": d.height,
        "sin_analogas": sin,
        "g9_1": {"salidas": d.height, "validas": ok.height},
        "g9_2": {
            grupo: {est: media(sub, f"tvd_{est}") for est in ["sistema_cis", "sistema", "b0", "b1"]}
            | {"preguntas": sub.height}
            for grupo, sub in [
                ("todas", ok),
                ("recurrentes", ok.filter(pl.col("recurrente"))),
                ("nuevas", ok.filter(~pl.col("recurrente"))),
                ("politicas", ok.filter(pl.col("politica"))),
            ]
        }
        | {
            "subgrupos": {
                "sistema": media(ok, "tvd_subgrupo_sistema"),
                "b1": media(ok, "tvd_subgrupo_b1"),
            },
            "ccaa": {"sistema": media(ok, "tvd_ccaa_sistema"), "b1": media(ok, "tvd_ccaa_b1")},
            "b2": "no ejecutado: necesita un modelo de lenguaje (D-069)",
        },
        "g9_3": {"llamadas": 0, "tokens": 0, "eur": 0.0, "segundos_por_pregunta": None},
        "g9_4": {
            "preguntas": int(ok["tvd_reformulacion"].drop_nulls().len()),
            "tvd_media": media(ok, "tvd_reformulacion"),
            "tvd_max": float(ok["tvd_reformulacion"].drop_nulls().max()),
            "por_encima_umbral": int((ok["tvd_reformulacion"].drop_nulls() > 0.03).sum()),
        },
        "g9_5": {
            "cobertura80": float(ok["cubre80"].sum() / ok["opciones"].sum()),
            "cobertura95": float(ok["cubre95"].sum() / ok["opciones"].sum()),
            "casos": int(ok["opciones"].sum()),
        },
        "g9_6": {
            "pares": ev.height,
            "pares_correctos": int(ev["direccion_correcta"].sum()),
            "eventos": por_evento.height,
            "eventos_correctos": int((por_evento["direccion_correcta"] > 0.5).sum()),
            "error_magnitud_pp_medio": float(ev["error_magnitud_pp"].mean()),
        },
        "g9_7": "no aplica: sin modelo de lenguaje no hay salidas que auditar (docs/06 §5)",
    }
    (REPORTS_DIR / "fase_09_validacion.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1, default=str), "utf-8"
    )
    return res


if __name__ == "__main__":
    print(json.dumps(ejecutar(), ensure_ascii=False, indent=1, default=str))
