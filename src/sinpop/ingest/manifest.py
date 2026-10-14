"""Manifiesto de ficheros brutos: `data/raw/MANIFEST.yaml` (docs/02, sección 6).

Cada fichero de `data/raw/<fuente>/<edicion>/` se registra con su URL oficial, la fecha
de descarga, la edición, el SHA-256, el tamaño y las condiciones de uso. Los datos no se
versionan en git; el manifiesto sí.
"""

from __future__ import annotations

import contextlib
import datetime as dt
import fcntl
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

from sinpop import RAW_DIR
from sinpop.repro import sha256_file

MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"

TipoFichero = Literal["datos", "diseno_registro", "metodologia", "cuestionario", "otro"]


class Entry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fuente: str
    fichero: str  # ruta relativa a data/raw
    tipo: TipoFichero
    edicion: str
    url_oficial: str = Field(pattern=r"^https://")
    fecha_descarga: dt.date
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    bytes: int = Field(ge=0)
    condiciones: str
    via: Literal["automatica", "manual"]


class Manifest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ficheros: list[Entry] = Field(default_factory=list)

    def get(self, fichero: str) -> Entry | None:
        return next((e for e in self.ficheros if e.fichero == fichero), None)


def load_manifest(path: Path = MANIFEST_PATH) -> Manifest:
    if not path.exists():
        return Manifest()
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return Manifest.model_validate(raw)


def save_manifest(m: Manifest, path: Path = MANIFEST_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "ficheros": [e.model_dump(mode="json") for e in sorted(m.ficheros, key=lambda e: e.fichero)]
    }
    header = "# Generado por `sinpop ingest`. No editar a mano los hashes.\n"
    tmp = path.with_suffix(".yaml.tmp")
    tmp.write_text(header + yaml.safe_dump(data, allow_unicode=True, sort_keys=False), "utf-8")
    tmp.replace(path)


def register_file(
    file: Path,
    fuente: str,
    edicion: str,
    url_oficial: str,
    condiciones: str,
    tipo: TipoFichero = "datos",
    via: Literal["automatica", "manual"] = "manual",
    raw_dir: Path = RAW_DIR,
    manifest_path: Path | None = None,
    fecha: dt.date | None = None,
) -> Entry:
    """Registra (o actualiza) un fichero que ya está en `raw_dir/<fuente>/<edicion>/`."""
    file = file.resolve()
    esperado = (raw_dir / fuente / edicion).resolve()
    if esperado not in file.parents:
        raise ValueError(f"{file} debe estar en {esperado}/")
    if not file.is_file():
        raise FileNotFoundError(file)
    mpath = manifest_path or raw_dir / "MANIFEST.yaml"
    sha = sha256_file(file)
    with _lock(mpath):
        m = load_manifest(mpath)
        rel = file.relative_to(raw_dir.resolve()).as_posix()
        entry = Entry(
            fuente=fuente,
            fichero=rel,
            tipo=tipo,
            edicion=edicion,
            url_oficial=url_oficial,
            fecha_descarga=fecha or dt.date.today(),
            sha256=sha,
            bytes=file.stat().st_size,
            condiciones=condiciones,
            via=via,
        )
        m.ficheros = [e for e in m.ficheros if e.fichero != rel] + [entry]
        save_manifest(m, mpath)
        return entry


def verify(raw_dir: Path = RAW_DIR, manifest_path: Path | None = None) -> dict[str, str]:
    """Comprueba cada entrada del manifiesto. Devuelve {fichero: 'ok'|'falta'|'hash distinto'}."""
    m = load_manifest(manifest_path or raw_dir / "MANIFEST.yaml")
    out: dict[str, str] = {}
    for e in m.ficheros:
        p = raw_dir / e.fichero
        if not p.exists():
            out[e.fichero] = "falta"
        elif sha256_file(p) != e.sha256:
            out[e.fichero] = "hash distinto"
        else:
            out[e.fichero] = "ok"
    return out


def unregistered_files(raw_dir: Path = RAW_DIR, manifest_path: Path | None = None) -> list[str]:
    """Ficheros presentes en data/raw que no figuran en el manifiesto."""
    m = load_manifest(manifest_path or raw_dir / "MANIFEST.yaml")
    known = {e.fichero for e in m.ficheros}
    ignorar = {"MANIFEST.yaml", "MANIFEST.lock", "MANUAL_DOWNLOADS.md", ".gitkeep"}
    return sorted(
        p.relative_to(raw_dir).as_posix()
        for p in raw_dir.rglob("*")
        if p.is_file()
        and p.name not in ignorar
        and p.suffix != ".part"
        and p.relative_to(raw_dir).as_posix() not in known
    )


@contextlib.contextmanager
def _lock(mpath: Path):
    """Bloqueo exclusivo del manifiesto: varias ingestas pueden correr en paralelo."""
    mpath.parent.mkdir(parents=True, exist_ok=True)
    with open(mpath.with_suffix(".lock"), "w") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)
