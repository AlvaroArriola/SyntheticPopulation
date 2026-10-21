"""Recuerdo de voto de las generales de 2023 (F8B, tareas 2 y 3; `03_arquitectura.md` §2.5).

1. **Datos:** todos los estudios del CIS posteriores al 23J (octubre de 2023 – junio de 2026)
   con la pregunta de participación y recuerdo (`RECUERDO`, o su versión de los votantes con
   `PARTICIPACIONG`), recodificada por la **etiqueta** con `partidos.yaml`
   (`recuerdo_cis_generales_2023`, D-067). Se usan los encuestados con derecho a voto en 2023
   que dan una opción (familia, blanco, nulo o abstención).
2. **Modelo:** multinomial ponderado con el perfil, la comunidad × edad, la religiosidad y la
   clase subjetiva (valores de F8A), regularizado por validación cruzada (D-064).
3. **Calibración:** sobre las probabilidades y en escala logit (desplazamientos por iteración
   proporcional), hasta reproducir el resultado oficial de los residentes de cada provincia con
   abstención (`targets/PROV_*.parquet`, `voto_generales_2023`). Dentro de la provincia, la forma
   por tamaño de municipio (el CIS no capta que en los pueblos se vota más) se toma de una
   **mitad** de los municipios, elegida por hash del código; la otra mitad queda reservada para
   validar (D-067, que sustituye la reserva completa del detalle municipal de D-022/F3).
   Después se sortea una opción por persona con la semilla.
4. **NS/NC:** el CIS registra un 3-5 % de «no recuerda» o «no contesta». Se modela aparte su
   propensión con el perfil (`recuerdo_voto_generales_ns_nc`): es lo que la persona respondería
   si se le preguntara, sin alterar su comportamiento calibrado (regla 10 de CLAUDE.md).

La mitad de validación del detalle municipal no se usa en nada de esto.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR, PROCESSED_DIR
from sinpop.config import load_config
from sinpop.opinion.cis import fechas
from sinpop.opinion.valores import COLUMNAS, Modelo, _edad_grupo, perfil_sintetico

ELECCION = dt.date(2023, 7, 23)
CORTE = dt.date(2026, 7, 1)
OPCIONES = [
    "izquierda_estatal",
    "socialdemocrata",
    "centro_derecha_estatal",
    "derecha_radical",
    "nacionalista_regionalista",
    "otros",
    "blanco",
    "nulo",
    "abstencion",
]
COLUMNAS_VOTO = COLUMNAS + ["religiosidad", "clase_subjetiva"]


def mapa() -> dict[str, str]:
    return load_config("partidos.yaml").recuerdo_cis_generales_2023  # type: ignore[attr-defined]


def respuestas() -> pl.DataFrame:
    """(estudio, encuestado, recuerdo) de los estudios posteriores al 23J. La variable es
    `RECUERDO` o, en el postelectoral 3420 (que pregunta también por 2019), `RECUERDO1`: la que
    el banco de preguntas enuncia como recuerdo de las generales de 2023."""
    banco = pl.read_parquet(INTERIM_DIR / "cis_preguntas.parquet")
    q = banco.filter(
        pl.col("variable").is_in(["RECUERDO", "RECUERDO1"])
        & pl.col("enunciado").str.contains("generales de 2023")
        & ~pl.col("enunciado").str.contains("de los votantes")
    ).explode("estudios")
    f = fechas()
    pares = [
        (e, v)
        for e, v in q.select("estudios", "variable").unique().iter_rows()
        if e in f and ELECCION < dt.date.fromisoformat(f[e]) < CORTE
    ]
    if len({e for e, _ in pares}) != len(pares):
        raise ValueError(f"RECUERDO: más de una variable de 2023 en un estudio: {sorted(pares)}")
    filtro = pl.lit(False)
    for e, v in pares:
        filtro = filtro | ((pl.col("estudio") == e) & (pl.col("variable") == v))
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter(filtro)
        .select("estudio", "encuestado", "etiqueta")
        .collect()
    )
    m = mapa()
    sin = sorted(set(lg["etiqueta"].drop_nulls().str.strip_chars().unique()) - set(m))
    if sin:
        raise ValueError(f"RECUERDO: etiquetas sin correspondencia en partidos.yaml: {sin}")
    return lg.with_columns(
        pl.col("etiqueta").str.strip_chars().replace_strict(m).alias("recuerdo")
    ).drop("etiqueta")


def datos() -> pl.DataFrame:
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    return (
        p.join(respuestas(), on=["estudio", "encuestado"])
        .filter(
            (pl.col("edad") >= 18)
            & ~pl.col("estudios_3").is_in(["NC", "NS"])
            & ~pl.col("actividad_3").is_in(["NC", "NS"])
            & ~pl.col("recuerdo").is_in(["no_tenia_edad", "sin_derecho_voto", "NP"])
        )
        .with_columns(
            (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
            _edad_grupo(pl.col("edad")),
        )
        .sort("estudio", "encuestado")
    )


def objetivos() -> pl.DataFrame:
    """Proporciones oficiales por provincia (residentes, con abstención)."""
    filas = []
    for f in sorted((PROCESSED_DIR / "targets").glob("PROV_*.parquet")):
        t = pl.read_parquet(f).filter(pl.col("objetivo") == "voto_generales_2023")
        filas.append(
            t.select(
                pl.col("territorio")
                .str.replace("PROV:", "")
                .str.replace("PROV_", "")
                .alias("provincia"),
                pl.col("clave").str.split("=").list.get(1).alias("opcion"),
                "valor",
            )
        )
    t = pl.concat(filas)
    return t.with_columns((pl.col("valor") / pl.col("valor").sum().over("provincia")).alias("p"))


MIN_CENSO_CELDA = 1000  # electores de la mitad de calibración para usar la forma de una celda


def mitad(municipio: str) -> int:
    """0 = municipio de calibración, 1 = de validación (reservado). Reparto fijo por hash del
    código INE (D-067): reproducible e independiente del resultado."""
    return int(hashlib.sha256(municipio.encode()).hexdigest()[:8], 16) % 2


def municipales() -> pl.DataFrame:
    """Opciones por municipio con su tamaño (Padrón 2025) y su mitad."""
    from sinpop.harmonize.censos import poblacion_municipal, tamanos_municipales
    from sinpop.targets.electorales import generales_municipios

    op, _ = generales_municipios()
    tam = tamanos_municipales(poblacion_municipal())
    sin = set(op["municipio"].unique()) - set(tam)
    if sin:
        raise ValueError(f"municipios sin tamaño en el Padrón: {sorted(sin)[:10]}")
    return op.with_columns(
        pl.col("municipio").replace_strict(tam).alias("tamano_municipio"),
        pl.col("municipio").map_elements(mitad, return_dtype=pl.Int64).alias("mitad"),
    )


def forma_celdas() -> pl.DataFrame:
    """Cociente r = p(opción | provincia, tamaño) / p(opción | provincia) en la mitad de
    calibración, para las celdas con al menos `MIN_CENSO_CELDA` electores en esa mitad."""
    a = municipales().filter(pl.col("mitad") == 0)
    cel = a.group_by("provincia", "tamano_municipio", "opcion").agg(pl.col("valor").sum())
    cel = cel.with_columns(
        pl.col("valor").sum().over("provincia", "tamano_municipio").alias("censo"),
    ).with_columns((pl.col("valor") / pl.col("censo")).alias("p_celda"))
    prov = (
        a.group_by("provincia", "opcion")
        .agg(pl.col("valor").sum())
        .with_columns((pl.col("valor") / pl.col("valor").sum().over("provincia")).alias("p_prov"))
        .drop("valor")
    )
    return (
        cel.join(prov, on=["provincia", "opcion"])
        .filter(pl.col("censo") >= MIN_CENSO_CELDA)
        .with_columns(
            pl.when(pl.col("p_prov") > 0)
            .then(pl.col("p_celda") / pl.col("p_prov"))
            .otherwise(1.0)
            .alias("r")
        )
        .select("provincia", "tamano_municipio", "opcion", "r", "censo")
    )


def _softmax(z: np.ndarray) -> np.ndarray:
    z = z - z.max(axis=1, keepdims=True)
    q = np.exp(z)
    return q / q.sum(axis=1, keepdims=True)


def calibrar_provincia(
    logp: np.ndarray,
    w: np.ndarray,
    celda: np.ndarray,
    total: np.ndarray,
    formas: dict[str, np.ndarray],
    rondas: int = 30,
) -> np.ndarray:
    """Logits calibrados: desplazamientos por celda de tamaño (forma de la mitad de calibración,
    escalada al total oficial de la provincia) alternados con un desplazamiento común de la
    provincia; la última pasada es la de la provincia, cuyo total queda exacto."""
    z = logp.copy()
    for _ in range(rondas):
        for c, r in formas.items():
            s = celda == c
            if not s.any():
                continue
            objetivo = total * r
            objetivo = objetivo / objetivo.sum()
            z[s] += calibrar(z[s], w[s], objetivo)
        z += calibrar(z, w, total)
    return z


def calibrar(logp: np.ndarray, w: np.ndarray, objetivo: np.ndarray, iters: int = 500) -> np.ndarray:
    """Desplazamientos δ por opción tales que Σ w·softmax(logp + δ) / Σ w = objetivo."""
    delta = np.where(objetivo > 0, 0.0, -np.inf)
    for _ in range(iters):
        z = logp + delta
        z -= z.max(axis=1, keepdims=True)
        pr = np.exp(z)
        pr /= pr.sum(axis=1, keepdims=True)
        actual = (pr * w[:, None]).sum(0) / w.sum()
        paso = np.where(objetivo > 0, np.log(objetivo / np.maximum(actual, 1e-300)), 0.0)
        delta = delta + paso
        if np.abs(actual - objetivo).max() < 1e-7:
            break
    return delta


def asignar(
    persons: pl.DataFrame, opinion: pl.DataFrame, elegible: np.ndarray, rng: np.random.Generator
) -> tuple[pl.DataFrame, dict]:
    perfil = perfil_sintetico(persons).join(
        opinion.select("person_id", "religiosidad", "clase_subjetiva"), on="person_id", how="left"
    )
    pesos = perfil.select("person_id").join(
        persons.select("person_id", "peso", "provincia", "tamano_municipio"),
        on="person_id",
        how="left",
    )
    d = datos()
    entreno = d.filter(pl.col("recuerdo").is_in(OPCIONES))
    m = Modelo("recuerdo", columnas=COLUMNAS_VOTO).ajustar(entreno)
    clases = list(m.clases)
    if sorted(clases) != sorted(OPCIONES):
        raise ValueError(f"opciones del modelo distintas de las previstas: {clases}")
    pr = m.probabilidades(perfil)
    logp = np.log(np.maximum(pr, 1e-12))
    obj = objetivos()
    formas_df = forma_celdas()
    prov = pesos["provincia"].to_numpy()
    tam = pesos["tamano_municipio"].to_numpy()
    w = pesos["peso"].to_numpy()
    eleg = elegible
    voto = np.full(perfil.height, None, dtype=object)
    info = {}
    for p in sorted(obj["provincia"].unique()):
        o = dict(obj.filter(pl.col("provincia") == p).select("opcion", "p").iter_rows())
        total = np.array([o.get(c, 0.0) for c in clases])
        sel = np.flatnonzero((prov == p) & eleg)
        if not len(sel):
            continue
        formas = {}
        for c in formas_df.filter(pl.col("provincia") == p)["tamano_municipio"].unique().sort():
            rr = dict(
                formas_df.filter((pl.col("provincia") == p) & (pl.col("tamano_municipio") == c))
                .select("opcion", "r")
                .iter_rows()
            )
            formas[c] = np.array([rr.get(k, 1.0) for k in clases])
        q = _softmax(calibrar_provincia(logp[sel], w[sel], tam[sel], total, formas))
        u = rng.random(len(sel))
        idx = (q.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(clases) - 1)
        voto[sel] = np.array(clases)[idx]
        info[p] = {"electores_sinteticos": len(sel), "celdas_con_forma": sorted(formas)}
    espanol = (perfil["nacionalidad_esp_ext"] == "espanola").to_numpy()
    voto = np.where(pd_null(voto), np.where(espanol, "no_tenia_edad", "sin_derecho_voto"), voto)
    # propensión a no recordar / no contestar, entre quienes tenían derecho a voto
    ns = d.filter(pl.col("recuerdo").is_in(OPCIONES + ["NS", "NC"])).with_columns(
        pl.col("recuerdo").is_in(["NS", "NC"]).cast(pl.Utf8).alias("ns_nc")
    )
    mn = Modelo("ns_nc", columnas=COLUMNAS).ajustar(ns)
    pns = mn.probabilidades(perfil)[:, list(mn.clases).index("true")]
    ns_nc = (rng.random(perfil.height) < pns) & eleg
    out = perfil.select("person_id").with_columns(
        pl.Series("recuerdo_voto_generales", voto, dtype=pl.Utf8),
        pl.Series("recuerdo_voto_generales_ns_nc", ns_nc),
    )
    meta = {
        "encuestados": entreno.height,
        "estudios": sorted(entreno["estudio"].unique()),
        "c": m.c_elegido,
        "ns_nc_cis": float((ns["ns_nc"] == "true").cast(pl.Float64).mean()),
        "calibracion": json.loads(json.dumps(info)),
    }
    return out, meta


def pd_null(a: np.ndarray) -> np.ndarray:
    return np.array([x is None for x in a])
