"""Estimadores sin modelo de lenguaje (F9, tareas 3, 5 y 7) (D-069).

Para una pregunta nueva (enunciado, opciones, escala, fecha de referencia):

1. **Análogas:** las preguntas del banco más parecidas (`recuperar`) cuyas respuestas se pueden
   alinear con las opciones nuevas (`opciones.alinear`). Se ordenan por peso
   w = similitud² · 0,5^(meses de antigüedad / 12) y se usan las `K` primeras, siempre que su
   similitud sea al menos `UMBRAL_RELATIVO` de la mejor.
2. **Sistema (estimador estadístico):** para cada análoga, una regresión multinomial ponderada de
   sus respuestas (llevadas a las opciones nuevas) con el perfil y los valores (religiosidad,
   clase subjetiva) de los encuestados, aplicada al marco de población sintética
   (`poblacion.marco`). El desglose por recuerdo de voto usa además el grupo de voto y la
   autoubicación. Las análogas se combinan con sus pesos.
3. **B0:** la distribución observada (ponderada) de las análogas, combinada con los mismos pesos.
4. **B1:** como el sistema, pero solo con el perfil demográfico (sexo, edad, estudios,
   actividad, comunidad, tamaño de municipio, comunidad × edad): el modelo clásico entrenado en
   el CIS y posestratificado a la población, sin las capas de opinión y política.
5. **Incertidumbre:** el desacuerdo entre análogas (desviación ponderada) más un término de
   escala c·p(1 − p); el intervalo es p ± q · σ, con q calibrado (conformal) en un *backtest*
   sobre los últimos barómetros anteriores al corte (`calibracion`).
"""

from __future__ import annotations

import datetime as dt
import json
from dataclasses import dataclass, field
from functools import cache

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR, PROCESSED_DIR
from sinpop import paquete as PK
from sinpop.opinion.valores import COLUMNAS, Modelo, _edad_grupo
from sinpop.politics import ideologia as ID
from sinpop.politics import recuerdo as RV
from sinpop.politics.rasgos_politicos import bloque_cis
from sinpop.predict import banco as B
from sinpop.predict import opciones as O
from sinpop.predict import poblacion as P
from sinpop.predict import recuperar as R
from sinpop.temporal.indicadores import DESCONOCIDO, _edad4, grupo_voto

K = 5
CANDIDATAS = 40
UMBRAL_RELATIVO = 0.6
SIMILITUD_MIN = 0.15
C_MODELO = 0.1
C_ESCALA = 0.0025
S_MIN = 0.01  # suelo de σ: sin él, una opción con p ≈ 0 en todas las análogas da cuantiles absurdos
# El voto y la ideología empeoran la predicción fuera de la muestra (backtest, D-069): los
# coeficientes se estiman con el voto **recordado** de los encuestados (sesgado hacia el PSOE y
# con menos abstención) y se aplicarían al voto **real** calibrado de la población. Solo se usan
# para el desglose por recuerdo de voto, que sin ellos no tendría diferencias entre electorados.
COLUMNAS_SISTEMA = COLUMNAS + ["religiosidad", "clase_subjetiva"]
COLUMNAS_VOTO = COLUMNAS_SISTEMA + ["grupo_voto", "ideologia_bloque"]
SUBGRUPO_VOTO = "recuerdo_voto_generales_familia"
# desgloses que necesitan el modelo con voto e ideología: sin ellos los grupos no se distinguen
SUBGRUPOS_VOTO = (SUBGRUPO_VOTO, "ideologia_bloque")
COLUMNAS_B1 = COLUMNAS
SUBGRUPOS = ["edad_4", "sexo", "estudios_3", "ccaa", "recuerdo_voto_generales_familia"]
# desgloses que ofrece la interfaz (D-081); la evaluación (F9-F11) sigue con SUBGRUPOS
SUBGRUPOS_AMPLIADOS = [
    "edad_4",
    "sexo",
    "estudios_3",
    "actividad_3",
    "tamano_municipio_cis",
    "ccaa",
    "provincia",
    "ideologia_bloque",
    "recuerdo_voto_generales_familia",
    "religiosidad",
    "clase_subjetiva",
]
CALIBRACION = (
    PK.ruta("calibracion.json") if PK.activo() else PROCESSED_DIR / "predict" / "calibracion.json"
)


@dataclass
class Pregunta:
    id: str
    enunciado: str
    opciones: list[str]
    escala: str = "nominal"  # nominal | ordinal
    fecha_referencia: str = "2026-07"
    subgrupos: list[str] = field(default_factory=lambda: list(SUBGRUPOS))


def _meses(a: str, b: str) -> float:
    ya, ma = int(a[:4]), int(a[5:7])
    yb, mb = int(b[:4]), int(b[5:7])
    return abs((yb - ya) * 12 + (mb - ma))


def analogas(q: Pregunta, excluir: pl.Expr | None = None) -> list[dict]:
    """Análogas alineables, con su correspondencia de opciones y su peso."""
    cand = R.indice().similares(q.enunciado, q.opciones, CANDIDATAS, excluir)
    if cand.is_empty():
        return []
    mejor = cand["similitud"][0]
    out = []
    for row in cand.iter_rows(named=True):
        if row["similitud"] < max(SIMILITUD_MIN, UMBRAL_RELATIVO * mejor):
            continue
        m = O.alinear(row["opciones"], q.opciones, q.escala == "ordinal")
        if m is None:
            continue
        w = row["similitud"] ** 2 * 0.5 ** (_meses(row["fecha"], q.fecha_referencia) / 12)
        out.append({**row, "mapeo": m, "peso_analoga": w})
    out.sort(key=lambda r: (-r["peso_analoga"], r["id"]))
    return out[:K]


@cache
def _personas() -> pl.DataFrame:
    return pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")


@cache
def _recuerdo() -> pl.DataFrame:
    return RV.respuestas().select("estudio", "encuestado", "recuerdo")


@cache
def _ideologia() -> pl.DataFrame:
    return ID.respuestas().select("estudio", "encuestado", "ideologia")


def encuestados(estudio: str, variable: str, mapeo: dict[str, str]) -> pl.DataFrame:
    """Encuestados de una análoga (españoles de 18+, el universo del CIS) con su respuesta
    llevada a las opciones nuevas y los predictores."""
    r = B.respuestas(estudio, variable).filter(pl.col("etiqueta").is_in(list(mapeo)))
    p = _personas().filter(pl.col("estudio") == estudio)
    rv = _recuerdo().filter(pl.col("estudio") == estudio).drop("estudio")
    ide = _ideologia().filter(pl.col("estudio") == estudio).drop("estudio")
    d = (
        p.join(r.drop("estudio"), on="encuestado")
        .join(rv, on="encuestado", how="left")
        .join(ide, on="encuestado", how="left")
        .filter(
            (pl.col("edad") >= 18)
            & (
                pl.col("nacionalidad_esp_ext").is_null()
                | (pl.col("nacionalidad_esp_ext") == "espanola")
            )
        )
        .with_columns(
            pl.col("etiqueta").replace_strict(mapeo).alias("valor"),
            _edad_grupo(pl.col("edad")),
            _edad4(pl.col("edad")),
            pl.when(pl.col("recuerdo").is_null())
            .then(pl.lit(DESCONOCIDO))
            .otherwise(grupo_voto(pl.col("recuerdo")))
            .alias("grupo_voto"),
            pl.when(pl.col("ideologia").is_null())
            .then(pl.lit(None, pl.Utf8))
            .otherwise(bloque_cis(pl.col("ideologia")))
            .alias("ideologia_bloque"),
            (pl.col("peso") / pl.col("peso").mean()).alias("peso"),
        )
        .sort("encuestado")
    )
    return d


def _disponibles(d: pl.DataFrame, columnas: list[str]) -> list[str]:
    out = []
    for c in columnas:
        if c not in d.columns and c != "ccaa_edad4":
            continue
        if c == "grupo_voto" and (d["grupo_voto"] == DESCONOCIDO).all():
            continue
        if c in d.columns and d[c].null_count() == d.height:
            continue
        out.append(c)
    return out


def _modelo(d: pl.DataFrame, columnas: list[str], opciones: list[str], marco: pl.DataFrame):
    """Probabilidades sobre las opciones nuevas para cada persona del marco."""
    pr = np.zeros((marco.height, len(opciones)))
    clases = sorted(d["valor"].unique().to_list())
    if len(clases) == 1:
        pr[:, opciones.index(clases[0])] = 1.0
        return pr
    m = Modelo("valor", c=C_MODELO, columnas=_disponibles(d, columnas)).ajustar(d)
    p = m.probabilidades(marco)
    for j, c in enumerate(m.clases):
        pr[:, opciones.index(c)] = p[:, j]
    return pr


def _observada(d: pl.DataFrame, opciones: list[str]) -> np.ndarray:
    w = d.group_by("valor").agg(pl.col("peso").sum())
    dd = dict(w.iter_rows())
    v = np.array([dd.get(o, 0.0) for o in opciones])
    return v / v.sum()


def _agregar(pr: np.ndarray, marco: pl.DataFrame, subgrupos: list[str], peso: str = "peso") -> dict:
    w = marco[peso].to_numpy()
    out = {"total": (pr * w[:, None]).sum(0) / w.sum()}
    for g in subgrupos:
        col = marco[g].cast(pl.Utf8).to_numpy()
        for lv in sorted({x for x in col if x is not None}):
            s = col == lv
            if w[s].sum() > 0:
                out[f"{g}={lv}"] = (pr[s] * w[s, None]).sum(0) / w[s].sum()
    return out


def _combinar(por_analoga: list[dict], pesos: np.ndarray) -> tuple[dict, dict]:
    """Media y desviación ponderadas entre análogas para cada clave (total y subgrupos)."""
    pesos = pesos / pesos.sum()
    media, desv = {}, {}
    for k in por_analoga[0]:
        x = np.array([a[k] for a in por_analoga])
        mu = (x * pesos[:, None]).sum(0)
        media[k] = mu
        desv[k] = np.sqrt((((x - mu) ** 2) * pesos[:, None]).sum(0))
    return media, desv


def calibracion() -> dict:
    if CALIBRACION.exists():
        return json.loads(CALIBRACION.read_text("utf-8"))
    return {"q80": 1.2816, "q95": 1.96, "c_escala": C_ESCALA, "calibrada": False}


TRAMOS_SIMILITUD = [0.0, 0.4, 0.7, 1.01]


def tramo(similitud: float) -> str:
    for a, b in zip(TRAMOS_SIMILITUD[:-1], TRAMOS_SIMILITUD[1:], strict=True):
        if a <= similitud < b:
            return f"{a:.1f}-{min(b, 1.0):.1f}"
    return f"{TRAMOS_SIMILITUD[-2]:.1f}-1.0"


def intervalos(
    mu: np.ndarray, sd: np.ndarray, cal: dict, similitud: float | None = None
) -> tuple[np.ndarray, np.ndarray]:
    """p ± q·σ; q es el cuantil conformal del tramo de similitud de la mejor análoga (cuanto
    menos se parece la pregunta al banco, más ancho), o el global si el tramo no se calibró."""
    q = cal
    if similitud is not None and tramo(similitud) in cal.get("por_tramo", {}):
        q = cal["por_tramo"][tramo(similitud)]
    s = np.maximum(np.sqrt(sd**2 + cal["c_escala"] * np.clip(mu * (1 - mu), 0, None)), S_MIN)
    i80 = np.column_stack([np.clip(mu - q["q80"] * s, 0, 1), np.clip(mu + q["q80"] * s, 0, 1)])
    i95 = np.column_stack([np.clip(mu - q["q95"] * s, 0, 1), np.clip(mu + q["q95"] * s, 0, 1)])
    return i80, i95


@dataclass
class Resultado:
    pregunta: Pregunta
    analogas: list[dict]
    sistema: dict  # clave → probabilidades (población: todos los adultos)
    sistema_sd: dict
    b0: np.ndarray | None
    b1: dict  # posestratificado a los españoles (universo del CIS)
    segundos: float
    sistema_cis: dict = field(default_factory=dict)  # como lo mediría el CIS
    sistema_cis_sd: dict = field(default_factory=dict)


def _por_analoga(a: dict, q: Pregunta, marco: pl.DataFrame):
    """Modelos de una análoga ajustados con sus encuestados (microdatos del CIS)."""
    d = encuestados(a["estudio"], a["variable"], a["mapeo"])
    if d.height < 50:
        return None
    pr = _modelo(d, COLUMNAS_SISTEMA, q.opciones, marco)
    con_voto = any(g in q.subgrupos for g in SUBGRUPOS_VOTO)
    prv = _modelo(d, COLUMNAS_VOTO, q.opciones, marco) if con_voto else None
    pr_b1 = _modelo(d, COLUMNAS_B1, q.opciones, marco)
    n_sub = {
        f"{g}={lv}": n
        for g in q.subgrupos
        if g in d.columns
        for lv, n in d.group_by(g).len().iter_rows()
    }
    return pr, prv, pr_b1, _observada(d, q.opciones), d.height, n_sub


def _por_analoga_paquete(a: dict, q: Pregunta, marco: pl.DataFrame):
    """Lo mismo con los modelos ya ajustados del paquete portable (D-076): se ajustaron sobre las
    opciones propias de la análoga y aquí se llevan a las de la pregunta sumando las que la
    alineación funde (`a["mapeo"]`); las opciones que la alineación deja fuera se descartan y se
    renormaliza, como hace el filtro de encuestados del modo completo."""
    x = PK.modelos().get(a["id"])
    if x is None:
        return None
    m = a["mapeo"]
    n = sum(x["n_opcion"].get(o, 0) for o in m)
    if n < 50:
        return None

    def llevar(p: np.ndarray, clases: list[str]) -> np.ndarray:
        out = np.zeros((p.shape[0], len(q.opciones)))
        for j, c in enumerate(clases):
            if c in m:
                out[:, q.opciones.index(m[c])] += p[:, j]
        s = out.sum(1, keepdims=True)
        return out / np.where(s > 0, s, 1)

    def pr(clave: str) -> np.ndarray:
        return llevar(*PK.probabilidades(x["modelos"][clave], marco))

    propias = list(x["n_opcion"])
    obs = llevar(np.array([x["b0"]]), propias)[0]
    frac = n / x["n"]
    dims = set(q.subgrupos)
    n_sub = {k: v * frac for k, v in x["n_sub"].items() if k.split("=")[0] in dims}
    prv = pr("voto") if any(g in q.subgrupos for g in SUBGRUPOS_VOTO) else None
    return pr("sistema"), prv, pr("b1"), obs, n, n_sub


def predecir(q: Pregunta, excluir: pl.Expr | None = None, run_id: str = P.NACIONAL) -> Resultado:
    t0 = dt.datetime.now()
    an = analogas(q, excluir)
    marco = P.marco(run_id)
    if not an:
        return Resultado(q, [], {}, {}, None, {}, 0.0)
    sis, sis_cis, b1, b0 = [], [], [], []
    por_analoga = _por_analoga_paquete if PK.activo() else _por_analoga
    for a in an:
        x = por_analoga(a, q, marco)
        if x is None:
            a["peso_analoga"] = 0.0
            sis.append(None)
            sis_cis.append(None)
            continue
        pr, prv, pr_b1, obs, n, n_sub = x
        otros = [g for g in q.subgrupos if g not in SUBGRUPOS_VOTO]
        de_voto = [g for g in q.subgrupos if g in SUBGRUPOS_VOTO]
        a_pob = _agregar(pr, marco, otros)
        a_cis = _agregar(pr, marco, otros, "peso_cis")
        if prv is not None:
            for k, v in _agregar(prv, marco, de_voto).items():
                if k != "total":
                    a_pob[k] = v
            for k, v in _agregar(prv, marco, de_voto, "peso_cis").items():
                if k != "total":
                    a_cis[k] = v
        sis.append(a_pob)
        sis_cis.append(a_cis)
        b1.append(_agregar(pr_b1, marco, q.subgrupos, "peso_es"))
        b0.append(obs)
        a["encuestados"] = n
        a["n_sub"] = n_sub
    validas = [i for i, s in enumerate(sis) if s is not None]
    an = [an[i] for i in validas]
    if not an:
        return Resultado(q, [], {}, {}, None, {}, 0.0)
    pesos = np.array([a["peso_analoga"] for a in an])
    sistema, sd = _combinar([sis[i] for i in validas], pesos)
    scis, sdcis = _combinar([sis_cis[i] for i in validas], pesos)
    b1c, _ = _combinar(b1, pesos)
    b0c = (np.array(b0) * (pesos / pesos.sum())[:, None]).sum(0)
    # combinación de estimadores para la medición del CIS (pesos aprendidos en el backtest de
    # construcción, `calibracion.combinar`)
    w = calibracion().get("combinacion")
    if w:
        scis = dict(scis)
        scis["total"] = w["sistema_cis"] * scis["total"] + w["b0"] * b0c + w["b1"] * b1c["total"]
    seg = (dt.datetime.now() - t0).total_seconds()
    return Resultado(q, an, sistema, sd, b0c, b1c, seg, scis, sdcis)
