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


CAPAS = {"opinion": "rasgos", "politica": "rasgos_politicos"}


def rasgos(capa: str = "opinion") -> list[str]:
    """Rasgos de `opinion.parquet` (F8A) o de `politics.parquet` (F8B, `rasgos_politicos`)."""
    return list(config().get(CAPAS[capa], {}))


def definicion(rasgo: str) -> dict:
    for seccion in CAPAS.values():
        if rasgo in config().get(seccion, {}):
            return config()[seccion][rasgo]
    raise KeyError(rasgo)


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


def _intermedios_numericos(lg: pl.DataFrame, defs: dict) -> pl.DataFrame:
    """En algunas escalas numéricas el fichero solo etiqueta los extremos («1 Totalmente
    incómodo/a» … «10 Totalmente cómodo/a»). Un código sin etiqueta se acepta como su número solo
    si está entre los dos extremos etiquetados de esa variable en ese estudio; fuera de ese
    intervalo sigue sin etiqueta y detiene el proceso (nunca se inventa un código)."""
    numericas = [
        v for v, d in defs.items() if (d["escala"] if isinstance(d, dict) else d) == "numerica"
    ]
    if not numericas:
        return lg
    extremos = (
        lg.filter(
            pl.col("variable").is_in(numericas) & pl.col("etiqueta").str.contains(r"^\d{1,2}(\s|$)")
        )
        .group_by("estudio", "variable")
        .agg(pl.col("codigo").min().alias("lo"), pl.col("codigo").max().alias("hi"))
    )
    return (
        lg.join(extremos, on=["estudio", "variable"], how="left")
        .with_columns(
            pl.when(
                pl.col("etiqueta").is_null()
                & pl.col("codigo").is_between(pl.col("lo"), pl.col("hi"))
                & (pl.col("codigo") == pl.col("codigo").round(0))
            )
            .then(pl.col("codigo").cast(pl.Int64).cast(pl.Utf8))
            .otherwise(pl.col("etiqueta"))
            .alias("etiqueta")
        )
        .drop("lo", "hi")
    )


def items(rasgo: str) -> pl.DataFrame:
    """Ancho: estudio, encuestado y una columna por ítem con su puntuación (nulo si no hay)."""
    c = definicion(rasgo)
    estudios = [str(e) for e in c["estudios"]]
    defs = c["items"]
    if c.get("fuente") == "ess":  # ítems ya puntuados por etiqueta en `ess.armonizar`
        d = pl.read_parquet(INTERIM_DIR / "ess_es.parquet")
        if "posicion_partido_votado" in defs:
            from sinpop.politics.posiciones import posicion

            d = d.with_columns(posicion(d["voto_generales_2023"], d["ccaa"]))
        invertir = [v for v, x in defs.items() if isinstance(x, dict) and x.get("invertir")]
        return (
            d.with_columns([-pl.col(v) for v in invertir])
            .select("estudio", "encuestado", *sorted(defs))
            .sort("estudio", "encuestado")
        )
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter(pl.col("estudio").is_in(estudios) & pl.col("variable").is_in(list(defs)))
        .select("estudio", "encuestado", "variable", "codigo", "etiqueta")
        .collect()
    )
    lg = _intermedios_numericos(lg, defs)
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
        lg.drop("codigo")
        .join(tabla, on=["variable", "etiqueta"], how="left")
        .pivot(on="variable", index=["estudio", "encuestado"], values="valor")
        .select("estudio", "encuestado", *sorted(defs))
        .sort("estudio", "encuestado")  # pivot no garantiza el orden: reproducibilidad
    )


def universo(rasgo: str) -> str:
    """«espanoles» (barómetros y estudios del CIS) o «todos» (la ESS entrevista a residentes
    de cualquier nacionalidad)."""
    return "todos" if definicion(rasgo).get("fuente") == "ess" else "espanoles"


def columnas(rasgo: str) -> list[str] | None:
    """Predictores del modelo de perfil del rasgo (None: los de siempre)."""
    return definicion(rasgo).get("columnas")


def _base(rasgo: str) -> pl.DataFrame:
    if universo(rasgo) == "todos":
        p = pl.read_parquet(INTERIM_DIR / "ess_es.parquet").drop(
            sorted(definicion(rasgo)["items"]), strict=False
        )
        return items(rasgo).join(p, on=["estudio", "encuestado"]).filter(pl.col("edad") >= 18)
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    return (
        items(rasgo)
        .join(p, on=["estudio", "encuestado"])
        .filter(
            (pl.col("edad") >= 18)
            & (
                pl.col("nacionalidad_esp_ext").is_null()
                | (pl.col("nacionalidad_esp_ext") == "espanola")
            )
        )
        .with_columns((pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"))
    )


def _corr_ponderada(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    w = w / w.sum()
    m = w @ x
    xc = x - m
    cov = (xc * w[:, None]).T @ xc
    sd = np.sqrt(np.diag(cov))
    return cov / np.outer(sd, sd)


def residuos(rasgo: str, cols: list[str]) -> list[tuple[int, int]]:
    """Pares de ítems con residuos correlacionados declarados en `rasgos.yaml` (D-067)."""
    return [(cols.index(a), cols.index(b)) for a, b in definicion(rasgo).get("residuos", [])]


def ajuste(rasgo: str) -> tuple[F.AjusteCFA, dict]:
    d = _base(rasgo)
    cols = sorted(definicion(rasgo)["items"])
    cc = d.drop_nulls(cols)
    x, w = cc.select(cols).to_numpy(), cc["peso"].to_numpy()
    S = _corr_ponderada(x, w)
    a = F.ajustar(S, cc.height, np.zeros(len(cols), dtype=int), residuos(rasgo, cols))
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
        "residuos_correlacionados": definicion(rasgo).get("residuos", []),
        "chi2": a.chi2,
        "gl": a.gl,
    }
    return a, info


def datos(rasgo: str) -> pl.DataFrame:
    """Encuestados con la puntuación del rasgo (media 0, desviación 1 ponderadas)."""
    a, _ = ajuste(rasgo)
    d = _base(rasgo)
    cols = sorted(definicion(rasgo)["items"])
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


def ajuste_conjunto(
    estudio: str, capa: str = "opinion", conjunto: str | None = None
) -> dict | None:
    """Factorial de varios factores con todos los rasgos medidos en un mismo estudio: contrasta
    el ajuste de los rasgos con pocos ítems (un factor con tres ítems tiene 0 grados de
    libertad) y que los rasgos son distintos (correlación entre factores)."""
    nombres = [
        r
        for r in rasgos(capa)
        if [str(e) for e in definicion(r)["estudios"]] == [estudio]
        and (conjunto is None or definicion(r).get("conjunto") == conjunto)
    ]
    if len(nombres) < 2:
        return None
    bases = [_base(r) for r in nombres]
    d = bases[0]
    for b in bases[1:]:
        d = d.join(
            b.select(
                "estudio", "encuestado", *[c for c in sorted(b.columns) if c not in d.columns]
            ),
            on=["estudio", "encuestado"],
        )
    cols, asignacion, pares = [], [], []
    for k, r in enumerate(nombres):
        propios = sorted(definicion(r)["items"])
        pares += [(len(cols) + i, len(cols) + j) for i, j in residuos(r, propios)]
        cols += propios
        asignacion += [k] * len(propios)
    cc = d.drop_nulls(cols)
    S = _corr_ponderada(cc.select(cols).to_numpy(), cc["peso"].to_numpy())
    a = F.ajustar(S, cc.height, np.array(asignacion), pares)
    return {
        "estudio": estudio,
        "conjunto": conjunto,
        "rasgos": nombres,
        "n_completos": cc.height,
        "cfi": a.cfi,
        "rmsea": a.rmsea,
        "chi2": a.chi2,
        "gl": a.gl,
        "correlaciones_factores": a.phi.round(3).tolist(),
    }
