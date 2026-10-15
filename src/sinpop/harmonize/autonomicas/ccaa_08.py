"""Castilla-La Mancha: elecciones a las Cortes de Castilla-La Mancha del 28 de mayo de 2023.

Fuente: DOCM núm. 114, de 16 de junio de 2023 (acuerdo de 14/06/2023 de la Junta Electoral de
Castilla-La Mancha, [2023/5411]), con los datos de las actas de proclamación de las juntas
provinciales:

- resumen por provincia y total: electores, votantes, votos a candidaturas, en blanco,
  válidos y nulos;
- votos por candidatura y provincia (las candidaturas figuran por su sigla; las celdas vacías
  son provincias donde la candidatura no aparece y no se rellenan);
- relación de diputados electos por provincia con su sigla (de ahí se cuentan los escaños);
- votantes CERA por consulado y provincia de destino.

El DOCM no dice si el resumen incluye el voto CERA: la tabla CERA se publica aparte por la
Instrucción 1/2023 de la JEC. Sus votantes por provincia se resumen en `notas` y no se suman.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa08-2023" / "autonomicas_ccaa08_2023-05-28.pdf"
PROVINCIAS = {
    "Albacete": "02",
    "Ciudad Real": "13",
    "Cuenca": "16",
    "Guadalajara": "19",
    "Toledo": "45",
}
TOTAL = "Castilla-La Mancha"
_NUM = r"\d{1,3}(?:\.\d{3})*"
# columnas del resumen, en el orden del DOCM
_RESUMEN = ["electores", "votantes", "a_candidaturas", "blancos", "validos", "nulos"]


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _resumen(lineas: list[str]) -> dict[str, dict[str, int]]:
    out: dict[str, dict[str, int]] = {}
    nombres = "|".join(re.escape(n) for n in [*PROVINCIAS, TOTAL])
    patron = re.compile(rf"^\s*({nombres})" + rf"\s+({_NUM})" * 6 + r"\s*$")
    for ln in lineas:
        m = patron.match(ln)
        if m:
            out[m.group(1)] = {k: _int(v) for k, v in zip(_RESUMEN, m.groups()[1:], strict=True)}
    return out


def _tabla_votos(lineas: list[str]) -> tuple[dict[str, dict[str, int]], dict[str, int]]:
    """Votos por candidatura (sigla) y columna; las cifras se asignan a la columna de
    cabecera cuyo centro está más cerca (hay celdas vacías)."""
    i0 = next(i for i, ln in enumerate(lineas) if ln.startswith(" Relación de votos"))
    ih = next(i for i in range(i0, len(lineas)) if "Albacete" in lineas[i])
    cab = lineas[ih]
    columnas = [*PROVINCIAS, TOTAL]
    centros = {c: cab.index(c) + len(c) / 2 for c in columnas}
    votos: dict[str, dict[str, int]] = {}
    total_fila: dict[str, int] = {}
    for ln in lineas[ih + 1 :]:
        if not ln.strip():
            continue
        m0 = re.search(rf"\s{{2,}}{_NUM}(?:\s|$)", ln)
        if m0 is None:
            break  # fin de la tabla (leyenda de siglas)
        sigla = re.sub(r"\s+", " ", ln[: m0.start()]).strip()
        fila: dict[str, int] = {}
        for m in re.finditer(rf"(?<!\S){_NUM}(?!\S)", ln[m0.start() :]):
            ini = m0.start() + m.start()
            centro = ini + len(m.group(0)) / 2
            col = min(columnas, key=lambda c: abs(centros[c] - centro))
            if col in fila:
                raise ValueError(f"{sigla}: dos cifras en la columna {col}")
            fila[col] = _int(m.group(0))
        if sigla == "TOTAL":
            total_fila = fila
            break
        if sigla in votos:
            raise ValueError(f"candidatura repetida: {sigla}")
        votos[sigla] = fila
    return votos, total_fila


def _escanos(lineas: list[str]) -> dict[str, dict[str, int]]:
    i0 = next(i for i, ln in enumerate(lineas) if ln.startswith("Relación de diputados"))
    i1 = next(i for i, ln in enumerate(lineas) if ln.strip().startswith("Resumen de los"))
    out: dict[str, dict[str, int]] = {}
    prov = None
    for ln in lineas[i0 + 1 : i1]:
        s = ln.strip()
        if s in PROVINCIAS:
            prov = s
            out[prov] = {}
            continue
        m = re.match(r"^D\.(?:ª)? .+\(([^)]+)\)$", s)
        if m and prov is not None:
            out[prov][m.group(1)] = out[prov].get(m.group(1), 0) + 1
    return out


def _cera(lineas: list[str]) -> dict[str, int]:
    """Votantes CERA por provincia de destino ('-' = sin dato, se ignora)."""
    i0 = next(i for i, ln in enumerate(lineas) if "Votos CERA por consulado" in ln)
    cab = next(ln for ln in lineas[i0:] if re.search(r"\bAB\s+CR\s+CU\s+GU\s+TO\b", ln))
    siglas = cab.split()[-5:]
    suma = dict.fromkeys(siglas, 0)
    for ln in lineas[i0:]:
        m = re.search(r"\S\s+((?:(?:-|\d+)\s+){4}(?:-|\d+))\s*$", ln)
        if m is None or ln.startswith("AÑO"):
            continue
        for s, v in zip(siglas, m.group(1).split(), strict=True):
            if v != "-":
                suma[s] += int(v)
    return suma


def leer(path: Path = PDF) -> Resultado:
    lineas = _texto(path).replace("\f", "\n").splitlines()
    resumen = _resumen(lineas)
    votos, total_fila = _tabla_votos(lineas)
    escanos = _escanos(lineas)
    if set(resumen) != {*PROVINCIAS, TOTAL}:
        raise ValueError(f"resumen incompleto: {sorted(resumen)}")

    def circ(nombre: str, codigo: str) -> Circunscripcion:
        r = resumen[nombre]
        c = Circunscripcion(
            codigo=codigo,
            nombre=nombre,
            electores=r["electores"],
            votantes=r["votantes"],
            nulos=r["nulos"],
            blancos=r["blancos"],
            votos={s: f[nombre] for s, f in votos.items() if nombre in f},
            escanos=escanos.get(nombre, {}),
            validos=r["validos"],
            a_candidaturas=r["a_candidaturas"],
        )
        if total_fila.get(nombre) != r["a_candidaturas"]:
            raise ValueError(f"{nombre}: fila TOTAL de votos ≠ votos a candidaturas")
        if set(c.escanos) - set(c.votos):
            raise ValueError(f"{nombre}: electos de una sigla sin votos: {c.escanos}")
        return c

    circs = [circ(n, c) for n, c in PROVINCIAS.items()]
    total = circ(TOTAL, "08")
    cera = _cera(lineas)
    notas = [
        "Candidaturas por su sigla, tal como figuran en la tabla de votos; la leyenda del DOCM "
        "da el nombre completo (con variantes de grafía: «PAIS CON GESTORES» en la tabla y "
        "«PAÍS CON GESTORES» en la leyenda; «TÚ patria» / «TÚpatria»; «FE de las J.O.N.S.» / "
        "«FALANGE ESTAÑOLA DE LAS JONS», sic).",
        "Escaños por provincia contados en la relación de diputados electos (sigla entre "
        "paréntesis); solo se anotan las siglas con escaño. El DOCM no da escaños totales de la "
        "comunidad y el total se deja sin escaños.",
        "El DOCM no dice si el resumen incluye el voto CERA. Publica aparte los votantes CERA "
        "por consulado y provincia (no sumados): "
        + ", ".join(f"{k} {v}" for k, v in cera.items())
        + " (suma de la tabla; «-» se ignora).",
    ]
    return Resultado(
        ccaa="08", eleccion="autonomicas-08-2023", circunscripciones=circs, total=total, notas=notas
    )
