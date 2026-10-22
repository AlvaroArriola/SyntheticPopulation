"""Informe PDF de un resultado (pregunta o dato de la población) con varios gráficos (D-078).

Recibe el mismo JSON que ya enseña la interfaz y lo convierte en un PDF A4:

1. **Resumen**: enunciado, territorio, población y un texto generado con reglas fijas a partir de
   los números (opción más frecuente, empates dentro del intervalo, mayor diferencia entre grupos,
   confianza, diferencia con lo que mediría el CIS, preguntas del CIS en que se apoya). No usa
   ningún modelo de lenguaje: cada frase sale de una cifra del resultado.
2. **Distribución** con los intervalos del 80 % y del 95 % y, para las preguntas, la comparación
   entre lo que piensa la población y lo que mediría el CIS.
3. **Por grupos**: un mapa de calor por cada dimensión (edad, sexo, estudios, recuerdo de voto).
4. **Por comunidad**: mapa coloreado de la opción más frecuente, con Canarias en un recuadro.

Los colores son los de la interfaz (paleta de referencia validada). Sin semilla ni aleatoriedad:
el mismo resultado da el mismo PDF salvo la fecha de generación.
"""

from __future__ import annotations

import datetime as dt
import io
import json
import textwrap
from pathlib import Path

import numpy as np

SERIE = "#2a78d6"
RANGO = "#cde2fb"
TEXTO, TEXTO_2, TEXTO_3 = "#0b0b0b", "#52514e", "#63625d"
BORDE = "#e2e0da"
SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
A4 = (8.27, 11.69)
GEOJSON = Path(__file__).parent / "web" / "territorios.geojson"
DIMENSIONES = {
    "edad_4": "Edad",
    "sexo": "Sexo",
    "estudios_3": "Estudios",
    "actividad_3": "Situación laboral",
    "tamano_municipio_cis": "Tamaño del municipio",
    "ideologia_bloque": "Ideología",
    "recuerdo_voto_generales_familia": "Recuerdo de voto 2023",
    "religiosidad": "Religiosidad",
    "clase_subjetiva": "Clase social (autopercibida)",
    "ccaa": "Comunidad",
    "provincia": "Provincia",
}
TERRITORIALES = ("ccaa", "provincia")
MAX_DIMENSIONES_PDF = 4
EDAD = {"18-34": "18–34", "35-49": "35–49", "50-64": "50–64", "65+": "65 y más"}


def _pct(x: float, dec: int = 0) -> str:
    return f"{100 * x:.{dec}f}".replace(".", ",") + " %"


def _nivel_confianza(c: float) -> str:
    return "alta" if c >= 0.7 else "media" if c >= 0.4 else "baja"


# ---------------------------------------------------------------- normalización


def normalizar(tipo: str, datos: dict, etiquetas: dict) -> dict:
    """Pasa un resultado de pregunta o un dato de la población a una forma común."""
    if tipo == "dato":
        et = datos["etiquetas"]
        cats = [c for c in datos["categorias"] if c != "NC" or datos["total"][c]["p"] >= 0.005]
        conv = {c: et.get(c, c) for c in cats}

        def dist(d: dict) -> dict:
            return {conv[c]: {"p": d[c]["p"], "ic95": d[c]["ic95"]} for c in cats}

        return {
            "tipo": "dato",
            "titulo": datos["descripcion"],
            "opciones": list(conv.values()),
            "total": dist(datos["total"]),
            "medicion_cis": None,
            "por_subgrupo": {k: dist(v) for k, v in datos["por_subgrupo"].items()},
            "confianza": None,
            "conf_sub": {},
            "similares": [],
            "universo": f"{datos['universo']} ({_pct(datos['cuota_universo'])} de los adultos)",
            "procedencia": datos.get("procedencia", {}),
            "fuentes": datos.get("fuentes", []),
            "aviso": datos.get("aviso", ""),
            "etiquetas": etiquetas,
        }
    ops = list(datos["total"])
    return {
        "tipo": "pregunta",
        "titulo": datos.get("enunciado") or datos.get("id", ""),
        "opciones": ops,
        "total": datos["total"],
        "medicion_cis": datos.get("medicion_cis"),
        "por_subgrupo": datos.get("por_subgrupo", {}),
        "confianza": (datos.get("confianza") or {}).get("total"),
        "conf_sub": (datos.get("confianza") or {}).get("por_subgrupo", {}),
        "similares": datos.get("preguntas_similares", []),
        "universo": "personas de 18 años o más",
        "procedencia": {},
        "fuentes": [],
        "aviso": datos.get("aviso", ""),
        "llm": (datos.get("versiones") or {}).get("modelo_llm"),
        "etiquetas": etiquetas,
    }


def _nombre(dim: str, nivel: str, et: dict) -> str:
    if dim == "edad_4":
        return EDAD.get(nivel, nivel)
    return (et.get(dim) or {}).get(nivel, nivel)


# ---------------------------------------------------------------- texto automático


def resumen(r: dict) -> list[str]:
    """Frases del resumen; cada una sale de una cifra del resultado (sin LLM)."""
    t = r["total"]
    orden = sorted(r["opciones"], key=lambda o: -t[o]["p"])
    sust = [o for o in orden if o not in ("N.S.", "N.C.")]
    a = sust[0]
    ic = t[a].get("ic95")
    frases = [
        f"La respuesta más frecuente es «{a}», con un {_pct(t[a]['p'])}"
        + (f" (intervalo del 95 %: {_pct(ic[0])} a {_pct(ic[1])})." if ic else ".")
    ]
    if len(sust) > 1:
        b = sust[1]
        frases.append(f"Le sigue «{b}» con un {_pct(t[b]['p'])}.")
        if ic and t[b].get("ic95") and t[b]["ic95"][1] >= ic[0]:
            frases.append(
                f"Los intervalos de «{a}» y «{b}» se solapan: con estos datos no se puede "
                "afirmar cuál de las dos es mayor."
            )
    nsnc = sum(t[o]["p"] for o in ("N.S.", "N.C.") if o in t)
    if nsnc >= 0.05:
        frases.append(f"Un {_pct(nsnc)} no sabe o no contesta.")
    # mayor diferencia entre grupos para la opción más frecuente
    mejor = None
    for dim in DIMENSIONES:
        if dim in TERRITORIALES:
            continue
        # solo grupos con datos suficientes (confianza ≥ 50 % cuando la hay)
        vals = {
            k.split("=", 1)[1]: v[a]["p"]
            for k, v in r["por_subgrupo"].items()
            if k.split("=", 1)[0] == dim and a in v and r["conf_sub"].get(k, 1) >= 0.5
        }
        if len(vals) >= 2:
            lo, hi = min(vals, key=vals.get), max(vals, key=vals.get)
            rango = vals[hi] - vals[lo]
            if mejor is None or rango > mejor[0]:
                mejor = (rango, dim, lo, hi, vals[lo], vals[hi])
    if mejor and mejor[0] >= 0.05:
        _, dim, lo, hi, plo, phi = mejor
        et = r["etiquetas"]
        frases.append(
            f"La mayor diferencia entre grupos está en {DIMENSIONES[dim].lower()}: «{a}» va del "
            f"{_pct(plo)} ({_nombre(dim, lo, et)}) al {_pct(phi)} ({_nombre(dim, hi, et)})."
        )
    elif mejor:
        frases.append("Las diferencias entre grupos son pequeñas (menos de 5 puntos).")
    ccaa = {k[5:]: v[a]["p"] for k, v in r["por_subgrupo"].items() if k.startswith("ccaa=")}
    if len(ccaa) >= 2:
        lo, hi = min(ccaa, key=ccaa.get), max(ccaa, key=ccaa.get)
        et = r["etiquetas"]
        frases.append(
            f"Por comunidades, «{a}» va del {_pct(ccaa[lo])} ({_nombre('ccaa', lo, et)}) al "
            f"{_pct(ccaa[hi])} ({_nombre('ccaa', hi, et)})."
        )
    if r["medicion_cis"]:
        dif = r["medicion_cis"][a]["p"] - t[a]["p"]
        if abs(dif) >= 0.02:
            frases.append(
                f"Medido como lo mediría el CIS (su universo y su forma de preguntar), «{a}» "
                f"sería un {_pct(r['medicion_cis'][a]['p'])}, {abs(100 * dif):.0f} puntos "
                f"{'más' if dif > 0 else 'menos'}."
            )
    if r["confianza"] is not None:
        c = r["confianza"]
        frases.append(
            f"Confianza {_nivel_confianza(c)}: {_pct(c)} de probabilidad de que el error total de "
            "la distribución sea menor de 10 puntos, según el historial del sistema en preguntas "
            "parecidas."
        )
        bajas = [k for k, v in r["conf_sub"].items() if v < 0.5]
        if bajas:
            frases.append(
                f"{len(bajas)} de {len(r['conf_sub'])} grupos tienen confianza baja (menos del "
                "50 %): hay pocos datos para ellos y conviene leerlos con cautela."
            )
    if r["procedencia"]:
        p = ", ".join(
            f"{_pct(v)} {k}" for k, v in sorted(r["procedencia"].items(), key=lambda x: -x[1])
        )
        frases.append(
            f"Es un dato de la población, no una predicción. Procedencia de los valores: {p}. "
            "El margen solo recoge el error de simulación."
        )
    return frases


# ---------------------------------------------------------------- gráficos


def _estilo(ax) -> None:
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom"].set_color(BORDE)
    ax.tick_params(colors=TEXTO_2, labelsize=8, length=0)
    ax.xaxis.grid(True, color=BORDE, linewidth=0.6)
    ax.set_axisbelow(True)


def _barras(ax, r: dict) -> None:
    ops = r["opciones"]
    y = np.arange(len(ops))[::-1]
    for yi, o in zip(y, ops, strict=True):
        d = r["total"][o]
        if d.get("ic95"):
            ax.plot(d["ic95"], [yi, yi], color=TEXTO_3, linewidth=1, alpha=0.7)
        if d.get("ic80"):
            ax.barh(yi, d["ic80"][1] - d["ic80"][0], left=d["ic80"][0], height=0.62, color=RANGO)
        ax.barh(yi, d["p"], height=0.36, color=SERIE)
        ax.text(
            d.get("ic95", [0, d["p"]])[1] + 0.01,
            yi,
            _pct(d["p"]),
            va="center",
            fontsize=8,
            color=TEXTO,
        )
    ax.set_yticks(y, [textwrap.shorten(o, 34) for o in ops], fontsize=8, color=TEXTO)
    ax.set_xlim(
        0, min(1, max(r["total"][o].get("ic95", [0, r["total"][o]["p"]])[1] for o in ops) + 0.12)
    )
    ax.xaxis.set_major_formatter(lambda v, _: _pct(v))
    _estilo(ax)


def _comparacion(ax, r: dict) -> None:
    ops = r["opciones"]
    y = np.arange(len(ops))[::-1]
    for yi, o in zip(y, ops, strict=True):
        a, b = r["total"][o]["p"], r["medicion_cis"][o]["p"]
        ax.plot([a, b], [yi, yi], color=BORDE, linewidth=2, zorder=1)
        ax.scatter([a], [yi], s=90, color=SERIE, zorder=2, edgecolor="white", linewidth=1.5)
        ax.scatter([b], [yi], s=26, color=TEXTO_3, zorder=3, edgecolor="white", linewidth=1)
    ax.set_yticks(y, [textwrap.shorten(o, 34) for o in ops], fontsize=8, color=TEXTO)
    ax.xaxis.set_major_formatter(lambda v, _: _pct(v))
    _estilo(ax)
    ax.scatter([], [], color=SERIE, label="Lo que piensa la población")
    ax.scatter([], [], color=TEXTO_3, label="Como lo mediría el CIS")
    ax.legend(loc="lower right", fontsize=7.5, frameon=False, labelcolor=TEXTO_2)


def _calor(ax, r: dict, dim: str) -> None:
    from matplotlib.colors import ListedColormap

    claves = [k for k in r["por_subgrupo"] if k.split("=", 1)[0] == dim]
    ops = r["opciones"]
    m = np.array([[r["por_subgrupo"][k][o]["p"] for o in ops] for k in claves])
    cmap = ListedColormap(SEQ)
    ax.imshow(m, cmap=cmap, aspect="auto", vmin=m.min(), vmax=max(m.max(), m.min() + 1e-6))
    for i in range(m.shape[0]):
        baja = r["conf_sub"].get(claves[i], 1) < 0.5
        for j in range(m.shape[1]):
            t = (m[i, j] - m.min()) / (m.max() - m.min() or 1)
            ax.text(
                j,
                i,
                _pct(m[i, j]) + ("*" if baja else ""),
                ha="center",
                va="center",
                fontsize=7,
                color="white" if t > 0.55 else TEXTO,
            )
    ax.set_xticks(
        range(len(ops)),
        [textwrap.shorten(o, 16) for o in ops],
        fontsize=7,
        rotation=30,
        ha="right",
        color=TEXTO,
    )
    ax.set_yticks(
        range(len(claves)),
        [textwrap.shorten(_nombre(dim, k.split("=", 1)[1], r["etiquetas"]), 40) for k in claves],
        fontsize=7.5,
        color=TEXTO,
    )
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(DIMENSIONES.get(dim, dim), loc="left", fontsize=9.5, color=TEXTO, pad=6)


def _mapa(fig, r: dict, opcion: str) -> None:
    from matplotlib.collections import PatchCollection
    from matplotlib.colors import ListedColormap, Normalize
    from matplotlib.patches import Polygon as Pol

    geo = json.loads(GEOJSON.read_text("utf-8"))
    vals = {k[5:]: v[opcion]["p"] for k, v in r["por_subgrupo"].items() if k.startswith("ccaa=")}
    norm = Normalize(min(vals.values()), max(vals.values()) or 1)
    cmap = ListedColormap(SEQ)

    def dibujar(ax, canarias: bool) -> None:
        parches, colores = [], []
        for f in geo["features"]:
            p = f["properties"]
            if p["nivel"] != "CCAA" or (p["codigo"] == "05") != canarias:
                continue
            g = f["geometry"]
            polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
            for poly in polys:
                xy = np.array(poly[0])
                xy[:, 1] = np.degrees(np.log(np.tan(np.pi / 4 + np.radians(xy[:, 1]) / 2)))
                parches.append(Pol(xy, closed=True))
                colores.append(cmap(norm(vals[p["codigo"]])) if p["codigo"] in vals else BORDE)
        ax.add_collection(
            PatchCollection(parches, facecolor=colores, edgecolor="white", linewidth=0.6)
        )
        ax.autoscale_view()
        ax.set_aspect("equal")
        ax.axis("off")

    ax = fig.add_axes([0.08, 0.30, 0.84, 0.48])
    dibujar(ax, False)
    ax.set_xlim(-9.6, 4.6)
    ins = fig.add_axes([0.08, 0.22, 0.25, 0.12])
    dibujar(ins, True)
    for s in ins.spines.values():
        s.set_visible(True)
        s.set_color(BORDE)
    ins.axis("on")
    ins.set_xticks([])
    ins.set_yticks([])
    cax = fig.add_axes([0.58, 0.22, 0.3, 0.012])
    cb = fig.colorbar(
        __import__("matplotlib.cm", fromlist=["ScalarMappable"]).ScalarMappable(norm, cmap),
        cax=cax,
        orientation="horizontal",
    )
    cb.outline.set_visible(False)
    cb.ax.tick_params(labelsize=7, colors=TEXTO_2, length=0)
    cb.ax.xaxis.set_major_formatter(lambda v, _: _pct(v))


def _destacadas(r: dict) -> list[str]:
    """Dimensiones no territoriales ordenadas por cuánto separan las respuestas (la mayor
    diferencia entre grupos con confianza ≥ 50 %), como en la interfaz."""
    sust = [o for o in r["opciones"] if o not in ("N.S.", "N.C.")]
    out = []
    for dim in DIMENSIONES:
        if dim in TERRITORIALES:
            continue
        ks = [
            k
            for k in r["por_subgrupo"]
            if k.split("=", 1)[0] == dim
            and r["conf_sub"].get(k, 1) >= 0.5
            and k.split("=", 1)[1] not in ("NC", "NS", "NS_NC")
        ]
        if len(ks) < 2:
            continue
        sub = r["por_subgrupo"]
        dif = max(max(sub[k][o]["p"] for k in ks) - min(sub[k][o]["p"] for k in ks) for o in sust)
        out.append((dif, dim))
    return [d for _, d in sorted(out, reverse=True)]


def _similares(ids: list[str]) -> list[str]:
    """Enunciado, estudio y fecha de las preguntas del CIS en que se apoya la predicción."""
    if not ids:
        return []
    from sinpop.predict import banco as B

    b = {r["id"]: r for r in B.preguntas().iter_rows(named=True)}
    out = []
    for i in ids:
        x = b.get(i)
        out.append(
            f"{x['enunciado']} (CIS, estudio {x['estudio']}, {str(x['fecha'])[:7]})" if x else i
        )
    return out


# ---------------------------------------------------------------- documento


def _cabecera(fig, titulo: str, pagina: int, total: int) -> None:
    fig.text(0.08, 0.955, "España sintética", fontsize=9, color=TEXTO_3, weight="bold")
    fig.text(0.92, 0.955, f"{pagina}/{total}", fontsize=8, color=TEXTO_3, ha="right")
    fig.text(0.08, 0.925, titulo, fontsize=13, color=TEXTO, weight="bold")


def _pie(fig, aviso: str) -> None:
    fig.text(0.08, 0.035, "\n".join(textwrap.wrap(aviso, 120)), fontsize=6.5, color=TEXTO_3)


def generar(tipo: str, datos: dict, contexto: dict, etiquetas: dict) -> bytes:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages

    from sinpop.repro import code_version

    r = normalizar(tipo, datos, etiquetas)
    r["similares"] = _similares(r["similares"])
    if contexto.get("enunciado"):
        r["titulo"] = contexto["enunciado"]
    dims = _destacadas(r)[:MAX_DIMENSIONES_PDF]
    hay_mapa = contexto.get("territorio") == "ES" and any(
        k.startswith("ccaa=") for k in r["por_subgrupo"]
    )
    total = 2 + (1 if dims else 0) + (1 if hay_mapa else 0)
    buf = io.BytesIO()
    plt.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})
    meta = {
        "Title": f"España sintética · {r['titulo'][:80]}",
        "Subject": "Resultado simulado con una población sintética",
        "Creator": f"sinpop {code_version()}",
        "CreationDate": None,
        "ModDate": None,
    }
    with PdfPages(buf, metadata=meta) as pdf:
        # 1 · resumen
        fig = plt.figure(figsize=A4)
        _cabecera(fig, "Informe del resultado", 1, total)
        y = 0.88
        for linea in textwrap.wrap(r["titulo"], 70):
            fig.text(0.08, y, linea, fontsize=12, color=TEXTO)
            y -= 0.022
        hoy = dt.date.today().isoformat()
        if r["tipo"] == "dato":
            clase = "dato de la población (no es una predicción)"
        else:
            clase = "predicción " + (
                f"con {r['llm']}" if r.get("llm") else "sin modelo de lenguaje"
            )
        tam, rid = contexto.get("tamano", ""), contexto.get("run_id", "")
        metas = [
            f"Territorio: {contexto.get('territorio_nombre', '')}",
            f"Población sintética: {tam} personas ({rid})",
            f"Universo: {r['universo']}",
            f"Tipo: {clase}",
            f"Generado el {hoy} · código {code_version()}",
        ]
        y -= 0.01
        for m in metas:
            fig.text(0.08, y, m, fontsize=8.5, color=TEXTO_2)
            y -= 0.018
        y -= 0.015
        fig.text(0.08, y, "Resumen automático", fontsize=10.5, color=TEXTO, weight="bold")
        y -= 0.025
        for frase in resumen(r):
            for linea in textwrap.wrap(frase, 95):
                fig.text(0.08, y, linea, fontsize=9, color=TEXTO)
                y -= 0.017
            y -= 0.006
        if r["similares"]:
            y -= 0.01
            fig.text(
                0.08,
                y,
                "Se apoya en estas preguntas del CIS",
                fontsize=10.5,
                color=TEXTO,
                weight="bold",
            )
            y -= 0.022
            for s in r["similares"][:6]:
                for i, linea in enumerate(textwrap.wrap(s, 100)):
                    fig.text(
                        0.08, y, ("· " if i == 0 else "  ") + linea, fontsize=7.5, color=TEXTO_2
                    )
                    y -= 0.014
        if r["fuentes"]:
            y -= 0.01
            fig.text(0.08, y, "Fuentes", fontsize=10.5, color=TEXTO, weight="bold")
            y -= 0.022
            for f in r["fuentes"]:
                txt = f"· {f['nombre']}" + (f" ({f['organismo']})" if f.get("organismo") else "")
                txt += f" · variable {f['variable_original']}" if f.get("variable_original") else ""
                for linea in textwrap.wrap(txt, 100):
                    fig.text(0.08, y, linea, fontsize=7.5, color=TEXTO_2)
                    y -= 0.014
        _pie(fig, r["aviso"])
        pdf.savefig(fig)
        plt.close(fig)

        # 2 · distribución
        fig = plt.figure(figsize=A4)
        _cabecera(fig, "Distribución de las respuestas", 2, total)
        alto = 0.36 if r["medicion_cis"] else min(0.6, 0.06 * len(r["opciones"]) + 0.12)
        ax = fig.add_axes([0.32, 0.88 - alto, 0.6, alto - 0.04])
        _barras(ax, r)
        leyenda = "Barra: estimación · banda clara: intervalo del 80 % · línea: intervalo del 95 %"
        if r["tipo"] == "dato":
            leyenda = "Barra: proporción · línea: margen de simulación del 95 %"
        fig.text(0.32, 0.88 - alto - 0.03, leyenda, fontsize=7, color=TEXTO_3)
        if r["medicion_cis"]:
            fig.text(
                0.08,
                0.44,
                "Lo que piensa la población frente a como lo mediría el CIS",
                fontsize=10.5,
                color=TEXTO,
                weight="bold",
            )
            ax2 = fig.add_axes([0.32, 0.1, 0.6, 0.31])
            _comparacion(ax2, r)
        _pie(fig, r["aviso"])
        pdf.savefig(fig)
        plt.close(fig)

        pagina = 3
        if dims:
            fig = plt.figure(figsize=A4)
            _cabecera(fig, "Por grupos", pagina, total)
            filas = [len([k for k in r["por_subgrupo"] if k.startswith(d + "=")]) for d in dims]
            alto_total, y = 0.78, 0.86
            for d, n in zip(dims, filas, strict=True):
                h = alto_total * n / sum(filas) - 0.05
                ax = fig.add_axes([0.36, y - h, 0.56, h])
                _calor(ax, r, d)
                y -= h + 0.06
            if r["conf_sub"]:
                fig.text(
                    0.08,
                    0.06,
                    "* Confianza baja (menos del 50 %): pocos datos para ese grupo.",
                    fontsize=7,
                    color=TEXTO_3,
                )
            _pie(fig, r["aviso"])
            pdf.savefig(fig)
            plt.close(fig)
            pagina += 1

        if hay_mapa:
            t = r["total"]
            opcion = max(
                (o for o in r["opciones"] if o not in ("N.S.", "N.C.")), key=lambda o: t[o]["p"]
            )
            fig = plt.figure(figsize=A4)
            _cabecera(fig, f"«{textwrap.shorten(opcion, 40)}» por comunidad", pagina, total)
            fig.text(
                0.08,
                0.895,
                "Proporción de la respuesta más frecuente en cada comunidad.",
                fontsize=8.5,
                color=TEXTO_2,
            )
            _mapa(fig, r, opcion)
            _pie(fig, r["aviso"])
            pdf.savefig(fig)
            plt.close(fig)
    return buf.getvalue()
