"""Navarra: elecciones al Parlamento de Navarra del 28 de mayo de 2023.

Fuente: BON núm. 147, de 14 de julio de 2023 (código de anuncio F2310356): Resolución 73/2023,
de 3 de julio, del director general de Presidencia y Gobierno Abierto, que publica como anexo el
acta de proclamación de la Junta Electoral Provincial de Navarra (6 de junio de 2023).
Circunscripción única (provincia 31).

El anexo (págs. 2 y 3 del PDF) es una imagen escaneada sin capa de texto: `pdftotext` solo
devuelve la resolución, y el OCR disponible (tesseract) confunde cifras (por ejemplo, lee 4.692
por 4.632). Por eso las cifras de este módulo son una transcripción manual del acta,
comprobada así:
- cada voto por candidatura coincide con su cifra en letra del acta;
- votos a candidaturas + blancos = válidos y válidos + nulos = votantes (cifras publicadas);
- la suma de electos es 50.
Además, `contraste_web` compara todas las cifras, electores incluidos (votantes +
abstención), con la página «Resultados Definitivos» del portal electoral del Gobierno de
Navarra; `leer` falla si no coinciden.

La transcripción vale solo para el fichero con la huella SHA-256 de `_SHA256`; con otro fichero
`leer` falla en vez de devolver cifras que podrían no corresponderle.
"""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa15-2023" / "autonomicas_ccaa15_2023-05-28.pdf"
# Página «Resultados Definitivos» del portal electoral del Gobierno de Navarra (impresión en
# PDF aportada por el responsable, con capa de texto): sirve para contrastar la transcripción.
PDF_WEB = AUTONOMICAS / "ccaa15-2023" / "navarra_resultados_definitivos_web.pdf"
# Siglas de la web, en el mismo orden que `_CANDIDATURAS`
_SIGLAS_WEB = [
    "UPN",
    "PSN-PSOE",
    "EH BILDU",
    "GEROA BAI",
    "PPN",
    "CONTIGO ZUREKIN",
    "VOX",
    "PUM+J",
    "CIUDADANOS",
    "EGUZKILORE",
    "VOLUNTAD FORAL",
]
_SHA256 = "24348e8ca40eae5714d5b851518ce378933e7493fca361c93b0fd71dfef26e05"

# Transcripción del acta de proclamación (pág. 2 del PDF), nombres tal como figuran.
_RESUMEN = {
    "electores": 518_998,
    "votantes": 334_493,
    "a_candidaturas": 324_001,
    "validos": 329_861,
    "nulos": 4_632,
    "blancos": 5_860,
}
_CANDIDATURAS: list[tuple[str, int, int | None]] = [  # (candidatura, votos, electos)
    ("UNION DEL PUEBLO NAVARRO", 92_392, 15),
    ("PARTIDO SOCIALISTA DE NAVARRA-PSOE", 68_247, 11),
    ("EUSKAL HERRIA BILDU", 56_535, 9),
    ("GEROA BAI", 43_660, 7),
    ("PARTIDO POPULAR", 24_019, 3),
    ("PODEMOS + IZQUIERDA UNIDA + BATZARRE + ALIANZA VERDE + BERDEAK EQUO", 20_095, 3),
    ("VOX", 14_197, 2),
    ("POR UN MUNDO MÁS JUSTO/BIDEZKO MUNDURANTZ", 1_740, None),
    ("CIUDADANOS", 1_273, None),
    ("EGUZKILORE", 1_261, None),
    ("VOLUNTAD FORAL", 582, None),
]


def _comprobar_fichero(path: Path) -> None:
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    if h != _SHA256:
        raise ValueError(
            f"{path} no es el fichero transcrito (SHA-256 {h}); hay que revisar la transcripción"
        )
    # Si algún día el anexo trae capa de texto, la transcripción manual sobra: se avisa.
    txt = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout
    if "UNION DEL PUEBLO NAVARRO" in txt:
        raise ValueError("el anexo tiene capa de texto: conviene leerlo en vez de transcribirlo")


def contraste_web(path: Path = PDF_WEB) -> list[str]:
    """Diferencias entre la transcripción del acta y la página de resultados definitivos."""
    import re

    txt = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout
    num = r"(\d{1,3}(?:\.\d{3})*)"
    dif: list[str] = []
    for (nombre, votos, electos), sig in zip(_CANDIDATURAS, _SIGLAS_WEB, strict=True):
        m = re.search(r"^\s*" + re.escape(sig) + r"\s+(\d+)\s+" + num + r"\s+\d+,\d+%", txt, re.M)
        if not m:
            dif.append(f"{sig}: no aparece en la web")
            continue
        if int(m.group(2).replace(".", "")) != votos:
            dif.append(f"{nombre}: acta {votos} ≠ web {m.group(2)}")
        if int(m.group(1)) != (electos or 0):
            dif.append(f"{nombre}: escaños acta {electos} ≠ web {m.group(1)}")
    # Primer bloque «2023 Resultados de participación»
    bloque = txt[txt.index("2023             Resultados de participación") :]
    filas = [
        [int(x.replace(".", "")) for x in re.findall(num + r"(?![\d,%])", ln)]
        for ln in bloque.splitlines()[:25]
        if re.match(r"^\s+\d", ln) and "%" not in ln
    ]
    votantes, abstencion = filas[0]
    validos, a_cand, blancos, nulos = filas[1]
    web = {
        "electores": votantes + abstencion,
        "votantes": votantes,
        "validos": validos,
        "a_candidaturas": a_cand,
        "blancos": blancos,
        "nulos": nulos,
    }
    for k, v in web.items():
        if _RESUMEN[k] != v:
            dif.append(f"{k}: acta {_RESUMEN[k]} ≠ web {v}")
    return dif


def leer(path: Path = PDF) -> Resultado:
    _comprobar_fichero(path)
    contraste = []
    if PDF_WEB.exists():
        dif = contraste_web()
        if dif:
            raise ValueError(f"la transcripción no coincide con la web oficial: {dif}")
        contraste = [
            "Contraste: todas las cifras transcritas (incluidos los electores = votantes + "
            "abstención) coinciden con la página «Resultados Definitivos» del portal electoral "
            "del Gobierno de Navarra (navarra_resultados_definitivos_web.pdf)."
        ]
    r = _RESUMEN
    c = Circunscripcion(
        codigo="31",
        nombre="Navarra",
        electores=r["electores"],
        votantes=r["votantes"],
        nulos=r["nulos"],
        blancos=r["blancos"],
        votos={n: v for n, v, _ in _CANDIDATURAS},
        escanos={n: e for n, _, e in _CANDIDATURAS if e is not None},
        validos=r["validos"],
        a_candidaturas=r["a_candidaturas"],
    )
    return Resultado(
        ccaa="15",
        eleccion="autonomicas-15-2023",
        circunscripciones=[c],
        total=None,
        notas=[
            "Fuente: BON núm. 147 de 14-7-2023 (anuncio F2310356), acta de proclamación de la "
            "Junta Electoral Provincial de Navarra (6-6-2023).",
            "El acta es una imagen escaneada sin capa de texto: cifras transcritas a mano y "
            "comprobadas con las cifras en letra y la aritmética del acta (véase el módulo).",
            *contraste,
            "Circunscripción única: el acta es a la vez el total de la comunidad; no se repite "
            "en `total`.",
            "La publicación no dice si los electores y votantes incluyen el CERA.",
        ],
    )
