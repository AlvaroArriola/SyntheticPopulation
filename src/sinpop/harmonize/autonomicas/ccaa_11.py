"""Extremadura: elecciones a la Asamblea de Extremadura del 21 de diciembre de 2025.

Fuente: Acuerdo de 7 de enero de 2026 de la Junta Electoral de Extremadura (DOE n.º 8, de 14 de
enero de 2026), que publica el escrutinio general por circunscripción (Badajoz y Cáceres):
electores, votantes, votos a candidaturas, en blanco, válidos y nulos; votos por candidatura y
escaños. No publica un total de la comunidad ni dice si las cifras incluyen el voto CERA.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa11-2025" / "autonomicas_ccaa11_2025-12-21.pdf"
CODIGOS = {"BADAJOZ": "06", "CÁCERES": "10"}
_RESUMEN = {
    "N.º DE ELECTORES": "electores",
    "N.º DE VOTANTES": "votantes",
    "N.º DE VOTOS A CANDIDATURAS": "a_candidaturas",
    "N.º DE VOTOS EN BLANCO": "blancos",
    "N.º DE VOTOS VÁLIDOS": "validos",
    "N.º DE VOTOS NULOS": "nulos",
}
_FILA = re.compile(r"^\s*(\S.*?)\s{2,}(\d{1,3}(?:\.\d{3})*)\s*$")


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _circunscripcion(nombre: str, bloque: list[str]) -> Circunscripcion:
    """Lee el bloque de una circunscripción: resumen, votos y escaños por candidatura."""
    resumen: dict[str, int] = {}
    votos: dict[str, int] = {}
    escanos: dict[str, int] = {}
    destino: dict[str, int] | None = None
    for ln in bloque:
        s = ln.strip()
        if "La distribución de votos" in s:
            destino = votos
            continue
        if "La distribución de los" in s and "escaños" in s:  # el DOE mete un \x07 delante
            destino = escanos
            continue
        m = _FILA.match(ln)
        if not m:
            continue
        etiqueta = re.sub(r"\s+", " ", m.group(1))
        if etiqueta in _RESUMEN:
            resumen[_RESUMEN[etiqueta]] = _int(m.group(2))
        elif destino is not None:
            if etiqueta in destino:
                raise ValueError(f"{nombre}: candidatura repetida {etiqueta!r}")
            destino[etiqueta] = _int(m.group(2))
    falta = set(_RESUMEN.values()) - set(resumen)
    if falta:
        raise ValueError(f"{nombre}: faltan {sorted(falta)}")
    return Circunscripcion(
        codigo=CODIGOS[nombre],
        nombre=nombre.title(),
        electores=resumen["electores"],
        votantes=resumen["votantes"],
        nulos=resumen["nulos"],
        blancos=resumen["blancos"],
        votos=votos,
        escanos=escanos,
        validos=resumen["validos"],
        a_candidaturas=resumen["a_candidaturas"],
    )


def leer(path: Path = PDF) -> Resultado:
    lineas = _texto(path).splitlines()
    # el bloque de resultados termina donde empieza la relación de electos
    fin = next(i for i, ln in enumerate(lineas) if "PROCLAMACIÓN DE CANDIDATURAS" in ln)
    cabeceras = [
        (i, m.group(1))
        for i, ln in enumerate(lineas[:fin])
        if (m := re.match(r"^\s*CIRCUNSCRIPCIÓN ELECTORAL DE (\S+)\s*$", ln))
    ]
    circs = []
    for k, (i, nombre) in enumerate(cabeceras):
        j = cabeceras[k + 1][0] if k + 1 < len(cabeceras) else fin
        circs.append(_circunscripcion(nombre, lineas[i + 1 : j]))
    if [c.codigo for c in circs] != ["06", "10"]:
        raise ValueError(f"circunscripciones inesperadas: {[c.nombre for c in circs]}")
    return Resultado(
        ccaa="11",
        eleccion="autonomicas-11-2025",
        circunscripciones=circs,
        notas=[
            "DOE n.º 8 (14-01-2026): sin total de la comunidad; el acuerdo no indica si las "
            "cifras incluyen el voto CERA."
        ],
    )
