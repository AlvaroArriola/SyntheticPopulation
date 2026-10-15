"""Comprobaciones de la puerta F2 sobre los ficheros armonizados (G2.1, G2.2, G2.3).

- G2.1: cada columna que es una variable categórica de `variables.yaml` solo contiene valores
  de su dominio (categorías más NS, NC, NP).
- G2.2: ninguna variable numérica contiene códigos especiales: los valores respetan el rango
  declarado y las columnas numéricas no tienen códigos NS/NC/NP como número.
- G2.3: los totales ponderados se conservan entre el fichero original y el armonizado
  (diferencia relativa < 0,01 %).
"""

from __future__ import annotations

from dataclasses import dataclass

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.config.schemas import ESPECIALES
from sinpop.harmonize.core import comprobar_dominio, variables

NO_VARIABLES = {"peso", "peso_16", "personas", "hogares", "person_id", "household_id", "norden"}
UMBRAL_G23 = 1e-4  # 0,01 %


def salidas() -> list[str]:
    return sorted(p.stem for p in INTERIM_DIR.glob("*.parquet"))


def g21_dominios() -> dict[str, dict[str, list[str]]]:
    """{fichero: {columna: valores fuera de dominio}} (vacío si todo está bien)."""
    out = {}
    for nombre in salidas():
        df = pl.read_parquet(INTERIM_DIR / f"{nombre}.parquet")
        malos = comprobar_dominio(df, df.columns)
        if malos:
            out[nombre] = malos
    return out


def columnas_categoricas_comprobadas() -> dict[str, list[str]]:
    v = variables().variables
    out = {}
    for nombre in salidas():
        cols = pl.read_parquet_schema(INTERIM_DIR / f"{nombre}.parquet")
        out[nombre] = [c for c in cols if c in v and v[c].categorias]
    return out


def g22_especiales() -> dict[str, dict[str, str]]:
    """{fichero: {columna: problema}} para columnas numéricas armonizadas."""
    v = variables().variables
    out: dict[str, dict[str, str]] = {}
    for nombre in salidas():
        df = pl.read_parquet(INTERIM_DIR / f"{nombre}.parquet")
        malos = {}
        for c, dtype in df.schema.items():
            if c in NO_VARIABLES:
                continue
            if dtype.is_numeric():
                s = df[c].drop_nulls()
                var = v.get(c)
                if var is not None and var.rango is not None:
                    lo, hi = var.rango
                    fuera = s.filter((s < lo) | (s > hi))
                    if fuera.len():
                        malos[c] = f"{fuera.len()} valores fuera de [{lo}, {hi}]"
                if c.startswith("n_") and s.len() and s.min() < 0:
                    malos[c] = "recuento negativo"
                if dtype.is_float() and s.is_nan().any():
                    malos[c] = "NaN"
            elif dtype == pl.Utf8 and c in v and v[c].tipo == "numerica":
                malos[c] = "variable numérica guardada como texto"
            elif dtype == pl.Utf8 and c in v and v[c].tipo == "ordinal":
                # una escala ordinal no puede tener los especiales mezclados como niveles
                cats = set(v[c].categorias or [])
                if cats & set(ESPECIALES):
                    malos[c] = "categorías especiales declaradas como niveles de la escala"
        if malos:
            out[nombre] = malos
    return out


@dataclass
class Total:
    fichero: str
    concepto: str
    original: float
    armonizado: float

    @property
    def diferencia_relativa(self) -> float:
        return abs(self.armonizado - self.original) / self.original if self.original else 0.0

    @property
    def ok(self) -> bool:
        return self.diferencia_relativa < UMBRAL_G23


def _filas_txt(path) -> int:
    n = 0
    with open(path, "rb") as fh:
        while b := fh.read(1 << 24):
            n += b.count(b"\n")
    return n


def g23_totales() -> list[Total]:
    from sinpop.harmonize import censos, encuestas
    from sinpop.harmonize.oficiales import _total_ine

    i = INTERIM_DIR
    out: list[Total] = []

    def suma(nombre: str, col: str) -> float:
        return float(pl.read_parquet(i / f"{nombre}.parquet", columns=[col])[col].sum())

    n21 = pl.scan_parquet(censos.C21).select(pl.len()).collect().item()
    out.append(
        Total(
            "censo2021_personas",
            "personas × factor 10",
            10.0 * n21,
            suma("censo2021_personas", "peso"),
        )
    )
    for a in ("2023", "2024", "2025"):
        base = RAW_DIR / f"censo_anual_micro_completo/{a}/extraido/md_Censo_muestra_{a}.txt"
        out.append(
            Total(
                f"censo_anual_muestra_{a}",
                "personas × factor 10",
                10.0 * _filas_txt(base),
                suma(f"censo_anual_muestra_{a}", "peso"),
            )
        )
    nex = pl.scan_parquet(censos.EXH).select(pl.len()).collect().item()
    out.append(
        Total(
            "censo_anual_exhaustivo_2025",
            "personas",
            float(nex),
            suma("censo_anual_exhaustivo_2025", "personas"),
        )
    )
    tr = pl.read_parquet(encuestas.ECV / "ECV_Tr_2025/md_ECV_Tr_2025.parquet", columns=["RB050"])
    tp = pl.read_parquet(encuestas.ECV / "ECV_Tp_2025/md_ECV_Tp_2025.parquet", columns=["PB040"])
    out.append(
        Total(
            "ecv",
            "RB050 (personas)",
            float(tr["RB050"].cast(pl.Float64).sum()),
            suma("ecv", "peso"),
        )
    )
    out.append(
        Total(
            "ecv", "PB040 (16+)", float(tp["PB040"].cast(pl.Float64).sum()), suma("ecv", "peso_16")
        )
    )
    for nombre, path, col in (
        ("epa", encuestas.EPA, "FACTOREL"),
        ("tic_h", encuestas.TIC, "FACTOR_P"),
        ("encuesta_salud", encuestas.SAL, "FACTORADULTO"),
    ):
        raw = pl.read_parquet(path, columns=[col])[col].cast(pl.Float64).sum()
        out.append(Total(nombre, col, float(raw), suma(nombre, "peso")))
    ecp = RAW_DIR / "ecp/2026-01-01"
    vf = _total_ine(
        ecp / "tabla_60124_20260101.json", Sexo="Total", **{"Totales de edad": "Todas las edades"}
    )
    tot = _total_ine(
        ecp / "tabla_59589_20260101.json",
        Sexo="Total",
        **{"Totales de edad": "Todas las edades", "Total Nacional": "Total Nacional"},
    )
    hog = _total_ine(
        ecp / "tabla_60133_20260101.json",
        **{"Composición del hogar": "Total", "Total Nacional": "Total Nacional"},
    )
    out += [
        Total(
            "ecp_viviendas_familiares", "personas", vf, suma("ecp_viviendas_familiares", "personas")
        ),
        Total("ecp_total", "personas", tot, suma("ecp_total", "personas")),
        Total("ecp_colectivos", "personas", tot - vf, suma("ecp_colectivos", "personas")),
        Total("ecp_hogares", "hogares", hog, suma("ecp_hogares", "hogares")),
    ]
    return out
