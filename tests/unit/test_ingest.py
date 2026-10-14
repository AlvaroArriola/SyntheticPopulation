"""Ingesta: manifiesto, hashes y dominios oficiales (F1)."""

from __future__ import annotations

import datetime as dt

import pytest

from sinpop.ingest.download import is_official
from sinpop.ingest.manifest import load_manifest, register_file, unregistered_files, verify


def _place(raw, fuente="padron_continuo", edicion="2026", name="t.csv", data=b"a;b\n1;2\n"):
    d = raw / fuente / edicion
    d.mkdir(parents=True)
    p = d / name
    p.write_bytes(data)
    return p


def test_register_and_verify(tmp_path) -> None:
    raw = tmp_path / "raw"
    p = _place(raw)
    e = register_file(
        p,
        "padron_continuo",
        "2026",
        "https://www.ine.es/x.csv",
        "citar INE",
        raw_dir=raw,
        fecha=dt.date(2026, 10, 14),
    )
    assert e.fichero == "padron_continuo/2026/t.csv"
    assert e.bytes == 8
    assert len(load_manifest(raw / "MANIFEST.yaml").ficheros) == 1
    assert verify(raw) == {"padron_continuo/2026/t.csv": "ok"}
    p.write_bytes(b"cambiado")
    assert verify(raw) == {"padron_continuo/2026/t.csv": "hash distinto"}
    p.unlink()
    assert verify(raw) == {"padron_continuo/2026/t.csv": "falta"}


def test_register_is_idempotent(tmp_path) -> None:
    raw = tmp_path / "raw"
    p = _place(raw)
    for _ in range(2):
        register_file(p, "padron_continuo", "2026", "https://www.ine.es/x", "c", raw_dir=raw)
    assert len(load_manifest(raw / "MANIFEST.yaml").ficheros) == 1


def test_register_rejects_file_outside_source_folder(tmp_path) -> None:
    raw = tmp_path / "raw"
    p = _place(raw, fuente="otra")
    with pytest.raises(ValueError):
        register_file(p, "padron_continuo", "2026", "https://www.ine.es/x", "c", raw_dir=raw)


def test_unregistered_files(tmp_path) -> None:
    raw = tmp_path / "raw"
    _place(raw)
    assert unregistered_files(raw) == ["padron_continuo/2026/t.csv"]


@pytest.mark.parametrize(
    "url,ok",
    [
        ("https://www.ine.es/ftp/microdatos/x.zip", True),
        ("https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/1", True),
        ("https://www.cis.es/documents/x.zip", True),
        ("https://infoelectoral.interior.gob.es/x.zip", True),
        ("http://www.ine.es/x.zip", False),
        ("https://www.ine.es.example.com/x.zip", False),
        ("https://github.com/someone/ine-mirror/x.zip", False),
    ],
)
def test_only_official_domains(url: str, ok: bool) -> None:
    assert is_official(url) is ok
