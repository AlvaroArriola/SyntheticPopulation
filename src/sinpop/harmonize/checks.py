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
from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.config.schemas import ESPECIALES
from sinpop.harmonize.core import comprobar_dominio, variables

NO_VARIABLES = {
    "peso",
    "peso_16",
    "peso_hogar",
    "personas",
    "hogares",
    "person_id",
    "household_id",
    "norden",
}
UMBRAL_G23 = 1e-4  # 0,01 %


def salidas() -> list[str]:
    return sorted(p.stem for p in INTERIM_DIR.glob("*.parquet"))


def g21_dominios() -> dict[str, dict[str, list[str]]]:
    """{fichero: {columna: valores fuera de dominio}} (vacío si todo está bien)."""
    out = {}
    v = variables().variables
    for nombre in salidas():
        # solo las columnas con dominio: cis_largo tiene decenas de millones de filas
        cols = [c for c in pl.read_parquet_schema(INTERIM_DIR / f"{nombre}.parquet") if c in v]
        if not cols:
            continue
        df = pl.read_parquet(INTERIM_DIR / f"{nombre}.parquet", columns=cols)
        malos = comprobar_dominio(df, df.columns)
        if malos:
            out[nombre] = malos
    return out


# Celdas vacías permitidas en los ficheros armonizados (D-033). Cada entrada dice en qué filas
# puede haber vacíos y por qué; un vacío fuera de esa condición, o en una columna que no está
# aquí, es un error de la armonización.
_PEQUENO = ["hasta_2000", "de_2001_a_10000"]
NULOS_DOCUMENTADOS: dict[tuple[str, str], tuple[pl.Expr, str]] = {
    # CIS (F8A, D-063): una pregunta que el estudio no hace queda vacía en todo el estudio
    ("cis_personas", "nacionalidad_esp_ext"): (
        pl.col("nacionalidad_esp_ext").is_null().all().over("estudio"),
        "el estudio no pregunta la nacionalidad (barómetros hasta mediados de 2024: universo de "
        "españoles)",
    ),
    ("cis_personas", "situacion_economica_personal"): (
        pl.col("situacion_economica_personal").is_null().all().over("estudio"),
        "el estudio no pregunta la situación económica personal (ECOPER)",
    ),
    ("cis_largo", "etiqueta"): (
        pl.col("codigo").is_not_null(),
        "valor sin etiqueta en el fichero SPSS (respuestas numéricas abiertas, como la edad o "
        "el número de personas, y puntos intermedios de escalas sin rotular)",
    ),
    ("censo2021_personas", "municipio"): (
        pl.col("tamano_municipio").is_in(_PEQUENO),
        "el INE no identifica los municipios de menos de 10.000 habitantes (CMUN 991–993)",
    ),
    ("censo_anual_exhaustivo_2025", "municipio"): (
        pl.col("tamano_municipio").is_in(_PEQUENO),
        "el INE no identifica los municipios de menos de 10.000 habitantes (CMUN 991–993)",
    ),
    ("ecv", "peso_16"): (
        pl.col("edad_31dic") < 16,
        "PB040 solo existe para quien tenía 16 años o más a 31/12 del año anterior (RB081): "
        "fichero de adultos",
    ),
    ("ecv", "privacion_material_n"): (
        pl.col("peso_16").is_null() | (pl.col("privacion_material") == "NC"),
        "solo se reconstruye para el fichero de adultos (16+ a 31/12) y cuando hay indicador "
        "oficial vrMATSOCDEP (D-044)",
    ),
    ("epa", "edad_4"): (
        pl.col("edad_grupo_epa") == "16",
        "la EPA agrupa 16–19 años y no permite separar a los de 18 y 19",
    ),
    ("elecciones_autonomicas_circunscripciones", "electores"): (
        pl.col("ccaa") == "02",
        "el informe de Aragón no publica electores",
    ),
    ("elecciones_autonomicas_circunscripciones", "votantes"): (
        pl.col("ccaa") == "07",
        "el BOCyL no publica votantes",
    ),
    ("elecciones_autonomicas_votos", "escanos"): (
        pl.lit(True),
        "la publicación no imprime escaños para esa candidatura (no se deducen; los escaños "
        "no se usan para construir la población)",
    ),
    ("elecciones_generales_2023_provincias_votos", "escanos"): (
        pl.col("escanos").is_null().all().over("siglas"),
        "candidaturas del cuadro III del BOE (sin escaño en ninguna provincia)",
    ),
}

# ESS ronda 11 (D-066, D-067): «Refusal», «Don't know», «No answer» y «Not applicable» no tienen
# posición en la escala ni categoría propia en estos ítems; quedan vacíos (respuesta legítima:
# los modelos los tratan como dato ausente y el emparejamiento de F8B los copia tal cual).
_ESS_PERFIL = {
    "estudio",
    "encuestado",
    "peso",
    "sexo",
    "edad",
    "estudios_3",
    "actividad_3",
    "ccaa",
    "nacionalidad_esp_ext",
}


def _nulos_ess() -> dict[tuple[str, str], tuple[pl.Expr, str]]:
    ruta = INTERIM_DIR / "ess_es.parquet"
    if not ruta.exists():
        return {}
    return {
        ("ess_es", c): (
            pl.lit(True),
            "no respuesta en la ESS (rechazo, no sabe, no contesta o no procede)",
        )
        for c in pl.read_parquet_schema(ruta)
        if c not in _ESS_PERFIL
    }


NULOS_DOCUMENTADOS |= _nulos_ess()


def g21_nulos() -> dict[str, str]:
    """{fichero.columna: problema} para los vacíos no documentados (vacío si todo está bien)."""
    out = {}
    for nombre in salidas():
        ruta = INTERIM_DIR / f"{nombre}.parquet"
        nulos = pl.scan_parquet(ruta).select(pl.all().null_count()).collect()
        for c, n in nulos.row(0, named=True).items():
            if not n:
                continue
            regla = NULOS_DOCUMENTADOS.get((nombre, c))
            if regla is None:
                out[f"{nombre}.{c}"] = f"{n} vacíos sin documentar"
                continue
            cols = sorted({c, *regla[0].meta.root_names()})
            df = pl.read_parquet(ruta, columns=cols)
            fuera = df.filter(pl.col(c).is_null() & ~regla[0]).height
            if fuera:
                out[f"{nombre}.{c}"] = f"{fuera} vacíos fuera de la condición documentada"
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
        ruta = INTERIM_DIR / f"{nombre}.parquet"
        cols = [
            c
            for c, dt in pl.read_parquet_schema(ruta).items()
            if c not in NO_VARIABLES and (dt.is_numeric() or c in v)
        ]
        df = pl.read_parquet(ruta, columns=cols)
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
    from sinpop.ingest.readers import layout_from_xlsx, read_fixed_width

    for a in ("2023", "2024", "2025"):
        base = RAW_DIR / f"censo_anual_micro_completo/{a}/extraido"
        lay = layout_from_xlsx(base / "dr_CensoAnual_muestra_2022.xlsx")
        crudo = read_fixed_width(base / f"md_Censo_muestra_{a}.txt", lay)
        assert crudo.height == _filas_txt(base / f"md_Censo_muestra_{a}.txt")
        desc = int(censos.descartados_d026(crudo).sum())
        out.append(
            Total(
                f"censo_anual_muestra_{a}",
                f"personas × factor 10 (sin {desc} descartados, D-026)",
                10.0 * (crudo.height - desc),
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
        ("epa", encuestas.ruta_epa(), "FACTOREL"),
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


# --------------------------------------------------------------------------- calidad

UMBRAL_NC = 0.05  # «no consta» por encima del 5 % del universo: se señala para revisión


def calidad() -> pl.DataFrame:
    """Por fichero y variable categórica: peso total y % ponderado de NP, NC y NS.

    El % de NC y NS se da también sobre el universo de la variable (total − NP), que es el que
    importa para la calidad: una variable con mucho NP no es mala si su universo es pequeño.
    Ponderación: `peso` si existe, `personas` en las tablas de recuentos; si no, cada fila
    cuenta 1 (se indica en la columna `ponderacion`).
    """
    v = variables().variables
    filas = []
    for nombre in salidas():
        cols = pl.read_parquet_schema(INTERIM_DIR / f"{nombre}.parquet")
        cats = [c for c in cols if c in v and v[c].categorias]
        if not cats:
            continue
        w = next((c for c in ("peso", "personas", "hogares") if c in cols), None)
        df = pl.read_parquet(
            INTERIM_DIR / f"{nombre}.parquet", columns=[*cats, *([w] if w else [])]
        )
        peso = pl.col(w).cast(pl.Float64) if w else pl.lit(1.0)
        tot = df.select(peso.sum()).item()
        for c in cats:
            r = df.select(
                *[peso.filter(pl.col(c) == e).sum().alias(e) for e in ("NP", "NC", "NS")],
                peso.filter(pl.col(c).is_null()).sum().alias("vacio"),
            ).row(0, named=True)
            universo = tot - r["NP"] - r["vacio"]
            filas.append(
                {
                    "fichero": nombre,
                    "variable": c,
                    "ponderacion": w or "sin peso",
                    "pct_NP": 100 * r["NP"] / tot,
                    "pct_vacio": 100 * r["vacio"] / tot,
                    "pct_NC_universo": 100 * r["NC"] / universo if universo else 0.0,
                    "pct_NS_universo": 100 * r["NS"] / universo if universo else 0.0,
                }
            )
    out = pl.DataFrame(filas)
    return out.with_columns(
        (pl.col("pct_NC_universo") + pl.col("pct_NS_universo") > 100 * UMBRAL_NC).alias("revisar")
    )


def informe_calidad(destino: Path) -> pl.DataFrame:
    t = calidad()
    lineas = [
        "# F2 · Calidad de las variables armonizadas",
        "",
        "Generado por `sinpop harmonize --check` (D-033). Porcentajes ponderados. NP = no procede "
        "(fuera del universo de la pregunta), NC = no consta, NS = no sabe. «Universo» = total "
        "menos NP y vacíos documentados. Se marcan para revisar las variables con más de un "
        f"{100 * UMBRAL_NC:.0f} % de NC + NS en su universo.",
        "",
        "| Fichero | Variable | Ponderación | % NP | % vacío | % NC (universo) "
        "| % NS (universo) | Revisar |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for r in t.iter_rows(named=True):
        lineas.append(
            f"| `{r['fichero']}` | `{r['variable']}` | {r['ponderacion']} | {r['pct_NP']:.2f} | "
            f"{r['pct_vacio']:.2f} | {r['pct_NC_universo']:.2f} | {r['pct_NS_universo']:.2f} | "
            f"{'**sí**' if r['revisar'] else ''} |"
        )
    destino.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return t
