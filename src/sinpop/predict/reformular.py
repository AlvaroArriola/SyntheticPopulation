"""Reformulaciones neutras para la prueba V-REFORMULACION (F9, G9.4) (D-069).

Reglas fijas, sin modelo de lenguaje, que cambian la redacción sin cambiar el sentido ni añadir
carga: sinónimos de las fórmulas del CIS («Grado de» → «Nivel de», «persona entrevistada» →
«persona encuestada»…), paso a pregunta directa con signos de interrogación y cambio de
mayúsculas. Las opciones no se tocan (la prueba es sobre el enunciado).
"""

from __future__ import annotations

import re

SINONIMOS = [
    (r"\bGrado de\b", "Nivel de"),
    (r"\bgrado de\b", "nivel de"),
    (r"\bValoración de\b", "Evaluación de"),
    (r"\bvaloración de\b", "evaluación de"),
    (r"\bpersona entrevistada\b", "persona encuestada"),
    (r"\bOpinión sobre\b", "Parecer sobre"),
    (r"\bopinión sobre\b", "parecer sobre"),
    (r"\bFrecuencia con la que\b", "Con qué frecuencia"),
    (r"\bFrecuencia de\b", "Con qué frecuencia se da"),
    (r"\bPreferencia\b", "Opción preferida"),
    (r"\bAcuerdo con\b", "Grado de acuerdo con"),
    (r"\bConfianza en\b", "Nivel de confianza en"),
]


def reformular(enunciado: str) -> str:
    t = enunciado.strip()
    for patron, sustituto in SINONIMOS:
        t = re.sub(patron, sustituto, t)
    t = t.rstrip(".?¿")
    if not t.startswith("¿"):
        t = "¿" + t[0].lower() + t[1:] + "?"
    return t
