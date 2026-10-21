"""G8A.5: respuestas simuladas por comunidad frente al Barómetro Sanitario (docs/04 F8A).

Para cada pregunta de opinión que se repite, con las mismas opciones, en la última oleada del
Barómetro Sanitario anterior al corte y en alguna oleada previa:

- el modelo de opinión (el multinomial ponderado de las variables de valores) se ajusta con las
  oleadas previas y la población sintética **responde**: a cada adulto de nacionalidad española
  en vivienda familiar (el universo del CIS) se le sortea una respuesta con la semilla;
- la distribución simulada de cada comunidad se compara con la observada en la última oleada,
  ponderada, por la TVD;
- referencias para leer el error: **B0**, la distribución nacional de las oleadas previas, igual
  para todas las comunidades; **B1**, la distribución observada de cada comunidad en las oleadas
  previas (estimación directa); y el **ruido muestral** de la oleada de contraste (TVD media entre
  réplicas bootstrap de la comunidad y su distribución observada).

La puerta pide informar del error, sin umbral (docs/04 G8A.5).
"""

from __future__ import annotations

import json

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion import valores as V
from sinpop.opinion.cis import SELECCION
from sinpop.opinion.cv import EXCLUIR, NO_OPINION
from sinpop.repro import make_rng
from sinpop.validate import metrics as M

REPLICAS = 100
NO_RESPUESTA = ["No procede", "N.P."]


def oleadas() -> list[str]:
    """Estudios del Barómetro Sanitario anteriores al corte, por fecha."""
    sel = json.loads(SELECCION.read_text("utf-8"))
    hechos = set(pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")["estudio"].unique())
    return [
        e["estudio"]
        for e in sorted(sel, key=lambda e: e["fecha"])
        if "sanitario" in e["titulo"].lower() and e["estudio"] in hechos
    ]


def preguntas(entreno: list[str], test: str) -> list[str]:
    banco = pl.read_parquet(INTERIM_DIR / "cis_preguntas.parquet")
    return sorted(
        banco.filter(
            pl.col("estudios").list.contains(test)
            & pl.col("estudios").list.eval(pl.element().is_in(entreno)).list.any()
            & ~pl.col("variable").is_in(list(EXCLUIR))
            & ~pl.col("variable").str.contains(NO_OPINION)
        )["variable"].unique()
    )


def _respuestas(variable: str, estudios: list[str]) -> pl.DataFrame:
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter((pl.col("variable") == variable) & pl.col("estudio").is_in(estudios))
        .select("estudio", "encuestado", pl.col("etiqueta").alias(variable))
        .collect()
    )
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    return (
        p.join(lg, on=["estudio", "encuestado"])
        .filter(
            (pl.col("edad") >= 18)
            & ~pl.col("estudios_3").is_in(["NC", "NS"])
            & ~pl.col("actividad_3").is_in(["NC", "NS"])
            & pl.col(variable).is_not_null()
            & ~pl.col(variable).is_in(NO_RESPUESTA)
        )
        .with_columns(
            V._edad_grupo(pl.col("edad")),
            (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
        )
    )


def _dist(etiquetas: np.ndarray, w: np.ndarray, clases: list[str]) -> np.ndarray:
    v = np.array([w[etiquetas == c].sum() for c in clases])
    return v / w.sum()


def evaluar(
    variable: str, entreno: list[str], test: str, perfil: pl.DataFrame, peso: np.ndarray, rng
) -> list[dict] | None:
    d = _respuestas(variable, entreno + [test])
    tr, te = d.filter(pl.col("estudio") != test), d.filter(pl.col("estudio") == test)
    if tr.height < 2000 or te.height < 1000 or tr[variable].n_unique() < 2:
        return None
    m = V.Modelo(variable).ajustar(tr)
    clases = list(m.clases) + sorted(set(te[variable].unique()) - set(m.clases))
    pr = m.probabilidades(perfil)
    u = rng.random(len(pr))
    idx = (pr.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(m.clases) - 1)
    simulada = np.array(m.clases)[idx]
    ccaa_s = perfil["ccaa"].to_numpy()
    b0 = _dist(tr[variable].to_numpy(), tr["peso"].to_numpy(), clases)
    filas = []
    for c in sorted(te["ccaa"].drop_nulls().unique()):
        g, h = te.filter(pl.col("ccaa") == c), tr.filter(pl.col("ccaa") == c)
        sel = ccaa_s == c
        if g.height < 50 or not sel.any():
            continue
        y, w = g[variable].to_numpy(), g["peso"].to_numpy()
        obs = _dist(y, w, clases)
        sim = _dist(simulada[sel], peso[sel], clases)
        b1 = _dist(h[variable].to_numpy(), h["peso"].to_numpy(), clases) if h.height else b0
        ruido = []
        for _ in range(REPLICAS):
            i = rng.integers(0, len(y), len(y))
            ruido.append(M.tvd(_dist(y[i], w[i], clases), obs))
        filas.append(
            {
                "variable": variable,
                "ccaa": c,
                "n_contraste": g.height,
                "tvd_simulada": M.tvd(sim, obs),
                "tvd_b0": M.tvd(b0, obs),
                "tvd_b1": M.tvd(b1, obs),
                "ruido_muestral": float(np.mean(ruido)),
            }
        )
    return filas


def g8a5(persons: pl.DataFrame, semilla: int, max_preguntas: int = 30) -> tuple[pl.DataFrame, dict]:
    ol = oleadas()
    if len(ol) < 2:
        return pl.DataFrame(), {"ok": False, "motivo": f"oleadas disponibles: {ol}"}
    test, entreno = ol[-1], ol[:-1]
    perfil = V.perfil_sintetico(persons.filter(pl.col("edad") >= 18)).filter(
        (pl.col("nacionalidad_esp_ext") == "espanola")
        & (pl.col("tipo_residencia") == "vivienda_familiar")
    )
    peso = (
        perfil.select("person_id")
        .join(persons.select("person_id", "peso"), on="person_id", how="left")["peso"]
        .to_numpy()
    )
    rng = make_rng(semilla)
    filas = []
    usadas = []
    for v in preguntas(entreno, test):
        r = evaluar(v, entreno, test, perfil, peso, rng)
        if r:
            filas += r
            usadas.append(v)
        if len(usadas) >= max_preguntas:
            break
    t = pl.DataFrame(filas)
    if t.is_empty():
        return t, {"ok": False, "motivo": "sin preguntas comunes evaluables"}
    res = {
        "ok": True,
        "oleada_contraste": test,
        "oleadas_ajuste": entreno,
        "preguntas": usadas,
        "celdas": t.height,
        "tvd_media_simulada": float(t["tvd_simulada"].mean()),
        "tvd_media_b0": float(t["tvd_b0"].mean()),
        "tvd_media_b1": float(t["tvd_b1"].mean()),
        "ruido_muestral_medio": float(t["ruido_muestral"].mean()),
        "por_ccaa": t.group_by("ccaa")
        .agg(pl.col("tvd_simulada", "tvd_b0", "tvd_b1", "ruido_muestral").mean())
        .sort("ccaa")
        .to_dicts(),
    }
    return t, res
