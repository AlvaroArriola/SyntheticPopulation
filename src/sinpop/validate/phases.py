"""Puertas de fase: `sinpop validate --phase N` (docs/04_fases.md).

Cada puerta devuelve una lista de comprobaciones y escribe
`reports/fase_XX_puerta.md` con el resultado. Las comprobaciones de revisión humana
no se pueden superar automáticamente: se listan como pendientes.
"""

from __future__ import annotations

import datetime as dt
import os
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from sinpop import REPO_ROOT, REPORTS_DIR

# Evita la recursión cuando la propia batería de tests ejecuta una puerta.
_IN_GATE_ENV = "SINPOP_IN_GATE"


@dataclass(frozen=True)
class Check:
    id: str
    descripcion: str
    ok: bool | None  # None = no evaluable automáticamente (revisión humana o no aplica)
    valor: str
    umbral: str


# --------------------------------------------------------------------------- F0


def _g0_1_pytest() -> Check:
    if os.environ.get(_IN_GATE_ENV):
        return Check(
            "G0.1", "pytest se ejecuta sin errores", None, "omitido (llamada anidada)", "0 fallos"
        )
    env = {**os.environ, _IN_GATE_ENV: "1"}
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )
    last = (proc.stdout.strip().splitlines() or ["(sin salida)"])[-1]
    return Check("G0.1", "pytest se ejecuta sin errores", proc.returncode == 0, last, "0 fallos")


def _g0_2_configs() -> Check:
    from sinpop.config import validate_all

    res = validate_all()
    malos = {k: v for k, v in res.items() if v is not None}
    valor = f"{len(res) - len(malos)}/{len(res)} válidas"
    if malos:
        valor += "; errores: " + "; ".join(f"{k}: {v.splitlines()[0]}" for k, v in malos.items())
    return Check(
        "G0.2",
        "Las configuraciones pasan la validación de esquema",
        not malos,
        valor,
        f"{len(res)}/{len(res)}",
    )


def _g0_3_leakage() -> Check:
    path = REPO_ROOT / "tests" / "test_no_leakage.py"
    if not path.exists():
        return Check(
            "G0.3",
            "test_no_leakage.py existe y detecta accesos a los datos de evaluación",
            False,
            "no existe",
            "existe y sus autotests pasan",
        )
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-p", "no:cacheprovider", str(path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    detectores = path.read_text(encoding="utf-8").count("def test_detector_")
    last = (proc.stdout.strip().splitlines() or [""])[-1]
    ok = proc.returncode == 0 and detectores >= 1
    return Check(
        "G0.3",
        "test_no_leakage.py existe y detecta accesos a los datos de evaluación",
        ok,
        f"{last}; {detectores} autotests del detector",
        "existe y sus autotests pasan",
    )


def _g0_4_help() -> Check:
    from typer.testing import CliRunner

    from sinpop.cli import COMMANDS, app

    out = CliRunner().invoke(app, ["--help"], terminal_width=200).output
    faltan = [c for c in COMMANDS if c not in out]
    return Check(
        "G0.4",
        "`sinpop --help` muestra todos los comandos",
        not faltan,
        f"faltan: {faltan}" if faltan else f"{len(COMMANDS)}/{len(COMMANDS)} comandos",
        f"{len(COMMANDS)}/{len(COMMANDS)}",
    )


# --------------------------------------------------------------------------- F1


def _p0_sources() -> list[str]:
    from sinpop.config import load_config

    return [f.id for f in load_config("sources.yaml").fuentes if f.prioridad == "P0"]  # type: ignore[attr-defined]


def _g1_1_p0_downloaded() -> Check:
    from sinpop.ingest.manifest import load_manifest, verify

    m = load_manifest()
    estados = verify()
    con_datos = {e.fuente for e in m.ficheros if e.tipo == "datos" and estados[e.fichero] == "ok"}
    faltan = [s for s in _p0_sources() if s not in con_datos]
    total = len(_p0_sources())
    return Check(
        "G1.1",
        "Fuentes P0 descargadas y con hash verificado",
        not faltan,
        f"{total - len(faltan)}/{total}" + (f"; faltan: {', '.join(faltan)}" if faltan else ""),
        f"{total}/{total}",
    )


def _g1_2_docs() -> Check:
    from sinpop.ingest.manifest import load_manifest

    m = load_manifest()
    con_datos = {e.fuente for e in m.ficheros if e.tipo == "datos"}
    con_doc = {e.fuente for e in m.ficheros if e.tipo != "datos"}
    sin_doc = sorted(con_datos - con_doc)
    ok = bool(con_datos) and not sin_doc
    valor = (
        "sin ficheros" if not con_datos else (f"sin documentación: {sin_doc}" if sin_doc else "ok")
    )
    return Check(
        "G1.2",
        "Cada fichero tiene su diseño de registro o documentación",
        ok,
        valor,
        "todas las fuentes descargadas",
    )


def _g1_3_coverage() -> Check:
    from sinpop.config import load_config
    from sinpop.ingest.manifest import load_manifest

    v = load_config("variables.yaml")
    con_datos = {e.fuente for e in load_manifest().ficheros if e.tipo == "datos"}
    p0 = [k for k, x in v.variables.items() if x.prioridad == "P0"]  # type: ignore[attr-defined]
    # Una variable P0 está cubierta cuando la matriz de cobertura de F1 la asigna a una fuente
    # descargada (columna `fuentes` del diccionario, que se rellena al hacer el inventario).
    sin = [k for k in p0 if not set(v.variables[k].fuentes) & con_datos]  # type: ignore[attr-defined]
    return Check(
        "G1.3",
        "Matriz de cobertura sin variables P0 sin fuente",
        not sin,
        f"{len(p0) - len(sin)}/{len(p0)} P0 cubiertas",
        f"{len(p0)}/{len(p0)}",
    )


def _g1_4_records() -> Check:
    import json

    path = REPORTS_DIR / "fase_01_inventario.json"
    if not path.exists():
        return Check(
            "G1.4",
            "Registros leídos = registros declarados por la documentación",
            False,
            "falta el inventario (sinpop ingest --inventory)",
            "igualdad exacta",
        )
    rec = json.loads(path.read_text(encoding="utf-8"))["recuentos"]
    decl = [r for r in rec if r["declarado"]]
    malos = [Path(r["fichero"]).name for r in decl if not r["ok"]]
    nodecl = [Path(r["fichero"]).name for r in rec if not r["declarado"]]
    valor = f"{len(decl) - len(malos)}/{len(decl)} con cifra declarada coinciden"
    if malos:
        valor += f"; no coinciden: {', '.join(malos)}"
    if nodecl:
        valor += f"; sin cifra exacta declarada: {', '.join(nodecl)}"
    return Check(
        "G1.4",
        "Registros leídos = registros declarados por la documentación",
        bool(decl) and not malos,
        valor,
        "igualdad exacta",
    )


def _g1_5_critical() -> Check:
    import yaml

    path = REPORTS_DIR / "fase_01_verificaciones.yaml"
    if not path.exists():
        return Check(
            "G1.5", "Las 7 verificaciones críticas resueltas y registradas", False, "0/7", "7/7"
        )
    v = yaml.safe_load(path.read_text(encoding="utf-8"))["verificaciones"]
    ok = [x for x in v if x["estado"] == "resuelta"]
    pend = [str(x["id"]) for x in v if x["estado"] != "resuelta"]
    valor = f"{len(ok)}/7" + (f"; pendientes: {', '.join(pend)}" if pend else "")
    return Check(
        "G1.5",
        "Las 7 verificaciones críticas resueltas y registradas",
        len(ok) == 7 and len(v) == 7,
        valor,
        "7/7",
    )


def _g1_6_human() -> Check:
    return Check("G1.6", "Revisión humana del inventario", None, "pendiente", "aprobación")


PHASES: dict[int, list[Callable[[], Check]]] = {
    0: [_g0_1_pytest, _g0_2_configs, _g0_3_leakage, _g0_4_help],
    1: [
        _g1_1_p0_downloaded,
        _g1_2_docs,
        _g1_3_coverage,
        _g1_4_records,
        _g1_5_critical,
        _g1_6_human,
    ],
}


def run_checks(phase: int) -> list[Check]:
    if phase not in PHASES:
        raise NotImplementedError(f"La puerta de la fase {phase} aún no está implementada")
    return [f() for f in PHASES[phase]]


def _icon(ok: bool | None) -> str:
    return {True: "✅", False: "❌", None: "⏸️"}[ok]


def write_gate_report(phase: int, checks: list[Check]) -> str:
    from sinpop.repro import code_version

    superada = all(c.ok is not False for c in checks)
    lines = [
        f"# Puerta de la fase F{phase}",
        "",
        f"**Resultado:** {'superada' if superada else 'fallida'}  ",
        f"**Fecha:** {dt.date.today().isoformat()} · **Versión del código:** {code_version()}  ",
        f"**Comando:** `sinpop validate --phase {phase}`",
        "",
        "| ID | Comprobación | Resultado | Valor | Umbral |",
        "| --- | --- | --- | --- | --- |",
    ]
    lines += [
        f"| {c.id} | {c.descripcion} | {_icon(c.ok)} | {c.valor} | {c.umbral} |" for c in checks
    ]
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORTS_DIR / f"fase_{phase:02d}_puerta.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path)


def run_phase(phase: int) -> bool:
    checks = run_checks(phase)
    for c in checks:
        print(f"{_icon(c.ok)} {c.id} {c.descripcion}: {c.valor} (umbral: {c.umbral})")
    path = write_gate_report(phase, checks)
    ok = all(c.ok is not False for c in checks)
    print(f"\nPuerta F{phase}: {'SUPERADA' if ok else 'FALLIDA'} · informe: {path}")
    return ok
