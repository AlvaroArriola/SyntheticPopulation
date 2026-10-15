"""G2.5 · Un test por cada tabla de recodificación de `configs/variables.yaml`.

Para cada (variable, fuente) con tabla:
- todos los destinos están en el dominio declarado (categorías + NS/NC/NP);
- `recode` traduce cada código de la tabla a su destino, sin pérdidas ni filas de más;
- un código que no está en la tabla detiene el proceso (`CodigoNoDocumentado`);
- un vacío solo pasa a NP/NC si lo justifica la regla de universo.
"""

from __future__ import annotations

import polars as pl
import pytest

from sinpop.harmonize.core import CodigoNoDocumentado, dominio, recode, tabla, variables

TABLAS = sorted(
    (var, fuente)
    for var, v in variables().variables.items()
    for fuente, f in v.fuentes.items()
    if f.recodificacion
)


def test_hay_tablas() -> None:
    assert len(TABLAS) > 50


@pytest.mark.parametrize(("var", "fuente"), TABLAS, ids=[f"{v}-{f}" for v, f in TABLAS])
def test_tabla(var: str, fuente: str) -> None:
    mapa = tabla(var, fuente)
    assert mapa, "tabla vacía"
    assert set(mapa.values()) <= dominio(var), "destinos fuera de dominio"
    claves = list(mapa)
    df = pl.DataFrame({"c": claves})
    out = recode(df, "c", var, fuente)
    assert out.len() == len(claves)
    assert out.to_list() == [mapa[k.strip()] for k in claves]
    with pytest.raises(CodigoNoDocumentado):
        recode(pl.DataFrame({"c": ["__codigo_inexistente__"]}), "c", var, fuente)
    if "" not in mapa:
        with pytest.raises(CodigoNoDocumentado):
            recode(pl.DataFrame({"c": [None]}), "c", var, fuente)


def test_vacios_por_universo() -> None:
    var, fuente = TABLAS[0]
    df = pl.DataFrame({"c": [None, None], "u": [True, False], "n": [False, True]})
    out = recode(df, "c", var, fuente, np_si=pl.col("u"), nc_si=pl.col("n"))
    assert out.to_list() == ["NP", "NC"]


def test_categorias_cubiertas_por_alguna_fuente() -> None:
    """Toda categoría de una variable con tablas es alcanzable desde alguna fuente o derivada."""
    v = variables().variables
    sin_fuente = {}
    for var, d in v.items():
        tablas = [f.recodificacion for f in d.fuentes.values() if f.recodificacion]
        if not tablas or not d.categorias:
            continue
        alcanzadas = set().union(*(set(t.values()) for t in tablas))
        faltan = set(d.categorias) - alcanzadas
        if faltan:
            sin_fuente[var] = sorted(faltan)
    # Categorías que se derivan en código y no por tabla (documentadas en DECISIONS.md D-025)
    permitidas = {"edad_5", "edad_4", "tamano_municipio", "tipo_hogar", "situacion_profesional"}
    assert {k for k in sin_fuente if k not in permitidas} == set(), sin_fuente
