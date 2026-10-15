"""Cataluña: elecciones al Parlamento de Cataluña del 12 de mayo de 2024.

Fuente: DOGC núm. 9178, de 6 de junio de 2024 (CVE-DOGC-B-24157038-2024): acuerdo de 4 de junio
de 2024 de la Junta Electoral Central que publica, según las actas de escrutinio general y de
proclamación de las juntas provinciales:

- Cuadro I: electores, votantes, votos a candidaturas, en blanco, válidos y nulos por
  provincia y total. Los electores son, según el acuerdo, el total de residentes en España,
  residentes ausentes (CERA) y certificaciones censales de alta, con datos definitivos de la
  Oficina del Censo Electoral;
- Cuadro II: votos y escaños por candidatura, provincia y total (celdas vacías = sin dato; los
  escaños vacíos no se rellenan).

El acuerdo se publica en castellano (páginas 1-8) y en aranés (9-16). Se lee la versión en
castellano y se contrasta con la aranesa cifra a cifra. Los nombres de candidatura ocupan
varias líneas: se unen con un espacio, salvo cuando la línea acaba en guion, que se une sin
espacio («(PSC-\\nPSOE)» → «(PSC-PSOE)»).
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa09-2024" / "autonomicas_ccaa09_2024-05-12.pdf"
PROVINCIAS = {"Barcelona": "08", "Girona": "17", "Lleida": "25", "Tarragona": "43"}
_NOMBRE_ARANES = {"Lhèida": "Lleida"}
# las cifras llevan punto de millares, salvo alguna errata del DOGC («297164»)
_NUM = r"\d{1,3}(?:\.\d{3})+|\d+"
_PAGINA = "<<salto de página>>"
_RESUMEN = ["electores", "votantes", "a_candidaturas", "blancos", "validos", "nulos"]


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _une(partes: list[str]) -> str:
    out = ""
    for p in partes:
        p = re.sub(r"\s+", " ", p).strip()
        if not p:
            continue
        out = f"{out}{p}" if (not out or out.endswith("-")) else f"{out} {p}"
    return out


def _cuadro_i(lineas: list[str]) -> dict[str, dict[str, int]]:
    out: dict[str, dict[str, int]] = {}
    nombres = "|".join([*PROVINCIAS, *_NOMBRE_ARANES, "TOTAL"])
    patron = re.compile(rf"^\s*({nombres})" + rf"\s+({_NUM})" * 6 + r"\s*$")
    for ln in lineas:
        m = patron.match(ln)
        if m:
            nombre = _NOMBRE_ARANES.get(m.group(1), m.group(1))
            out[nombre] = {k: _int(v) for k, v in zip(_RESUMEN, m.groups()[1:], strict=True)}
    return out


def _es_cabecera(tokens: list[str], votos_etq: str) -> bool:
    return len(tokens) == 10 and tokens[0::2] == [votos_etq] * 5


def _cuadro_ii(lineas: list[str], votos_etq: str) -> list[tuple[str, dict[str, tuple]]]:
    """Filas (candidatura, {columna: (votos|None, escaños|None)}) del Cuadro II.

    El ancho de las columnas cambia de una página a otra, así que en cada página se toman como
    referencia las posiciones de la primera fila con las cinco cifras de votos. Fuera de la fila
    TOTAL, una cifra de una o dos cifras sin punto es un número de escaños y va con los votos
    que la preceden; el resto son votos y se asignan a la columna de votos más cercana. En la
    fila TOTAL (todas las celdas llenas) votos y escaños se alternan."""
    ih = next(i for i, ln in enumerate(lineas) if _es_cabecera(ln.split(), votos_etq))
    columnas = [*PROVINCIAS, "TOTAL"]
    num = re.compile(rf"(?<!\S)(?:{_NUM})(?!\S)")
    # filas de cifras agrupadas por página: (texto a la izquierda, [(cifra, centro)])
    paginas: list[list[tuple[str, list[tuple[str, float]]]]] = [[]]
    for ln in lineas[ih + 1 :]:
        if ln == _PAGINA:
            paginas.append([])
            continue
        if re.match(r"^(ISSN|\d+/16|CVE-)", ln.strip()) or "Diari Oficial" in ln:
            continue
        if not ln.strip():
            continue
        m0 = re.search(rf"\s{{2,}}(?:{_NUM})(?:\s|$)", ln)
        texto = ln if m0 is None else ln[: m0.start()]
        cifras = (
            []
            if m0 is None
            else [
                (m.group(0), m.start() + len(m.group(0)) / 2) for m in num.finditer(ln, m0.start())
            ]
        )
        paginas[-1].append((texto, cifras))
        if texto.strip() == "TOTAL":
            break
    filas: list[tuple[list[str], dict[str, list]]] = []
    for pag in paginas:
        es_total = [t.strip() == "TOTAL" for t, _ in pag]
        ref = None
        for (t, cifras), tot in zip(pag, es_total, strict=True):
            votos = (
                cifras[0::2] if tot else [c for c in cifras if not re.fullmatch(r"\d{1,2}", c[0])]
            )
            if len(votos) == len(columnas):
                ref = [c for _, c in votos]
                break
        if ref is None and any(c for _, c in pag):
            raise ValueError("página del Cuadro II sin fila completa de referencia")
        for (texto, cifras), tot in zip(pag, es_total, strict=True):
            if not cifras:
                if filas:
                    filas[-1][0].append(texto)
                continue
            celdas: dict[str, list] = {}
            col = None
            for k, (c, centro) in enumerate(cifras):
                escano = (k % 2 == 1) if tot else bool(re.fullmatch(r"\d{1,2}", c))
                if not escano:
                    j = min(range(len(columnas)), key=lambda i: abs(ref[i] - centro))
                    col = columnas[j]
                if col is None:
                    raise ValueError(f"escaños sin votos delante: {texto!r}")
                celda = celdas.setdefault(col, [None, None])
                if celda[escano] is not None:
                    raise ValueError(f"dos cifras en la misma celda: {texto!r} {cifras}")
                celda[escano] = _int(c)
            filas.append(([texto], celdas))
    return [(_une(t), {k: tuple(v) for k, v in c.items()}) for t, c in filas]


def leer(path: Path = PDF) -> Resultado:
    texto = _texto(path)
    corte = texto.index("ACÒRD de 4 de junh")
    cast = texto[:corte].replace("\f", f"\n{_PAGINA}\n").splitlines()
    aran = texto[corte:].replace("\f", f"\n{_PAGINA}\n").splitlines()

    res = _cuadro_i(cast)
    if _cuadro_i(aran) != res:
        raise ValueError("el Cuadro I en castellano y en aranés no coinciden")
    filas = _cuadro_ii(cast[: next(i for i, ln in enumerate(cast) if "Cuadro III" in ln)], "Votos")
    filas_ar = _cuadro_ii(aran, "Vòts")
    if [c for _, c in filas] != [c for _, c in filas_ar]:
        raise ValueError("el Cuadro II en castellano y en aranés no coinciden")
    *cands, (etq_total, fila_total) = filas
    if etq_total != "TOTAL":
        raise ValueError(f"última fila del Cuadro II inesperada: {etq_total!r}")

    def circ(nombre: str, codigo: str, col: str) -> Circunscripcion:
        r = res[nombre]
        votos = {k: c[col][0] for k, c in cands if col in c and c[col][0] is not None}
        escanos = {k: c[col][1] for k, c in cands if col in c and c[col][1] is not None}
        if fila_total[col][0] != r["a_candidaturas"]:
            raise ValueError(f"{nombre}: fila TOTAL del Cuadro II ≠ votos a candidaturas")
        if fila_total[col][1] != sum(escanos.values()):
            raise ValueError(f"{nombre}: escaños de la fila TOTAL ≠ suma de escaños")
        return Circunscripcion(
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

    circs = [circ(n, c, n) for n, c in PROVINCIAS.items()]
    total = circ("TOTAL", "09", "TOTAL")
    total.nombre = "Cataluña"
    notas = [
        "Electores: según el acuerdo de la JEC, total de residentes en España, residentes "
        "ausentes (CERA) y certificaciones censales de alta, con datos definitivos de la "
        "Oficina del Censo Electoral (no los del acta). El acuerdo no detalla el voto CERA.",
        "Escaños vacíos en el Cuadro II no se rellenan (se dejan fuera de `escanos`).",
        "Errata tipográfica del DOGC: votos a candidaturas de Girona impresos «297164» sin punto "
        "de millares en la versión en castellano (la aranesa da 297.164).",
    ]
    return Resultado(
        ccaa="09", eleccion="autonomicas-09-2024", circunscripciones=circs, total=total, notas=notas
    )
