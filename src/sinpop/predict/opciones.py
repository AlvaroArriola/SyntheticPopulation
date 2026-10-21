"""Opciones de respuesta: normalización y alineación entre preguntas (F9) (D-069).

Una pregunta análoga del banco solo sirve si sus respuestas se pueden llevar a las opciones de la
pregunta nueva sin inventar nada:

1. **Por etiqueta:** la misma etiqueta normalizada (minúsculas, sin acentos, sin «(NO LEER)»).
   «N.S.», «No sabe», «No recuerda»… van a NS; «N.C.», «No contesta», a NC.
2. **Por posición (escalas ordinales):** si las dos son ordinales y tienen el mismo número de
   opciones sustantivas, la k-ésima va a la k-ésima.
3. **Escalas numéricas** (0-10, 1-10, 1-7…): por posición relativa en el recorrido.

Si alguna opción sustantiva de la análoga no se puede alinear, la análoga se descarta. «No
procede» no es una respuesta (no se preguntó) y se excluye.
"""

from __future__ import annotations

import re
import unicodedata

NS = "NS"
NC = "NC"
NO_PROCEDE = {"no procede", "no procede.", "n.p.", "np"}
_NS = {
    "n.s.",
    "ns",
    "no sabe",
    "n.s./no recuerda",
    "no recuerda",
    "n.r.",
    "no sabe, duda",
    "no sabe/duda",
    "no sabe todavia",
    "no lo sabe",
}
_NC = {"n.c.", "nc", "no contesta", "no contesta/no sabe"}


def normalizar(etiqueta: str) -> str:
    t = unicodedata.normalize("NFKD", etiqueta).encode("ascii", "ignore").decode()
    t = re.sub(r"\(\s*no leer\s*\)", "", t, flags=re.I)
    t = t.lower().strip().strip("'\"").strip()
    return re.sub(r"\s+", " ", t)


def tipo(etiqueta: str) -> str | None:
    """NS, NC, "NP" (no procede) o None (respuesta sustantiva)."""
    n = normalizar(etiqueta)
    if n in _NS:
        return NS
    if n in _NC:
        return NC
    if n in NO_PROCEDE:
        return "NP"
    return None


def numero(etiqueta: str) -> int | None:
    """El número con que empieza una etiqueta de escala numérica («1 Izquierda», «7»)."""
    m = re.match(r"^(\d{1,2})(\s|$)", normalizar(etiqueta))
    return int(m.group(1)) if m else None


def sustantivas(opciones: list[str]) -> list[str]:
    return [o for o in opciones if tipo(o) is None]


def es_numerica(opciones: list[str]) -> bool:
    s = sustantivas(opciones)
    nums = [numero(o) for o in s]
    return len(s) >= 5 and all(n is not None for n in nums)


def alinear(origen: list[str], destino: list[str], ordinal: bool) -> dict[str, str] | None:
    """Correspondencia etiqueta de `origen` (análoga, en su orden) → etiqueta de `destino`
    (pregunta nueva, en su orden), o None si no se puede alinear sin inventar."""
    dest_norm = {normalizar(d): d for d in destino}
    dest_ns = next((d for d in destino if tipo(d) == NS), None)
    dest_nc = next((d for d in destino if tipo(d) == NC), None)
    so, sd = sustantivas(origen), sustantivas(destino)
    m: dict[str, str] = {}
    for o in origen:
        t = tipo(o)
        if t == NS and dest_ns:
            m[o] = dest_ns
        elif t == NC and dest_nc:
            m[o] = dest_nc
        elif t is None and normalizar(o) in dest_norm:
            m[o] = dest_norm[normalizar(o)]
    if all(o in m for o in so):
        return m
    if es_numerica(so) and es_numerica(sd):
        a = [numero(o) for o in so]
        b = [numero(d) for d in sd]
        lo_a, hi_a, lo_b, hi_b = min(a), max(a), min(b), max(b)
        por_num = {n: d for n, d in zip(b, sd, strict=True)}
        for o, n in zip(so, a, strict=True):
            r = (n - lo_a) / (hi_a - lo_a)
            objetivo = round(lo_b + r * (hi_b - lo_b))
            cerca = min(por_num, key=lambda x: abs(x - objetivo))
            m[o] = por_num[cerca]
        return m
    if ordinal and len(so) == len(sd):
        for o, d in zip(so, sd, strict=True):
            m.setdefault(o, d)
        return m
    return None


_ORDINALES = re.compile(
    r"\b(muy|bastante|poco|nada|mucho|mucha|algo|regular|siempre|nunca|a veces|"
    r"frecuencia|acuerdo|desacuerdo|mejor|peor|igual|mas|menos|totalmente|"
    r"satisfech|probable|seguro|buena|mala|bueno|malo|alto|alta|bajo|baja)\b"
)


def escala_probable(opciones: list[str]) -> str:
    """«ordinal» si las opciones sustantivas son una escala numérica o graduada (muy/bastante/
    poco/nada, acuerdo/desacuerdo, frecuencia, mejor/peor…); si no, «nominal»."""
    s = sustantivas(opciones)
    if es_numerica(s):
        return "ordinal"
    con = sum(bool(_ORDINALES.search(normalizar(o))) for o in s)
    return "ordinal" if len(s) >= 3 and con >= len(s) - 1 else "nominal"
