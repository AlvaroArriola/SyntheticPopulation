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
    from sinpop.config import load_config

    autodoc = {
        f.id
        for f in load_config("sources.yaml").fuentes  # type: ignore[attr-defined]
        if f.documentacion_en_fichero
    }
    con_doc = {e.fuente for e in m.ficheros if e.tipo != "datos"} | autodoc
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
    import yaml

    vpath = REPORTS_DIR / "fase_01_verificaciones.yaml"
    vdata = yaml.safe_load(vpath.read_text(encoding="utf-8")) if vpath.exists() else {}
    aceptados = {a["fichero"]: a["decision"] for a in vdata.get("recuentos_aceptados") or []}
    decl = [r for r in rec if r["declarado"]]
    malos = [
        Path(r["fichero"]).name
        for r in decl
        if not r["ok"] and Path(r["fichero"]).name not in aceptados
    ]
    nodecl = [
        Path(r["fichero"]).name
        for r in rec
        if not r["declarado"] and Path(r["fichero"]).name not in aceptados
    ]
    acept = [f for f in aceptados if any(Path(r["fichero"]).name == f for r in rec)]
    exactos = sum(1 for r in decl if r["ok"])
    valor = f"{exactos}/{len(decl)} con cifra declarada coinciden exactamente"
    if malos:
        valor += f"; no coinciden: {', '.join(malos)}"
    if nodecl:
        valor += f"; sin cifra exacta declarada: {', '.join(nodecl)}"
    if acept:
        valor += "; diferencias aceptadas por el responsable: " + ", ".join(
            f"{f} ({aceptados[f]})" for f in acept
        )
    return Check(
        "G1.4",
        "Registros leídos = registros declarados por la documentación",
        bool(decl) and not malos and not nodecl,
        valor,
        "igualdad exacta o diferencia aceptada por el responsable",
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


# --------------------------------------------------------------------------- F2


def _g2_1_dominios() -> Check:
    from sinpop.harmonize import checks

    malos = checks.g21_dominios()
    nulos = checks.g21_nulos()
    n = sum(len(v) for v in checks.columnas_categoricas_comprobadas().values())
    valor = f"{n} columnas categóricas en {len(checks.salidas())} ficheros; fuera de dominio: "
    valor += "0" if not malos else "; ".join(f"{k}: {v}" for k, v in malos.items())
    valor += "; vacíos sin documentar: "
    valor += "0" if not nulos else "; ".join(f"{k}: {v}" for k, v in nulos.items())
    return Check(
        "G2.1",
        "Valores dentro del dominio declarado y vacíos documentados",
        not malos and not nulos,
        valor,
        "0 y 0",
    )


def _g2_2_especiales() -> Check:
    from sinpop.harmonize import checks

    malos = checks.g22_especiales()
    valor = "0 columnas numéricas con códigos especiales" if not malos else str(malos)
    return Check("G2.2", "Ningún NS/NC/NP como valor numérico", not malos, valor, "0")


def _g2_3_totales() -> Check:
    from sinpop.harmonize import checks

    t = checks.g23_totales()
    peor = max(x.diferencia_relativa for x in t)
    malos = [f"{x.fichero} ({x.concepto})" for x in t if not x.ok]
    valor = f"{len(t)} totales; diferencia máxima {100 * peor:.6f} %"
    if malos:
        valor += "; fallan: " + ", ".join(malos)
    return Check("G2.3", "Totales ponderados conservados", not malos, valor, "< 0,01 %")


def _g2_4_cifras() -> Check:
    import json

    from sinpop.config import load_config

    path = REPORTS_DIR / "fase_02_cifras_oficiales.json"
    if not path.exists():
        return Check(
            "G2.4",
            "≥3 cifras oficiales por fuente P0/P1",
            False,
            "falta reports/fase_02_cifras_oficiales.json (sinpop harmonize --check)",
            "≥3 por fuente",
        )
    cifras = json.loads(path.read_text(encoding="utf-8"))
    fuentes = [
        f.id
        for f in load_config("sources.yaml").fuentes  # type: ignore[attr-defined]
        if f.prioridad in ("P0", "P1")
    ]
    malas = []
    for f in fuentes:
        c = [x for x in cifras if x["fuente"] == f]
        if len(c) < 3 or not all(x["ok"] for x in c):
            malas.append(f"{f} ({sum(x['ok'] for x in c)}/{len(c)})")
    valor = f"{len(fuentes) - len(malas)}/{len(fuentes)} fuentes; {len(cifras)} cifras"
    if malas:
        valor += "; fallan: " + ", ".join(malas)
    return Check(
        "G2.4",
        "≥3 cifras oficiales por fuente P0/P1",
        not malas,
        valor,
        "≥3 por fuente dentro de tolerancia (D-027)",
    )


def _g2_5_tests() -> Check:
    from sinpop.harmonize.core import variables

    n = sum(
        1 for v in variables().variables.values() for f in v.fuentes.values() if f.recodificacion
    )
    if os.environ.get(_IN_GATE_ENV):
        return Check(
            "G2.5",
            "Tests por tabla de recodificación",
            None,
            f"{n} tablas; omitido (llamada anidada)",
            "1 test por tabla, 0 fallos",
        )
    env = {**os.environ, _IN_GATE_ENV: "1"}
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-p",
            "no:cacheprovider",
            "-q",
            "tests/unit/test_recodificaciones.py",
            "tests/unit/test_armonizacion.py",
            "tests/integration/test_interim.py",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )
    last = (proc.stdout.strip().splitlines() or ["(sin salida)"])[-1]
    return Check(
        "G2.5",
        "Tests por tabla de recodificación",
        proc.returncode == 0,
        f"{n} tablas con test parametrizado; {last}",
        "1 test por tabla, 0 fallos",
    )


def _g2_6_electorales() -> Check:
    from sinpop.harmonize import elecciones

    estado = elecciones.estado_g26()
    return Check(
        "G2.6",
        "Resultados electorales = totales oficiales",
        estado["ok"],
        estado["valor"],
        "sin diferencias (nacional y provincial)",
    )


def _g2_7_cis() -> Check:
    from sinpop.harmonize import elecciones

    sin = elecciones.codigos_cis_sin_asignar()
    valor = "0 códigos sin asignar" if not sin else f"sin asignar: {sin}"
    return Check("G2.7", "Códigos de partido del CIS en partidos.yaml", not sin, valor, "0")


def _g2_8_human() -> Check:
    """Revisión humana: se da por superada cuando DECISIONS.md registra la aprobación de F2."""
    texto = (REPO_ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    i = texto.find("Aprobación de F2")
    bloque = texto[i : texto.find("\n## D-", i)] if i >= 0 else ""
    ok = "**Estado:** aprobada" in bloque
    return Check(
        "G2.8",
        "Revisión humana: 20 registros por fuente frente al original",
        True if ok else None,
        "aprobada por el responsable (DECISIONS.md, D-035)" if ok else "pendiente",
        "aprobación",
    )


# --------------------------------------------------------------------------- F3


def _fs():
    from sinpop.targets import checks

    return checks.ficheros()


def _lista(malos: list[str], n: int = 3) -> str:
    return "0" if not malos else f"{len(malos)}: " + "; ".join(malos[:n])


def _g3_1_totales() -> Check:
    from sinpop.targets import checks

    fs = _fs()
    malos = checks.g31_totales(fs)
    return Check(
        "G3.1",
        "Las marginales suman el total oficial",
        not malos,
        f"{len(fs)} territorios; fuera de umbral: {_lista(malos)}",
        "< 0,1 %",
    )


def _g3_2_coherencia() -> Check:
    from sinpop.targets import checks

    malos = checks.g32_coherencia(_fs())
    return Check(
        "G3.2",
        "Marginales coherentes entre cruces",
        not malos,
        f"incoherencias: {_lista(malos)}",
        "diferencia relativa < 1e-6 (redondeo)",
    )


def _g3_3_ccaa() -> Check:
    from sinpop.targets import checks

    malos = checks.g33_ccaa_suman_espana(_fs())
    return Check(
        "G3.3",
        "Las 19 comunidades suman España",
        not malos,
        f"celdas distintas: {_lista(malos)}",
        "|diferencia| < 0,001 personas",
    )


def _g3_4_separacion() -> Check:
    from sinpop.config import load_config

    try:
        cfg = load_config("targets.yaml")
        ok = True
        valor = f"{len(cfg.calibrar)} calibrados, {len(cfg.reservar)} reservados; ninguno repetido"  # type: ignore[attr-defined]
    except Exception as e:  # noqa: BLE001
        ok, valor = False, str(e).splitlines()[0]
    if os.environ.get(_IN_GATE_ENV):
        return Check("G3.4", "Ningún objetivo reservado se calibra", ok, valor, "0")
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-p",
            "no:cacheprovider",
            "-q",
            "tests/unit/test_config.py::test_targets_reject_reserved_in_calibration",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env={**os.environ, _IN_GATE_ENV: "1"},
    )
    ok = ok and proc.returncode == 0
    return Check(
        "G3.4",
        "Ningún objetivo reservado se calibra (test automático)",
        ok,
        valor + ("; test superado" if proc.returncode == 0 else "; test FALLIDO"),
        "0",
    )


def _g3_5_metadatos() -> Check:
    from sinpop.targets import checks

    malos = checks.g35_metadatos(_fs())
    return Check(
        "G3.5",
        "Cada objetivo registra fuente, edición y fecha",
        not malos,
        f"filas sin metadatos: {_lista(malos)}",
        "0",
    )


def _g3_6_electorales() -> Check:
    from sinpop.targets import checks

    malos, difs = checks.g36_electorales(_fs())
    peor = max(difs.items(), key=lambda x: abs(x[1])) if difs else ("—", 0.0)
    es = difs.get("ES", float("nan"))
    valor = (
        f"censo de residentes 2023 frente a españoles 18+ 2026: España {100 * es:+.2f} %, "
        f"máximo {peor[0]} {100 * peor[1]:+.2f} %; incidencias: {_lista(malos)}"
    )
    return Check(
        "G3.6",
        "Objetivos electorales al 100 % y coherentes con el derecho a voto",
        not malos,
        valor,
        "100 % y diferencia < 5 %",
    )


# --------------------------------------------------------------------------- F4


def _f4() -> dict | None:
    import json

    from sinpop.validate.fase4 import RESUMEN

    return json.loads(RESUMEN.read_text(encoding="utf-8")) if RESUMEN.exists() else None


def _sin_resumen(id_: str, desc: str, umbral: str) -> Check:
    return Check(
        id_,
        desc,
        False,
        "falta reports/fase_04_validacion.json (python -m sinpop.validate.fase4)",
        umbral,
    )


def _g4_1_marg() -> Check:
    d, desc, um = (
        _f4(),
        "Marginales calibradas dentro del umbral ajustado al tamaño (V-MARG)",
        ("TVD ≤ 1,2 × TVD_ref(N) + 0,002 (España y comunidades)"),
    )
    if d is None:
        return _sin_resumen("G4.1", desc, um)
    n = sum(x["v_marg"]["comprobaciones"] for x in d["poblaciones"])
    f = [(x["run_id"], y) for x in d["poblaciones"] for y in x["v_marg"]["fallos"]]
    ej = "; ".join(
        f"{r} {y['territorio']} {y['objetivo']} {y['tvd']:.4f}>{y['umbral']:.4f}" for r, y in f[:3]
    )
    return Check(
        "G4.1",
        desc,
        not f,
        f"{len(d['poblaciones'])} poblaciones, {n} comprobaciones; "
        f"fallos: {len(f)}{' (' + ej + ')' if f else ''}",
        um,
    )


def _g4_2_cruce() -> Check:
    d, desc = _f4(), "Cruces reservados dentro de umbral (V-CRUCE)"
    um = "TVD ≤ máx(TVD_ref, 0,03 / 0,05 / 0,08); |Δ V de Cramér| ≤ 0,03 (España)"
    if d is None:
        return _sin_resumen("G4.2", desc, um)
    n = sum(x["v_cruce"]["comprobaciones"] for x in d["poblaciones"])
    f = [(x["run_id"], y) for x in d["poblaciones"] for y in x["v_cruce"]["fallos"]]
    cr = [c for x in d["poblaciones"] for c in x.get("v_cramer", []) if not c["ok"]]
    ej = "; ".join(
        f"{r} {y['territorio']} {y['objetivo']} {y['tvd']:.4f}>{y['umbral']:.4f}" for r, y in f[:3]
    )
    ejc = "; ".join(f"{c['objetivo']} {c['par']} Δ={c['dif']:.3f}" for c in cr[:3])
    return Check(
        "G4.2",
        desc,
        not f and not cr,
        f"{n} comprobaciones; fallos TVD: {len(f)}"
        f"{' (' + ej + ')' if f else ''}; fallos Cramér: {len(cr)}{' (' + ejc + ')' if cr else ''}",
        um,
    )


def _g4_3_reglas() -> Check:
    d, desc, um = _f4(), "0 violaciones de las reglas de coherencia duras (V-REGLAS)", "0"
    if d is None:
        return _sin_resumen("G4.3", desc, um)
    v = sum(r["violaciones"] for x in d["poblaciones"] for r in x["v_reglas_duras"])
    bl = [r["regla"] for x in d["poblaciones"] for r in x["v_reglas_blandas"] if not r["ok"]]
    ble = [
        r["regla"] for x in d["poblaciones"] for r in x["v_reglas_blandas"] if not r["ok_estricto"]
    ]
    return Check(
        "G4.3",
        desc,
        v == 0,
        f"violaciones duras: {v}; reglas blandas (informativo): "
        f"{len(bl)} fuera con margen de muestreo, {len(ble)} fuera sin él",
        um,
    )


def _g4_4_pesos() -> Check:
    d, desc = _f4(), "Diagnóstico de pesos dentro de umbral (V-PESOS)"
    um = "desviación ≤ 0,1 %; ≥ 99 % de factores en [0,2; 5]; Kish/n ≥ 0,30; 0 pesos ≤ 0"
    if d is None:
        return _sin_resumen("G4.4", desc, um)
    vp = d["calibracion"]["v_pesos"]
    malos = [b["bloque"] for b in vp if not b["ok"]]
    kmin = min(b["kish_ratio"] for b in vp)
    rmin = min(b["proporcion_en_rango"] for b in vp)
    return Check(
        "G4.4",
        desc,
        not malos,
        f"{len(vp)} bloques ({d['calibracion']['metodo']}); "
        f"en rango mín {100 * rmin:.2f} %; Kish/n mín {kmin:.3f}; bloques fuera: {malos or 0}",
        um,
    )


def _g4_5_semillas() -> Check:
    d, desc, um = (
        _f4(),
        "Variabilidad entre semillas dentro de lo esperado (V-SEMILLAS)",
        ("sd entre 5 semillas ≤ 1,5 × sd de muestra aleatoria simple"),
    )
    if d is None:
        return _sin_resumen("G4.5", desc, um)
    fuera = sum(x["fuera"] for x in d["v_semillas"])
    tot = sum(x["proporciones"] for x in d["v_semillas"])
    rm = max(x["razon_media"] for x in d["v_semillas"])
    return Check(
        "G4.5",
        desc,
        fuera == 0,
        f"{tot} proporciones; fuera: {fuera}; razón media sd/sd_MAS máx {rm:.2f}",
        um,
    )


def _g4_6_repro() -> Check:
    d, desc, um = _f4(), "Reproducibilidad: misma semilla, mismo hash (V-REPRO)", "hashes iguales"
    if d is None:
        return _sin_resumen("G4.6", desc, um)
    r = d["v_repro"]
    return Check(
        "G4.6",
        desc,
        r["hashes_iguales"],
        f"{r['run_id']}: "
        f"{'iguales' if r['hashes_iguales'] else 'distintos'} (persons, households, lineage)",
        um,
    )


def _g4_7_sobremuestreo() -> Check:
    d, desc = _f4(), "Modo de sobremuestreo: estimaciones ponderadas dentro del error de muestreo"
    um = "TVD ponderada ≤ 1,2 × TVD_ref(n efectivo) + 0,002; mínimo alcanzado"
    if d is None:
        return _sin_resumen("G4.7", desc, um)
    g = d["g47"]
    malos = [m["objetivo"] for m in g["marginales"] if not m["ok"]]
    return Check(
        "G4.7",
        desc,
        g["ok"],
        f"{g['spec']}: {g['miembros']} miembros "
        f"(mínimo {g['minimo']}); marginales fuera: {malos or 0}",
        um,
    )


def _g4_8_human() -> Check:
    texto = (REPO_ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    i = texto.find("Aprobación de F4")
    bloque = texto[i : texto.find("\n## D-", i)] if i >= 0 else ""
    ok = "**Estado:** aprobada" in bloque
    return Check(
        "G4.8",
        "Revisión humana del informe",
        True if ok else None,
        "aprobada" if ok else "pendiente (reports/fase_04.md)",
        "aprobación",
    )


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
    2: [
        _g2_1_dominios,
        _g2_2_especiales,
        _g2_3_totales,
        _g2_4_cifras,
        _g2_5_tests,
        _g2_6_electorales,
        _g2_7_cis,
        _g2_8_human,
    ],
    4: [
        _g4_1_marg,
        _g4_2_cruce,
        _g4_3_reglas,
        _g4_4_pesos,
        _g4_5_semillas,
        _g4_6_repro,
        _g4_7_sobremuestreo,
        _g4_8_human,
    ],
    3: [
        _g3_1_totales,
        _g3_2_coherencia,
        _g3_3_ccaa,
        _g3_4_separacion,
        _g3_5_metadatos,
        _g3_6_electorales,
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
