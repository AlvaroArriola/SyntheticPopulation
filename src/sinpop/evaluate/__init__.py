"""Evaluación final (F11).

Es el ÚNICO paquete autorizado a leer o escribir en los datos de evaluación
(regla 5 de CLAUDE.md). Cualquier otro módulo que necesite guardar algo allí
(por ejemplo, los estudios del CIS posteriores a la fecha de corte en F8A)
debe hacerlo a través de las funciones de este paquete (decisión D-009).
"""

from pathlib import Path

from sinpop import DATA_DIR

EVAL_DIR: Path = DATA_DIR / "eval"
