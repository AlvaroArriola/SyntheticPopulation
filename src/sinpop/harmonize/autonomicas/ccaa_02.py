"""Aragón: elecciones a las Cortes de Aragón de 08/02/2026.

Fuente: «Informe Resultados Definitivos» del Gobierno de Aragón (119 páginas; resultados de
la comunidad, las provincias, las comarcas y los municipios). La fecha de la elección no
figura en el PDF (D-023). Solo se leen la comunidad y las tres provincias:
- página de resultados: candidatura, diputados/as, votos y % de 2026 (columna izquierda; la
  derecha es 2023 y se ignora);
- página (o bloque) de participación: participación (votantes), votos nulos, válidos, a
  candidaturas y en blanco de 2026.

Electores: el informe no da la cifra de electores. Trae el «CENSO» de la constitución de mesas
y la abstención, pero ninguno de los dos se presenta como electores, así que
`electores` queda a None (no se deduce).

Voto CERA: el informe no lo dice en el texto, pero los resultados municipales incluyen una
columna «Residentes ausentes-<provincia>». Se comprueba que la participación de todos los
municipios, contando esa columna (y sin los distritos de Zaragoza, que desglosan la capital),
reproduce la participación provincial; el resultado queda en las notas.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

RUTA = AUTONOMICAS / "ccaa02-2026" / "autonomicas_ccaa02_2026-02-08.pdf"
ELECCION = "autonomicas-02-2026"

_PROVINCIAS = {"Huesca": "22", "Teruel": "44", "Zaragoza": "50"}
_NUM = r"(\d{1,3}(?:\.\d{3})*)"
_RESUMEN = {
    "Votos nulos": "nulos",
    "Votos válidos": "validos",
    "Votos a candidaturas": "a_candidaturas",
    "Votos en blanco": "blancos",
}
_FILA = re.compile(r"^\s*(\S.*?)\s{2,}(\d+)\s+" + _NUM + r"\s+\d{1,3},\d{2}%\s*$")


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _paginas(path: Path) -> list[str]:
    txt = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout
    return txt.split("\f")


def _ambito(pagina: str) -> str | None:
    """«Aragón» o el nombre de la provincia, si la página es de resultados de ese ámbito."""
    if not re.search(r"^Resultados\b", pagina, re.M) or "Escrutado" not in pagina:
        return None
    m = re.search(r"^Aragón(?: \(Comunidad\)| > (\w+) \(Provincia\))\s*$", pagina, re.M)
    if m is None:
        return None
    return m.group(1) or "Aragón"


def _candidaturas(pagina: str) -> tuple[dict[str, int], dict[str, int]] | None:
    """(votos, diputados) de 2026, o None si la página no trae la tabla de candidaturas."""
    lineas = pagina.splitlines()
    i = next((i for i, ln in enumerate(lineas) if ln.count("Candidaturas") == 2), None)
    if i is None:
        return None
    hdr = lineas[i]
    if "Diputados/as" not in hdr:
        raise ValueError("tabla de candidaturas sin columna de diputados/as")
    corte = hdr.find("Candidaturas", hdr.find("Candidaturas") + 1)
    votos: dict[str, int] = {}
    escanos: dict[str, int] = {}
    for ln in lineas[i + 1 :]:
        if ln.strip() == "Participación":
            break
        izq = ln[:corte]
        if not izq.strip():
            continue  # fila solo de 2023, o en blanco
        m = _FILA.match(izq)
        if m is None:
            raise ValueError(f"fila de candidatura no reconocida: {ln.strip()}")
        nombre = re.sub(r"\s+", " ", m.group(1))
        if nombre in votos:
            raise ValueError(f"candidatura repetida: {nombre}")
        votos[nombre] = _int(m.group(3))
        escanos[nombre] = int(m.group(2))
    return votos, escanos


def _participacion(pagina: str) -> dict[str, int] | None:
    """Votantes, nulos, válidos, a candidaturas y blancos de 2026, si la página los trae."""
    if not re.search(r"^PARTICIPACIÓN\s", pagina, re.M):
        return None
    out = {}
    m = re.search(r"^2026\s+\d{1,3},\d{2}%\s+[-+]?\d+,\d{2}\s+" + _NUM + r"\s", pagina, re.M)
    if m is None:
        raise ValueError("participación de 2026 no reconocida")
    out["votantes"] = _int(m.group(1))
    for etiqueta, clave in _RESUMEN.items():
        m = re.search(rf"^\s*{etiqueta}\s+\d{{1,3}},\d{{2}}%\s+{_NUM}\s", pagina, re.M)
        if m is None:
            raise ValueError(f"{etiqueta} no reconocido")
        out[clave] = _int(m.group(1))
    return out


def _participacion_municipal(paginas: list[str]) -> tuple[dict[str, int], set[str]]:
    """Suma de la participación de los municipios por provincia y provincias con la columna
    «Residentes ausentes-…». Las columnas «Distritos de …» (desglose de la capital) se
    excluyen: en cada bloque son las últimas, tantas como rótulos «Distritos de» lleve."""
    suma: dict[str, int] = {}
    con_cera: set[str] = set()
    for p in paginas:
        m = re.search(r"^Aragón > Municipios de (\w+) \(Provincia\)\s*$", p, re.M)
        if m is None:
            continue
        prov = m.group(1)
        distritos = 0
        for ln in p.splitlines():
            if "Residentes ausentes-" in ln:
                con_cera.add(prov)
            if re.match(r"^\s*Participación\s+\d", ln):
                valores = [_int(v) for v in re.findall(_NUM + r"\s+\d{1,3}(?:,\d{2})?%", ln)]
                suma[prov] = suma.get(prov, 0) + sum(valores[: len(valores) - distritos])
                distritos = 0
            else:
                distritos += ln.count("Distritos de")
    return suma, con_cera


def leer(path: Path = RUTA) -> Resultado:
    paginas = _paginas(path)
    datos: dict[str, dict] = {}
    for p in paginas:
        ambito = _ambito(p)
        if ambito is None:
            continue
        d = datos.setdefault(ambito, {})
        cand = _candidaturas(p)
        if cand is not None:
            if "votos" in d:
                raise ValueError(f"{ambito}: dos tablas de candidaturas")
            d["votos"], d["escanos"] = cand
        part = _participacion(p)
        if part is not None:
            if "votantes" in d:
                raise ValueError(f"{ambito}: dos bloques de participación")
            d.update(part)
    if set(datos) != {"Aragón", *_PROVINCIAS} or any(len(d) != 7 for d in datos.values()):
        raise ValueError(f"ámbitos incompletos: { {k: sorted(v) for k, v in datos.items()} }")

    def circ(ambito: str, codigo: str) -> Circunscripcion:
        d = datos[ambito]
        return Circunscripcion(
            codigo=codigo,
            nombre=ambito,
            electores=None,  # no publicado (véase el docstring del módulo)
            votantes=d["votantes"],
            nulos=d["nulos"],
            blancos=d["blancos"],
            votos=d["votos"],
            escanos=d["escanos"],
            validos=d["validos"],
            a_candidaturas=d["a_candidaturas"],
        )

    circs = [circ(nombre, codigo) for nombre, codigo in _PROVINCIAS.items()]
    total = circ("Aragón", "02")
    notas = [
        "Fuente: Informe de resultados definitivos del Gobierno de Aragón (elecciones a las "
        "Cortes de Aragón de 08/02/2026); se usan las páginas de la comunidad y las provincias.",
        "ELECTORES NO PUBLICADOS: el informe no da electores (solo el censo de constitución de "
        "mesas y la abstención); `electores` queda a None.",
        "Total de la comunidad publicado (Aragón (Comunidad)).",
    ]
    suma, con_cera = _participacion_municipal(paginas)
    iguales = all(suma.get(p) == datos[p]["votantes"] for p in _PROVINCIAS)
    if con_cera == set(_PROVINCIAS) and iguales:
        notas.append(
            "Voto CERA incluido: los resultados municipales traen la columna «Residentes "
            "ausentes-<provincia>» y la participación de los municipios, con ella, reproduce la "
            "provincial (el texto del informe no lo dice expresamente)."
        )
    else:
        notas.append(
            "Voto CERA: no se ha podido comprobar con los resultados municipales "
            f"(provincias con «Residentes ausentes»: {sorted(con_cera)}; suma de municipios "
            f"{suma} frente a votantes provinciales "
            f"{ {p: datos[p]['votantes'] for p in _PROVINCIAS} })."
        )
    return Resultado(
        ccaa="02", eleccion=ELECCION, circunscripciones=circs, total=total, notas=notas
    )
