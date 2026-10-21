"""Diagrama de calibración de la confianza (F10) en SVG, sin dependencias de gráficos (D-070).

Eje x: confianza media del intervalo; eje y: proporción de aciertos (TVD ≤ umbral). Una
confianza bien calibrada cae sobre la diagonal. El área de cada punto es proporcional a los casos.

Comando: `python -m sinpop.confidence.diagrama`
"""

from __future__ import annotations

import json
import math

from sinpop import REPORTS_DIR

DESTINO = REPORTS_DIR / "fase_10" / "diagrama_calibracion.svg"
COLORES = ["#2a6fb0", "#d0632a"]
L, T, A = 60, 20, 360  # margen izquierdo, margen superior, lado del gráfico


def _xy(c: float, a: float) -> tuple[float, float]:
    return L + c * A, T + (1 - a) * A


def svg(series: dict[str, list[dict]]) -> str:
    total = max(sum(b["casos"] for b in bs) for bs in series.values())
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{L + A + 230}" height="{T + A + 50}" '
        'font-family="sans-serif" font-size="12">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<rect x="{L}" y="{T}" width="{A}" height="{A}" fill="none" stroke="#999"/>',
    ]
    for i in range(11):
        v = i / 10
        x, y = _xy(v, v)
        p.append(f'<line x1="{x}" y1="{T}" x2="{x}" y2="{T + A}" stroke="#eee"/>')
        p.append(f'<line x1="{L}" y1="{y}" x2="{L + A}" y2="{y}" stroke="#eee"/>')
        if i % 2 == 0:
            e = f"{v:.1f}".replace(".", ",")
            p.append(f'<text x="{x}" y="{T + A + 16}" text-anchor="middle">{e}</text>')
            p.append(f'<text x="{L - 6}" y="{y + 4}" text-anchor="end">{e}</text>')
    x0, y0 = _xy(0, 0)
    x1, y1 = _xy(1, 1)
    p.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="#555" stroke-dasharray="4"/>')
    p.append(
        f'<text x="{L + A / 2}" y="{T + A + 36}" text-anchor="middle">confianza predicha</text>'
    )
    p.append(
        f'<text x="16" y="{T + A / 2}" text-anchor="middle" '
        f'transform="rotate(-90 16 {T + A / 2})">proporción de aciertos (TVD ≤ 0,10)</text>'
    )
    for k, (nombre, bs) in enumerate(series.items()):
        col = COLORES[k % len(COLORES)]
        pts = [_xy(b["confianza_media"], b["acierto"]) for b in bs]
        p.append(
            f'<polyline fill="none" stroke="{col}" stroke-width="1.5" points="'
            + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
            + '"/>'
        )
        for (x, y), b in zip(pts, bs, strict=True):
            r = 3 + 12 * math.sqrt(b["casos"] / total)
            p.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}" fill-opacity="0.45" '
                f'stroke="{col}"><title>{nombre} {b["bin"]}: {b["casos"]} casos</title></circle>'
            )
        ly = T + 20 + 22 * k
        p.append(f'<circle cx="{L + A + 20}" cy="{ly - 4}" r="6" fill="{col}"/>')
        p.append(f'<text x="{L + A + 32}" y="{ly}">{nombre}</text>')
    p.append("</svg>")
    return "\n".join(p)


def construir() -> None:
    series = {}
    bt = REPORTS_DIR / "fase_10" / "backtest_metricas.json"
    if bt.exists():
        m = json.loads(bt.read_text("utf-8"))["validacion_cruzada_backtest"]
        series["backtest (validación cruzada)"] = m["diagrama_calibracion"]
    va = REPORTS_DIR / "fase_10_validacion.json"
    if va.exists():
        v = json.loads(va.read_text("utf-8"))
        m = v[v.get("publicada", "calibrado_en_validacion")]
        series["validación jul.-sep. 2026"] = m["diagrama_calibracion"]
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(svg(series), "utf-8")


if __name__ == "__main__":
    construir()
