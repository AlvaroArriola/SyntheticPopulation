"""European Social Survey, ronda 11 (España) para F8A (D-066).

Fichero integrado, edición 4.2 (`data/raw/ess/ESS11/ESS11e04_2.zip`, descargado a mano tras
iniciar sesión en el portal de la ESS; no se redistribuye). Se usan los casos de España
(`cntry == "ES"`, 1.844 entrevistas) de 18 años y más, con el peso de análisis `anweight`
(normalizado a media 1). La ESS entrevista a residentes de 15 años y más en viviendas
familiares, de cualquier nacionalidad.

Todo se recodifica por la **etiqueta** del fichero SPSS; los códigos 66, 77, 88 y 99 («Not
applicable», «Refusal», «Don't know», «No answer») son ausentes en los ítems y NS/NC en el
perfil.

- Confianza interpersonal: `ppltrst`, `pplfair`, `pplhlp` (0-10).
- Valores humanos de Schwartz (PVQ-21; en la ronda 11 los nombres llevan una «a» final): de
  «Very much like me» (6) a «Not like me at all» (1), invertidos para que más sea más.
- Región: NUTS 2 (`region`), traducida a comunidad por su nombre con `territories.yaml`.
"""

from __future__ import annotations

import tempfile
import zipfile
from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.opinion import cis as C

ZIP = RAW_DIR / "ess" / "ESS11" / "ESS11e04_2.zip"
SALIDA = INTERIM_DIR / "ess_es.parquet"
CONFIANZA = ["ppltrst", "pplfair", "pplhlp"]
# PVQ-21 por valor de Schwartz (Schwartz, 2003; guía de la ESS «Human values scale»)
PVQ = {
    "ipcrtiva": "autodireccion",
    "impfreea": "autodireccion",
    "impdiffa": "estimulacion",
    "ipadvnta": "estimulacion",
    "ipgdtima": "hedonismo",
    "impfuna": "hedonismo",
    "impricha": "poder",
    "iprspota": "poder",
    "ipshabta": "logro",
    "ipsucesa": "logro",
    "impsafea": "seguridad",
    "ipstrgva": "seguridad",
    "ipfrulea": "conformidad",
    "ipbhprpa": "conformidad",
    "ipmodsta": "tradicion",
    "imptrada": "tradicion",
    "iphlppla": "benevolencia",
    "iplylfra": "benevolencia",
    "ipeqopta": "universalismo",
    "ipudrsta": "universalismo",
    "impenva": "universalismo",
}
APERTURA = ["autodireccion", "estimulacion"]
CONSERVACION = ["seguridad", "conformidad", "tradicion"]
ESCALA_PVQ = {
    "Very much like me": 6,
    "Like me": 5,
    "Somewhat like me": 4,
    "A little like me": 3,
    "Not like me": 2,
    "Not like me at all": 1,
}
AUSENTE = {"Not applicable", "Refusal", "Don't know", "No answer"}
ESTUDIOS = {  # eisced (ES-ISCED)
    "ES-ISCED I , less than lower secondary": "hasta_obligatoria",
    "ES-ISCED II, lower secondary": "hasta_obligatoria",
    "ES-ISCED IIIb, lower tier upper secondary": "secundaria_2a_etapa",
    "ES-ISCED IIIa, upper tier upper secondary": "secundaria_2a_etapa",
    # IV: FP avanzada y ciclos cortos (CINE 4-5); en España es sobre todo la FP de grado superior
    "ES-ISCED IV, advanced vocational, sub-degree": "superior",
    "ES-ISCED V1, lower tertiary education, BA level": "superior",
    "ES-ISCED V2, higher tertiary education, >= MA level": "superior",
}
ACTIVIDAD = {  # mnactic
    "Paid work": "ocupado",
    "Unemployed, looking for job": "parado",
    "Unemployed, not looking for job": "parado",
    "Education": "inactivo",
    "Permanently sick or disabled": "inactivo",
    "Retired": "inactivo",
    "Community or military service": "inactivo",
    "Housework, looking after children, others": "inactivo",
    "Other": "inactivo",
}


def _etiquetar(df: pl.DataFrame, meta, var: str) -> pl.Series:
    lab = meta.variable_value_labels.get(var, {})
    return df[var].map_elements(lambda x: lab.get(x), return_dtype=pl.Utf8)


def _recod(s: pl.Series, mapa: dict, var: str, ausente_como: str | None) -> pl.Series:
    sin = (
        set(s.drop_nulls().unique())
        - set(mapa)
        - AUSENTE
        - {"Not possible to harmonise into ES-ISCED", "Other"}
    )
    if sin:
        raise ValueError(f"ESS {var}: etiquetas no previstas {sorted(sin)}")
    return s.replace_strict(mapa, default=ausente_como, return_dtype=pl.Utf8)


def armonizar() -> dict:
    import pyreadstat

    cols = (
        ["idno", "cntry", "anweight", "gndr", "agea", "eisced", "mnactic", "region", "ctzcntr"]
        + CONFIANZA
        + list(PVQ)
    )
    with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(ZIP) as z:
        z.extract("ESS11e04_2.sav", tmp)
        df, meta = pyreadstat.read_sav(str(Path(tmp) / "ESS11e04_2.sav"), usecols=cols)
    d = pl.from_pandas(df).filter(pl.col("cntry") == "ES")
    edad = d["agea"]
    region = _etiquetar(d, meta, "region")
    out = pl.DataFrame(
        {
            "estudio": ["ESS11"] * d.height,
            "encuestado": d["idno"].cast(pl.Int64),
            "peso": d["anweight"] / d["anweight"].mean(),
            "sexo": _recod(
                _etiquetar(d, meta, "gndr"), {"Male": "hombre", "Female": "mujer"}, "gndr", "NC"
            ),
            "edad": edad.cast(pl.Int64),
            "estudios_3": _recod(_etiquetar(d, meta, "eisced"), ESTUDIOS, "eisced", "NC"),
            "actividad_3": _recod(_etiquetar(d, meta, "mnactic"), ACTIVIDAD, "mnactic", "NC"),
            "ccaa": region.map_elements(
                lambda n: C.codigo_territorio(n, "ccaa"), return_dtype=pl.Utf8
            ),
            "nacionalidad_esp_ext": _recod(
                _etiquetar(d, meta, "ctzcntr"),
                {"Yes": "espanola", "No": "extranjera"},
                "ctzcntr",
                "NC",
            ),
        }
    )
    for v in CONFIANZA:
        s = d[v]
        # 0-10 con los extremos etiquetados; 77, 88 y 99 son rechazo, no sabe y no contesta
        out = out.with_columns(
            pl.Series(v, s).cast(pl.Float64).replace({77.0: None, 88.0: None, 99.0: None})
        )
    for v in PVQ:
        et = _etiquetar(d, meta, v)
        sin = set(et.drop_nulls().unique()) - set(ESCALA_PVQ) - AUSENTE
        if sin:
            raise ValueError(f"ESS {v}: etiquetas no previstas {sorted(sin)}")
        out = out.with_columns(
            et.replace_strict(ESCALA_PVQ, default=None, return_dtype=pl.Float64).alias(v)
        )
    out = out.filter(pl.col("edad").is_between(18, 120))
    out.write_parquet(SALIDA)
    return {"personas": out.height, "ccaa": out["ccaa"].n_unique()}
