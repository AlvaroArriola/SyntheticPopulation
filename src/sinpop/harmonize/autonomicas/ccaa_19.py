"""Melilla: elecciones a la Asamblea de Melilla del 28 de mayo de 2023.

Misma fuente que Ceuta (`ccaa_18`): BOE núm. 261, de 1 de noviembre de 2023
(BOE-A-2023-22387), resumen de resultados de las elecciones locales publicado por la Junta
Electoral Central. Melilla está en la pág. 146077 del BOE (última del PDF). Circunscripción
única (código 52).
"""

from __future__ import annotations

from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Resultado
from sinpop.harmonize.autonomicas.ccaa_18 import leer_ciudad, notas_boe

PDF = AUTONOMICAS / "ccaa19-2023" / "autonomicas_ccaa19_2023-05-28.pdf"


def leer(path: Path = PDF) -> Resultado:
    c = leer_ciudad(path, "MELILLA", "52", "Melilla")
    return Resultado(
        ccaa="19",
        eleccion="autonomicas-19-2023",
        circunscripciones=[c],
        total=None,
        notas=notas_boe("Melilla"),
    )
