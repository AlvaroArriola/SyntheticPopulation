"""Genera las tablas de recodificación de los censos en `configs/variables.yaml` (F2).

Las tablas se construyen a partir de los diccionarios oficiales del INE (diseños de
registro del Censo 2021 y del Censo Anual) y de las agrupaciones documentadas en
DECISIONS.md (D-025). Una vez escritas, la fuente de verdad es `variables.yaml`: este
script solo deja constancia de cómo se generaron y se puede volver a ejecutar.

Uso: python tools/generar_recodificaciones_censos.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from sinpop.ingest.readers import codelists_from_xlsx  # noqa: E402

RAW = ROOT / "data/raw"
C21 = json.loads(
    (RAW / "censo2021_micro_hogares/2021/extraido/dr_CensoPersonas_2021.json").read_text(
        encoding="utf-8"
    )
)["codelists"]
CA = codelists_from_xlsx(
    RAW / "censo_anual_micro_completo/2024/extraido/dr_CensoAnual_muestra_2022.xlsx"
)
CEX = json.loads(
    (RAW / "censo_anual_micro_demograficas/2025/extraido/dr_CensoAnual_2026.json").read_text(
        encoding="utf-8"
    )
)["codelists"]

# ---------------------------------------------------------------- países (D-025)
# Estados miembros de la UE-27 distintos de España, por su nombre en los diccionarios INE.
UE = {
    "Alemania",
    "Austria",
    "Bélgica",
    "Bulgaria",
    "Chipre",
    "Croacia",
    "Dinamarca",
    "República Eslovaca",
    "Eslovenia",
    "Estonia",
    "Finlandia",
    "Francia",
    "Grecia",
    "Hungría",
    "Irlanda",
    "Italia",
    "Letonia",
    "Lituania",
    "Luxemburgo",
    "Malta",
    "Países Bajos",
    "Polonia",
    "Portugal",
    "República Checa",
    "Rumanía",
    "Suecia",
    "Otros países de la Unión Europea",
}
NORTEAMERICA = {"Canadá", "Estados Unidos de América"}
TOP15 = [
    "228",
    "343",
    "128",
    "351",
    "115",
    "125",
    "348",
    "407",
    "135",
    "321",
    "340",
    "345",
    "126",
    "110",
    "347",
]  # 15 nacionalidades extranjeras más numerosas, Censo Anual 2025


def grupo_pais(codigo: str, nombre: str, *, nacimiento: bool) -> str:
    if codigo == "108":
        return "espana" if nacimiento else "espanola"
    if nombre in UE:
        return "ue"
    c = codigo[0]
    if c == "1":
        return "resto_europa"
    if c == "2":
        return "africa"
    if c == "3":
        return "otros" if nombre in NORTEAMERICA else "america_latina"
    if c == "4":
        return "asia"
    return "otros"  # Oceanía (5xx), apátridas (555), antiguos territorios (966)


def slug(nombre: str) -> str:
    import unicodedata

    s = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode().lower()
    return "".join(ch if ch.isalnum() else "_" for ch in s).strip("_")


def paises(cl: dict, *, nacimiento: bool) -> dict[str, str]:
    return {
        k: grupo_pais(k, v, nacimiento=nacimiento)
        for k, v in cl.items()
        if k[0] in "123459" and k != "999"
    }


def top(cl: dict) -> dict[str, str]:
    out = {}
    for k, v in cl.items():
        if k == "108":
            out[k] = "espanola"
        elif k in TOP15:
            out[k] = slug(v)
        elif k[0] in "123459" and k != "999":
            out[k] = "otras_extranjeras"
    return out


# ---------------------------------------------------------------- tablas comunes
CNEDA = {
    "01": "analfabetos",
    "02": "primaria_incompleta",
    "03": "primaria",
    "04": "secundaria_1a_etapa",
    "05": "bachillerato",
    "06": "fp_grado_medio",
    "07": "postsecundaria_no_superior",
    "08": "fp_grado_superior",
    "09": "grado_240",
    "10": "grado_mas_240_licenciatura",
    "11": "master",
    "12": "doctorado",
}
ESTUDIOS3 = {
    "01": "hasta_obligatoria",
    "02": "hasta_obligatoria",
    "03": "hasta_obligatoria",
    "04": "hasta_obligatoria",
    "05": "secundaria_2a_etapa",
    "06": "secundaria_2a_etapa",
    "07": "secundaria_2a_etapa",
    "08": "superior",
    "09": "superior",
    "10": "superior",
    "11": "superior",
    "12": "superior",
}
ECIVIL = {"0": "NC", "1": "soltero", "2": "casado", "3": "viudo", "4": "separado_divorciado"}
SITU = {
    "1": "empresario",
    "2": "autonomo",
    "3": "asalariado_indefinido",
    "4": "asalariado_temporal",
    "5": "otra",
}
SEXO = {"1": "hombre", "6": "mujer"}
DEGURBA = {"1": "ciudad", "2": "intermedio", "3": "rural"}
LLEGADA = {
    "0001": "antes_1981",
    "0002": "1981_1990",
    "0003": "1991_2000",
    "0004": "2001_2010",
    "0005": "2011_2015",
    "9999": "NP",
}
LLEGADA.update({str(y): "2016_2020" for y in range(2016, 2021)})
LLEGADA.update({str(y): "2021_o_despues" for y in range(2021, 2031)})
# CNAE-2009: división (2 dígitos) -> sección
SECCIONES = [
    ("A", 1, 3),
    ("B", 5, 9),
    ("C", 10, 33),
    ("D", 35, 35),
    ("E", 36, 39),
    ("F", 41, 43),
    ("G", 45, 47),
    ("H", 49, 53),
    ("I", 55, 56),
    ("J", 58, 63),
    ("K", 64, 66),
    ("L", 68, 68),
    ("M", 69, 75),
    ("N", 77, 82),
    ("O", 84, 84),
    ("P", 85, 85),
    ("Q", 86, 88),
    ("R", 90, 93),
    ("S", 94, 96),
    ("T", 97, 98),
    ("U", 99, 99),
]


def cnae_seccion(cl: dict) -> dict[str, str]:
    out = {}
    for k in cl:
        if k == "XX":
            out[k] = "NC"
            continue
        d = int(k)
        out[k] = next(s for s, a, b in SECCIONES if a <= d <= b)
    return out


def cno_1d(cl: dict) -> dict[str, str]:
    return {k: ("NC" if k == "XX" else k[0]) for k in cl}


def tamano_muni(cl: dict) -> dict[str, str]:
    return {"991": "hasta_2000", "992": "de_2001_a_10000", "993": "de_2001_a_10000"}


def main() -> None:
    path = ROOT / "configs/variables.yaml"
    hdr = path.read_text(encoding="utf-8").split("variables:")[0]
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    V = raw["variables"]

    # Dominios fijados en F2 (D-025)
    V["nacionalidad_grupo"]["categorias"] = [
        "espanola",
        "ue",
        "resto_europa",
        "africa",
        "america_latina",
        "asia",
        "otros",
    ]
    V["nacionalidad_top"].pop("dominio_pendiente", None)
    V["nacionalidad_top"]["categorias"] = (
        ["espanola"] + [slug(C21["T_PAIS"][k]) for k in TOP15] + ["otras_extranjeras"]
    )
    V["nivel_estudios"].pop("dominio_pendiente", None)
    V["nivel_estudios"]["categorias"] = list(CNEDA.values())
    V["relacion_actividad"]["categorias"] = [
        "ocupado",
        "parado",
        "jubilado_pensionista",
        "incapacidad_permanente",
        "estudiante",
        "otra_inactividad",
    ]
    V["situacion_profesional"]["categorias"] = list(SITU.values())
    V["anio_llegada_espana"].pop("dominio_pendiente", None)
    V["anio_llegada_espana"]["categorias"] = [
        "antes_1981",
        "1981_1990",
        "1991_2000",
        "2001_2010",
        "2011_2015",
        "2016_2020",
        "2021_o_despues",
    ]
    V["edad_5"]["categorias"] = V["edad_5"]["categorias"][:-1] + ["85-89", "90+"]
    V["tamano_municipio"]["categorias"] = [
        "hasta_2000",
        "de_2001_a_10000",
        "de_10001_a_50000",
        "de_50001_a_100000",
        "de_100001_a_500000",
        "mas_de_500000",
    ]
    V["tenencia_censo"] = {
        "prioridad": "P1",
        "nivel": "hogar",
        "tipo": "categorica",
        "descripcion": "Régimen de tenencia según el Censo (D-018.3)",
        "categorias": ["propiedad", "alquiler", "otro"],
        "fuente_principal": "censo2021",
    }

    def put(var: str, src: str, orig: str, rec: dict, ver: str, notas: str | None = None) -> None:
        f = V[var].setdefault("fuentes", {}).get(src, {})
        f.update({"variable_original": orig, "verificado_contra": ver, "recodificacion": rec})
        if notas:
            f["notas"] = notas
        V[var]["fuentes"][src] = f

    for src, cl, ver in [
        ("censo2021_micro_hogares", C21, "dr_CensoPersonas_2021.json (INE)"),
        ("censo_anual_micro_completo", CA, "dr_CensoAnual_muestra_2022.xlsx (INE)"),
    ]:
        put("sexo", src, "SEXO", SEXO, ver)
        put("nacionalidad_grupo", src, "PNACIO", paises(cl["T_PAIS"], nacimiento=False), ver)
        put("pais_nacimiento_grupo", src, "PNACIM", paises(cl["T_PAIS"], nacimiento=True), ver)
        put("nacionalidad_top", src, "PNACIO", top(cl["T_PAIS"]), ver)
        put("estado_civil", src, "ECIVIL", ECIVIL, ver, "0 = No consta → NC; NP para menores de 16")
        put(
            "nivel_estudios",
            src,
            "ESREAL_CNEDA" if src.startswith("censo2021") else "ESREAL",
            CNEDA,
            ver,
            "en blanco = no aplica (menores de 15) → NP",
        )
        put(
            "estudios_3",
            src,
            "ESREAL_CNEDA" if src.startswith("censo2021") else "ESREAL",
            ESTUDIOS3,
            ver,
            "en blanco = no aplica (menores de 15) → NP",
        )
        put(
            "ocupacion",
            src,
            "OCU63" if src.startswith("censo2021") else "CNO",
            cno_1d(cl["T_CNO"]),
            ver,
            "primer dígito del código CNO-11; XX = No consta → NC",
        )
        put(
            "sector_actividad",
            src,
            "ACT89" if src.startswith("censo2021") else "CNAE",
            cnae_seccion(cl["T_CNAE"]),
            ver,
            "división CNAE-09 → sección; XX = No consta → NC",
        )
        put("situacion_profesional", src, "SITU", SITU, ver, "en blanco = no ocupado → NP")
        put(
            "anio_llegada_espana",
            src,
            "VARANOE",
            LLEGADA,
            ver,
            "los años desde 2016 vienen como año literal; 9999 = siempre en España → NP",
        )
        put(
            "grado_urbanizacion",
            src,
            "TIPO_MUN_DEGURBA" if src.startswith("censo2021") else "DEGURBA",
            DEGURBA,
            ver,
        )
        put(
            "tamano_municipio",
            src,
            "CMUN",
            tamano_muni(cl),
            ver,
            "991–993 = tamaño; el resto son municipios ≥10.000 hab. y se clasifican con la "
            "población municipal del Censo Anual exhaustivo 2025",
        )

    put(
        "relacion_actividad",
        "censo2021_micro_hogares",
        "RELA",
        {
            "1": "ocupado",
            "2": "parado",
            "4": "incapacidad_permanente",
            "5": "jubilado_pensionista",
            "6": "otra_inactividad",
            "7": "estudiante",
        },
        "dr_CensoPersonas_2021.json (INE)",
        "en blanco = menores de 16 → NP",
    )
    put(
        "relacion_actividad",
        "censo_anual_micro_completo",
        "RELA",
        {
            "01": "ocupado",
            "02": "parado",
            "03": "incapacidad_permanente",
            "04": "jubilado_pensionista",
            "05": "otra_inactividad",
            "06": "estudiante",
        },
        "dr_CensoAnual_muestra_2022.xlsx (INE)",
        "en blanco = menores de 16 → NP",
    )
    put(
        "tenencia_censo",
        "censo2021_micro_hogares",
        "TENEN_VIV",
        {"2": "propiedad", "3": "alquiler", "4": "otro", "9": "NC"},
        "dr_CensoPersonas_2021.json (INE)",
    )

    ver = "dr_CensoAnual_2026.json (INE)"
    src = "censo_anual_micro_demograficas"
    put("sexo", src, "SEXO", SEXO, ver)
    put("nacionalidad_grupo", src, "PNACIO", paises(CEX["T_PAIS"], nacimiento=False), ver)
    put("pais_nacimiento_grupo", src, "PNACIM", paises(CEX["T_PAIS"], nacimiento=True), ver)
    put("nacionalidad_top", src, "PNACIO", top(CEX["T_PAIS"]), ver)
    put("grado_urbanizacion", src, "DEGURBA", DEGURBA, ver)
    put("tamano_municipio", src, "CMUN", tamano_muni(CEX), ver)

    path.write_text(
        hdr + yaml.safe_dump(raw, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
