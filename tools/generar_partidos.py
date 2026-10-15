"""Genera `configs/partidos.yaml` (F2, G2.7). Decisiones: D-030.

- Candidaturas de las generales de 2023: las siglas de las hojas municipales del Ministerio
  del Interior (`data/interim/elecciones_generales_2023_votos.parquet`), su ámbito (provincias
  donde se presentan) y su familia.
- Catálogo de códigos de partido de cada estudio del CIS usado (etiquetas de valores de los
  ficheros .sav, solo metadatos): cada código recibe una familia o un tipo especial.

Criterios de familia (los mismos para todos los electorados):
1. Partidos de ámbito estatal: por su posición, si han tenido representación en el Congreso o
   en el Parlamento Europeo desde 2015 (izquierda estatal, socialdemócrata, centro-derecha
   estatal, derecha radical). Sin esa representación: «otros».
2. Federaciones, marcas territoriales y coaliciones encabezadas por un partido estatal: la
   familia de ese partido (PSC → socialdemócrata; En Comú, Más Madrid → izquierda estatal).
3. Partidos que solo se presentan en una comunidad, provincia o municipio, sin vínculo con un
   partido estatal: «nacionalistas y regionalistas», con desglose por territorio.
4. Siglas cuyo nombre completo no se ha podido verificar con la publicación oficial (BOE, no
   accesible desde el entorno): se aplica el criterio 3 por su ámbito y se marca en `notas`.

Uso: python tools/generar_partidos.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import polars as pl
import pyreadstat
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sinpop.harmonize.core import ccaa_de_provincia  # noqa: E402

IZQ, SOC, CDE, DRA, NAC, OTR = (
    "izquierda_estatal",
    "socialdemocrata",
    "centro_derecha_estatal",
    "derecha_radical",
    "nacionalista_regionalista",
    "otros",
)

# ----------------------------------------------------------------- generales 2023
# siglas → (nombre, familia, códigos del estudio 3567 en RECUVOTOG/RECUERDO, notas)
CANDIDATURAS_2023: dict[str, tuple[str, str, list[int], str | None]] = {
    "PP": ("Partido Popular", CDE, [2], None),
    "PSOE": ("Partido Socialista Obrero Español", SOC, [1], None),
    "PSC": ("Partit dels Socialistes de Catalunya", SOC, [1], "federación del PSOE en Cataluña"),
    "PSdeG- PSOE": ("Partido dos Socialistas de Galicia-PSOE", SOC, [1], "federación del PSOE"),
    "PSE-EE (PSOE)": (
        "Partido Socialista de Euskadi-Euskadiko Ezkerra",
        SOC,
        [1],
        "federación del PSOE",
    ),
    "PSIB-PSOE": ("Partit Socialista de les Illes Balears-PSOE", SOC, [1], "federación del PSOE"),
    "PSN-PSOE": ("Partido Socialista de Navarra-PSOE", SOC, [1], "federación del PSOE"),
    "VOX": ("VOX", DRA, [3], None),
    "SUMAR": ("Sumar", IZQ, [21], "coalición de Movimiento Sumar, IU, Más País y otros"),
    "SUMAR - ECP": (
        "Sumar-En Comú Podem",
        IZQ,
        [21],
        "marca de Sumar en Cataluña; el CIS la recoge como Sumar",
    ),
    "SUMAR - COMPROMÍS": (
        "Sumar-Compromís",
        IZQ,
        [21],
        "Compromís concurrió dentro de Sumar en la Comunitat Valenciana",
    ),
    "MÉS PER MALLORCA- MÉS PER MENORCA- SUMAR": (
        "Més per Mallorca-Més per Menorca-Sumar",
        IZQ,
        [21],
        "marca de Sumar en Illes Balears",
    ),
    "SUMAR ARAGÓN": ("Sumar Aragón", IZQ, [21], "marca de Sumar en Aragón"),
    "ERC": ("Esquerra Republicana de Catalunya", NAC, [901], None),
    "JxCAT - JUNTS": ("Junts per Catalunya", NAC, [902], None),
    "EH Bildu": ("Euskal Herria Bildu", NAC, [1602], None),
    "EAJ-PNV": ("Euzko Alderdi Jeltzalea-Partido Nacionalista Vasco", NAC, [1601], None),
    "B.N.G.": ("Bloque Nacionalista Galego", NAC, [1201], None),
    "CCa": ("Coalición Canaria", NAC, [503], None),
    "U.P.N.": ("Unión del Pueblo Navarro", NAC, [1501], None),
    "PACMA": ("Partido Animalista con el Medio Ambiente", OTR, [6], None),
    "NC-bc": ("Nueva Canarias-Bloque Canarista", NAC, [8995], None),
    "CUP-PR": ("Candidatura d'Unitat Popular-Per la Ruptura", NAC, [8995], None),
    "PDeCAT-E- CiU": ("Partit Demòcrata Europeu Català-Espai CiU", NAC, [8995], None),
    "U.P.L.": ("Unión del Pueblo Leonés", NAC, [8995], None),
    "EXISTE": ("Existe (Teruel Existe / Aragón Existe)", NAC, [8995], None),
    "GBAI": ("Geroa Bai", NAC, [8995], None),
    "SY": ("Soria ¡Ya!", NAC, [8995], None),
    "ADELANTE ANDALUCÍA": ("Adelante Andalucía", NAC, [8995], None),
    "JM+": ("Jaén Merece Más", NAC, [8995], None),
    "XAV": ("Por Ávila", NAC, [8995], None),
    "PAR": ("Partido Aragonés", NAC, [8995], None),
    "ESPAÑA VACIADA": ("España Vaciada", NAC, [8995], None),
    "ASTURIAS EXISTE EV": ("Asturias Existe-España Vaciada", NAC, [8995], None),
    "XH": ("Por Huelva", NAC, [8995], None),
    "Zsi": ("Zamora Sí", NAC, [8995], None),
    "VB": ("Vía Burgalesa", NAC, [8995], None),
    "AHORA CANARIAS- PCPC": (
        "Ahora Canarias-Partido Comunista del Pueblo Canario",
        NAC,
        [8995],
        None,
    ),
    "CpM": ("Coalición por Melilla", NAC, [8995], None),
    "EV-PCAS- TC": ("España Vaciada-Partido Castellano-Tierra Comunera", NAC, [8995], None),
    "JxG": ("Juntos por Granada", NAC, [8995], None),
    "PREPAL": ("Partido Regionalista del País Leonés", NAC, [8995], None),
    "FO": ("Frente Obrero", OTR, [8995], None),
    "RECORTES CERO": ("Recortes Cero", OTR, [8995], None),
    "PUM+J": ("Por un Mundo Más Justo", OTR, [8995], None),
    "PCTE": ("Partido Comunista de los Trabajadores de España", OTR, [8995], None),
    "PCTC": (
        "Partit Comunista dels Treballadors de Catalunya",
        OTR,
        [8995],
        "marca territorial del PCTE",
    ),
    "PCTG": (
        "Partido Comunista dos Traballadores de Galiza",
        OTR,
        [8995],
        "marca territorial del PCTE",
    ),
    "PCTE/ELAK": ("PCTE/ELAK", OTR, [8995], "marca territorial del PCTE"),
    "ESCAÑOS EN BLANCO": ("Escaños en Blanco", OTR, [8995], None),
    "ESCONS EN BLANC": ("Escons en Blanc", OTR, [8995], "marca de Escaños en Blanco en catalán"),
    "CJ": ("Caminando Juntos", OTR, [8995], None),
    "FE de las JONS": ("Falange Española de las JONS", OTR, [8995], None),
    "PH": ("Partido Humanista", OTR, [8995], None),
}

# ----------------------------------------------------------------- catálogo CIS
FAMILIA_CIS: dict[int, tuple[str, str | None]] = {
    1: (SOC, None),
    2: (CDE, None),
    3: (DRA, None),
    4: (IZQ, None),
    5: (CDE, None),
    6: (OTR, None),
    7: (IZQ, None),
    8: (IZQ, None),
    9: (IZQ, None),
    10: (OTR, None),
    11: (IZQ, "concurrió en coaliciones con representación (Compromís-Q 2011, Más País 2019)"),
    12: (OTR, None),
    13: (OTR, None),
    14: (OTR, None),
    15: (OTR, None),
    16: (OTR, None),
    17: (OTR, None),
    18: (CDE, "representación en el Congreso 2008–2015"),
    19: (OTR, None),
    20: (OTR, None),
    21: (IZQ, None),
    22: (OTR, None),
    23: (OTR, None),
    24: (OTR, None),
    25: (OTR, None),
    26: (OTR, None),
    27: (OTR, None),
    28: (DRA, "representación en el Parlamento Europeo desde 2024"),
    29: (OTR, "etiqueta genérica del CIS sin partido identificable"),
    101: (NAC, None),
    102: (NAC, None),
    103: (IZQ, "coalición de IU, Podemos y Más País en Andalucía"),
    104: (NAC, None),
    105: (NAC, None),
    106: (NAC, None),
    107: (NAC, None),
    201: (NAC, None),
    202: (NAC, None),
    203: (NAC, None),
    204: (IZQ, "confluencia municipal con IU y Podemos"),
    205: (IZQ, None),
    206: (IZQ, None),
    207: (NAC, None),
    301: (NAC, None),
    401: (NAC, None),
    402: (NAC, None),
    403: (NAC, None),
    501: (NAC, None),
    502: (NAC, None),
    503: (NAC, None),
    504: (NAC, None),
    505: (NAC, None),
    506: (NAC, None),
    601: (NAC, None),
    **{c: (NAC, None) for c in range(801, 814)},
    814: (IZQ, "confluencia municipal con IU y Podemos"),
    815: (IZQ, None),
    816: (IZQ, None),
    817: (NAC, None),
    818: (IZQ, None),
    901: (NAC, None),
    902: (NAC, None),
    903: (IZQ, None),
    904: (NAC, None),
    905: (NAC, None),
    906: (NAC, None),
    907: (NAC, None),
    908: (CDE, "candidatura municipal en coalición con Ciudadanos"),
    909: (NAC, None),
    910: (NAC, None),
    911: (NAC, None),
    912: (IZQ, None),
    913: (NAC, None),
    914: (NAC, None),
    915: (NAC, None),
    916: (NAC, None),
    1001: (NAC, None),
    1002: (NAC, None),
    1003: (NAC, None),
    1004: (NAC, "coalición encabezada por Compromís"),
    1101: (NAC, None),
    1102: (NAC, None),
    1103: (NAC, None),
    1201: (NAC, None),
    1202: (IZQ, None),
    1203: (IZQ, "confluencia con Podemos y EU"),
    1204: (NAC, None),
    1205: (NAC, None),
    1206: (IZQ, "confluencia municipal con Podemos y EU"),
    1207: (NAC, None),
    1208: (NAC, None),
    1209: (NAC, None),
    1210: (IZQ, "confluencia municipal con Podemos y EU"),
    1211: (NAC, None),
    1212: (NAC, None),
    1213: (NAC, None),
    1301: (IZQ, "marca de Más País en Madrid"),
    1501: (NAC, None),
    1502: (NAC, None),
    1601: (NAC, None),
    1602: (NAC, None),
    1603: (IZQ, None),
    1604: (IZQ, None),
    1605: (IZQ, None),
    1650: (CDE, "coalición de PP y Ciudadanos en el País Vasco"),
    1701: (NAC, None),
    1801: (NAC, None),
    1802: (NAC, None),
    1901: (NAC, None),
    5001: (IZQ, None),
    5002: (NAC, "coalición de ERC, EH Bildu y BNG"),
    5003: (NAC, None),
    5004: (NAC, None),
    5005: (NAC, None),
    5006: (DRA, None),
    5007: (NAC, None),
    8888: (OTR, "otros partidos locales (sin identificar)"),
    8889: (NAC, "otros partidos autonómicos (sin identificar)"),
    8993: (OTR, "otros partidos de izquierda (sin identificar)"),
    8994: (OTR, "otros partidos de derecha (sin identificar)"),
    8995: (OTR, "otro partido (sin identificar)"),
}
# Códigos que cambian de significado en un estudio concreto
FAMILIA_CIS_ESTUDIO: dict[str, dict[int, tuple[str, str | None]]] = {
    "3411": {
        1501: (NAC, "Na+ (UPN, PP y Cs) en las variables de 2019; UPN en las de 2023"),
        1603: (CDE, "en este estudio el código 1603 es PP+Ciudadanos"),
        912: (NAC, "en este estudio el código 912 es Valents (partido de ámbito catalán)"),
    },
}
ESPECIALES = {
    0: "NP",
    8996: "en_blanco",
    9977: "nulo",
    9993: "mismo_partido",
    9995: "no_tenia_edad",
    9996: "sin_derecho_voto",
    9997: "no_voto_o_ninguno",
    9998: "NS",
    9999: "NC",
}
VARIABLES = [
    "RECUVOTOG",
    "RECUVOTOGR",
    "RECUERDO",
    "CERCANIA",
    "CERCANIAR",
    "CERCANIAR2",
    "INTENCIONG",
    "INTENCIONGR",
    "INTENCIONGALTER",
    "INTENCIONGALTERR",
    "VOTOSIMG",
    "VOTOSIMGR",
    "SIMPATIA",
    "SIMPATIAR",
    "INTENCIONA",
    "INTENCIONAR",
    "PARTIDOGANA",
    "PARTIDOGUSTAR",
    "P8R",
    "P9R",
    "PARTIDO_1",
    "PARTIDO_2",
    "PARTIDO_1R",
    "PARTIDO_2R",
]
ESTUDIOS = {
    "3567": (
        "data/raw/cis_barometros/3567/extraido/3567.sav",
        "Barómetro CIS 3567",
        "generales-2023",
    ),
    "3411": (
        "data/raw/cis_electorales/3411/extraido/3411.sav",
        "Preelectoral elecciones generales 2023 (CIS 3411)",
        None,
    ),
}


def catalogo(estudio: str) -> dict:
    sav, titulo, recuerdo = ESTUDIOS[estudio]
    _, meta = pyreadstat.read_sav(str(ROOT / sav), metadataonly=True)
    variables = [v for v in VARIABLES if v in meta.variable_to_label]
    etiquetas: dict[int, set[str]] = {}
    for v in variables:
        for c, lab in meta.value_labels[meta.variable_to_label[v]].items():
            etiquetas.setdefault(int(c), set()).add(str(lab).strip())
    codigos = {}
    for c in sorted(etiquetas):
        etq = " / ".join(sorted(etiquetas[c]))
        if c in ESPECIALES and c != 8995:
            codigos[c] = {"etiqueta": etq, "especial": ESPECIALES[c]}
            if c == 9997:
                codigos[c]["notas"] = (
                    "«no votó» en el recuerdo; «ninguno» o «no votaría» en el resto"
                )
            continue
        fam, nota = FAMILIA_CIS_ESTUDIO.get(estudio, {}).get(c) or FAMILIA_CIS[c]
        codigos[c] = {"etiqueta": etq, "familia": fam}
        if nota:
            codigos[c]["notas"] = nota
    out = {"titulo": titulo, "variables": variables, "codigos": codigos}
    if recuerdo:
        out["recuerdo_de"] = recuerdo
    return out


# Siglas de las hojas de Interior → siglas del BOE cuando no coinciden al normalizar
# (federaciones, marcas territoriales, coaliciones y grafías distintas). D-030 y D-032.
INTERIOR_A_BOE = {
    "PSdeG- PSOE": "PSOE",
    "PSE-EE (PSOE)": "PSOE",
    "PSIB-PSOE": "PSOE",
    "PSN-PSOE": "PSOE",
    "SUMAR - ECP": "SUMAR",
    "SUMAR - COMPROMÍS": "SUMAR",
    "MÉS PER MALLORCA- MÉS PER MENORCA- SUMAR": "SUMAR",
    "SUMAR ARAGÓN": "SUMAR",
    "JxCAT - JUNTS": "JUNTS",
    "ESCONS EN BLANC": "ESCAÑOS EN BLANCO",
    "PCTC": "PCTE",
    "PCTG": "PCTE",
    "PCTE/ELAK": "PCTE",
    "ASTURIAS EXISTE EV": "ESPAÑA VACIADA",
    "EVC": "EVR",
}


def _norm(s: str) -> str:
    return "".join(ch for ch in s.upper() if ch.isalnum() or ch == "+")


def candidaturas_2023() -> list[dict]:
    from sinpop.harmonize import boe_generales

    votos = pl.read_parquet(ROOT / "data/interim/elecciones_generales_2023_votos.parquet")
    _, boe, _ = boe_generales.leer()
    boe_nombre = dict(boe.select("siglas", "candidatura").unique().iter_rows())
    boe_prov = {
        k: set(v) for k, v in boe.group_by("siglas").agg(pl.col("provincia").unique()).iter_rows()
    }
    por_norma = {_norm(k): k for k in boe_nombre}
    ccaa = ccaa_de_provincia()
    amb = votos.group_by("candidatura").agg(pl.col("provincia").unique().sort())
    out = []
    for sig, provs in amb.sort("candidatura").iter_rows():
        sb = INTERIOR_A_BOE.get(sig) or por_norma.get(_norm(sig))
        if sb is None:
            raise ValueError(f"{sig}: sin candidatura en el BOE")
        if not set(provs) <= boe_prov[sb]:
            raise ValueError(f"{sig} → {sb}: provincias sin fila en el BOE")
        comunidades = sorted({ccaa[p] for p in provs})
        ambito = (
            "ES"
            if len(comunidades) > 1 and len(provs) > 10
            else ",".join(f"PROV:{p}" for p in provs)
        )
        nombre_boe = re.sub(r"\s*\([^()]*\)\.?$", "", boe_nombre[sb]).strip()
        if sig in CANDIDATURAS_2023:
            nombre, fam, cis, nota = CANDIDATURAS_2023[sig]
            if sig not in INTERIOR_A_BOE:
                nombre = nombre_boe
        elif len(comunidades) == 1:
            nombre, fam, cis, nota = nombre_boe, NAC, [8995], None
        else:
            nombre, fam, cis, nota = nombre_boe, OTR, [8995], None
        if sig in INTERIOR_A_BOE:
            dentro = f"en el BOE figura dentro de «{boe_nombre[sb]}»"
            nota = f"{nota}; {dentro}" if nota else dentro
        c = {
            "codigo_oficial": sig,
            "codigo_boe": sb,
            "nombre": nombre,
            "familia": fam,
            "ambito": ambito,
            "codigos_cis": {"3567": [str(x) for x in cis]},
        }
        if nota:
            c["notas"] = nota
        out.append(c)
    return out


def main() -> None:
    path = ROOT / "configs/partidos.yaml"
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    raw["elecciones"]["generales-2023"] = {
        "fecha": "2023-07-23",
        "fuente": "infoelectoral_resultados",
        "candidaturas": candidaturas_2023(),
    }
    raw["cis"] = {e: catalogo(e) for e in ESTUDIOS}
    cabecera = (
        "# Partidos por elección y familias estables (docs/02, sección 3.5, regla 1).\n"
        "# Generado por tools/generar_partidos.py (criterios en su cabecera y en D-030).\n"
        "# Las siglas de 2023 son las de las hojas del Ministerio del Interior; los códigos del\n"
        "# CIS, los de las etiquetas de valores de cada .sav (solo metadatos).\n"
    )
    path.write_text(
        cabecera + yaml.safe_dump(raw, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
