"""Illes Balears, elecciones al Parlamento de 28 de mayo de 2023.

Resultado oficial (`leer`): BOIB núm. 78, de 13 de junio de 2023, anuncio 5722 de la Junta
Electoral de las Illes Balears: actas de proclamación de cada circunscripción insular, con
electores, votantes, votos a candidaturas, blancos, válidos, nulos y votos y electos por
candidatura. Las actas no dicen si incluyen el voto CERA.

Voto CERA (`leer_cera`): BOIB núm. 83, de 20 de junio de 2023, anuncio 5935: acta de
escrutinio del voto de los residentes ausentes por circunscripción y anexo por consulado. Se
guarda como información complementaria; no se suma al resultado oficial.

Códigos: "07-MA" Mallorca, "07-ME" Menorca, "07-EF" Eivissa (el acta dice «IBIZA»),
"07-FO" Formentera. Nombres de candidatura tal como figuran, sin el número de orden.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa04-2023" / "boib78_2023_proclamacion.pdf"
PDF_CERA = AUTONOMICAS / "ccaa04-2023" / "autonomicas_ccaa04_2023-05-28.pdf"
ELECCION = "autonomicas-04-2023"

# Rótulo en el acta → (código, nombre)
CIRCUNSCRIPCIONES = {
    "MALLORCA": ("07-MA", "Mallorca"),
    "MENORCA": ("07-ME", "Menorca"),
    "IBIZA": ("07-EF", "Eivissa"),
    "FORMENTERA": ("07-FO", "Formentera"),
}
_NUM = r"(\d{1,3}(?:\.\d{3})*)"
_RESUMEN = {
    "electores": r"Total electores",
    "votantes": r"Núm\. de votantes",
    "blancos": r"Núm\. votos en blanco",
    "nulos": r"Núm\. de votos nulos",
}


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _seccion(texto: str, rotulo: str) -> dict:
    resumen: dict[str, int] = {}
    for clave, etiqueta in _RESUMEN.items():
        ms = re.findall(r"^\s*" + etiqueta + r"\s+" + _NUM + r"\s*$", texto, re.M)
        if len(ms) != 1:
            raise ValueError(f"{rotulo}: «{etiqueta}» aparece {len(ms)} veces")
        resumen[clave] = _int(ms[0])
    # Candidaturas: entre la cabecera «CANDIDATURAS  VOTOS OBTENIDOS» y el anexo
    ini = texto.index("VOTOS OBTENIDOS")
    fin = texto.index("Anexo al acta de escrutinio")
    votos: dict[str, int] = {}
    for ln in texto[ini:fin].splitlines():
        m = re.match(r"^\s*(\d+)\.\s*(\S.*?)\s{2,}" + _NUM + r"\s*$", ln)
        if not m:
            continue
        if int(m.group(1)) != len(votos) + 1:
            raise ValueError(f"{rotulo}: candidatura nº {m.group(1)} fuera de orden")
        nombre = re.sub(r"\s+", " ", m.group(2)).strip()
        if nombre in votos:
            raise ValueError(f"{rotulo}: candidatura repetida {nombre}")
        votos[nombre] = _int(m.group(3))
    # Anexo: votos por consulado (CONSULADO / PAÍS / Número de votos)
    anexo = 0
    for ln in texto[fin:].splitlines():
        m = re.match(r"^\s*\S.*?\S\s{2,}\S.*?\S\s{2,}" + _NUM + r"\s*$", ln)
        if m:
            anexo += _int(m.group(1))
    return {"resumen": resumen, "votos": votos, "anexo": anexo}


def leer_cera(path: Path = PDF_CERA) -> Resultado:
    """Escrutinio del voto CERA (BOIB núm. 83): complementario, no es el resultado oficial."""
    texto = _texto(path)
    partes = re.split(r"^\s*CIRCUMSCRIPCIÓN DE ([A-ZÁÉÍÓÚ]+)\s*$", texto, flags=re.M)
    secciones = dict(zip(partes[1::2], partes[2::2], strict=True))
    if list(secciones) != list(CIRCUNSCRIPCIONES):
        raise ValueError(f"circunscripciones inesperadas: {list(secciones)}")
    notas = [
        "El fichero contiene SOLO el escrutinio del voto CERA (residentes ausentes); faltan "
        "los resultados generales de las circunscripciones, que deben obtenerse de otra "
        "publicación oficial. Estas cifras no sirven como resultado electoral de la isla.",
        "electores = censo CERA de la circunscripción («Total electores» del acta CERA).",
        "Sin escaños: el acta CERA no los reparte.",
    ]
    circs = []
    for rotulo, (codigo, nombre) in CIRCUNSCRIPCIONES.items():
        s = _seccion(secciones[rotulo], rotulo)
        r = s["resumen"]
        if s["anexo"] != r["votantes"]:
            notas.append(
                f"{nombre}: el anexo por consulado suma {s['anexo']} votos y el acta da "
                f"{r['votantes']} votantes."
            )
        circs.append(
            Circunscripcion(
                codigo=codigo,
                nombre=nombre,
                electores=r["electores"],
                votantes=r["votantes"],
                nulos=r["nulos"],
                blancos=r["blancos"],
                votos=s["votos"],
                notas="Solo voto CERA.",
            )
        )
    return Resultado(ccaa="04", eleccion=ELECCION, circunscripciones=circs, notas=notas)


# --------------------------------------------------------------------------- resultado oficial

_PROCLAMACION = {
    "electores": r"Núm\. de electores",
    "votantes": r"Núm\. de votantes",
    "a_candidaturas": r"Núm\. votos candidaturas",
    "blancos": r"Núm\. votos en blanco",
    "validos": r"Núm\. de votos v[aá]lidos",
    "nulos": r"Núm\. de votos nulos",
}


def _proclamacion(texto: str, rotulo: str) -> tuple[dict[str, int], dict[str, int], dict]:
    resumen: dict[str, int] = {}
    for clave, etiqueta in _PROCLAMACION.items():
        ms = re.findall(r"^\s*" + etiqueta + r"\s+" + _NUM + r"\s*$", texto, re.M)
        if len(ms) != 1:
            raise ValueError(f"{rotulo}: «{etiqueta}» aparece {len(ms)} veces")
        resumen[clave] = _int(ms[0])
    ini = texto.index("VOTOS OBTENIDOS")
    fin = texto.index("De acuerdo con los resultados")
    votos: dict[str, int] = {}
    escanos: dict[str, int] = {}
    for ln in texto[ini:fin].splitlines():
        m = re.match(r"^\s*(\d+)\.\s*(\S.*?)\s{2,}" + _NUM + r"\s+(\d+)\s*$", ln)
        if not m:
            continue
        if int(m.group(1)) != len(votos) + 1:
            raise ValueError(f"{rotulo}: candidatura nº {m.group(1)} fuera de orden")
        nombre = re.sub(r"\s+", " ", m.group(2)).strip()
        votos[nombre] = _int(m.group(3))
        escanos[nombre] = int(m.group(4))
    return resumen, votos, escanos


def leer(path: Path = PDF) -> Resultado:
    """Resultado oficial por circunscripción insular (actas de proclamación, BOIB núm. 78)."""
    texto = _texto(path)
    partes = re.split(r"^\s*CIRCUMSCRIPCIÓN DE ([A-ZÁÉÍÓÚ]+)\s*$", texto, flags=re.M)
    secciones = dict(zip(partes[1::2], partes[2::2], strict=True))
    if list(secciones) != list(CIRCUNSCRIPCIONES):
        raise ValueError(f"circunscripciones inesperadas: {list(secciones)}")
    circs = []
    for rotulo, (codigo, nombre) in CIRCUNSCRIPCIONES.items():
        r, votos, escanos = _proclamacion(secciones[rotulo], rotulo)
        circs.append(
            Circunscripcion(
                codigo=codigo,
                nombre=nombre,
                electores=r["electores"],
                votantes=r["votantes"],
                nulos=r["nulos"],
                blancos=r["blancos"],
                votos=votos,
                escanos=escanos,
                validos=r["validos"],
                a_candidaturas=r["a_candidaturas"],
            )
        )
    notas = [
        "Fuente: BOIB núm. 78 (13/06/2023), anuncio 5722: actas de proclamación de la Junta "
        "Electoral de las Illes Balears.",
        "Voto CERA: las actas no dicen si lo incluyen; su escrutinio está aparte en el BOIB "
        "núm. 83 (leer_cera).",
        "Sin total de la comunidad: cada isla es una circunscripción.",
    ]
    return Resultado(ccaa="04", eleccion=ELECCION, circunscripciones=circs, notas=notas)
