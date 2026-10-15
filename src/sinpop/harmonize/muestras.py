"""Muestras de 20 registros por fuente para la revisión humana G2.8.

Cada fichero `data/interim/muestras_g28/<fuente>.csv` pone lado a lado los campos originales
(`orig__<campo>`, tal como vienen en el fichero del INE) y los armonizados (`arm__<variable>`).
El revisor los compara a mano con el diseño de registro.

Regla 8 de CLAUDE.md: los registros originales no salen del entorno local. Las muestras se
escriben en `data/` (excluido del control de versiones) y el informe versionado
(`reports/fase_02_muestras.md`) solo describe los ficheros, sin valores.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR, REPORTS_DIR
from sinpop.repro import make_rng

SEMILLA = 2026
N = 20
DESTINO = INTERIM_DIR / "muestras_g28"


def _indices(n_total: int, rng) -> list[int]:
    return sorted(int(i) for i in rng.choice(n_total, size=N, replace=False))


def _lado_a_lado(orig: pl.DataFrame, arm: pl.DataFrame) -> pl.DataFrame:
    return pl.concat(
        [
            orig.rename({c: f"orig__{c}" for c in orig.columns}),
            arm.rename({c: f"arm__{c}" for c in arm.columns}),
        ],
        how="horizontal",
    )


def _por_fila(nombre: str, crudo: pl.DataFrame, rng) -> pl.DataFrame:
    """Para armonizaciones que conservan el orden de las filas del fichero original."""
    arm = pl.read_parquet(INTERIM_DIR / f"{nombre}.parquet")
    if arm.height != crudo.height:
        raise ValueError(f"{nombre}: {arm.height} filas armonizadas ≠ {crudo.height} originales")
    idx = _indices(crudo.height, rng)
    return _lado_a_lado(crudo[idx], arm[idx]).with_columns(
        pl.Series("fila_fichero_original", [i + 1 for i in idx])
    )


def muestras() -> dict[str, tuple[int, str]]:
    """Escribe las muestras y devuelve {fuente: (filas, documento de referencia)}."""
    from sinpop.harmonize import censos, encuestas
    from sinpop.ingest.readers import layout_from_xlsx, read_fixed_width

    rng = make_rng(SEMILLA)
    DESTINO.mkdir(parents=True, exist_ok=True)
    out: dict[str, pl.DataFrame] = {}
    ref: dict[str, str] = {}

    # Censo 2021: enlace por vivienda y número de orden
    c21 = pl.read_parquet(censos.C21, columns=censos.COLS21)
    idx = _indices(c21.height, rng)
    orig = c21[idx]
    arm = pl.read_parquet(INTERIM_DIR / "censo2021_personas.parquet").join(
        orig.select(pl.col("NVIV").alias("household_id"), pl.col("NORDEN").alias("norden")),
        on=["household_id", "norden"],
        how="semi",
    )
    orig = orig.sort("NVIV", "NORDEN")
    out["censo2021_micro_hogares"] = _lado_a_lado(orig, arm.sort("household_id", "norden"))
    ref["censo2021_micro_hogares"] = "dr_CensoPersonas_2021.xlsx"

    # Muestras del Censo Anual (el orden de filas se conserva)
    for a in ("2023", "2024", "2025"):
        base = RAW_DIR / f"censo_anual_micro_completo/{a}/extraido"
        lay = layout_from_xlsx(base / "dr_CensoAnual_muestra_2022.xlsx")
        crudo = read_fixed_width(base / f"md_Censo_muestra_{a}.txt", lay)
        out[f"censo_anual_micro_completo_{a}"] = _por_fila(f"censo_anual_muestra_{a}", crudo, rng)
        ref[f"censo_anual_micro_completo_{a}"] = "dr_CensoAnual_muestra_2022.xlsx"

    # Censo Anual exhaustivo: 20 personas y su celda armonizada
    ex = pl.scan_parquet(censos.EXH)
    n = ex.select(pl.len()).collect().item()
    idx = _indices(n, rng)
    orig = ex.with_row_index("_i").filter(pl.col("_i").is_in(idx)).drop("_i").collect()
    tmp = DESTINO / "_exhaustivo_20.parquet"
    orig.write_parquet(tmp)
    arm = censos.censo_anual_exhaustivo(tmp)
    tmp.unlink()
    out["censo_anual_micro_demograficas"] = _lado_a_lado(
        orig.sort("CPRO", "CMUN", "SEXO", "VAREDAD", "PNACIO", "PNACIM", "DEGURBA"), arm
    ).drop("arm__personas")
    ref["censo_anual_micro_demograficas"] = "dr_CensoAnual_2026.json"

    # ECV: enlace por identificador de persona
    tr = pl.read_parquet(encuestas.ECV / "ECV_Tr_2025/md_ECV_Tr_2025.parquet")
    idx = _indices(tr.height, rng)
    orig = tr[idx]
    arm = pl.read_parquet(INTERIM_DIR / "ecv.parquet")
    arm = orig.select(pl.col("RB030").cast(pl.Utf8).alias("person_id")).join(
        arm, on="person_id", how="left"
    )
    tp = pl.read_parquet(encuestas.ECV / "ECV_Tp_2025/md_ECV_Tp_2025.parquet")
    orig = orig.join(tp.rename({"PB030": "RB030"}), on="RB030", how="left")
    out["ecv"] = _lado_a_lado(orig, arm)
    ref["ecv"] = "disreg_ecv25 (diseños de los ficheros R, P, H y D)"

    for nombre, path, doc in (
        ("epa", encuestas.EPA, "dr_EPA_2026.json"),
        ("tic_h", encuestas.TIC, "dr_TICHcuestionario_2025.json"),
        ("encuesta_salud", encuestas.SAL, "dr_ESdEadulto_2023.json"),
    ):
        out[nombre] = _por_fila(nombre, pl.read_parquet(path), rng)
        ref[nombre] = doc

    # Tablas (ECP) y resultados electorales: 20 filas armonizadas con su referencia
    for nombre, doc in (
        ("ecp_viviendas_familiares", "INE, tabla 60129 (JSON de la API)"),
        ("ecp_total", "INE, tabla 59589"),
        ("ecp_hogares", "INE, tabla 60133"),
        ("elecciones_generales_2023_municipios", "PDF de Interior: página del municipio"),
    ):
        arm = pl.read_parquet(INTERIM_DIR / f"{nombre}.parquet")
        out[nombre] = arm[_indices(arm.height, rng)]
        ref[nombre] = doc

    resumen = {}
    for k, df in out.items():
        df.write_csv(DESTINO / f"{k}.csv")
        resumen[k] = (df.height, ref[k])
    return resumen


def informe(resumen: dict[str, tuple[int, str]]) -> Path:
    lineas = [
        "# F2 · Muestras para la revisión humana G2.8",
        "",
        f"Generadas el {dt.date.today().isoformat()} con `sinpop harmonize --samples` "
        f"(semilla {SEMILLA}). Los ficheros están en `data/interim/muestras_g28/` y **no se "
        "versionan**: contienen registros originales, que no pueden salir del entorno local "
        "(regla 8 de CLAUDE.md).",
        "",
        "Cada fichero pone lado a lado los campos originales (`orig__…`) y los armonizados "
        "(`arm__…`). Para revisar: abrir el CSV, buscar cada código original en el diseño de "
        "registro indicado y comprobar que la categoría armonizada es la que fija "
        "`configs/variables.yaml` (o la regla de universo de D-025 a D-028).",
        "",
        "| Fichero | Registros | Diseño de registro o documento de referencia |",
        "| --- | ---: | --- |",
    ]
    lineas += [f"| `{k}.csv` | {n} | {d} |" for k, (n, d) in resumen.items()]
    path = REPORTS_DIR / "fase_02_muestras.md"
    path.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return path
