"""Trayectorias de los indicadores de cada persona sintética (F8C, tarea 2) (D-068).

Para cada adulto y cada mes del periodo (`configs/temporal.yaml`), la probabilidad de cada
categoría sale del modelo con efectos de periodo (`temporal/modelo.py`) con su perfil, su grupo
de voto de 2023 (desde agosto de 2023; antes, «desconocido», como en los datos) y los niveles
suavizados del mes. La categoría de cada mes se obtiene con un **cuantil fijo por persona**
(u ~ U(0, 1), sorteado una vez con la semilla): la persona conserva su posición dentro de la
distribución de su tipo y solo cambia de categoría cuando la evolución de su grupo la mueve. Así
la trayectoria es coherente en el tiempo y su grupo reproduce la evolución observada.

Cada trayectoria es **modelada** (`docs/02` §6): no es la historia de una persona real. Las de
los extranjeros y los residentes en colectivos, fuera del universo del CIS, son `extrapolada`.
"""

from __future__ import annotations

import datetime as dt
import json

import numpy as np
import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

from sinpop import POPULATIONS_DIR, REPORTS_DIR
from sinpop.opinion.valores import perfil_sintetico
from sinpop.politics.run import semilla_capa
from sinpop.repro import code_version, make_rng, sha256_file
from sinpop.temporal import indicadores as T
from sinpop.temporal.modelo import NACIONAL, ModeloTemporal, _softmax

MES_RECUERDO = "2023-08"  # primer mes con recuerdo de las generales del 23/07/2023
ORDEN = {
    "ideologia": ["izquierda", "centro", "derecha", "NS_NC"],
}


def orden(indicador: str, clases: list[str]) -> list[str]:
    """Orden de las categorías para el cuantil fijo (ordinal cuando lo hay)."""
    c = T.config()["indicadores"][indicador]
    if "categorias" in c:
        o = list(c["categorias"])
    elif "menciones" in c:
        o = ["no", "si"]
    else:
        o = ORDEN.get(c.get("especial"), sorted(clases))
    return [x for x in o if x in clases] + [x for x in clases if x not in o]


def meses_salida() -> list[str]:
    m = T.meses()
    if T.config()["periodo"].get("frecuencia", "mensual") == "trimestral":
        return [x for x in m if int(x[5:]) % 3 == 0]
    return m


def perfil(run_id: str) -> pl.DataFrame:
    d = POPULATIONS_DIR / run_id
    persons = pl.read_parquet(d / "persons.parquet")
    pol = pl.read_parquet(
        d / "politics.parquet",
        columns=["person_id", "recuerdo_voto_generales", "recuerdo_voto_generales_ns_nc"],
    )
    return (
        perfil_sintetico(persons)
        .join(pol, on="person_id")
        .join(persons.select("person_id", "peso"), on="person_id")
        .with_columns(
            T._edad4(pl.col("edad")),
            T.grupo_voto(
                pl.col("recuerdo_voto_generales"), pl.col("recuerdo_voto_generales_ns_nc")
            ),
        )
        .sort("person_id")
    )


def construir(run_id: str) -> dict:
    p = perfil(run_id)
    meta_pob = json.loads((POPULATIONS_DIR / run_id / "metadata.json").read_text("utf-8"))
    semilla = semilla_capa(int(meta_pob["semilla"]), "trayectorias")
    salida = meses_salida()
    desconocido = p.with_columns(pl.lit(T.DESCONOCIDO).alias("grupo_voto"))
    fuera = (
        (p["nacionalidad_esp_ext"] != "espanola") | (p["tipo_residencia"] != "vivienda_familiar")
    ).to_numpy()
    universo = ~fuera
    w = p["peso"].to_numpy()
    codigos: dict[str, np.ndarray] = {}
    categorias: dict[str, list[str]] = {}
    series = []
    info = {}
    for ind in T.indicadores():
        d = T.datos(ind)
        m = ModeloTemporal(ind).ajustar(d, T.meses())
        cats = orden(ind, m.clases)
        perm = [m.clases.index(c) for c in cats]
        base = {
            True: np.log(np.maximum(m.perfil.probabilidades(p), 1e-12)),
            False: np.log(np.maximum(m.perfil.probabilidades(desconocido), 1e-12)),
        }
        u = make_rng(semilla_capa(semilla, ind)).random(p.height)
        cod = np.zeros((len(salida), p.height), dtype=np.uint8)
        for i, mes in enumerate(salida):
            conocido = mes >= MES_RECUERDO
            df = p if conocido else desconocido
            tm = np.full(p.height, m.meses.index(mes))
            z = base[conocido].copy()
            for c in m.componentes:
                lab = (
                    np.full(p.height, NACIONAL) if c.nombre == NACIONAL else df[c.nombre].to_numpy()
                )
                z += m._offset(c, lab, tm)
            q = _softmax(z)[:, perm]
            cod[i] = (q.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(cats) - 1)
            for j, cat in enumerate(cats):
                series.append(
                    {
                        "indicador": ind,
                        "mes": mes,
                        "valor": cat,
                        "p_sintetica": float(
                            np.average(cod[i][universo] == j, weights=w[universo])
                        ),
                    }
                )
        codigos[ind], categorias[ind] = cod, cats
        info[ind] = {
            "encuestados": d.height,
            "estudios": sorted(d["estudio"].unique()),
            "c_perfil": m.c,
            "varianza_paseo": {c.nombre: c.q for c in m.componentes},
            "categorias": cats,
        }
    destino = POPULATIONS_DIR / run_id / "trajectories.parquet"
    calidad = np.where(fuera, "extrapolada", "modelada")
    escritor = None
    for i, mes in enumerate(salida):
        cols = {
            "person_id": p["person_id"].to_arrow(),
            "mes": pa.array([mes] * p.height),
            **{ind: pa.array(np.array(categorias[ind])[codigos[ind][i]]) for ind in codigos},
            "calidad": pa.array(calidad),
        }
        tabla = pa.table(cols)
        if escritor is None:
            escritor = pq.ParquetWriter(destino, tabla.schema)
        escritor.write_table(tabla)
    assert escritor is not None
    escritor.close()
    s = pl.DataFrame(series)
    (REPORTS_DIR / "fase_08c").mkdir(parents=True, exist_ok=True)
    s.write_csv(REPORTS_DIR / "fase_08c" / f"{run_id}_series_sinteticas.csv")
    meta = {
        "run_id": run_id,
        "capa": "trayectorias",
        "periodo": T.config()["periodo"],
        "meses": salida,
        "semilla_poblacion": meta_pob["semilla"],
        "semilla_capa": semilla,
        "version_codigo": code_version(),
        "fecha": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "calidad": "modelada (trayectoria simulada, no la historia de una persona real); "
        "extrapolada fuera del universo del CIS (extranjeros y colectivos)",
        "fuentes": {
            "cis_barometros": "CIS, barómetros mensuales y estudios nacionales 2023-2026 (citar "
            "el número de estudio y al CIS)",
        },
        "indicadores": info,
        "personas": p.height,
        "filas": p.height * len(salida),
        "sha256": sha256_file(destino),
    }
    (POPULATIONS_DIR / run_id / "trajectories_metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1, default=str), "utf-8"
    )
    return meta
