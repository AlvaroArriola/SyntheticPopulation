"""Recuerdo de voto en las últimas autonómicas de cada comunidad (F8B, tarea 4) (D-067).

La elección es la última de cada comunidad hasta junio de 2026 (`configs/elecciones.yaml`). El
voto autonómico se asigna **condicionado al de generales** ya calibrado (voto dual), con un
modelo multinomial ponderado del voto autonómico según el de generales y el perfil, ajustado con
el postelectoral autonómico del CIS de esa comunidad:

| Comunidad | Elección | Estudio | Autonómicas | Generales |
| --- | --- | --- | --- | --- |
| Andalucía | 17/05/2026 | 3566 | RVAUTO26 | RECUERDO (2023) |
| Aragón | 08/02/2026 | 3548 | RVAUTO26 | RECUERDO (2023) |
| Castilla y León | 15/03/2026 | 3550 | RVAUTO26 | RECUERDO (2023) |
| Extremadura | 21/12/2025 | 3541 | RVAUTO25 | RECUERDO (2023) |
| Galicia | 18/02/2024 | 3446 | RVAUTO | RECUERDO (2023) |
| País Vasco | 21/04/2024 | 3459 | RVAUTO | RECUERDO (2023) |
| Cataluña | 12/05/2024 | 3464 | RVAUTO | RECUERDO (2023) |
| Doce comunidades, Ceuta y Melilla | 28/05/2023 | 3410 | RECUVOTOA/RECUERDOA | INTENCIONG |

En las comunidades del 28/05/2023 no hay estudio con el recuerdo de esas autonómicas y el de las
generales de 2023 (el 3410 es de junio de 2023): se usa la intención de voto en las generales de
julio como aproximación, en un modelo conjunto con la comunidad como predictor.

Después se calibra en el espacio logit, como el de generales, a los **resultados oficiales de
cada circunscripción** (abstención incluida; en Aragón no se publican los electores y el objetivo
es sobre los votantes, manteniendo la abstención del modelo). Tienen recuerdo quienes tenían
derecho a voto en la fecha de su elección (edad a esa fecha; la residencia y la nacionalidad son
las actuales: limitación documentada). «No recuerda / no contesta» se marca aparte, como en
generales.
"""

from __future__ import annotations

import datetime as dt
from functools import lru_cache

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR, PROCESSED_DIR
from sinpop.config import load_config
from sinpop.opinion.valores import Modelo, _edad_grupo, perfil_sintetico
from sinpop.politics import derecho as DV
from sinpop.politics import recuerdo as RV

OPCIONES = RV.OPCIONES
SIN_DERECHO = ["no_tenia_edad", "sin_derecho_voto"]
POSTELECTORALES = {
    "01": ("3566", "RVAUTO26"),
    "02": ("3548", "RVAUTO26"),
    "07": ("3550", "RVAUTO26"),
    "11": ("3541", "RVAUTO25"),
    "12": ("3446", "RVAUTO"),
    "16": ("3459", "RVAUTO"),
    "09": ("3464", "RVAUTO"),
}
ESTUDIO_2023 = "3410"
COLUMNAS = ["generales", "sexo", "edad_grupo", "estudios_3", "tamano_municipio_cis"]
# generales: el voto de 2023 (o "no_tenia_edad" para quien cumplió 18 años después)
GENERALES = OPCIONES + ["no_tenia_edad"]


@lru_cache(maxsize=1)
def elecciones() -> dict[str, dt.date]:
    """ccaa → fecha de su última elección autonómica."""
    cfg = load_config("elecciones.yaml")
    out = {}
    for e in cfg.elecciones:  # type: ignore[attr-defined]
        if e.tipo == "autonomicas":
            out[e.ambito.replace("CCAA:", "")] = dt.date.fromisoformat(str(e.fecha))
    return out


def _mapa(nombre: str) -> dict[str, str]:
    return getattr(load_config("partidos.yaml"), nombre)


def _etiquetas(filtro: pl.Expr) -> pl.DataFrame:
    return (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter(filtro)
        .select("estudio", "encuestado", "variable", pl.col("etiqueta").str.strip_chars())
        .collect()
    )


def _recodificar(lg: pl.DataFrame, mapa: dict[str, str], que: str) -> pl.DataFrame:
    sin = sorted(set(lg["etiqueta"].drop_nulls().unique()) - set(mapa))
    if sin:
        raise ValueError(f"{que}: etiquetas sin correspondencia en partidos.yaml: {sin}")
    return lg.with_columns(pl.col("etiqueta").replace_strict(mapa, default=None).alias("valor"))


def respuestas() -> pl.DataFrame:
    """(estudio, encuestado, generales, autonomicas) de los postelectorales autonómicos."""
    mapa = _mapa("recuerdo_cis_autonomicas")
    filas = []
    for _, (e, v) in sorted(POSTELECTORALES.items()):
        a = _recodificar(
            _etiquetas((pl.col("estudio") == e) & (pl.col("variable") == v)), mapa, f"{e} {v}"
        )
        filas.append(a.select("estudio", "encuestado", pl.col("valor").alias("autonomicas")))
    reg = pl.concat(filas).join(
        RV.respuestas().rename({"recuerdo": "generales"}), on=["estudio", "encuestado"]
    )
    # 3410: el detalle de partidos (RECUVOTOA, solo votantes) y, si no, la participación + recuerdo
    lg = _etiquetas(
        (pl.col("estudio") == ESTUDIO_2023)
        & pl.col("variable").is_in(["RECUVOTOA", "RECUERDOA", "INTENCIONG"])
    )
    det = _recodificar(lg.filter(pl.col("variable") == "RECUVOTOA"), mapa, "3410 RECUVOTOA")
    gen = _recodificar(lg.filter(pl.col("variable") == "RECUERDOA"), mapa, "3410 RECUERDOA")
    auto = (
        gen.select("encuestado", pl.col("valor").alias("g"))
        .join(det.select("encuestado", pl.col("valor").alias("d")), on="encuestado", how="left")
        .select("encuestado", pl.coalesce("d", "g").alias("autonomicas"))
    )
    intencion = _recodificar(
        lg.filter(pl.col("variable") == "INTENCIONG"),
        _mapa("intencion_cis_generales_2023_3410"),
        "3410 INTENCIONG",
    ).select("encuestado", pl.col("valor").alias("generales"))
    r2023 = auto.join(intencion, on="encuestado").with_columns(
        pl.lit(ESTUDIO_2023).alias("estudio")
    )
    return pl.concat([reg, r2023.select(reg.columns)])


def datos() -> pl.DataFrame:
    """Encuestados con voto autonómico y de generales conocidos (sin NS/NC) y su perfil."""
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    d = p.join(respuestas(), on=["estudio", "encuestado"]).filter(
        (pl.col("edad") >= 18)
        & ~pl.col("estudios_3").is_in(["NC", "NS"])
        & pl.col("autonomicas").is_in(OPCIONES)
        & pl.col("generales").is_in(GENERALES)
    )
    # solo las comunidades cuya elección cubre el estudio
    del_2023 = [c for c, f in elecciones().items() if f == dt.date(2023, 5, 28)]
    propias = pl.lit(False)
    for c, (e, _) in POSTELECTORALES.items():
        propias = propias | ((pl.col("estudio") == e) & (pl.col("ccaa") == c))
    propias = propias | ((pl.col("estudio") == ESTUDIO_2023) & pl.col("ccaa").is_in(del_2023))
    return (
        d.filter(propias)
        .with_columns(
            (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
            _edad_grupo(pl.col("edad")),
        )
        .sort("estudio", "encuestado")
    )


def objetivos() -> pl.DataFrame:
    """Proporciones oficiales por circunscripción provincial (provincia, opcion, p)."""
    filas = []
    for f in sorted((PROCESSED_DIR / "targets").glob("PROV_*.parquet")):
        t = pl.read_parquet(f).filter(pl.col("objetivo") == "voto_autonomicas")
        filas.append(
            t.select(
                pl.col("territorio").str.replace("PROV:", "").alias("provincia"),
                pl.col("clave").str.split("=").list.get(1).alias("opcion"),
                "valor",
            )
        )
    t = pl.concat(filas)
    return t.with_columns((pl.col("valor") / pl.col("valor").sum().over("provincia")).alias("p"))


def _softmax(z: np.ndarray) -> np.ndarray:
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)


def asignar(
    persons: pl.DataFrame, voto: pl.DataFrame, rng: np.random.Generator
) -> tuple[pl.DataFrame, dict]:
    perfil = (
        perfil_sintetico(persons)
        .join(
            voto.select(
                "person_id",
                "recuerdo_voto_generales",
                "recuerdo_voto_generales_ns_nc",
            ),
            on="person_id",
        )
        .join(persons.select("person_id", "provincia", "peso"), on="person_id")
        .with_columns(
            pl.when(pl.col("recuerdo_voto_generales") == "sin_derecho_voto")
            .then(pl.lit("no_tenia_edad"))  # sin uso: los extranjeros no votan en autonómicas
            .otherwise(pl.col("recuerdo_voto_generales"))
            .alias("generales")
        )
    )
    d = datos()
    obj = objetivos()
    fechas = elecciones()
    ccaa = perfil["ccaa"].to_numpy()
    prov = perfil["provincia"].to_numpy()
    w = perfil["peso"].to_numpy()
    # derecho a voto en la fecha de la elección de su comunidad
    eleg = np.zeros(perfil.height, dtype=bool)
    for c, f in sorted(fechas.items()):
        s = np.flatnonzero(ccaa == c)
        if len(s):
            eleg[s] = DV.elegible(perfil[s], f, rng)
    salida = np.full(perfil.height, None, dtype=object)
    info: dict = {"modelos": {}, "circunscripciones": {}}
    grupos = {c: [c] for c in POSTELECTORALES}
    grupos[ESTUDIO_2023] = sorted(c for c in fechas if c not in POSTELECTORALES)
    for clave, comunidades in sorted(grupos.items()):
        entreno = d.filter(pl.col("ccaa").is_in(comunidades))
        cols = COLUMNAS + (["ccaa"] if len(comunidades) > 1 else [])
        m = Modelo("autonomicas", columnas=cols).ajustar(entreno)
        clases = list(m.clases)
        sel_g = np.flatnonzero(np.isin(ccaa, comunidades) & eleg)
        if not len(sel_g):
            continue
        logp = np.log(np.maximum(m.probabilidades(perfil[sel_g]), 1e-12))
        info["modelos"][clave] = {
            "comunidades": comunidades,
            "encuestados": entreno.height,
            "estudios": sorted(entreno["estudio"].unique()),
            "c": m.c_elegido,
            "opciones": clases,
        }
        for p in sorted(set(prov[sel_g])):
            loc = np.flatnonzero(prov[sel_g] == p)
            o = dict(obj.filter(pl.col("provincia") == p).select("opcion", "p").iter_rows())
            if not o:
                raise ValueError(f"autonómicas: sin resultado oficial para la provincia {p}")
            total = np.array([o.get(k, 0.0) for k in clases])
            if "abstencion" not in o:  # Aragón: objetivo sobre votantes
                i = clases.index("abstencion")
                ab = (_softmax(logp[loc])[:, i] * w[sel_g][loc]).sum() / w[sel_g][loc].sum()
                total = total * (1 - ab)
                total[i] = ab
            z = logp[loc] + RV.calibrar(logp[loc], w[sel_g][loc], total)
            q = _softmax(z)
            u = rng.random(len(loc))
            idx = (q.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(clases) - 1)
            salida[sel_g[loc]] = np.array(clases)[idx]
            info["circunscripciones"][p] = {
                "electores_sinteticos": int(len(loc)),
                "abstencion_del_modelo": "abstencion" not in o,
            }
    espanol = (perfil["nacionalidad_esp_ext"] == "espanola").to_numpy()
    sin = RV.pd_null(salida)
    salida = np.where(sin, np.where(espanol, "no_tenia_edad", "sin_derecho_voto"), salida)
    # NS/NC: quien no dice su voto de generales tampoco dice el autonómico; el resto, hasta la
    # proporción de los postelectorales
    todos = (
        pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
        .join(respuestas(), on=["estudio", "encuestado"])
        .filter(pl.col("autonomicas").is_in(OPCIONES + ["NS", "NC"]))
    )
    p_ns = float(
        (todos["autonomicas"].is_in(["NS", "NC"]).cast(pl.Float64) * todos["peso"]).sum()
        / todos["peso"].sum()
    )
    ns_gen = perfil["recuerdo_voto_generales_ns_nc"].to_numpy() & eleg
    base = ns_gen[eleg].mean() if eleg.any() else 0.0
    extra = max(0.0, (p_ns - base) / (1 - base))
    ns_nc = eleg & (ns_gen | (rng.random(perfil.height) < extra))
    out = perfil.select("person_id").with_columns(
        pl.Series("derecho_voto_autonomicas_ultima", eleg),
        pl.Series("recuerdo_voto_autonomicas", salida, dtype=pl.Utf8),
        pl.Series("recuerdo_voto_autonomicas_ns_nc", ns_nc),
    )
    info["ns_nc_postelectorales"] = p_ns
    info["elecciones"] = {c: f.isoformat() for c, f in sorted(fechas.items())}
    return out, info
