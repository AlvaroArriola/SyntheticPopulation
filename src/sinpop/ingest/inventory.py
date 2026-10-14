"""Inventario de fuentes (F1): perfil de cada fichero de microdatos y recuento de registros.

`sinpop ingest --inventory` escribe `reports/fase_01_inventario.json` y `.md`.
Las estadísticas con peso usan la variable de peso oficial de cada encuesta; las de
los censos (sin peso) se marcan «sin ponderar» (regla 4 de CLAUDE.md).
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

import polars as pl

from sinpop import RAW_DIR, REPORTS_DIR
from sinpop.ingest.readers import layout_from_xlsx, read_fixed_width


@dataclass(frozen=True)
class Spec:
    fuente: str
    edicion: str
    fichero: str  # relativo a data/raw
    unidad: str
    peso: str | None = None
    edad: str | None = None
    geo: str | None = None
    diseno: str | None = None  # xlsx para ficheros de ancho fijo


@dataclass
class Perfil:
    fuente: str
    edicion: str
    fichero: str
    unidad: str
    registros: int
    columnas: int
    peso: str | None
    total_ponderado: float | None
    edad_min: float | None
    edad_max: float | None
    geo: str | None
    geo_valores: int | None
    notas: list[str] = field(default_factory=list)


C21 = "censo2021_micro_hogares/2021/extraido/"
CA = "censo_anual_micro_completo/{y}/extraido/"
SPECS: list[Spec] = [
    Spec(
        "censo2021_micro_hogares",
        "2021",
        C21 + "md_CensoPersonas_2021.parquet",
        "persona",
        edad="VAREDAD",
        geo="CPRO",
    ),
    *[
        Spec(
            "censo_anual_micro_completo",
            y,
            CA.format(y=y) + f"md_Censo_muestra_{y}.txt",
            "persona",
            edad="VAREDAD",
            geo="CPRO",
            diseno=CA.format(y=y) + "dr_CensoAnual_muestra_2022.xlsx",
        )
        for y in ("2023", "2024", "2025")
    ],
    Spec(
        "censo_anual_micro_demograficas",
        "2025",
        "censo_anual_micro_demograficas/2025/extraido/md_CensoAnual_2025.parquet",
        "persona",
        edad="VAREDAD",
        geo="CPRO",
    ),
    Spec(
        "ecv",
        "2025",
        "ecv/2025/extraido/ECV_Tr_2025/md_ECV_Tr_2025.parquet",
        "persona",
        peso="RB050",
        edad="RB082",
    ),
    Spec(
        "ecv",
        "2025",
        "ecv/2025/extraido/ECV_Tp_2025/md_ECV_Tp_2025.parquet",
        "persona 16+",
        peso="PB040",
    ),
    Spec(
        "ecv",
        "2025",
        "ecv/2025/extraido/ECV_Td_2025/md_ECV_Td_2025.parquet",
        "hogar",
        peso="DB090",
        geo="DB040",
    ),
    Spec("ecv", "2025", "ecv/2025/extraido/ECV_Th_2025/md_ECV_Th_2025.parquet", "hogar"),
    Spec(
        "epa",
        "2T2026",
        "epa/2T2026/extraido/md_EPA_2026T2.parquet",
        "persona",
        peso="FACTOREL",
        geo="PROV",
    ),
    Spec(
        "tic_h",
        "2025",
        "tic_h/2025/extraido/FicheroCuestionario/md_TICHcuestionario_2025.parquet",
        "persona 16+",
        peso="FACTOR_P",
        edad="EDAD",
        geo="CCAA",
    ),
    Spec(
        "tic_h",
        "2025",
        "tic_h/2025/extraido/FicheroMiembros/md_TICHmiembros_2025.parquet",
        "miembro del hogar",
        edad="EDAD",
        geo="CCAA",
    ),
    Spec(
        "encuesta_salud",
        "2023",
        "encuesta_salud/2023/extraido/ESdEadulto_2023/md_ESdEadulto_2023.parquet",
        "persona 15+",
        peso="FACTORADULTO",
        edad="EDADa",
        geo="CCAA",
    ),
]


def _num(c: str) -> pl.Expr:
    return (
        pl.col(c)
        .cast(pl.Utf8)
        .str.strip_chars()
        .str.replace(",", ".")
        .cast(pl.Float64, strict=False)
    )


def load(spec: Spec, raw_dir: Path = RAW_DIR, columns: list[str] | None = None) -> pl.DataFrame:
    path = raw_dir / spec.fichero
    if spec.diseno:
        return read_fixed_width(path, layout_from_xlsx(raw_dir / spec.diseno), columns)
    return pl.read_parquet(path, columns=columns)


def profile(spec: Spec, raw_dir: Path = RAW_DIR) -> Perfil:
    df = load(spec, raw_dir)
    notas = [] if spec.peso else ["sin variable de peso: estadísticas sin ponderar"]
    tot = float(df.select(_num(spec.peso).sum()).item()) if spec.peso else None
    emin = emax = None
    if spec.edad:
        emin, emax = df.select(
            _num(spec.edad).min().alias("a"), _num(spec.edad).max().alias("b")
        ).row(0)
    return Perfil(
        spec.fuente,
        spec.edicion,
        spec.fichero,
        spec.unidad,
        df.height,
        len(df.columns),
        spec.peso,
        tot,
        emin,
        emax,
        spec.geo,
        df[spec.geo].n_unique() if spec.geo else None,
        notas,
    )


# --------------------------------------------------------------------------- G1.4


def _ine_total(path: Path, prefijo: str) -> float:
    for s in json.loads(path.read_text(encoding="utf-8")):
        if s["Nombre"].startswith(prefijo):
            return float(s["Data"][0]["Valor"])
    raise KeyError(prefijo)


@dataclass
class Recuento:
    fichero: str
    registros: int
    referencia: str
    valor_referencia: float
    regla: str
    ok: bool
    declarado: bool  # True si la documentación oficial declara el número exacto


def record_checks(perfiles: list[Perfil], raw_dir: Path = RAW_DIR) -> list[Recuento]:
    """Contrasta el número de registros con la cifra oficial.

    - Muestras del Censo Anual: el INE declara una muestra del 10 % de la población;
      se exige registros == round(población oficial / 10) ± 1 (redondeo).
    - Censo 2021: el INE declara el 10 % de los hogares, sin cifra exacta; se informa el
      cociente frente a la población oficial y no se puede exigir igualdad (declarado=False).
    """
    out: list[Recuento] = []
    tablas = {
        "2023": raw_dir / "censo_anual_tablas/2023-01-01/tabla_67988_20230101.json",
        "2024": raw_dir / "censo_anual_tablas/2024-01-01/tabla_67988_20240101.json",
        "2025": raw_dir / "censo_anual_tablas/ultimo/tabla_67988_ultimo.json",
    }
    pref = "Total Nacional. Total. Total. Todas las edades."
    for p in perfiles:
        if p.fuente == "censo_anual_micro_completo" and p.edicion in tablas:
            pob = _ine_total(tablas[p.edicion], pref)
            out.append(
                Recuento(
                    p.fichero,
                    p.registros,
                    f"Censo Anual {p.edicion}, tabla 67988 (población total)",
                    pob,
                    "registros = población / 10 (±1 por redondeo)",
                    abs(p.registros - pob / 10) <= 1,
                    True,
                )
            )
        elif p.fuente == "censo_anual_micro_demograficas" and p.edicion in tablas:
            pob = _ine_total(tablas[p.edicion], pref)
            out.append(
                Recuento(
                    p.fichero,
                    p.registros,
                    f"Censo Anual {p.edicion}, tabla 67988 (población total)",
                    pob,
                    "fichero exhaustivo: registros = población oficial",
                    p.registros == pob,
                    True,
                )
            )
        elif p.fuente == "censo2021_micro_hogares":
            t21 = raw_dir / "censo_anual_tablas/2021-01-01/tabla_67988_20210101.json"
            pob = _ine_total(t21, pref)
            out.append(
                Recuento(
                    p.fichero,
                    p.registros,
                    "Censo 2021, tabla 67988 a 01/01/2021 (población total, "
                    "incluye establecimientos colectivos)",
                    pob,
                    "10 % de los hogares: sin cifra exacta declarada; se informa el cociente",
                    0.098 <= p.registros / pob <= 0.100,
                    False,
                )
            )
    return out


def _n(x: float) -> str:
    return f"{x:,.0f}".replace(",", ".")


def run(raw_dir: Path = RAW_DIR, reports_dir: Path = REPORTS_DIR) -> dict:
    perfiles = [profile(s, raw_dir) for s in SPECS if (raw_dir / s.fichero).exists()]
    recuentos = record_checks(perfiles, raw_dir)
    data = {"perfiles": [asdict(p) for p in perfiles], "recuentos": [asdict(r) for r in recuentos]}
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / "fase_01_inventario.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    lines = [
        "# Inventario de microdatos (F1)",
        "",
        "Generado por `sinpop ingest --inventory`. Totales ponderados con el peso oficial;",
        "los censos no tienen peso y se marcan sin ponderar.",
        "",
        "| Fuente | Edición | Fichero | Unidad | Registros | Peso | Total ponderado | Edad | Geo (valores) |",  # noqa: E501
        "| --- | --- | --- | --- | ---: | --- | ---: | --- | --- |",
    ]
    for p in perfiles:
        tot = _n(p.total_ponderado) if p.total_ponderado else "sin ponderar"
        edad = f"{p.edad_min:g}–{p.edad_max:g}" if p.edad_min is not None else "—"
        geo = f"{p.geo} ({p.geo_valores})" if p.geo else "—"
        lines.append(
            f"| `{p.fuente}` | {p.edicion} | `{Path(p.fichero).name}` | {p.unidad} | "
            f"{_n(p.registros)} | {p.peso or '—'} | {tot} | {edad} | {geo} |"
        )
    lines += [
        "",
        "## Recuento de registros (G1.4)",
        "",
        "| Fichero | Registros | Referencia oficial | Valor | Regla | Resultado |",
        "| --- | ---: | --- | ---: | --- | --- |",
    ]
    for r in recuentos:
        icon = "✅" if r.ok and r.declarado else ("⚠️ no declarado" if r.ok else "❌")
        lines.append(
            f"| `{Path(r.fichero).name}` | {_n(r.registros)} | {r.referencia} | "
            f"{_n(r.valor_referencia)} | {r.regla} | {icon} |"
        )
    (reports_dir / "fase_01_inventario.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return data
