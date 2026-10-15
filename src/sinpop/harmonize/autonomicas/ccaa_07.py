"""Castilla y León: elecciones a las Cortes de 15/03/2026 (BOCyL nº 80, 29/04/2026).

Resolución de 27 de abril de 2026 de la Junta Electoral de Castilla y León:
- Anexo I (resumen general): por junta electoral provincial y total, electores, votos a
  candidaturas, en blanco, válidos (TOTAL) y nulos. No trae la cifra de votantes.
- Anexo II: escaños y votos de las candidaturas que han obtenido escaño.
- Anexo III (tres páginas): votos de las candidaturas que no han obtenido escaño.
- Anexo V: escrutinio del voto CERA (aparte; no se usa aquí). Anexos IV y VI: electos y voto
  CERA por consulado (no se usan).

Las tablas de los anexos II y III tienen la cabecera de cada candidatura partida en varias
líneas. Los nombres se escriben en `_NOMBRES` tal como figuran, uniendo las líneas (el salto
de línea tras un guion o un paréntesis no se convierte en espacio), y se comprueba que los
caracteres de la cabecera de cada página son exactamente los de esos nombres. Cada cifra se
asigna a la columna cuyo TOTAL termina en la misma posición del texto (± `_TOLERANCIA`).

Votantes: la publicación no la da y no se deduce (regla 3 de CLAUDE.md): queda a `None`. Se
comprueban válidos = candidaturas + blancos, votos a candidaturas = suma de candidaturas y el
total de la comunidad.
"""

from __future__ import annotations

import re
import subprocess
from collections import Counter
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

RUTA = AUTONOMICAS / "ccaa07-2026" / "autonomicas_ccaa07_2026-03-15.pdf"
ELECCION = "autonomicas-07-2026"

_PROVINCIAS = {
    "ÁVILA": "05",
    "BURGOS": "09",
    "LEÓN": "24",
    "PALENCIA": "34",
    "SALAMANCA": "37",
    "SEGOVIA": "40",
    "SORIA": "42",
    "VALLADOLID": "47",
    "ZAMORA": "49",
}
# Candidaturas por página (anexo II y anexo III 1/3, 2/3 y 3/3), en el orden de las columnas.
_NOMBRES = {
    "II": [
        "PARTIDO POPULAR (PP)",
        "PARTIDO SOCIALISTA OBRERO ESPAÑOL (PSOE)",
        "VOX (VOX)",
        "UNIÓN DEL PUEBLO LEONÉS (UPL)",
        "POR ÁVILA (XÁV)",
        "SORIA ¡YA! (SY)",
    ],
    "III (1 / 3)": [
        "IZQUIERDA UNIDA-MOVIMIENTO SUMAR-VERDES EQUO (IU-MS-VQ)",
        "SE ACABÓ LA FIESTA (SALF)",
        "PODEMOS-ALIANZA VERDE CYL 2026 (PODEMOS – AV)",
        "PARTIDO ANIMALISTA CON EL MEDIO AMBIENTE (PACMA)",
        "ESCAÑOS EN BLANCO PARA DEJAR ESCAÑOS VACÍOS (ESCAÑOS EN BLANCO)",
        "CIUDADANOS-PARTIDO DE LA CIUDADANÍA (Cs)",
        "NUEVE CASTILLA Y LEÓN (NUEVECYL)",
        "VÍA BURGALESA MUNICIPALISTA (VBM)",
    ],
    "III (2 / 3)": [
        "PARTIDO CASTELLANO-TIERRA COMUNERA (PCAS-TC)",
        "COALICIÓN POR EL BIERZO (C. Bierzo)",
        "PARTIDO COMUNISTA DE LOS TRABAJADORES DE ESPAÑA (PCTE)",
        "VAMOS PALENCIA (VP)",
        "POR UN MUNDO MÁS JUSTO (MUNDO+JUSTO)",
        "ESPAÑA VACIADA (ESPAÑA VACIADA)",
        "AHORA DECIDE-ESPAÑA VACIADA (AD-EV)",
    ],
    "III (3 / 3)": [
        "MUNICIPALISTAS-ESPAÑA VACIADA (MEV)",
        "PARTIDO NACIONALISTA DE CASTILLA Y LEÓN- UNIÓN REFORMISTA CIUDADANA (PANCAL-URCI)",
        "FALANGE ESPAÑOLA DE LAS J.O.N.S. (FE de las JONS)",
        "DECIDE NUEVE CYL (DECIDE-NUEVECYL)",
        "PROYECTO ALANTRE (P. ALANTRE)",
        "PARTIDO REGIONALISTA DEL PAÍS LEONÉS (PREPAL)",
        "SOBERANÍA ALIMENTARIA ESPAÑOLA (SAE)",
    ],
}
# Rótulos de la cabecera que no forman parte de los nombres de candidatura.
_ROTULOS = ("JUNTAS", "ELECTORALES", "PROVINCIALES", "Escaños", "Votos")
# Desfase máximo (en caracteres) entre el final de una cifra y el de su TOTAL; las columnas
# están separadas por 6 caracteres o más, y las sumas por columna se contrastan con el TOTAL.
_TOLERANCIA = 2
_NUM = re.compile(r"(?<![\d.])\d{1,3}(?:\.\d{3})*(?![\d.])")
_FILA = re.compile(r"^\s*(" + "|".join([*_PROVINCIAS, "TOTAL"]) + r")\b(.*)$")


def _int(s: str) -> int:
    return int(s.replace(".", ""))


def _paginas(path: Path) -> list[str]:
    txt = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout
    return txt.split("\f")


def _resumen(pagina: str) -> dict[str, tuple[int, ...]]:
    """Anexo I: fila → (electores, a candidaturas, en blanco, válidos, nulos)."""
    out = {}
    for ln in pagina.splitlines():
        m = re.match(r"^\s*([A-ZÁÉÍÓÚ][a-záéíóúñ]+|TOTAL)\s+(.*)$", ln)
        if not m:
            continue
        nombre = m.group(1).upper()
        nums = _NUM.findall(m.group(2))
        if nombre in _PROVINCIAS or nombre == "TOTAL":
            if len(nums) != 5 or re.sub(r"[\d.\s]", "", m.group(2)):
                raise ValueError(f"anexo I: fila no reconocida: {ln.strip()}")
            out[nombre] = tuple(_int(n) for n in nums)
    return out


def _comprobar_cabecera(lineas: list[str], nombres: list[str], clave: str) -> None:
    """Los caracteres de la cabecera (sin rótulos) son exactamente los de los nombres."""
    i0 = next(i for i, ln in enumerate(lineas) if "FORMACIONES POLÍTICAS" in ln)
    i1 = next(i for i, ln in enumerate(lineas) if _FILA.match(ln))
    texto = " ".join(lineas[i0 + 1 : i1])
    for r in _ROTULOS:
        texto = re.sub(rf"\b{r}\b", " ", texto)
    if Counter(texto.replace(" ", "")) != Counter("".join(nombres).replace(" ", "")):
        raise ValueError(f"anexo {clave}: la cabecera no coincide con los nombres esperados")


def _tabla(pagina: str, clave: str) -> dict[str, list[dict[str, int]]]:
    """Fila (provincia o TOTAL) → por columna, {"votos": n} o {"votos": n, "escanos": e}."""
    nombres = _NOMBRES[clave]
    lineas = pagina.splitlines()
    _comprobar_cabecera(lineas, nombres, clave)
    filas = {}
    for ln in lineas:
        m = _FILA.match(ln)
        if m:
            filas[m.group(1)] = [(mm.end(), _int(mm.group())) for mm in _NUM.finditer(ln)]
    if set(filas) != set(_PROVINCIAS) | {"TOTAL"}:
        raise ValueError(f"anexo {clave}: filas {sorted(filas)}")
    con_escanos = clave == "II"
    anclas = [fin for fin, _ in filas["TOTAL"]]
    if len(anclas) != len(nombres) * (2 if con_escanos else 1):
        raise ValueError(f"anexo {clave}: {len(anclas)} columnas en TOTAL")
    out = {}
    for fila, celdas in filas.items():
        valores: dict[int, int] = {}
        for fin, v in celdas:
            j = min(range(len(anclas)), key=lambda k: abs(anclas[k] - fin))
            if abs(anclas[j] - fin) > _TOLERANCIA or j in valores:
                raise ValueError(f"anexo {clave}, {fila}: cifra {v} fuera de columna")
            valores[j] = v
        cols: list[dict[str, int]] = []
        for j in range(len(nombres)):
            if con_escanos:
                d = {}
                if 2 * j + 1 in valores:
                    d["votos"] = valores[2 * j + 1]
                if 2 * j in valores:
                    d["escanos"] = valores[2 * j]
            else:
                d = {"votos": valores[j]} if j in valores else {}
            cols.append(d)
        out[fila] = cols
    return out


def leer(path: Path = RUTA) -> Resultado:
    paginas = _paginas(path)
    resumen: dict[str, tuple[int, ...]] | None = None
    tablas: dict[str, dict[str, list[dict[str, int]]]] = {}
    for p in paginas:
        if re.search(r"^\s*ANEXO I\s*$", p, re.M) and "Resumen general" in p:
            resumen = _resumen(p)
        elif re.search(r"^\s*ANEXO II\s*$", p, re.M):
            tablas["II"] = _tabla(p, "II")
        elif re.search(r"^\s*ANEXO III\s*$", p, re.M):
            m = re.search(r"\((\d) / 3\)", p)
            if m is None:
                raise ValueError("anexo III sin número de página")
            clave = f"III ({m.group(1)} / 3)"
            tablas[clave] = _tabla(p, clave)
    if resumen is None or set(tablas) != set(_NOMBRES):
        raise ValueError(f"faltan anexos: resumen={resumen is not None}, tablas={sorted(tablas)}")

    def circ(fila: str, codigo: str, nombre: str) -> Circunscripcion:
        electores, a_cand, blancos, validos, nulos = resumen[fila]
        votos: dict[str, int] = {}
        escanos: dict[str, int] = {}
        for clave, nombres in _NOMBRES.items():
            for nom, celda in zip(nombres, tablas[clave][fila], strict=True):
                if "votos" in celda:
                    votos[nom] = celda["votos"]
                if "escanos" in celda:
                    escanos[nom] = celda["escanos"]
        return Circunscripcion(
            codigo=codigo,
            nombre=nombre,
            electores=electores,
            votantes=None,  # no publicada
            nulos=nulos,
            blancos=blancos,
            votos=votos,
            escanos=escanos,
            validos=validos,
            a_candidaturas=a_cand,
        )

    circs = [circ(f, c, f.capitalize()) for f, c in _PROVINCIAS.items()]
    total = circ("TOTAL", "07", "Castilla y León")
    notas = [
        "Fuente: BOCyL nº 80 (29/04/2026), Resolución de 27/4/2026 de la Junta Electoral de "
        "Castilla y León, anexos I, II y III.",
        "VOTANTES NO PUBLICADOS: el anexo I no trae votantes; se dejan vacíos (no se deducen).",
        "Electores: según la resolución, la columna de electores del resumen general recoge los "
        "datos remitidos por la Oficina del Censo Electoral; no indica si incluyen el CERA.",
        "Voto CERA: la resolución publica aparte su escrutinio (anexo V) pero no dice "
        "expresamente si los anexos I a III lo incluyen.",
        "Escaños: solo los que figuran en el anexo II; las candidaturas del anexo III no "
        "obtuvieron escaño y no se les asigna cifra.",
        "Total de la comunidad publicado (fila TOTAL de los anexos I a III).",
    ]
    return Resultado(
        ccaa="07", eleccion=ELECCION, circunscripciones=circs, total=total, notas=notas
    )
