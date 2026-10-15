"""Cantabria: elecciones al Parlamento de Cantabria del 28 de mayo de 2023.

Fuente: BOC extraordinario núm. 46, de 7 de junio de 2023 (CVE-2023-5565), que publica tres
actas de la Junta Electoral Provincial de Cantabria (circunscripción única):

1. acta de escrutinio general (electores, votantes, nulos, blancos y votos por candidatura,
   en letra y en número);
2. acta de proclamación (repite las cifras y añade votos a candidaturas y votos válidos; la
   columna «Núm. Electos» viene vacía y los electos se listan por sigla);
3. acta de escrutinio del voto CERA (residentes ausentes).

El BOC no dice expresamente si el acta general incluye el voto CERA. Se toma el acta general
como resultado de la circunscripción y el acta CERA no se suma (sumarla podría contar dos
veces); sus cifras se dejan en `notas`. Los votos se leen en número y se contrastan con la
cifra en letra y con el acta de proclamación.
"""

from __future__ import annotations

import re
import subprocess
import unicodedata
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa06-2023" / "autonomicas_ccaa06_2023-05-28.pdf"
_NUM = r"\d{1,3}(?:\.\d{3})*"
# fila de candidatura: nº de orden, nombre (mayúsculas), cifra en letra, cifra en número
_FILA = re.compile(
    r"(?:^|\s{2,})(\d{1,2})\s+([A-ZÁÉÍÓÚÑ][^a-z]*?)\s{2,}([A-ZÁÉÍÓÚ][a-záéíóúñ ]+?)\s{2,}"
    rf"({_NUM})\s*$"
)
# fila del acta de proclamación: cifra en letra y en número (el nombre puede partirse)
_FILA_PROCL = re.compile(rf"\s{{2,}}([A-ZÁÉÍÓÚ][a-záéíóúñ ]+?)\s{{2,}}({_NUM})\s*$")

_UNIDADES = {
    "un": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7,
    "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14,
    "quince": 15, "dieciseis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
    "veinte": 20, "veintiun": 21, "veintiuno": 21, "veintidos": 22, "veintitres": 23,
    "veinticuatro": 24, "veinticinco": 25, "veintiseis": 26, "veintisiete": 27,
    "veintiocho": 28, "veintinueve": 29, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
    "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100, "ciento": 100,
    "doscientos": 200, "trescientos": 300, "cuatrocientos": 400, "quinientos": 500,
    "seiscientos": 600, "setecientos": 700, "ochocientos": 800, "novecientos": 900,
}  # fmt: skip


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _letra(s: str) -> int:
    """Cifra escrita en letra (castellano) → entero; ValueError si hay una palabra extraña."""
    s = unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()
    total, parcial = 0, 0
    for w in s.split():
        if w == "y":
            continue
        if w == "mil":
            total += (parcial or 1) * 1000
            parcial = 0
        elif w in _UNIDADES:
            parcial += _UNIDADES[w]
        else:
            raise ValueError(f"palabra no reconocida en cifra en letra: {w!r}")
    return total + parcial


def _campo(texto: str, etiqueta: str) -> int:
    m = re.search(re.escape(etiqueta) + rf"\s+({_NUM})\b", texto)
    if m is None:
        raise ValueError(f"no se encuentra «{etiqueta}» en el acta")
    return _int(m.group(1))


def _filas(pagina: str) -> list[tuple[str, int]]:
    out = []
    for ln in pagina.splitlines():
        m = _FILA.search(ln)
        if m is None:
            continue
        nombre = re.sub(r"\s+", " ", m.group(2)).strip()
        votos = _int(m.group(4))
        if _letra(m.group(3)) != votos:
            raise ValueError(f"{nombre}: cifra en letra «{m.group(3)}» ≠ {votos}")
        out.append((nombre, votos))
    return out


def leer(path: Path = PDF) -> Resultado:
    paginas = _texto(path).split("\f")
    general = next(p for p in paginas if "ACTA DE ESCRUTINIO\n" in p and "CERA" not in p)
    procl = next(p for p in paginas if "Núm. De votos a candidaturas" in p)
    cera = next(p for p in paginas if "RESIDENTES" in p and "ACTA DE ESCRUTINIO PARA" in p)

    filas = _filas(general)
    votos = dict(filas)
    if len(votos) != len(filas):
        raise ValueError("candidatura repetida en el acta general")
    # contraste con el acta de proclamación (mismo orden de candidaturas)
    votos_procl = [_int(m.group(2)) for ln in procl.splitlines() if (m := _FILA_PROCL.search(ln))]
    if votos_procl != [v for _, v in filas]:
        raise ValueError("los votos del acta de proclamación no coinciden con el acta general")
    for etq_g, etq_p in [
        ("TOTAL ELECTORES (1 + 2)", "Núm. De Electores/as"),
        ("NÚMERO DE VOTANTES", "Núm. De Votantes"),
        ("NÚMERO DEVOTOS NULOS", "Núm. De votos nulos"),
        ("NÚMERO DE VOTOS EN BLANCO", "Núm. De votos en blanco"),
    ]:
        if _campo(general, etq_g) != _campo(procl, etq_p):
            raise ValueError(f"«{etq_g}» no coincide entre acta general y de proclamación")

    circ = Circunscripcion(
        codigo="39",
        nombre="Cantabria",
        electores=_campo(general, "TOTAL ELECTORES (1 + 2)"),
        votantes=_campo(general, "NÚMERO DE VOTANTES"),
        nulos=_campo(general, "NÚMERO DEVOTOS NULOS"),
        blancos=_campo(general, "NÚMERO DE VOTOS EN BLANCO"),
        votos=votos,
        validos=_campo(procl, "Núm. De votos válidos"),
        a_candidaturas=_campo(procl, "Núm. De votos a candidaturas"),
    )

    filas_cera = _filas(cera)
    hoja_electos = next(p for p in paginas if "se proclama electos" in p)
    electos = re.findall(r"\(\d+\)\s+[^()]+?\(([^)]+)\)", hoja_electos)
    siglas: dict[str, int] = {}
    for s in electos:
        siglas[s] = siglas.get(s, 0) + 1
    notas = [
        "Circunscripción única; no se rellena `total` porque coincide con la circunscripción.",
        "El BOC no indica si el acta general incluye el voto CERA; se toma el acta general "
        "(que coincide con la de proclamación) y no se le suma el acta CERA.",
        "Acta CERA (no sumada): electores {}, votantes {}, nulos {}, blancos {}, "
        "votos a candidaturas {} ({} candidaturas).".format(
            *(
                f"{n:,}".replace(",", ".")
                for n in (
                    _campo(cera, "TOTAL ELECTORES (1 + 2)"),
                    _campo(cera, "NÚMERO DE VOTANTES"),
                    _campo(cera, "NÚMERO DEVOTOS NULOS"),
                    _campo(cera, "NÚMERO DE VOTOS EN BLANCO"),
                    sum(v for _, v in filas_cera),
                    len(filas_cera),
                )
            )
        ),
        "Escaños: la columna «Núm. Electos» del acta de proclamación está vacía y los electos "
        "se listan por sigla sin enlace explícito con el nombre de la candidatura; no se "
        "rellenan. Electos por sigla según el acta: "
        + ", ".join(f"{k} {v}" for k, v in siglas.items())
        + ".",
    ]
    return Resultado(
        ccaa="06", eleccion="autonomicas-06-2023", circunscripciones=[circ], notas=notas
    )
