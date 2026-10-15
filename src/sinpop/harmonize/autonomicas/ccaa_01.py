"""Andalucía: elecciones al Parlamento de Andalucía del 17 de mayo de 2026.

Fuente: Resolución de 2 de junio de 2026 de la Junta Electoral de Andalucía (BOJA n.º 108, de
8 de junio de 2026). Se leen:
- Cuadro I (resumen general): electores, votantes, válidos, a candidaturas, en blanco y nulos
  por provincia y total de Andalucía;
- Cuadro II: escaños y votos de las formaciones con escaño, por provincia y total;
- Cuadro III (varias páginas): votos de las formaciones sin escaño, por provincia y total
  («---» = la formación no concurre en esa provincia).

Los cuadros II y III están en páginas apaisadas con el nombre de cada formación partido en
varias líneas de cabecera; cada trozo de cabecera se asigna a la columna de cifras más cercana.
Los cuadros IV a VI (voto CERA) no se leen.

Voto CERA: la resolución dice que las juntas provinciales excluyeron los sobres consulares que
no cumplían los requisitos y añadieron al voto por correo el de los electores CERA que votaron
por correo desde España, y que el número de electores es el definitivo de la Oficina del Censo
Electoral; los cuadros IV-VI desglosan el voto CERA (302.074 electores y 21.583 votantes). No
dice expresamente si la columna de electores del cuadro I incluye el CERA.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

_NUM = r"\d{1,3}(?:\.\d{3})*"
PDF = AUTONOMICAS / "ccaa01-2026" / "autonomicas_ccaa01_2026-05-17.pdf"
CODIGOS = {
    "ALMERÍA": "04",
    "CÁDIZ": "11",
    "CÓRDOBA": "14",
    "GRANADA": "18",
    "HUELVA": "21",
    "JAÉN": "23",
    "MÁLAGA": "29",
    "SEVILLA": "41",
}
_NOMBRES = {
    "04": "Almería",
    "11": "Cádiz",
    "14": "Córdoba",
    "18": "Granada",
    "21": "Huelva",
    "23": "Jaén",
    "29": "Málaga",
    "41": "Sevilla",
}
# fila de datos: nombre de provincia (o TOTAL) seguido solo de cifras o «---»
_FILA = re.compile(
    r"^\s*(" + "|".join([*CODIGOS, "TOTAL"]) + r")((?:\s+(?:" + _NUM + r"|-{3,}))+)\s*$"
)
_CELDA = re.compile(r"(?<!\S)(" + _NUM + r"|-{3,})(?!\S)")
# trozos de cabecera que son texto del margen de la página, no nombres de formación
_MARGEN = re.compile(
    r"^(BOJA|Circunscripción|Boletín Oficial|Número \d+|Depósito Legal|https?://|página|\d+$)"
)


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _une(partes: list[str]) -> str:
    """Une los trozos de un nombre partido en líneas (tras guion, sin espacio)."""
    out = ""
    for p in (re.sub(r"\s+", " ", x).strip() for x in partes):
        if p:
            out = f"{out}{p}" if out.endswith("-") or not out else f"{out} {p}"
    return out


def _cuadro_i(pagina: str) -> dict[str, list[int]]:
    """Filas del cuadro I: electores, votantes, válidos, a candidaturas, blanco, nulos."""
    out = {}
    for ln in pagina.splitlines():
        m = _FILA.match(ln)
        if m:
            cifras = re.findall(r"(?<!\S)" + _NUM + r"(?!\S)", m.group(2))
            if len(cifras) != 6:
                raise ValueError(f"cuadro I, fila {m.group(1)}: {len(cifras)} cifras")
            out[m.group(1)] = [_int(x) for x in cifras]
    return out


def _tabla_formaciones(pagina: str) -> tuple[dict[str, dict[str, int]], dict[str, dict], int]:
    """Lee una página de los cuadros II o III.

    Devuelve (votos[fila][formación], escaños[fila][formación], nº de formaciones). Las filas son
    las provincias y «TOTAL». En el cuadro II cada formación ocupa dos columnas (escaños y votos)
    y la primera columna son los escaños de la circunscripción, que se contrastan con la suma.
    """
    lineas = pagina.splitlines()
    filas: dict[str, list[tuple[int, int, str]]] = {}
    i_primera = None
    for i, ln in enumerate(lineas):
        m = _FILA.match(ln)
        if m:
            off = m.start(2)
            filas[m.group(1)] = [
                (off + c.start(), off + c.end(), c.group(1)) for c in _CELDA.finditer(m.group(2))
            ]
            if i_primera is None:
                i_primera = i
    if set(filas) != {*CODIGOS, "TOTAL"}:
        raise ValueError(f"filas inesperadas: {sorted(filas)}")
    ncel = {len(v) for v in filas.values()}
    if len(ncel) != 1:
        raise ValueError(f"filas con distinto número de celdas: {ncel}")
    ncel = ncel.pop()
    i_cab = next((i for i, ln in enumerate(lineas[:i_primera]) if "Circunscripción" in ln), None)
    con_escanos = i_cab is not None and "Escaños" in lineas[i_cab]
    # extensión horizontal de cada columna de cifras
    cols = [
        (min(f[k][0] for f in filas.values()), max(f[k][1] for f in filas.values()))
        for k in range(ncel)
    ]
    if con_escanos:
        if ncel % 2 != 1:
            raise ValueError("cuadro II: número de columnas par")
        grupos = [(cols[k][0], cols[k + 1][1]) for k in range(1, ncel, 2)]
    else:
        grupos = cols
    centros = [(a + b) / 2 for a, b in grupos]
    # cabecera: líneas por encima de la primera fila, tras el título del cuadro
    i_ini = max((i for i, ln in enumerate(lineas[:i_primera]) if "CUADRO" in ln), default=-1)
    trozos: list[list[str]] = [[] for _ in grupos]
    for ln in lineas[i_ini + 1 : i_primera]:
        if con_escanos and "Escaños" in ln:
            continue
        for t in re.finditer(r"\S+(?: \S+)*", ln):
            if _MARGEN.match(t.group()):
                continue
            c = (t.start() + t.end()) / 2
            k = min(range(len(centros)), key=lambda j: abs(centros[j] - c))
            trozos[k].append(t.group())
    nombres = [_une(t) for t in trozos]
    if any(not n for n in nombres) or len(set(nombres)) != len(nombres):
        raise ValueError(f"cabeceras ilegibles: {nombres}")
    votos: dict[str, dict[str, int]] = {}
    escanos: dict[str, dict] = {}
    for fila, celdas in filas.items():
        vals = [c[2] for c in celdas]
        votos[fila], escanos[fila] = {}, {}
        if con_escanos:
            escanos[fila]["__circunscripcion__"] = _int(vals[0])
            for k, nombre in enumerate(nombres):
                e, v = vals[1 + 2 * k], vals[2 + 2 * k]
                if not v.startswith("-"):
                    votos[fila][nombre] = _int(v)
                    escanos[fila][nombre] = _int(e)
        else:
            for nombre, v in zip(nombres, vals, strict=True):
                if not v.startswith("-"):
                    votos[fila][nombre] = _int(v)
    return votos, escanos, len(nombres)


def leer(path: Path = PDF) -> Resultado:
    paginas = _texto(path).split("\f")
    i_i = next(i for i, p in enumerate(paginas) if "CUADRO I. RESUMEN GENERAL" in p)
    i_ii = next(i for i, p in enumerate(paginas) if "CUADRO II." in p)
    i_iii = next(i for i, p in enumerate(paginas) if "CUADRO III." in p)
    # el cuadro III sigue en las páginas siguientes hasta la relación de electos
    i_fin = next(
        i for i, p in enumerate(paginas) if "RELACIÓN DE DIPUTADOS PROCLAMADOS ELECTOS" in p
    )
    resumen = _cuadro_i(paginas[i_i])
    votos: dict[str, dict[str, int]] = {f: {} for f in [*CODIGOS, "TOTAL"]}
    escanos: dict[str, dict] = {f: {} for f in [*CODIGOS, "TOTAL"]}
    notas = []
    for p in [paginas[i_ii], *paginas[i_iii:i_fin]]:
        v, e, _ = _tabla_formaciones(p)
        for fila in votos:
            if set(v[fila]) & set(votos[fila]):
                raise ValueError(f"{fila}: formación repetida en varias páginas")
            votos[fila].update(v[fila])
            escanos[fila].update(e[fila])
    for fila, e in escanos.items():
        total_escanos = e.pop("__circunscripcion__")
        if sum(e.values()) != total_escanos:
            notas.append(
                f"{fila}: escaños de la circunscripción {total_escanos} ≠ suma de formaciones "
                f"{sum(e.values())} (cuadro II)."
            )

    def circ(fila: str, codigo: str, nombre: str) -> Circunscripcion:
        electores, votantes, validos, a_cand, blancos, nulos = resumen[fila]
        return Circunscripcion(
            codigo=codigo,
            nombre=nombre,
            electores=electores,
            votantes=votantes,
            nulos=nulos,
            blancos=blancos,
            votos=votos[fila],
            escanos=escanos[fila],
            validos=validos,
            a_candidaturas=a_cand,
        )

    circs = [circ(f, c, _NOMBRES[c]) for f, c in CODIGOS.items()]
    return Resultado(
        ccaa="01",
        eleccion="autonomicas-01-2026",
        circunscripciones=circs,
        total=circ("TOTAL", "total", "Andalucía"),
        notas=[
            "BOJA n.º 108 (08-06-2026): total de Andalucía publicado (fila TOTAL de los cuadros "
            "I-III) y contrastado con la suma de provincias.",
            "Resultados de las actas de escrutinio de las juntas provinciales, con el voto CERA "
            "escrutado (excluidos los sobres consulares que no cumplían los requisitos) y el CERA "
            "por correo desde España añadido al voto por correo; electores de la OCE. La "
            "resolución no dice expresamente si los electores del cuadro I incluyen el CERA.",
            *notas,
        ],
    )
