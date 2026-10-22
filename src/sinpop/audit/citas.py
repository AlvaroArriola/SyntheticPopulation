"""Citas de las fuentes (`docs/08` §1; G12.3) generadas desde `configs/sources.yaml` y
`data/raw/MANIFEST.yaml`, para que no se desajusten de lo que de verdad se descargó.

Comando: `python -m sinpop.audit.citas` → `docs/guias/fuentes_y_citas.md`.
"""

from __future__ import annotations

from collections import defaultdict

import yaml

from sinpop import RAW_DIR, REPO_ROOT
from sinpop.config import load_config

DESTINO = REPO_ROOT / "docs" / "guias" / "fuentes_y_citas.md"
# barómetros posteriores al corte (ventanas de validación y evaluación, D-069): no pasan por el
# manifiesto de construcción
CIS_EVALUACION = {"3571": "julio de 2026", "3577": "septiembre de 2026", "3582": "octubre de 2026"}
ESS = (
    "European Social Survey European Research Infrastructure (ESS ERIC). ESS round 11 - "
    "2023. Fichero integrado, edición 4.2 (ESS11e04_2). Sikt - Norwegian Agency for Shared "
    "Services in Education and Research. Uso no comercial previo registro."
)


def _manifiesto() -> dict[str, dict]:
    m = yaml.safe_load((RAW_DIR / "MANIFEST.yaml").read_text("utf-8"))["ficheros"]
    out: dict[str, dict] = defaultdict(lambda: {"ediciones": set(), "fechas": set()})
    for f in m:
        out[f["fuente"]]["ediciones"].add(str(f.get("edicion")))
        out[f["fuente"]]["fechas"].add(str(f.get("fecha_descarga")))
    return out


def construir() -> str:
    fuentes = load_config("sources.yaml").fuentes  # type: ignore[attr-defined]
    man = _manifiesto()
    lineas = [
        "# Fuentes y citas",
        "",
        "Generado con `python -m sinpop.audit.citas` desde `configs/sources.yaml` y "
        "`data/raw/MANIFEST.yaml` (ediciones y fechas de descarga reales). Cada informe y ficha "
        "de datos cita las fuentes que usa con estas referencias (`docs/08` §1).",
        "",
        "Los resultados de este proyecto son una **simulación** elaborada a partir de estos "
        "datos. Los organismos citados no son responsables de ellos.",
        "",
        "| Fuente | Cita | Ediciones descargadas | Condiciones |",
        "| --- | --- | --- | --- |",
    ]
    for f in fuentes:
        mf = man.get(f.id)
        if mf is None:
            continue
        eds = sorted(e for e in mf["ediciones"] if e not in ("None", "ultimo", "catalogo"))
        if f.id == "ess":
            cita = ESS
        elif f.id.startswith("cis"):
            cita = (
                f"Centro de Investigaciones Sociológicas (CIS). {f.nombre}. Estudios nº "
                f"{', '.join(eds)}. {f.url_oficial}"
            )
            eds = [f"{len(eds)} estudio{'s' if len(eds) != 1 else ''}"]
        else:
            ed = f", edición {f.edicion}" if f.edicion else ""
            cita = f"{f.organismo}. {f.nombre}{ed}. {f.url_oficial}"
        fechas = sorted(mf["fechas"])
        desc = f"{', '.join(eds) or '—'} (descarga {fechas[0]}" + (
            f" a {fechas[-1]})" if len(fechas) > 1 else ")"
        )
        lineas.append(f"| `{f.id}` | {cita} | {desc} | {f.condiciones} |")
    lineas += [
        "",
        "## Ventanas de validación y evaluación (posteriores al corte)",
        "",
        "Barómetros del CIS de la ventana de evaluación (D-069; solo los lee "
        "`src/sinpop/evaluate/`, regla 5):",
        "",
    ]
    lineas += [
        f"- Centro de Investigaciones Sociológicas (CIS). Barómetro de {mes}. Estudio nº {n}."
        for n, mes in CIS_EVALUACION.items()
    ]
    lineas += [
        "",
        "## Modelos de lenguaje",
        "",
        "Los modelos declarados en `configs/llm.yaml` (proveedor, identificador y fecha de corte "
        "de conocimiento) se citan en las salidas que los usan (`versiones.modelo_llm`). Solo "
        "reciben enunciados públicos y agregados (`docs/08` §2).",
        "",
    ]
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    texto = "\n".join(lineas)
    DESTINO.write_text(texto, "utf-8")
    return texto


if __name__ == "__main__":
    construir()
