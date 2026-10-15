"""Región de Murcia: elecciones a la Asamblea Regional del 28 de mayo de 2023.

Fuente: edicto de la Junta Electoral Provincial de Murcia (BORM n.º 135, de 14 de junio de
2023, anuncio 3692) con los resultados definitivos: electores, votantes, votos válidos, nulos,
a candidaturas y en blanco; votos por candidatura (en letra y en número) y electos. La comunidad
es una sola circunscripción, así que no hay un total aparte.

El edicto publica además los votantes CERA por consulado y por país (2.640 en total), pero no
dice si las cifras generales los incluyen.

Los votos en número se contrastan con los votos en letra.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa14-2023" / "autonomicas_ccaa14_2023-05-28.pdf"
_NUM = r"\d{1,3}(?:\.\d{3})*"
_RESUMEN = {
    "ELECTORES": "electores",
    "VOTANTES": "votantes",
    "VOTOS VÁLIDOS": "validos",
    "VOTOS NULOS": "nulos",
    "VOTOS A": "a_candidaturas",  # «NÚMERO DE VOTOS A / CANDIDATURAS», partido en dos líneas
    "VOTOS EN BLANCO": "blancos",
}
# fila de candidatura: [nº] [nombre]  votos en letra  votos en número  [electos]
_FILA = re.compile(
    r"^\s*(?:(\d+)\s{2,})?(.*?)\s*"
    r"([A-ZÁÉÍÓÚ][a-záéíóúñ][a-záéíóúñ ]*?)\s{2,}(" + _NUM + r")(?:\s+(\d+))?\s*$"
)
_RUIDO = ("NPE:", "Número 135", "Página")

_UNIDADES = {
    "un": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7,
    "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14,
    "quince": 15, "dieciséis": 16, "dieciseis": 16, "diecisiete": 17, "dieciocho": 18,
    "diecinueve": 19, "veinte": 20, "veintiun": 21, "veintiuno": 21, "veintiún": 21,
    "veintidós": 22, "veintidos": 22, "veintitrés": 23, "veintitres": 23,
    "veinticuatro": 24, "veinticinco": 25, "veintiséis": 26, "veintiseis": 26,
    "veintisiete": 27, "veintiocho": 28, "veintinueve": 29, "treinta": 30, "cuarenta": 40,
    "cincuenta": 50, "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90,
    "cien": 100, "ciento": 100, "doscientos": 200, "trescientos": 300,
    "cuatrocientos": 400, "quinientos": 500, "seiscientos": 600, "setecientos": 700,
    "ochocientos": 800, "novecientos": 900,
}  # fmt: skip


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _letra(texto: str) -> int:
    """Convierte una cantidad escrita en letra (hasta millones) a número."""
    total = parcial = 0
    for p in texto.lower().split():
        if p == "y":
            continue
        if p == "mil":
            total += (parcial or 1) * 1000
            parcial = 0
        elif p in _UNIDADES:
            parcial += _UNIDADES[p]
        else:
            raise ValueError(f"palabra no reconocida en cifra en letra: {p!r} ({texto!r})")
    return total + parcial


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _une(partes: list[str]) -> str:
    """Une los trozos de un nombre partido en líneas (tras guion, sin espacio)."""
    out = ""
    for p in (re.sub(r"\s+", " ", x).strip() for x in partes):
        if not p:
            continue
        out = f"{out}{p}" if out.endswith("-") or not out else f"{out} {p}"
    return out


def _resumen(lineas: list[str]) -> dict[str, int]:
    out: dict[str, int] = {}
    pendiente = None  # etiqueta cuya cifra cae en la línea siguiente
    for ln in lineas:
        if pendiente and (m := re.match(r"^\s*(" + _NUM + r")\s", ln)):
            out[_RESUMEN[pendiente]] = _int(m.group(1))
            pendiente = None
        for m in re.finditer(r"NÚMERO DE ([A-ZÁÉÍÓÚ ]+?)(?:\s{2,}(" + _NUM + r")|\s*$)", ln):
            etiqueta = m.group(1).strip()
            if etiqueta not in _RESUMEN:
                continue
            if m.group(2) is None:
                pendiente = etiqueta
            else:
                out[_RESUMEN[etiqueta]] = _int(m.group(2))
    falta = set(_RESUMEN.values()) - set(out)
    if falta:
        raise ValueError(f"faltan cifras del resumen: {sorted(falta)}")
    return out


def _candidaturas(lineas: list[str]) -> tuple[dict[str, int], dict[str, int]]:
    votos: dict[str, int] = {}
    escanos: dict[str, int] = {}
    trozos: list[str] = []
    for ln in lineas:
        if not ln.strip() or any(r in ln for r in _RUIDO):
            continue
        m = _FILA.match(ln)
        if m is None:
            # trozo del nombre; puede llevar delante el número de orden
            mm = re.match(r"^\s*(?:(\d+)\s{2,})?(.*)$", ln)
            trozos.append(mm.group(2))
            continue
        nombre = _une([*trozos, m.group(2)])
        trozos = []
        n = _int(m.group(4))
        if _letra(m.group(3)) != n:
            raise ValueError(f"{nombre}: votos en letra {m.group(3)!r} ≠ en número {n}")
        if nombre in votos:
            raise ValueError(f"candidatura repetida {nombre!r}")
        votos[nombre] = n
        if m.group(5):
            escanos[nombre] = int(m.group(5))
    if trozos and any(t.strip() for t in trozos):
        raise ValueError(f"texto sin asignar al final de la tabla: {trozos}")
    return votos, escanos


def leer(path: Path = PDF) -> Resultado:
    lineas = _texto(path).splitlines()

    def pos(patron: str, desde: int = 0) -> int:
        return next(i for i in range(desde, len(lineas)) if re.search(patron, lineas[i]))

    i_res = pos(r"RESULTADOS ELECCIONES ASAMBLEA REGIONAL DE MURCIA")
    i_tab = pos(r"NÚMERO DE VOTOS OBTENIDO POR CADA CANDIDATURA", i_res)
    i_cab = pos(r"EN LETRA\s+EN NÚM", i_tab)
    i_fin = pos(r"De acuerdo con los resultados reflejados", i_cab)
    r = _resumen(lineas[i_res + 1 : i_tab])
    votos, escanos = _candidaturas(lineas[i_cab + 1 : i_fin])
    circ = Circunscripcion(
        codigo="30",
        nombre="Murcia",
        electores=r["electores"],
        votantes=r["votantes"],
        nulos=r["nulos"],
        blancos=r["blancos"],
        votos=votos,
        escanos=escanos,
        validos=r["validos"],
        a_candidaturas=r["a_candidaturas"],
        notas="El edicto publica aparte los votantes CERA por consulado (2.640); no dice si "
        "las cifras generales los incluyen.",
    )
    notas = [
        "BORM n.º 135 (14-06-2023): circunscripción única; sin total aparte.",
        "Votos por candidatura contrastados con las cifras en letra.",
    ]
    if circ.votantes != circ.validos + circ.nulos:
        notas.append(
            f"Discrepancia en el documento oficial: votantes publicados {circ.votantes} ≠ "
            f"válidos + nulos {circ.validos + circ.nulos} (diferencia "
            f"{circ.votantes - circ.validos - circ.nulos}); el resto de cifras cuadra "
            "(válidos = candidaturas + blancos). Se conservan las cifras publicadas y "
            "errores() lo señala."
        )
    return Resultado(
        ccaa="14", eleccion="autonomicas-14-2023", circunscripciones=[circ], notas=notas
    )
