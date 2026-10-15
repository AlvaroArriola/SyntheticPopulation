"""Descarga de ficheros oficiales (F1).

Solo descarga desde los dominios de los organismos oficiales declarados aquí.
Nunca se buscan copias en otros sitios (CLAUDE.md, «Descarga de datos»).
"""

from __future__ import annotations

import shutil
import time
import urllib.error
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
    "boe.es",
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
    _fetch_resumable(url, tmp, timeout=timeout)
    tmp.replace(dest)
    return register_file(
        dest, fuente, edicion, url, condiciones, tipo=tipo, via="automatica", raw_dir=raw_dir
    )


def _fetch_resumable(url: str, tmp: Path, timeout: int = 120, retries: int = 8) -> None:
    """Descarga a `tmp` reanudando con cabecera Range si la conexión se corta."""
    total: int | None = None
    for intento in range(retries):
        done = tmp.stat().st_size if tmp.exists() else 0
        if total is not None and done >= total:
            return
        req = urllib.request.Request(url, headers={"Range": f"bytes={done}-"} if done else {})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
                if done and resp.status != 206:  # el servidor no admite Range: empezar de cero
                    done = 0
                length = resp.headers.get("Content-Length")
                if length is not None:
                    total = done + int(length)
                with open(tmp, "ab" if done else "wb") as fh:
                    shutil.copyfileobj(resp, fh, length=1 << 20)
            if total is None or tmp.stat().st_size >= total:
                return
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError):
            if intento == retries - 1:
                raise
        time.sleep(min(2**intento, 30))
    raise OSError(f"descarga incompleta de {url}")


INE_TEMPUS = "https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/{tabla}?tip={tip}&{periodo}"


def download_ine_table(
    tabla: int,
    fuente: str,
    edicion: str,
    condiciones: str,
    fecha: str | None = None,
    raw_dir: Path = RAW_DIR,
    metadatos: bool = False,
) -> Entry:
    """Descarga una tabla de INEbase (API Tempus) en JSON.

    Con `metadatos=True` (tip=AM) cada serie trae los códigos de sus dimensiones.

    `fecha` en formato AAAAMMDD selecciona un único periodo; sin ella, el último publicado.
    """
    periodo = f"date={fecha}" if fecha else "nult=1"
    url = INE_TEMPUS.format(tabla=tabla, periodo=periodo, tip="AM" if metadatos else "A")
    dest_dir = raw_dir / fuente / edicion
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"tabla_{tabla}_{fecha or 'ultimo'}.json"
    tmp = dest.with_suffix(".json.part")
    tmp.unlink(missing_ok=True)
    _fetch_resumable(url, tmp, timeout=300)
    head = tmp.read_bytes()[:200]
    if not head.lstrip().startswith(b"["):
        tmp.unlink()
        raise ValueError(f"la API del INE no devolvió una tabla para {tabla}: {head!r}")
    tmp.replace(dest)
    return register_file(
        dest, fuente, edicion, url, condiciones, tipo="datos", via="automatica", raw_dir=raw_dir
    )


def download_ine_table_meta(
    tabla: int, fuente: str, edicion: str, condiciones: str, raw_dir: Path = RAW_DIR
) -> Entry:
    """Descarga la definición de dimensiones de una tabla de INEbase (su documentación)."""
    url = f"https://servicios.ine.es/wstempus/js/ES/GRUPOS_TABLA/{tabla}"
    dest = raw_dir / fuente / edicion / f"tabla_{tabla}_dimensiones.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".json.part")
    tmp.unlink(missing_ok=True)
    _fetch_resumable(url, tmp, timeout=120)
    tmp.replace(dest)
    return register_file(
        dest,
        fuente,
        edicion,
        url,
        condiciones,
        tipo="metodologia",
        via="automatica",
        raw_dir=raw_dir,
    )
