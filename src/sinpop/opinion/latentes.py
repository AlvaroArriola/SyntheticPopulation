"""Rasgos latentes de actitud (F8A, tarea 4; `02_datos_y_variables.md` §3.4, docs/03 §2.4).

Cada rasgo se define en `configs/rasgos.yaml` por una batería de ítems de un estudio del CIS:
qué variables, con qué puntuación por **etiqueta** (nunca por código: los códigos cambian entre
estudios) y en qué estudios. «No sabe», «No contesta» y «No procede» no tienen posición en la
escala: cuentan como dato ausente del ítem (su propensión es el rasgo `estilo_ns_nc`).

1. Factorial confirmatorio de un factor por rasgo (máxima verosimilitud sobre la matriz de
   correlaciones de Pearson ponderada, casos completos) → V-LATENTE (CFI, RMSEA, omega).
2. Puntuación de cada encuestado con al menos la mitad de los ítems contestados: puntuación de
   regresión con los ítems tipificados (ausentes = media), tipificada de nuevo con los pesos y
   orientada para que las cargas sean positivas (más puntuación = más rasgo).
3. El modelo de perfil y la extracción con residuo real (`rasgos.ModeloRasgo`) son los mismos que
   los del estilo NS/NC.
"""

from __future__ import annotations

import math
import re
from functools import lru_cache

import numpy as np
import polars as pl
import yaml

from sinpop import CONFIGS_DIR, INTERIM_DIR
from sinpop.opinion import factorial as F
from sinpop.opinion.valores import _edad_grupo

SIN_POSICION = {"N.S.", "N.C.", "No sabe", "No contesta", "No procede", "N.P.", "No sabe, duda"}


@lru_cache(maxsize=1)
def config() -> dict:
    return yaml.safe_load((CONFIGS_DIR / "rasgos.yaml").read_text("utf-8"))


def rasgos() -> list[str]:
    return list(config()["rasgos"])


def _puntuar(etiqueta: str | None, escala: str | dict, var: str) -> float | None:
    if etiqueta is None:
        return None
    et = etiqueta.strip()
    if et in SIN_POSICION or et.startswith("(NO LEER) N.S") or et.startswith("N.S."):
        return None
    if escala == "numerica":  # escalas 0-10 o 1-10: el número inicial de la etiqueta
        m = re.match(r"^(\d{1,2})(\s|$)", et)
        if m:
            return float(m.group(1))
        raise ValueError(f"{var}: etiqueta sin número en escala numérica: {et!r}")
    mapa = config()["escalas"][escala] if isinstance(escala, str) else escala
    limpia = re.sub(r"^\(NO LEER\)\s*", "", et)
    for k in (et, limpia):
        if k in mapa:
            v = mapa[k]
            return None if v is None else float(v)
    raise ValueError(f"{var}: etiqueta no prevista en la escala {escala}: {et!r}")


def items(rasgo: str) -> pl.DataFrame:
    """Ancho: estudio, encuestado y una columna por ítem con su puntuación (nulo si no hay)."""
    c = config()["rasgos"][rasgo]
    estudios = [str(e) for e in c["estudios"]]
    defs = c["items"]
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter(pl.col("estudio").is_in(estudios) & pl.col("variable").is_in(list(defs)))
        .select("estudio", "encuestado", "variable", "etiqueta")
        .collect()
    )
    faltan = set(defs) - set(lg["variable"].unique())
    if faltan:
        raise ValueError(f"{rasgo}: ítems sin datos en {estudios}: {sorted(faltan)}")
    puntos = []
    for (var, et), _ in lg.group_by("variable", "etiqueta"):
        d = defs[var]
        esc = d["escala"] if isinstance(d, dict) else d
        v = _puntuar(et, esc, var)
        if v is not None and isinstance(d, dict) and d.get("invertir"):
            v = -v
        puntos.append({"variable": var, "etiqueta": et, "valor": v})
    tabla = pl.DataFrame(
        puntos, schema={"variable": pl.Utf8, "etiqueta": pl.Utf8, "valor": pl.Float64}
    )
    return (
        lg.join(tabla, on=["variable", "etiqueta"], how="left")
        .pivot(on="variable", index=["estudio", "encuestado"], values="valor")
        .select("estudio", "encuestado", *sorted(defs))
    )


def _base(rasgo: str) -> pl.DataFrame:
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    return (
        items(rasgo)
        .join(p, on=["estudio", "encuestado"])
        .filter(pl.col("edad") >= 18)
        .with_columns((pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"))
    )


def _corr_ponderada(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    w = w / w.sum()
    m = w @ x
    xc = x - m
    cov = (xc * w[:, None]).T @ xc
    sd = np.sqrt(np.diag(cov))
    return cov / np.outer(sd, sd)


def ajuste(rasgo: str) -> tuple[F.AjusteCFA, dict]:
    d = _base(rasgo)
    cols = sorted(config()["rasgos"][rasgo]["items"])
    cc = d.drop_nulls(cols)
    x, w = cc.select(cols).to_numpy(), cc["peso"].to_numpy()
    S = _corr_ponderada(x, w)
    a = F.ajustar(S, cc.height, np.zeros(len(cols), dtype=int))
    signo = 1.0 if a.cargas[:, 0].sum() >= 0 else -1.0
    info = {
        "rasgo": rasgo,
        "items": cols,
        "estudios": sorted(d["estudio"].unique().to_list()),
        "n_completos": cc.height,
        "cargas": dict(zip(cols, (signo * a.cargas[:, 0]).round(3).tolist(), strict=True)),
        "cfi": a.cfi,
        "rmsea": a.rmsea,
        "omega": float(a.omega[0]),
        "chi2": a.chi2,
        "gl": a.gl,
    }
    return a, info


def datos(rasgo: str) -> pl.DataFrame:
    """Encuestados con la puntuación del rasgo (media 0, desviación 1 ponderadas)."""
    a, _ = ajuste(rasgo)
    d = _base(rasgo)
    cols = sorted(config()["rasgos"][rasgo]["items"])
    x = d.select(cols).to_numpy().astype(float)
    w = d["peso"].to_numpy()
    validos = (~np.isnan(x)).sum(axis=1) >= math.ceil(len(cols) / 2)
    z = np.zeros_like(x)
    for j in range(len(cols)):
        ok = ~np.isnan(x[:, j])
        m = np.average(x[ok, j], weights=w[ok])
        s = math.sqrt(np.average((x[ok, j] - m) ** 2, weights=w[ok]))
        z[:, j] = np.where(ok, (x[:, j] - m) / s, 0.0)
    f = F.puntuaciones(z, a)[:, 0]
    if a.cargas[:, 0].sum() < 0:
        f = -f
    m = np.average(f[validos], weights=w[validos])
    s = math.sqrt(np.average((f[validos] - m) ** 2, weights=w[validos]))
    d = d.with_columns(pl.Series(rasgo, (f - m) / s)).filter(pl.Series(validos))
    return d.filter(
        ~pl.col("estudios_3").is_in(["NC", "NS"]) & ~pl.col("actividad_3").is_in(["NC", "NS"])
    ).with_columns(_edad_grupo(pl.col("edad")))
