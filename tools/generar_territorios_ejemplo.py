"""Genera los territorios de ejemplo por lista de municipios de F5 (docs/04, F5, tarea 4).

Los códigos no se escriben a mano: salen del Padrón a 01/01/2025 (tabla INE 29005), por nombre
oficial (urbano) o por un criterio de población (rural). Ninguno es una delimitación oficial.
Uso: python tools/generar_territorios_ejemplo.py
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from sinpop import CONFIGS_DIR
from sinpop.harmonize.censos import PADRON_MUNI

URBANO = [
    "València",
    "Paterna",
    "Torrent",
    "Burjassot",
    "Mislata",
    "Xirivella",
    "Quart de Poblet",
    "Manises",
    "Alboraia/Alboraya",
    "Alfafar",
    "Sedaví",
    "Tavernes Blanques",
]


def municipios() -> list[tuple[str, str, int]]:
    out = []
    for s in json.loads(Path(PADRON_MUNI).read_text(encoding="utf-8")):
        md = {m["T3_Variable"]: m for m in s["MetaData"]}
        if md["Sexo"]["Codigo"] != "0" or md["Tamaño de los municipios"]["Codigo"] != "0":
            continue
        if s["Data"]:
            m = md["Municipios"]
            out.append((m["Codigo"], m["Nombre"], int(s["Data"][0]["Valor"])))
    return out


def main() -> None:
    ms = municipios()
    por_nombre = {(c[:2], n): c for c, n, _ in ms}
    faltan = [n for n in URBANO if ("46", n) not in por_nombre]
    if faltan:
        raise SystemExit(f"nombres sin código en el Padrón: {faltan}")
    urbano = {
        "nombre": "Ejemplo urbano: València y municipios de L'Horta",
        "descripcion": "Selección técnica de 12 municipios de la provincia de Valencia (no es una "
        "delimitación oficial); códigos tomados del Padrón 2025 por su nombre oficial: "
        + ", ".join(URBANO),
        "municipios": sorted(por_nombre[("46", n)] for n in URBANO),
    }
    rural = {
        "nombre": "Ejemplo rural: municipios de Teruel de menos de 2.000 habitantes",
        "descripcion": "Todos los municipios de la provincia de Teruel con menos de 2.000 "
        "habitantes en el Padrón a 01/01/2025 (criterio objetivo, no una comarca oficial)",
        "municipios": sorted(c for c, _, p in ms if c[:2] == "44" and p < 2000),
    }
    for nombre, d in (("ejemplo_valencia_urbano", urbano), ("ejemplo_teruel_rural", rural)):
        path = CONFIGS_DIR / "territorios" / f"{nombre}.yaml"
        cab = "# Generado por tools/generar_territorios_ejemplo.py (F5). No editar a mano.\n"
        path.write_text(
            cab + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=100),
            encoding="utf-8",
        )
        print(f"{path.name}: {len(d['municipios'])} municipios")


if __name__ == "__main__":
    main()
