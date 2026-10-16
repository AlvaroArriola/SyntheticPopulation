"""Generación de una población sintética (F4; docs/03 §2.1 y §4; `sinpop build`).

1. Unidades donantes: hogares del Censo 2021 y módulo de colectivos (`donantes`).
2. Calibración por bloques (`pesos`), guardada en `data/processed/calibracion/`: no depende del
   tamaño ni de la semilla, así que se reutiliza mientras no cambien sus entradas.
3. Integerización TRS y, si se pide, sobremuestreo (`muestreo`).
4. Salidas en `data/populations/<run_id>/`: `persons.parquet`, `households.parquet`,
   `lineage.parquet` (referencia al donante, aparte) y `metadata.json`.
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import numpy as np
import polars as pl

from sinpop import CONFIGS_DIR, INTERIM_DIR, POPULATIONS_DIR, PROCESSED_DIR
from sinpop.repro import code_version, make_rng, sha256_file
from sinpop.synth import donantes as D
from sinpop.synth import muestreo as S
from sinpop.synth import pesos as P
from sinpop.validate.poblacion import frecuencias_blandas

CALIBRACION_DIR = PROCESSED_DIR / "calibracion"
METODO = "logit"  # D-038: elegido frente al raking con la comparación de reports/fase_04.md

CALIDADES = pl.Enum(["observada", "emparejada", "modelada", "extrapolada"])

COLUMNAS_PERSONA = [
    "edad",
    "edad_5",
    "edad_4",
    "sexo",
    "nacionalidad_grupo",
    "nacionalidad_esp_ext",
    "nacionalidad_top",
    "pais_nacimiento_grupo",
    "anio_llegada_espana",
    "estado_civil",
    "nivel_estudios",
    "estudios_3",
    "relacion_actividad",
    "ocupacion",
    "sector_actividad",
    "situacion_profesional",
    "tipo_residencia",
    "relacion_persona_ref",
    "tipo_hogar",
    "tamano_hogar",
    "tamano_hogar_4",
    "n_personas_hogar",
    "n_menores_hogar",
    "n_mayores_65_hogar",
    "n_mayores_80_hogar",
    "ccaa",
    "provincia",
    "municipio",
    "tamano_municipio",
    "grado_urbanizacion",
]
COLUMNAS_HOGAR = [
    "tamano_hogar",
    "tamano_hogar_4",
    "tipo_hogar",
    "n_personas_hogar",
    "n_menores_hogar",
    "n_mayores_65_hogar",
    "n_mayores_80_hogar",
    "tenencia_censo",
    "ccaa",
    "provincia",
    "municipio",
    "tamano_municipio",
    "grado_urbanizacion",
]
# En los colectivos solo proceden de la cifra oficial la edad, el sexo, el territorio y el tipo
# de residencia; el resto se toma de una persona parecida (D-021: `modelada`).
OBSERVADAS_COLECTIVO = {"edad", "edad_5", "edad_4", "sexo", "ccaa", "provincia", "tipo_residencia"}
TERRITORIALES = {"ccaa", "provincia", "municipio", "tamano_municipio", "grado_urbanizacion"}


def unidades_todas() -> D.Unidades:
    from sinpop.targets.build import provincias_de

    ph = D.hogares()
    pc = D.colectivos(D.objetivos_colectivos(provincias_de("ES")), ph)
    return D.unidades(ph, pc)


def _entradas_calibracion(territorio: str) -> dict[str, str]:
    from sinpop.targets import run

    meta_i = json.loads((INTERIM_DIR / "metadata.json").read_text(encoding="utf-8"))["salidas"]
    meta_t = json.loads((run.DESTINO / "metadata.json").read_text(encoding="utf-8"))["salidas"]
    ent = {"interim/censo2021_personas.parquet": meta_i["censo2021_personas"]["sha256"]}
    ent |= {f"targets/{i['fichero']}": i["sha256"] for i in meta_t.values()}
    ent |= {
        f"configs/{c}": sha256_file(CONFIGS_DIR / c) for c in ("targets.yaml", "variables.yaml")
    }
    for f in sorted(Path(__file__).parent.glob("*.py")):
        if f.name in ("donantes.py", "pesos.py", "calibracion.py"):
            ent[f"codigo/{f.name}"] = sha256_file(f)
    ent["territorio"] = territorio
    return ent


def calibracion(
    u: D.Unidades, territorio: str, metodo: str = METODO, forzar: bool = False
) -> tuple[P.Calibrado, dict]:
    """Calibración del territorio, desde la caché si sus entradas no han cambiado."""
    from sinpop.targets.run import nombre_fichero

    CALIBRACION_DIR.mkdir(parents=True, exist_ok=True)
    base = CALIBRACION_DIR / f"{nombre_fichero(territorio)}_{metodo}"
    ent = _entradas_calibracion(territorio)
    meta_p = base.with_suffix(".json")
    if not forzar and meta_p.exists():
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
        if meta.get("entradas") == ent:
            cal = P.Calibrado(
                unidades=pl.read_parquet(base.with_suffix(".parquet")),
                diagnosticos=meta["diagnosticos"],
                ceros=pl.DataFrame(meta["ceros"]),
                ampliaciones=pl.DataFrame(meta["ampliaciones"]),
                fusiones=pl.DataFrame(meta["fusiones"]),
            )
            return cal, meta
    cal = P.calibrar(u, territorio, metodo)
    cal.unidades.write_parquet(base.with_suffix(".parquet"), compression="zstd", statistics=False)
    meta = {
        "territorio": territorio,
        "metodo": metodo,
        "entradas": ent,
        "sha256": sha256_file(base.with_suffix(".parquet")),
        "diagnosticos": cal.diagnosticos,
        "ceros": cal.ceros.to_dicts(),
        "ampliaciones": cal.ampliaciones.to_dicts(),
        "fusiones": cal.fusiones.to_dicts(),
        "version_codigo": code_version(),
        "fecha": dt.date.today().isoformat(),
    }
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    return cal, meta


def _orden(p: pl.DataFrame) -> pl.DataFrame:
    """Una fila por unidad calibrada con sus claves de estratificación implícita."""
    ref = p.filter(pl.col("relacion_persona_ref").is_in(["persona_referencia", "NP"]))
    return (
        ref.group_by("unidad_cal")
        .agg(
            pl.col(
                "bloque",
                "provincia",
                "grado_urbanizacion",
                "tamano_municipio",
                "tipo_residencia",
                "tipo_hogar",
                "tamano_hogar",
                "nacionalidad_top",
                "edad_5",
                "w",
                "unidad",
                "local",
            ).first()
        )
        .join(p.group_by("unidad_cal").agg(pl.len().alias("m")), on="unidad_cal")
        .sort(
            "bloque",
            "provincia",
            "grado_urbanizacion",
            "tamano_municipio",
            "tipo_residencia",
            "tipo_hogar",
            "tamano_hogar",
            "nacionalidad_top",
            "edad_5",
            "unidad_cal",
        )
    )


def _matriz_equilibrado(p: pl.DataFrame, o: pl.DataFrame, territorio: str):
    """Unidades (en el orden de `o`) × celdas calibradas por bloque (bloque, objetivo, clave)."""
    from scipy import sparse

    from sinpop.targets import run

    obj = D.objetivos_calibrables(run.leer(territorio))
    trozos, base = [], 0
    for objetivo, unidad_obj, universo in (
        obj.select("objetivo", "unidad", "universo").unique(maintain_order=True).iter_rows()
    ):
        vs = D.variables_de(objetivo)
        k = (
            D.en_universo(p, universo, unidad_obj, [*vs, "unidad_cal", "bloque"])
            .group_by("unidad_cal", "bloque", D.clave(vs).alias("clave"))
            .agg(pl.len().alias("x"))
            .with_columns(
                (pl.struct("bloque", "clave").rank("dense").cast(pl.Int64) - 1 + base).alias("j")
            )
            .select("unidad_cal", "j", "x")
        )
        base = int(k["j"].max()) + 1
        trozos.append(k)
    fila = o.select("unidad_cal").with_row_index("i")
    t = pl.concat(trozos).join(fila, on="unidad_cal")
    return sparse.csr_matrix(
        (t["x"].to_numpy().astype(float), (t["i"].to_numpy(), t["j"].to_numpy())),
        shape=(o.height, base),
    )


def run_id(territorio: str, n: int, semilla: int, sobremuestreo: str | None) -> str:
    from sinpop.config import load_config
    from sinpop.targets.run import nombre_fichero

    fecha = str(load_config("targets.yaml").fecha_referencia)  # type: ignore[attr-defined]
    rid = f"{fecha}_{nombre_fichero(territorio)}_{n}_s{semilla}"
    if sobremuestreo:
        import hashlib

        rid += "_sm" + hashlib.sha256(sobremuestreo.encode()).hexdigest()[:6]
    return rid


def construir(
    territorio: str,
    n: int,
    semilla: int,
    sobremuestreo: str | None = None,
    metodo: str = METODO,
    u: D.Unidades | None = None,
    destino: Path = POPULATIONS_DIR,
) -> dict:
    if not isinstance(semilla, int) or n <= 0:
        raise ValueError("hacen falta un tamaño positivo y una semilla entera")
    if territorio.startswith("MUNIS:"):
        raise NotImplementedError("los territorios por municipios se generan en F5")
    u = u if u is not None else unidades_todas()
    cal, meta_cal = calibracion(u, territorio, metodo)
    p = P.personas_ponderadas(u, cal)
    o = _orden(p)
    w, m = o["w"].to_numpy(), o["m"].to_numpy().astype(float)
    e = S.copias_esperadas(w, m, n)
    sm = S.parse_sobremuestreo(sobremuestreo)
    info_sm = None
    f = np.ones_like(e)
    if sm is not None:
        g = (
            p.with_columns(sm.condicion(p.schema).alias("_g"))
            .group_by("unidad_cal")
            .agg(pl.col("_g").sum())
        )
        g = o.select("unidad_cal").join(g, on="unidad_cal", how="left").fill_null(0)
        f, info_sm = S.factores_sobremuestreo(e, m, g["_g"].to_numpy(), n, sm.minimo)
        e = e * f
    rng = make_rng(semilla)
    copias = S.trs(e, int(rng.integers(0, 2**31)))
    # Equilibrado: los recuentos de la muestra en las celdas calibradas de cada bloque se
    # acercan a los esperados sin cambiar el tamaño (D-038).
    bloques_idx = o["bloque"].rank("dense").cast(pl.Int64).to_numpy()
    copias, info_eq = S.equilibrar(
        copias,
        e,
        m,
        bloques_idx,
        _matriz_equilibrado(p, o, territorio),
        int(rng.integers(0, 2**31)),
    )
    o = o.with_columns(pl.Series("copias", copias), pl.Series("peso", 1.0 / f))
    sel = o.filter(pl.col("copias") > 0).select("unidad_cal", "copias", "peso")
    sel = (
        sel.with_columns(pl.col("copias").cast(pl.Int64))
        .with_columns(pl.int_ranges(0, pl.col("copias")).alias("copia"))
        .explode("copia")
    )
    # Orden final aleatorio (con la semilla) para que los identificadores no reflejen el orden
    # de estratificación ni el de los donantes.
    perm = rng.permutation(sel.height)
    sel = sel.with_columns(pl.Series("k", perm)).sort("k")
    pers = (
        sel.join(p, on="unidad_cal", how="left")
        .sort("k", "norden")
        .with_columns(pl.int_range(pl.len()).alias("_pi"))
    )
    familiar = pl.col("tipo_residencia") == "vivienda_familiar"
    pers = pers.with_columns(
        pl.when(familiar)
        .then(pl.format("H{}", pl.col("k").cast(pl.Utf8).str.zfill(8)))
        .alias("household_id_nuevo"),
        pl.format("P{}", pl.col("_pi").cast(pl.Utf8).str.zfill(9)).alias("person_id"),
        # Colectivos y unidades trasladadas: el municipio del donante no es el suyo.
        pl.when(familiar & pl.col("local")).then(pl.col("municipio")).alias("municipio"),
    )
    # Unidades trasladadas desde otra provincia (ampliación de donantes): su tamaño de municipio
    # era el de origen y puede no existir en la de destino. Se toma la clase más frecuente entre
    # los donantes locales de la provincia con el mismo grado de urbanización (`modelada`).
    clase = (
        p.filter(pl.col("local"))
        .group_by("provincia", "grado_urbanizacion", "tamano_municipio")
        .agg(pl.col("w").sum())
        .sort("w", "tamano_municipio", descending=True)
        .unique(["provincia", "grado_urbanizacion"], keep="first")
        .select("provincia", "grado_urbanizacion", pl.col("tamano_municipio").alias("_tm"))
    )
    pers = (
        pers.join(clase, on=["provincia", "grado_urbanizacion"], how="left")
        .with_columns(
            pl.when(pl.col("local"))
            .then(pl.col("tamano_municipio"))
            .otherwise(pl.coalesce("_tm", "tamano_municipio"))
            .alias("tamano_municipio")
        )
        .drop("_tm")
        .sort("k", "norden")
    )
    calidad = []
    for c in COLUMNAS_PERSONA:
        modelada = (~familiar & pl.lit(c not in OBSERVADAS_COLECTIVO)) | (
            ~pl.col("local") & pl.lit(c in TERRITORIALES)
        )
        calidad.append(
            pl.when(modelada)
            .then(pl.lit("modelada"))
            .otherwise(pl.lit("observada"))
            .cast(CALIDADES)
            .alias(f"{c}__calidad")
        )
    persons = pers.select(
        "person_id",
        pl.col("household_id_nuevo").alias("household_id"),
        "peso",
        "es_adulto",
        *COLUMNAS_PERSONA,
        *calidad,
    )
    households = (
        pers.filter(familiar & (pl.col("relacion_persona_ref") == "persona_referencia"))
        .select(pl.col("household_id_nuevo").alias("household_id"), *COLUMNAS_HOGAR, "peso")
        .sort("household_id")
    )
    lineage = pers.select(
        "person_id",
        pl.col("household_id_nuevo").alias("household_id"),
        pl.col("household_id").alias("donante_household_id"),
        pl.col("norden").alias("donante_norden"),
        "tipo_unidad",
        "bloque",
        "local",
        "colectivo_donante_nivel",
    )
    from sinpop.targets.run import nombre_fichero

    rid = run_id(territorio, n, semilla, sobremuestreo)
    out = destino / rid
    out.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for nombre, df in (("persons", persons), ("households", households), ("lineage", lineage)):
        path = out / f"{nombre}.parquet"
        df.write_parquet(path, compression="zstd", statistics=False)
        hashes[path.name] = sha256_file(path)
    meta = _metadata(rid, territorio, n, persons.height, semilla, sobremuestreo, info_sm)
    meta |= {
        "metodo_calibracion": f"{metodo} (Deville-Särndal, factores en [0,2; 5]); bloques: "
        + ", ".join(P.bloques(territorio)),
        "calibracion": {
            "fichero": f"processed/calibracion/{nombre_fichero(territorio)}_{metodo}.parquet",
            "sha256": meta_cal["sha256"],
            "version_codigo": meta_cal["version_codigo"],
            "proporcion_local": {
                b: d["proporcion_local"] for b, d in meta_cal["diagnosticos"].items()
            },
        },
        "integerizacion": "TRS con muestreo sistemático ordenado (bloque, provincia, grado de "
        "urbanización, tamaño de municipio, residencia, tipo y tamaño de hogar, nacionalidad y "
        "edad de la persona de referencia)",
        "hogares": households.height,
        "equilibrado": info_eq,
        # Referencia de V-REGLAS-BLANDAS: frecuencias en los donantes con los pesos calibrados.
        "referencia_reglas_blandas": frecuencias_blandas(p, "w"),
        "sha256": hashes,
    }
    (out / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    return meta


def _metadata(rid, territorio, n, obtenido, semilla, sobremuestreo, info_sm) -> dict:
    from sinpop.config import load_config
    from sinpop.targets import run

    cfg = load_config("targets.yaml")
    meta_i = json.loads((INTERIM_DIR / "metadata.json").read_text(encoding="utf-8"))["salidas"]
    meta_t = json.loads((run.DESTINO / "metadata.json").read_text(encoding="utf-8"))["salidas"]
    bloques = P.bloques(territorio)
    tipo = {"ES": "pais"}.get(territorio, territorio.split(":")[0].lower())
    return {
        "run_id": rid,
        "territorio": {"tipo": tipo, "codigo": territorio},
        "tamano_solicitado": n,
        "tamano_obtenido": obtenido,
        "modo": "sobremuestreo" if sobremuestreo else "representativo",
        "sobremuestreo": {"spec": sobremuestreo, **(info_sm or {})} if sobremuestreo else None,
        "semilla": semilla,
        "fecha_referencia": str(cfg.fecha_referencia),  # type: ignore[attr-defined]
        "fuentes": [
            {
                "id": "censo2021_personas",
                "edicion": "Censo 2021, microdatos de hogares (muestra)",
                "sha256": meta_i["censo2021_personas"]["sha256"],
            },
            *[
                {"id": f"objetivos {b}", "sha256": meta_t[b]["sha256"]}
                for b in [territorio, *bloques]
                if b in meta_t
            ],
        ],
        "objetivos_calibrados": [
            o.id
            for o in cfg.calibrar  # type: ignore[attr-defined]
            if o.universo in {*D.UNIVERSOS_PERSONA, "hogares"} and o.ambito != "municipios"
        ],
        "objetivos_reservados": [o.id for o in cfg.reservar],  # type: ignore[attr-defined]
        "objetivos_otras_fases": ["voto_generales_2023", "voto_autonomicas (F8B)"],
        "configuracion": {
            c: sha256_file(CONFIGS_DIR / c)
            for c in ("targets.yaml", "variables.yaml", "thresholds.yaml")
        },
        "version_codigo": code_version(),
        "fecha": dt.date.today().isoformat(),
        "validacion": {"estado": "pendiente", "informe": f"reports/{rid}/validacion.md"},
    }
