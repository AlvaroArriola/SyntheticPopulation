"""Extracción reproducible de ficheros de un ZIP oficial ya registrado (F1).

Los ficheros extraídos se guardan en `data/raw/<fuente>/<edicion>/extraido/` y se
registran en el manifiesto con la URL del ZIP más `#<miembro>`.
"""

from __future__ import annotations

import fnmatch
import zipfile
from pathlib import Path

from sinpop import RAW_DIR
from sinpop.ingest.manifest import Entry, load_manifest, register_file


def extract(fuente: str, edicion: str, patrones: list[str], raw_dir: Path = RAW_DIR) -> list[Entry]:
    m = load_manifest(raw_dir / "MANIFEST.yaml")
    zips = [
        e
        for e in m.ficheros
        if e.fuente == fuente
        and e.edicion == edicion
        and e.fichero.endswith(".zip")
        and "/extraido/" not in e.fichero
    ]
    if not zips:
        raise FileNotFoundError(f"no hay ZIP registrado para {fuente}/{edicion}")
    out: list[Entry] = []
    dest = raw_dir / fuente / edicion / "extraido"
    for z in zips:
        out += _extract_zip(
            raw_dir / z.fichero, f"{z.url_oficial}#", dest, patrones, z, fuente, edicion, raw_dir
        )
    return out


def _tipo(name: str) -> str:
    low = Path(name).name.lower()
    if low.startswith(("dr_", "dise", "disreg")) or "diseno" in low or "diseño" in low:
        return "diseno_registro"
    if low.endswith((".txt", ".pdf")) and not low.startswith("md_") and "leeme" in low:
        return "otro"
    return "datos"


def _extract_zip(
    zpath: Path,
    url_base: str,
    dest: Path,
    patrones: list[str],
    z: Entry,
    fuente: str,
    edicion: str,
    raw_dir: Path,
    depth: int = 0,
) -> list[Entry]:
    out: list[Entry] = []
    with zipfile.ZipFile(zpath) as zf:
        for name in zf.namelist():
            if name.endswith("/"):
                continue
            nested = name.lower().endswith(".zip") and depth < 2
            if not nested and not any(fnmatch.fnmatch(name, p) for p in patrones):
                continue
            target = dest / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(name) as src, open(target, "wb") as fh:
                while block := src.read(1 << 20):
                    fh.write(block)
            if nested:
                out += _extract_zip(
                    target,
                    f"{url_base}{name}#",
                    target.parent / target.stem,
                    patrones,
                    z,
                    fuente,
                    edicion,
                    raw_dir,
                    depth + 1,
                )
                target.unlink()
                continue
            out.append(
                register_file(
                    target,
                    fuente,
                    edicion,
                    f"{url_base}{name}",
                    z.condiciones,
                    tipo=_tipo(name),
                    via=z.via,
                    raw_dir=raw_dir,  # type: ignore[arg-type]
                )
            )
    return out
