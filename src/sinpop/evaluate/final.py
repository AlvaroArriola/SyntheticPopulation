"""Evaluación final sin contaminación (F11; `docs/04`; D-069, D-071).

Una sola vez, desde una etiqueta git congelada y sin cambios locales, sobre la ventana de
evaluación final (`validacion.EVALUACION_FINAL`), que no ha leído ningún paso anterior:

1. comprueba la etiqueta y que el árbol está limpio (G11.1); si ya existe una evaluación, no se
   repite (`DESTINO`);
2. mide el sistema y los baselines B0 y B1 en total, por subgrupo y por comunidad, con la
   cobertura de los intervalos (mismas métricas que F9, `validacion.evaluar_pregunta`);
3. con la capa de LLM activa, B2 y las preguntas nuevas (`evaluate.llm`), y el **sistema final**:
   el LLM anclado donde no hay análogas fiables (si en validación se decidió usarlo), el
   componente estadístico en el resto;
4. la calibración de la confianza declarada (F10): Spearman y ECE en esta ventana;
5. separa las preguntas políticas de las de vida cotidiana.

Comando: `python -m sinpop.evaluate.final --tag <etiqueta>`.
"""

from __future__ import annotations

import datetime as dt
import json
import subprocess

import polars as pl

from sinpop import REPO_ROOT, REPORTS_DIR
from sinpop.evaluate import validacion as V

DESTINO = REPORTS_DIR / "fase_11_evaluacion.json"
DETALLE = REPORTS_DIR / "fase_11"


class EvaluacionNoPermitida(RuntimeError):
    pass


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout.strip()


def comprobar_congelacion(tag: str) -> dict:
    try:
        commit_tag = _git("rev-list", "-n", "1", tag)
    except subprocess.CalledProcessError as e:
        raise EvaluacionNoPermitida(f"no existe la etiqueta {tag}") from e
    head = _git("rev-parse", "HEAD")
    cambios = _git("status", "--porcelain", "--untracked-files=no")
    if head != commit_tag:
        raise EvaluacionNoPermitida(f"HEAD ({head[:8]}) no es la etiqueta {tag} ({commit_tag[:8]})")
    if cambios:
        raise EvaluacionNoPermitida("hay cambios sin confirmar en ficheros versionados")
    return {"tag": tag, "commit": commit_tag, "limpio": True}


def ejecutar(tag: str) -> dict:
    if DESTINO.exists():
        raise EvaluacionNoPermitida(f"la evaluación final ya se ejecutó ({DESTINO}); no se repite")
    git = comprobar_congelacion(tag)
    from sinpop.llm import cliente as C
    from sinpop.predict import asistido as A
    from sinpop.predict import salida as S

    DETALLE.mkdir(parents=True, exist_ok=True)
    filas, sin = [], []
    for estudio, fecha in V.EVALUACION_FINAL.items():
        p, lg, banco = V._cargar(estudio, fecha)
        for q in V.preguntas(banco, estudio, fecha):
            try:
                f = V.evaluar_pregunta(q, p, lg)
            except ValueError as exc:
                f = {"id": q["id"], "formato_ok": False, "error": str(exc)}
            if f is None:
                continue
            if f.get("sin_analogas"):
                sin.append(q["id"])
                f = {"id": q["id"], "politica": q["politica"], "sin_analogas": True}
            filas.append(f | {"estudio": estudio})
    d = pl.DataFrame(filas, infer_schema_length=None)

    llm = None
    if C.disponible():
        from sinpop.evaluate import llm as L

        llm = L.ejecutar(
            V.EVALUACION_FINAL,
            calibrar=False,
            eventos=False,
            destino=REPORTS_DIR / "fase_11_llm.json",
        )
        dl = pl.read_csv(L.DETALLE / "llm_preguntas.csv")
        dl = dl.select("id", *[c for c in ["tvd_b2", "tvd_nueva"] if c in dl.columns])
        d = d.join(dl, on="id", how="left")
    cal = S.calibracion_llm()
    usar = bool(llm and cal and cal.get("usar") and "tvd_nueva" in d.columns)
    sim = pl.col("similitud_max") if "similitud_max" in d.columns else pl.lit(None)
    if usar:
        d = d.with_columns(
            pl.when(sim.is_null() | (sim < A.UMBRAL))
            .then(pl.col("tvd_nueva"))
            .otherwise(pl.col("tvd_sistema_cis"))
            .alias("tvd_sistema_final")
        )
    else:
        d = d.with_columns(pl.col("tvd_sistema_cis").alias("tvd_sistema_final"))
    d.write_csv(DETALLE / "preguntas.csv")

    def resumen(df: pl.DataFrame) -> dict:
        def m(c: str) -> float | None:
            if c not in df.columns or not df[c].drop_nulls().len():
                return None
            return float(df[c].drop_nulls().mean())

        out = {
            "preguntas": df.height,
            "sistema_final": m("tvd_sistema_final"),
            "sistema_cis": m("tvd_sistema_cis"),
            "b0": m("tvd_b0"),
            "b1": m("tvd_b1"),
            "b2": m("tvd_b2"),
            "subgrupos": {"sistema": m("tvd_subgrupo_sistema"), "b1": m("tvd_subgrupo_b1")},
            "ccaa": {"sistema": m("tvd_ccaa_sistema"), "b1": m("tvd_ccaa_b1")},
        }
        if "opciones" in df.columns and df["opciones"].drop_nulls().sum():
            out["cobertura80"] = float(df["cubre80"].sum() / df["opciones"].sum())
            out["cobertura95"] = float(df["cubre95"].sum() / df["opciones"].sum())
        return out

    pol = pl.col("politica").fill_null(False)
    res = {
        "fecha": dt.date.today().isoformat(),
        "git": git,
        "estudios": V.EVALUACION_FINAL,
        "sin_analogas": sin,
        "todas": resumen(d),
        "politicas": resumen(d.filter(pol)),
        "vida_cotidiana": resumen(d.filter(~pol)),
        "llm": llm,
        "usa_llm_en_preguntas_nuevas": usar,
    }
    # calibración de la confianza declarada (F10) en esta ventana
    from sinpop.confidence import modelo as M
    from sinpop.evaluate import confianza as EC

    if M.cargar() is not None:
        fc = M.confianza_final(EC.filas(estudios=V.EVALUACION_FINAL))
        if fc is not None and fc.height:
            fc.write_csv(DETALLE / "confianza.csv")
            res["confianza"] = M.metricas(fc)
    DESTINO.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str), "utf-8")
    return res


if __name__ == "__main__":
    import argparse

    a = argparse.ArgumentParser(description="Evaluación final (F11), una sola vez")
    a.add_argument("--tag", required=True, help="etiqueta git congelada")
    print(json.dumps(ejecutar(a.parse_args().tag), ensure_ascii=False, indent=1, default=str))
