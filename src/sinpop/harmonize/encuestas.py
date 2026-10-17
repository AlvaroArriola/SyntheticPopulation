"""Armonización de las encuestas de enriquecimiento (F2): ECV, EPA, TIC-H y ESdE.

Cada salida tiene una fila por persona, su peso oficial (`peso`), las variables llave
comunes con la población (edad, sexo, CCAA, nacionalidad, estudios, actividad) y las
variables de enriquecimiento. Decisiones: D-028.
"""

from __future__ import annotations

import polars as pl

from sinpop import RAW_DIR
from sinpop.harmonize.core import edad_4, edad_5, recode

ECV = RAW_DIR / "ecv/2025/extraido"
EPA = RAW_DIR / "epa/2T2026/extraido/md_EPA_2026T2.parquet"
TIC = RAW_DIR / "tic_h/2025/extraido/FicheroCuestionario/md_TICHcuestionario_2025.parquet"
SAL = RAW_DIR / "encuesta_salud/2023/extraido/ESdEadulto_2023/md_ESdEadulto_2023.parquet"


def _act3(col: str = "relacion_actividad") -> pl.Expr:
    return (
        pl.when(pl.col(col).is_in(["ocupado", "parado"]))
        .then(pl.col(col))
        .when(pl.col(col).is_in(["NP", "NC", "NS"]))
        .then(pl.col(col))
        .otherwise(pl.lit("inactivo"))
        .alias("relacion_actividad_3")
    )


def con_deciles(df: pl.DataFrame, valor: str, nombre: str, por: str | None = None) -> pl.DataFrame:
    """Añade el decil ponderado (D01..D10) de `valor` según la distribución de `peso`.

    El decil de cada persona es ceil(10 · F), con F la proporción acumulada de peso al
    ordenar por `valor` (dentro de `por`, si se indica).
    """
    keys = [por] if por else []
    tmp = df.with_row_index("_i").sort([*keys, valor, "_i"])
    cum = pl.col("peso").cum_sum()
    tot = pl.col("peso").sum()
    if por:
        cum, tot = cum.over(por), tot.over(por)
    # redondeo a 9 decimales antes del techo: evita que un límite exacto (p. ej. 0,1 · 10)
    # caiga en el decil siguiente por error de coma flotante
    tmp = tmp.with_columns(
        ((cum / tot) * 10).round(9).ceil().clip(1, 10).cast(pl.Int32).alias("_d")
    )
    tmp = tmp.with_columns(
        pl.format("D{}", pl.col("_d").cast(pl.Utf8).str.pad_start(2, "0")).alias(nombre)
    )
    return tmp.sort("_i").drop("_i", "_d")


# --------------------------------------------------------------------------- ECV


# Los 13 conceptos de la carencia material y social de la UE (D-044; códigos en disreg_ecv25)
ATRASOS = ["HS011", "HS021", "HS031"]  # 1, 2 = sí (una vez, dos o más); 3 = no
NO_PUEDE = ["HH050", "HS040", "HS050", "HS060"]  # 2 = no
NO_PUEDE_PERMITIR = ["HS110", "HD080"]  # 2 = no puede permitírselo
ITEMS_HOGAR = [*ATRASOS, *NO_PUEDE, *NO_PUEDE_PERMITIR]
ITEMS_PERSONA = ["PD020", "PD030", "PD050", "PD060", "PD070", "PD080"]  # 2 = no puede


def carencias(df: pl.DataFrame) -> pl.Expr:
    """Número de carencias (0-13) de una persona del fichero de adultos."""
    c = {x: pl.col(x).cast(pl.Utf8) for x in [*ITEMS_HOGAR, *ITEMS_PERSONA]}
    atrasos = pl.any_horizontal([c[x].is_in(["1", "2"]) for x in ATRASOS]).cast(pl.Int32)
    hogar = [(c[x] == "2").cast(pl.Int32) for x in [*NO_PUEDE, *NO_PUEDE_PERMITIR]]
    persona = [(c[x] == "2").cast(pl.Int32) for x in ITEMS_PERSONA]
    return atrasos + pl.sum_horizontal([*hogar, *persona])


def ecv() -> pl.DataFrame:
    tr = pl.read_parquet(
        ECV / "ECV_Tr_2025/md_ECV_Tr_2025.parquet",
        columns=["RB030", "RB050", "RB080", "RB081", "RB082", "RB090", "RB290", "vrMATSOCDEP"],
    )
    tp = pl.read_parquet(
        ECV / "ECV_Tp_2025/md_ECV_Tp_2025.parquet",
        columns=[
            "PB030",
            "PB040",
            "PE041",
            "PL032",
            "PH010",
            "PH030",
            "PE041_F",
            "PL032_F",
            "PH010_F",
            "PH030_F",
            *ITEMS_PERSONA,
        ],
    )
    th = pl.read_parquet(
        ECV / "ECV_Th_2025/md_ECV_Th_2025.parquet",
        columns=[
            "HB030",
            "HX040",
            "HX240",
            "vhRentaa",
            "HH021",
            "HS120",
            "HS110",
            "HH021_F",
            "HS120_F",
            "HS110_F",
            *(x for x in ITEMS_HOGAR if x != "HS110"),
        ],
    )
    td = pl.read_parquet(
        ECV / "ECV_Td_2025/md_ECV_Td_2025.parquet", columns=["DB030", "DB040", "DB090", "DB100"]
    )
    df = (
        tr.with_columns((pl.col("RB030") // 100).alias("HB030"))
        .join(tp.rename({"PB030": "RB030"}), on="RB030", how="left")
        .join(th, on="HB030", how="left")
        .join(td.rename({"DB030": "HB030"}), on="HB030", how="left")
    )
    # RB082 = −1 en nacidos en el año de la encuesta (RB080 = 2025): edad 0 (D-028)
    edad = pl.when(pl.col("RB082") < 0).then(0).otherwise(pl.col("RB082")).cast(pl.Int32)
    df = df.with_columns(edad.alias("edad"))
    s = "ecv"
    # Universo del fichero de adultos: quien no está en Tp → NP. Marca _F = −1 → «no consta».
    fuera_tp = pl.col("PB040").is_null()

    def nc(v: str) -> pl.Expr:
        return (pl.col(f"{v}_F") == "-1") | (pl.col("PL032") == "7")

    out = df.select(
        pl.col("RB030").cast(pl.Utf8).alias("person_id"),
        pl.col("HB030").cast(pl.Utf8).alias("household_id"),
        pl.col("RB050").alias("peso"),
        pl.col("PB040").alias("peso_16"),
        # Peso transversal del hogar (DB090): para emparejar hogares en F6 (D-044)
        pl.col("DB090").cast(pl.Float64).alias("peso_hogar"),
        "edad",
        # Edad a 31/12 del año anterior: define el universo del fichero de adultos (16+)
        pl.col("RB081").cast(pl.Int32).alias("edad_31dic"),
        edad_4(pl.col("edad")),
        pl.col("HX040").alias("n_personas_hogar"),
        (pl.col("vhRentaa") / pl.col("HX240")).alias("renta_equivalente"),
    ).with_columns(
        recode(df, "RB090", "sexo", s),
        recode(df, "DB040", "ccaa", s),
        recode(df, "RB290", "nacionalidad_esp_ext", s),
        recode(df, "PE041", "estudios_3", s, np_si=fuera_tp, nc_si=nc("PE041")),
        recode(df, "PL032", "relacion_actividad", s, np_si=fuera_tp, nc_si=nc("PL032")),
        recode(df, "PH010", "salud_autopercibida", s, np_si=fuera_tp, nc_si=nc("PH010")),
        recode(df, "PH030", "discapacidad_limitacion", s, np_si=fuera_tp, nc_si=nc("PH030")),
        recode(
            df,
            "HH021",
            "tenencia_vivienda",
            s,
            np_si=pl.col("HH021_F") == "-2",
            nc_si=pl.col("HH021_F") == "-1",
        ),
        recode(
            df,
            "HS120",
            "dificultad_fin_mes",
            s,
            np_si=pl.col("HS120_F") == "-2",
            nc_si=pl.col("HS120_F") == "-1",
        ),
        recode(
            df,
            "HS110",
            "vehiculo_hogar",
            s,
            np_si=pl.col("HS110_F") == "-2",
            nc_si=pl.col("HS110_F") == "-1",
        ),
        recode(df, "vrMATSOCDEP", "privacion_material", s, nc_si=pl.lit(True)),
        # Solo 16+ (fichero de adultos); sin indicador oficial → nulo (NC en privacion_material)
        df.select(
            pl.when(~fuera_tp & (pl.col("vrMATSOCDEP").cast(pl.Utf8).fill_null("") != ""))
            .then(carencias(df))
            .alias("privacion_material_n")
        ).to_series(),
        recode(
            df,
            "HH021",
            "tenencia_ecv",
            s,
            np_si=pl.col("HH021_F") == "-2",
            nc_si=pl.col("HH021_F") == "-1",
        ),
        recode(df, "DB100", "grado_urbanizacion", s),
    )
    out = out.with_columns(_act3())
    out = con_deciles(out, "renta_equivalente", "renta_hogar_decil")
    return con_deciles(out, "renta_equivalente", "renta_hogar_decil_ccaa", por="ccaa")


# --------------------------------------------------------------------------- EPA


COLS_EPA = [
    "CCAA",
    "PROV",
    "EDAD1",
    "SEXO1",
    "NAC1",
    "NFORMA",
    "AOI",
    "SITU",
    "PARCO1",
    "OCUP1",
    "DUCON1",
    "SIDI1",
    "SIDI2",
    "SIDI3",
    "CURSR",
    "CURSNR",
    "FACTOREL",
]


def _situacion_inactividad(df: pl.DataFrame) -> pl.DataFrame:
    """Una sola situación de inactividad por persona (D-049).

    SIDI1-SIDI3 son hasta tres respuestas ordenadas por código, no por importancia (SIDI1 es
    siempre menor que SIDI2), así que SIDI1 no es la situación principal. Prioridad, como en el
    Censo (registros administrativos): pensión de jubilación o prejubilación (02), incapacidad
    permanente (04), estudiante (01) si cursa enseñanza reglada (CURSR 1 o 2) y, si no, la
    primera de las demás. Un «estudiante» sin estudios reglados es «01NR»."""
    sid = [pl.col(c).str.strip_chars() for c in ("SIDI1", "SIDI2", "SIDI3")]

    def tiene(c: str) -> pl.Expr:
        return pl.any_horizontal([x == c for x in sid])

    reglados = pl.col("CURSR").str.strip_chars().is_in(["1", "2"])
    resto = pl.coalesce([pl.when(x.is_in(["03", "05", "06", "07"])).then(x) for x in sid])
    return df.with_columns(
        pl.when(tiene("02"))
        .then(pl.lit("02"))
        .when(tiene("04"))
        .then(pl.lit("04"))
        .when(tiene("01") & reglados)
        .then(pl.lit("01"))
        .when(resto.is_not_null())
        .then(resto)
        .when(tiene("01"))
        .then(pl.lit("01NR"))
        .otherwise(pl.col("SIDI1").str.strip_chars())
        .alias("SIDI")
    )


def _formacion(df: pl.DataFrame) -> pl.DataFrame:
    """Código derivado `_CURS` de CURSR y CURSNR (tabla TCURSR): 1 si alguna es 1 (sí) o 2
    (estudiante en vacaciones); 3 si las dos son 3 (no); vacío en el resto."""
    r, nr = pl.col("CURSR").str.strip_chars(), pl.col("CURSNR").str.strip_chars()
    return df.with_columns(
        pl.when(r.is_in(["1", "2"]) | nr.is_in(["1", "2"]))
        .then(pl.lit("1"))
        .when((r == "3") & (nr == "3"))
        .then(pl.lit("3"))
        .otherwise(pl.lit(""))
        .alias("_CURS")
    )


def _actividad_epa(df: pl.DataFrame, menor16: pl.Expr) -> pl.Series:
    df = _situacion_inactividad(df)
    inactivo = recode(
        df,
        "SIDI",
        "relacion_actividad",
        "epa",
        nc_si=pl.col("AOI").is_in(["07", "08", "09"]),
        # SIDI1 solo se pregunta a los inactivos: en el resto, vacío = no procede
        np_si=menor16 | pl.col("AOI").is_in(["03", "04", "05", "06"]),
        otros={"01NR": "otra_inactividad"},
    )
    aoi = df["AOI"]
    return (
        pl.DataFrame({"aoi": aoi, "ina": inactivo})
        .select(
            pl.when(pl.col("aoi").is_in(["03", "04"]))
            .then(pl.lit("ocupado"))
            .when(pl.col("aoi").is_in(["05", "06"]))
            .then(pl.lit("parado"))
            .when(pl.col("aoi").is_in(["07", "08", "09"]))
            .then(pl.col("ina"))
            .otherwise(pl.lit("NP"))
            .alias("relacion_actividad")
        )
        .to_series()
    )


def epa() -> pl.DataFrame:
    cols = COLS_EPA
    df = pl.read_parquet(EPA, columns=cols).with_columns(
        pl.col(c).cast(pl.Utf8).fill_null("") for c in cols if c != "FACTOREL"
    )
    s = "epa"
    menor16 = pl.col("EDAD1").is_in(["00", "05", "10"])
    no_ocup = ~pl.col("AOI").is_in(["03", "04"])
    edad4 = (
        pl.when(menor16)
        .then(pl.lit("NP"))
        .when(pl.col("EDAD1") == "16")
        .then(pl.lit(None))  # 16–19: la EPA no permite separar a los de 18 y 19 (D-033)
        .when(pl.col("EDAD1").is_in(["20", "25", "30"]))
        .then(pl.lit("18-34"))
        .when(pl.col("EDAD1").is_in(["35", "40", "45"]))
        .then(pl.lit("35-49"))
        .when(pl.col("EDAD1").is_in(["50", "55", "60"]))
        .then(pl.lit("50-64"))
        .otherwise(pl.lit("65+"))
    )
    out = df.select(
        pl.col("FACTOREL").cast(pl.Float64).alias("peso"),
        pl.col("EDAD1").alias("edad_grupo_epa"),
        edad4.alias("edad_4"),
        pl.col("PROV").alias("provincia"),
    ).with_columns(
        recode(df, "SEXO1", "sexo", s),
        recode(df, "CCAA", "ccaa", s),
        recode(df, "NAC1", "nacionalidad_esp_ext", s),
        recode(df, "NFORMA", "estudios_3", s, np_si=menor16),
        recode(df, "AOI", "relacion_actividad_3", s, np_si=menor16),
        # D-049: ocupados y parados por AOI; inactivos por su situación autopercibida (SIDI1-3)
        _actividad_epa(df, menor16),
        # D-050: educación o formación en las cuatro últimas semanas (reglada o no)
        recode(
            _formacion(df),
            "_CURS",
            "cursa_formacion",
            s,
            np_si=menor16,
            nc_si=~menor16,
        ),
        recode(df, "SITU", "situacion_profesional", s, np_si=no_ocup),
        recode(df, "SITU", "sector_publico", s, np_si=no_ocup),
        recode(df, "PARCO1", "tipo_jornada", s, np_si=no_ocup),
        recode(df, "OCUP1", "ocupacion", s, np_si=no_ocup),
    )
    return out


# --------------------------------------------------------------------------- TIC-H


COLS_TIC = [
    "CCAA",
    "SEXO",
    "EDAD",
    "NACIONALIDAD",
    "NIVELEST",
    "SIT_LAB",
    "ULT_INT",
    "FREC_INT",
    "ULT_COM",
    "TELETRAB",
    "ULT_TTRAB",
    "TTRAB_ACTUAL",
    "FACTOR_P",
]


def tic_h() -> pl.DataFrame:
    cols = COLS_TIC
    df = pl.read_parquet(TIC, columns=cols).with_columns(
        pl.col(c).cast(pl.Utf8).fill_null("").str.strip_chars() for c in cols if c != "FACTOR_P"
    )
    df = df.with_columns(
        (
            pl.col("ULT_INT")
            + "|"
            + pl.when(pl.col("ULT_INT") == "1").then(pl.col("FREC_INT")).otherwise(pl.lit(""))
        ).alias("_int"),
        # TELETRAB = 6: el trabajo exige presencia y no se pregunta ULT_TTRAB → «nunca»
        pl.when(pl.col("TELETRAB") == "6")
        .then(pl.lit("6|"))
        .when((pl.col("TELETRAB") == "") & (pl.col("ULT_TTRAB") == ""))
        .then(pl.lit(""))  # pregunta no formulada (no ocupados) → NP
        .otherwise(
            pl.col("ULT_TTRAB")
            + "|"
            + pl.when(pl.col("ULT_TTRAB") == "1").then(pl.col("TTRAB_ACTUAL")).otherwise(pl.lit(""))
        )
        .alias("_tt"),
        pl.col("ULT_COM").replace("", "4").alias("_com"),
    )
    s = "tic_h"
    edad = pl.col("EDAD").cast(pl.Int32)
    no_ocup = ~pl.col("SIT_LAB").is_in(["1", "2", "3", "4"])
    out = df.select(
        pl.col("FACTOR_P").cast(pl.Float64).alias("peso"),
        edad.alias("edad"),
        edad_4(edad),
        edad_5(edad),
    ).with_columns(
        recode(df, "SEXO", "sexo", s),
        recode(df, "CCAA", "ccaa", s),
        recode(df, "NACIONALIDAD", "nacionalidad_esp_ext", s),
        recode(df, "NIVELEST", "estudios_3", s),
        recode(df, "SIT_LAB", "relacion_actividad", s),
        recode(df, "_int", "uso_internet", s),
        recode(df, "_com", "compra_online", s),
        recode(df, "_tt", "teletrabajo", s, np_si=no_ocup),
    )
    # Teletrabajo solo para ocupados: sin respuesta de un no ocupado → NP
    out = out.with_columns(
        pl.when(df.select(no_ocup).to_series())
        .then(pl.lit("NP"))
        .otherwise(pl.col("teletrabajo"))
        .alias("teletrabajo"),
        _act3(),
    )
    return out


# --------------------------------------------------------------------------- ESdE


COLS_SAL = ["CCAA", "SEXOa", "EDADa", "A2a_1", "NIVEST", "C1", "C3a", "FACTORADULTO"]


def encuesta_salud() -> pl.DataFrame:
    cols = COLS_SAL
    df = pl.read_parquet(SAL, columns=cols).with_columns(
        pl.col(c).cast(pl.Utf8).fill_null("").str.strip_chars() for c in cols if c != "FACTORADULTO"
    )
    s = "encuesta_salud"
    edad = pl.col("EDADa").cast(pl.Int32)
    return df.select(
        pl.col("FACTORADULTO").cast(pl.Float64).alias("peso"),
        edad.alias("edad"),
        edad_4(edad),
        edad_5(edad),
    ).with_columns(
        recode(df, "SEXOa", "sexo", s),
        recode(df, "CCAA", "ccaa", s),
        recode(df, "A2a_1", "nacionalidad_esp_ext", s),
        recode(df, "NIVEST", "estudios_3", s),
        recode(df, "C1", "salud_autopercibida", s),
        recode(df, "C3a", "discapacidad_limitacion", s),
    )
