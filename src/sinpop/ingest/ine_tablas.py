"""Lectura de tablas de INEbase descargadas con metadatos (tip=AM) en formato largo."""

from __future__ import annotations

import json
from pathlib import Path

import polars as pl


def leer(path: Path) -> pl.DataFrame:
    """Una fila por serie y periodo; una columna por dimensión (nombre) y `<dim>__cod`."""
    filas = []
    for s in json.loads(path.read_text(encoding="utf-8")):
        dims = {}
        for m in s.get("MetaData", []):
            var = m["T3_Variable"]
            if var == "Tipo de dato":
                continue
            dims[var] = m["Nombre"].strip()
            dims[f"{var}__cod"] = str(m.get("Codigo", ""))
        for d in s["Data"]:
            if d.get("Valor") is None:
                continue
            # Las tablas de operaciones no periódicas (p. ej. la ESdE) no traen «Fecha»
            fecha = d["Fecha"][:10] if d.get("Fecha") else None
            filas.append({**dims, "fecha": fecha, "valor": float(d["Valor"])})
    return pl.DataFrame(filas, infer_schema_length=None)
