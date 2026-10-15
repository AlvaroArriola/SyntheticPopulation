"""Galicia: elecciones al Parlamento de Galicia del 18 de febrero de 2024.

Fuente: Acuerdo de 4 de marzo de 2024 de la Junta Electoral de Galicia (DOG n.º 47, de 6 de
marzo de 2024). Publica (I) los resultados generales de la comunidad, (II) los resultados por
provincia (electores, votantes, votos a candidaturas, en blanco, válidos, nulos y votos por
candidatura) y (III) la relación nominal de electos por provincia y candidatura.

El acuerdo no trae una tabla de escaños: los escaños por candidatura se obtienen contando los
electos que la sección III relaciona bajo cada candidatura. Tampoco dice si las cifras incluyen
el voto CERA.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa12-2024" / "autonomicas_ccaa12_2024-02-18.pdf"
CODIGOS = {"A Coruña": "15", "Lugo": "27", "Ourense": "32", "Pontevedra": "36"}
_RESUMEN = {
    "Núm. de electores/as": "electores",
    "Núm. de votantes": "votantes",
    "Núm. de votos a candidaturas": "a_candidaturas",
    "Núm. de votos en blanco": "blancos",
    "Núm. de votos válidos": "validos",
    "Núm. de votos nulos": "nulos",
}
_FILA = re.compile(r"^\s*(\S.*?)\s{2,}(\d{1,3}(?:\.\d{3})*)\s*$")
_RUIDO = ("CVE-DOG", "ISSN", "DOG Núm.")


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _bloque(codigo: str, nombre: str, lineas: list[str]) -> Circunscripcion:
    """Lee un bloque de resultados (general o provincial): resumen y votos por candidatura."""
    resumen: dict[str, int] = {}
    votos: dict[str, int] = {}
    for ln in lineas:
        if any(r in ln for r in _RUIDO):
            continue
        m = _FILA.match(ln)
        if not m:
            continue
        etiqueta = re.sub(r"\s+", " ", m.group(1))
        if etiqueta in _RESUMEN:
            resumen[_RESUMEN[etiqueta]] = _int(m.group(2))
        else:
            if etiqueta in votos:
                raise ValueError(f"{nombre}: candidatura repetida {etiqueta!r}")
            votos[etiqueta] = _int(m.group(2))
    falta = set(_RESUMEN.values()) - set(resumen)
    if falta:
        raise ValueError(f"{nombre}: faltan {sorted(falta)}")
    return Circunscripcion(
        codigo=codigo,
        nombre=nombre,
        electores=resumen["electores"],
        votantes=resumen["votantes"],
        nulos=resumen["nulos"],
        blancos=resumen["blancos"],
        votos=votos,
        validos=resumen["validos"],
        a_candidaturas=resumen["a_candidaturas"],
    )


def _escanos(lineas: list[str]) -> dict[str, dict[str, int]]:
    """Cuenta los electos de la sección III por provincia y candidatura."""
    out: dict[str, dict[str, int]] = {}
    prov = cand = None
    for ln in lineas:
        s = ln.strip()
        if m := re.fullmatch(r"Provincia de (.+)", s):
            prov, cand = m.group(1), None
            out[prov] = {}
        elif m := re.fullmatch(r"– Por (?:el |la |los |las )?(.+):", s):
            cand = re.sub(r"\s+", " ", m.group(1))
        elif re.fullmatch(r"\d+\. \S.*", s):
            if prov is None or cand is None:
                raise ValueError(f"electo fuera de provincia o candidatura: {s!r}")
            out[prov][cand] = out[prov].get(cand, 0) + 1
    return out


def leer(path: Path = PDF) -> Resultado:
    lineas = _texto(path).splitlines()

    def pos(patron: str, desde: int = 0) -> int:
        return next(i for i in range(desde, len(lineas)) if re.search(patron, lineas[i]))

    i_gen = pos(r"^\s*Resultados generales\s*$")
    i_circ = pos(r"Resultados por circunscripciones electorales", i_gen)
    i_elec = pos(r"Relación de diputadas y deputados proclamados electos", i_circ)
    total = _bloque("total", "Galicia", lineas[i_gen + 1 : i_circ])

    cabeceras = [
        (i, m.group(1))
        for i in range(i_circ, i_elec)
        if (m := re.match(r"^\s*\d\. POR LA PROVINCIA DE (.+?)\s*$", lineas[i]))
    ]
    escanos = _escanos(lineas[i_elec:])
    circs = []
    for k, (i, nombre_may) in enumerate(cabeceras):
        j = cabeceras[k + 1][0] if k + 1 < len(cabeceras) else i_elec
        nombre = next(n for n in CODIGOS if n.upper() == nombre_may)
        c = _bloque(CODIGOS[nombre], nombre, lineas[i + 1 : j])
        c.escanos = escanos.get(nombre, {})
        desconocidas = set(c.escanos) - set(c.votos)
        if desconocidas:
            raise ValueError(f"{nombre}: electos de candidaturas sin votos {desconocidas}")
        circs.append(c)
    if [c.codigo for c in circs] != ["15", "27", "32", "36"]:
        raise ValueError(f"circunscripciones inesperadas: {[c.nombre for c in circs]}")
    notas = [
        "DOG n.º 47 (06-03-2024): total de la comunidad publicado (sección I) y contrastado "
        "con la suma de provincias.",
        "Escaños contados a partir de la relación nominal de electos (sección III); el "
        "acuerdo no trae tabla de escaños.",
        "El acuerdo no indica si las cifras incluyen el voto CERA.",
    ]
    # Discrepancia del propio DOG (sección I): se conservan las cifras publicadas.
    suma = sum(total.votos.values())
    if total.a_candidaturas != suma or total.validos != suma + total.blancos:
        notas.append(
            "Discrepancia en el documento oficial (sección I): votos a candidaturas "
            f"{total.a_candidaturas} y válidos {total.validos} publicados, frente a "
            f"{suma} y {suma + total.blancos} que dan la suma de candidaturas del total y la "
            "suma de provincias; con las cifras publicadas, válidos + nulos = "
            f"{total.validos + total.nulos} ≠ votantes {total.votantes}. Se conservan las "
            "cifras publicadas y errores() lo señala."
        )
    return Resultado(
        ccaa="12",
        eleccion="autonomicas-12-2024",
        circunscripciones=circs,
        total=total,
        notas=notas,
    )
