"""Comprobación de número de registros del inventario (G1.4)."""

from __future__ import annotations

import json

from sinpop.ingest.inventory import Perfil, record_checks


def _tabla(path, valor):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            [
                {
                    "Nombre": "Total Nacional. Total. Total. Todas las edades. Dato base. ",
                    "Data": [{"Valor": valor}],
                },
                {
                    "Nombre": "Albacete. Total. Total. Todas las edades. Dato base. ",
                    "Data": [{"Valor": 1}],
                },
            ]
        ),
        encoding="utf-8",
    )


def _perfil(fuente, edicion, n):
    return Perfil(
        fuente,
        edicion,
        f"{fuente}/{edicion}/x",
        "persona",
        n,
        1,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def test_sample_and_exhaustive_counts(tmp_path) -> None:
    raw = tmp_path
    _tabla(raw / "censo_anual_tablas/2024-01-01/tabla_67988_20240101.json", 48_619_695)
    _tabla(raw / "censo_anual_tablas/ultimo/tabla_67988_ultimo.json", 49_128_297)
    _tabla(raw / "censo_anual_tablas/2021-01-01/tabla_67988_20210101.json", 47_400_798)
    perf = [
        _perfil("censo_anual_micro_completo", "2024", 4_861_970),  # = round(N/10)
        _perfil("censo_anual_micro_completo", "2025", 4_912_000),  # no cuadra
        _perfil("censo_anual_micro_demograficas", "2025", 49_128_297),
        _perfil("censo2021_micro_hogares", "2021", 4_707_186),
    ]
    rec = {(r.fichero): r for r in record_checks(perf, raw)}
    assert rec["censo_anual_micro_completo/2024/x"].ok
    assert not rec["censo_anual_micro_completo/2025/x"].ok
    assert rec["censo_anual_micro_demograficas/2025/x"].ok
    r21 = rec["censo2021_micro_hogares/2021/x"]
    assert r21.ok and not r21.declarado
