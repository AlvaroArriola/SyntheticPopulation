"""Construye el paquete portable de predicción (D-076).

Se ejecuta donde están los datos. Para cada pregunta del banco ajusta, con sus encuestados
(españoles de 18+, como el estimador), los tres modelos que usa la predicción (sistema, B1 y voto)
sobre sus **propias** opciones y guarda solo agregados:

- coeficientes, término independiente, clases y categorías de cada predictor;
- distribución observada ponderada por opción (B0) y número de encuestados por opción;
- encuestados por nivel de cada subgrupo (para la señal de datos del modelo de confianza).

Añade el banco (enunciados públicos), los marcos de las poblaciones sintéticas listas (sin
variables de la ESS), la composición del CIS por territorio (agregada), las calibraciones, el
modelo de confianza, el banco de efectos de eventos y las fichas.

Comando: `python -m sinpop.paquete.exportar [destino] [--procesos N]`.
"""

from __future__ import annotations

import argparse
import gzip
import json
import multiprocessing
import shutil
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import polars as pl

from sinpop import REPO_ROOT, REPORTS_DIR

DESTINO = REPO_ROOT / "dist" / "paquete"
# columnas del marco que usa la predicción (perfil, valores, voto, subgrupos y pesos); ninguna de
# la ESS ni identificadores de hogares
COLUMNAS_MARCO = [
    "person_id",
    "sexo",
    "edad",
    "edad_grupo",
    "edad_4",
    "estudios_3",
    "actividad_3",
    "ccaa",
    "provincia",
    "tamano_municipio_cis",
    "religiosidad",
    "clase_subjetiva",
    "grupo_voto",
    "ideologia_bloque",
    "recuerdo_voto_generales_familia",
    "peso",
    "peso_es",
    "peso_cis",
]
SUBGRUPOS_N = [
    "edad_4",
    "sexo",
    "estudios_3",
    "ccaa",
    "provincia",
    "recuerdo_voto_generales_familia",
]


def _modelo_json(d: pl.DataFrame, columnas: list[str]) -> dict:
    from sinpop.opinion.valores import Modelo
    from sinpop.predict import estimador as E

    clases = sorted(d["valor"].unique().to_list())
    if len(clases) == 1:
        return {"constante": clases[0]}
    m = Modelo("valor", c=E.C_MODELO, columnas=E._disponibles(d, columnas)).ajustar(d)
    return {
        "columnas": m.columnas,
        "cats": {v: sorted(m.cats[v], key=m.cats[v].get) for v in m.columnas},
        "clases": [str(c) for c in m.lr.classes_],
        "coef": np.round(m.lr.coef_, 7).tolist(),
        "intercept": np.round(m.lr.intercept_, 7).tolist(),
    }


def _una(fila: dict) -> dict | None:
    from sinpop.predict import estimador as E

    ops = fila["opciones"]
    d = E.encuestados(fila["estudio"], fila["variable"], {o: o for o in ops})
    if d.height < 50:
        return None
    n_op = dict(d.group_by("valor").len().iter_rows())
    return {
        "id": fila["id"],
        "n": d.height,
        "n_opcion": {o: int(n_op.get(o, 0)) for o in ops},
        "b0": E._observada(d, ops).round(7).tolist(),
        "n_sub": {
            f"{g}={lv}": int(n)
            for g in SUBGRUPOS_N
            if g in d.columns
            for lv, n in d.group_by(g).len().iter_rows()
            if lv is not None
        },
        "modelos": {
            "sistema": _modelo_json(d, E.COLUMNAS_SISTEMA),
            "b1": _modelo_json(d, E.COLUMNAS_B1),
            "voto": _modelo_json(d, E.COLUMNAS_VOTO),
        },
    }


def _lote(filas: list[dict]) -> list[dict]:
    from threadpoolctl import threadpool_limits

    with threadpool_limits(1):
        return [x for x in map(_una, filas) if x is not None]


def modelos(destino: Path, procesos: int = 2) -> int:
    from sinpop.predict import banco as B

    filas = B.preguntas().to_dicts()
    trozos = [filas[i :: procesos * 8] for i in range(procesos * 8)]
    out = []
    # «spawn»: con «fork» los hilos de Polars del proceso padre dejan bloqueados a los hijos
    contexto = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(procesos, mp_context=contexto) as ex:
        for i, parte in enumerate(ex.map(_lote, trozos), 1):
            out += parte
            print(f"lote {i}/{len(trozos)}: {len(out)} preguntas", flush=True)
    out.sort(key=lambda x: x["id"])
    with gzip.open(destino / "modelos.jsonl.gz", "wt", encoding="utf-8") as f:
        for x in out:
            f.write(json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "\n")
    return len(out)


def poblaciones(destino: Path) -> list[str]:
    from sinpop.predict import atributos as AT
    from sinpop.predict import poblacion as P
    from sinpop.servicio.app import poblaciones as listar

    (destino / "marcos").mkdir(parents=True, exist_ok=True)
    (destino / "fichas").mkdir(parents=True, exist_ok=True)
    comp, hechas = {}, []
    for p in listar():
        if not p["lista"]:
            continue
        rid = p["run_id"]
        m = P.marco(rid).select([c for c in COLUMNAS_MARCO if c in P.marco(rid).columns])
        m.write_parquet(destino / "marcos" / f"{rid}.parquet", compression="zstd")
        (destino / "marcos" / f"{rid}.json").write_text(
            json.dumps(p, ensure_ascii=False, indent=1), "utf-8"
        )
        (destino / "atributos").mkdir(exist_ok=True)
        (destino / "atributos" / f"{rid}.json").write_text(
            json.dumps(AT.todas(rid), ensure_ascii=False, separators=(",", ":")), "utf-8"
        )
        f = REPORTS_DIR / rid / "ficha.md"
        if f.exists():
            shutil.copy(f, destino / "fichas" / f"{rid}.md")
        t = p["territorio"]
        comp[t] = P.composicion_cis(t) if t != "ES" else P.composicion_cis()
        hechas.append(rid)
        P.marco.cache_clear()
    (destino / "composicion_cis.json").write_text(json.dumps(comp, ensure_ascii=False), "utf-8")
    return hechas


def auxiliares(destino: Path) -> None:
    from sinpop.confidence import modelo as M
    from sinpop.predict import banco as B
    from sinpop.predict import estimador as E
    from sinpop.predict import salida as S
    from sinpop.temporal import eventos as EV

    B.preguntas().write_parquet(destino / "banco.parquet")
    shutil.copy(E.CALIBRACION, destino / "calibracion.json")
    if S.CALIBRACION_LLM.exists():
        shutil.copy(S.CALIBRACION_LLM, destino / "calibracion_llm.json")
    (destino / "confianza").mkdir(exist_ok=True)
    shutil.copy(M.DESTINO, destino / "confianza" / "modelo.pkl")
    if M.RECALIBRACION.exists():
        shutil.copy(M.RECALIBRACION, destino / "confianza" / "recalibracion.pkl")
    shutil.copy(EV.DESTINO, destino / "banco_efectos_eventos.parquet")


def construir(destino: Path = DESTINO, procesos: int = 2) -> dict:
    import datetime as dt

    import sklearn

    from sinpop.repro import code_version

    destino.mkdir(parents=True, exist_ok=True)
    auxiliares(destino)
    pobs = poblaciones(destino)
    n = modelos(destino, procesos)
    man = {
        "fecha": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "version_codigo": code_version(),
        "scikit_learn": sklearn.__version__,
        "preguntas_con_modelo": n,
        "poblaciones": pobs,
        "contenido": "modelos ajustados (coeficientes), distribuciones y recuentos agregados, "
        "banco de enunciados públicos, marcos de poblaciones sintéticas; sin microdatos (D-076)",
        "fuentes": "ver docs/guias/fuentes_y_citas.md",
        "aviso": "Resultados simulados con una población sintética: describen distribuciones de "
        "grupo, no a personas reales, y no sustituyen a una encuesta.",
    }
    (destino / "MANIFIESTO.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), "utf-8")
    return man


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("destino", nargs="?", default=str(DESTINO))
    a.add_argument("--procesos", type=int, default=2)
    a.add_argument("--solo", choices=["auxiliares", "poblaciones", "modelos"])
    args = a.parse_args()
    d = Path(args.destino)
    d.mkdir(parents=True, exist_ok=True)
    if args.solo == "auxiliares":
        auxiliares(d)
    elif args.solo == "poblaciones":
        print(poblaciones(d))
    elif args.solo == "modelos":
        print(modelos(d, args.procesos))
    else:
        print(json.dumps(construir(d, args.procesos), ensure_ascii=False, indent=1))
