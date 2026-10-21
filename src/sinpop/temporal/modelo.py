"""Modelo de cada indicador con efectos de periodo (F8C; docs/03 §2.6) (D-068).

Dos piezas, en el espacio log de las probabilidades (desplazamientos de un softmax):

1. **Perfil (estático):** regresión logística multinomial ponderada con los predictores de F8A
   (sexo, edad, estudios, actividad, comunidad, tamaño de municipio, comunidad × edad) y el grupo
   de voto de 2023 de F8B («desconocido» antes de agosto de 2023), con todos los meses.
2. **Periodo (dinámico):** para cada mes y categoría, la desviación entre la proporción observada
   y la que predice el modelo, d = log(observada / predicha), con su varianza muestral
   (1 − p) / (n_efectivo · p). Esas desviaciones siguen un **nivel local** (paseo aleatorio)
   observado con ruido, que se estima con el filtro de Kalman; la varianza del paseo se elige
   por máxima verosimilitud. El filtro separa el ruido muestral (unos ±0,8 puntos con 4.000
   entrevistas) del cambio real y un mes sin barómetro (agosto) se queda en el nivel anterior.

   Hay un nivel nacional y uno por grupo de cada interacción de `temporal.yaml` (edad en cuatro
   grupos, comunidad y grupo de voto), que recoge lo que cada grupo se separa de la evolución
   nacional. Se estiman por pasadas sucesivas (*backfitting*): cada componente con los demás
   fijos.

Para el periodo de construcción se usa el nivel **suavizado** (con todos los meses, Rauch-Tung-
Striebel). Para predecir el mes t + h con datos hasta t se usa el nivel **filtrado** en t (el
paseo aleatorio no tiene tendencia: su predicción es el último nivel).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import polars as pl

from sinpop.opinion.valores import COLUMNAS, Modelo
from sinpop.temporal import indicadores as T

PERFIL = COLUMNAS + ["grupo_voto"]
NACIONAL = "nacional"
PASADAS = 3
PSEUDO = 0.5  # pseudoconteo para proporciones nulas en grupos pequeños
Q_REJILLA = np.array([0.0, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3])


def kalman(d: np.ndarray, v: np.ndarray, q: float, suavizar: bool) -> tuple[np.ndarray, float]:
    """Nivel local: μ_t = μ_{t−1} + η (var q), d_t = μ_t + ε (var v_t; NaN = sin dato).
    Devuelve los niveles (filtrados o suavizados) y la log-verosimilitud. Arranque difuso."""
    n = len(d)
    a, p = 0.0, 1e6
    af, pf, ap, pp = np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n)
    ll = 0.0
    for t in range(n):
        if t > 0:
            p = p + q
        ap[t], pp[t] = a, p
        if not np.isnan(d[t]):
            f = p + v[t]
            k = p / f
            e = d[t] - a
            if p < 1e5:  # la primera observación solo inicializa
                ll += -0.5 * (np.log(2 * np.pi * f) + e * e / f)
            a = a + k * e
            p = (1 - k) * p
        af[t], pf[t] = a, p
    if not suavizar:
        return af, ll
    s = af.copy()
    for t in range(n - 2, -1, -1):
        j = pf[t] / pp[t + 1] if pp[t + 1] > 0 else 0.0
        s[t] = af[t] + j * (s[t + 1] - ap[t + 1])
    return s, ll


@dataclass
class Componente:
    nombre: str  # "nacional" o la columna del grupo
    niveles: list[str]
    q: float = 0.0
    # desplazamiento[nivel] → matriz meses × clases
    desplazamiento: dict[str, np.ndarray] = field(default_factory=dict)


def _softmax(z: np.ndarray) -> np.ndarray:
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)


class ModeloTemporal:
    def __init__(self, indicador: str, c: float | None = None) -> None:
        self.indicador = indicador
        self.c = c

    def ajustar(self, d: pl.DataFrame, meses: list[str], suavizar: bool = True) -> ModeloTemporal:
        """`meses`: los del modelo (los posteriores al último con datos toman su nivel)."""
        self.meses = meses
        self.perfil = Modelo("valor", c=self.c, columnas=PERFIL).ajustar(d)
        self.c = self.perfil.c_elegido
        self.clases = list(self.perfil.clases)
        base = np.log(np.maximum(self.perfil.probabilidades(d), 1e-12))
        im = {m: i for i, m in enumerate(meses)}
        t = np.array([im[m] for m in d["mes"]])
        y = np.zeros((d.height, len(self.clases)))
        y[np.arange(d.height), [self.clases.index(v) for v in d["valor"]]] = 1.0
        w = d["peso"].to_numpy()
        grupos = T.config().get("interacciones", [])
        self.componentes = [Componente(NACIONAL, [NACIONAL])] + [
            Componente(g, sorted(set(d[g].unique()) - {T.DESCONOCIDO})) for g in grupos
        ]
        etiquetas = {
            c.nombre: (
                np.full(d.height, NACIONAL) if c.nombre == NACIONAL else d[c.nombre].to_numpy()
            )
            for c in self.componentes
        }
        k, nm = len(self.clases), len(meses)
        for c in self.componentes:
            c.desplazamiento = {lv: np.zeros((nm, k)) for lv in c.niveles}
        for _ in range(PASADAS):
            for c in self.componentes:
                otros = base + sum(
                    self._offset(o, etiquetas[o.nombre], t) for o in self.componentes if o is not c
                )
                p = _softmax(otros)
                obs = {}
                for lv in c.niveles:
                    sel = etiquetas[c.nombre] == lv
                    dd = np.full((nm, k), np.nan)
                    vv = np.full((nm, k), np.nan)
                    for m in np.unique(t[sel]):
                        s = sel & (t == m)
                        ws = w[s]
                        n_ef = ws.sum() ** 2 / (ws**2).sum()
                        e = (p[s] * ws[:, None]).sum(0) / ws.sum()
                        o = (y[s] * ws[:, None]).sum(0) / ws.sum()
                        o = (o * n_ef + PSEUDO * e) / (n_ef + PSEUDO)
                        dd[m] = np.log(o / e)
                        vv[m] = (1 - o) / (n_ef * o)
                    obs[lv] = (dd, vv)
                c.q = self._elegir_q(obs)
                for lv, (dd, vv) in obs.items():
                    c.desplazamiento[lv] = np.column_stack(
                        [kalman(dd[:, j], vv[:, j], c.q, suavizar)[0] for j in range(k)]
                    )
        return self

    @staticmethod
    def _elegir_q(obs: dict) -> float:
        mejor, valor = 0.0, -np.inf
        for q in Q_REJILLA:
            ll = sum(
                kalman(dd[:, j], vv[:, j], q, False)[1]
                for dd, vv in obs.values()
                for j in range(dd.shape[1])
            )
            if ll > valor:
                mejor, valor = float(q), ll
        return mejor

    def _offset(self, c: Componente, etiquetas: np.ndarray, t: np.ndarray) -> np.ndarray:
        out = np.zeros((len(t), len(self.clases)))
        for lv, m in c.desplazamiento.items():
            s = etiquetas == lv
            out[s] = m[t[s]]
        return out

    def probabilidades(self, df: pl.DataFrame, mes: str) -> np.ndarray:
        """Probabilidad de cada clase para las filas de `df` en `mes`; un mes posterior al
        último del modelo toma el último nivel. `df` necesita las columnas del perfil y de los
        grupos (con el grupo de voto que corresponda a ese mes)."""
        m = self.meses.index(mes) if mes in self.meses else len(self.meses) - 1
        z = np.log(np.maximum(self.perfil.probabilidades(df), 1e-12))
        t = np.full(df.height, m)
        for c in self.componentes:
            lab = np.full(df.height, NACIONAL) if c.nombre == NACIONAL else df[c.nombre].to_numpy()
            z = z + self._offset(c, lab, t)
        return _softmax(z)
