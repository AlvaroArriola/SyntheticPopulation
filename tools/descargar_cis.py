"""Descarga de estudios del CIS desde su web oficial (F8A).

La web del CIS limita las peticiones (429) y corta conexiones, así que se va despacio: una
petición cada `PAUSA` segundos, reintentos con espera creciente y caché de las páginas ya
leídas (`data/raw/cis_catalogo/`). Solo se descargan ficheros de `www.cis.es`.

- Catálogo: las fichas de estudio (número, título, fecha y enlace) de las páginas del
  catálogo, hasta la fecha `DESDE`.
- Ficha: los enlaces a microdatos (`MD<n>.zip`), cuestionario (`cues<n>.pdf`) y ficha técnica
  (`FT<n>.pdf`).
- Destino: `data/raw/cis_barometros/<n>/` si la fecha de la ficha es anterior al corte
  (01/07/2026); si no, `data/eval/cis/<n>/` (datos de evaluación, CLAUDE.md regla 5).

Uso: `python tools/descargar_cis.py [--tipos barometro,sanitario] [--max-paginas 12]`
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

from sinpop import DATA_DIR, RAW_DIR  # noqa: E402
from sinpop.ingest.download import download  # noqa: E402

BASE = "https://www.cis.es"
CATALOGO = BASE + "/en/studies/catalogue?catalogo=estudio&sort=createDateBDE-&t=0&start={}"
CACHE = RAW_DIR / "cis_catalogo"
DESDE = dt.date(2023, 1, 1)
CORTE = dt.date(2026, 7, 1)
PAUSA = 25
CONDICIONES = "CIS: citar el número de estudio y al CIS como fuente"
TIPOS = {
    "barometro": re.compile(r"^Barómetro de [a-zé]+ \d{4}$", re.I),
    "sanitario": re.compile(r"^Barómetro sanitario", re.I),
    "postelectoral_generales": re.compile(r"^Postelectoral elecciones generales", re.I),
}


def _get(url: str, reintentos: int = 6) -> str:
    espera = 60
    for i in range(reintentos):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                texto = r.read().decode("utf-8", errors="ignore")
            time.sleep(PAUSA)
            return texto
        except Exception as exc:  # 429, cortes de conexión, tiempo agotado
            print(f"  fallo ({exc}); reintento {i + 1} en {espera} s", flush=True)
            time.sleep(espera)
            espera = min(espera * 2, 900)
    raise RuntimeError(f"no se pudo leer {url}")


def _pagina(url: str, nombre: str) -> str:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / nombre
    if f.exists():
        return f.read_text("utf-8")
    texto = _get(url)
    f.write_text(texto, "utf-8")
    return texto


def catalogo(max_paginas: int) -> list[dict]:
    patron = re.compile(
        r'alt="([^"]+)"[\s\S]{0,600}?<a href="([^"]+)"[\s\S]{0,800}?Study (\d+)\s*</li>\s*'
        r"<li>(\d{2})/(\d{2})/(\d{4})</li>"
    )
    estudios: dict[str, dict] = {}
    for p in range(1, max_paginas + 1):
        texto = _pagina(CATALOGO.format(p), f"catalogo_{p:03d}.html")
        filas = patron.findall(texto)
        for titulo, url, n, d, m, a in filas:
            estudios[n] = {
                "estudio": n,
                "titulo": titulo,
                "url": url,
                "fecha": dt.date(int(a), int(m), int(d)).isoformat(),
            }
        fechas = [dt.date(int(a), int(m), int(d)) for *_, d, m, a in filas]
        print(f"página {p}: {len(filas)} estudios", flush=True)
        if not filas or min(fechas) < DESDE:
            break
    return sorted(estudios.values(), key=lambda e: e["fecha"])


def ficheros(estudio: dict) -> list[str]:
    texto = _pagina(estudio["url"], f"estudio_{estudio['estudio']}.html")
    n = estudio["estudio"]
    enlaces = re.findall(r'href="([^"]*documents/20117/[^"]+)"', texto)
    utiles = [e for e in enlaces if re.search(rf"/(MD{n}\.zip|cues{n}\.pdf|FT{n}\.pdf)$", e, re.I)]
    return sorted({e if e.startswith("http") else BASE + e for e in utiles})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tipos", default="barometro,sanitario")
    ap.add_argument("--max-paginas", type=int, default=12)
    args = ap.parse_args()
    tipos = [TIPOS[t] for t in args.tipos.split(",")]
    lista = [
        e
        for e in catalogo(args.max_paginas)
        if dt.date.fromisoformat(e["fecha"]) >= DESDE and any(t.search(e["titulo"]) for t in tipos)
    ]
    (CACHE / "seleccion.json").write_text(json.dumps(lista, ensure_ascii=False, indent=1), "utf-8")
    print(f"{len(lista)} estudios seleccionados", flush=True)
    for e in lista:
        posterior = dt.date.fromisoformat(e["fecha"]) >= CORTE
        raw = DATA_DIR / "eval" if posterior else RAW_DIR
        fuente = "cis" if posterior else "cis_barometros"
        destino = raw / fuente / e["estudio"]
        for url in ficheros(e):
            nombre = url.rsplit("/", 1)[-1]
            if (destino / nombre).exists():
                continue
            tipo = (
                "datos"
                if nombre.upper().startswith("MD")
                else "cuestionario"
                if nombre.lower().startswith("cues")
                else "metodologia"
            )
            download(url, fuente, e["estudio"], CONDICIONES, tipo=tipo, raw_dir=raw)
            print(f"  {e['estudio']} {e['titulo']}: {nombre}", flush=True)
            time.sleep(PAUSA)


if __name__ == "__main__":
    main()
