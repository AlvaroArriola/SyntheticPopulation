"""V-OPINION-CV (G8A.2): validación cruzada por pregunta completa (docs/05 §7).

Para cada pregunta del CIS que se repite, con las mismas opciones, en al menos `MIN_ESTUDIOS`
barómetros anteriores al corte:

- se reserva el estudio más reciente en que aparece (la pregunta completa de ese estudio no se
  usa en el ajuste);
- el modelo de opinión (regresión multinomial ponderada con el perfil y el territorio, el mismo
  de las variables de valores) se ajusta con las respuestas de los estudios anteriores;
- se predice la distribución de respuestas del estudio reservado en cada grupo
  edad_4 × sexo × estudios con al menos `MIN_GRUPO` encuestados, y se mide la TVD frente a la
  distribución observada (ponderada);
- **B0** (baseline ingenuo, docs/04 F9.7): la distribución histórica nacional de la pregunta en
  los estudios anteriores, igual para todos los grupos.

La puerta pide que la TVD media del modelo sea menor que la de B0.
"""

from __future__ import annotations

import json

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR
from sinpop.opinion import valores as V
from sinpop.validate import metrics as M

MIN_ESTUDIOS = 3
MIN_GRUPO = 100
MIN_RESPUESTAS = 5000
EXCLUIR = {  # perfil, pesos y control de calidad: no son preguntas de opinión
    "SEXO", "EDAD", "ESTUDIOS", "NIVELESTENTREV", "SITLAB", "NACIONALIDAD", "ECIVIL", "TAMUNI",
    "RELALAB", "SITCONV", "PESO", "PESOCCAA", "ADQUINAC", "PAISNAC", "PAISNAC2",
}  # fmt: skip


# Preguntas que no son de opinión: técnicas de la entrevista, perfil socioeconómico y las
# políticas (voto, líderes, partidos, ideología), que son de la capa política (F8B, D-005), y
# las observaciones del entrevistador sobre la entrevista (V2_*, V3)
NO_OPINION = (
    r"^(IA_|TIPO_TEL|SINCERIDAD|ESCUELA|INGRES|ESTUDIOS|HOGAR|NUMPERS|MOVIL|TELEF|"
    r"LIDER|VOTO|RECUERDO|RECUVOTO|INTENCION|VOTOSIM|ESCIDEOL|PARTIDO|CERCANIA|SIMPATIA|"
    r"CONFIANZAPTE|CONFIANZAOPOSIC|PROBVOTO|VALORA|PREFPTE|PREFERENCIA|AFILIA|PARTICIPA|"
    r"CONOMINIS|VALMINIS|CONOLIDER|FIDEVOTO|MVOTO|CAPITAL|CNO11|ENTREV|ESTUDIO$|CUES|PROV|MUN|"
    r"V2_|V3$)"
)


def preguntas_repetidas() -> pl.DataFrame:
    """Una versión por pregunta (la que aparece en más estudios): las listas de opciones
    cambian con el tiempo (por ejemplo, los problemas codificados) y cada lista es una
    pregunta distinta en el banco."""
    banco = pl.read_parquet(INTERIM_DIR / "cis_preguntas.parquet")
    # solo estudios de ámbito nacional (los autonómicos entrevistan a una comunidad, D-065)
    nacionales = V.estudios_nacionales()
    banco = banco.with_columns(
        pl.col("estudios").list.eval(pl.element().filter(pl.element().is_in(nacionales)))
    )
    return (
        banco.filter(
            (pl.col("estudios").list.len() >= MIN_ESTUDIOS)
            & ~pl.col("variable").is_in(list(EXCLUIR))
            & ~pl.col("variable").str.contains(NO_OPINION)
            & ~pl.col("enunciado").str.contains(
                r"(?i)^nacionalidad|^edad|^sexo|^provincia|^municipio"
            )
        )
        .sort(pl.col("estudios").list.len(), "variable", descending=[True, False])
        .unique(["variable", "enunciado"], keep="first", maintain_order=True)
        .sort("variable")
    )


def _grupo(df: pl.DataFrame) -> pl.DataFrame:
    from sinpop.validate.fase8a import _edad_4

    return df.with_columns(_edad_4(pl.col("edad")))


def evaluar(variable: str, estudios: list[str]) -> dict | None:
    lg = (
        pl.scan_parquet(INTERIM_DIR / "cis_largo.parquet")
        .filter((pl.col("variable") == variable) & pl.col("estudio").is_in(estudios))
        .select("estudio", "encuestado", pl.col("etiqueta").alias(variable))
        .collect()
    )
    p = pl.read_parquet(INTERIM_DIR / "cis_personas.parquet")
    d = (
        p.join(lg, on=["estudio", "encuestado"])
        .filter(
            (pl.col("edad") >= 18)
            & ~pl.col("estudios_3").is_in(["NC", "NS"])
            & ~pl.col("actividad_3").is_in(["NC", "NS"])
            & pl.col(variable).is_not_null()
            & ~pl.col(variable).is_in(["No procede", "N.P."])
        )
        .with_columns(
            V._edad_grupo(pl.col("edad")),
            (pl.col("peso") / pl.col("peso").mean().over("estudio")).alias("peso"),
        )
    )
    orden = sorted(estudios, key=lambda e: d.filter(pl.col("estudio") == e)["fecha"].min() or "")
    test, entreno = orden[-1], orden[:-1]
    tr, te = d.filter(pl.col("estudio").is_in(entreno)), d.filter(pl.col("estudio") == test)
    if tr.height < MIN_RESPUESTAS or te.height < 1000 or tr[variable].n_unique() < 2:
        return None
    m = V.Modelo(variable).ajustar(tr)
    te = _grupo(te)
    pr = m.probabilidades(te)
    clases = list(m.clases)
    b0 = (
        tr.group_by(variable)
        .agg(pl.col("peso").sum())
        .with_columns(pl.col("peso") / pl.col("peso").sum())
    )
    b0v = np.array([dict(b0.iter_rows()).get(c, 0.0) for c in clases])
    tvd_m, tvd_b = [], []
    grupo = ["edad_4", "sexo", "estudios_3"]
    te = te.with_columns(pl.int_range(te.height).alias("_i"))
    for _, g in te.group_by(grupo):
        if g.height < MIN_GRUPO:
            continue
        w = g["peso"].to_numpy()
        obs = np.array([w[g[variable].to_numpy() == c].sum() for c in clases])
        extra = w.sum() - obs.sum()  # respuestas que no vio el entrenamiento
        obs = np.append(obs, extra) / w.sum()
        pred = np.append((pr[g["_i"].to_numpy()] * w[:, None]).sum(0) / w.sum(), 0.0)
        tvd_m.append(M.tvd(pred, obs))
        tvd_b.append(M.tvd(np.append(b0v, 0.0), obs))
    if not tvd_m:
        return None
    return {
        "variable": variable,
        "estudio_reservado": test,
        "estudios_entreno": entreno,
        "grupos": len(tvd_m),
        "tvd_modelo": float(np.mean(tvd_m)),
        "tvd_b0": float(np.mean(tvd_b)),
    }


def v_opinion_cv(max_preguntas: int = 40) -> dict:
    filas = []
    for var, estudios in preguntas_repetidas().select("variable", "estudios").iter_rows():
        r = evaluar(var, list(estudios))
        if r:
            filas.append(r)
        if len(filas) >= max_preguntas:
            break
    tm = float(np.mean([f["tvd_modelo"] for f in filas])) if filas else None
    tb = float(np.mean([f["tvd_b0"] for f in filas])) if filas else None
    return {
        "preguntas": len(filas),
        "tvd_media_modelo": tm,
        "tvd_media_b0": tb,
        "ok": bool(filas) and tm < tb,
        "detalle": filas,
    }


if __name__ == "__main__":
    print(json.dumps(v_opinion_cv(), ensure_ascii=False, indent=1)[:3000])
