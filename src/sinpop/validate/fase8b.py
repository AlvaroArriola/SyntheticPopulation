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

- G8B.3 V-POL-PERFIL: composición de cada electorado (edad en cuatro grupos, sexo, estudios y
  tamaño de municipio) frente al postelectoral de las generales de 2023 del CIS (estudio 3420),
  ponderado y reponderado a la composición edad × sexo × estudios del universo (su peso solo
  corrige la comunidad y su muestra tiene un 48 % de titulados superiores; D-067); TVD ≤ 0,08 en
  cada variable de cada electorado con al menos 300 casos.
- G8B.4 V-POL-COHERENCIA: autoubicación (1-10, sin NS/NC) dentro de cada electorado frente a
  todos los estudios del CIS con recuerdo de 2023: media a ± 0,3 y razón de desviaciones en
  [0,8; 1,2].
- G8B.6: ninguna variable política en la población base ni en la capa de opinión, que además no
  cambian (su sha256 es el de su metadata).
- G8B.7 V-POL-SESGO: (1) diversidad no política de cada electorado (edad, sexo, estudios,
  tamaño, comunidad, religiosidad, clase subjetiva): razón de entropías sintética / CIS ≥ 0,9;
  (2) contrafactual: con los mismos perfiles y solo el recuerdo cambiado, la diferencia de
  ideología media entre cada electorado y el socialdemócrata se compara con la de los datos
  dentro de celdas edad × sexo × estudios × religiosidad (el modelo descuenta la religiosidad;
  tolerancia ± 0,3 puntos, la de V-POL-COHERENCIA; D-067).
- G8B.8: nadie sin derecho a voto en las generales de 2023 tiene recuerdo de esa elección.

Las comparaciones con el CIS se hacen sobre su universo: personas de nacionalidad española en
viviendas familiares.

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
from sinpop.opinion.valores import TAMANO_A_CIS
from sinpop.politics import ideologia as ID
from sinpop.politics import recuerdo as RV
from sinpop.repro import code_version, sha256_file
from sinpop.validate import metrics as M
from sinpop.validate.layers import layer_violations

NACIONAL = "2026-01-01_ES_1000000_s1"
RESUMEN = REPORTS_DIR / "fase_08b_validacion.json"
DETALLE = REPORTS_DIR / "fase_08b"
MIN_ELECTORES_CELDA = 500  # electores sintéticos para evaluar una celda
MIN_MUNICIPIOS_RESERVADOS = 5  # una celda con menos no representa su comunidad × tamaño
REPLICAS = 200
POSTELECTORAL = "3420"
MIN_CASOS_PERFIL = 300
TVD_PERFIL = 0.08
TOL_MEDIA = 0.3
RAZON_SD = (0.8, 1.2)
RAZON_ENTROPIA = 0.9
REFERENCIA_CF = "socialdemocrata"
MUESTRA_CF = 20000
VARIABLES_PERFIL = ["edad_4", "sexo", "estudios_3", "tamano_municipio_cis"]
VARIABLES_DIVERSIDAD = VARIABLES_PERFIL + ["ccaa", "religiosidad", "clase_subjetiva"]


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


def _edad4(e: pl.Expr) -> pl.Expr:
    return (
        pl.when(e < 35)
        .then(pl.lit("18-34"))
        .when(e < 50)
        .then(pl.lit("35-49"))
        .when(e < 65)
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
        .alias("edad_4")
    )


def sintetica(run_id: str) -> pl.DataFrame:
    d = POPULATIONS_DIR / run_id
    p = pl.read_parquet(
        d / "persons.parquet",
        columns=[
            "person_id",
            "peso",
            "provincia",
            "ccaa",
            "tamano_municipio",
            "edad",
            "sexo",
            "estudios_3",
            "nacionalidad_esp_ext",
            "tipo_residencia",
        ],
    ).with_columns(
        _edad4(pl.col("edad")),
        pl.col("tamano_municipio")
        .replace_strict(TAMANO_A_CIS, default=None)
        .alias("tamano_municipio_cis"),
    )
    o = pl.read_parquet(
        d / "opinion.parquet", columns=["person_id", "religiosidad", "clase_subjetiva"]
    )
    return pl.read_parquet(d / "politics.parquet").join(p, on="person_id").join(o, on="person_id")


def universo_cis(s: pl.DataFrame) -> pl.DataFrame:
    """Electores sintéticos en el universo del CIS (españoles en viviendas familiares)."""
    return s.filter(
        pl.col("recuerdo_voto_generales").is_in(RV.OPCIONES)
        & (pl.col("nacionalidad_esp_ext") == "espanola")
        & (pl.col("tipo_residencia") == "vivienda_familiar")
    )


def _reparto(df: pl.DataFrame, col: str, peso: str = "peso") -> dict:
    t = df.filter(pl.col(col).is_not_null()).group_by(col).agg(pl.col(peso).sum())
    tot = t[peso].sum()
    return {k: v / tot for k, v in t.iter_rows()}


def _tvd_dict(a: dict, b: dict) -> float:
    return 0.5 * sum(abs(a.get(k, 0.0) - b.get(k, 0.0)) for k in set(a) | set(b))


def _entropia(p: dict) -> float:
    x = np.array([v for v in p.values() if v > 0])
    return float(-(x * np.log(x)).sum())


def reponderar_postelectoral(cis: pl.DataFrame, e: pl.DataFrame) -> pl.DataFrame:
    """El 3420 solo se pondera por comunidad (ficha técnica) y su muestra telefónica tiene un
    48 % de titulados superiores frente al 38 % de la población (y del CIS apilado): se lleva a la
    composición edad × sexo × estudios del universo sintético antes de comparar electorados.
    El reparto del voto entre celdas no se toca (D-067)."""
    celdas = ["edad_4", "sexo", "estudios_3"]
    pc = cis.group_by(celdas).agg(pl.col("peso").sum().alias("wc"))
    ps = e.group_by(celdas).agg(pl.col("peso").sum().alias("ws"))
    f = pc.join(ps, on=celdas).with_columns(
        (pl.col("ws") / pl.col("ws").sum() / (pl.col("wc") / pl.col("wc").sum())).alias("f")
    )
    return cis.join(f.select(*celdas, "f"), on=celdas).with_columns(pl.col("peso") * pl.col("f"))


def v_pol_perfil(s: pl.DataFrame) -> pl.DataFrame:
    e = universo_cis(s)
    bruto = (
        RV.datos().filter(pl.col("estudio") == POSTELECTORAL).with_columns(_edad4(pl.col("edad")))
    )
    cis = reponderar_postelectoral(bruto, e)
    filas = []
    for f in RV.OPCIONES:
        c = cis.filter(pl.col("recuerdo") == f)
        cb = bruto.filter(pl.col("recuerdo") == f)
        g = e.filter(pl.col("recuerdo_voto_generales") == f)
        for v in VARIABLES_PERFIL:
            filas.append(
                {
                    "electorado": f,
                    "variable": v,
                    "casos_cis": c.height,
                    "evaluable": c.height >= MIN_CASOS_PERFIL,
                    "tvd": _tvd_dict(_reparto(g, v), _reparto(c, v)),
                    "tvd_sin_reponderar": _tvd_dict(_reparto(g, v), _reparto(cb, v)),
                }
            )
    return pl.DataFrame(filas).with_columns((pl.col("tvd") <= TVD_PERFIL).alias("ok"))


def _media_sd(x: np.ndarray, w: np.ndarray) -> tuple[float, float]:
    m = float(np.average(x, weights=w))
    return m, float(np.sqrt(np.average((x - m) ** 2, weights=w)))


def v_pol_coherencia(s: pl.DataFrame) -> pl.DataFrame:
    cis = ID.datos()
    e = universo_cis(s)
    filas = []
    for f in RV.OPCIONES:
        c = cis.filter(pl.col("recuerdo") == f)
        g = e.filter(pl.col("recuerdo_voto_generales") == f)
        cn = c.filter(~pl.col("ideologia").is_in(["NS", "NC"]))
        gn = g.filter(~pl.col("ideologia_autoubicacion").is_in(["NS", "NC"]))
        mc, sc = _media_sd(cn["ideologia"].cast(pl.Float64).to_numpy(), cn["peso"].to_numpy())
        ms, ss = _media_sd(
            gn["ideologia_autoubicacion"].cast(pl.Float64).to_numpy(), gn["peso"].to_numpy()
        )
        filas.append(
            {
                "electorado": f,
                "casos_cis": c.height,
                "media_cis": mc,
                "media_sintetica": ms,
                "sd_cis": sc,
                "sd_sintetica": ss,
                "razon_sd": ss / sc,
                "ns_nc_cis": 1 - cn["peso"].sum() / c["peso"].sum(),
                "ns_nc_sintetica": 1 - gn["peso"].sum() / g["peso"].sum(),
            }
        )
    return pl.DataFrame(filas).with_columns(
        (
            ((pl.col("media_sintetica") - pl.col("media_cis")).abs() <= TOL_MEDIA)
            & pl.col("razon_sd").is_between(*RAZON_SD)
        ).alias("ok")
    )


def v_pol_capas(run_id: str, s_cols: list[str]) -> dict:
    d = POPULATIONS_DIR / run_id
    politicas = set(pl.read_parquet_schema(d / "politics.parquet")) - {
        "person_id",
        "fecha_referencia",
    }
    base = list(pl.read_parquet_schema(d / "persons.parquet"))
    opinion = list(pl.read_parquet_schema(d / "opinion.parquet"))
    meta = json.loads((d / "metadata.json").read_text("utf-8"))
    meta_op = json.loads((d / "opinion_metadata.json").read_text("utf-8"))
    res = {
        "base_con_politica": sorted(set(base) & politicas) + layer_violations(base),
        "opinion_con_politica": sorted(set(opinion) & politicas),
        "persons_sin_cambios": sha256_file(d / "persons.parquet")
        == meta["sha256"]["persons.parquet"],
        "opinion_sin_cambios": sha256_file(d / "opinion.parquet") == meta_op["sha256"],
    }
    res["ok"] = (
        not res["base_con_politica"]
        and not res["opinion_con_politica"]
        and res["persons_sin_cambios"]
        and res["opinion_sin_cambios"]
    )
    return res


def v_pol_diversidad(s: pl.DataFrame) -> pl.DataFrame:
    cis = RV.datos().with_columns(_edad4(pl.col("edad")))
    e = universo_cis(s)
    filas = []
    for f in RV.OPCIONES:
        c = cis.filter(pl.col("recuerdo") == f)
        g = e.filter(pl.col("recuerdo_voto_generales") == f)
        for v in VARIABLES_DIVERSIDAD:
            hc, hs = _entropia(_reparto(c, v)), _entropia(_reparto(g, v))
            filas.append(
                {
                    "electorado": f,
                    "variable": v,
                    "entropia_cis": hc,
                    "entropia_sintetica": hs,
                    "razon": hs / hc,
                }
            )
    return pl.DataFrame(filas).with_columns((pl.col("razon") >= RAZON_ENTROPIA).alias("ok"))


def _ideologia_esperada(pr: np.ndarray, clases: list[str]) -> np.ndarray:
    num = [i for i, k in enumerate(clases) if k.isdigit()]
    v = np.array([float(clases[i]) for i in num])
    p = pr[:, num]
    return (p * v).sum(1) / p.sum(1)


def v_pol_contrafactual(run_id: str, s: pl.DataFrame) -> pl.DataFrame:
    """Mismos perfiles, recuerdo cambiado: diferencia de ideología media con el electorado de
    referencia en el modelo frente a la de los datos dentro de celdas edad × sexo × estudios ×
    religiosidad."""
    from sinpop.opinion.valores import Modelo, perfil_sintetico

    d = POPULATIONS_DIR / run_id
    persons = pl.read_parquet(d / "persons.parquet")
    opinion = pl.read_parquet(
        d / "opinion.parquet", columns=["person_id", "religiosidad", "clase_subjetiva"]
    )
    ids = universo_cis(s)["person_id"]
    perfil = (
        perfil_sintetico(persons.filter(pl.col("person_id").is_in(ids.implode())))
        .join(opinion, on="person_id")
        .sort("person_id")
    )
    perfil = perfil.sample(min(MUESTRA_CF, perfil.height), seed=0).with_columns(
        _edad4(pl.col("edad"))
    )
    datos = ID.datos()
    m = Modelo("ideologia", columnas=ID.COLUMNAS_IDEOLOGIA).ajustar(datos)
    familias = [f for f in RV.OPCIONES]
    cf = {
        f: float(
            _ideologia_esperada(
                m.probabilidades(perfil.with_columns(pl.lit(f).alias("recuerdo"))), m.clases
            ).mean()
        )
        for f in familias
    }
    # datos: diferencia dentro de cada celda, promediada con el reparto de celdas de los perfiles
    celdas = ["edad_4", "sexo", "estudios_3", "religiosidad"]
    reparto = perfil.group_by(celdas).len().with_columns(pl.col("len") / pl.col("len").sum())
    num = (
        datos.with_columns(_edad4(pl.col("edad")))
        .filter(~pl.col("ideologia").is_in(["NS", "NC"]))
        .with_columns(pl.col("ideologia").cast(pl.Float64))
        .group_by([*celdas, "recuerdo"])
        .agg(((pl.col("ideologia") * pl.col("peso")).sum() / pl.col("peso").sum()).alias("m"))
    )
    ref = num.filter(pl.col("recuerdo") == REFERENCIA_CF).select(*celdas, pl.col("m").alias("r"))
    filas = []
    for f in familias:
        x = (
            num.filter(pl.col("recuerdo") == f)
            .join(ref, on=celdas)
            .join(reparto, on=celdas)
            .with_columns(pl.col("len") / pl.col("len").sum())
        )
        dif_datos = float(((x["m"] - x["r"]) * x["len"]).sum())
        dif_cf = cf[f] - cf[REFERENCIA_CF]
        filas.append(
            {
                "electorado": f,
                "diferencia_contrafactual": dif_cf,
                "diferencia_datos": dif_datos,
                "celdas": x.height,
            }
        )
    return pl.DataFrame(filas).with_columns(
        (
            (pl.col("diferencia_contrafactual") - pl.col("diferencia_datos")).abs() <= TOL_MEDIA
        ).alias("ok")
    )


def v_pol_derecho(s: pl.DataFrame) -> dict:
    sin = s.filter(~pl.col("derecho_voto_generales_2023"))
    con_recuerdo = sin.filter(
        pl.col("recuerdo_voto_generales").is_in(RV.OPCIONES)
        | pl.col("recuerdo_voto_generales_ns_nc").fill_null(False)
    ).height
    con = s.filter(pl.col("derecho_voto_generales_2023"))
    sin_dato = con.filter(~pl.col("recuerdo_voto_generales").is_in(RV.OPCIONES)).height
    return {
        "sin_derecho": sin.height,
        "sin_derecho_con_recuerdo": con_recuerdo,
        "con_derecho_sin_recuerdo": sin_dato,
        "ok": con_recuerdo == 0 and sin_dato == 0,
    }


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
    perfil = v_pol_perfil(s)
    perfil.write_csv(DETALLE / f"{run_id}_v_pol_perfil.csv")
    coh = v_pol_coherencia(s)
    coh.write_csv(DETALLE / f"{run_id}_v_pol_coherencia.csv")
    div = v_pol_diversidad(s)
    div.write_csv(DETALLE / f"{run_id}_v_pol_diversidad.csv")
    cf = v_pol_contrafactual(run_id, s)
    cf.write_csv(DETALLE / f"{run_id}_v_pol_contrafactual.csv")
    perfil_ev = perfil.filter(pl.col("evaluable"))
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
        "g8b3": {
            "estudio_cis": POSTELECTORAL,
            "comparaciones": perfil_ev.height,
            "dentro": int(perfil_ev["ok"].sum()),
            "fuera": perfil_ev.filter(~pl.col("ok"))
            .select("electorado", "variable", "tvd")
            .to_dicts(),
            "tvd_max": float(perfil_ev["tvd"].max()),
        },
        "g8b4": {
            "electorados": coh.height,
            "dentro": int(coh["ok"].sum()),
            "fuera": coh.filter(~pl.col("ok"))
            .select("electorado", "media_cis", "media_sintetica", "razon_sd")
            .to_dicts(),
        },
        "g8b6": v_pol_capas(run_id, s.columns),
        "g8b7": {
            "diversidad_comparaciones": div.height,
            "diversidad_dentro": int(div["ok"].sum()),
            "diversidad_razon_min": float(div["razon"].min()),
            "diversidad_fuera": div.filter(~pl.col("ok"))
            .select("electorado", "variable", "razon")
            .to_dicts(),
            "contrafactual_dentro": int(cf["ok"].sum()),
            "contrafactual_electorados": cf.height,
            "contrafactual_fuera": cf.filter(~pl.col("ok")).to_dicts(),
        },
        "g8b8": v_pol_derecho(s),
    }
    RESUMEN.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    return res


if __name__ == "__main__":
    print(json.dumps(ejecutar(), ensure_ascii=False, indent=1))
