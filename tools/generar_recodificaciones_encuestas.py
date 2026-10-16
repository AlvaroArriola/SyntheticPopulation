"""Genera las tablas de recodificación de las encuestas (ECV, EPA, TIC-H, ESdE) en
`configs/variables.yaml` (F2). Fuente de los códigos: los diseños de registro oficiales
(JSON/Excel del INE) citados en `verificado_contra`. Decisiones: D-028.

Uso: python tools/generar_recodificaciones_encuestas.py
"""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

ECV = "disreg_ecv25 / dr_ECV_SM_T*_2025.json (INE)"
EPA = "dr_EPA_2026.json (INE)"
TIC = "dr_TICHcuestionario_2025.json (INE)"
SAL = "dr_ESdEadulto_2023.json (INE)"

NUTS_CCAA = {
    "ES61": "01",
    "ES24": "02",
    "ES12": "03",
    "ES53": "04",
    "ES70": "05",
    "ES13": "06",
    "ES41": "07",
    "ES42": "08",
    "ES51": "09",
    "ES52": "10",
    "ES43": "11",
    "ES11": "12",
    "ES30": "13",
    "ES62": "14",
    "ES22": "15",
    "ES21": "16",
    "ES23": "17",
    "ES63": "18",
    "ES64": "19",
}
CCAA_19 = {f"{i:02d}": f"{i:02d}" for i in range(1, 20)}
EPA_CCAA = {**{f"{i:02d}": f"{i:02d}" for i in range(1, 18)}, "51": "18", "52": "19"}

TABLAS: dict[str, dict[str, tuple[str, dict[str, str], str, str | None]]] = {
    # variable -> fuente -> (variable_original, recodificación, verificado_contra, notas)
    "sexo": {
        "ecv": ("RB090", {"1": "hombre", "2": "mujer"}, ECV, None),
        "epa": ("SEXO1", {"1": "hombre", "6": "mujer"}, EPA, None),
        "tic_h": ("SEXO", {"1": "hombre", "6": "mujer"}, TIC, None),
        "encuesta_salud": ("SEXOa", {"1": "hombre", "2": "mujer"}, SAL, None),
    },
    "ccaa": {
        "ecv": ("DB040", NUTS_CCAA, ECV, "región NUTS-2 → código INE de CCAA"),
        "epa": ("CCAA", EPA_CCAA, EPA, "51 Ceuta → 18; 52 Melilla → 19"),
        "tic_h": ("CCAA", CCAA_19, TIC, None),
        "encuesta_salud": ("CCAA", CCAA_19, SAL, None),
    },
    "nacionalidad_esp_ext": {
        "ecv": ("RB290", {"1": "espanola", "2": "extranjera", "3": "extranjera"}, ECV, None),
        "epa": (
            "NAC1",
            {"1": "espanola", "2": "espanola", "3": "extranjera"},
            EPA,
            "2 = española y doble nacionalidad → española",
        ),
        "tic_h": (
            "NACIONALIDAD",
            {"1": "espanola", "2": "extranjera", "3": "espanola", "4": "extranjera"},
            TIC,
            "3 = española y otra → española; 4 = ninguna (apátrida) → extranjera",
        ),
        "encuesta_salud": (
            "A2a_1",
            {"1": "espanola", "2": "extranjera"},
            SAL,
            "A2a_1 = 1 si tiene nacionalidad española",
        ),
    },
    "estudios_3": {
        "ecv": (
            "PE041",
            {
                "000": "hasta_obligatoria",
                "100": "hasta_obligatoria",
                "200": "hasta_obligatoria",
                "340": "secundaria_2a_etapa",
                "344": "secundaria_2a_etapa",
                "350": "secundaria_2a_etapa",
                "353": "secundaria_2a_etapa",
                "354": "secundaria_2a_etapa",
                "450": "secundaria_2a_etapa",
                "500": "superior",
            },
            ECV,
            None,
        ),
        "epa": (
            "NFORMA",
            {
                "AN": "hasta_obligatoria",
                "P1": "hasta_obligatoria",
                "P2": "hasta_obligatoria",
                "S1": "hasta_obligatoria",
                "SG": "secundaria_2a_etapa",
                "SP": "secundaria_2a_etapa",
                "SU": "superior",
            },
            EPA,
            None,
        ),
        "tic_h": (
            "NIVELEST",
            {
                "0": "hasta_obligatoria",
                "1": "hasta_obligatoria",
                "2": "hasta_obligatoria",
                "3": "secundaria_2a_etapa",
                "4": "secundaria_2a_etapa",
                "5": "superior",
                "6": "superior",
                "7": "superior",
                "8": "superior",
                "9": "NC",
            },
            TIC,
            "9 = no se puede codificar → NC",
        ),
        "encuesta_salud": (
            "NIVEST",
            {
                "02": "hasta_obligatoria",
                "03": "hasta_obligatoria",
                "04": "hasta_obligatoria",
                "05": "hasta_obligatoria",
                "06": "secundaria_2a_etapa",
                "07": "secundaria_2a_etapa",
                "08": "superior",
                "09": "superior",
                "01": "NP",
                "99": "hasta_obligatoria",
            },
            SAL,
            "99: el diseño lo llama «No contesta», pero el fichero no usa el 03 (primaria "
            "incompleta) y el 99 reproduce el nivel básico de la tabla oficial 71335 (D-034)",
        ),
    },
    "relacion_actividad": {
        "ecv": (
            "PL032",
            {
                "1": "ocupado",
                "2": "parado",
                "3": "jubilado_pensionista",
                "4": "incapacidad_permanente",
                "5": "estudiante",
                "6": "otra_inactividad",
                "8": "otra_inactividad",
                "7": "NC",
            },
            ECV,
            "6 = labores del hogar → otra_inactividad (D-018); 7 = sin cuestionario → NC",
        ),
        "tic_h": (
            "SIT_LAB",
            {
                "1": "ocupado",
                "2": "ocupado",
                "3": "ocupado",
                "4": "ocupado",
                "5": "parado",
                "6": "estudiante",
                "7": "jubilado_pensionista",
                "8": "incapacidad_permanente",
                "9": "otra_inactividad",
                "0": "otra_inactividad",
            },
            TIC,
            "9 = labores del hogar → otra_inactividad",
        ),
    },
    "relacion_actividad_3": {
        "epa": (
            "AOI",
            {
                "03": "ocupado",
                "04": "ocupado",
                "05": "parado",
                "06": "parado",
                "07": "inactivo",
                "08": "inactivo",
                "09": "inactivo",
            },
            EPA,
            "clasificación OIT; la EPA no distingue los tipos de inactividad del Censo",
        ),
    },
    "situacion_profesional": {
        "epa": (
            "SITU",
            {
                "01": "empresario",
                "03": "autonomo",
                "05": "otra",
                "06": "otra",
                "07": "asalariado",
                "08": "asalariado",
                "09": "otra",
            },
            EPA,
            "la EPA no separa indefinido/temporal en SITU (va en DUCON1)",
        ),
    },
    "sector_publico": {
        "epa": (
            "SITU",
            {"07": "si", "08": "no", "01": "no", "03": "no", "05": "no", "06": "no", "09": "no"},
            EPA,
            "07 = asalariado del sector público",
        ),
    },
    "tipo_jornada": {"epa": ("PARCO1", {"1": "completa", "6": "parcial"}, EPA, None)},
    "ocupacion": {"epa": ("OCUP1", {str(i): str(i) for i in range(10)}, EPA, None)},
    "salud_autopercibida": {
        "ecv": (
            "PH010",
            {"1": "muy_buena", "2": "buena", "3": "regular", "4": "mala", "5": "muy_mala"},
            ECV,
            None,
        ),
        "encuesta_salud": (
            "C1",
            {"1": "muy_buena", "2": "buena", "3": "regular", "4": "mala", "5": "muy_mala"},
            SAL,
            None,
        ),
    },
    "discapacidad_limitacion": {
        "ecv": (
            "PH030",
            {"1": "limitacion_grave", "2": "limitacion_moderada", "3": "sin_limitacion"},
            ECV,
            None,
        ),
        "encuesta_salud": (
            "C3a",
            {"1": "limitacion_grave", "2": "limitacion_moderada", "3": "sin_limitacion", "9": "NC"},
            SAL,
            None,
        ),
    },
    "tenencia_vivienda": {
        "ecv": (
            "HH021",
            {
                "1": "propiedad_sin_hipoteca",
                "2": "propiedad_con_hipoteca",
                "3": "alquiler_mercado",
                "4": "alquiler_inferior_cesion",
                "5": "alquiler_inferior_cesion",
            },
            ECV,
            "5 = cesión gratuita",
        ),
    },
    "dificultad_fin_mes": {
        "ecv": (
            "HS120",
            {
                "1": "mucha_dificultad",
                "2": "dificultad",
                "3": "cierta_dificultad",
                "4": "cierta_facilidad",
                "5": "facilidad",
                "6": "mucha_facilidad",
            },
            ECV,
            None,
        ),
    },
    "vehiculo_hogar": {"ecv": ("HS110", {"1": "si", "2": "no", "3": "no"}, ECV, None)},
    "privacion_material": {
        "ecv": (
            "vrMATSOCDEP",
            {"1": "si", "0": "no", "9": "NP"},
            ECV,
            "carencia material y social severa (indicador oficial UE desde 2021)",
        ),
    },
    "uso_internet": {
        "tic_h": (
            "ULT_INT + FREC_INT",
            {
                "4|": "nunca",
                "3|": "menos_frecuente",
                "2|": "menos_frecuente",
                "1|1": "diario",
                "1|2": "diario",
                "1|3": "semanal",
                "1|4": "menos_frecuente",
            },
            TIC,
            "clave = ULT_INT|FREC_INT; FREC_INT solo para quien usó internet en 3 meses",
        ),
    },
    "compra_online": {
        "tic_h": (
            "ULT_COM",
            {"1": "si", "2": "no", "3": "no", "4": "no"},
            TIC,
            "compra en los últimos 3 meses; vacío = no ha usado internet → no",
        ),
    },
    "teletrabajo": {
        "tic_h": (
            "TELETRAB + ULT_TTRAB + TTRAB_ACTUAL",
            {
                "6|": "nunca",
                "1|1": "habitual",
                "1|2": "habitual",
                "1|3": "habitual",
                "1|4": "habitual",
                "1|5": "habitual",
                "1|6": "ocasional",
                "1|7": "ocasional",
            },
            TIC,
            "clave = ULT_TTRAB|TTRAB_ACTUAL; TELETRAB = 6 (el trabajo exige presencia, no se "
            "pregunta ULT_TTRAB) → clave 6| → nunca; habitual = 2 días o más por semana",
        ),
    },
}

NUEVAS = {
    "nacionalidad_esp_ext": {
        "prioridad": "P1",
        "nivel": "persona",
        "tipo": "categorica",
        "descripcion": "Nacionalidad española o extranjera (llave común con las encuestas)",
        "categorias": ["espanola", "extranjera"],
        "fuente_principal": "censo / encuestas",
        "derivada_de": "nacionalidad_grupo",
    },
    "relacion_actividad_3": {
        "prioridad": "P1",
        "nivel": "persona",
        "tipo": "categorica",
        "descripcion": "Relación con la actividad en tres grupos (llave común con la EPA)",
        "categorias": ["ocupado", "parado", "inactivo"],
        "fuente_principal": "censo / epa",
        "derivada_de": "relacion_actividad",
    },
    "sector_publico": {
        "prioridad": "P2",
        "nivel": "persona",
        "tipo": "categorica",
        "descripcion": "Asalariado del sector público (D-018.2)",
        "categorias": ["si", "no"],
        "fuente_principal": "epa",
    },
}


def main() -> None:
    path = ROOT / "configs/variables.yaml"
    hdr = path.read_text(encoding="utf-8").split("variables:")[0]
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    V = raw["variables"]
    for k, v in NUEVAS.items():
        V.setdefault(k, v)
    # Categorías ajustadas para que las encuestas encajen (D-028)
    V["situacion_profesional"]["categorias"] = [
        "empresario",
        "autonomo",
        "asalariado_indefinido",
        "asalariado_temporal",
        "asalariado",
        "otra",
    ]
    for b in ("compra_online", "privacion_material", "vehiculo_hogar"):
        V[b]["tipo"] = "categorica"
        V[b]["categorias"] = ["si", "no"]
    for var, fuentes in TABLAS.items():
        for src, (orig, rec, ver, notas) in fuentes.items():
            f = V[var].setdefault("fuentes", {}).get(src, {})
            f.update({"variable_original": orig, "verificado_contra": ver, "recodificacion": rec})
            if notas:
                f["notas"] = notas
            V[var]["fuentes"][src] = f
    path.write_text(
        hdr + yaml.safe_dump(raw, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
