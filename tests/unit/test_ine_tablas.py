"""Lector de tablas INEbase con metadatos."""

from __future__ import annotations

import json

from sinpop.ingest.ine_tablas import leer


def _serie(dims: dict[str, tuple[str, str]], valor: float | None) -> dict:
    md = [{"T3_Variable": k, "Nombre": n, "Codigo": c} for k, (n, c) in dims.items()]
    md.append({"T3_Variable": "Tipo de dato", "Nombre": "Número", "Codigo": ""})
    data = [] if valor is None else [{"Fecha": "2026-01-01T00:00:00", "Valor": valor}]
    return {"Nombre": "x", "MetaData": md, "Data": data}


def test_dimension_that_appears_late_is_kept(tmp_path) -> None:
    series = [_serie({"Total Nacional": ("Total Nacional", "")}, 10.0) for _ in range(150)]
    series.append(_serie({"Provincias": ("Albacete", "02")}, 3.0))
    series.append(_serie({"Provincias": ("Soria", "42")}, None))  # sin dato: se ignora
    p = tmp_path / "t.json"
    p.write_text(json.dumps(series), encoding="utf-8")
    df = leer(p)
    assert df.height == 151
    assert df.filter(df["Provincias"] == "Albacete")["Provincias__cod"].to_list() == ["02"]
