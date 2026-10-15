"""País Vasco: elecciones al Parlamento Vasco de 21/04/2024 (BOPV nº 90, 09/05/2024).

Acuerdo de 2 de mayo de 2024 de la Junta Electoral de la Comunidad Autónoma del País Vasco
(anuncio 2024/2188). Por cada territorio histórico (Álava, Bizkaia, Gipuzkoa) da electores,
votantes, nulos, válidos, blancos, votos a candidaturas, votos por candidatura y la
distribución de escaños; para el conjunto de la comunidad da solo los votos por candidatura y
los escaños.

Particularidades de la publicación (se conservan tal como figuran):
- el mismo partido aparece con nombres distintos según el territorio («Partido Popular» en
  Álava, «Partido Popular (PP)» en Bizkaia, Gipuzkoa y el total);
- en el total de la comunidad figura «Escaños en Blanco para Dejar Ecaños Vacíos-…» (sic);
- los escaños se dan con siglas («EH-BILDU», «PSE-EE», «PP»…), que se asignan a la
  candidatura del territorio con la tabla explícita `_SIGLAS`.

El total de la comunidad no trae electores, votantes, nulos ni blancos, así que no se
construye `Resultado.total` (no se deduce ninguna cifra): sus votos por candidatura y escaños
se contrastan con la suma de los territorios y el resultado queda en `Resultado.notas`.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

RUTA = AUTONOMICAS / "ccaa16-2024" / "autonomicas_ccaa16_2024-04-21.pdf"
ELECCION = "autonomicas-16-2024"

_TERRITORIOS = {"ÁLAVA": "01", "GIPUZKOA": "20", "BIZKAIA": "48"}
_RESUMEN = {
    "Número total de electores": "electores",
    "Número de votantes": "votantes",
    "Número de votos nulos": "nulos",
    "Número de votos válidos": "validos",
    "Número de votos en blanco": "blancos",
    "Número de votos a candidaturas": "a_candidaturas",
}
# Siglas de la «Distribución de escaños» → nombres con que la candidatura figura en los votos
# (según el territorio). Se exige que en cada territorio coincida exactamente uno.
_SIGLAS = {
    "EH-BILDU": ("Euskal Herria Bildu (EH Bildu)",),
    "EH Bildu": ("Euskal Herria Bildu (EH Bildu)",),
    "EAJ-PNV": ("Euzko Alderdi Jeltzalea-Partido Nacionalista Vasco (EAJ-PNV)",),
    "PSE-EE": ("Partido Socialista de Euskadi-Euskadiko Ezkerra (PSOE)",),
    "PP": ("Partido Popular", "Partido Popular (PP)"),
    "Vox": ("Vox (VOX)",),
    "Sumar": ("Sumar",),
}
# Variantes de nombre de una misma candidatura dentro de la publicación (solo para contrastar
# el total de la comunidad con la suma de los territorios; los nombres no se cambian).
_MISMA_CANDIDATURA = {
    "Partido Popular": "Partido Popular (PP)",
    "Escaños en Blanco para Dejar Ecaños Vacíos-Aulki Zuriak Eserlekuak Hutsik Uzteko": (
        "Escaños en Blanco para Dejar Escaños Vacíos-Aulki Zuriak Eserlekuak Hutsik Uzteko"
    ),
}
_UNIDADES = (
    "cero un dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince "
    "dieciséis diecisiete dieciocho diecinueve veinte veintiún veintidós veintitrés veinticuatro "
    "veinticinco veintiséis veintisiete veintiocho veintinueve treinta"
).split()
_PALABRA_NUM = {p: i for i, p in enumerate(_UNIDADES)} | {"uno": 1, "veintiuno": 21}
_CABECERA = re.compile(
    r"^\s*(BOLETÍN OFICIAL DEL PAÍS VASCO.*|\w+ \d+ de \w+ de \d{4}|2024/2188 \(\d/\d\))\s*$"
)


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _texto(path: Path) -> str:
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout


def _entradas(texto: str) -> list[str]:
    """Párrafos del texto (sin cabeceras ni pies de página), cada uno en una sola línea."""
    lineas = [ln for ln in texto.replace("\f", "\n").splitlines() if not _CABECERA.match(ln)]
    out: list[str] = []
    actual: list[str] = []
    for ln in lineas + [""]:
        if ln.strip():
            actual.append(ln.strip())
        elif actual:
            out.append(re.sub(r"\s+", " ", " ".join(actual)))
            actual = []
    return out


def _secciones(texto: str) -> dict[str, list[str]]:
    """Párrafos agrupados por sección: «ÁLAVA», «BIZKAIA», «GIPUZKOA» o «COMUNIDAD»."""
    secciones: dict[str, list[str]] = {}
    clave = None
    for e in _entradas(texto):
        m = re.fullmatch(r"TERRITORIO HISTÓRICO DE (\S+)", e)
        if m:
            clave = m.group(1)
        elif e == "COMUNIDAD AUTÓNOMA VASCA":
            clave = "COMUNIDAD"
        elif clave is not None:
            secciones.setdefault(clave, []).append(e)
    return secciones


def _parse(entradas: list[str]) -> tuple[dict[str, int], dict[str, int], dict[str, int]]:
    """(resumen, votos por candidatura, escaños por sigla) de una sección."""
    resumen: dict[str, int] = {}
    votos: dict[str, int] = {}
    escanos: dict[str, int] = {}
    en_escanos = False
    for e in entradas:
        if e == "Distribución de escaños":
            en_escanos = True
            continue
        if e.startswith("Vitoria-Gasteiz"):
            break
        m = re.match(r"^[–•] (.+?): (\d{1,3}(?:\.\d{3})*|\d+) ?\(", e)
        if m and not en_escanos:
            nombre, valor = m.group(1).strip(), _int(m.group(2))
            if nombre in _RESUMEN:
                resumen[_RESUMEN[nombre]] = valor
            else:
                if nombre in votos:
                    raise ValueError(f"candidatura repetida: {nombre}")
                votos[nombre] = valor
            continue
        m = re.fullmatch(r"(.+?): (\S+) escaños?\.", e)
        if m and en_escanos:
            escanos[m.group(1)] = _PALABRA_NUM[m.group(2)]
    return resumen, votos, escanos


def _asignar_escanos(siglas: dict[str, int], votos: dict[str, int], nombre: str) -> dict[str, int]:
    out = {}
    for sigla, n in siglas.items():
        candidatas = [c for c in _SIGLAS[sigla] if c in votos]
        if len(candidatas) != 1:
            raise ValueError(f"{nombre}: la sigla {sigla!r} no identifica una candidatura")
        out[candidatas[0]] = n
    return out


def leer(path: Path = RUTA) -> Resultado:
    secciones = _secciones(_texto(path))
    if set(secciones) != set(_TERRITORIOS) | {"COMUNIDAD"}:
        raise ValueError(f"secciones inesperadas: {sorted(secciones)}")
    circs = []
    for nombre, codigo in sorted(_TERRITORIOS.items(), key=lambda kv: kv[1]):
        resumen, votos, siglas = _parse(secciones[nombre])
        faltan = set(_RESUMEN.values()) - set(resumen)
        if faltan:
            raise ValueError(f"{nombre}: faltan {sorted(faltan)}")
        circs.append(
            Circunscripcion(
                codigo=codigo,
                nombre=nombre.capitalize(),
                electores=resumen["electores"],
                votantes=resumen["votantes"],
                nulos=resumen["nulos"],
                blancos=resumen["blancos"],
                votos=votos,
                escanos=_asignar_escanos(siglas, votos, nombre),
                validos=resumen["validos"],
                a_candidaturas=resumen["a_candidaturas"],
            )
        )
    notas = [
        "Fuente: BOPV nº 90 (09/05/2024), Acuerdo de 2/5/2024 de la Junta Electoral de la "
        "Comunidad Autónoma del País Vasco (escrutinio general).",
        "La publicación no indica si las cifras incluyen el voto CERA.",
        "Nombres de candidatura tal como figuran en cada territorio: «Partido Popular» (Álava) "
        "y «Partido Popular (PP)» (Bizkaia, Gipuzkoa) son la misma candidatura.",
        "Escaños publicados con siglas; asignados a la candidatura con la tabla _SIGLAS.",
    ]
    notas += _contrastar_total(circs, *total_comunidad(path))
    return Resultado(ccaa="16", eleccion=ELECCION, circunscripciones=circs, notas=notas)


def total_comunidad(path: Path = RUTA) -> tuple[dict[str, int], dict[str, int]]:
    """Votos por candidatura y escaños (por sigla) del total de la comunidad publicado."""
    _, votos, escanos = _parse(_secciones(_texto(path))["COMUNIDAD"])
    return votos, escanos


def _contrastar_total(
    circs: list[Circunscripcion], votos_total: dict[str, int], escanos_total: dict[str, int]
) -> list[str]:
    suma: dict[str, int] = {}
    escanos: dict[str, int] = {}
    for c in circs:
        for k, v in c.votos.items():
            k = _MISMA_CANDIDATURA.get(k, k)
            suma[k] = suma.get(k, 0) + v
        for k, v in c.escanos.items():
            k = _MISMA_CANDIDATURA.get(k, k)
            escanos[k] = escanos.get(k, 0) + v
    difs = []
    for k in set(suma) | {_MISMA_CANDIDATURA.get(k, k) for k in votos_total}:
        publicado = sum(v for n, v in votos_total.items() if _MISMA_CANDIDATURA.get(n, n) == k)
        if publicado != suma.get(k, 0):
            difs.append(f"{k}: publicado {publicado} ≠ suma {suma.get(k, 0)}")
    # En el total, cada sigla se lleva al último nombre de `_SIGLAS` (el de Bizkaia y Gipuzkoa).
    escanos_pub = {_SIGLAS[s][-1]: n for s, n in escanos_total.items()}
    if escanos_pub != escanos:
        difs.append(f"escaños: publicado {escanos_pub} ≠ suma {escanos}")
    if difs:
        return ["DISCREPANCIA en el total de la comunidad publicado: " + "; ".join(sorted(difs))]
    return [
        "Total de la comunidad: la publicación solo da votos por candidatura y escaños (no "
        "electores, votantes, nulos ni blancos); la suma de los territorios los reproduce."
    ]
