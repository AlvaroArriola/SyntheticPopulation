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
