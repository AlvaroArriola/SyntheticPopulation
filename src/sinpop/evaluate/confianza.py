"""Confianza (F10) en la ventana de validación (G10.1-G10.3) (D-070).

Con los barómetros de validación (`validacion.VALIDACION`), se predice cada pregunta con el
componente estadístico, se calcula su error real (total y subgrupos con datos suficientes) y se
compara con la confianza del modelo entrenado en el *backtest* histórico:

- **sin recalibrar:** el modelo tal como sale del *backtest*;
- **calibrado en validación** (`docs/04`, F10, tarea 3), sin ver la misma pregunta: isotónica
  ajustada en un barómetro y evaluada en el otro (y al revés).

Se publica la recalibración (`confidence.modelo.RECALIBRACION`, ajustada con los dos barómetros)
solo si mejora el ECE cruzado; si no, la confianza publicada es la del modelo tal cual. La puerta
F10 evalúa la variante publicada (`publicada`).

Comando: `python -m sinpop.evaluate.confianza`
"""

from __future__ import annotations

import json
import pickle

import polars as pl

from sinpop import REPORTS_DIR
from sinpop.confidence import backtest as BT
from sinpop.confidence import modelo as M
from sinpop.evaluate import validacion as V
from sinpop.predict import estimador as E
from sinpop.predict import opciones as O

DESTINO = REPORTS_DIR / "fase_10_validacion.json"
FILAS = REPORTS_DIR / "fase_10" / "validacion_confianza.csv"


def filas(limite: int | None = None, estudios: dict[str, str] | None = None) -> pl.DataFrame:
    out = []
    for estudio, fecha in (V.VALIDACION if estudios is None else estudios).items():
        p, lg, banco = V._cargar(estudio, fecha)
        qs = V.preguntas(banco, estudio, fecha)
        if limite:
            qs = qs[:limite]
        for q in qs:
            d = V.verdad(p, lg, q["variable"], q["opciones"])
            if d.height < 200:
                continue
            pq = E.Pregunta(
                q["id"],
                q["enunciado"],
                q["opciones"],
                O.escala_probable(q["opciones"]),
                q["mes"],
                BT.SUBGRUPOS,
            )
            r = E.predecir(pq)
            if not r.analogas:
                continue
            v = d.rename({"etiqueta": "valor"}).with_columns(
                (pl.col("peso") / pl.col("peso").mean()).alias("peso")
            )
            for f in BT.filas_pregunta(r, v, BT.SUBGRUPOS):
                out.append(f | {"estudio": estudio})
    return pl.DataFrame(out)


def ejecutar(limite: int | None = None) -> dict:
    from sklearn.isotonic import IsotonicRegression

    modelo = M.cargar()
    if modelo is None:
        raise FileNotFoundError("falta el modelo de confianza (python -m sinpop.confidence.run)")
    d = modelo.predecir(filas(limite))
    FILAS.parent.mkdir(parents=True, exist_ok=True)
    sin = M.metricas(d)
    # calibración cruzada entre los dos barómetros de validación
    cal = []
    estudios = sorted(d["estudio"].unique())
    for e in estudios:
        tr, te = d.filter(pl.col("estudio") != e), d.filter(pl.col("estudio") == e)
        iso = IsotonicRegression(out_of_bounds="clip", y_min=0, y_max=1).fit(
            tr["confianza"].to_numpy(), (tr["tvd"].to_numpy() <= M.UMBRAL_TVD).astype(float)
        )
        cal.append(te.with_columns(pl.Series("confianza", iso.predict(te["confianza"].to_numpy()))))
    dc = pl.concat(cal)
    con = M.metricas(dc)
    dc.write_csv(FILAS)
    # se publica la recalibración solo si mejora la calibración cruzada; si no, el modelo tal cual
    recalibrar = con["ece"] < sin["ece"]
    if recalibrar:
        final = IsotonicRegression(out_of_bounds="clip", y_min=0, y_max=1).fit(
            d["confianza"].to_numpy(), (d["tvd"].to_numpy() <= M.UMBRAL_TVD).astype(float)
        )
        M.RECALIBRACION.parent.mkdir(parents=True, exist_ok=True)
        M.RECALIBRACION.write_bytes(pickle.dumps(final))
    else:
        M.RECALIBRACION.unlink(missing_ok=True)
    res = {
        "estudios": estudios,
        "sin_recalibrar": sin,
        "calibrado_en_validacion": con,
        "publicada": "calibrado_en_validacion" if recalibrar else "sin_recalibrar",
        "tvd_umbral": M.UMBRAL_TVD,
    }
    DESTINO.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    return res


if __name__ == "__main__":
    print(json.dumps(ejecutar(), ensure_ascii=False, indent=1))
