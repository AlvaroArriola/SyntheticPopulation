"""Lector de ancho fijo y de diseños de registro en Excel."""

from __future__ import annotations

import openpyxl

from sinpop.ingest.readers import codelists_from_xlsx, layout_from_xlsx, read_fixed_width


def _design(tmp_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Diseño"
    ws.append(["Diseño de registro"])
    ws.append(["Variable", "Diccionario de la variable", "Longitud", "Tipo", "Descripción"])
    ws.append(["CPRO", "T_CPRO", 2, "A", "Provincia"])
    ws.append(["SEXO", "T_SEXO", 1, "A", "Sexo"])
    ws.append(["EDAD", None, 3, "N", "Edad"])
    ws.append(["RELA", "T_RELA", 2, "A", "Actividad"])
    ws.append(["*** TOTAL ***", None, 8])
    t = wb.create_sheet("Tablas1")
    t.append(["T_SEXO"])
    t.append(["Código", "Descripción"])
    t.append(["1", "Hombre"])
    t.append(["6", "Mujer"])
    t.append([])
    t.append(["T_RELA"])
    t.append(["Código", "Descripción"])
    t.append(["01", "Ocupados"])
    p = tmp_path / "dr.xlsx"
    wb.save(p)
    return p


def test_layout_and_codelists(tmp_path) -> None:
    p = _design(tmp_path)
    lay = layout_from_xlsx(p)
    assert [(c.nombre, c.longitud) for c in lay] == [
        ("CPRO", 2),
        ("SEXO", 1),
        ("EDAD", 3),
        ("RELA", 2),
    ]
    cl = codelists_from_xlsx(p)
    assert cl == {"T_SEXO": {"1": "Hombre", "6": "Mujer"}, "T_RELA": {"01": "Ocupados"}}


def test_fixed_width_pads_trimmed_lines(tmp_path) -> None:
    lay = layout_from_xlsx(_design(tmp_path))
    f = tmp_path / "md.txt"
    f.write_text("281 4501\n086 7\n", encoding="utf-8")  # segunda línea recortada
    df = read_fixed_width(f, lay)
    assert df.height == 2
    assert df.row(0) == ("28", "1", "45", "01")
    assert df.row(1) == ("08", "6", "7", "")
