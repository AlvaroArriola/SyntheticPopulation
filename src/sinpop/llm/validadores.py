"""Comprobaciones semánticas de las salidas del LLM, descritas como datos (D-071, D-074).

Se describen con un diccionario (`spec`) y no con funciones para que una petición se pueda
exportar a un fichero, enviarse desde otra sesión y validarse igual en los dos lados.
"""

from __future__ import annotations

from collections.abc import Callable

TOLERANCIA_SUMA = 0.03
CAMBIO_MAX_PP = 50


def construir(spec: dict | None) -> Callable[[dict], None] | None:
    if spec is None:
        return None
    if spec["tipo"] == "distribucion":
        return _distribucion(spec["n"], spec["claves"])
    if spec["tipo"] == "evento":
        return _evento(spec["categorias"])
    raise ValueError(f"validador desconocido: {spec['tipo']}")


def _distribucion(n: int, claves: list[str]) -> Callable[[dict], None]:
    def _v(s: dict) -> None:
        dists = [("total", s["total"])] + [(x["clave"], x["distribucion"]) for x in s["subgrupos"]]
        faltan = set(claves) - {x["clave"] for x in s["subgrupos"]}
        if faltan:
            raise ValueError(f"faltan subgrupos: {sorted(faltan)[:5]}")
        for k, v in dists:
            if len(v) != n:
                raise ValueError(f"{k}: {len(v)} proporciones para {n} opciones")
            if min(v) < 0 or abs(sum(v) - 1) > TOLERANCIA_SUMA:
                raise ValueError(f"{k}: proporciones negativas o que no suman 1 ({sum(v):.3f})")

    return _v


def _evento(categorias: list[str]) -> Callable[[dict], None]:
    def _v(s: dict) -> None:
        if {x["categoria"] for x in s["categorias"]} != set(categorias):
            raise ValueError("las categorías no coinciden con las pedidas")
        if any(abs(x["cambio_pp"]) > CAMBIO_MAX_PP for x in s["categorias"]):
            raise ValueError(f"cambio de más de {CAMBIO_MAX_PP} puntos")

    return _v
