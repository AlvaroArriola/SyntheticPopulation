"""Canarias, elecciones al Parlamento de Canarias de 28 de mayo de 2023 (BOC núm. 121).

Fuente: Resolución de 16 de junio de 2023 del Presidente de la Junta Electoral de Canarias
(BOC núm. 121, de 22 de junio de 2023, anuncio 2027). Se leen:
- Anexo I (pág. 2): electores, votantes, válidos, votos a candidaturas, blancos y nulos por
  circunscripción;
- Anexos II y III (págs. 3 a 6, tablas giradas 90°): votos y escaños por formación y
  circunscripción. El anexo III recoge las formaciones «que no han obtenido escaño»: su
  escaño es 0 porque así lo dice el título del anexo, no por deducción.

Canarias elige diputados en dos tipos de circunscripción con papeletas distintas: la
autonómica (toda la comunidad) y siete insulares. Se devuelven las ocho en un solo
`Resultado` y se distinguen por el código:
    "05-AUT" autonómica; "35-GC", "35-LZ", "35-FV", "38-TF", "38-LP", "38-GO", "38-EH".
La autonómica y las insulares NO se suman entre sí: cada votante vota en ambas. Por eso no
se rellena `Resultado.total`: la publicación no da un total de electores ni de votantes de la
comunidad distinto de la fila de la circunscripción autonómica. La columna «TOTAL» de los
anexos II y III (suma de las ocho circunscripciones por formación) se contrasta dentro de
`leer()` y, si no cuadrase, se anotaría en `Resultado.notas`.

En la tabla, «―» significa que la formación no concurrió en esa circunscripción: no se
guarda (ni como 0). Los nombres de formación son los de los anexos II y III, tal como
figuran (en mayúsculas y abreviados en algunos casos), uniendo las líneas de cada celda.

Lectura con `pdftotext -bbox` (poppler), por coordenadas de palabra: las tablas de los
anexos II y III están giradas y la salida de texto plano mezcla las celdas.
"""

from __future__ import annotations

import html
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

from sinpop.harmonize.autonomicas import AUTONOMICAS, Circunscripcion, Resultado

PDF = AUTONOMICAS / "ccaa05-2023" / "autonomicas_ccaa05_2023-05-28.pdf"
ELECCION = "autonomicas-05-2023"

# Nombre en la publicación → (código, nombre)
CIRCUNSCRIPCIONES = {
    "AUTONÓMICA": ("05-AUT", "Autonómica"),
    "EL HIERRO": ("38-EH", "El Hierro"),
    "FUERTEVENTURA": ("35-FV", "Fuerteventura"),
    "GRAN CANARIA": ("35-GC", "Gran Canaria"),
    "LA GOMERA": ("38-GO", "La Gomera"),
    "LANZAROTE": ("35-LZ", "Lanzarote"),
    "LA PALMA": ("38-LP", "La Palma"),
    "TENERIFE": ("38-TF", "Tenerife"),
}
# Columnas de los anexos II y III, en orden de lectura
COLUMNAS = [*CIRCUNSCRIPCIONES, "TOTAL"]
PAGINA_ANEXO_I = 2
PAGINAS_ANEXOS_II_III = (3, 6)
_GUION = "―"
_NUM = r"\d{1,3}(?:\.\d{3})*"
_WORD = re.compile(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>'
)


def _int(s: str) -> int:
    if not re.fullmatch(r"\d+(?:\.\d{3})*", s):
        raise ValueError(f"cifra ilegible: {s!r}")
    return int(s.replace(".", ""))


@dataclass
class _Palabra:
    x0: float
    y0: float
    x1: float
    y1: float
    t: str

    @property
    def xc(self) -> float:
        return (self.x0 + self.x1) / 2

    @property
    def yc(self) -> float:
        return (self.y0 + self.y1) / 2


def _palabras(path: Path, primera: int, ultima: int) -> list[list[_Palabra]]:
    """Palabras con su caja, por página (coordenadas de la página sin girar)."""
    out = subprocess.run(
        ["pdftotext", "-f", str(primera), "-l", str(ultima), "-bbox", str(path), "-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    paginas = []
    for trozo in out.split("<page ")[1:]:
        paginas.append(
            [
                _Palabra(float(a), float(b), float(c), float(d), html.unescape(t))
                for a, b, c, d, t in _WORD.findall(trozo)
            ]
        )
    return paginas


def _anexo_i(path: Path) -> dict[str, dict[str, int]]:
    """Fila por circunscripción: electores, votantes, válidos, a candidaturas, blancos, nulos."""
    txt = subprocess.run(
        ["pdftotext", "-f", str(PAGINA_ANEXO_I), "-l", str(PAGINA_ANEXO_I), "-layout", str(path)]
        + ["-"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    # La cabecera ocupa tres líneas: «Votos a / candidaturas» y «Votos en / blanco» van
    # partidas por encima y por debajo de la línea de «Circunscripción».
    cab = re.search(
        r"Votos a\s+Votos en\s*\n\s*Circunscripción\s+Electores\s+Votantes\s+Votos válidos"
        r"\s+Votos nulos\s*\n\s*candidaturas\s+blanco",
        txt,
    )
    if cab is None:
        raise ValueError("anexo I: no se reconoce la cabecera de la tabla")
    filas = {}
    for ln in txt.splitlines():
        m = re.match(r"\s*([A-ZÁÉÍÓÚÑ ]+?)\s+" + r"\s+".join([f"({_NUM})"] * 6) + r"\s*$", ln)
        if m and m.group(1) in CIRCUNSCRIPCIONES:
            v = [_int(g) for g in m.groups()[1:]]
            filas[m.group(1)] = dict(
                zip(
                    ("electores", "votantes", "validos", "a_candidaturas", "blancos", "nulos"),
                    v,
                    strict=True,
                )
            )
    if set(filas) != set(CIRCUNSCRIPCIONES):
        raise ValueError(f"anexo I: faltan circunscripciones {set(CIRCUNSCRIPCIONES) - set(filas)}")
    return filas


def _columnas(ws: list[_Palabra], x_tope: float, y_tope: float) -> list[tuple[str, float]]:
    """Cabeceras de columna (nombre, y central) en orden de lectura, comprobadas."""
    circ = next(w for w in ws if w.t == "Circunscripciones")
    # «TOTAL» es la última columna: acota la tabla (fuera queda la cabecera del boletín)
    total = next(w for w in ws if w.t == "TOTAL" and circ.x0 - 12 < w.xc < x_tope)
    cab = [
        w
        for w in ws
        if circ.x0 - 12 < w.xc < x_tope
        and total.y0 - 2 < w.yc < y_tope
        and w.t != "Circunscripciones"
    ]
    grupos: list[list[_Palabra]] = []
    for w in sorted(cab, key=lambda w: -w.yc):
        if grupos and abs(grupos[-1][0].yc - w.yc) < 10:
            grupos[-1].append(w)
        else:
            grupos.append([w])
    cols = [
        (" ".join(w.t for w in sorted(g, key=lambda w: w.x0)), sum(w.yc for w in g) / len(g))
        for g in grupos
    ]
    if [c for c, _ in cols] != COLUMNAS:
        raise ValueError(f"anexos II/III: columnas inesperadas {[c for c, _ in cols]}")
    return cols


def _anexos_ii_iii(path: Path) -> list[tuple[str, dict[str, int], dict[str, int]]]:
    """[(formación, votos por columna, escaños por columna)] de los anexos II y III."""
    out = []
    for ws in _palabras(path, *PAGINAS_ANEXOS_II_III):
        cab = next(w for w in ws if w.t == "FORMACIONES")
        etiquetas = sorted(
            (w for w in ws if w.t in ("Votos", "Escaños") and w.x0 > cab.x1 + 5),
            key=lambda w: w.xc,
        )
        if not etiquetas:
            raise ValueError("anexos II/III: página sin filas")
        y_etiqueta = min(w.y0 for w in etiquetas)
        cols = _columnas(ws, etiquetas[0].x0 - 4, y_etiqueta)
        # Cabecera de la columna de nombres: «FORMACIONES POLÍTICAS [/ COALICIONES]»
        cab_nombres = [
            w
            for w in ws
            if w.t in ("FORMACIONES", "POLÍTICAS", "/", "COALICIONES") and abs(w.x0 - cab.x0) < 15
        ]
        x_cab = max(w.x1 for w in cab_nombres)
        y_cab = max(w.y1 for w in cab_nombres)
        # Cada formación: una fila «Votos», precedida de una «Escaños» en el anexo II
        partidos: list[dict] = []
        for w in etiquetas:
            if w.t == "Votos" and partidos and partidos[-1]["votos"] is None:
                partidos[-1]["votos"] = w
            else:
                partidos.append({"escanos": None, "votos": None, "nombre": []})
                partidos[-1]["escanos" if w.t == "Escaños" else "votos"] = w
        if any(p["votos"] is None for p in partidos):
            raise ValueError("anexos II/III: fila de escaños sin fila de votos")
        for p in partidos:
            filas = [f for f in (p["escanos"], p["votos"]) if f is not None]
            p["x"] = sum(f.xc for f in filas) / len(filas)
        # Nombre: palabras a la derecha de la columna de etiquetas, agrupadas en líneas
        nombre = [
            w
            for w in ws
            if y_etiqueta + 20 < w.y0 and w.y1 < y_cab + 15 and x_cab < w.x0 < etiquetas[-1].x1 + 15
        ]
        lineas: list[list[_Palabra]] = []
        for w in sorted(nombre, key=lambda w: w.x0):
            if lineas and abs(lineas[-1][0].x0 - w.x0) < 3:
                lineas[-1].append(w)
            else:
                lineas.append([w])
        for ln in lineas:
            xc = sum(w.xc for w in ln) / len(ln)
            p = min(partidos, key=lambda p: abs(p["x"] - xc))
            p["nombre"].append(" ".join(w.t for w in sorted(ln, key=lambda w: -w.yc)))
        for p in partidos:
            fila: dict[str, dict[str, int]] = {}
            for clave in ("escanos", "votos"):
                if p[clave] is None:
                    continue
                celdas = [
                    w
                    for w in ws
                    if abs(w.xc - p[clave].xc) < 8 and cols[-1][1] - 20 < w.yc < y_etiqueta
                ]
                if len(celdas) != len(COLUMNAS):
                    raise ValueError(f"{p['nombre']}: {len(celdas)} celdas en la fila {clave}")
                fila[clave] = {}
                for w in celdas:
                    col = min(cols, key=lambda c: abs(c[1] - w.yc))[0]
                    if col in fila[clave]:
                        raise ValueError(f"{p['nombre']}: dos celdas en la columna {col}")
                    if w.t != _GUION:
                        fila[clave][col] = _int(w.t)
            nombre_p = re.sub(r"\s+", " ", " ".join(p["nombre"])).strip()
            if not nombre_p:
                raise ValueError("anexos II/III: formación sin nombre")
            out.append((nombre_p, fila["votos"], fila.get("escanos")))
    return out


def leer(path: Path = PDF) -> Resultado:
    resumen = _anexo_i(path)
    formaciones = _anexos_ii_iii(path)
    notas = [
        "Ocho circunscripciones con papeletas distintas: la autonómica (05-AUT) y siete "
        "insulares. No se suman entre sí; no hay total de la comunidad en la publicación.",
        "Formaciones del anexo III («que no han obtenido escaño»): escaños = 0 por el título "
        "del anexo.",
        "La publicación da en sus anexos V y VI el voto CERA por consulado e isla, pero no dice "
        "expresamente si el anexo I lo incluye.",
    ]
    nombres = [n for n, _, _ in formaciones]
    if len(set(nombres)) != len(nombres):
        raise ValueError("anexos II/III: formación repetida")
    for nombre, votos, _ in formaciones:
        suma = sum(v for k, v in votos.items() if k != "TOTAL")
        if votos.get("TOTAL") != suma:
            notas.append(f"{nombre}: columna TOTAL publicada {votos.get('TOTAL')} ≠ suma {suma}")
    for nombre, _, escanos in formaciones:
        if escanos is not None:
            suma = sum(v for k, v in escanos.items() if k != "TOTAL")
            if escanos.get("TOTAL") != suma:
                notas.append(f"{nombre}: escaños TOTAL publicados {escanos.get('TOTAL')} ≠ {suma}")
    circs = []
    for etiqueta, (codigo, nombre) in CIRCUNSCRIPCIONES.items():
        r = resumen[etiqueta]
        votos, escanos = {}, {}
        for formacion, v, e in formaciones:
            if etiqueta not in v:
                continue
            votos[formacion] = v[etiqueta]
            if e is None:
                escanos[formacion] = 0
            elif etiqueta in e:
                escanos[formacion] = e[etiqueta]
        circs.append(
            Circunscripcion(
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
        )
    for c in circs:
        suma = sum(c.votos.values())
        if suma != c.a_candidaturas:
            notas.append(
                f"Discrepancia en la propia publicación, {c.nombre} ({c.codigo}): la suma de los "
                f"votos por formación de los anexos II y III es {suma}, y el anexo I da "
                f"{c.a_candidaturas} votos a candidaturas (y válidos y votantes coherentes con "
                "esa cifra). Se conservan las cifras publicadas; `errores()` lo señala."
            )
    return Resultado(ccaa="05", eleccion=ELECCION, circunscripciones=circs, notas=notas)
