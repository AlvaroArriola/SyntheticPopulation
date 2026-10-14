"""Reproducibilidad y trazabilidad (reglas 6 y 7 de CLAUDE.md, docs/03 sección 7)."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

import numpy as np

from sinpop import REPO_ROOT


def make_rng(seed: int) -> np.random.Generator:
    """Único punto de creación de generadores aleatorios. La semilla es obligatoria."""
    if not isinstance(seed, int | np.integer) or isinstance(seed, bool):
        raise TypeError("la semilla debe ser un entero")
    return np.random.default_rng(int(seed))


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while block := fh.read(chunk):
            h.update(block)
    return h.hexdigest()


def code_version() -> str:
    """`git:<hash>` del código (con `-dirty` si hay cambios sin confirmar)."""
    try:
        sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        dirty = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        return f"git:{sha}{'-dirty' if dirty else ''}"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "git:desconocida"
