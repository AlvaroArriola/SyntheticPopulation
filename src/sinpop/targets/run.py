"""`sinpop targets`: escribe los objetivos de un territorio (F3).

Salida: `data/processed/targets/<territorio>.parquet` (formato largo de `build.COLUMNAS`, con
`territorio` en lugar de `provincia`) y `data/processed/targets/metadata.json` con, por
fichero, su SHA-256, las entradas (SHA-256 de los ficheros armonizados y de las tablas
oficiales), el SHA-256 de `targets.yaml`, la versión del código y la fecha. El cálculo es
determinista (sin aleatoriedad) y las salidas se ordenan, así que su hash es reproducible.
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import polars as pl

from sinpop import CONFIGS_DIR, DATA_DIR, INTERIM_DIR
from sinpop.repro import code_version, sha256_file

DESTINO = DATA_DIR / "processed/targets"

ENTRADAS_INTERIM = [
    "ecp_total",
    "ecp_viviendas_familiares",
    "ecp_colectivos",
    "ecp_hogares",
    "censo_anual_exhaustivo_2025",
    "censo2021_personas",
]
ENTRADAS_RAW = [
    "censo_anual_tablas/ultimo/tabla_66601_ultimo.json",
    "censo_anual_tablas/ultimo/tabla_67128_ultimo.json",
    "censo_anual_tablas/ultimo/tabla_76291_ultimo.json",
    "degurba/ultimo/tabla_79341_ultimo.json",
    "padron_continuo/ultimo/tabla_29005_ultimo.json",
]


def nombre_fichero(territorio: str) -> str:
    if territorio.startswith("MUNIS:"):
        return "MUNIS_" + Path(territorio.split(":", 1)[1]).stem
    return territorio.replace(":", "_")


def _entradas() -> dict[str, str]:
    from sinpop import RAW_DIR

    meta = json.loads((INTERIM_DIR / "metadata.json").read_text(encoding="utf-8"))["salidas"]
    out = {f"interim/{n}.parquet": meta[n]["sha256"] for n in ENTRADAS_INTERIM}
    out |= {f"raw/{r}": sha256_file(RAW_DIR / r) for r in ENTRADAS_RAW}
    return out


def territorios_estandar() -> list[str]:
    from sinpop.harmonize.core import ccaa_de_provincia

    ccaa = ccaa_de_provincia()
    return (
        ["ES"]
        + [f"CCAA:{c}" for c in sorted(set(ccaa.values()))]
        + [f"PROV:{p}" for p in sorted(ccaa)]
    )


def ejecutar(territorios: list[str], destino: Path = DESTINO) -> dict[str, dict]:
    from sinpop.targets import build

    destino.mkdir(parents=True, exist_ok=True)
    meta_path = destino / "metadata.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    salidas = meta.setdefault("salidas", {})
    prov = build.provincias() if any(not t.startswith("MUNIS:") for t in territorios) else None
    entradas = _entradas()
    hechos = {}
    for t in territorios:
        if t.startswith("MUNIS:"):
            from sinpop.targets import municipios

            df = municipios.construir(Path(t.split(":", 1)[1]))
            ent = entradas | municipios.entradas()
        else:
            df = build.agregar(prov, t)
            ent = entradas
        path = destino / f"{nombre_fichero(t)}.parquet"
        df.write_parquet(path, compression="zstd", statistics=False)
        salidas[t] = {
            "fichero": path.name,
            "sha256": sha256_file(path),
            "filas": df.height,
            "entradas": ent,
            "semilla": None,
        }
        hechos[t] = salidas[t]
    meta.update(
        {
            "fase": "F3",
            "configuracion": {"targets.yaml": sha256_file(CONFIGS_DIR / "targets.yaml")},
            "version_codigo": code_version(),
            "fecha": dt.date.today().isoformat(),
            "nota": "objetivos deterministas: no usan aleatoriedad ni semilla",
        }
    )
    meta["salidas"] = dict(sorted(salidas.items()))
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    return hechos


def leer(territorio: str, destino: Path = DESTINO) -> pl.DataFrame:
    return pl.read_parquet(destino / f"{nombre_fichero(territorio)}.parquet")
