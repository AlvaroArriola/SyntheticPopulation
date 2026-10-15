"""La Rioja: elecciones al Parlamento de La Rioja del 28 de mayo de 2023.

Fuente: BOR núm. 125, de 20 de junio de 2023, págs. 12131-12190 (III.2358): publicación de la
Junta Electoral de la Comunidad Autónoma de La Rioja con el acta de escrutinio general
(pág. 12131) y el «Libro Resumen de Resultados Definitivos - Resumen General por Municipio»
(págs. 12132-12190), que incluye una fila «RESIDENTES AUSENTES». Circunscripción única
(provincia 26).

La circunscripción se toma del acta de escrutinio general. El detalle municipal se lee solo
para contrastarlo con el acta: la suma de los municipios y los residentes ausentes debe
reproducir cada cifra del acta. El acta no trae escaños, que quedan vacíos.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa17-2023" / "autonomicas_ccaa17_2023-05-28.pdf"

_NUM = r"(\d{1,3}(?:\.\d{3})*)"
_RESUMEN = {
    "electores": r"TOTAL ELECTORES: \(1\+2\):",
    "votantes": r"Nº DE VOTANTES:",
    "nulos": r"Nº DE VOTOS NULOS:",
    "blancos": r"Nº DE VOTOS EN BLANCO:",
}
# Fila de candidatura del acta: nº, nombre, votos en letra y votos en número.
_FILA = re.compile(r"^(\s+)(\d{1,2})\s+(\S.*?)\s{2,}(\S.*?)\s{2,}" + _NUM + r"\s*$")
# Fila de municipio del libro resumen: nombre, censo inicial, censo escrutado, emitidos,
# nulos, válidos, blancos, a candidaturas y la primera candidatura con sus votos.
_MUNI = re.compile(
    r"^  (\S.*?)\s{2,}" + r"\s+".join([_NUM] * 7) + r"\s+(\S.*?)\s{2,}" + _NUM + r"\s*$"
)
_SIGLA = re.compile(r"^\s{20,}(\S.*?)\s{2,}" + _NUM + r"\s*$")


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    txt = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout
    # El acta separa las palabras con un carácter que pdftotext no reconoce (U+FFFD).
    return txt.replace("�", " ")


def _acta(pagina: str) -> tuple[dict[str, int], dict[str, int]]:
    r = {}
    for clave, etiqueta in _RESUMEN.items():
        m = re.search(r"^\s*" + etiqueta + r"\s+" + _NUM + r"\s*$", pagina, re.M)
        if m is None:
            raise ValueError(f"no se encuentra «{clave}» en el acta")
        r[clave] = _int(m.group(1))
    lineas = pagina.splitlines()
    ini = next(i for i, ln in enumerate(lineas) if "CANDIDATURAS" in ln)
    entradas: list[list] = []
    col_letra = None
    for ln in lineas[ini + 1 :]:
        if ln.strip().startswith("Se extiende"):
            break
        m = _FILA.match(ln)
        if m:
            col_letra = m.start(4)
            entradas.append([m.group(3), _int(m.group(5))])
            continue
        if not ln.strip() or col_letra is None or not entradas:
            continue
        # Continuación: antes de la columna en letra es nombre; después, cifra en letra.
        if len(ln) - len(ln.lstrip()) < col_letra:
            entradas[-1][0] += " " + ln[:col_letra].strip()
    votos: dict[str, int] = {}
    for nombre, v in entradas:
        nombre = re.sub(r"\s+", " ", nombre).strip()
        if nombre in votos:
            raise ValueError(f"candidatura repetida: {nombre}")
        votos[nombre] = v
    return r, votos


def _libro(paginas: list[str]) -> tuple[list[dict[str, int]], dict[str, int]]:
    """Filas del libro resumen por municipio y suma de votos por sigla."""
    filas = []
    siglas: dict[str, int] = {}
    for p in paginas:
        for ln in p.splitlines():
            m = _MUNI.match(ln)
            if m:
                g = [_int(x) for x in m.groups()[1:8]]
                filas.append(
                    dict(
                        zip(
                            (
                                "censo_inicial",
                                "censo_escrutado",
                                "votantes",
                                "nulos",
                                "validos",
                                "blancos",
                                "a_candidaturas",
                            ),
                            g,
                            strict=True,
                        ),
                        nombre=m.group(1).strip(),
                    )
                )
                s = m.group(9).strip()
                siglas[s] = siglas.get(s, 0) + _int(m.group(10))
                continue
            m = _SIGLA.match(ln)
            if m and filas:
                s = m.group(1).strip()
                siglas[s] = siglas.get(s, 0) + _int(m.group(2))
    return filas, siglas


def leer(path: Path = PDF) -> Resultado:
    paginas = _texto(path).split("\f")
    r, votos = _acta(paginas[0])
    filas, siglas = _libro(paginas[1:])

    notas = [
        "Fuente: BOR núm. 125 de 20-6-2023 (III.2358), acta de escrutinio general de la Junta "
        "Electoral de la Comunidad Autónoma de La Rioja (2-6-2023) y libro resumen por municipio.",
        "Circunscripción única: el acta es a la vez el total de la comunidad; no se repite en "
        "`total`.",
        "El acta no trae escaños ni votos válidos ni votos a candidaturas en su resumen.",
    ]
    # Contraste con el libro resumen por municipio (incluida la fila de residentes ausentes).
    cera = [f for f in filas if f["nombre"] == "RESIDENTES AUSENTES"]
    suma = {k: sum(f[k] for f in filas) for k in ("censo_escrutado", "votantes", "nulos")}
    suma["blancos"] = sum(f["blancos"] for f in filas)
    difs = [
        f"{k}: acta {r[c]} ≠ suma del libro {suma[k]}"
        for k, c in (
            ("censo_escrutado", "electores"),
            ("votantes", "votantes"),
            ("nulos", "nulos"),
            ("blancos", "blancos"),
        )
        if r[c] != suma[k]
    ]
    # El libro usa siglas y el acta nombres completos; se comparan en el orden de la papeleta,
    # que es el mismo en ambos.
    if list(siglas.values()) != list(votos.values()):
        difs.append("los votos por sigla del libro no reproducen los del acta")
    if difs:
        notas.append("Discrepancia entre el acta y el libro por municipio: " + "; ".join(difs))
    else:
        notas.append(
            f"El libro por municipio ({len(filas) - len(cera)} municipios + residentes "
            "ausentes) reproduce exactamente electores (censo escrutado), votantes, nulos, "
            "blancos y votos por candidatura del acta."
        )
    ini = sum(f["censo_inicial"] for f in filas)
    if ini != suma["censo_escrutado"]:
        notas.append(
            f"En el libro por municipio el censo inicial suma {ini} y el censo escrutado "
            f"{suma['censo_escrutado']}; los electores del acta coinciden con el escrutado."
        )
    if cera:
        f = cera[0]
        notas.append(
            "CERA incluido: el libro por municipio trae la fila «RESIDENTES AUSENTES» "
            f"({f['censo_escrutado']} electores, {f['votantes']} votantes), que entra en la "
            "suma que reproduce el acta."
        )

    c = Circunscripcion(
        codigo="26",
        nombre="La Rioja",
        electores=r["electores"],
        votantes=r["votantes"],
        nulos=r["nulos"],
        blancos=r["blancos"],
        votos=votos,
        notas=(
            "Electores = «TOTAL ELECTORES (1+2)» del acta (certificaciones censales de alta: "
            "«---»)."
        ),
    )
    return Resultado(
        ccaa="17",
        eleccion="autonomicas-17-2023",
        circunscripciones=[c],
        total=None,
        notas=notas,
    )
