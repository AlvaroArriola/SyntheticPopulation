"""Integerización y muestreo a tamaño N (F4, tareas 3 y 4; docs/03 §2.1).

Método TRS (*truncate, replicate, sample*): cada unidad calibrada debe aparecer
e_i = w_i · N / Σ_j w_j m_j veces (m_j = personas de la unidad). Se replica la parte entera y la
parte fraccionaria se sortea con **muestreo sistemático** sobre las unidades ordenadas
(estratificación implícita por territorio y tipo de unidad), con un arranque aleatorio que
depende de la semilla. El número de personas resultante difiere de N en unas pocas personas
(los hogares no se parten); se informa como `tamano_obtenido`.

Sobremuestreo (docs/03 §2.1): si se pide un mínimo de personas de un grupo, las unidades con
algún miembro del grupo se multiplican por β y las demás por α, con α y β tales que el tamaño
esperado sigue siendo N y el número esperado de miembros del grupo es el mínimo pedido. Cada
persona lleva `peso` = 1 / factor de su unidad, de modo que las estimaciones ponderadas
reproducen las del modo representativo.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np
import polars as pl

from sinpop.repro import make_rng

_OPS = {">=": "ge", "<=": "le", "==": "eq", "!=": "ne", ">": "gt", "<": "lt"}


@dataclass
class Sobremuestreo:
    expresion: str
    minimo: int

    def condicion(self, esquema: pl.Schema) -> pl.Expr:
        m = re.fullmatch(r"\s*(\w+)\s*(>=|<=|==|!=|>|<)\s*'?([^']+?)'?\s*", self.expresion)
        if not m:
            raise ValueError(f"expresión de sobremuestreo no válida: {self.expresion!r}")
        var, op, val = m.groups()
        if var not in esquema:
            raise ValueError(f"variable desconocida en el sobremuestreo: {var}")
        dato: object = val
        if esquema[var].is_numeric():
            dato = float(val)
        return getattr(pl.col(var), _OPS[op])(dato)


def parse_sobremuestreo(spec: str | None) -> Sobremuestreo | None:
    """'edad>=85:2000' → grupo `edad >= 85` con al menos 2.000 personas."""
    if not spec:
        return None
    expr, _, n = spec.rpartition(":")
    if not expr or not n.strip().isdigit():
        raise ValueError(f"sobremuestreo no válido: {spec!r} (formato «expresión:mínimo»)")
    return Sobremuestreo(expr, int(n))


def copias_esperadas(w: np.ndarray, m: np.ndarray, n: int) -> np.ndarray:
    return w * n / float(np.dot(w, m))


def factores_sobremuestreo(
    e: np.ndarray, m: np.ndarray, g: np.ndarray, n: int, minimo: int
) -> tuple[np.ndarray, dict]:
    """Factor por unidad. `g`: miembros del grupo en cada unidad."""
    en_g = g > 0
    esperado = float(np.dot(e, g))
    info = {"esperado_sin_sobremuestreo": esperado, "minimo": minimo}
    if esperado >= minimo:
        info |= {"alfa": 1.0, "beta": 1.0}
        return np.ones_like(e), info
    beta = minimo / esperado
    e_g = float(np.dot(e[en_g], m[en_g]))
    alfa = (n - beta * e_g) / (n - e_g)
    if alfa <= 0:
        raise ValueError(
            f"sobremuestreo imposible: {minimo} miembros exigen más de {n} personas en total"
        )
    info |= {"alfa": alfa, "beta": beta}
    return np.where(en_g, beta, alfa), info


def trs(e: np.ndarray, semilla: int) -> np.ndarray:
    """Copias enteras por unidad (en el orden dado, que debe ser el de estratificación)."""
    base = np.floor(e)
    r = e - base
    u0 = make_rng(semilla).random()
    c = np.cumsum(r)
    # Puntos u0, u0 + 1, u0 + 2…: la unidad i recibe una copia por cada punto en (c_{i-1}, c_i].
    sel = np.floor(c - u0 + 1.0) - np.floor(np.concatenate([[0.0], c[:-1]]) - u0 + 1.0)
    return (base + sel).astype(np.int64)


def equilibrar(
    c: np.ndarray,
    e: np.ndarray,
    m: np.ndarray,
    bloque: np.ndarray,
    X,
    semilla: int,
    max_iter: int = 200_000,
    z_parada: float = 0.5,
) -> tuple[np.ndarray, dict]:
    """Equilibrado posterior al TRS (variante de la fase de aterrizaje del método del cubo,
    Deville y Tillé, 2004): intercambia una copia de una unidad seleccionada por otra unidad del
    mismo bloque cuando el cambio reduce la discrepancia
    Σ_j (C_j − E_j)² / máx(E_j, 1) entre los recuentos de la muestra (C = X'c) y los esperados
    (E = X'e) en las celdas calibradas. Se trabaja siempre sobre la celda más desviada y se para
    cuando todas las desviaciones tipificadas son ≤ `z_parada` o no hay intercambio que mejore.
    Como las celdas de edad y sexo suman las personas, el tamaño también se acerca al esperado.
    Determinista con la semilla."""
    from scipy import sparse

    rng = make_rng(semilla)
    c = c.astype(np.int64).copy()
    X = sparse.csr_matrix(X)
    Xc = X.tocsc()
    E = X.T @ e
    C = X.T @ c.astype(float)
    iw = 1.0 / np.maximum(E, 1.0)
    tope = np.ceil(e).astype(np.int64) + 1  # como mucho una copia más que el TRS
    grupos: dict[int, np.ndarray] = {}
    orden = np.argsort(bloque, kind="stable")
    cortes = np.flatnonzero(np.diff(bloque[orden]) != 0) + 1
    for g in np.split(orden, cortes):
        grupos[int(bloque[g[0]])] = g

    def fila(i: int) -> tuple[np.ndarray, np.ndarray]:
        a, b = X.indptr[i], X.indptr[i + 1]
        return X.indices[a:b], X.data[a:b]

    def delta(a: int, b: int) -> float:
        ja, xa = fila(a)
        jb, xb = fila(b)
        idx = np.concatenate([ja, jb])
        val = np.concatenate([-xa, xb])
        u, inv = np.unique(idx, return_inverse=True)
        cambio = np.bincount(inv, weights=val)
        d0 = C[u] - E[u]
        return float((((d0 + cambio) ** 2 - d0**2) * iw[u]).sum())

    bloqueadas = np.zeros(len(E), dtype=bool)
    it = aceptados = 0
    inicial = float(np.max(np.abs(C - E) * np.sqrt(iw)))
    while it < max_iter:
        z = np.abs(C - E) * np.sqrt(iw)
        z[bloqueadas] = 0
        j = int(np.argmax(z))
        if z[j] <= z_parada:
            break
        col = Xc.indices[Xc.indptr[j] : Xc.indptr[j + 1]]
        exito = False
        for _ in range(30):
            it += 1
            if C[j] > E[j]:
                sel = col[c[col] > 0]
                if len(sel) == 0:
                    break
                a = int(sel[rng.integers(len(sel))])
                g = grupos[int(bloque[a])]
                b = int(g[rng.integers(len(g))])
                if c[b] >= tope[b] or e[b] <= 0 or b == a:
                    continue
            else:
                cand = col[(c[col] < tope[col]) & (e[col] > 0)]
                if len(cand) == 0:
                    break
                b = int(cand[rng.integers(len(cand))])
                g = grupos[int(bloque[b])]
                gs = g[c[g] > 0]
                if len(gs) == 0:
                    break
                a = int(gs[rng.integers(len(gs))])
                if a == b:
                    continue
            if delta(a, b) < 0:
                ja, xa = fila(a)
                jb, xb = fila(b)
                np.subtract.at(C, ja, xa)
                np.add.at(C, jb, xb)
                c[a] -= 1
                c[b] += 1
                aceptados += 1
                exito = True
                break
        if not exito:
            bloqueadas[j] = True
    final = np.abs(C - E) * np.sqrt(iw)
    return c, {
        "intercambios": aceptados,
        "propuestas": it,
        "z_max_inicial": inicial,
        "z_max_final": float(final.max()),
        "celdas": int(len(E)),
    }
