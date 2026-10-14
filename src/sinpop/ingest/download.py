"""Descarga de ficheros oficiales (F1).

Solo descarga desde los dominios de los organismos oficiales declarados aquí.
Nunca se buscan copias en otros sitios (CLAUDE.md, «Descarga de datos»).
"""

from __future__ import annotations

import shutil
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from sinpop import RAW_DIR
from sinpop.ingest.manifest import Entry, register_file

OFFICIAL_DOMAINS = (
    "ine.es",
    "cis.es",
    "interior.gob.es",
    "sanidad.gob.es",
    "europeansocialsurvey.org",
    "sikt.no",
    "gencat.cat",
    "ehu.eus",
    "europa.eu",
)


def is_official(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return urlparse(url).scheme == "https" and any(
        host == d or host.endswith("." + d) for d in OFFICIAL_DOMAINS
    )


def download(
    url: str,
    fuente: str,
    edicion: str,
    condiciones: str,
    tipo: str = "datos",
    raw_dir: Path = RAW_DIR,
    timeout: int = 120,
) -> Entry:
    if not is_official(url):
        raise ValueError(f"{url} no pertenece a un dominio oficial declarado")
    dest_dir = raw_dir / fuente / edicion
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = Path(urlparse(url).path).name or "descarga"
    dest = dest_dir / name
    tmp = dest.with_suffix(dest.suffix + ".part")
    with urllib.request.urlopen(url, timeout=timeout) as resp, open(tmp, "wb") as fh:  # noqa: S310
        shutil.copyfileobj(resp, fh)
    tmp.replace(dest)
    return register_file(
        dest, fuente, edicion, url, condiciones, tipo=tipo, via="automatica", raw_dir=raw_dir
    )
