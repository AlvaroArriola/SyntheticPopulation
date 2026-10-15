"""Illes Balears, elecciones al Parlamento de 28 de mayo de 2023: SOLO voto CERA (BOIB).

Fuente: BOIB núm. 83, de 20 de junio de 2023, anuncio 5935 de la Junta Electoral de las
Illes Balears: «Datos relativos a la votación en las elecciones al Parlamento de las Illes
Balears de las personas inscritas en el Censo de los Electores Residentes-Ausentes». Trae,
por circunscripción insular, el acta de escrutinio del voto CERA (electores CERA, votantes,
blancos, nulos y votos por candidatura) y un anexo con los votos por consulado.

El fichero NO contiene los resultados generales de las circunscripciones (el escrutinio de
las mesas en territorio): solo el voto de los residentes ausentes. Por eso cada
`Circunscripcion` de este lector es únicamente el escrutinio CERA, y `electores` es el censo
CERA («Total electores» del acta CERA), no el censo total de la isla. No hay escaños (el
acta CERA no los reparte) ni total de la comunidad.

Códigos: "07-MA" Mallorca, "07-ME" Menorca, "07-EF" Eivissa (el acta dice «IBIZA»),
"07-FO" Formentera. Nombres de candidatura tal como figuran, sin el número de orden.
Se contrasta además que la suma del anexo por consulado coincide con los votantes del acta.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa04-2023" / "autonomicas_ccaa04_2023-05-28.pdf"
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


def leer(path: Path = PDF) -> Resultado:
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
