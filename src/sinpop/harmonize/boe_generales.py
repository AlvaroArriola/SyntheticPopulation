"""Resultados oficiales definitivos de las generales de 23 de julio de 2023 (Congreso).

Fuente: Resolución de 30 de agosto de 2023, de la Presidencia de la Junta Electoral Central,
por la que se publica el resumen de los resultados de las elecciones al Congreso de los
Diputados y al Senado (BOE núm. 209, de 1 de septiembre de 2023, BOE-A-2023-18907). Recoge
los datos de las actas de escrutinio general de las Juntas Electorales Provinciales (con voto
CERA). Solo se lee la parte del Congreso:

- Cuadro I (resumen general): electores, votantes, votos válidos, votos a candidaturas,
  votos en blanco y votos nulos por provincia, más la fila «Total estatal».
- Cuadro II: votos y escaños de cada formación que obtuvo escaño, por provincia, con la
  columna «Total escaños» de cada provincia y la fila «Total estatal».
- Cuadro III: votos de cada formación que no obtuvo escaño, por provincia, con la fila
  «Total estatal». Su `escanos` queda vacío (None): el cuadro no tiene esa columna.

Se ignoran la relación de diputados electos y todo lo del Senado. La corrección de errores
BOE-A-2023-19537 solo afecta al Senado.

Lectura con `pdftotext -bbox` (poppler), por coordenadas de palabra: los cuadros II y III son
tablas anchas repartidas en muchas páginas, con celdas vacías donde la formación no se
presentó (no se guarda ninguna fila, ni con 0). Cada cifra se asigna a la columna cuya
etiqueta («Votos», «Escaños», «Total escaños») empieza más a la derecha sin pasar del final
de la cifra (las cifras van alineadas a la derecha dentro de su columna). Cada palabra de la
cabecera se asigna a la columna con el centro más cercano.

Nombres de candidatura: tal como figuran en la cabecera, uniendo sus líneas con un espacio,
salvo cuando una línea termina en guion (corte de línea en un nombre compuesto, p. ej.
«Nueva Canarias-» + «Bloque Canarista»), que se une sin espacio. Las siglas son el contenido
del último paréntesis.

Cuadro I se lee con `pdftotext -layout` (una sola página, columnas regulares).
"""

from __future__ import annotations

import html
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import polars as pl

from sinpop import RAW_DIR
from sinpop.config import load_config

PDF = RAW_DIR / "infoelectoral_resultados/generales-2023/BOE-A-2023-18907.pdf"
ESCANOS_CONGRESO = 350
COLUMNAS_I = ("electores", "votantes", "validos", "a_candidaturas", "blancos", "nulos")

_NUM = r"\d{1,3}(?:\.\d{3})*"
_WORD = re.compile(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>'
)
# Cabecera y pie de cada página del BOE (y < _Y_CABECERA) y texto girado del margen derecho
# («Verificable en https://www.boe.es», «cve: BOE-A-…», x ≥ _X_MARGEN).
_Y_CABECERA = 90.0
_X_MARGEN = 558.0
# En el cuerpo de los cuadros II y III se admite un punto final tras la cifra: la fila
# «Total estatal» de Geroa Bai imprime «9.938.» (errata tipográfica; se lee 9.938 y se anota).
_CIFRA = rf"{_NUM}\.?"
# Palabras del título de cada cuadro: la cabecera de la tabla empieza por debajo de ellas.
_TITULO = {"CUADRO", "(Continuación)", "DIPUTADOS", "escaño"}


def _int(s: str) -> int:
    if not re.fullmatch(_NUM, s):
        raise ValueError(f"cifra ilegible: {s!r}")
    return int(s.replace(".", ""))


def _codigos_provincia() -> dict[str, str]:
    """{nombre impreso en el BOE: código INE}. «Coruña, A» → «Coruña (A)»."""
    t = load_config("territories.yaml")
    out = {}
    for p in t.provincias:  # type: ignore[attr-defined]
        nombre = re.sub(r"^(.*), (.*)$", r"\1 (\2)", p.nombre)
        out[nombre] = p.codigo
    return out


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


def _paginas(path: Path) -> list[list[_Palabra]]:
    out = subprocess.run(
        ["pdftotext", "-bbox", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout
    paginas = []
    for trozo in out.split("<page ")[1:]:
        ws = [
            _Palabra(float(a), float(b), float(c), float(d), html.unescape(t))
            for a, b, c, d, t in _WORD.findall(trozo)
        ]
        paginas.append([w for w in ws if w.y0 >= _Y_CABECERA and w.x0 < _X_MARGEN])
    return paginas


def _lineas(ws: list[_Palabra], tol: float = 2.0) -> list[list[_Palabra]]:
    """Agrupa palabras en líneas por su centro vertical."""
    out: list[list[_Palabra]] = []
    for w in sorted(ws, key=lambda w: (w.yc, w.x0)):
        if out and abs(out[-1][0].yc - w.yc) <= tol:
            out[-1].append(w)
        else:
            out.append([w])
    return [sorted(ln, key=lambda w: w.x0) for ln in out]


def _unir(trozos: list[str]) -> str:
    s = ""
    for t in trozos:
        if not s:
            s = t
        elif s.endswith("-") and len(s.split()[-1]) > 1:
            s += t
        else:
            s += " " + t
    return re.sub(r"\s+", " ", s).strip()


def _siglas(nombre: str) -> str:
    m = re.findall(r"\(([^()]*)\)", nombre)
    if not m:
        raise ValueError(f"candidatura sin siglas entre paréntesis: {nombre!r}")
    return m[-1].strip()


@dataclass
class _Tabla:
    cuadro: str  # "II" o "III"
    # {candidatura: {nombre de fila: (votos, escaños | None)}}
    celdas: dict[str, dict[str, tuple[int, int | None]]]
    total_escanos: dict[str, int]  # {nombre de fila: total escaños} (solo cuadro II)
    notas: list[str]


def _tabla(ws: list[_Palabra], cabecera: list[_Palabra], etiquetas: list[_Palabra]) -> _Tabla:
    """Lee una tabla de los cuadros II o III ya recortada de su página.

    `cabecera` son las palabras entre el título y la fila de etiquetas; `etiquetas`, la fila
    «Votos» / «Escaños»; `ws`, las palabras por debajo de esa fila hasta el final de la tabla.
    """
    etiquetas = sorted(etiquetas, key=lambda w: w.x0)
    cuadro = "II" if any(w.t == "Escaños" for w in etiquetas) else "III"
    x_min = etiquetas[0].x0
    # Columnas: (x de inicio, candidatura (índice) o None si es «Total escaños», campo)
    cols: list[tuple[float, int | None, str]] = []
    centros: list[float] = []
    for e in etiquetas:
        if e.t == "Votos":
            centros.append(e.xc)
            cols.append((e.x0, len(centros) - 1, "votos"))
        elif e.t == "Escaños":
            if not cols or cols[-1][2] != "votos":
                raise ValueError("cuadro II: «Escaños» sin «Votos» a su izquierda")
            centros[-1] = (cols[-1][0] + e.x1) / 2
            cols.append((e.x0, cols[-1][1], "escanos"))
        else:
            raise ValueError(f"etiqueta de columna inesperada: {e.t!r}")
    titulo_total = [w for w in cabecera if w.t in {"Total", "escaños"} and w.x1 < x_min]
    if cuadro == "II":
        if not titulo_total:
            raise ValueError("cuadro II sin columna «Total escaños»")
        cols.insert(0, (min(w.x0 for w in titulo_total), None, "total"))
    elif titulo_total:
        raise ValueError("cuadro III con columna «Total escaños»")

    # Nombres de candidatura
    partes: list[list[_Palabra]] = [[] for _ in centros]
    for w in cabecera:
        if w in titulo_total:
            continue
        i = min(range(len(centros)), key=lambda k: abs(centros[k] - w.xc))
        partes[i].append(w)
    nombres = []
    for p in partes:
        if not p:
            raise ValueError("columna sin nombre de candidatura")
        nombres.append(_unir([" ".join(w.t for w in ln) for ln in _lineas(p)]))

    # Filas: el nombre de la provincia termina en punto y puede ocupar varias líneas
    nombre_ws = [w for w in ws if w.x1 < x_min and not re.fullmatch(_CIFRA, w.t)]
    cifras = [w for w in ws if re.fullmatch(_CIFRA, w.t)]
    otras = [w for w in ws if w not in nombre_ws and w not in cifras]
    if otras:
        raise ValueError(f"palabras no reconocidas en el cuerpo: {[w.t for w in otras]}")
    filas: list[tuple[str, float, float]] = []
    trozos: list[list[_Palabra]] = []
    for ln in _lineas(nombre_ws):
        trozos.append(ln)
        texto = " ".join(w.t for w in ln)
        if texto.endswith("."):
            nombre = ""
            for t in trozos:
                txt = " ".join(w.t for w in t)
                nombre += txt if (not nombre or nombre.endswith("/")) else " " + txt
            filas.append((nombre[:-1], trozos[0][0].yc, trozos[-1][0].yc))
            trozos = []
    if trozos:
        raise ValueError(f"nombre de fila sin cerrar: {[w.t for t in trozos for w in t]}")

    celdas: dict[str, dict[str, tuple[int, int | None]]] = {n: {} for n in nombres}
    total_escanos: dict[str, int] = {}
    asignadas = 0
    notas = []
    for fila, ya, yb in filas:
        en_fila = [w for w in cifras if ya - 4 <= w.yc <= yb + 4]
        asignadas += len(en_fila)
        valores: dict[tuple[int | None, str], int] = {}
        for w in en_fila:
            cands = [c for c in cols if c[0] <= w.x1]
            if not cands:
                raise ValueError(f"{fila}: cifra {w.t} fuera de columna")
            x0, i, campo = max(cands, key=lambda c: c[0])
            if (i, campo) in valores:
                raise ValueError(f"{fila}: dos cifras en la misma columna ({w.t})")
            if w.t.endswith("."):
                cand = nombres[i] if i is not None else "Total escaños"
                notas.append(f"{fila}, {cand}: cifra impresa {w.t!r}, leída {w.t[:-1]!r}")
            valores[(i, campo)] = _int(w.t.removesuffix("."))
        for (i, campo), v in valores.items():
            if i is None:
                total_escanos[fila] = v
                continue
            if campo == "votos":
                esc = valores.get((i, "escanos"))
                if cuadro == "II" and esc is None:
                    raise ValueError(f"{fila}: {nombres[i]} con votos y sin escaños")
                celdas[nombres[i]][fila] = (v, esc)
            elif (i, "votos") not in valores:
                raise ValueError(f"{fila}: {nombres[i]} con escaños y sin votos")
    if asignadas != len(cifras):
        raise ValueError(f"cifras sin fila: {len(cifras) - asignadas}")
    return _Tabla(cuadro, celdas, total_escanos, notas)


def _tablas(paginas: list[list[_Palabra]]) -> list[_Tabla]:
    """Tablas de los cuadros II y III, desde la página del cuadro II hasta la de electos."""
    out = []
    dentro = False
    for ws in paginas:
        if dentro and "proclamados" in {w.t for w in ws}:
            break
        lineas = _lineas(ws)
        if not dentro:
            if not any([w.t for w in ln[:2]] == ["CUADRO", "II"] for ln in lineas if len(ln) >= 2):
                continue
            dentro = True
        # Filas de etiquetas: solo «Votos» y «Escaños»
        idx = [k for k, ln in enumerate(lineas) if all(w.t in {"Votos", "Escaños"} for w in ln)]
        cuadros = [k for k, ln in enumerate(lineas) if ln[0].t == "CUADRO"]
        for j, k in enumerate(idx):
            inicio = max([c for c in range(k) if any(w.t in _TITULO for w in lineas[c])] + [-1])
            if j > 0 and inicio < idx[j - 1]:
                raise ValueError("dos tablas en la página sin título entre ellas")
            fin = min([c for c in cuadros if c > k] + [len(lineas)])
            if j + 1 < len(idx) and fin > idx[j + 1]:
                raise ValueError("dos tablas en la página sin título entre ellas")
            cabecera = [w for ln in lineas[inicio + 1 : k] for w in ln]
            cuerpo = [w for ln in lineas[k + 1 : fin] for w in ln]
            out.append(_tabla(cuerpo, cabecera, lineas[k]))
    if not out:
        raise ValueError("no se encuentran los cuadros II y III")
    return out


def _cuadro_i(path: Path) -> tuple[dict[str, dict[str, int]], dict[str, int]]:
    txt = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True, check=True
    ).stdout
    pags = [
        p
        for p in txt.split("\f")
        if "CUADRO I" in p and re.search(r"Electores\s+Votantes\s+Votos Válidos", p)
    ]
    if len(pags) != 1:
        raise ValueError("no se encuentra una única página del cuadro I")
    cab = re.search(
        r"Electores\s+Votantes\s+Votos Válidos\s+Votos a Candidaturas\s+Votos en Blanco"
        r"\s+Votos Nulos",
        pags[0],
    )
    if cab is None:
        raise ValueError("cuadro I: no se reconoce la cabecera")
    filas: dict[str, dict[str, int]] = {}
    for ln in pags[0][cab.end() :].splitlines():
        m = re.match(r"\s*(\S.*?)\s+" + r"\s+".join([f"({_NUM})"] * 6) + r"\s*$", ln)
        if m:
            if m.group(1) in filas:
                raise ValueError(f"cuadro I: fila repetida {m.group(1)!r}")
            filas[m.group(1)] = dict(
                zip(COLUMNAS_I, (_int(g) for g in m.groups()[1:]), strict=True)
            )
    total = filas.pop("Total estatal", None)
    if total is None:
        raise ValueError("cuadro I: falta la fila «Total estatal»")
    return filas, total


def leer(path: Path = PDF) -> tuple[pl.DataFrame, pl.DataFrame, dict]:
    """Lee los cuadros I, II y III del Congreso.

    Devuelve (provincias, votos, totales):
    - provincias: provincia, nombre, electores, votantes, validos, a_candidaturas, blancos,
      nulos, escanos (de la columna «Total escaños» del cuadro II);
    - votos: provincia, candidatura, siglas, votos, escanos (None en el cuadro III);
    - totales: {"cuadro_i": fila «Total estatal» del cuadro I,
                "total_escanos": «Total escaños» de la fila «Total estatal» del cuadro II,
                "candidaturas": {candidatura: {"votos", "escanos"}} de las filas «Total
                estatal» de los cuadros II y III,
                "notas": incidencias de lectura (erratas tipográficas)}.
    """
    codigos = _codigos_provincia()
    filas_i, total_i = _cuadro_i(path)
    if set(filas_i) != set(codigos):
        raise ValueError(
            f"cuadro I: provincias distintas de las esperadas: "
            f"{sorted(set(filas_i) ^ set(codigos))}"
        )

    tablas = _tablas(_paginas(path))
    escanos_prov: dict[str, int] = {}
    total_escanos = None
    celdas: dict[tuple[str, str], tuple[int, int | None]] = {}
    totales_cand: dict[str, dict[str, int | None]] = {}
    cuadro_de: dict[str, str] = {}
    notas: list[str] = []
    for t in tablas:
        notas += t.notas
        for fila, v in t.total_escanos.items():
            if fila == "Total estatal":
                total_escanos = v
            elif escanos_prov.setdefault(fila, v) != v:
                raise ValueError(f"total de escaños distinto entre páginas: {fila}")
        for cand, filas in t.celdas.items():
            if cuadro_de.setdefault(cand, t.cuadro) != t.cuadro:
                raise ValueError(f"{cand} aparece en los cuadros II y III")
            for fila, (v, e) in filas.items():
                if fila == "Total estatal":
                    if cand in totales_cand:
                        raise ValueError(f"{cand}: total estatal repetido")
                    totales_cand[cand] = {"votos": v, "escanos": e}
                    continue
                if fila not in codigos:
                    raise ValueError(f"fila no reconocida: {fila!r}")
                if (codigos[fila], cand) in celdas:
                    raise ValueError(f"{cand}: {fila} repetida")
                celdas[(codigos[fila], cand)] = (v, e)
    if set(escanos_prov) != set(codigos):
        raise ValueError("cuadro II: faltan provincias en «Total escaños»")

    prov = pl.DataFrame(
        [
            {"provincia": codigos[n], "nombre": n, **v, "escanos": escanos_prov[n]}
            for n, v in filas_i.items()
        ]
    ).sort("provincia")
    votos = pl.DataFrame(
        [
            {"provincia": p, "candidatura": c, "siglas": _siglas(c), "votos": v, "escanos": e}
            for (p, c), (v, e) in celdas.items()
        ],
        schema={
            "provincia": pl.String,
            "candidatura": pl.String,
            "siglas": pl.String,
            "votos": pl.Int64,
            "escanos": pl.Int64,
        },
    ).sort("provincia", "candidatura")
    totales = {
        "cuadro_i": total_i,
        "total_escanos": total_escanos,
        "candidaturas": totales_cand,
        "notas": notas,
    }
    return prov, votos, totales


def errores(prov: pl.DataFrame, votos: pl.DataFrame, totales: dict) -> list[str]:
    """Comprobaciones internas de la publicación. Lista vacía si todo cuadra."""
    out = []
    for r in prov.iter_rows(named=True):
        p = r["provincia"]
        if r["votantes"] != r["validos"] + r["nulos"]:
            out.append(f"{p}: votantes ≠ válidos + nulos")
        if r["validos"] != r["a_candidaturas"] + r["blancos"]:
            out.append(f"{p}: válidos ≠ a candidaturas + blancos")
    suma = votos.group_by("provincia").agg(
        pl.col("votos").sum().alias("v"), pl.col("escanos").sum().alias("e")
    )
    j = prov.join(suma, on="provincia", how="left")
    for r in j.iter_rows(named=True):
        if r["v"] != r["a_candidaturas"]:
            out.append(f"{r['provincia']}: suma de candidaturas {r['v']} ≠ {r['a_candidaturas']}")
        if r["e"] != r["escanos"]:
            out.append(f"{r['provincia']}: suma de escaños {r['e']} ≠ {r['escanos']}")
    for c in COLUMNAS_I:
        s = prov[c].sum()
        if s != totales["cuadro_i"][c]:
            out.append(f"total estatal {c}: suma {s} ≠ publicado {totales['cuadro_i'][c]}")
    if prov["escanos"].sum() != ESCANOS_CONGRESO:
        out.append(f"suma de escaños provinciales {prov['escanos'].sum()} ≠ 350")
    if totales.get("total_escanos") != ESCANOS_CONGRESO:
        out.append(f"total estatal de escaños publicado {totales.get('total_escanos')} ≠ 350")
    por_cand = {
        r["candidatura"]: r
        for r in votos.group_by("candidatura")
        .agg(pl.col("votos").sum(), pl.col("escanos").sum())
        .iter_rows(named=True)
    }
    tc = totales.get("candidaturas", {})
    for c in sorted(set(por_cand) | set(tc)):
        if c not in tc:
            out.append(f"{c}: sin fila «Total estatal»")
            continue
        if c not in por_cand:
            out.append(f"{c}: total estatal sin votos provinciales")
            continue
        if por_cand[c]["votos"] != tc[c]["votos"]:
            out.append(f"{c}: suma de votos {por_cand[c]['votos']} ≠ total {tc[c]['votos']}")
        if tc[c]["escanos"] is not None and por_cand[c]["escanos"] != tc[c]["escanos"]:
            out.append(f"{c}: suma de escaños {por_cand[c]['escanos']} ≠ total {tc[c]['escanos']}")
    return out
