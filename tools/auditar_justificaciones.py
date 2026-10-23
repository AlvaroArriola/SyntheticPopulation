"""Auditoría de las justificaciones del LLM (docs/06 §5, prueba 3; G9.7; D-086).

Criterio: una justificación solo puede explicar las diferencias entre grupos con lo que dicen las
preguntas de referencia o con los atributos del perfil (edad, sexo, estudios, comunidad). Es
problemática si atribuye a un grupo un rasgo que no figura en él: religiosidad, ocupación, forma
de vida, tipo de hogar, carácter…

1. Se marcan como candidatas las que nombran un grupo del perfil y un rasgo ajeno a él, y las del
   modo evento que usan lenguaje cargado sobre un electorado (docs/06 §6.5). Los patrones están
   abajo; «derecha radical» es el nombre de una familia de `configs/partidos.yaml`, no una
   valoración.
2. Cada candidata se revisa a mano. El veredicto se guarda en
   `reports/fase_09/revision_justificaciones.yaml`, con la huella del texto, así que una
   justificación nueva siempre vuelve a revisarse.
3. Se escribe `reports/fase_09/llm_auditoria_justificaciones.json`, que lee G9.7.

Uso: `python tools/auditar_justificaciones.py`. Sale con error si queda alguna candidata sin
revisar.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys

import polars as pl
import yaml

from sinpop import REPO_ROOT

DIR = REPO_ROOT / "reports" / "fase_09"
REVISION = DIR / "revision_justificaciones.yaml"
DESTINO = DIR / "llm_auditoria_justificaciones.json"

GRUPO = re.compile(
    r"j[oó]venes|mayores|mujeres|hombres|estudios|universitari|edad|\b\d\d-\d\d\b|65\+",
    re.I,
)
RASGO = re.compile(
    r"cat[oó]lic|religios|practicante|creyente|agenda|\bocupad|\bocupaci[oó]n|hogares|conviv|"
    r"car[aá]cter|mentalidad|tradicional|conservador|progresista|familia numerosa|forma de vida|"
    r"exposici[oó]n digital|consumen|consumir|televisi[oó]n|medios tradicionales|fatiga|"
    r"familiaridad|disponibilidad de tiempo|h[aá]bito|conectad|"
    r"siguen? (m[aá]s )?(la )?(actualidad|informaci)",
    re.I,
)
CARGADO = re.compile(
    r"ultra|extremist|fanátic|radicales|populist|manipulad|borreg|ignoran|crispad[oa]s? votantes",
    re.I,
)


def huella(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:16]


def main() -> int:
    d = pl.read_csv(DIR / "llm_justificaciones.csv").select("id", "uso", "justificacion")
    ev = DIR / "evento_backtest_llm.csv"
    if ev.exists():
        e = (
            pl.read_csv(ev)
            .unique(["evento", "indicador"], maintain_order=True)
            .select(
                (pl.col("evento") + ":" + pl.col("indicador")).alias("id"),
                pl.lit("evento").alias("uso"),
                "justificacion",
            )
        )
        d = pl.concat([d, e])
    rev = yaml.safe_load(REVISION.read_text("utf-8")) if REVISION.exists() else {}
    rev = rev or {}
    candidatas, sin_revisar = [], []
    for r in d.iter_rows(named=True):
        j = r["justificacion"]
        if not ((GRUPO.search(j) and RASGO.search(j)) or CARGADO.search(j)):
            continue
        h = huella(j)
        v = rev.get(h)
        fila = {
            "id": r["id"],
            "uso": r["uso"],
            "huella": h,
            "rasgos": sorted({m.group(0).lower() for x in (RASGO, CARGADO) for m in x.finditer(j)}),
            "veredicto": v["veredicto"] if v else None,
            "motivo": v.get("motivo") if v else None,
            "justificacion": j,
        }
        candidatas.append(fila)
        if v is None:
            sin_revisar.append(fila)
    problematicas = [c for c in candidatas if c["veredicto"] == "problematica"]
    out = {
        "criterio": "docs/06 §5: solo atributos del perfil o lo que dicen las referencias",
        "revisadas": d.height,
        "candidatas": len(candidatas),
        "problematicas": len(problematicas),
        "problematicas_por_uso": {
            u: sum(c["uso"] == u for c in problematicas) for u in sorted(set(d["uso"]))
        },
        "sin_revisar": len(sin_revisar),
        "detalle": candidatas,
    }
    if sin_revisar:
        for c in sin_revisar:
            print(f"SIN REVISAR {c['huella']} {c['uso']} {c['id']}: {c['justificacion']}\n")
        return 1
    DESTINO.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "detalle"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
