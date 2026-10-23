"""¿De qué depende la respuesta? Importancia de cada variable del perfil en una pregunta (D-090).

Para cada dimensión (edad, sexo, estudios, comunidad…) se mide cuánto separa las respuestas: la
**fuerza de la asociación** η entre la dimensión y la respuesta,

    η² = Σ_g w_g Σ_o (p_go − p_o)²  /  Σ_o p_o (1 − p_o),

donde `p_go` es la proporción de la opción `o` en el grupo `g`, `w_g` el peso del grupo y `p_o` la
proporción total. Es la razón de correlación de toda la vida (la parte de la varianza de la
respuesta que explican los grupos): 0 si todos los grupos responden igual, 1 si cada grupo da una
única respuesta. Con dos opciones coincide con la η de un análisis de varianza.

- En las **predicciones**, `p_go` sale del modelo y `w_g` del marco de la población: dice en qué
  variables se apoya la predicción (lo que el CIS ha mostrado que separa respuestas parecidas).
- En los **datos observados** (validación), cada `p_go` tiene ruido de muestreo que infla η; se
  descuenta su valor esperado, `Σ_o p_o(1−p_o) · Σ_g w_g / n_g`, con `n_g` el tamaño efectivo
  (Kish) del grupo.

Es una medida descriptiva, no causal: dos variables correlacionadas (edad y estudios) pueden
repartirse el mismo efecto. Por eso se enseña también la mayor diferencia concreta entre grupos.
"""

from __future__ import annotations

import numpy as np

NO_SUSTANTIVOS = {"NC", "NS", "NS_NC", "N.S.", "N.C.", "NP"}


def fuerza(
    grupos: dict[str, np.ndarray],
    pesos: dict[str, float],
    total: np.ndarray,
    n_efectivo: dict[str, float] | None = None,
) -> float | None:
    """η de una dimensión. `grupos` y `pesos` por nivel; `n_efectivo` solo para datos muestrales."""
    niveles = [g for g in grupos if g in pesos and pesos[g] > 0]
    if len(niveles) < 2:
        return None
    w = np.array([pesos[g] for g in niveles], dtype=float)
    w = w / w.sum()
    p = total / total.sum()
    var = float((p * (1 - p)).sum())
    if var <= 0:
        return 0.0
    entre = float(sum(wi * ((grupos[g] - p) ** 2).sum() for wi, g in zip(w, niveles, strict=True)))
    if n_efectivo:
        entre -= var * float(
            sum(wi / max(n_efectivo.get(g, 1.0), 1.0) for wi, g in zip(w, niveles, strict=True))
        )
    return float(np.sqrt(max(entre, 0.0) / var))


def importancia(
    por_subgrupo: dict[str, np.ndarray],
    pesos: dict[str, float],
    total: np.ndarray,
    opciones: list[str],
    n_efectivo: dict[str, float] | None = None,
    dimensiones: list[str] | None = None,
) -> list[dict]:
    """Dimensiones ordenadas de más a menos fuerza, con la mayor diferencia entre sus grupos.

    `por_subgrupo` y `pesos` usan claves `dimension=nivel`. Los niveles «No contesta» no cuentan."""
    dims: dict[str, dict[str, np.ndarray]] = {}
    for k, v in por_subgrupo.items():
        d, lv = k.split("=", 1)
        if lv in NO_SUSTANTIVOS or (dimensiones and d not in dimensiones):
            continue
        dims.setdefault(d, {})[lv] = np.asarray(v, dtype=float)
    sust = [j for j, o in enumerate(opciones) if o not in NO_SUSTANTIVOS]
    out = []
    for d, grupos in dims.items():
        pw = {lv: pesos.get(f"{d}={lv}", 0.0) for lv in grupos}
        nef = (
            {lv: n_efectivo[f"{d}={lv}"] for lv in grupos if f"{d}={lv}" in n_efectivo}
            if n_efectivo
            else None
        )
        f = fuerza(grupos, pw, total, nef)
        if f is None:
            continue
        validos = [lv for lv in grupos if pw[lv] > 0]
        j, dif, alto, bajo = max(
            (
                (
                    j,
                    max(grupos[g][j] for g in validos) - min(grupos[g][j] for g in validos),
                    max(validos, key=lambda g: grupos[g][j]),
                    min(validos, key=lambda g: grupos[g][j]),
                )
                for j in sust
            ),
            key=lambda x: x[1],
        )
        out.append(
            {
                "dimension": d,
                "fuerza": round(f, 4),
                "opcion": opciones[j],
                "diferencia": round(float(dif), 4),
                "grupo_alto": alto,
                "valor_alto": round(float(grupos[alto][j]), 4),
                "grupo_bajo": bajo,
                "valor_bajo": round(float(grupos[bajo][j]), 4),
            }
        )
    return sorted(out, key=lambda x: -x["fuerza"])


def pesos_marco(marco, dimensiones: list[str], peso: str = "peso") -> dict[str, float]:
    """Peso de cada grupo `dimension=nivel` en el marco de una población sintética."""
    import polars as pl

    out = {}
    for d in dimensiones:
        if d not in marco.columns:
            continue
        t = marco.group_by(pl.col(d).cast(pl.Utf8)).agg(pl.col(peso).sum()).sort(d)
        tot = float(t[peso].sum())
        for lv, w in t.iter_rows():
            if lv is not None and tot > 0:
                out[f"{d}={lv}"] = float(w) / tot
    return out
