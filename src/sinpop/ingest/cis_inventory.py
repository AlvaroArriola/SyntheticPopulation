"""Inventario de variables políticas y de valores de un estudio del CIS (verificación 7 de F1).

Lee el fichero SPSS del estudio (etiquetas de variables y de valores) y registra, para
cada variable de interés del diccionario, el nombre original, su número de códigos y los
códigos especiales (NS, NC, no recuerda, no procede, en blanco), que varían por variable.
"""

from __future__ import annotations

import re
from pathlib import Path

import pyreadstat

# Variable armonizada -> patrón sobre la etiqueta de la variable del CIS
OBJETIVOS: dict[str, str] = {
    "recuerdo_voto_generales": r"^recuerdo de voto en las elecciones generales",
    "participacion_generales": r"participaci.n.*(recuerdo|elecciones generales)|^votó en",
    "intencion_voto": r"^intenci.n de voto en (unas )?supuestas elecciones generales$",
    "cercania_partido": r"partido pol.tico que considera m.s cercano",
    "simpatia_partido": r"simpat.a",
    "ideologia_autoubicacion": r"escala de autoubicaci.n ideol.gica",
    "religiosidad": r"^religiosidad",
    "clase_subjetiva": r"clase social subjetiva",
    "interes_politica": r"inter.s por la pol.tica",
    "identidad_territorial": r"sentimiento.*(nacional|auton)|identificaci.n.*(espa|comunidad)",
    "lengua_habitual": r"lengua",
    "confianza_instituciones": r"confianza en",
    "situacion_economica_personal": r"situaci.n econ.mica personal",
    "medio_informacion_principal": r"medio.*informa",
    "peso": r"^ponderaci.n",
    "ccaa": r"^comunidad aut.noma$",
    "provincia": r"^provincia$",
    "tamano_municipio": r"^tama.o de (municipio|h.bitat)",
    "sexo": r"^sexo de la persona entrevistada",
    "edad": r"^edad de la persona entrevistada",
    "estudios": r"^estudios de la persona entrevistada|nivel de estudios alcanzado",
    "situacion_laboral": r"^situaci.n laboral",
    "nacionalidad": r"^nacionalidad de la persona entrevistada",
}
_ESPECIAL = re.compile(
    r"^(N\.?S\.?|N\.?C\.?|N\.?R\.?|No sabe|No contesta|No recuerda|No procede|En blanco|"
    r"No sabe todav.a|Nulo|No vot)",
    re.I,
)


def inventariar(sav: Path) -> list[dict]:
    _, meta = pyreadstat.read_sav(str(sav), metadataonly=True)
    filas = []
    for var, etiqueta in zip(meta.column_names, meta.column_labels, strict=True):
        etiqueta = etiqueta or ""
        for armonizada, patron in OBJETIVOS.items():
            if re.search(patron, etiqueta, re.I):
                vl = meta.variable_value_labels.get(var, {})
                especiales = {
                    str(int(k)) if float(k).is_integer() else str(k): v
                    for k, v in vl.items()
                    if _ESPECIAL.search(str(v))
                }
                filas.append(
                    {
                        "armonizada": armonizada,
                        "variable": var,
                        "etiqueta": etiqueta,
                        "n_codigos": len(vl),
                        "especiales": especiales,
                    }
                )
    return filas


def informe(estudios: dict[str, Path], destino: Path) -> None:
    lines = [
        "# Variables políticas y de valores en los estudios del CIS (F1, verificación 7)",
        "",
        "Generado desde las etiquetas de los ficheros SPSS oficiales. Los códigos especiales",
        "cambian de una variable a otra: se recodifican uno a uno en F2, nunca como valores de",
        "escala (regla 2 de CLAUDE.md).",
        "",
    ]
    for estudio, sav in estudios.items():
        lines += [
            f"## Estudio {estudio}",
            "",
            "| Variable armonizada | Variable CIS | Etiqueta | Códigos | Códigos especiales |",
            "| --- | --- | --- | ---: | --- |",
        ]
        for f in inventariar(sav):
            esp = "; ".join(f"{k} = {v}" for k, v in f["especiales"].items()) or "—"
            lines.append(
                f"| `{f['armonizada']}` | `{f['variable']}` | {f['etiqueta'][:70]} | "
                f"{f['n_codigos']} | {esp} |"
            )
        lines.append("")
    destino.write_text("\n".join(lines), encoding="utf-8")
