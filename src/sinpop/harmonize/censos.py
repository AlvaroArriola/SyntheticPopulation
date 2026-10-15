"""Armonización de los censos del INE (F2).

- `censo2021`: microdatos de personas del Censo 2021 (donantes: hogares completos).
- `censo_anual_muestra`: muestras del 10 % del Censo Anual (2023, 2024, 2025).
- `censo_anual_exhaustivo`: fichero exhaustivo de 2025, guardado como tabla de recuentos
  (agregación sin pérdida de las variables demográficas que contiene).

Las muestras censales no traen peso: se usa un factor uniforme de 10 (D-016).
"""

from __future__ import annotations

from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.harmonize.core import (
    ccaa_de_provincia,
    edad_4,
    edad_5,
    recode,
    tabla,
    tamano_por_poblacion,
)
from sinpop.ingest.readers import layout_from_xlsx, read_fixed_width

C21 = RAW_DIR / "censo2021_micro_hogares/2021/extraido/md_CensoPersonas_2021.parquet"
EXH = RAW_DIR / "censo_anual_micro_demograficas/2025/extraido/md_CensoAnual_2025.parquet"
FACTOR_MUESTRA = 10.0  # D-016

SRC21 = "censo2021_micro_hogares"
SRCCA = "censo_anual_micro_completo"
SRCEX = "censo_anual_micro_demograficas"


# --------------------------------------------------------------------------- municipios


PADRON_MUNI = RAW_DIR / "padron_continuo/ultimo/tabla_29005_ultimo.json"


def poblacion_municipal(path: Path = PADRON_MUNI) -> pl.DataFrame:
    """Cifras oficiales de población municipal (Padrón a 01/01/2025, tabla INE 29005)."""
    import json

    filas = []
    for s in json.loads(path.read_text(encoding="utf-8")):
        md = {m["T3_Variable"]: m for m in s["MetaData"]}
        if md["Sexo"]["Codigo"] != "0" or md["Tamaño de los municipios"]["Codigo"] != "0":
            continue
        if not s["Data"]:
            continue
        cod = md["Municipios"]["Codigo"]
        filas.append((cod[:2], cod[2:], int(s["Data"][0]["Valor"])))
    return pl.DataFrame(filas, schema=["CPRO", "CMUN", "poblacion"], orient="row")


def tamanos_municipales(pob: pl.DataFrame) -> dict[str, str]:
    """{CPRO+CMUN: tamano_municipio} para los municipios identificados."""
    return {
        f"{p}{m}": tamano_por_poblacion(int(n))
        for p, m, n in pob.select("CPRO", "CMUN", "poblacion").iter_rows()
    }


def _tamano(df: pl.DataFrame, fuente: str, tam: dict[str, str]) -> pl.Series:
    clave = (pl.col("CPRO") + pl.col("CMUN")).alias("_pm")
    tmp = df.select(clave, pl.col("CMUN"))
    base = tabla("tamano_municipio", fuente)
    out = [base.get(m) or tam.get(pm) for pm, m in tmp.iter_rows()]
    faltan = sorted({pm for (pm, _), o in zip(tmp.iter_rows(), out, strict=True) if o is None})
    if faltan:
        raise ValueError(f"{fuente}: municipios sin población de referencia: {faltan[:20]}")
    return pl.Series("tamano_municipio", out, dtype=pl.Utf8)


# --------------------------------------------------------------------------- comunes


def _personales(df: pl.DataFrame, fuente: str, cols: dict[str, str]) -> pl.DataFrame:
    """Variables personales comunes al Censo 2021 y al Censo Anual."""
    edad = pl.col("VAREDAD").cast(pl.Int32)
    out = df.select(
        edad.alias("edad"),
        edad_5(edad),
        edad_4(edad),
        pl.col("CPRO").alias("provincia"),
    ).with_columns(
        pl.col("provincia").replace_strict(ccaa_de_provincia()).alias("ccaa"),
        (pl.col("edad") >= 18).alias("es_adulto"),
    )
    series = [
        recode(df, "SEXO", "sexo", fuente),
        recode(df, "PNACIO", "nacionalidad_grupo", fuente),
        recode(df, "PNACIM", "pais_nacimiento_grupo", fuente),
        recode(df, "PNACIO", "nacionalidad_top", fuente),
        recode(df, cols["degurba"], "grado_urbanizacion", fuente),
        recode(df, "VARANOE", "anio_llegada_espana", fuente),
    ]
    if cols.get("rela") and df[cols["rela"]].str.strip_chars().ne("").any():
        menor16 = pl.col("VAREDAD").cast(pl.Int32) < 16
        menor15 = pl.col("VAREDAD").cast(pl.Int32) < 15  # el INE deja en blanco hasta 14 años
        series += [
            recode(df, cols["rela"], "relacion_actividad", fuente, np_si=menor15),
            recode(df, cols["estudios"], "nivel_estudios", fuente, np_si=menor15),
            recode(df, cols["estudios"], "estudios_3", fuente, np_si=menor15),
        ]
        ec = recode(df, "ECIVIL", "estado_civil", fuente, np_si=menor16)
        # Estado civil solo para 16+: el Censo 2021 codifica «soltero» también a los niños.
        ec = (
            df.select(pl.col("VAREDAD"))
            .with_columns(ec)
            .select(pl.when(menor16).then(pl.lit("NP")).otherwise(pl.col("estado_civil")))
            .to_series()
        )
        series.append(ec.alias("estado_civil"))
    if cols.get("cno") and df[cols["cno"]].str.strip_chars().ne("").any():
        no_ocup = pl.col(cols["rela"]).cast(pl.Utf8).str.strip_chars() != cols["ocupado"]
        ocup = ~no_ocup  # ocupados con el campo en blanco: «no consta» (D-026)
        series += [
            recode(df, cols["cno"], "ocupacion", fuente, np_si=no_ocup, nc_si=ocup),
            recode(df, cols["cnae"], "sector_actividad", fuente, np_si=no_ocup, nc_si=ocup),
            recode(df, "SITU", "situacion_profesional", fuente, np_si=no_ocup, nc_si=ocup),
        ]
    return out.with_columns(series)


# --------------------------------------------------------------------------- Censo 2021


def _hogar_censo2021(df: pl.DataFrame) -> pl.DataFrame:
    """Persona de referencia (la de más edad; empate: menor NORDEN) y parentescos (D-021)."""
    base = df.select(
        "NVIV",
        "NORDEN",
        pl.col("VAREDAD").cast(pl.Int32).alias("_edad"),
        "NORDEN_CON",
        "NORDEN_PAD",
        "NORDEN_MAD",
        "FAMILIA",
    )
    ref = (
        base.sort(["NVIV", "_edad", "NORDEN"], descending=[False, True, False])
        .group_by("NVIV", maintain_order=True)
        .first()
        .select(
            "NVIV",
            pl.col("NORDEN").alias("r_norden"),
            pl.col("NORDEN_CON").alias("r_con"),
            pl.col("NORDEN_PAD").alias("r_pad"),
            pl.col("NORDEN_MAD").alias("r_mad"),
            pl.col("FAMILIA").alias("r_fam"),
        )
    )
    j = base.join(ref, on="NVIV", how="left")
    nz = lambda c: pl.col(c) != ""  # noqa: E731
    rel = (
        pl.when(pl.col("NORDEN") == pl.col("r_norden"))
        .then(pl.lit("persona_referencia"))
        .when(
            (nz("r_con") & (pl.col("NORDEN") == pl.col("r_con")))
            | (pl.col("NORDEN_CON") == pl.col("r_norden"))
        )
        .then(pl.lit("pareja"))
        .when(
            (pl.col("NORDEN_PAD") == pl.col("r_norden"))
            | (pl.col("NORDEN_MAD") == pl.col("r_norden"))
            | (
                nz("r_con")
                & (
                    (pl.col("NORDEN_PAD") == pl.col("r_con"))
                    | (pl.col("NORDEN_MAD") == pl.col("r_con"))
                )
            )
        )
        .then(pl.lit("hijo"))
        .when(
            (nz("r_pad") & (pl.col("NORDEN") == pl.col("r_pad")))
            | (nz("r_mad") & (pl.col("NORDEN") == pl.col("r_mad")))
        )
        .then(pl.lit("padre_madre"))
        .when((pl.col("FAMILIA") != "NN") & (pl.col("FAMILIA") == pl.col("r_fam")))
        .then(pl.lit("otro_familiar"))
        .otherwise(pl.lit("no_familiar"))
    )
    return j.select(rel.alias("relacion_persona_ref"))


COLS21 = [
    "CPRO",
    "CMUN",
    "NVIV",
    "NORDEN",
    "VAREDAD",
    "SEXO",
    "PNACIO",
    "PNACIM",
    "VARANOE",
    "ECIVIL",
    "ESREAL_CNEDA",
    "RELA",
    "OCU63",
    "ACT89",
    "SITU",
    "TENEN_VIV",
    "NORDEN_PAD",
    "NORDEN_MAD",
    "NORDEN_CON",
    "FAMILIA",
    "NUCLEO",
    "TIPO_NUC",
    "TAM_HOG",
    "TIPO_HOG",
    "TIPO_MUN_DEGURBA",
]


def censo2021(raw: Path = C21, tam: dict[str, str] | None = None) -> pl.DataFrame:
    df = pl.read_parquet(raw, columns=COLS21)
    if tam is None:
        tam = tamanos_municipales(poblacion_municipal())
    fuente = SRC21
    p = _personales(
        df,
        fuente,
        {
            "degurba": "TIPO_MUN_DEGURBA",
            "rela": "RELA",
            "estudios": "ESREAL_CNEDA",
            "cno": "OCU63",
            "cnae": "ACT89",
            "ocupado": "1",
        },
    )
    edad = pl.col("VAREDAD").cast(pl.Int32)
    hogar_n = df.group_by("NVIV").agg(
        (edad < 18).sum().alias("_n18"),
        (edad >= 65).sum().alias("n_mayores_65_hogar"),
        (edad >= 80).sum().alias("n_mayores_80_hogar"),
        pl.len().alias("_nper"),
    )
    nuc = df.filter(pl.col("NUCLEO") == "01").group_by("NVIV").agg(pl.col("TIPO_NUC").first())
    hh = (
        df.select("NVIV", "TIPO_HOG")
        .unique("NVIV")
        .join(nuc, on="NVIV", how="left")
        .with_columns(pl.col("TIPO_NUC").fill_null("9"))
        .with_columns((pl.col("TIPO_HOG") + "|" + pl.col("TIPO_NUC")).alias("_th"))
    )
    hh = hh.with_columns(recode(hh, "_th", "tipo_hogar", fuente)).select("NVIV", "tipo_hogar")
    out = pl.concat(
        [
            df.select(
                pl.col("NVIV").alias("household_id"),
                pl.col("NORDEN").alias("norden"),
                pl.col("TAM_HOG").cast(pl.Utf8).alias("_tam"),
            ),
            p,
            _hogar_censo2021(df),
            df.select(_tamano(df, fuente, tam)),
            df.select(recode(df, "TENEN_VIV", "tenencia_censo", fuente)),
            df.select(
                pl.when(pl.col("CMUN").is_in(["991", "992", "993"]))
                .then(pl.lit(None))
                .otherwise(pl.col("CPRO") + pl.col("CMUN"))
                .alias("municipio")
            ),
        ],
        how="horizontal",
    )
    out = out.with_columns(recode(out, "_tam", "tamano_hogar", fuente)).drop("_tam")
    out = (
        out.join(hogar_n.rename({"NVIV": "household_id"}), on="household_id", how="left")
        .join(hh.rename({"NVIV": "household_id"}), on="household_id", how="left")
        .with_columns(
            pl.when(pl.col("_n18") >= 3)
            .then(pl.lit("3+"))
            .otherwise(pl.col("_n18").cast(pl.Utf8))
            .alias("n_menores_hogar"),
            pl.lit(FACTOR_MUESTRA).alias("peso"),
        )
        .drop("_n18")
    )
    return out.sort("household_id", "norden")


# --------------------------------------------------------------------------- Censo Anual


def censo_anual_muestra(anio: str, tam: dict[str, str] | None = None) -> pl.DataFrame:
    base = RAW_DIR / f"censo_anual_micro_completo/{anio}/extraido"
    lay = layout_from_xlsx(base / "dr_CensoAnual_muestra_2022.xlsx")
    df = read_fixed_width(base / f"md_Censo_muestra_{anio}.txt", lay)
    if tam is None:
        tam = tamanos_municipales(poblacion_municipal())
    p = _personales(
        df,
        SRCCA,
        {
            "degurba": "DEGURBA",
            "rela": "RELA",
            "estudios": "ESREAL",
            "cno": "CNO",
            "cnae": "CNAE",
            "ocupado": "01",
        },
    )
    return pl.concat(
        [
            p,
            df.select(_tamano(df, SRCCA, tam)),
            pl.DataFrame({"peso": [FACTOR_MUESTRA] * df.height}),
        ],
        how="horizontal",
    ).with_columns(pl.lit(anio).alias("edicion"))


def censo_anual_exhaustivo(path: Path = EXH, tam: dict[str, str] | None = None) -> pl.DataFrame:
    """Tabla de recuentos por todas las variables demográficas del fichero exhaustivo."""
    if tam is None:
        tam = tamanos_municipales(poblacion_municipal())
    agg = (
        pl.scan_parquet(path)
        .group_by("CPRO", "CMUN", "SEXO", "VAREDAD", "PNACIO", "PNACIM", "DEGURBA")
        .agg(pl.len().alias("personas"))
        .collect()
        .with_columns(pl.col("VAREDAD").cast(pl.Utf8))
    )
    edad = pl.col("VAREDAD").cast(pl.Int32)
    out = agg.select(
        edad.alias("edad"),
        edad_5(edad),
        edad_4(edad),
        pl.col("CPRO").alias("provincia"),
        pl.when(pl.col("CMUN").is_in(["991", "992", "993"]))
        .then(pl.lit(None))
        .otherwise(pl.col("CPRO") + pl.col("CMUN"))
        .alias("municipio"),
        "personas",
    ).with_columns(
        pl.col("provincia").replace_strict(ccaa_de_provincia()).alias("ccaa"),
        recode(agg, "SEXO", "sexo", SRCEX),
        recode(agg, "PNACIO", "nacionalidad_grupo", SRCEX),
        recode(agg, "PNACIM", "pais_nacimiento_grupo", SRCEX),
        recode(agg, "PNACIO", "nacionalidad_top", SRCEX),
        recode(agg, "DEGURBA", "grado_urbanizacion", SRCEX),
        _tamano(agg, SRCEX, tam),
    )
    return out


def escribir(df: pl.DataFrame, nombre: str, destino: Path = INTERIM_DIR) -> Path:
    destino.mkdir(parents=True, exist_ok=True)
    path = destino / f"{nombre}.parquet"
    df.write_parquet(path, compression="zstd", statistics=False)
    return path
