"""Comunitat Valenciana: elecciones a Les Corts Valencianes del 28 de mayo de 2023.

Fuente: DOGV núm. 9618, de 15 de junio de 2023 ([2023/6826]): publicación de la Junta Electoral
de la Comunitat Valenciana de los resultados finales y la relación de diputados electos.

La tabla de la página 2 da, por provincia y para el total de la comunidad: electores,
votantes, votos en blanco, votos nulos y votos por candidatura (nombre completo con la sigla
entre paréntesis; las celdas están todas llenas y una candidatura que no concurre en una
provincia aparece con 0, que se conserva tal cual). No se publican votos válidos ni votos a
candidaturas. La relación de electos (página 3) es una lista de nombres por partido en
columnas sin recuento; no se extraen escaños.

El total de electores de la comunidad publicado (2.426.278) no es la suma de las provincias;
es una errata del DOGV y se deja `total.electores = None` (véase `Resultado.notas`).

El documento no dice si los resultados incluyen el voto CERA.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa10-2023" / "autonomicas_ccaa10_2023-05-28.pdf"
# columnas de la tabla, en orden: Alicante, Castellón, Valencia y total de la comunidad
PROVINCIAS = {"Alicante": "03", "Castellón": "12", "Valencia": "46"}
_NUM = r"\d{1,3}(?:\.\d{3})*"
_CIFRAS = re.compile(rf"\s{{2,}}({_NUM})\s+({_NUM})\s+({_NUM})\s+({_NUM})\s*$")
_RESUMEN = {
    "Electors / Electores": "electores",
    "Votants / Votantes": "votantes",
    "Vots en blanc / Votos en blanco": "blancos",
    "Vots nuls / Votos nulos": "nulos",
}


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _fmt(n: int | None) -> str:
    return "None" if n is None else f"{n:,}".replace(",", ".")


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _filas(pagina: str) -> list[tuple[str, list[int]]]:
    """Bloques de la tabla separados por líneas en blanco: (etiqueta, [4 cifras]).

    La etiqueta de una candidatura puede ocupar una línea antes y otra después de la línea con
    las cifras; se unen en orden con un espacio."""
    lineas = pagina.splitlines()
    i0 = next(i for i, ln in enumerate(lineas) if ln.strip().startswith("Electors / Electores"))
    out = []
    bloque: list[str] = []
    for ln in [*lineas[i0:], ""]:
        if ln.strip():
            bloque.append(ln)
            continue
        if not bloque:
            continue
        partes, cifras = [], None
        for b in bloque:
            m = _CIFRAS.search(b)
            if m:
                if cifras is not None:
                    raise ValueError(f"bloque con dos filas de cifras: {bloque}")
                cifras = [_int(x) for x in m.groups()]
                b = b[: m.start()]
            partes.append(b)
        if cifras is None:
            raise ValueError(f"bloque sin cifras: {bloque}")
        out.append((re.sub(r"\s+", " ", " ".join(partes)).strip(), cifras))
        bloque = []
    return out


def leer(path: Path = PDF) -> Resultado:
    pagina = next(p for p in _texto(path).split("\f") if "Electors / Electores" in p)
    filas = _filas(pagina)
    resumen = {_RESUMEN[k]: v for k, v in filas if k in _RESUMEN}
    if set(resumen) != set(_RESUMEN.values()):
        raise ValueError(f"faltan filas de resumen: {sorted(resumen)}")
    cands = [(k, v) for k, v in filas if k not in _RESUMEN]
    if len({k for k, _ in cands}) != len(cands):
        raise ValueError("candidatura repetida")

    def circ(j: int, nombre: str, codigo: str) -> Circunscripcion:
        return Circunscripcion(
            codigo=codigo,
            nombre=nombre,
            electores=resumen["electores"][j],
            votantes=resumen["votantes"][j],
            nulos=resumen["nulos"][j],
            blancos=resumen["blancos"][j],
            votos={k: v[j] for k, v in cands},
        )

    circs = [circ(j, n, c) for j, (n, c) in enumerate(PROVINCIAS.items())]
    total = circ(3, "Comunitat Valenciana", "10")
    electores_publicado = total.electores
    suma = sum(c.electores or 0 for c in circs)
    notas = [
        "El DOGV no indica si los resultados incluyen el voto CERA.",
        "Las celdas con 0 votos se conservan como 0 (el DOGV no distingue entre no concurrir "
        "en la provincia y obtener 0 votos).",
        "No se extraen escaños: la relación de electos es una lista de nombres sin recuento.",
    ]
    if electores_publicado != suma:
        # errata del propio DOGV: no se corrige, se deja sin dato y se documenta
        total.electores = None
        sin_alicante = sum(c.electores or 0 for c in circs if c.codigo != "03")
        notas.append(
            f"Errata en el DOGV: el total de electores de la comunidad publicado "
            f"({_fmt(electores_publicado)}) no es la suma de las provincias ({_fmt(suma)})"
            + (
                " y coincide con Castellón + Valencia, sin Alicante"
                if electores_publicado == sin_alicante
                else ""
            )
            + ". Se deja `total.electores = None`; los electores por provincia se conservan."
        )
    return Resultado(
        ccaa="10", eleccion="autonomicas-10-2023", circunscripciones=circs, total=total, notas=notas
    )
