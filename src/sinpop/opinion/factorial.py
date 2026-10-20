"""Análisis factorial confirmatorio para V-LATENTE (F8A; docs/05 §7).

Máxima verosimilitud sobre la matriz de correlaciones S (n observaciones, p ítems), con un modelo
de factores correlacionados en el que cada ítem carga en un solo factor:
Σ = Λ Φ Λᵀ + Ψ, con varianzas de los factores fijadas en 1 y Ψ diagonal.

- Discrepancia: F = log|Σ| + tr(S Σ⁻¹) − log|S| − p; χ² = (n − 1) F.
- CFI = 1 − máx(χ² − gl, 0) / máx(χ²₀ − gl₀, χ² − gl, 0), con el modelo de independencia como
  referencia (χ²₀ = −(n − 1) log|S|, gl₀ = p (p − 1) / 2).
- RMSEA = √(máx(χ² − gl, 0) / (gl (n − 1))).
- Omega de McDonald por factor: (Σλ)² / ((Σλ)² + Σψ).

`semopy` no compila en el entorno (D-063); estas fórmulas son las estándar de los programas de
ecuaciones estructurales.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize


@dataclass
class AjusteCFA:
    cargas: np.ndarray  # p × k (ceros fuera del factor de cada ítem)
    phi: np.ndarray  # k × k (correlaciones entre factores)
    psi: np.ndarray  # p (unicidades)
    chi2: float
    gl: int
    cfi: float
    rmsea: float
    omega: np.ndarray  # k


def _sigma(theta: np.ndarray, asignacion: np.ndarray, k: int) -> tuple:
    p = len(asignacion)
    lam = theta[:p]
    n_phi = k * (k - 1) // 2
    r = theta[p : p + n_phi]
    psi = np.exp(theta[p + n_phi :])
    L = np.zeros((p, k))
    L[np.arange(p), asignacion] = lam
    phi = np.eye(k)
    iu = np.triu_indices(k, 1)
    phi[iu] = np.tanh(r)
    phi[(iu[1], iu[0])] = np.tanh(r)
    return L @ phi @ L.T + np.diag(psi), L, phi, psi


def ajustar(S: np.ndarray, n: int, asignacion: list[int] | np.ndarray) -> AjusteCFA:
    """S: matriz de correlaciones p × p; asignacion[i]: factor del ítem i (0..k−1)."""
    S = np.asarray(S, dtype=float)
    a = np.asarray(asignacion, dtype=int)
    p, k = len(a), int(a.max()) + 1
    _, logdet_s = np.linalg.slogdet(S)

    def f(theta: np.ndarray) -> float:
        sig, *_ = _sigma(theta, a, k)
        signo, logdet = np.linalg.slogdet(sig)
        if signo <= 0:
            return 1e10
        return float(logdet + np.trace(S @ np.linalg.inv(sig)) - logdet_s - p)

    theta0 = np.concatenate([np.full(p, 0.6), np.zeros(k * (k - 1) // 2), np.log(np.full(p, 0.6))])
    res = minimize(f, theta0, method="L-BFGS-B")
    sig, L, phi, psi = _sigma(res.x, a, k)
    chi2 = (n - 1) * res.fun
    n_par = p + k * (k - 1) // 2 + p
    gl = p * (p + 1) // 2 - n_par
    chi2_0 = -(n - 1) * logdet_s
    gl_0 = p * (p - 1) // 2
    d, d0 = max(chi2 - gl, 0.0), max(chi2_0 - gl_0, 0.0)
    cfi = 1.0 - d / max(d0, d, 1e-12)
    rmsea = float(np.sqrt(d / (gl * (n - 1)))) if gl > 0 else 0.0
    omega = np.array(
        [L[a == j, j].sum() ** 2 / (L[a == j, j].sum() ** 2 + psi[a == j].sum()) for j in range(k)]
    )
    return AjusteCFA(L, phi, psi, float(chi2), int(gl), float(cfi), rmsea, omega)


def puntuaciones(Z: np.ndarray, ajuste: AjusteCFA) -> np.ndarray:
    """Puntuaciones factoriales de regresión (Thurstone): Φ Λᵀ Σ⁻¹ z, con z tipificado."""
    sig = ajuste.cargas @ ajuste.phi @ ajuste.cargas.T + np.diag(ajuste.psi)
    return Z @ np.linalg.solve(sig, ajuste.cargas @ ajuste.phi)
