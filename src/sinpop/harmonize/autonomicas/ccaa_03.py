"""Principado de Asturias, elecciones a la Junta General de 28 de mayo de 2023 (BOPA).

Fuente: BOPA núm. 119, de 22 de junio de 2023 (cód. 2023-05292), Junta Electoral Provincial
de Asturias: «Actas de escrutinio y anexo al acta de escrutinio voto CERA». Las páginas 1 a 3
son las actas de proclamación de las tres circunscripciones (Centro, Occidente y Oriente);
las páginas 4 a 10, el anexo CERA (votos recibidos por consulado), que no se lee aquí.

El PDF no tiene texto extraíble (las fuentes no traen correspondencia a Unicode), así que se
lee por OCR: cada página se rasteriza a 300 ppp en gris (`pdftoppm`), se localiza la rejilla
de las tablas por proyección de píxeles oscuros y se pasa `tesseract -l spa` celda a celda.
Todo en un directorio temporal. Las cifras se aceptan solo si:
- el número escrito en cifras coincide con el escrito en letra (columna «EN LETRA»);
- las cifras del resumen cuadran: válidos = a candidaturas + blancos, votantes = válidos +
  nulos (y lo comprueba también `Resultado.errores()`), y la suma de candidaturas reproduce
  los votos a candidaturas.
Si algo no se lee con seguridad, `leer()` falla con un error que dice qué celda; nunca se
completa una cifra.

Escaños: la columna «NÚM ELECTOS» del acta; una casilla en blanco se toma como 0 electos.
Nombres de candidatura: los del acta, con espacios normalizados; solo se corrigen artefactos
evidentes del OCR en los nombres (tabla `_CORRECCIONES_OCR`), nunca en las cifras.

Las actas no dicen si los electores y votos incluyen el voto CERA (el anexo CERA solo da
votos por consulado), y no hay total de la comunidad: `Resultado.total` queda a None.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
import unicodedata
from pathlib import Path

import numpy as np

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa03-2023" / "autonomicas_ccaa03_2023-05-28.pdf"
ELECCION = "autonomicas-03-2023"
PPP = 300
# Página del acta → (código, nombre, rótulo de la circunscripción en el acta)
PAGINAS = {
    1: ("33-C", "Central", "CENTRO"),
    2: ("33-OC", "Occidental", "OCCIDENTE"),
    3: ("33-OR", "Oriental", "ORIENTE"),
}
_RESUMEN = {
    "electores": r"ELECTORES",
    "votantes": r"VOTANTES",
    "a_candidaturas": r"CANDIDATURAS",
    "validos": r"V[AÁ]LIDOS",
    "nulos": r"NULOS",
    "blancos": r"BLANCO",
}
# Artefactos del OCR en nombres (lectura errónea → texto impreso), revisados a mano
_CORRECCIONES_OCR = {
    # «IU» leído como «lU» (ele minúscula) en el acta de Oriente
    "CONVOCATORIA POR ASTURIES lU-MÁS PAÍS-IAS": "CONVOCATORIA POR ASTURIES IU-MÁS PAÍS-IAS",
}
_NUM = re.compile(r"\d{1,3}(?:\.\d{3})*")

# --- Números escritos en letra ----------------------------------------------------------

_UNIDADES = {
    "un": 1, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6,
    "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12, "trece": 13,
    "catorce": 14, "quince": 15, "dieciseis": 16, "diecisiete": 17, "dieciocho": 18,
    "diecinueve": 19, "veinte": 20, "veintiun": 21, "veintiuno": 21, "veintiuna": 21,
    "veintidos": 22, "veintitres": 23, "veinticuatro": 24, "veinticinco": 25,
    "veintiseis": 26, "veintisiete": 27, "veintiocho": 28, "veintinueve": 29,
    "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
    "ochenta": 80, "noventa": 90, "cien": 100, "ciento": 100, "doscientos": 200,
    "doscientas": 200, "trescientos": 300, "trescientas": 300, "cuatrocientos": 400,
    "cuatrocientas": 400, "quinientos": 500, "quinientas": 500, "seiscientos": 600,
    "seiscientas": 600, "setecientos": 700, "setecientas": 700, "ochocientos": 800,
    "ochocientas": 800, "novecientos": 900, "novecientas": 900,
}  # fmt: skip


def _sin_tildes(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    ).lower()


def _grupo(palabras: list[str]) -> int | None:
    """Número de 1 a 999: [centena] [decena [y unidad] | unidad de 1 a 29]."""
    v, i = 0, 0
    if i < len(palabras) and 100 <= _UNIDADES.get(palabras[i], 0):
        v += _UNIDADES[palabras[i]]
        i += 1
        if v == 100 and palabras[i - 1] == "cien" and i < len(palabras):
            return None  # «cien» va solo; si sigue algo es «ciento»
    if i < len(palabras) and 30 <= _UNIDADES.get(palabras[i], 0) <= 90:
        v += _UNIDADES[palabras[i]]
        i += 1
        if i < len(palabras) and palabras[i] == "y":
            if i + 1 >= len(palabras) or not 1 <= _UNIDADES.get(palabras[i + 1], 0) <= 9:
                return None
            v += _UNIDADES[palabras[i + 1]]
            i += 2
    elif i < len(palabras) and 1 <= _UNIDADES.get(palabras[i], 0) <= 29:
        v += _UNIDADES[palabras[i]]
        i += 1
    return v if i == len(palabras) and v > 0 else None


def numero_en_letra(texto: str) -> int | None:
    """Entero escrito en letra (castellano, hasta 999.999) o None si no se reconoce."""
    palabras = re.findall(r"[a-zñ]+", _sin_tildes(texto))
    if not palabras or palabras.count("mil") > 1:
        return None
    if "mil" not in palabras:
        return _grupo(palabras)
    i = palabras.index("mil")
    miles = _grupo(palabras[:i]) if i else 1
    resto = _grupo(palabras[i + 1 :]) if i + 1 < len(palabras) else 0
    if miles is None or resto is None or (i and miles == 1):
        return None  # «un mil» no se usa
    return miles * 1000 + resto


# --- Imagen y rejilla -------------------------------------------------------------------


def _pgm(path: Path) -> np.ndarray:
    datos = path.read_bytes()
    cab = datos.split(maxsplit=4)
    if cab[0] != b"P5":
        raise ValueError(f"{path}: no es PGM binario")
    ancho, alto = int(cab[1]), int(cab[2])
    return np.frombuffer(datos[-ancho * alto :], dtype=np.uint8).reshape(alto, ancho)


def _guardar_pgm(img: np.ndarray, path: Path) -> None:
    alto, ancho = img.shape
    path.write_bytes(f"P5\n{ancho} {alto}\n255\n".encode() + img.astype(np.uint8).tobytes())


def _picos(perfil: np.ndarray, umbral: float, sep: int) -> list[int]:
    """Máximos locales por encima del umbral, separados al menos `sep` píxeles."""
    perfil = perfil.astype(float).copy()
    out = []
    while True:
        i = int(perfil.argmax())
        if perfil[i] <= umbral:
            break
        out.append(i)
        perfil[max(0, i - sep) : i + sep + 1] = 0
    return sorted(out)


def _rejilla(oscuro: np.ndarray) -> tuple[list[int], list[int], tuple[int, int]]:
    """(x de las 6 líneas verticales de la tabla, y de sus líneas horizontales, (y0, y1) del
    recuadro de resumen)."""
    alto, ancho = oscuro.shape
    y0, y1 = int(0.45 * alto), int(0.78 * alto)  # franja siempre dentro de la tabla
    perfil = np.convolve(oscuro[y0:y1].sum(0), np.ones(9), "same")
    perfil[: int(0.28 * ancho)] = 0  # barra azul y marco de la página
    perfil[int(0.88 * ancho) :] = 0
    xs = _picos(perfil, 2 * (y1 - y0), 25)
    if len(xs) != 6:
        raise ValueError(f"rejilla: {len(xs)} líneas verticales en la tabla (se esperan 6)")
    fila = oscuro[:, xs[0] : xs[-1]].sum(1)
    lineas = []
    for y in np.where(fila > 0.9 * (xs[-1] - xs[0]))[0]:
        if lineas and y - lineas[-1][-1] <= 4:
            lineas[-1].append(int(y))
        else:
            lineas.append([int(y)])
    ys = [round(sum(g) / len(g)) for g in lineas]
    # La tabla es el tramo más largo de líneas con separación regular (< 140 px)
    tramos: list[list[int]] = []
    for y in ys:
        if tramos and y - tramos[-1][-1] < 140:
            tramos[-1].append(y)
        else:
            tramos.append([y])
    tabla = max(tramos, key=len)
    previa = ys[ys.index(tabla[0]) - 1]
    return xs, tabla, (previa, tabla[0])


# --- OCR --------------------------------------------------------------------------------


def _ocr(img: np.ndarray, tmp: Path, psm: int, cifras: bool = False) -> str:
    f = tmp / "celda.pgm"
    # margen blanco alrededor: tesseract lee peor el texto pegado al borde
    _guardar_pgm(np.pad(img, 20, constant_values=255), f)
    cmd = ["tesseract", str(f), "stdout", "-l", "spa", "--psm", str(psm)]
    if cifras:
        cmd += ["-c", "tessedit_char_whitelist=0123456789."]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return re.sub(r"\s+", " ", out).strip()


def _celda(gris: np.ndarray, x0: int, x1: int, y0: int, y1: int, m: int = 8) -> np.ndarray:
    """Recorte de la celda sin las líneas de la rejilla.

    La página está algo girada: la posición de cada línea se estima en la página entera y
    puede desviarse unos píxeles en una fila concreta, y el texto va pegado a las líneas.
    Se recorta con `m` píxeles de holgura y, en cada lado, se corta por dentro de la línea
    real (fila o columna del borde con tinta en más del 75 % de su longitud); si no se
    encuentra (línea entrecortada), se corta a 2 píxeles de la posición estimada.
    """
    c = gris[y0 - m : y1 + m + 1, x0 - m : x1 + m + 1]
    oscuro = c < 160
    cortes = []
    for eje in (0, 1):  # 0: filas (líneas horizontales), 1: columnas (verticales)
        frac = oscuro.mean(axis=1 - eje)
        n = len(frac)
        ini = [i for i in range(2 * m + 1) if frac[i] > 0.75]
        fin = [i for i in range(n - 2 * m - 1, n) if frac[i] > 0.75]
        cortes.append((max(ini) + 2 if ini else m + 2, min(fin) - 1 if fin else n - m - 1))
    (a, b), (i, j) = cortes
    return c[a:b, i:j].copy()


def _linea_de_cifras(c: np.ndarray) -> np.ndarray:
    """Banda de texto principal de una celda numérica (una sola línea).

    La página está algo girada y las líneas verticales de la rejilla dejan restos
    entrecortados junto al borde, que el OCR lee como cifras o puntos. Se toma la banda de
    filas con más tinta, calculada sin los 10 píxeles de cada lado, y se descarta el resto.
    """
    tinta = (c[:, 10:-10] < 160).sum(1)
    bandas = _bandas(tinta > 0, hueco=3)
    if not bandas:
        return c[:0]
    b0, b1 = max(bandas, key=lambda b: int(tinta[b[0] : b[1] + 1].sum()))
    return c[max(0, b0 - 3) : b1 + 4]


def _cifra(texto: str, donde: str) -> int:
    t = texto.replace(" ", "")
    if not re.fullmatch(_NUM.pattern, t):
        raise ValueError(f"{donde}: cifra ilegible {texto!r}")
    return int(t.replace(".", ""))


def _leer_cifra(img: np.ndarray, tmp: Path, donde: str) -> str:
    """Cifra leída dos veces, con dos modos de tesseract (línea con solo dígitos y bloque
    libre): las dos lecturas deben coincidir; si no, la cifra no se lee con seguridad y se
    detiene la lectura. Casilla vacía → ''."""
    a = _ocr(img, tmp, 7, cifras=True)
    b = _ocr(img, tmp, 6).replace(" ", "")
    if not a and not re.search(r"\d", b):
        return ""
    if a != b:
        raise ValueError(f"{donde}: lecturas distintas de la misma cifra {a!r} / {b!r}")
    return a


def _pagina(path: Path, pagina: int, tmp: Path) -> dict:
    prefijo = tmp / f"p{pagina}"
    subprocess.run(
        ["pdftoppm", "-r", str(PPP), "-gray", "-f", str(pagina), "-l", str(pagina)]
        + [str(path), str(prefijo)],
        check=True,
    )
    (img_path,) = tmp.glob(f"p{pagina}-*.pgm")
    gris = _pgm(img_path)
    img_path.unlink()
    xs, ys, (r0, r1) = _rejilla(gris < 160)

    # Rótulo de la circunscripción, encima del recuadro de resumen
    cabecera = _ocr(gris[int(0.04 * gris.shape[0]) : r0], tmp, 4)

    # Recuadro de resumen: dos cajas (izquierda y derecha) con tres cifras cada una
    resumen: dict[str, int] = {}
    perfil = (gris[r0:r1] < 160).sum(0)
    bordes = [x for x in _picos(perfil, 0.8 * (r1 - r0), 15) if xs[0] - 60 < x < xs[-1] + 60]
    if len(bordes) != 4:
        raise ValueError(f"página {pagina}: {len(bordes)} bordes en el resumen (se esperan 4)")
    for bx0, bx1 in ((bordes[0], bordes[1]), (bordes[2], bordes[3])):
        caja = gris[r0 + 5 : r1 - 4, bx0 + 6 : bx1 - 5]
        # Etiqueta a la izquierda, cifra alineada a la derecha: se separan por columnas
        corte = int(0.72 * caja.shape[1])
        etiquetas = caja[:, :corte]
        cifras = caja[:, corte:]
        # Filas del recuadro: tres bandas de texto
        tinta = (cifras < 160).sum(1) > 0
        bandas = _bandas(tinta)
        if len(bandas) != 3:
            raise ValueError(f"página {pagina}: {len(bandas)} cifras en una caja del resumen")
        for b0, b1 in bandas:
            # la etiqueta puede ocupar dos líneas (VOTOS A / CANDIDATURAS): banda ampliada
            e0, e1 = max(0, b0 - 45), min(caja.shape[0], b1 + 45)
            etiqueta = _ocr(etiquetas[e0:e1], tmp, 6)
            cifra = _leer_cifra(cifras[max(0, b0 - 8) : b1 + 8], tmp, f"página {pagina}")
            claves = [k for k, pat in _RESUMEN.items() if re.search(pat, etiqueta.upper())]
            if "a_candidaturas" in claves and len(claves) > 1:
                claves = ["a_candidaturas"]
            if len(claves) != 1 or claves[0] in resumen:
                raise ValueError(f"página {pagina}: etiqueta de resumen ilegible {etiqueta!r}")
            resumen[claves[0]] = _cifra(cifra, f"página {pagina}, {claves[0]}")
    if set(resumen) != set(_RESUMEN):
        raise ValueError(
            f"página {pagina}: faltan cifras del resumen {set(_RESUMEN) - set(resumen)}"
        )

    # Tabla de candidaturas: Nº | CANDIDATURAS | EN LETRA | EN NÚM. | NÚM ELECTOS
    filas = []
    for y0, y1 in zip(ys, ys[1:], strict=False):
        donde = f"página {pagina}, fila {len(filas) + 1}"
        # votos: una lectura; se contrasta después con la cifra en letra
        num = _ocr(_linea_de_cifras(_celda(gris, xs[3], xs[4], y0, y1)), tmp, 7, cifras=True)
        if not num.strip("."):
            continue  # cabeceras y filas vacías: sin cifra de votos
        orden = str(len(filas) + 1)
        nombre = _ocr(_celda(gris, xs[1], xs[2], y0, y1), tmp, 6)
        letra = _ocr(_celda(gris, xs[2], xs[3], y0, y1), tmp, 6)
        electos = _leer_cifra(_linea_de_cifras(_celda(gris, xs[4], xs[5], y0, y1)), tmp, donde)
        donde = f"página {pagina}, fila {orden} ({nombre})"
        votos = _cifra(num, donde)
        en_letra = numero_en_letra(letra)
        if en_letra != votos:
            raise ValueError(f"{donde}: cifra {votos} ≠ letra {letra!r} ({en_letra})")
        filas.append(
            {
                "orden": int(orden),
                "nombre": nombre,
                "votos": votos,
                "electos": _cifra(electos, donde) if electos else 0,
            }
        )
    return {"cabecera": cabecera, "resumen": resumen, "filas": filas}


def _bandas(tinta: np.ndarray, hueco: int = 12) -> list[tuple[int, int]]:
    """Tramos con tinta separados por al menos `hueco` filas en blanco."""
    out: list[list[int]] = []
    for i in np.where(tinta)[0]:
        if out and i - out[-1][1] <= hueco:
            out[-1][1] = int(i)
        else:
            out.append([int(i), int(i)])
    return [(a, b) for a, b in out if b - a >= 8]


def _nombre(texto: str) -> str:
    t = re.sub(r"\s+", " ", texto).strip()
    return _CORRECCIONES_OCR.get(t, t)


def leer(path: Path = PDF) -> Resultado:
    circs = []
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        for pagina, (codigo, nombre, rotulo) in PAGINAS.items():
            p = _pagina(path, pagina, tmp)
            if rotulo not in p["cabecera"].upper():
                raise ValueError(f"página {pagina}: no figura la circunscripción {rotulo}")
            r = p["resumen"]
            votos = {_nombre(f["nombre"]): f["votos"] for f in p["filas"]}
            if len(votos) != len(p["filas"]):
                raise ValueError(f"página {pagina}: candidaturas repetidas")
            circs.append(
                Circunscripcion(
                    codigo=codigo,
                    nombre=nombre,
                    electores=r["electores"],
                    votantes=r["votantes"],
                    nulos=r["nulos"],
                    blancos=r["blancos"],
                    votos=votos,
                    escanos={_nombre(f["nombre"]): f["electos"] for f in p["filas"]},
                    validos=r["validos"],
                    a_candidaturas=r["a_candidaturas"],
                )
            )
    notas = [
        "Lectura por OCR de las actas de proclamación (BOPA núm. 119, 22-VI-2023); cada voto "
        "por candidatura coincide con su expresión en letra.",
        "Las actas no dicen si incluyen el voto CERA (el anexo CERA solo da votos por "
        "consulado). No hay total de la comunidad en la publicación.",
        "Escaños: casilla «NÚM ELECTOS» en blanco = 0.",
    ]
    return Resultado(ccaa="03", eleccion=ELECCION, circunscripciones=circs, notas=notas)
