"""Comunidad de Madrid: elecciones a la Asamblea de Madrid del 28 de mayo de 2023.

Fuente: BOCM núm. 136, de 9 de junio de 2023, págs. 215-217, anuncio 72 (BOCM-20230609-72):
acta de proclamación de la Junta Electoral Provincial de Madrid. Circunscripción única
(provincia 28).

El acta da electores, votantes, votos a candidatura, en blanco, válidos y nulos, y para cada
candidatura los votos (en letra y en número) y los electos. Se leen las cifras en número; la
cifra en letra se ignora.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa13-2023" / "autonomicas_ccaa13_2023-05-28.pdf"

_NUM = r"(\d{1,3}(?:\.\d{3})*)"
_RESUMEN = {
    "electores": r"N\.º DE ELECTORES(?: \(1\))?",
    "votantes": r"N\.º DE VOTANTES",
    "a_candidaturas": r"N\.º DE VOTOS A CANDIDATURA",
    "blancos": r"N\.º DE VOTOS EN BLANCO",
    "validos": r"N\.º DE VOTOS VÁLIDOS(?: \(2\))?",
    "nulos": r"N\.º DE VOTOS NULOS",
}
# Fila de candidatura: nº, nombre, votos en letra, votos en número y, si los hay, electos.
_FILA = re.compile(r"^(\s+)(\d{1,2})\s{2,}(\S.*?)\s{2,}(\S.*?)\s{2,}" + _NUM + r"(?:\s+(\d+))?\s*$")


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _resumen(txt: str) -> dict[str, int]:
    out = {}
    for clave, etiqueta in _RESUMEN.items():
        m = re.search(r"^\s*" + etiqueta + r"\s+" + _NUM + r"\s*$", txt, re.M)
        if m is None:
            raise ValueError(f"no se encuentra «{clave}» en el acta")
        out[clave] = _int(m.group(1))
    return out


def _candidaturas(txt: str) -> tuple[dict[str, int], dict[str, int]]:
    """Votos y electos por candidatura; los nombres en varias líneas se unen."""
    lineas = txt.splitlines()
    ini = next(i for i, ln in enumerate(lineas) if ln.rstrip().endswith(" CANDIDATURAS"))
    entradas: list[list] = []  # [nombre, votos, electos]
    col_letra = None
    for ln in lineas[ini + 1 :]:
        if ln.strip().startswith("(1)"):
            break  # notas al pie del cuadro
        m = _FILA.match(ln)
        if m:
            col_letra = m.start(4)
            electos = int(m.group(6)) if m.group(6) else None
            entradas.append([m.group(3), _int(m.group(5)), electos])
            continue
        if not ln.strip() or col_letra is None or not entradas:
            continue
        # Línea de continuación: si empieza antes de la columna de la cifra en letra, es
        # parte del nombre; si no, es continuación de la cifra en letra y se ignora.
        sangria = len(ln) - len(ln.lstrip())
        if sangria < col_letra:
            entradas[-1][0] += " " + ln[:col_letra].strip()
    votos: dict[str, int] = {}
    escanos: dict[str, int] = {}
    for nombre, v, e in entradas:
        nombre = re.sub(r"\s+", " ", nombre).strip()
        if nombre in votos:
            raise ValueError(f"candidatura repetida: {nombre}")
        votos[nombre] = v
        if e is not None:
            escanos[nombre] = e
    return votos, escanos


def leer(path: Path = PDF) -> Resultado:
    txt = _texto(path)
    r = _resumen(txt)
    votos, escanos = _candidaturas(txt)
    c = Circunscripcion(
        codigo="28",
        nombre="Madrid",
        electores=r["electores"],
        votantes=r["votantes"],
        nulos=r["nulos"],
        blancos=r["blancos"],
        votos=votos,
        escanos=escanos,
        validos=r["validos"],
        a_candidaturas=r["a_candidaturas"],
        notas=(
            "Electores según nota (1) del acta: «Los que figuran en la lista del Censo "
            "Electoral más las certificaciones censales aportadas»."
        ),
    )
    return Resultado(
        ccaa="13",
        eleccion="autonomicas-13-2023",
        circunscripciones=[c],
        total=None,
        notas=[
            "Fuente: BOCM núm. 136 de 9-6-2023, anuncio 72 (acta de proclamación de la Junta "
            "Electoral Provincial de Madrid, 5-6-2023).",
            "Circunscripción única: el acta es a la vez el total de la comunidad; no se repite "
            "en `total`.",
            "La publicación no dice si los electores y votantes incluyen el CERA.",
        ],
    )
