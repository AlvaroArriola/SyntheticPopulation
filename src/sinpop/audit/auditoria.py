"""Auditoría de sesgos y minorías de una población (F7; docs/06 §3, docs/05 §6).

Para cada grupo de `configs/watchlist.yaml` que se puede medir en la población:

1. Representación (V-MINORIAS): proporción sintética dentro del universo del grupo frente a la
   oficial; ratio en [0,9; 1,1] si el recuento esperado es ≥ 200 y, si no, dentro del intervalo
   del 95 % de una muestra aleatoria simple. Si la referencia es una encuesta, también vale que la
   proporción sintética caiga en su IC 95 %.
2. Perfil interno (V-MINORIAS-PERFIL): sexo, edad, estudios y actividad dentro del grupo frente
   al oficial, si existe: TVD ≤ 0,08.
3. Concentración de donantes (V-CONCENTRACION): los 5 hogares donantes más usados pesan ≤ 20 %
   y hay al menos mín(50, tamaño / 3) donantes distintos.
4. Calidad de los atributos enriquecidos dentro del grupo y donantes no locales.
5. Semáforo: verde, ámbar (> 50 % de donantes no locales o > 30 % de atributos extrapolados)
   o rojo (falla alguna comprobación).

Además, para toda la población: V-DIVERSIDAD (`v_diversidad`) y V-RAREZA.
"""

from __future__ import annotations

import numpy as np
import polars as pl

from sinpop.audit import referencias as R
from sinpop.config import load_config
from sinpop.targets.edades import agrupar
from sinpop.validate import metrics as M
from sinpop.validate import poblacion as V

AGRUPACIONES = {"edad_actividad": "edad_actividad", "edad_nacionalidad": "edad_nacionalidad"}


def grupos() -> list:
    """Grupos de la lista de vigilancia más una entrada por nacionalidad principal."""
    from sinpop.targets import run

    gs = list(load_config("watchlist.yaml").grupos)  # type: ignore[attr-defined]
    top = run.leer("ES").filter(pl.col("objetivo") == "nacionalidad_top")
    for clave in top["clave"].to_list():
        nac = clave.split("=", 1)[1]
        if nac in ("espanola", "otras_extranjeras"):
            continue
        gs.append(
            type(gs[0])(
                id=f"nacionalidad_{nac}",
                nombre=f"Nacionalidad {nac}",
                definicion=f"nacionalidad_top = '{nac}'",
                referencia="censo_anual_micro_demograficas",
                motivo="Una de las 15 nacionalidades extranjeras más numerosas",
            )
        )
    return gs


def preparar(p: pl.DataFrame) -> pl.DataFrame:
    """Variables derivadas para comparar perfiles con las fuentes oficiales."""
    cortes = load_config("targets.yaml").agrupaciones_edad  # type: ignore[attr-defined]
    return p.with_columns(
        R._edad_grupos(pl.col("edad")),
        agrupar(pl.col("edad"), cortes["edad_actividad"], "edad_actividad"),
        agrupar(pl.col("edad"), cortes["edad_nacionalidad"], "edad_nacionalidad"),
    )


def _tvd_perfil(sub: pl.DataFrame, var: str, ref: pl.DataFrame) -> float | None:
    if var not in sub.columns or sub.is_empty():
        return None
    s = sub.filter(~pl.col(var).cast(pl.Utf8).is_in(["NC", "NS", "NP"]))
    if var == "edad_4":
        s = s.filter(pl.col(var).is_in(R.EDAD_4))
    if s.is_empty():
        return None
    a = R._perfil(s, var, "peso")
    j = a.join(ref, on="categoria", how="full", coalesce=True, suffix="_ref").fill_null(0.0)
    return float(M.tvd(j["p"], j["p_ref"]))


def auditar(p: pl.DataFrame, lineage: pl.DataFrame, territorio: str) -> pl.DataFrame:
    """Una fila por grupo vigilado con todas las comprobaciones y su semáforo."""
    cm = V.umbrales()["V-MINORIAS"]
    cc = V.umbrales()["V-CONCENTRACION"]
    tvd_max = V.umbrales()["V-MINORIAS-PERFIL"]["tvd_max"]
    p = preparar(p)
    donante = pl.concat_str(
        [pl.col("donante_household_id").cast(pl.Utf8), pl.col("donante_norden").cast(pl.Utf8)],
        separator="|",
    )
    lin = lineage.select(
        "person_id",
        pl.when(pl.col("tipo_unidad") == "colectivo")
        .then(donante)
        .otherwise(pl.col("donante_household_id").cast(pl.Utf8))
        .alias("_donante"),
        "local",
    )
    p = p.join(lin, on="person_id", how="left")
    calidad_cols = [
        c
        for c in p.columns
        if c.endswith("__calidad")
        and c.removesuffix("__calidad")
        in {
            "renta_hogar_decil",
            "tenencia_vivienda",
            "dificultad_fin_mes",
            "vehiculo_hogar",
            "salud_autopercibida",
            "discapacidad_limitacion",
            "privacion_material",
            "tipo_jornada",
            "sector_publico",
            "uso_internet",
            "compra_online",
            "teletrabajo",
        }
    ]
    filas = []
    for g in grupos():
        fila = {"grupo": g.id, "nombre": g.nombre, "capa": g.capa}
        if g.capa in ("politica", "opinion"):
            filas.append({**fila, "estado": "pendiente", "motivo": f"capa {g.capa} (F8)"})
            continue
        if not g.medible:
            filas.append({**fila, "estado": "no_medible", "motivo": g.motivo})
            continue
        try:
            cond, uni = pl.sql_expr(g.definicion), pl.sql_expr(g.universo)
        except Exception as exc:  # pragma: no cover - definición mal escrita
            raise ValueError(f"{g.id}: definición no válida: {exc}") from exc
        base = p.filter(uni)
        if g.unidad == "hogar":
            base = base.filter(pl.col("relacion_persona_ref") == "persona_referencia")
        n = float(base["peso"].sum())
        sub = base.filter(cond)
        obs = float(sub["peso"].sum())
        ref = R.referencia(g.id, territorio)
        fila |= {"universo": g.universo, "unidad": g.unidad, "n_universo": n, "observado": obs}
        fila["proporcion_sintetica"] = obs / n if n else None
        if ref is None:
            fila |= {"estado": "sin_referencia", "motivo": "sin cifra oficial para este territorio"}
        else:
            q = ref.proporcion
            esperado = q * n
            ratio = obs / esperado if esperado else None
            if esperado >= cm["recuento_esperado_min"]:
                ok = ratio is not None and cm["ratio"][0] <= ratio <= cm["ratio"][1]
            else:
                ok = abs(obs - esperado) <= 1.96 * float(np.sqrt(n * q * (1 - q)))
            if not ok and ref.ic is not None and n:
                ok = ref.ic[0] <= obs / n <= ref.ic[1]
            perf = {v: _tvd_perfil(sub, v, r) for v, r in ref.perfiles.items()}
            perf = {v: x for v, x in perf.items() if x is not None}
            fila |= {
                "proporcion_oficial": q,
                "ic_oficial": list(ref.ic) if ref.ic else None,
                "fuente": ref.fuente,
                "nota": ref.nota,
                "esperado": esperado,
                "ratio": ratio,
                "ok_representacion": bool(ok),
                "perfil_tvd": perf,
                "ok_perfil": all(x <= tvd_max for x in perf.values()),
            }
        # Concentración de donantes y calidad
        don = sub.group_by("_donante").agg(pl.col("peso").sum())
        top5 = float(don.sort("peso", descending=True).head(5)["peso"].sum() / obs) if obs else 0.0
        minimo = min(cc["donantes_distintos_min"], obs / cc["divisor_tamano_grupo"])
        fila |= {
            "donantes_distintos": don.height,
            "top5": top5,
            "ok_concentracion": top5 <= cc["top5_max"] and don.height >= minimo,
            "no_locales": float(1 - sub["local"].mean()) if sub.height else None,
        }
        if calidad_cols and sub.height:
            vals = sub.select(calidad_cols).unpivot()["value"]
            fila["extrapolada"] = float((vals == "extrapolada").mean())
            fila["modelada"] = float((vals == "modelada").mean())
        filas.append(fila)
    out = pl.DataFrame(filas, infer_schema_length=None)
    return out.with_columns(_semaforo().alias("semaforo"))


def _semaforo() -> pl.Expr:
    falla = (
        (pl.col("ok_representacion") == False)  # noqa: E712
        | (pl.col("ok_perfil") == False)  # noqa: E712
        | (pl.col("ok_concentracion") == False)  # noqa: E712
    )
    ambar = (pl.col("no_locales") > 0.5) | (pl.col("extrapolada").fill_null(0) > 0.3)
    return (
        pl.when(pl.col("estado").is_in(["pendiente", "no_medible"]))
        .then(pl.col("estado"))
        .when(falla)
        .then(pl.lit("rojo"))
        .when(ambar)
        .then(pl.lit("ambar"))
        .otherwise(pl.lit("verde"))
    )


# --------------------------------------------------------------------------- V-DIVERSIDAD

ATRIBUTOS_DIVERSIDAD = [
    "nacionalidad_grupo",
    "pais_nacimiento_grupo",
    "estado_civil",
    "nivel_estudios",
    "relacion_actividad",
    "ocupacion",
    "situacion_profesional",
    "tipo_hogar",
    "tamano_hogar",
    "grado_urbanizacion",
    "tamano_municipio",
]
GRUPO_DIVERSIDAD = ["edad_4", "sexo", "estudios_3", "ccaa"]


def _entropias(df: pl.DataFrame, atributo: str, peso: str) -> pl.DataFrame:
    g = (
        df.group_by([*GRUPO_DIVERSIDAD, atributo])
        .agg(pl.col(peso).sum().alias("w"))
        .with_columns((pl.col("w") / pl.col("w").sum().over(GRUPO_DIVERSIDAD)).alias("q"))
    )
    return g.group_by(GRUPO_DIVERSIDAD).agg((-(pl.col("q") * pl.col("q").log())).sum().alias("h"))


def v_diversidad(p: pl.DataFrame, referencia: pl.DataFrame, peso_ref: str = "w") -> pl.DataFrame:
    """Entropía de cada atributo dentro de los grupos edad_4 × sexo × estudios_3 × CCAA con al
    menos 100 personas, frente a la de los donantes ponderados de la calibración."""
    c = V.umbrales()["V-DIVERSIDAD"]
    adultos = p.filter(pl.col("edad_4").is_in(R.EDAD_4))
    ref = referencia.filter(pl.col("edad_4").is_in(R.EDAD_4))
    tam = adultos.group_by(GRUPO_DIVERSIDAD).agg(pl.col("peso").sum().alias("n"))
    tam = tam.filter(pl.col("n") >= c["tamano_grupo_min"])
    filas = []
    for a in ATRIBUTOS_DIVERSIDAD:
        if a not in p.columns or a not in referencia.columns:
            continue
        hs = _entropias(adultos, a, "peso").rename({"h": "h_sintetica"})
        hr = _entropias(ref, a, peso_ref).rename({"h": "h_referencia"})
        j = tam.join(hs, on=GRUPO_DIVERSIDAD).join(hr, on=GRUPO_DIVERSIDAD)
        j = j.filter(pl.col("h_referencia") > 0.05)  # atributos casi constantes en el grupo
        ok = j["h_sintetica"] >= c["ratio_entropia_min"] * j["h_referencia"]
        filas.append(
            {
                "atributo": a,
                "grupos": j.height,
                "proporcion_ok": float(ok.mean()) if j.height else None,
                "ratio_mediano": float((j["h_sintetica"] / j["h_referencia"]).median())
                if j.height
                else None,
                "ok": (float(ok.mean()) >= c["proporcion_grupos"]) if j.height else True,
            }
        )
    return pl.DataFrame(filas)
