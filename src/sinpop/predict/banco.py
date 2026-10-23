"""Banco histórico de preguntas cerradas del CIS (F9, tarea 1) (D-069).

Cada entrada es una pregunta de un estudio nacional del CIS anterior al corte (los de
`temporal.indicadores.estudios_temporales`: estudios nacionales y barómetros), con su enunciado
(la etiqueta de la variable en el fichero), sus opciones en el orden de sus códigos y la fecha
del estudio. Se excluyen las variables de perfil, de control de campo y de recodificación del
CIS, y las preguntas con una sola opción sustantiva o con más de `MAX_OPCIONES`.

Las respuestas de los encuestados (para los modelos) se leen bajo demanda, con las mismas reglas
que F8A: etiqueta del fichero; los puntos intermedios sin etiqueta de una escala numérica toman
su número; «No procede» se excluye.
"""

from __future__ import annotations

import json
import re
from functools import cache

import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion.cis import fechas
from sinpop.opinion.latentes import _intermedios_numericos
from sinpop.predict import opciones as O

MAX_OPCIONES = 30
EXCLUIDAS = re.compile(
    r"^(IA_|PESO|ESTU|CUES|ENTREV|TIPO_TEL|SINCERIDAD|SEXO|EDAD|ESCUELA|ESTUDIOS|NIVELEST|"
    r"CNO|SITLAB|RELALAB|ECIVIL|CAPITAL|P0$|NACIONALIDAD|PAISNAC|PAIS_NAC|LUGAR|PROV|F_|M_|"
    r"CCAA|MUN|TAMUNI|ADQUINAC|EMPADRONA|INGRESHOG|CLASESUB|CLASESOCIAL|RELIGION|ESCIDEOL$|"
    r"PRACTICARELIG|IDIOMA|REGISTRO|NUM_|TELEF|DIA|HORA|FECHA)"
    r"|(_COD$|R$|R2$|GR$|GRA$)"
)

# variables que la regla de recodificación («…R$») excluiría por error: no son recodificaciones
# de otra variable del fichero (no existe su versión sin la R final) (D-082)
INCLUIDAS = {"ECOPER"}


def _opciones(js: str) -> list[str]:
    """Opciones de una pregunta en orden de código, sin «No procede».

    Escalas numéricas con solo los extremos etiquetados («1 Muy mal» … «10 Muy bien»): se añaden
    los valores intermedios como su número («2» … «9»), con la misma regla que
    `opinion.latentes._intermedios_numericos` aplica a las respuestas: solo los enteros entre los
    dos extremos etiquetados con su número. Así la pregunta tiene las mismas opciones que cuando
    el diseño de registro las etiqueta todas (D-089); nunca se inventa un código fuera de ella."""
    d = json.loads(js)
    pares = sorted(((float(k), v.strip()) for k, v in d.items()), key=lambda x: x[0])
    numericos = [
        c for c, v in pares if ESCALA.match(v) and c == int(c) and v.split()[0] == str(int(c))
    ]
    if len(numericos) >= 2:
        lo, hi = min(numericos), max(numericos)
        hay = {c for c, _ in pares}
        pares += [(float(c), str(c)) for c in range(int(lo) + 1, int(hi)) if float(c) not in hay]
        pares.sort(key=lambda x: x[0])
    return [v for _, v in pares if O.tipo(v) != "NP"]


ESCALA = re.compile(r"^\d{1,2}(\s|$)")  # etiqueta que empieza por su número («10 Muy bien»)


@cache
def preguntas() -> pl.DataFrame:
    """id, estudio, variable, fecha, enunciado, opciones (lista, en orden de código)."""
    from sinpop import paquete as PK

    if PK.activo():  # paquete portable (D-076): el banco ya filtrado
        return pl.read_parquet(PK.ruta("banco.parquet"))
    from sinpop.temporal.indicadores import estudios_temporales

    nac = set(estudios_temporales())
    f = fechas()
    b = pl.read_parquet(INTERIM_DIR / "cis_preguntas.parquet").explode("estudios")
    filas = []
    for var, enun, ops, est in b.select(
        "variable", "enunciado", "opciones", "estudios"
    ).iter_rows():
        if est not in nac or est not in f or (EXCLUIDAS.search(var) and var not in INCLUIDAS):
            continue
        op = _opciones(ops)
        k = len(O.sustantivas(op))
        if k < 2 or k > MAX_OPCIONES or not (enun or "").strip():
            continue
        filas.append(
            {
                "id": f"CIS-{est}-{var}",
                "estudio": est,
                "variable": var,
                "fecha": f[est],
                "enunciado": enun.strip(),
                "opciones": op,
            }
        )
    return pl.DataFrame(filas).unique("id").sort("id")


def respuestas(estudio: str, variable: str) -> pl.DataFrame:
    """(estudio, encuestado, etiqueta) de una pregunta, sin «No procede» ni vacíos."""
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter((pl.col("estudio") == estudio) & (pl.col("variable") == variable))
        .select("estudio", "encuestado", "variable", "codigo", "etiqueta")
        .collect()
    )
    lg = _intermedios_numericos(lg, {variable: "numerica"})
    return (
        lg.filter(pl.col("etiqueta").is_not_null())
        .with_columns(pl.col("etiqueta").str.strip_chars())
        .filter(
            pl.col("etiqueta").map_elements(lambda e: O.tipo(e) != "NP", return_dtype=pl.Boolean)
        )
        .select("estudio", "encuestado", "etiqueta")
    )
