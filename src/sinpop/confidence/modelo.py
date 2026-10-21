"""Modelo de confianza (F10, tareas 2 y 3) (D-070).

Dos modelos sobre las señales de `senales.py`, entrenados con el *backtest* histórico
(`backtest.py`, solo componente estadístico):

- **error predicho:** regresión por *gradient boosting* de la TVD;
- **confianza:** probabilidad de que la TVD sea ≤ `UMBRAL_TVD` (la definición de V-CONF-ECE),
  clasificador por *gradient boosting* con calibración isotónica por validación cruzada.

Ambos llevan **restricciones de monotonía**: más similitud con el banco y más datos del subgrupo
nunca empeoran la confianza ni aumentan el error predicho; más desacuerdo entre análogas o entre
estimadores y un intervalo más ancho, al revés. Así se cumple por construcción lo que pide G10.3
(la confianza baja con el tamaño del territorio y del subgrupo) y el modelo no aprende relaciones
espurias de un backtest finito.
"""

from __future__ import annotations

import json
import pickle

import numpy as np
import polars as pl
from threadpoolctl import threadpool_limits

from sinpop import PROCESSED_DIR

# un hilo en ajuste y predicción: los datos son pequeños y OpenMP, con otros procesos en marcha,
# se sobresuscribe (minutos en lugar de segundos)
UMBRAL_TVD = 0.10
SENALES = {
    # señal: monotonía respecto a la confianza (+1 sube, −1 baja, 0 libre)
    "similitud_max": 1,
    "similitud_media": 1,
    "analogas": 0,
    "desacuerdo_analogas": -1,
    "tvd_sistema_b0": -1,
    "tvd_sistema_b1": -1,
    "anchura_ic80": -1,
    "log_n_datos": 1,
    "opciones": 0,
    "ordinal": 0,
    "meses_ultima": -1,
    "recurrente": 1,
    "es_subgrupo": -1,
}
DESTINO = PROCESSED_DIR / "confidence" / "modelo.pkl"
# isotónica ajustada en la ventana de validación (docs/04, F10, tarea 3) por
# `sinpop.evaluate.confianza`; si existe, se aplica encima del modelo
RECALIBRACION = PROCESSED_DIR / "confidence" / "recalibracion.pkl"


def _x(d: pl.DataFrame) -> np.ndarray:
    return d.select(list(SENALES)).to_numpy().astype(float)


class ModeloConfianza:
    def ajustar(self, d: pl.DataFrame) -> ModeloConfianza:
        import sklearn.ensemble  # noqa: F401  (carga libgomp antes de limitar los hilos)

        with threadpool_limits(1):
            return self._ajustar(d)

    def _ajustar(self, d: pl.DataFrame) -> ModeloConfianza:
        from sklearn.calibration import CalibratedClassifierCV
        from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor

        x = _x(d)
        y_err = d["tvd"].to_numpy()
        y_ok = (y_err <= UMBRAL_TVD).astype(int)
        mono = list(SENALES.values())
        self.error = HistGradientBoostingRegressor(
            max_iter=300,
            learning_rate=0.05,
            max_leaf_nodes=15,
            monotonic_cst=[-m for m in mono],
            random_state=0,
        ).fit(x, y_err)
        base = HistGradientBoostingClassifier(
            max_iter=300,
            learning_rate=0.05,
            max_leaf_nodes=15,
            monotonic_cst=mono,
            random_state=0,
        )
        # isotónica por pregunta: los pliegues no mezclan filas de una misma pregunta
        from sklearn.model_selection import GroupKFold

        grupos = d["id"].to_numpy()
        cv = list(GroupKFold(5).split(x, y_ok, grupos))
        self.confianza = CalibratedClassifierCV(base, method="isotonic", cv=cv).fit(x, y_ok)
        self.n = d.height
        return self

    def predecir(self, d: pl.DataFrame) -> pl.DataFrame:
        x = _x(d)
        with threadpool_limits(1):
            err, conf = self.error.predict(x), self.confianza.predict_proba(x)[:, 1]
        return d.with_columns(pl.Series("error_predicho", err), pl.Series("confianza", conf))

    def guardar(self) -> None:
        DESTINO.parent.mkdir(parents=True, exist_ok=True)
        DESTINO.write_bytes(pickle.dumps(self))


def cargar() -> ModeloConfianza | None:
    return pickle.loads(DESTINO.read_bytes()) if DESTINO.exists() else None  # noqa: S301


def recalibrador():
    return pickle.loads(RECALIBRACION.read_bytes()) if RECALIBRACION.exists() else None  # noqa: S301


def confianza_final(d: pl.DataFrame) -> pl.DataFrame | None:
    """Confianza que se publica: modelo del backtest más la recalibración en validación."""
    m = cargar()
    if m is None:
        return None
    d = m.predecir(d)
    iso = recalibrador()
    if iso is not None:
        d = d.with_columns(pl.Series("confianza", iso.predict(d["confianza"].to_numpy())))
    return d


def ece(confianza: np.ndarray, acierto: np.ndarray, bins: int = 10) -> float:
    """Error de calibración esperado con `bins` intervalos iguales de confianza."""
    cortes = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(confianza, cortes[1:-1]), 0, bins - 1)
    total = 0.0
    for b in range(bins):
        s = idx == b
        if s.any():
            total += s.mean() * abs(confianza[s].mean() - acierto[s].mean())
    return float(total)


def metricas(d: pl.DataFrame) -> dict:
    """V-CONF-CORR, V-CONF-ECE y la relación con el tamaño de los datos (G10.3)."""
    from scipy.stats import spearmanr

    acierto = (d["tvd"].to_numpy() <= UMBRAL_TVD).astype(float)
    conf = d["confianza"].to_numpy()
    sub = d.filter(pl.col("es_subgrupo") == 1)
    rho_n = spearmanr(sub["confianza"], sub["log_n_datos"]).statistic if sub.height > 2 else None
    ccaa = sub.filter(pl.col("grupo") == "ccaa")
    rho_t = spearmanr(ccaa["confianza"], ccaa["log_n_datos"]).statistic if ccaa.height > 2 else None
    cal = []
    cortes = np.linspace(0, 1, 11)
    idx = np.clip(np.digitize(conf, cortes[1:-1]), 0, 9)
    for b in range(10):
        s = idx == b
        if s.any():
            cal.append(
                {
                    "bin": f"{cortes[b]:.1f}-{cortes[b + 1]:.1f}",
                    "casos": int(s.sum()),
                    "confianza_media": float(conf[s].mean()),
                    "acierto": float(acierto[s].mean()),
                }
            )
    return {
        "casos": d.height,
        "spearman_error": float(spearmanr(d["error_predicho"], d["tvd"]).statistic),
        # V-CONF-CORR: más confianza, menos error (se informa con el signo cambiado)
        "spearman_confianza": float(-spearmanr(conf, d["tvd"]).statistic),
        "ece": ece(conf, acierto),
        "spearman_confianza_n_subgrupo": float(rho_n) if rho_n is not None else None,
        "spearman_confianza_n_ccaa": float(rho_t) if rho_t is not None else None,
        "confianza_media_total": float(d.filter(pl.col("es_subgrupo") == 0)["confianza"].mean()),
        "confianza_media_subgrupos": float(sub["confianza"].mean()) if sub.height else None,
        "diagrama_calibracion": cal,
    }


def guardar_metricas(m: dict, ruta) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(m, ensure_ascii=False, indent=1), "utf-8")
