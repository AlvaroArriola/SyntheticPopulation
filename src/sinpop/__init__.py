"""sinpop: población sintética de las personas adultas residentes en España."""

import os
from pathlib import Path

# polars usa jemalloc, que por defecto retiene la memoria liberada: preparar los 4,7 millones de
# donantes llegaba a 11 GB de memoria residente para 1 GB de datos. Con estas opciones la
# devuelve al sistema enseguida (no cambia ningún resultado). Debe fijarse antes de importar
# polars; el `setdefault` respeta una configuración del usuario.
os.environ.setdefault(
    "_RJEM_MALLOC_CONF", "background_thread:true,dirty_decay_ms:0,muzzy_decay_ms:0"
)

__version__ = "0.1.0"

# Raíz del repositorio (src/sinpop/__init__.py -> ../../)
REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIGS_DIR = REPO_ROOT / "configs"
REPORTS_DIR = REPO_ROOT / "reports"
DATA_DIR = REPO_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
POPULATIONS_DIR = DATA_DIR / "populations"
# La ruta de los datos de evaluación solo se define en sinpop.evaluate (regla 5 de CLAUDE.md).
