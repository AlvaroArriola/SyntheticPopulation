"""Validación de F8B: capa política (docs/04 F8B, docs/05 V-POL-*).

- G8B.1 V-POL-RECUERDO: recuerdo de las generales de 2023 por provincia (la unidad de
  calibración) frente al resultado oficial de los residentes, abstención incluida.
- G8B.2 V-POL-RESERVADA: las europeas de 2024 están excluidas (D-022). Se valida con la
  **mitad reservada** de los municipios (D-067), que no interviene en la calibración: voto por
  comunidad × tamaño de municipio y por tamaño en España, con los umbrales de V-POL-RESERVADA
  (TVD ≤ 0,04 en España y ≤ 0,06 por comunidad; error de participación ≤ 3 puntos). Como la
  mitad reservada es una muestra de municipios, la TVD de cada celda se compara con su umbral
  más el ruido de ese muestreo: bootstrap de los municipios reservados de la celda (la mitad es
  una muestra de municipios, no de personas) y el de la propia muestra sintética. Solo se
  evalúan las celdas con al menos 5 municipios reservados; las demás se informan.

Comando: `python -m sinpop.validate.fase8b`
"""

from __future__ import annotations

import datetime as dt
import json

import numpy as np
import polars as pl

from sinpop import POPULATIONS_DIR, REPORTS_DIR
from sinpop.config import load_config
from sinpop.harmonize.core import ccaa_de_provincia
from sinpop.politics import recuerdo as RV
from sinpop.repro import code_version
from sinpop.validate import metrics as M

NACIONAL = "2026-01-01_ES_1000000_s1"
RESUMEN = REPORTS_DIR / "fase_08b_validacion.json"
DETALLE = REPORTS_DIR / "fase_08b"
MIN_ELECTORES_CELDA = 500  # electores sintéticos para evaluar una celda
MIN_MUNICIPIOS_RESERVADOS = 5  # una celda con menos no representa su comunidad × tamaño
REPLICAS = 200


def ruido_municipios(
    o: pl.DataFrame, b: np.ndarray, rng: np.random.Generator
) -> tuple[float, float]:
    """Percentil 95 de la TVD y del error de participación (puntos) entre réplicas bootstrap de
    los municipios reservados de la celda y su distribución: la incertidumbre de la mitad
    reservada como estimación de la celda (muestreo de municipios, no de personas)."""
    ancho = o.pivot(on="opcion", index="municipio", values="valor").fill_null(0.0)
    x = np.column_stack(
        [ancho[k].to_numpy() if k in ancho.columns else np.zeros(ancho.height) for k in RV.OPCIONES]
    )
    pb = b / b.sum()
    i = RV.OPCIONES.index("abstencion")
    tv, ab = [], []
    for _ in range(REPLICAS):
        s = x[rng.integers(0, len(x), len(x))].sum(0)
        ps = s / s.sum()
        tv.append(0.5 * np.abs(ps - pb).sum())
        ab.append(abs(ps[i] - pb[i]) * 100)
    return float(np.percentile(tv, 95)), float(np.percentile(ab, 95))


def sintetica(run_id: str) -> pl.DataFrame:
    d = POPULATIONS_DIR / run_id
    p = pl.read_parquet(
        d / "persons.parquet",
        columns=["person_id", "peso", "provincia", "ccaa", "tamano_municipio", "edad", "sexo"],
    )
    return pl.read_parquet(d / "politics.parquet").join(p, on="person_id")


def _dist(df: pl.DataFrame, col: str, peso: str) -> np.ndarray:
    d = dict(df.group_by(col).agg(pl.col(peso).sum()).iter_rows())
    return np.array([d.get(k, 0.0) for k in RV.OPCIONES], dtype=float)


def v_pol_recuerdo(s: pl.DataFrame) -> pl.DataFrame:
    c = load_config("thresholds.yaml").v_pol_recuerdo  # type: ignore[attr-defined]
    obj = RV.objetivos()
    e = s.filter(pl.col("recuerdo_voto_generales").is_in(RV.OPCIONES))
    filas = []
    for p in sorted(obj["provincia"].unique()):
        g = e.filter(pl.col("provincia") == p)
        od = dict(obj.filter(pl.col("provincia") == p).select("opcion", "p").iter_rows())
        b = np.array([od.get(k, 0.0) for k in RV.OPCIONES])
        a = _dist(g, "recuerdo_voto_generales", "peso")
        ref = M.tvd_ref(b, g.height)
        filas.append(
            {
                "provincia": p,
                "electores": g.height,
                "tvd": M.tvd(a, b),
                "umbral": c.factor_tvd_ref * ref + c.tolerancia,
            }
        )
    return pl.DataFrame(filas).with_columns((pl.col("tvd") <= pl.col("umbral")).alias("ok"))


def v_pol_reservada(s: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame]:
    c = load_config("thresholds.yaml").v_pol_reservada  # type: ignore[attr-defined]
    mun = RV.municipales().filter(pl.col("mitad") == 1)
    mun = mun.with_columns(pl.col("provincia").replace_strict(ccaa_de_provincia()).alias("ccaa"))
    e = s.filter(pl.col("recuerdo_voto_generales").is_in(RV.OPCIONES))
    i_abs = RV.OPCIONES.index("abstencion")
    rng = np.random.default_rng(0)

    def comparar(claves: list[str], umbral: float) -> pl.DataFrame:
        filas = []
        for k, g in e.group_by(claves):
            filtro = pl.lit(True)
            for col, val in zip(claves, k, strict=True):
                filtro = filtro & (pl.col(col) == val)
            o = mun.filter(filtro)
            if o.is_empty() or g.height < MIN_ELECTORES_CELDA:
                continue
            n_mun = o["municipio"].n_unique()
            od = dict(o.group_by("opcion").agg(pl.col("valor").sum()).iter_rows())
            b = np.array([od.get(x, 0.0) for x in RV.OPCIONES])
            a = _dist(g, "recuerdo_voto_generales", "peso")
            pa, pb = a / a.sum(), b / b.sum()
            r_tvd, r_part = ruido_municipios(o, b, rng)
            r_sint = M.tvd_ref(pb, g.height)
            filas.append(
                {
                    **dict(zip(claves, k, strict=True)),
                    "electores_sinteticos": g.height,
                    "censo_reservado": float(b.sum()),
                    "municipios": n_mun,
                    "evaluable": n_mun >= MIN_MUNICIPIOS_RESERVADOS,
                    "tvd": M.tvd(a, b),
                    "umbral": umbral + r_tvd + r_sint,
                    "error_participacion_pp": abs(pa[i_abs] - pb[i_abs]) * 100,
                    "umbral_participacion_pp": c.error_participacion_max * 100 + r_part,
                }
            )
        return pl.DataFrame(filas).with_columns(
            (
                (pl.col("tvd") <= pl.col("umbral"))
                & (pl.col("error_participacion_pp") <= pl.col("umbral_participacion_pp"))
            ).alias("ok")
        )

    return comparar(["tamano_municipio"], c.tvd_espana), comparar(
        ["ccaa", "tamano_municipio"], c.tvd_ccaa
    )


def ejecutar(run_id: str = NACIONAL) -> dict:
    DETALLE.mkdir(parents=True, exist_ok=True)
    s = sintetica(run_id)
    r1 = v_pol_recuerdo(s)
    r1.write_csv(DETALLE / f"{run_id}_v_pol_recuerdo.csv")
    esp, cc = v_pol_reservada(s)
    esp.write_csv(DETALLE / f"{run_id}_v_pol_reservada_espana.csv")
    cc.write_csv(DETALLE / f"{run_id}_v_pol_reservada_ccaa.csv")
    res = {
        "fecha": dt.date.today().isoformat(),
        "version_codigo": code_version(),
        "run_id": run_id,
        "g8b1": {
            "provincias": r1.height,
            "dentro": int(r1["ok"].sum()),
            "tvd_max": float(r1["tvd"].max()),
        },
        "g8b2": {
            "espana_celdas": esp.height,
            "espana_dentro": int(esp["ok"].sum()),
            "ccaa_celdas": cc.height,
            "ccaa_evaluables": int(cc["evaluable"].sum()),
            "ccaa_dentro": int(cc.filter(pl.col("evaluable"))["ok"].sum()),
            "ccaa_fuera": cc.filter(pl.col("evaluable") & ~pl.col("ok"))
            .select("ccaa", "tamano_municipio", "tvd", "error_participacion_pp")
            .to_dicts(),
            "tvd_media_ccaa": float(cc["tvd"].mean()),
            "error_participacion_max_pp": float(cc["error_participacion_pp"].max()),
        },
    }
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    return res


if __name__ == "__main__":
    print(json.dumps(ejecutar(), ensure_ascii=False, indent=1))
