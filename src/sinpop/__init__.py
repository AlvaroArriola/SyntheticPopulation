"""sinpop: población sintética de las personas adultas residentes en España."""

from pathlib import Path

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
