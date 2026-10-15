"""Reproducción de cifras oficiales publicadas con los microdatos armonizados (G2.4).

Tolerancias (D-027):
- ficheros exhaustivos: igualdad exacta;
- muestras (factor de elevación conocido): |p̂ − p| ≤ 3 · EE, con EE el error típico de una
  proporción en un muestreo aleatorio simple con fracción f (corrección por población finita);
- encuestas con tasas publicadas redondeadas: |p̂ − p| ≤ redondeo de la publicación + 3 · EE.
"""

from __future__ import annotations

# ruff: noqa: E501  (etiquetas literales de las tablas del INE)
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.ingest.ine_tablas import leer

TAB = RAW_DIR / "censo_anual_tablas"


@dataclass
class Cifra:
    fuente: str
    edicion: str
    cifra: str
    categoria: str
    oficial: float
    reproducida: float
    tolerancia: float
    tipo: str  # exacta | muestral
    referencia: str

    @property
    def diferencia(self) -> float:
        return self.reproducida - self.oficial

    @property
    def ok(self) -> bool:
        return abs(self.diferencia) <= self.tolerancia + 1e-9


def _ee(p: float, n: int, f: float) -> float:
    return math.sqrt(max(p * (1 - p), 1e-12) / max(n, 1) * (1 - f))


def _proporciones(
    oficial: dict[str, float],
    muestra: dict[str, int],
    *,
    fuente: str,
    edicion: str,
    cifra: str,
    referencia: str,
    f: float = 0.10,
) -> list[Cifra]:
    to = sum(oficial.values())
    n = sum(muestra.values())
    out = []
    for k in oficial:
        p = oficial[k] / to
        q = muestra.get(k, 0) / n
        out.append(
            Cifra(
                fuente,
                edicion,
                cifra,
                k,
                round(100 * p, 3),
                round(100 * q, 3),
                round(100 * 3 * _ee(p, n, f), 3),
                "muestral",
                referencia,
            )
        )
    return out


def _filtra(df: pl.DataFrame, **igual: str | None) -> pl.DataFrame:
    for col, val in igual.items():
        df = df.filter(pl.col(col).is_null()) if val is None else df.filter(pl.col(col) == val)
    return df


# --------------------------------------------------------------------------- correspondencias
FORMACION = {  # tabla 66601 → nivel_estudios  # noqa: E501
    "Sin estudios": ["analfabetos", "primaria_incompleta"],
    "Educación primaria": ["primaria"],
    "Primera etapa de Educación Secundaria y similar": ["secundaria_1a_etapa"],
    "Segunda etapa de educación secundaria, con orientación general": ["bachillerato"],
    "Segunda etapa de educación secundaria con orientación profesional; Educación postsecundaria no superior": [
        "fp_grado_medio",
        "postsecundaria_no_superior",
    ],
    "Enseñanzas de formación profesional, artes plásticas y diseño y deportivas de grado superior y equivalentes": [
        "fp_grado_superior"
    ],
    "Grados universitarios de hasta 240 créditos ECTS, diplomados universitarios y equivalentes": [
        "grado_240"
    ],
    "Grados universitarios de más de 240 créditos ECTS, licenciados y equivalentes": [
        "grado_mas_240_licenciatura"
    ],
    "Másteres, especialidades en Ciencias de la Salud por el sistema de residencia y similares": [
        "master"
    ],
    "Doctorado universitario": ["doctorado"],
}
ACTIVIDAD = {  # tabla 67132 → relacion_actividad
    "Ocupado/a": "ocupado",
    "Parado/a": "parado",
    "Perceptor/a pensión de incapacidad": "incapacidad_permanente",
    "Perceptor/a pensión de jubilación, prejubilación": "jubilado_pensionista",
    "Estudiante": "estudiante",
    "Otra situación de inactividad": "otra_inactividad",
}
ECIVIL = {
    "Soltero/a": "soltero",
    "Casado/a": "casado",
    "Viudo/a": "viudo",
    "Divorciado/a o separado/a": "separado_divorciado",
    "No consta": "NC",
}


def _tabla_nacional(path: Path, dim: str, semi: str) -> dict[str, float]:
    df = leer(path)
    geo = "Total Nacional"
    d = _filtra(df, Sexo="Total", Nacionalidad="Total", **{"Semiintervalos de edad": semi})
    if "Grupos de edad" in d.columns:
        d = d.filter(pl.col("Grupos de edad").is_null())
    if "Valores simples de edad" in d.columns:
        d = d.filter(pl.col("Valores simples de edad").is_null())
    d = d.filter(pl.col(geo).is_not_null() & (pl.col(dim) != "Total"))
    return {k: v for k, v in d.select(dim, "valor").iter_rows()}


def _cuenta(
    df: pl.DataFrame, var: str, filtro: pl.Expr, mapa: dict[str, list[str] | str]
) -> dict[str, int]:
    vc = dict(df.filter(filtro).group_by(var).len().iter_rows())
    out = {}
    for k, v in mapa.items():
        cats = [v] if isinstance(v, str) else v
        out[k] = sum(vc.get(c, 0) for c in cats)
    return out


def censos() -> list[Cifra]:
    out: list[Cifra] = []
    # ---------------------------------------------------- exhaustivo 2025: exacto
    ex = pl.read_parquet(INTERIM_DIR / "censo_anual_exhaustivo_2025.parquet")
    t = leer(TAB / "ultimo/tabla_67988_ultimo.json")
    ref = "INE, Censo Anual 2025, tabla 67988"
    nac = _filtra(t, Sexo="Total").filter(pl.col("Total Nacional").is_not_null())["valor"][0]
    out.append(
        Cifra(
            "censo_anual_micro_demograficas",
            "2025",
            "Población total",
            "España",
            nac,
            float(ex["personas"].sum()),
            0,
            "exacta",
            ref,
        )
    )
    prov = t.filter(pl.col("Provincias").is_not_null() & (pl.col("Sexo") == "Total")).select(
        pl.col("Provincias__cod").alias("provincia"), "Provincias", "valor"
    )
    pe = dict(ex.group_by("provincia").agg(pl.col("personas").sum()).iter_rows())
    malas = [(n, v, pe.get(c)) for c, n, v in prov.iter_rows() if pe.get(c) != v]
    out.append(
        Cifra(
            "censo_anual_micro_demograficas",
            "2025",
            "Población por provincia",
            f"{prov.height} provincias",
            0,
            float(len(malas)),
            0,
            "exacta",
            ref + " (nº de provincias que no coinciden)",
        )
    )
    sx = dict(
        _filtra(
            t,
        )
        .filter(pl.col("Total Nacional").is_not_null())
        .select("Sexo", "valor")
        .iter_rows()
    )
    es = dict(ex.group_by("sexo").agg(pl.col("personas").sum()).iter_rows())
    out.append(
        Cifra(
            "censo_anual_micro_demograficas",
            "2025",
            "Población por sexo",
            "Mujeres",
            sx["Mujeres"],
            float(es["mujer"]),
            0,
            "exacta",
            ref,
        )
    )
    out.append(
        Cifra(
            "censo_anual_micro_demograficas",
            "2025",
            "Población por sexo",
            "Hombres",
            sx["Hombres"],
            float(es["hombre"]),
            0,
            "exacta",
            ref,
        )
    )

    # ---------------------------------------------------- muestras del Censo Anual
    m24 = pl.read_parquet(INTERIM_DIR / "censo_anual_muestra_2024.parquet")
    r24 = "INE, Censo Anual 2024, tabla {t}"
    out += _proporciones(
        _tabla_nacional(
            TAB / "ultimo/tabla_66601_ultimo.json", "Nivel de formación alcanzado", "15 y más años"
        ),
        _cuenta(m24, "nivel_estudios", pl.col("edad") >= 15, FORMACION),
        fuente="censo_anual_micro_completo",
        edicion="2024",
        cifra="Nivel de formación (15+), %",
        referencia=r24.format(t=66601),
    )
    out += _proporciones(
        _tabla_nacional(
            TAB / "ultimo/tabla_67132_ultimo.json", "Relación con la actividad", "16 y más años"
        ),
        _cuenta(m24, "relacion_actividad", pl.col("edad") >= 16, ACTIVIDAD),
        fuente="censo_anual_micro_completo",
        edicion="2024",
        cifra="Relación con la actividad (16+), %",
        referencia=r24.format(t=67132),
    )
    out += _proporciones(
        _tabla_nacional(TAB / "ultimo/tabla_76291_ultimo.json", "Estado civil", "16 y más años"),
        _cuenta(m24, "estado_civil", pl.col("edad") >= 16, ECIVIL),
        fuente="censo_anual_micro_completo",
        edicion="2024",
        cifra="Estado civil (16+), %",
        referencia=r24.format(t=76291),
    )
    m23 = pl.read_parquet(
        INTERIM_DIR / "censo_anual_muestra_2023.parquet",
        columns=["ocupacion", "relacion_actividad"],
    )
    t69 = leer(TAB / "2023-01-01/tabla_69959_20230101.json")
    t69 = t69.filter(
        pl.col("Total Nacional").is_not_null()
        & (pl.col("Sexo") == "Total")
        & (pl.col("OCUPACIONES") != "Total")
    )
    of = {}
    for nom, cod, v in t69.select("OCUPACIONES", "OCUPACIONES__cod", "valor").iter_rows():
        k = "NC" if nom == "No consta" else cod[0]
        of[k] = of.get(k, 0) + v
    out += _proporciones(
        of,
        dict(
            m23.filter(pl.col("relacion_actividad") == "ocupado")
            .group_by("ocupacion")
            .len()
            .iter_rows()
        ),
        fuente="censo_anual_micro_completo",
        edicion="2023",
        cifra="Ocupados por gran grupo CNO-11, %",
        referencia="INE, Censo Anual 2023, tabla 69959",
    )

    # ---------------------------------------------------- Censo 2021 (sin colectivos)
    c21 = pl.read_parquet(
        INTERIM_DIR / "censo2021_personas.parquet",
        columns=["edad", "nivel_estudios", "relacion_actividad", "estado_civil"],
    )
    r21 = "INE, Censo 2021 (Censo Anual a 01/01/2021), tabla {t}; la muestra excluye colectivos"
    out += _proporciones(
        _tabla_nacional(
            TAB / "2021-01-01/tabla_66601_20210101.json",
            "Nivel de formación alcanzado",
            "15 y más años",
        ),
        _cuenta(c21, "nivel_estudios", pl.col("edad") >= 15, FORMACION),
        fuente="censo2021_micro_hogares",
        edicion="2021",
        cifra="Nivel de formación (15+), %",
        referencia=r21.format(t=66601),
    )
    out += _proporciones(
        _tabla_nacional(
            TAB / "2021-01-01/tabla_67132_20210101.json",
            "Relación con la actividad",
            "16 y más años",
        ),
        _cuenta(c21, "relacion_actividad", pl.col("edad") >= 16, ACTIVIDAD),
        fuente="censo2021_micro_hogares",
        edicion="2021",
        cifra="Relación con la actividad (16+), %",
        referencia=r21.format(t=67132),
    )
    out += _proporciones(
        _tabla_nacional(
            TAB / "2021-01-01/tabla_76291_20210101.json", "Estado civil", "16 y más años"
        ),
        _cuenta(c21, "estado_civil", pl.col("edad") >= 16, ECIVIL),
        fuente="censo2021_micro_hogares",
        edicion="2021",
        cifra="Estado civil (16+), %",
        referencia=r21.format(t=76291),
    )
    return out


def tabla(cifras: list[Cifra]) -> pl.DataFrame:
    return pl.DataFrame([{**asdict(c), "diferencia": c.diferencia, "ok": c.ok} for c in cifras])


# --------------------------------------------------------------------------- encuestas
# Cifras de las notas de prensa del INE (registradas en el manifiesto). La encuesta completa
# debe reproducirlas dentro del redondeo de la publicación (0,05 puntos con un decimal;
# 0,005 con dos; 50 personas en cifras redondeadas a centenas).


def _pct(num: float, den: float) -> float:
    return round(100 * num / den, 4)


def _w(df: pl.DataFrame, cond: pl.Expr, peso: str = "peso") -> float:
    return float(df.filter(cond)[peso].sum())


def encuestas() -> list[Cifra]:
    out: list[Cifra] = []
    # ---------------------------------------------------- EPA 2T2026 (nota de prensa EPA2T26)
    epa = pl.read_parquet(INTERIM_DIR / "epa.parquet")
    ref = "INE, nota de prensa EPA 2T2026"
    oc = _w(epa, pl.col("relacion_actividad_3") == "ocupado")
    pa = _w(epa, pl.col("relacion_actividad_3") == "parado")
    pub = _w(
        epa, (pl.col("relacion_actividad_3") == "ocupado") & (pl.col("sector_publico") == "si")
    )
    out += [
        Cifra("epa", "2T2026", "Ocupados", "España", 22_779_000, round(oc), 50, "exacta", ref),
        Cifra("epa", "2T2026", "Parados", "España", 2_495_300, round(pa), 50, "exacta", ref),
        Cifra(
            "epa",
            "2T2026",
            "Tasa de paro, %",
            "España",
            9.87,
            _pct(pa, oc + pa),
            0.005,
            "exacta",
            ref,
        ),
        Cifra(
            "epa",
            "2T2026",
            "Asalariados del sector público",
            "España",
            3_646_900,
            round(pub),
            50,
            "exacta",
            ref,
        ),
    ]
    # ---------------------------------------------------- ECV 2025 (nota de prensa ECV2025)
    ecv = pl.read_parquet(INTERIM_DIR / "ecv.parquet")
    ref = "INE, nota de prensa ECV 2025"
    v = ecv.filter(pl.col("privacion_material").is_in(["si", "no"]))
    out.append(
        Cifra(
            "ecv",
            "2025",
            "Carencia material y social severa, %",
            "España",
            8.1,
            _pct(_w(v, pl.col("privacion_material") == "si"), v["peso"].sum()),
            0.05,
            "exacta",
            ref,
        )
    )
    d = ecv  # el INE incluye a los «no consta» en el denominador de este porcentaje
    out.append(
        Cifra(
            "ecv",
            "2025",
            "Llega a fin de mes con mucha dificultad, %",
            "España",
            8.5,
            _pct(_w(d, pl.col("dificultad_fin_mes") == "mucha_dificultad"), d["peso"].sum()),
            0.05,
            "exacta",
            ref,
        )
    )
    raw = pl.read_parquet(
        RAW_DIR / "ecv/2025/extraido/ECV_Tr_2025/md_ECV_Tr_2025.parquet",
        columns=["RB050", "vrEU2030_nuevo"],
    )
    out.append(
        Cifra(
            "ecv",
            "2025",
            "Tasa AROPE (lectura del fichero, vrEU2030_nuevo), %",
            "España",
            25.7,
            _pct(_w(raw, pl.col("vrEU2030_nuevo") == "1", "RB050"), raw["RB050"].sum()),
            0.05,
            "exacta",
            ref,
        )
    )
    # ---------------------------------------------------- TIC-H 2025 (nota de prensa TICH2025)
    tic = pl.read_parquet(INTERIM_DIR / "tic_h.parquet").filter(pl.col("edad") <= 74)
    ref = "INE, nota de prensa TIC-H 2025 (población de 16 a 74 años)"
    rtic = pl.read_parquet(
        RAW_DIR / "tic_h/2025/extraido/FicheroCuestionario/md_TICHcuestionario_2025.parquet",
        columns=["EDAD", "ULT_INT", "FACTOR_P"],
    ).filter(pl.col("EDAD").cast(pl.Int32) <= 74)
    out += [
        Cifra(
            "tic_h",
            "2025",
            "Usó internet en los últimos 3 meses, %",
            "España",
            96.3,
            _pct(
                _w(rtic, pl.col("ULT_INT").cast(pl.Utf8) == "1", "FACTOR_P"), rtic["FACTOR_P"].sum()
            ),
            0.05,
            "exacta",
            ref,
        ),
        Cifra(
            "tic_h",
            "2025",
            "Uso diario de internet, %",
            "España",
            92.5,
            _pct(_w(tic, pl.col("uso_internet") == "diario"), tic["peso"].sum()),
            0.05,
            "exacta",
            ref,
        ),
        Cifra(
            "tic_h",
            "2025",
            "Compró por internet en los últimos 3 meses, %",
            "España",
            59.6,
            _pct(_w(tic, pl.col("compra_online") == "si"), tic["peso"].sum()),
            0.05,
            "exacta",
            ref,
        ),
    ]
    # ---------------------------------------------------- ESdE 2023 (nota de prensa ESdE2023)
    ref = "INE, nota de prensa ESdE 2023 (población de 15 y más años)"
    sal = pl.read_parquet(
        RAW_DIR / "encuesta_salud/2023/extraido/ESdEadulto_2023/md_ESdEadulto_2023.parquet",
        columns=["Q1", "C2", "I1", "FACTORADULTO"],
    ).with_columns(pl.col("Q1", "C2", "I1").cast(pl.Utf8))
    w = "FACTORADULTO"
    tot = sal[w].sum()
    q1 = sal.filter(pl.col("Q1") != "9")  # la ESdE excluye «No contesta» del denominador
    c2 = sal.filter(pl.col("C2") != "9")
    out += [
        Cifra(
            "encuesta_salud",
            "2023",
            "Fuma a diario, %",
            "España",
            16.6,
            _pct(_w(q1, pl.col("Q1") == "1", w), q1[w].sum()),
            0.05,
            "exacta",
            ref,
        ),
        Cifra(
            "encuesta_salud",
            "2023",
            "Enfermedad o problema de salud crónico, %",
            "España",
            57.7,
            _pct(_w(c2, pl.col("C2") == "1", w), c2[w].sum()),
            0.05,
            "exacta",
            ref,
        ),
        Cifra(
            "encuesta_salud",
            "2023",
            "Consultó al médico de familia en 4 semanas, %",
            "España",
            22.6,
            _pct(_w(sal, pl.col("I1") == "1", w), tot),
            0.05,
            "exacta",
            ref,
        ),
    ]
    return out


# --------------------------------------------------------------------------- ECP y Padrón


def _total_ine(path: Path, **igual: str) -> float:
    df = leer(path)
    for k, v in igual.items():
        df = df.filter(pl.col(k) == v)
    return float(df["valor"][0])


def ecp_padron() -> list[Cifra]:
    out: list[Cifra] = []
    ecp = RAW_DIR / "ecp/2026-01-01"
    ref = "INE, ECP a 01/01/2026, tabla {t} (total nacional publicado)"
    vf = pl.read_parquet(INTERIM_DIR / "ecp_viviendas_familiares.parquet")
    tot = pl.read_parquet(INTERIM_DIR / "ecp_total.parquet")
    col = pl.read_parquet(INTERIM_DIR / "ecp_colectivos.parquet")
    hog = pl.read_parquet(INTERIM_DIR / "ecp_hogares.parquet")
    nac_vf = _total_ine(
        ecp / "tabla_60124_20260101.json", Sexo="Total", **{"Totales de edad": "Todas las edades"}
    )
    nac_tot = _total_ine(
        ecp / "tabla_59589_20260101.json",
        Sexo="Total",
        **{"Totales de edad": "Todas las edades", "Total Nacional": "Total Nacional"},
    )
    nac_hog = _total_ine(
        ecp / "tabla_60133_20260101.json",
        **{"Composición del hogar": "Total", "Total Nacional": "Total Nacional"},
    )
    out += [
        Cifra(
            "ecp",
            "2026-01-01",
            "Población en viviendas familiares (suma de 52 provincias × sexo × edad × nacionalidad)",
            "España",
            nac_vf,
            float(vf["personas"].sum()),
            0,
            "exacta",
            ref.format(t=60124),
        ),
        Cifra(
            "ecp",
            "2026-01-01",
            "Población residente (suma de 52 provincias × sexo × edad)",
            "España",
            nac_tot,
            float(tot["personas"].sum()),
            0,
            "exacta",
            ref.format(t=59589),
        ),
        Cifra(
            "ecp",
            "2026-01-01",
            "Hogares (suma de 52 provincias × tamaño)",
            "España",
            nac_hog,
            float(hog["hogares"].sum()),
            0,
            "exacta",
            ref.format(t=60133),
        ),
        Cifra(
            "ecp",
            "2026-01-01",
            "Población en establecimientos colectivos (total − familiares)",
            "España",
            nac_tot - nac_vf,
            float(col["personas"].sum()),
            0,
            "exacta",
            ref.format(t="59589 − 60124"),
        ),
    ]
    # Padrón municipal (tabla 29005) frente a la tabla provincial (2852)
    from sinpop.harmonize.censos import poblacion_municipal

    pm = poblacion_municipal()
    t2852 = leer(RAW_DIR / "padron_continuo/ultimo/tabla_2852_ultimo.json")
    t2852 = t2852.filter(pl.col("Sexo") == "Total")
    nac = float(t2852.filter(pl.col("Total Nacional").is_not_null())["valor"][0])
    prov = dict(
        t2852.filter(pl.col("Provincias").is_not_null())
        .select("Provincias__cod", "valor")
        .iter_rows()
    )
    sm = dict(pm.group_by("CPRO").agg(pl.col("poblacion").sum()).iter_rows())
    malas = [p for p, v in prov.items() if sm.get(p) != v]
    ref = "INE, Padrón a 01/01/2025: tabla 29005 (municipios) frente a tabla 2852 (provincias)"
    out += [
        Cifra(
            "padron_continuo",
            "2025-01-01",
            "Población (suma de municipios)",
            "España",
            nac,
            float(pm["poblacion"].sum()),
            0,
            "exacta",
            ref,
        ),
        Cifra(
            "padron_continuo",
            "2025-01-01",
            "Provincias cuya suma municipal no coincide",
            f"{len(prov)} provincias",
            0,
            float(len(malas)),
            0,
            "exacta",
            ref,
        ),
        Cifra(
            "padron_continuo",
            "2025-01-01",
            "Número de municipios",
            "España",
            8132,
            float(pm.height),
            0,
            "exacta",
            "INE, tabla 29005 (8.132 municipios con dato)",
        ),
    ]
    return out


def todas() -> list[Cifra]:
    return censos() + encuestas() + ecp_padron()
