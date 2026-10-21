"""Microdatos del CIS anteriores al corte, armonizados (F8A, docs/03 §2.4).

Cada estudio se lee de su fichero SPSS (`MD<n>.zip` → `<n>.sav`) con sus etiquetas de valores.
Todo se recodifica **por la etiqueta**, nunca por el código: el CIS numera las comunidades por
orden alfabético (7 = Castilla-La Mancha, 8 = Castilla y León) y el INE al revés, y sus clases
de tamaño de municipio no son las del Padrón (CLAUDE.md, regla 2). Una etiqueta no prevista
detiene el proceso.

Salidas (`data/interim/`):
- `cis_personas.parquet`: una fila por encuestado con su perfil armonizado, el peso, la fecha y
  las variables de valores de `02_datos_y_variables.md` §3.4 que tenga el estudio;
- `cis_largo.parquet`: formato largo de todas las preguntas (estudio, encuestado, variable,
  código y etiqueta de la respuesta);
- `cis_preguntas.parquet`: banco de preguntas (enunciado, opciones y estudios en que aparece).

Los estudios con trabajo de campo posterior al corte están en `data/eval/` y aquí no se leen.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import unicodedata
import zipfile
from functools import lru_cache
from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR

CARPETA = RAW_DIR / "cis_barometros"
CORTE = dt.date(2026, 7, 1)
SELECCION = RAW_DIR / "cis_catalogo" / "seleccion.json"
NS_NC = {"N.S.": "NS", "N.C.": "NC", "No sabe, duda": "NS", "N.S./No recuerda": "NS"}


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s)


def _tokens(s: str) -> frozenset[str]:
    return frozenset(t for t in _norm(s).split() if t not in {"de", "la", "el", "les", "del"})


@lru_cache(maxsize=1)
def _territorios() -> tuple[dict[frozenset[str], str], dict[frozenset[str], str]]:
    from sinpop.config import load_config

    c = load_config("territories.yaml")
    ccaa = {_tokens(x.nombre): x.codigo for x in c.ccaa}  # type: ignore[attr-defined]
    prov = {_tokens(x.nombre): x.codigo for x in c.provincias}  # type: ignore[attr-defined]
    return ccaa, prov


def codigo_territorio(etiqueta: str, nivel: str) -> str:
    """Código INE de una comunidad o provincia a partir de la etiqueta del CIS."""
    ccaa, prov = _territorios()
    tabla = ccaa if nivel == "ccaa" else prov
    t = _tokens(etiqueta)
    if t in tabla:
        return tabla[t]
    # «Ceuta (Ciudad autónoma de)» frente a «Ceuta»; «Alicante» frente a «Alicante/Alacant»
    candidatos = {c for k, c in tabla.items() if k <= t or t <= k}
    if len(candidatos) == 1:
        return candidatos.pop()
    raise ValueError(f"etiqueta de {nivel} del CIS no reconocida: {etiqueta!r}")


# Recodificaciones por etiqueta (verificadas contra las etiquetas de valores del .sav)
SEXO = {"Hombre": "hombre", "Mujer": "mujer"}
TAMUNI = {
    "Menos o igual a 2.000 habitantes": "hasta_2000",
    "2.001 a 10.000 habitantes": "de_2001_a_10000",
    "10.001 a 50.000 habitantes": "de_10001_a_50000",
    "50.001 a 100.000 habitantes": "de_50001_a_100000",
    "100.001 a 400.000 habitantes": "mas_de_100000",
    "400.001 a 1.000.000 habitantes": "mas_de_100000",
    "Más de 1.000.000 habitantes": "mas_de_100000",
}
ESTUDIOS = {  # ESTUDIOS (resumen); la F.P. sin nivel se precisa con NIVELESTENTREV
    "Sin estudios": "hasta_obligatoria",
    "Primaria": "hasta_obligatoria",
    "Secundaria 1ª etapa": "hasta_obligatoria",
    "Secundaria 2ª etapa": "secundaria_2a_etapa",
    "Superiores": "superior",
}
# NIVELESTENTREV (nivel alcanzado, CNED): para precisar «F.P.» y «Otros» del resumen ESTUDIOS.
# 1-4: hasta la ESO (CINE 0-2); 5-6: FP de grado medio y bachillerato (CINE 3-4); 7-15: FP de
# grado superior y universitarios (CINE 5-8); 16 «Otros estudios», 98 y 99: no consta.
NIVEL_ESTUDIOS = {
    1: "hasta_obligatoria",
    2: "hasta_obligatoria",
    3: "hasta_obligatoria",
    4: "hasta_obligatoria",
    5: "secundaria_2a_etapa",
    6: "secundaria_2a_etapa",
    **dict.fromkeys(range(7, 16), "superior"),
}
SITLAB = {
    "Trabaja": "ocupado",
    "En paro y ha trabajado antes": "parado",
    "En paro y busca su primer empleo": "parado",
    "Jubilado/a o pensionista (anteriormente ha trabajado)": "inactivo",
    "Pensionista (anteriormente no ha trabajado)": "inactivo",
    "Estudiante": "inactivo",
    "Trabajo doméstico no remunerado": "inactivo",
    "Otra situación": "inactivo",
}
NACIONALIDAD = {
    "La nacionalidad española": "espanola",
    "La nacionalidad española y otra": "espanola",
    "Otra nacionalidad": "extranjera",
}
RELIGION = {
    "Católico/a practicante": "catolico_practicante",
    "Católico/a no practicante": "catolico_no_practicante",
    "Creyente de otra religión": "otra_religion",
    "Agnóstico/a": "agnostico",
    "Indiferente, no creyente": "indiferente",
    "Ateo/a": "ateo",
}
CLASESOCIAL = {  # respuesta espontánea codificada por el CIS
    "Clase alta": "alta",
    "Clase media-alta": "media_alta",
    "Clase media-media": "media",
    "Clase media-baja": "media_baja",
    "Clase trabajadora/obrera": "obrera",
    "Proletariado": "obrera",
    "Clase pobre": "baja",
    "Infraclase": "baja",
    "A los/as de abajo": "baja",
    "Excluidos/as": "baja",
    "Clase baja": "baja",
    "A la gente común": "otras",
    "Otras": "otras",
    "No cree en las clases": "no_cree_clases",
}
ECOPER = {
    "Muy buena": "muy_buena",
    "Buena": "buena",
    "(NO LEER) Regular": "regular",
    "Regular": "regular",
    "Mala": "mala",
    "Muy mala": "muy_mala",
}
VALORES = {  # variable de §3.4 → (variable del CIS, recodificación)
    "religiosidad": ("RELIGION", RELIGION),
    "clase_subjetiva": ("CLASESOCIAL", CLASESOCIAL),
    "situacion_economica_personal": ("ECOPER", ECOPER),
}


def estudios_disponibles() -> list[str]:
    return sorted(p.name for p in CARPETA.iterdir() if p.is_dir() and p.name.isdigit())


@lru_cache(maxsize=1)
def fechas() -> dict[str, str]:
    """Fecha de referencia de cada estudio (primer día del mes del barómetro, del catálogo)."""
    out = {"3567": "2026-06-01"}
    if SELECCION.exists():
        out |= {e["estudio"]: e["fecha"] for e in json.loads(SELECCION.read_text("utf-8"))}
    return out


def _sav(estudio: str) -> Path:
    d = CARPETA / estudio
    ext = d / "extraido"
    savs = list(ext.glob("*.sav")) if ext.exists() else []
    if not savs:
        zs = list(d.glob("MD*.zip")) + list(d.glob("md*.zip"))
        if not zs:
            raise FileNotFoundError(f"{estudio}: sin microdatos")
        ext.mkdir(exist_ok=True)
        with zipfile.ZipFile(zs[0]) as z:
            for n in z.namelist():
                if n.lower().endswith(".sav"):
                    z.extract(n, ext)
        savs = list(ext.rglob("*.sav"))
    return savs[0]


def leer(estudio: str):
    import pyreadstat

    df, meta = pyreadstat.read_sav(str(_sav(estudio)), apply_value_formats=False)
    return pl.from_pandas(df), meta


def _etiquetas(meta, var: str) -> dict[float, str]:
    return meta.variable_value_labels.get(var, {})


def _buscar(mapa: dict[str, str], et: str) -> str | None:
    """Categoría de una etiqueta: tal cual o sin su aclaración final entre paréntesis
    («Ateo/a (niegan la existencia de Dios)» → «Ateo/a»)."""
    et = et.strip()
    if et in mapa:
        return mapa[et]
    corta = et.split(" (")[0].strip()
    return mapa.get(corta) if corta and not et.startswith("(") else None


def _recodificar(df: pl.DataFrame, meta, var: str, mapa: dict[str, str], estudio: str) -> pl.Series:
    """Código → categoría por la etiqueta. NS/NC se conservan; «No procede» → NP; una etiqueta
    no prevista detiene el proceso."""
    lab = _etiquetas(meta, var)
    tabla: dict[float, str] = {}
    for cod, et in lab.items():
        et = et.strip()
        if _buscar(mapa, et) is not None:
            tabla[cod] = _buscar(mapa, et)
        elif et in NS_NC:
            tabla[cod] = NS_NC[et]
        elif et in ("No procede", "N.P."):
            tabla[cod] = "NP"
        else:
            raise ValueError(f"{estudio} {var}: etiqueta no prevista {et!r} ({cod})")
    s = df[var].cast(pl.Float64)
    sin = set(s.drop_nulls().unique().to_list()) - set(tabla)
    if sin:
        raise ValueError(f"{estudio} {var}: códigos sin etiqueta {sorted(sin)}")
    return s.replace_strict(tabla, return_dtype=pl.Utf8, default=None).alias(var)


def _territorio(df: pl.DataFrame, meta, var: str, nivel: str, estudio: str) -> pl.Series:
    lab = _etiquetas(meta, var)
    tabla = {c: codigo_territorio(e, nivel) for c, e in lab.items()}
    return df[var].cast(pl.Float64).replace_strict(tabla, return_dtype=pl.Utf8).alias(nivel)


def _estudios(df: pl.DataFrame, meta, estudio: str) -> pl.Series:
    """estudios_3 desde el resumen ESTUDIOS; «F.P.» y «Otros», con NIVELESTENTREV."""
    lab = _etiquetas(meta, "ESTUDIOS")
    base, ambiguos = {}, []
    for c, e in lab.items():
        e = e.strip()
        if e in ESTUDIOS:
            base[c] = ESTUDIOS[e]
        elif e in NS_NC:
            base[c] = "NC"
        elif e in ("F.P.", "Otros"):
            ambiguos.append(c)
        else:
            raise ValueError(f"{estudio} ESTUDIOS: etiqueta no prevista {e!r}")
    cod = df["ESTUDIOS"].cast(pl.Float64)
    s = cod.replace_strict(base, return_dtype=pl.Utf8, default=None)
    if ambiguos and "NIVELESTENTREV" in df.columns:
        nivel = (
            df["NIVELESTENTREV"]
            .cast(pl.Int64)
            .replace_strict(NIVEL_ESTUDIOS, return_dtype=pl.Utf8, default=None)
        )
        s = pl.select(pl.when(cod.is_in(ambiguos)).then(nivel).otherwise(s)).to_series()
    return s.fill_null("NC").alias("estudios_3")


def personas(estudio: str) -> pl.DataFrame:
    """Perfil armonizado, peso, fecha y variables de valores de un estudio."""
    df, meta = leer(estudio)
    cols = [
        pl.lit(estudio).alias("estudio"),
        pl.lit(fechas().get(estudio)).alias("fecha"),
        pl.int_range(df.height).alias("encuestado"),
    ]
    out = df.select(*cols)
    columnas = {
        "sexo": _recodificar(df, meta, "SEXO", SEXO, estudio),
        "edad": df["EDAD"].cast(pl.Int64),
        "ccaa": _territorio(df, meta, "CCAA", "ccaa", estudio),
        "provincia": _territorio(df, meta, "PROV", "provincia", estudio),
        "tamano_municipio_cis": _recodificar(df, meta, "TAMUNI", TAMUNI, estudio),
        "estudios_3": _estudios(df, meta, estudio),
        "actividad_3": _recodificar(df, meta, "SITLAB", SITLAB, estudio),
        "peso": df["PESO"].cast(pl.Float64)
        if "PESO" in df.columns
        else pl.Series([1.0] * df.height),
    }
    if "NACIONALIDAD" in df.columns:
        columnas["nacionalidad_esp_ext"] = _recodificar(
            df, meta, "NACIONALIDAD", NACIONALIDAD, estudio
        )
    for v, (orig, mapa) in VALORES.items():
        if orig in df.columns:
            columnas[v] = _recodificar(df, meta, orig, mapa, estudio)
    return out.with_columns([s.alias(k) for k, s in columnas.items()])


def largo(estudio: str) -> tuple[pl.DataFrame, pl.DataFrame]:
    """Formato largo de todas las preguntas con etiquetas de valores y su banco."""
    df, meta = leer(estudio)
    filas, banco = [], []
    for var, enunciado in zip(meta.column_names, meta.column_labels, strict=True):
        lab = _etiquetas(meta, var)
        if not lab or var in {"ESTU", "CUES", "CCAA", "PROV", "MUN", "TAMUNI"}:
            continue
        banco.append(
            {
                "estudio": estudio,
                "variable": var,
                "enunciado": enunciado or "",
                "opciones": json.dumps(
                    {str(int(k)): v for k, v in lab.items()}, ensure_ascii=False
                ),
            }
        )
        s = df[var].cast(pl.Float64)
        filas.append(
            pl.DataFrame(
                {
                    "estudio": estudio,
                    "encuestado": pl.int_range(df.height, eager=True),
                    "variable": var,
                    "codigo": s,
                    "etiqueta": s.replace_strict(
                        {k: v.strip() for k, v in lab.items()}, return_dtype=pl.Utf8, default=None
                    ),
                }
            ).drop_nulls("codigo")
        )
    return pl.concat(filas), pl.DataFrame(banco)


def armonizar() -> dict:
    """Escribe las tres salidas con todos los estudios disponibles anteriores al corte."""
    pers, largos, bancos, info = [], [], [], {}
    for e in estudios_disponibles():
        f = fechas().get(e)
        if f is None or dt.date.fromisoformat(f) >= CORTE:
            info[e] = "sin fecha o posterior al corte: no se usa"
            continue
        p = personas(e)
        lg, bq = largo(e)
        pers.append(p)
        largos.append(lg)
        bancos.append(bq)
        info[e] = {
            "fecha": f,
            "encuestados": p.height,
            "valores": [v for v in VALORES if v in p.columns],
        }
    personas_df = pl.concat(pers, how="diagonal_relaxed")
    personas_df.write_parquet(INTERIM_DIR / "cis_personas.parquet")
    pl.concat(largos).write_parquet(INTERIM_DIR / "cis_largo.parquet")
    banco = (
        pl.concat(bancos)
        .group_by("variable", "enunciado", "opciones")
        .agg(pl.col("estudio").sort().alias("estudios"))
        .sort("variable")
    )
    banco.write_parquet(INTERIM_DIR / "cis_preguntas.parquet")
    return {"estudios": info, "encuestados": personas_df.height, "preguntas": banco.height}
