"""`lengua_habitual` (F8A, D-066) desde la ECEPOV 2021 del INE.

La Encuesta de Características Esenciales de la Población y las Viviendas 2021 (424.493
personas en viviendas familiares principales) pregunta, para cada lengua que la persona conoce
(hasta seis, con su nombre en texto), la frecuencia con que la usa en familia, con los amigos y
en el trabajo o la escuela (`T_FREC`: 1 nunca, 2 a veces, 3 frecuentemente, 4 siempre; en blanco
si no consta). La primera lengua es siempre el castellano y la segunda, en las comunidades con
lengua cooficial, la cooficial (diseño de registro `dr_ECEPOVhogar_2021.xlsx`).

Lengua habitual = la más usada **en familia**:
- castellano y cooficial empatadas en la frecuencia máxima → `bilingue`;
- si no, la cooficial con la frecuencia máxima → su lengua;
- otra lengua (ni castellano ni cooficial) con la frecuencia máxima y por encima del
  castellano → `otras`;
- el castellano con la frecuencia máxima → `castellano`;
- sin ninguna frecuencia en familia → `NC`.

Los nombres de lengua se clasifican por texto («CATALÁN (MALLORQUÍN, …)» y «VALENCIANO» →
`catalan_valenciano`); un nombre no previsto cuenta como `otras` (aranés, asturiano, aragonés y
lenguas extranjeras), salvo que esté vacío.

Perfil: sexo, edad, estudios (`ESTUDIOS`, fichero de adultos), actividad (`SITLAB`), provincia
(`IDQ_PV`, códigos INE), tamaño de municipio (`TAM_MUNI`, cuatro clases), nacionalidad (`NAC`) y
país de nacimiento (`PNACIM`, códigos INE de país, los mismos del Censo 2021 con la tabla de
`variables.yaml`; «000 No sabe / No contesta» → NC). Peso: `FACTOR`.
"""

from __future__ import annotations

import re
import tempfile
import zipfile
from pathlib import Path

import numpy as np
import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.harmonize.core import ccaa_de_provincia, tabla
from sinpop.opinion.valores import Modelo, _edad_grupo
from sinpop.repro import make_rng

ZIP = RAW_DIR / "ecepov2021" / "2021" / "datos_2021.zip"
SALIDA = INTERIM_DIR / "ecepov_lengua.parquet"
COOFICIALES = {
    "catalan_valenciano": r"^(CATAL[AÁ]N|VALENCIANO)\b",
    "gallego": r"^GALLEGO\b",
    "euskera": r"^EUSKERA\b",
}
ESTUDIOS = {  # T_ESTUD (adultos): 01-04 hasta CINE 2; 05-07 CINE 3-4; 08-12 CINE 5-8
    **dict.fromkeys(["01", "02", "03", "04"], "hasta_obligatoria"),
    **dict.fromkeys(["05", "06", "07"], "secundaria_2a_etapa"),
    **dict.fromkeys(["08", "09", "10", "11", "12"], "superior"),
}
SITLAB = {  # T_STLAB
    "1": "ocupado",
    "2": "ocupado",
    "4": "parado",
    "5": "parado",
    **dict.fromkeys(["3", "6", "7", "8", "9"], "inactivo"),
}
TAMANO = {  # T_TAMUN
    "1": "hasta_50000",
    "2": "de_50001_a_100000",
    "3": "de_100001_a_500000",
    "4": "mas_de_500000",
}
TAMANO_SINTETICA = {
    "hasta_2000": "hasta_50000",
    "de_2001_a_10000": "hasta_50000",
    "de_10001_a_50000": "hasta_50000",
    "de_50001_a_100000": "de_50001_a_100000",
    "de_100001_a_500000": "de_100001_a_500000",
    "mas_de_500000": "mas_de_500000",
}
COLUMNAS = [
    "sexo",
    "edad_grupo",
    "estudios_3",
    "actividad_3",
    "provincia",
    "tamano_municipio_ecepov",
    "nacionalidad_esp_ext",
    "pais_nacimiento_grupo",
    "provincia_edad4",
]


def clase_lengua(nombre: str | None) -> str | None:
    if nombre is None or not nombre.strip():
        return None
    n = nombre.strip().upper()
    if n.startswith("CASTELLANO"):
        return "castellano"
    for clase, patron in COOFICIALES.items():
        if re.match(patron, n):
            return clase
    return "otras"


def habitual(frecuencias: dict[str, int]) -> str:
    """{clase de lengua: máxima frecuencia de uso en familia} → lengua habitual."""
    if not frecuencias:
        return "NC"
    top = max(frecuencias.values())
    en_top = {k for k, v in frecuencias.items() if v == top}
    cast = "castellano" in en_top
    coof = sorted(en_top & set(COOFICIALES))
    if cast and coof:
        return "bilingue"
    if coof:
        return coof[0]
    if "otras" in en_top and not cast:
        return "otras"
    if cast:
        return "castellano"
    return "otras"


def _leer(zipf: zipfile.ZipFile, interior: str, nombre: str, cols: list[str]) -> pl.DataFrame:
    with tempfile.TemporaryDirectory() as tmp:
        zipf.extract(interior, tmp)
        with zipfile.ZipFile(Path(tmp) / interior) as z2:
            z2.extract(nombre, tmp)
        return pl.read_csv(
            Path(tmp) / nombre, separator="\t", columns=cols, infer_schema_length=0
        ).with_columns(pl.col(cols).str.strip_chars())


def armonizar() -> dict:
    hog_cols = (
        ["IDEN", "IDQ_PV", "TAM_MUNI", "FACTOR", "NPV", "SEXO", "EDAD", "NAC", "PNACIM"]
        + [f"NOMLENG{k}" for k in range(1, 7)]
        + [f"LENGFAM{k}" for k in range(1, 7)]
    )
    with zipfile.ZipFile(ZIP) as z:
        h = _leer(z, "ECEPOVhogar.zip", "CSV/ECEPOVhogar_2021.csv", hog_cols)
        a = _leer(
            z,
            "ECEPOVadultos.zip",
            "CSV/ECEPOVadultos_2021.csv",
            ["IDEN", "NPV", "ESTUDIOS", "SITLAB"],
        )
    h = h.with_columns(pl.col("EDAD").cast(pl.Int64)).filter(pl.col("EDAD") >= 18)
    d = h.join(a, on=["IDEN", "NPV"], how="left")
    # lengua habitual
    largo = []
    for k in range(1, 7):
        largo.append(
            d.select(
                "IDEN",
                "NPV",
                pl.col(f"NOMLENG{k}")
                .map_elements(clase_lengua, return_dtype=pl.Utf8)
                .alias("clase"),
                pl.col(f"LENGFAM{k}").replace("", None).cast(pl.Int64).alias("frec"),
            )
        )
    lg = pl.concat(largo).drop_nulls(["clase", "frec"])
    fuera = lg.filter(~pl.col("frec").is_between(1, 4))
    if fuera.height:
        raise ValueError(f"LENGFAM con códigos no documentados: {fuera['frec'].unique().to_list()}")
    maximos = lg.group_by("IDEN", "NPV", "clase").agg(pl.col("frec").max())
    por_persona = {}
    for (iden, npv), g in maximos.group_by("IDEN", "NPV"):
        por_persona[(iden, npv)] = habitual(dict(zip(g["clase"], g["frec"], strict=True)))
    hab = pl.DataFrame(
        {
            "IDEN": [k[0] for k in por_persona],
            "NPV": [k[1] for k in por_persona],
            "lengua_habitual": list(por_persona.values()),
        }
    )
    pais = tabla("pais_nacimiento_grupo", "censo2021_micro_hogares") | {"000": "NC"}
    sin = set(d["PNACIM"].unique()) - set(pais)
    if sin:
        raise ValueError(f"PNACIM sin documentar: {sorted(sin)}")
    for var, mapa in [("ESTUDIOS", ESTUDIOS), ("SITLAB", SITLAB), ("TAM_MUNI", TAMANO)]:
        sin = set(d[var].drop_nulls().unique()) - set(mapa) - {""}
        if sin:
            raise ValueError(f"{var} sin documentar: {sorted(sin)}")
    out = (
        d.join(hab, on=["IDEN", "NPV"], how="left")
        .select(
            pl.col("IDEN").alias("iden"),
            pl.col("NPV").alias("npv"),
            pl.col("FACTOR").cast(pl.Float64).alias("peso"),
            pl.col("SEXO").replace_strict({"1": "hombre", "2": "mujer"}).alias("sexo"),
            pl.col("EDAD").alias("edad"),
            pl.col("IDQ_PV").alias("provincia"),
            pl.col("IDQ_PV").replace_strict(ccaa_de_provincia()).alias("ccaa"),
            pl.col("TAM_MUNI").replace_strict(TAMANO).alias("tamano_municipio_ecepov"),
            pl.col("NAC")
            .replace_strict({"1": "espanola", "2": "extranjera"})
            .alias("nacionalidad_esp_ext"),
            pl.col("PNACIM").replace_strict(pais).alias("pais_nacimiento_grupo"),
            pl.col("ESTUDIOS").replace_strict(ESTUDIOS, default="NC").alias("estudios_3"),
            pl.col("SITLAB").replace_strict(SITLAB, default="NC").alias("actividad_3"),
            pl.col("lengua_habitual").fill_null("NC"),
        )
        .sort("iden", "npv")
    )
    out.write_parquet(SALIDA)
    return {
        "personas": out.height,
        "lengua_habitual": dict(
            out.group_by("lengua_habitual").agg(pl.col("peso").sum()).iter_rows()
        ),
    }


def datos() -> pl.DataFrame:
    d = pl.read_parquet(SALIDA)
    return d.filter((pl.col("estudios_3") != "NC") & (pl.col("actividad_3") != "NC")).with_columns(
        _edad_grupo(pl.col("edad"))
    )


def asignar(persons: pl.DataFrame, semilla: int) -> tuple[pl.DataFrame, dict]:
    """Extracción de la lengua habitual por perfil, provincia, nacionalidad y país de
    nacimiento. La ECEPOV cubre las viviendas familiares de cualquier nacionalidad: solo los
    residentes en establecimientos colectivos quedan `extrapolada`."""
    from sinpop.opinion.valores import perfil_sintetico

    perfil = (
        perfil_sintetico(persons)
        .join(
            persons.select("person_id", "provincia", "pais_nacimiento_grupo", "tamano_municipio"),
            on="person_id",
            how="left",
        )
        .with_columns(
            pl.col("tamano_municipio")
            .replace_strict(TAMANO_SINTETICA, default=None)
            .alias("tamano_municipio_ecepov")
        )
    )
    d = datos()
    # con 350.000 adultos la regularización apenas importa: C fijo (sin validación cruzada)
    m = Modelo("lengua_habitual", c=1.0, columnas=COLUMNAS).ajustar(d)
    pr = m.probabilidades(perfil)
    u = make_rng(semilla).random(len(pr))
    idx = (pr.cumsum(axis=1) < u[:, None]).sum(axis=1).clip(max=len(m.clases) - 1)
    calidad = np.where(perfil["tipo_residencia"] != "vivienda_familiar", "extrapolada", "modelada")
    out = perfil.select("person_id").with_columns(
        pl.Series("lengua_habitual", np.array(m.clases)[idx]),
        pl.Series("lengua_habitual__calidad", calidad),
    )
    return out, {"lengua_habitual": {"encuestados": m.n, "fuente": "ECEPOV 2021 (INE)"}}
