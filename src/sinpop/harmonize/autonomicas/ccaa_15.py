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
El número de electores no tiene cifra en letra ni otra comprobación interna.

La transcripción vale solo para el fichero con la huella SHA-256 de `_SHA256`; con otro fichero
`leer` falla en vez de devolver cifras que podrían no corresponderle.
"""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa15-2023" / "autonomicas_ccaa15_2023-05-28.pdf"
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


def leer(path: Path = PDF) -> Resultado:
    _comprobar_fichero(path)
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
            "comprobadas con las cifras en letra y la aritmética del acta (véase el módulo). "
            "Los electores no tienen comprobación independiente.",
            "Circunscripción única: el acta es a la vez el total de la comunidad; no se repite "
            "en `total`.",
            "La publicación no dice si los electores y votantes incluyen el CERA.",
        ],
    )
