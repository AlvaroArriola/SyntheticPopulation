"""Orquestación de la armonización (F2): `sinpop harmonize --source all`.

Cada paso lee sus ficheros de `data/raw/`, aplica `configs/variables.yaml` y escribe
`data/interim/<nombre>.parquet`. La armonización no usa aleatoriedad (no necesita semilla) y
ordena sus salidas, así que la misma entrada produce ficheros idénticos.

La trazabilidad (regla 7) va en `data/interim/metadata.json`, y no dentro del Parquet, para que
la fecha y la versión del código no cambien el hash del fichero (regla 6): fuentes y SHA-256 del
manifiesto, SHA-256 de `variables.yaml`, versión del código, fecha y SHA-256 de cada salida.
"""

from __future__ import annotations

import datetime as dt
import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import polars as pl

from sinpop import CONFIGS_DIR, INTERIM_DIR
from sinpop.ingest.manifest import load_manifest
from sinpop.repro import code_version, sha256_file

PADRON = "padron_continuo/ultimo/tabla_29005"


@dataclass(frozen=True)
class Paso:
    nombre: str
    fuente: str
    entradas: tuple[str, ...]  # prefijos de rutas del manifiesto
    funcion: Callable[[], pl.DataFrame]


def _pasos() -> list[Paso]:
    from sinpop.harmonize import censos, ecp, elecciones, encuestas

    tam: dict[str, str] = {}

    def t() -> dict[str, str]:
        if not tam:
            tam.update(censos.tamanos_municipales(censos.poblacion_municipal()))
        return tam

    def colectivos() -> pl.DataFrame:
        return ecp.colectivos(ecp.total(), ecp.viviendas_familiares())

    gen: list[pl.DataFrame] = []
    aut: list[pl.DataFrame] = []

    def autonomicas_(i: int) -> pl.DataFrame:
        if not aut:
            from sinpop.harmonize import autonomicas

            res, vot = [], []
            for d in autonomicas.todas().values():
                if d["resultado"] is not None:
                    r, v = d["resultado"].frames()
                    res.append(r)
                    vot.append(v)
            aut.append(pl.concat(res, how="diagonal_relaxed").sort("ccaa", "circunscripcion"))
            aut.append(
                pl.concat(vot, how="diagonal_relaxed").sort(
                    "ccaa", "circunscripcion", "candidatura"
                )
            )
        return aut[i]

    def generales(i: int) -> pl.DataFrame:
        if not gen:
            gen.extend(elecciones.generales_2023())
        return gen[i]

    return [
        Paso(
            "censo2021_personas",
            "censo2021_micro_hogares",
            ("censo2021_micro_hogares/", PADRON),
            lambda: censos.censo2021(tam=t()),
        ),
        *[
            Paso(
                f"censo_anual_muestra_{a}",
                "censo_anual_micro_completo",
                (f"censo_anual_micro_completo/{a}/", PADRON),
                lambda a=a: censos.censo_anual_muestra(a, tam=t()),
            )
            for a in ("2023", "2024", "2025")
        ],
        Paso(
            "censo_anual_exhaustivo_2025",
            "censo_anual_micro_demograficas",
            ("censo_anual_micro_demograficas/2025/", PADRON),
            lambda: censos.censo_anual_exhaustivo(tam=t()),
        ),
        Paso("ecv", "ecv", ("ecv/2025/",), encuestas.ecv),
        Paso("epa", "epa", ("epa/2T2026/",), encuestas.epa),
        Paso("tic_h", "tic_h", ("tic_h/2025/",), encuestas.tic_h),
        Paso(
            "encuesta_salud", "encuesta_salud", ("encuesta_salud/2023/",), encuestas.encuesta_salud
        ),
        Paso(
            "ecp_viviendas_familiares",
            "ecp",
            ("ecp/2026-01-01/tabla_60129",),
            ecp.viviendas_familiares,
        ),
        Paso("ecp_total", "ecp", ("ecp/2026-01-01/tabla_59589",), ecp.total),
        Paso(
            "ecp_colectivos",
            "ecp",
            ("ecp/2026-01-01/tabla_59589", "ecp/2026-01-01/tabla_60129"),
            colectivos,
        ),
        Paso("ecp_hogares", "ecp", ("ecp/2026-01-01/tabla_60133",), ecp.hogares),
        Paso(
            "elecciones_generales_2023_municipios",
            "infoelectoral_resultados",
            ("infoelectoral_resultados/generales-2023/congreso", PADRON),
            lambda: generales(0),
        ),
        Paso(
            "elecciones_generales_2023_votos",
            "infoelectoral_resultados",
            ("infoelectoral_resultados/generales-2023/congreso", PADRON),
            lambda: generales(1),
        ),
        Paso(
            "elecciones_autonomicas_circunscripciones",
            "resultados_autonomicas",
            ("resultados_autonomicas/",),
            lambda: autonomicas_(0),
        ),
        Paso(
            "elecciones_autonomicas_votos",
            "resultados_autonomicas",
            ("resultados_autonomicas/",),
            lambda: autonomicas_(1),
        ),
    ]


def fuentes_de(prefijos: tuple[str, ...]) -> list[dict[str, str]]:
    m = load_manifest()
    return [
        {"fuente": e.fuente, "fichero": e.fichero, "edicion": e.edicion, "sha256": e.sha256}
        for e in m.ficheros
        if e.tipo == "datos" and e.fichero.startswith(prefijos)
    ]


def ejecutar(fuente: str = "all", destino: Path = INTERIM_DIR) -> dict[str, dict]:
    """Ejecuta los pasos de `fuente` (id de sources.yaml, nombre de salida o 'all')."""
    from sinpop.harmonize.censos import escribir

    pasos = [p for p in _pasos() if fuente in ("all", p.fuente, p.nombre)]
    if not pasos:
        raise ValueError(f"fuente sin armonizador: {fuente}")
    meta_path = destino / "metadata.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    salidas = meta.setdefault("salidas", {})
    for p in pasos:
        df = p.funcion()
        path = escribir(df, p.nombre, destino)
        salidas[p.nombre] = {
            "fichero": path.name,
            "sha256": sha256_file(path),
            "filas": df.height,
            "fuente": p.fuente,
            "entradas": fuentes_de(p.entradas),
            "semilla": None,
        }
    meta.update(
        {
            "fase": "F2",
            "configuracion": {
                "variables.yaml": sha256_file(CONFIGS_DIR / "variables.yaml"),
            },
            "version_codigo": code_version(),
            "fecha": dt.date.today().isoformat(),
            "nota": "armonización determinista: no usa aleatoriedad ni semilla",
        }
    )
    meta["salidas"] = dict(sorted(salidas.items()))
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    return {p.nombre: salidas[p.nombre] for p in pasos}
