"""Calibración de los pesos de las unidades donantes (F4, tarea 2; docs/03 §2.1).

Métodos de la familia de Deville y Särndal (1992): w_i = d_i · F(x_i' λ), con λ tal que
X' w = T. Se resuelve por Newton sobre las restricciones escaladas (X_j / T_j, objetivo 1), con
mínimos cuadrados en cada paso porque las restricciones son redundantes (todos los objetivos de
persona suman lo mismo; viviendas familiares + colectivos = residentes).

- `raking`: F(u) = exp(u) (raking generalizado; equivale al IPF con las mismas marginales).
- `logit`: F acotada en [L, U] (logit truncado de Deville y Särndal): los factores de ajuste
  w/d quedan siempre dentro del rango.

Las celdas con objetivo 0 no se admiten: exigirían peso 0 a los donantes que caen en ellas.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy import sparse


@dataclass
class Resultado:
    metodo: str
    w: np.ndarray
    convergido: bool
    iteraciones: int
    desviacion_max: float  # máx |X'w / T − 1|
    historia: list[float] = field(default_factory=list)


def _f_raking(u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    e = np.exp(np.clip(u, -50, 50))
    return e, e


def _f_logit(lim: tuple[float, float]):
    lo, up = lim
    a = (up - lo) / ((1 - lo) * (up - 1))

    def f(u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        e = np.exp(np.clip(a * u, -50, 50))
        den = (up - 1) + (1 - lo) * e
        val = (lo * (up - 1) + up * (1 - lo) * e) / den
        der = a * e * (up - 1) * (1 - lo) * (up - lo) / den**2
        return val, der

    return f


def calibrar(
    X: sparse.csr_matrix,
    d: np.ndarray,
    T: np.ndarray,
    metodo: str = "raking",
    limites: tuple[float, float] = (0.2, 5.0),
    tol: float = 1e-7,
    max_iter: int = 200,
) -> Resultado:
    """Calibra `d` a los totales `T` (X: unidades × celdas)."""
    if np.any(T <= 0):
        raise ValueError("hay celdas con objetivo ≤ 0")
    if metodo == "raking":
        F = _f_raking
    elif metodo == "logit":
        F = _f_logit(limites)
    else:
        raise ValueError(f"método desconocido: {metodo}")
    Xs = sparse.csr_matrix(X @ sparse.diags(1.0 / T))  # cada restricción: X_j/T_j suma 1
    XsT = Xs.T.tocsr()
    lam = np.zeros(X.shape[1])
    historia = []

    def residuo(lam):
        val, der = F(Xs @ lam)
        w = d * val
        return w, der, XsT @ w - 1.0

    w, der, g = residuo(lam)
    conv = False
    it = 0
    for it in range(1, max_iter + 1):
        dev = float(np.max(np.abs(g)))
        historia.append(dev)
        if dev <= tol:
            conv = True
            it -= 1
            break
        H = (XsT @ sparse.diags(d * der) @ Xs).toarray()
        try:
            paso = np.linalg.lstsq(H, -g, rcond=1e-10)[0]
        except np.linalg.LinAlgError:
            # Con restricciones redundantes (p. ej. objetivos que suman lo mismo, D-050) la SVD
            # de LAPACK puede no converger; QR con pivotaje da la misma solución de mínimos
            # cuadrados de forma más robusta
            from scipy.linalg import lstsq as lstsq_sp

            paso = lstsq_sp(H, -g, cond=1e-10, lapack_driver="gelsy")[0]
        # Búsqueda en línea: se reduce el paso hasta que baje la norma del residuo.
        n0 = float(np.linalg.norm(g))
        t = 1.0
        while t > 1e-6:
            w2, der2, g2 = residuo(lam + t * paso)
            if np.all(np.isfinite(g2)) and np.linalg.norm(g2) < n0:
                break
            t /= 2
        else:
            break  # no hay paso que mejore: sin solución (p. ej. límites demasiado estrechos)
        lam = lam + t * paso
        w, der, g = w2, der2, g2
    dev = float(np.max(np.abs(g)))
    return Resultado(
        metodo=metodo,
        w=w,
        convergido=conv or dev <= tol,
        iteraciones=it,
        desviacion_max=dev,
        historia=historia,
    )


def kish(w: np.ndarray) -> float:
    """Tamaño efectivo de Kish: (Σw)² / Σw²."""
    return float(w.sum() ** 2 / np.square(w).sum())


def diagnostico(r: Resultado, d: np.ndarray, limites: tuple[float, float] = (0.2, 5.0)) -> dict:
    """V-PESOS: convergencia, factores de ajuste, Kish y pesos no positivos."""
    g = r.w / d
    q = np.quantile(g, [0, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 1])
    lo, up = limites
    return {
        "metodo": r.metodo,
        "convergido": r.convergido,
        "iteraciones": r.iteraciones,
        "desviacion_max": r.desviacion_max,
        "proporcion_en_rango": float(np.mean((g >= lo - 1e-9) & (g <= up + 1e-9))),
        "factor_cuantiles": dict(
            zip(
                ["min", "p01", "p05", "p25", "p50", "p75", "p95", "p99", "max"],
                map(float, q),
                strict=True,
            )
        ),
        "kish": kish(r.w),
        "kish_ratio": kish(r.w) / len(r.w),
        "kish_inicial_ratio": kish(d) / len(d),
        "no_positivos": int(np.sum(r.w <= 0)),
        "n_unidades": len(r.w),
    }
