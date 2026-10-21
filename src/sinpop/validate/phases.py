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
    from collections import Counter

    from sinpop.config import load_config

    minimo = load_config("thresholds.yaml").v_marg.poblaciones_fallo_min  # type: ignore[attr-defined]
    d, desc, um = (
        _f4(),
        "Marginales calibradas dentro del umbral ajustado al tamaño (V-MARG)",
        (
            "TVD ≤ 1,2 × TVD_ref(N) + 0,002 (España y comunidades); fallo si la misma marginal"
            f" queda fuera en ≥ {minimo} poblaciones de la serie (D-056)"
        ),
    )
    if d is None:
        return _sin_resumen("G4.1", desc, um)
    n = sum(x["v_marg"]["comprobaciones"] for x in d["poblaciones"])
    f = [(x["run_id"], y) for x in d["poblaciones"] for y in x["v_marg"]["fallos"]]
    veces = Counter((y["territorio"], y["objetivo"]) for _, y in f)
    sistematicos = [k for k, v in veces.items() if v >= minimo]
    ej = "; ".join(
        f"{r} {y['territorio']} {y['objetivo']} {y['tvd']:.4f}>{y['umbral']:.4f}" for r, y in f[:3]
    )
    return Check(
        "G4.1",
        desc,
        not sistematicos,
        f"{len(d['poblaciones'])} poblaciones, {n} comprobaciones; "
        f"fallos estrictos: {len(f)}{' (' + ej + ')' if f else ''}; repetidos en ≥ {minimo}"
        f" poblaciones: {sistematicos or 0}",
        um,
    )


def _g4_2_cruce() -> Check:
    """V-CRUCE con los criterios aprobados: umbral de D-038 A, excepciones de D-038 B y, por
    D-039, se separa el azar del sesgo: cada población puede tener como mucho un 5 % de fallos y
    ningún cruce puede fallar en todas las semillas de un mismo tamaño."""
    from collections import Counter

    from sinpop.config import load_config

    d, desc = _f4(), "Cruces reservados dentro de umbral (V-CRUCE)"
    lim = load_config("thresholds.yaml").v_cruce.proporcion_fallos_max  # type: ignore[attr-defined]
    um = (
        "TVD ≤ máx(1,2 × TVD_ref + 0,002, 0,03 / 0,05 / 0,08) (D-038 A); por población ≤ "
        f"{100 * lim:.0f} % de fallos y ningún cruce fallido en todas las semillas (D-039); "
        "|Δ V de Cramér| ≤ 0,03"
    )
    if d is None:
        return _sin_resumen("G4.2", desc, um)
    n = sum(x["v_cruce"]["comprobaciones"] for x in d["poblaciones"])
    exc = sum(bool(y.get("excepcion")) for x in d["poblaciones"] for y in x["v_cruce"]["fallos"])
    tasas, cuenta, semillas = [], Counter(), Counter()
    for x in d["poblaciones"]:
        f = [y for y in x["v_cruce"]["fallos"] if not y.get("excepcion")]
        tasas.append((len(f) / x["v_cruce"]["comprobaciones"], x["run_id"]))
        semillas[x["n"]] += 1
        for y in f:
            cuenta[(x["n"], y["nivel"], y["territorio"], y["objetivo"])] += 1
    sistematicos = [k for k, v in cuenta.items() if v == semillas[k[0]]]
    peor = max(tasas)
    total = sum(cuenta.values())
    cr = [c for x in d["poblaciones"] for c in x.get("v_cramer", []) if not c["ok"]]
    ok = peor[0] <= lim and not sistematicos and not cr
    return Check(
        "G4.2",
        desc,
        ok,
        f"{n} comprobaciones; fallos por azar: {total} (máximo por población "
        f"{100 * peor[0]:.1f} %, {peor[1]}); sistemáticos: "
        f"{len(sistematicos)}{' ' + str(sistematicos[:3]) if sistematicos else ''}; "
        f"excepciones aceptadas (D-038 B): {exc}; fallos Cramér: {len(cr)}",
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
    from collections import Counter

    from sinpop.config import load_config

    cfg = load_config("thresholds.yaml").v_semillas  # type: ignore[attr-defined]
    d, desc, um = (
        _f4(),
        "Variabilidad entre semillas dentro de lo esperado (V-SEMILLAS)",
        f"sd entre 5 semillas ≤ {cfg.factor_sd} × sd de muestra aleatoria simple; fallo si la "
        f"misma proporción lo supera en ≥ {cfg.tamanos_fallo_min} tamaños (D-047)",
    )
    if d is None:
        return _sin_resumen("G4.5", desc, um)
    fuera = sum(x["fuera"] for x in d["v_semillas"])
    tot = sum(x["proporciones"] for x in d["v_semillas"])
    rm = max(x["razon_media"] for x in d["v_semillas"])
    veces = Counter((p["objetivo"], p["clave"]) for x in d["v_semillas"] for p in x["peores"])
    sistematicos = [k for k, n in veces.items() if n >= cfg.tamanos_fallo_min]
    # «peores» guarda hasta 10 por tamaño: con más fuera, no se puede descartar la repetición
    incompleto = any(x["fuera"] > len(x["peores"]) for x in d["v_semillas"])
    return Check(
        "G4.5",
        desc,
        not sistematicos and not incompleto,
        f"{tot} proporciones; fuera (estricto): {fuera}; repetidos en ≥ {cfg.tamanos_fallo_min} "
        f"tamaños: {sistematicos or 0}; razón media sd/sd_MAS máx {rm:.2f}",
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


# --------------------------------------------------------------------------- F5


def _f5() -> dict | None:
    import json

    from sinpop.validate.fase5 import RESUMEN

    return json.loads(RESUMEN.read_text(encoding="utf-8")) if RESUMEN.exists() else None


def _sin_f5(id_: str, desc: str, um: str) -> Check:
    return Check(
        id_,
        desc,
        False,
        "falta reports/fase_05_validacion.json (python -m sinpop.validate.fase5)",
        um,
    )


def _g5_1() -> Check:
    d, desc = _f5(), "Todos los territorios superan V-MARG y V-REGLAS"
    um = "0 fallos de V-MARG y 0 violaciones de reglas duras"
    if d is None:
        return _sin_f5("G5.1", desc, um)
    ts = d["territorios"]
    fm = [(x["territorio"], y["objetivo"]) for x in ts for y in x["v_marg"]["fallos"]]
    fr = [x["territorio"] for x in ts if x["v_reglas_duras"]]
    n = sum(x["v_marg"]["comprobaciones"] for x in ts)
    return Check(
        "G5.1",
        desc,
        not fm and not fr,
        f"{len(ts)} territorios, {n} marginales; "
        f"fallos V-MARG: {len(fm)} {fm[:3] if fm else ''}; con violaciones: {fr or 0}",
        um,
    )


def _g5_2() -> Check:
    from sinpop.config import load_config

    d, desc = _f5(), "Cruces reservados por CCAA dentro de V-CRUCE (umbral territorial)"
    lim = load_config("thresholds.yaml").v_cruce.proporcion_fallos_max  # type: ignore[attr-defined]
    um = (
        f"máx(1,2 × TVD_ref + 0,002, 0,05 / 0,08) (D-038 A); ≤ {100 * lim:.0f} % de fallos por "
        "población (D-039); |Δ V de Cramér| ≤ 0,03"
    )
    if d is None:
        return _sin_f5("G5.2", desc, um)
    cc = [x for x in d["territorios"] if x["territorio"].startswith("CCAA:")]
    peor = max(cc, key=lambda x: x["v_cruce"]["proporcion_fallos"])
    cr = [(x["territorio"], c["par"]) for x in cc for c in x.get("v_cramer", []) if not c["ok"]]
    nf = sum(len(x["v_cruce"]["fallos"]) for x in cc)
    ok = peor["v_cruce"]["proporcion_fallos"] <= lim and not cr
    return Check(
        "G5.2",
        desc,
        ok,
        f"19 comunidades; fallos: {nf} (máximo "
        f"{100 * peor['v_cruce']['proporcion_fallos']:.1f} %, {peor['territorio']}); "
        f"Cramér fuera: {len(cr)} {cr[:3] if cr else ''}",
        um,
    )


def _g5_3() -> Check:
    d, desc = _f5(), "La agregación de las 19 comunidades reproduce la nacional (V-COHERENCIA)"
    um = "TVD ≤ 0,01 (calibradas) y ≤ 0,02 (reservadas)"
    if d is None or "coherencia" not in d:
        return _sin_f5("G5.3", desc, um)
    f = d["coherencia"]["comparaciones"]
    malos = [x["objetivo"] for x in f if not x["ok"]]
    mx = max(f, key=lambda x: x["tvd"])
    return Check(
        "G5.3",
        desc,
        not malos,
        f"{len(f)} comparaciones; fuera: {malos or 0}; máxima {mx['objetivo']} {mx['tvd']:.4f}",
        um,
    )


def _g5_4() -> Check:
    d, desc = _f5(), "Donantes no locales informados y tamaño efectivo mínimo (V-DONANTES)"
    um = "Kish de los hogares donantes ≥ 200; proporción local informada"
    if d is None:
        return _sin_f5("G5.4", desc, um)
    ts = d["territorios"]
    dn = {x["territorio"]: x["donantes"] for x in ts}
    bajos = [t for t, x in dn.items() if x["kish_hogares_donantes"] < x["kish_min"]]
    red = [t for t, x in dn.items() if x["confianza_reducida"]]
    kmin = min(dn, key=lambda t: dn[t]["kish_hogares_donantes"])
    lmin = min(dn, key=lambda t: dn[t]["proporcion_local"])
    txt = (
        f"Kish mínimo {dn[kmin]['kish_hogares_donantes']:.0f} ({kmin}); local mínimo "
        f"{100 * dn[lmin]['proporcion_local']:.1f} % ({lmin}); confianza reducida: "
        f"{red or 'ninguno'}; bajo el mínimo: {bajos or 0}"
    )
    return Check("G5.4", desc, not bajos, txt, um)


def _g5_5() -> Check:
    import polars as pl

    from sinpop.targets import run

    d, desc = _f5(), "Ceuta, Melilla y 2+ provincias de < 150.000 habitantes, con su confianza"
    um = "generadas sin errores, con confianza declarada"
    if d is None:
        return _sin_f5("G5.5", desc, um)
    ts = {x["territorio"]: x for x in d["territorios"]}

    def residentes(t: str) -> float:
        return float(run.leer(t).filter(pl.col("objetivo") == "edad5_sexo")["valor"].sum())

    pequenas = [
        t
        for t in ts
        if t.startswith("PROV:") and t not in ("PROV:51", "PROV:52") and residentes(t) < 150_000
    ]
    cm = [t for t in ("PROV:51", "PROV:52") if t in ts]
    ok = len(cm) == 2 and len(pequenas) >= 2
    txt = "; ".join(
        f"{t} ({residentes(t):,.0f} hab.): confianza {ts[t]['donantes']['confianza']}"
        f"{', reducida' if ts[t]['donantes']['confianza_reducida'] else ''}"
        for t in cm + pequenas
    )
    return Check("G5.5", desc, ok, txt, um)


def _g5_6_human() -> Check:
    texto = (REPO_ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    i = texto.find("Aprobación de F5")
    bloque = texto[i : texto.find("\n## D-", i)] if i >= 0 else ""
    ok = "**Estado:** aprobada" in bloque
    return Check(
        "G5.6",
        "Revisión humana del informe",
        True if ok else None,
        "aprobada" if ok else "pendiente (reports/fase_05.md)",
        "aprobación",
    )


def _f6() -> dict | None:
    import json

    from sinpop.validate.fase6 import RESUMEN

    return json.loads(RESUMEN.read_text(encoding="utf-8")) if RESUMEN.exists() else None


def _sin_f6(id_: str, desc: str, um: str) -> Check:
    return Check(
        id_,
        desc,
        False,
        "falta reports/fase_06_validacion.json (python -m sinpop.validate.fase6)",
        um,
    )


def _g6_1() -> Check:
    from sinpop.config import load_config

    cfg = load_config("thresholds.yaml").v_enriq_marg  # type: ignore[attr-defined]
    lim, propios = cfg.limitaciones, cfg.tvd_ajustada_max
    d, desc = _f6(), "Distribuciones por CCAA × edad_4 frente a la encuesta (V-ENRIQ-MARG)"
    um = (
        "≥ 90 % de las celdas de cada variable en el IC 95 % y TVD nacional ≤ 0,02; o, con la "
        "composición de la encuesta, TVD ≤ 0,02 y limitación declarada (D-048)"
    )
    if d is None:
        return _sin_f6("G6.1", desc, um)
    m, t = d["v_enriq_marg"], d["tvd_nacional"]
    aj = {x["variable"]: x["tvd"] for x in d.get("tvd_ajustada", [])}
    tvd = {x["variable"]: x["tvd"] for x in t["por_variable"]}
    estrictas = [
        x["variable"]
        for x in m["por_variable"]
        if x["proporcion"] < m["umbral"] or tvd[x["variable"]] > t["umbral"]
    ]
    malas = [
        v
        for v in estrictas
        if not (v in lim and aj.get(v, 1.0) <= max(t["umbral"], propios.get(v, 0.0)))
    ]
    return Check(
        "G6.1",
        desc,
        not malas,
        f"{len(m['por_variable'])} variables; en IC global {100 * m['global']:.1f} %; fuera del "
        f"umbral estricto: {estrictas or 0}; aceptadas como limitación (D-048): "
        f"{[v for v in estrictas if v not in malas] or 0}; fuera: {malas or 0}",
        um,
    )


def _g6_2() -> Check:
    d, desc = _f6(), "Asociación con las variables llave (V-ENRIQ-ASOC)"
    um = "|Δ V de Cramér| ≤ 0,05"
    if d is None:
        return _sin_f6("G6.2", desc, um)
    a = d["v_enriq_asoc"]
    fuera = [(x["variable"], x["llave"]) for x in a["fuera"]]
    return Check(
        "G6.2",
        desc,
        not fuera,
        f"{a['comprobaciones']} pares; fuera: {fuera or 0}; Δ máx. {a['dif_max']:.3f}",
        um,
    )


def _g6_3() -> Check:
    d, desc = _f6(), "Relaciones internas de cada bloque (V-ENRIQ-BLOQUE)"
    um = "|Δ| máx. ≤ 0,05 y medio ≤ 0,02"
    if d is None:
        return _sin_f6("G6.3", desc, um)
    b = d["v_enriq_bloque"]
    ok = b["dif_max"] <= b["umbral_max"] and b["dif_media"] <= b["umbral_media"]
    return Check(
        "G6.3",
        desc,
        ok,
        f"{len(b['pares'])} pares; Δ máx. {b['dif_max']:.3f}, medio {b['dif_media']:.3f}",
        um,
    )


def _g6_4() -> Check:
    d, desc = _f6(), "Emparejar sin una llave y recuperar su asociación (V-ENRIQ-HOLDOUT)"
    um = "mejor que la independencia (D-046 B1); se informa |Δ V de Cramér| frente a 0,05"
    if d is None:
        return _sin_f6("G6.4", desc, um)
    h = d["v_enriq_holdout"]
    f = h["filas"]
    # Mejor que la independencia: la asociación sintética se acerca a la de la encuesta más que
    # la independencia (V = 0); asociaciones despreciables (V < 0,02) no cuentan
    malos = [
        (x["llave"], x["variable"])
        for x in f
        if x["dif_independencia"] >= 0.02 and x["dif"] >= x["dif_independencia"]
    ]
    sobre = sum(x["dif"] > h["umbral"] for x in f)
    return Check(
        "G6.4",
        desc,
        not malos,
        f"llaves reservadas {', '.join(h['llaves'])}; {len(f)} pares; peor que la "
        f"independencia: {malos or 0}; |Δ| > {h['umbral']}: {sobre} (informativo)",
        um,
    )


def _g6_5() -> Check:
    d, desc = _f6(), "El enriquecimiento no altera las variables de los donantes (igualdad)"
    um = "columnas idénticas con y sin enriquecimiento"
    if d is None:
        return _sin_f6("G6.5", desc, um)
    g = d["g65"]
    txt = "; ".join(
        f"{f}: {'idénticas' if x['identicas'] else 'DISTINTAS'} ({x['columnas_base']} columnas)"
        for f, x in g["ficheros"].items()
    )
    return Check("G6.5", desc, g["ok"], txt, um)


def _g6_6() -> Check:
    d, desc = _f6(), "Renta media por territorio frente al Atlas de renta"
    um = "|error relativo| ≤ máx(2 %, 2 errores típicos) donde se calibra (D-046 C)"
    if d is None:
        return _sin_f6("G6.6", desc, um)
    g = d["g66"]
    mu = g["municipios"]
    return Check(
        "G6.6",
        desc,
        not g["fuera"],
        f"{len(g['provincias'])} provincias; fuera: {g['fuera'] or 0}; error máx. "
        f"{100 * g['error_max']:.2f} %; municipios identificados (no calibrados): {mu['n']}, "
        f"correlación de la renta relativa con el Atlas {mu['correlacion_relativa']:.2f}",
        um,
    )


def _f7() -> dict | None:
    import json

    from sinpop.validate.fase7 import RESUMEN

    return json.loads(RESUMEN.read_text(encoding="utf-8")) if RESUMEN.exists() else None


def _sin_f7(id_: str, desc: str, um: str) -> Check:
    return Check(
        id_,
        desc,
        False,
        "falta reports/fase_07_validacion.json (python -m sinpop.validate.fase7)",
        um,
    )


def _grupos_f7(d: dict) -> list[tuple[str, dict]]:
    return [(x["territorio"], g) for x in d["poblaciones"] for g in x["grupos"]]


def _g7_aceptado(territorio: str, grupo: str) -> bool:
    """Fallo aceptado como limitación declarada por la persona responsable (D-059)."""
    from sinpop.config import load_config

    cfg = load_config("thresholds.yaml").v_minorias  # type: ignore[attr-defined]
    if grupo in cfg.limitaciones or f"{territorio}|{grupo}" in cfg.excepciones:
        return True
    return (
        cfg.nacionalidades_territoriales
        and grupo.startswith("nacionalidad_")
        and territorio != "ES"
    )


def _g7_check(id_: str, desc: str, um: str, campo: str) -> Check:
    d = _f7()
    if d is None:
        return _sin_f7(id_, desc, um)
    malos = [(t, g["grupo"]) for t, g in _grupos_f7(d) if g.get(campo) is False]
    n = sum(1 for _, g in _grupos_f7(d) if g.get(campo) is not None)
    resto = [(t, g) for t, g in malos if not _g7_aceptado(t, g)]
    return Check(
        id_,
        desc,
        not resto,
        f"{n} grupos × población; fuera en estricto: {len(malos)}; aceptados como limitación"
        f" (D-059, D-061, D-062): {len(malos) - len(resto)}; fuera: {len(resto)}"
        f" {resto[:8] if resto else ''}",
        um,
    )


def _g7_1() -> Check:
    return _g7_check(
        "G7.1",
        "Grupos vigilados dentro de su rango de representación (V-MINORIAS)",
        "ratio en [0,9; 1,1] si el esperado es ≥ 200; si no, IC 95 % de MAS (o IC de la encuesta)",
        "ok_representacion",
    )


def _g7_2() -> Check:
    d, desc = _f7(), "Diversidad dentro de grupos (V-DIVERSIDAD)"
    um = "entropía ≥ 0,9 × la de los donantes ponderados en ≥ 95 % de los grupos (≥ 100 personas)"
    if d is None:
        return _sin_f7("G7.2", desc, um)
    filas = [(x["territorio"], a) for x in d["poblaciones"] for a in x.get("v_diversidad", [])]
    malos = [(t, a["atributo"], round(a["proporcion_ok"], 3)) for t, a in filas if not a["ok"]]
    return Check(
        "G7.2",
        desc,
        bool(filas) and not malos,
        f"{len(filas)} atributo × población; fuera: {malos or 0}",
        um,
    )


def _g7_3() -> Check:
    return _g7_check(
        "G7.3",
        "Concentración de donantes por grupo (V-CONCENTRACION)",
        "5 donantes más usados ≤ 20 %; donantes distintos ≥ mín(50, tamaño / 3)",
        "ok_concentracion",
    )


def _g7_4() -> Check:
    return _g7_check(
        "G7.4",
        "Perfil interno de cada grupo frente al oficial (V-MINORIAS-PERFIL)",
        "TVD ≤ 0,08 en sexo, edad, estudios y actividad, donde hay referencia",
        "ok_perfil",
    )


def _g7_5() -> Check:
    d, desc = _f7(), "Combinaciones de atributos P0 sin donante (V-RAREZA)"
    um = "0 con el método base"
    if d is None:
        return _sin_f7("G7.5", desc, um)
    r = [y for x in d["poblaciones"] for y in x.get("v_rareza", [])]
    nuevas = sum(y.get("sin_donante", 0) for y in r)
    return Check("G7.5", desc, bool(r) and nuevas == 0, f"combinaciones nuevas: {nuevas}", um)


def _g7_6() -> Check:
    desc = "Sección de limitaciones con los grupos no observables (docs/06 §2)"
    um = (
        "personas sin hogar, no empadronados, grupos étnicos, orientación sexual, identidad de "
        "género"
    )
    f = REPO_ROOT / "reports" / "fase_07.md"
    if not f.exists():
        return Check("G7.6", desc, False, "falta reports/fase_07.md", um)
    t = f.read_text(encoding="utf-8").lower()
    claves = [
        "sin hogar",
        "empadronad",
        "étnic",
        "orientación sexual",
        "identidad de género",
        "colectivos",
    ]
    faltan = [c for c in claves if c not in t]
    return Check("G7.6", desc, "## limitaciones" in t and not faltan, f"faltan: {faltan or 0}", um)


def _g7_7_human() -> Check:
    texto = (REPO_ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    i = texto.find("Aprobación de F7")
    bloque = texto[i : texto.find("\n## D-", i)] if i >= 0 else ""
    ok = "**Estado:** aprobada" in bloque
    return Check(
        "G7.7",
        "Revisión humana: aprobación expresa de la población",
        True if ok else None,
        "aprobada" if ok else "pendiente (reports/fase_07.md)",
        "aprobación",
    )


def _f8a() -> dict | None:
    import json

    from sinpop.validate.fase8a import RESUMEN

    return json.loads(RESUMEN.read_text(encoding="utf-8")) if RESUMEN.exists() else None


def _sin_f8a(id_: str, desc: str, um: str) -> Check:
    falta = "falta reports/fase_08a_validacion.json (python -m sinpop.validate.fase8a)"
    return Check(id_, desc, False, falta, um)


def _g8a_1() -> Check:
    from sinpop.config import load_config

    c = load_config("thresholds.yaml").v_latente  # type: ignore[attr-defined]
    d, desc = _f8a(), "Ajuste del modelo latente (V-LATENTE)"
    um = f"CFI ≥ {c.cfi_min}, RMSEA ≤ {c.rmsea_max}, omega ≥ {c.omega_min} por rasgo"
    if d is None or "g8a1" not in d:
        return _sin_f8a("G8A.1", desc, um)
    rs = d["g8a1"]["rasgos"]
    malos = [
        r["rasgo"]
        for r in rs
        if r["cfi"] < c.cfi_min
        or r["rmsea"] > c.rmsea_max
        or r["omega"] < c.excepciones_omega.get(r["rasgo"], c.omega_min) - 1e-3
    ]
    excepciones = [r["rasgo"] for r in rs if r["rasgo"] in c.excepciones_omega]
    return Check(
        "G8A.1",
        desc,
        bool(rs) and not malos,
        "; ".join(
            f"{r['rasgo']}: CFI {r['cfi']:.3f}, RMSEA {r['rmsea']:.3f}, omega {r['omega']:.2f}"
            for r in rs
        )
        + f"; fuera: {malos or 0}"
        + (f"; excepciones aprobadas (omega): {excepciones}" if excepciones else ""),
        um,
    )


def _g8a_2() -> Check:
    d, desc = _f8a(), "Validación cruzada por pregunta completa frente a B0 (V-OPINION-CV)"
    um = "TVD media del modelo < TVD media de B0 (distribución histórica)"
    if d is None or "g8a2" not in d:
        return _sin_f8a("G8A.2", desc, um)
    g = d["g8a2"]
    return Check(
        "G8A.2",
        desc,
        bool(g["ok"]),
        f"{g['preguntas']} preguntas; TVD modelo {g['tvd_media_modelo']:.4f} frente a B0 "
        f"{g['tvd_media_b0']:.4f}",
        um,
    )


def _g8a_3() -> Check:
    d, desc = _f8a(), "Varianza de los rasgos dentro de los grupos frente a la real (V-DIVERSIDAD)"
    um = "ratio de varianzas en [0,8; 1,2] en cada grupo con ≥ 200 encuestados"
    if d is None or "g8a3" not in d:
        return _sin_f8a("G8A.3", desc, um)
    g = d["g8a3"]
    return Check(
        "G8A.3",
        desc,
        g["grupos"] > 0 and g["dentro"] == g["grupos"],
        f"{g['dentro']} de {g['grupos']} grupos dentro; ratio de {g['ratio_min']:.2f} a "
        f"{g['ratio_max']:.2f}",
        um,
    )


def _g8a_4() -> Check:
    d, desc = _f8a(), "Variables de valores por CCAA × edad frente al CIS (V-ENRIQ-MARG)"
    um = "≥ 90 % de las celdas en el IC 95 % del CIS y TVD nacional ≤ 0,02"
    if d is None or "g8a4" not in d:
        return _sin_f8a("G8A.4", desc, um)
    g = d["g8a4"]
    malas = [x["variable"] for x in g["por_variable"] if x["proporcion"] < g["umbral_celdas"]]
    malas += [x["variable"] for x in g["tvd_nacional"] if x["tvd"] > g["umbral_tvd"]]
    return Check(
        "G8A.4",
        desc,
        not malas,
        f"en IC global {100 * g['global']:.1f} %; "
        + "; ".join(f"{x['variable']} {100 * x['proporcion']:.1f} %" for x in g["por_variable"])
        + f"; fuera: {sorted(set(malas)) or 0}",
        um,
    )


def _g8a_5() -> Check:
    d, desc = _f8a(), "Respuestas simuladas por CCAA frente al Barómetro Sanitario (se informa)"
    um = "se informa el error (sin umbral)"
    if d is None or "g8a5" not in d:
        return _sin_f8a("G8A.5", desc, um)
    g = d["g8a5"]
    return Check("G8A.5", desc, True, g.get("resumen", ""), um)


def _g8a_6() -> Check:
    c = _g0_3_leakage()
    return Check("G8A.6", "test_no_leakage.py pasa", c.ok, c.valor, c.umbral)


def _g8a_7_human() -> Check:
    texto = (REPO_ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    i = texto.find("### Aprobación de F8A")
    ok = i >= 0 and "**Estado:** aprobada" in texto[i : i + 400]
    return Check(
        "G8A.7",
        "Revisión humana del informe de F8A",
        True if ok else None,
        "aprobada" if ok else "pendiente (reports/fase_08a.md)",
        "aprobación",
    )


def _f8b() -> dict | None:
    import json

    from sinpop.validate.fase8b import RESUMEN

    return json.loads(RESUMEN.read_text(encoding="utf-8")) if RESUMEN.exists() else None


def _sin_f8b(id_: str, desc: str, um: str) -> Check:
    falta = "falta reports/fase_08b_validacion.json (python -m sinpop.validate.fase8b)"
    return Check(id_, desc, False, falta, um)


def _g8b_1() -> Check:
    d, desc = _f8b(), "Recuerdo de generales por provincia frente al oficial (V-POL-RECUERDO)"
    um = "TVD ≤ 1,2 × TVD_ref + 0,005 en cada provincia"
    if d is None:
        return _sin_f8b("G8B.1", desc, um)
    g = d["g8b1"]
    return Check(
        "G8B.1",
        desc,
        g["dentro"] == g["provincias"],
        f"{g['dentro']}/{g['provincias']} provincias; TVD máx. {g['tvd_max']:.3f}",
        um,
    )


def _g8b_2() -> Check:
    d, desc = _f8b(), "Mitad reservada de municipios frente al oficial (V-POL-RESERVADA)"
    um = "TVD ≤ 0,04 España y ≤ 0,06 CCAA (+ ruido de muestreo); participación ≤ 3 puntos"
    if d is None:
        return _sin_f8b("G8B.2", desc, um)
    from sinpop.config import load_config

    exc = load_config("thresholds.yaml").v_pol_reservada.excepciones_ccaa  # type: ignore[attr-defined]
    g = d["g8b2"]
    fuera = [f"{x['ccaa']} {x['tamano_municipio']}" for x in g["ccaa_fuera"]]
    sin_aprobar = [f for f in fuera if f not in exc]
    return Check(
        "G8B.2",
        desc,
        g["espana_dentro"] == g["espana_celdas"] and not sin_aprobar,
        f"España {g['espana_dentro']}/{g['espana_celdas']}; CCAA × tamaño "
        f"{g['ccaa_dentro']}/{g['ccaa_evaluables']} evaluables; fuera: {sin_aprobar or 0}"
        + (f"; excepciones aprobadas: {sorted(set(fuera) & set(exc))}" if exc else ""),
        um,
    )


def _g8b_3() -> Check:
    d, desc = _f8b(), "Perfil de cada electorado frente al postelectoral 3420 (V-POL-PERFIL)"
    um = "TVD ≤ 0,08 por variable en electorados con ≥ 300 casos"
    if d is None:
        return _sin_f8b("G8B.3", desc, um)
    g = d["g8b3"]
    return Check(
        "G8B.3",
        desc,
        g["dentro"] == g["comparaciones"],
        f"{g['dentro']}/{g['comparaciones']}; TVD máx. {g['tvd_max']:.3f}",
        um,
    )


def _g8b_4() -> Check:
    d, desc = _f8b(), "Ideología dentro de cada electorado frente al CIS (V-POL-COHERENCIA)"
    um = "media ± 0,3; razón de desviaciones en [0,8; 1,2]"
    if d is None:
        return _sin_f8b("G8B.4", desc, um)
    g = d["g8b4"]
    return Check(
        "G8B.4",
        desc,
        g["dentro"] == g["electorados"],
        f"{g['dentro']}/{g['electorados']} electorados; fuera: {g['fuera'] or 0}",
        um,
    )


def _g8b_5() -> Check:
    d, desc = _f8b(), "Transferencia generales → autonómicas frente al CIS (V-POL-TRANSFERENCIA)"
    um = "TVD ≤ 0,10 por fila con ≥ 200 casos (CIS ajustado por IPF a los márgenes oficiales)"
    if d is None or "g8b5" not in d:
        return _sin_f8b("G8B.5", desc, um)
    g = d["g8b5"]
    return Check(
        "G8B.5",
        desc,
        g["evaluables"] > 0 and g["dentro"] == g["evaluables"],
        f"{g['dentro']}/{g['evaluables']} filas; TVD media {g['tvd_media']:.3f}",
        um,
    )


def _g8b_6() -> Check:
    d, desc = _f8b(), "Ninguna variable política en la población base ni en la de opinión"
    um = "0 columnas; persons y opinion sin cambios (sha256)"
    if d is None:
        return _sin_f8b("G8B.6", desc, um)
    g = d["g8b6"]
    return Check(
        "G8B.6",
        desc,
        g["ok"],
        f"base: {g['base_con_politica'] or 0}; opinión: {g['opinion_con_politica'] or 0}; "
        f"sin cambios: {g['persons_sin_cambios'] and g['opinion_sin_cambios']}",
        um,
    )


def _g8b_7() -> Check:
    d, desc = _f8b(), "Pruebas de sesgo político (V-POL-SESGO)"
    um = "razón de entropías ≥ 0,9; contrafactual de ideología ± 0,3"
    if d is None:
        return _sin_f8b("G8B.7", desc, um)
    g = d["g8b7"]
    return Check(
        "G8B.7",
        desc,
        g["diversidad_dentro"] == g["diversidad_comparaciones"]
        and g["contrafactual_dentro"] == g["contrafactual_electorados"],
        f"diversidad {g['diversidad_dentro']}/{g['diversidad_comparaciones']} "
        f"(razón mín. {g['diversidad_razon_min']:.2f}); contrafactual "
        f"{g['contrafactual_dentro']}/{g['contrafactual_electorados']}",
        um,
    )


def _g8b_8() -> Check:
    d, desc = _f8b(), "Sin recuerdo de voto sin derecho a voto en esa elección"
    um = "0 personas"
    if d is None:
        return _sin_f8b("G8B.8", desc, um)
    g = d["g8b8"]
    a = g["autonomicas"]
    return Check(
        "G8B.8",
        desc,
        g["ok"],
        f"generales: {g['sin_derecho_con_recuerdo']} de {g['sin_derecho']} sin derecho; "
        f"autonómicas: {a['sin_derecho_con_recuerdo']} de {a['sin_derecho']}",
        um,
    )


def _g8b_latentes() -> Check:
    from sinpop.config import load_config

    c = load_config("thresholds.yaml").v_latente  # type: ignore[attr-defined]
    d, desc = _f8b(), "Ajuste de los rasgos políticos latentes (V-LATENTE, tarea 6)"
    um = f"CFI ≥ {c.cfi_min}, RMSEA ≤ {c.rmsea_max}, omega ≥ {c.omega_min} por rasgo"
    if d is None or "latentes" not in d:
        return _sin_f8b("G8B.L", desc, um)
    rs = d["latentes"]
    malos = [
        r["rasgo"]
        for r in rs
        if r["cfi"] < c.cfi_min or r["rmsea"] > c.rmsea_max or r["omega"] < c.omega_min - 1e-3
    ]
    return Check(
        "G8B.L",
        desc,
        bool(rs) and not malos,
        "; ".join(
            f"{r['rasgo']}: CFI {r['cfi']:.3f}, RMSEA {r['rmsea']:.3f}, omega {r['omega']:.2f}"
            for r in rs
        )
        + f"; fuera: {malos or 0}",
        um,
    )


def _g8b_9_human() -> Check:
    texto = (REPO_ROOT / "DECISIONS.md").read_text(encoding="utf-8")
    i = texto.find("### Aprobación de F8B")
    ok = i >= 0 and "**Estado:** aprobada" in texto[i : i + 400]
    return Check(
        "G8B.9",
        "Revisión humana del informe de F8B",
        True if ok else None,
        "aprobada" if ok else "pendiente (reports/fase_08b.md)",
        "aprobación",
    )


def _f8c() -> dict | None:
    import json

    from sinpop.validate.fase8c import RESUMEN

    return json.loads(RESUMEN.read_text(encoding="utf-8")) if RESUMEN.exists() else None


def _sin_f8c(id_: str, desc: str, um: str) -> Check:
    falta = "falta reports/fase_08c_validacion.json (python -m sinpop.validate.fase8c)"
    return Check(id_, desc, False, falta, um)


def _g8c_1() -> Check:
    d, desc = _f8c(), "Backtest temporal frente a la persistencia (V-TEMPORAL)"
    um = "error medio del modelo < error medio de repetir el último valor (t+1 a t+3)"
    if d is None:
        return _sin_f8c("G8C.1", desc, um)
    g = d["g8c1"]
    return Check(
        "G8C.1",
        desc,
        g["error_modelo_pp"] < g["error_persistencia_pp"],
        f"modelo {g['error_modelo_pp']:.2f} pp frente a persistencia "
        f"{g['error_persistencia_pp']:.2f} pp ({g['predicciones']} predicciones, "
        f"{g['origenes']} orígenes)",
        um,
    )


def _g8c_2() -> Check:
    d, desc = _f8c(), "Series de la población frente a las del CIS (V-TEMPORAL-SERIES)"
    if d is None:
        return _sin_f8c("G8C.2", desc, "≤ 2 pp")
    g = d["g8c2"]
    um = f"diferencia absoluta media ≤ {g['umbral_pp']} pp"
    return Check(
        "G8C.2",
        desc,
        g["dif_media_pp"] <= g["umbral_pp"],
        f"{g['dif_media_pp']:.2f} pp en {g['comparaciones']} mes × categoría",
        um,
    )


def _g8c_3() -> Check:
    d, desc = _f8c(), "Cada evento del banco tiene fecha, fuente y efecto con su incertidumbre"
    um = "todos los eventos"
    if d is None:
        return _sin_f8c("G8C.3", desc, um)
    g = d["g8c3"]
    return Check(
        "G8C.3",
        desc,
        g["ok"],
        f"{g['con_efecto']}/{g['eventos']} eventos con efecto e IC 95 %; sin fuente: "
        f"{g['sin_fuente'] or 0}",
        um,
    )


def _f9() -> dict | None:
    import json

    ruta = REPO_ROOT / "reports" / "fase_09_validacion.json"
    return json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else None


def _sin_f9(id_: str, desc: str, um: str) -> Check:
    falta = "falta reports/fase_09_validacion.json (python -m sinpop.evaluate.validacion)"
    return Check(id_, desc, False, falta, um)


def _g9_1() -> Check:
    d, desc = _f9(), "Salidas en el formato de §2.8 validadas por esquema (V-FORMATO)"
    if d is None:
        return _sin_f9("G9.1", desc, "100 %")
    g = d["g9_1"]
    return Check(
        "G9.1", desc, g["validas"] == g["salidas"], f"{g['validas']}/{g['salidas']}", "100 %"
    )


def _g9_2() -> Check:
    d, desc = _f9(), "Sistema y baselines en la ventana de validación (total, subgrupo, CCAA)"
    um = "B0, B1, B2 y sistema informados"
    if d is None:
        return _sin_f9("G9.2", desc, um)
    t = d["g9_2"]["todas"]
    valor = (
        f"TVD media: medición CIS {t['sistema_cis']:.3f}, B0 {t['b0']:.3f}, B1 {t['b1']:.3f} "
        f"({t['preguntas']} preguntas); B2 pendiente del modelo de lenguaje (D-069)"
    )
    return Check("G9.2", desc, None, valor, um)


def _g9_3() -> Check:
    from sinpop.config import load_config

    d, desc = _f9(), "Coste por pregunta informado y dentro del presupuesto"
    pres = load_config("llm.yaml").presupuesto.eur_max_por_prediccion  # type: ignore[attr-defined]
    um = f"≤ {pres} € por predicción"
    if d is None:
        return _sin_f9("G9.3", desc, um)
    g = d["g9_3"]
    return Check("G9.3", desc, g["eur"] <= pres, f"{g['llamadas']} llamadas, {g['eur']} €", um)


def _g9_4() -> Check:
    from sinpop.config import load_config

    tmax = load_config("thresholds.yaml").v_reformulacion.tvd_max  # type: ignore[attr-defined]
    d, desc = _f9(), "Reformulación neutra (V-REFORMULACION)"
    um = f"TVD ≤ {tmax} en cada pregunta"
    if d is None:
        return _sin_f9("G9.4", desc, um)
    g = d["g9_4"]
    return Check(
        "G9.4",
        desc,
        g["por_encima_umbral"] == 0,
        f"{g['preguntas']} preguntas; TVD media {g['tvd_media']:.4f}, máx. {g['tvd_max']:.4f}; "
        f"por encima: {g['por_encima_umbral']}",
        um,
    )


def _g9_5() -> Check:
    from sinpop.config import load_config

    c = load_config("thresholds.yaml").v_cobertura  # type: ignore[attr-defined]
    d, desc = _f9(), "Cobertura de los intervalos (V-COBERTURA)"
    um = f"IC80 en {c.ic80}, IC95 en {c.ic95}"
    if d is None:
        return _sin_f9("G9.5", desc, um)
    g = d["g9_5"]
    ok = c.ic80[0] <= g["cobertura80"] <= c.ic80[1] and c.ic95[0] <= g["cobertura95"] <= c.ic95[1]
    return Check(
        "G9.5",
        desc,
        ok,
        f"IC80 {g['cobertura80']:.2f}, IC95 {g['cobertura95']:.2f} ({g['casos']} opciones)",
        um,
    )


def _g9_6() -> Check:
    d, desc = _f9(), "Modo evento con eventos pasados (V-EVENTO)"
    um = "dirección correcta en ≥ 2 de cada 3 eventos; magnitud informada"
    if d is None:
        return _sin_f9("G9.6", desc, um)
    g = d["g9_6"]
    return Check(
        "G9.6",
        desc,
        g["eventos"] >= 3 and g["eventos_correctos"] / g["eventos"] >= 2 / 3,
        f"{g['eventos_correctos']}/{g['eventos']} eventos ({g['pares_correctos']}/{g['pares']} "
        f"evento × indicador); error de magnitud {g['error_magnitud_pp_medio']:.1f} pp",
        um,
    )


def _g9_7() -> Check:
    return Check(
        "G9.7",
        "Pruebas de estereotipos de la capa de IA",
        None,
        "no aplica mientras no intervenga un modelo de lenguaje (docs/06 §5, D-069)",
        "pruebas superadas",
    )


def _f10() -> dict | None:
    import json

    ruta = REPO_ROOT / "reports" / "fase_10_validacion.json"
    if not ruta.exists():
        return None
    return json.loads(ruta.read_text(encoding="utf-8"))["calibrado_en_validacion"]


def _sin_f10(id_: str, desc: str, um: str) -> Check:
    falta = "falta reports/fase_10_validacion.json (python -m sinpop.evaluate.confianza)"
    return Check(id_, desc, False, falta, um)


def _g10_1() -> Check:
    from sinpop.config import load_config

    rmin = load_config("thresholds.yaml").v_conf_corr.spearman_min  # type: ignore[attr-defined]
    d, desc = _f10(), "Correlación de rangos entre confianza y error real (V-CONF-CORR)"
    um = f"Spearman(confianza, −error) ≥ {rmin}"
    if d is None:
        return _sin_f10("G10.1", desc, um)
    r = d["spearman_confianza"]
    return Check("G10.1", desc, r >= rmin, f"{r:.3f} ({d['casos']} casos)", um)


def _g10_2() -> Check:
    from sinpop.config import load_config

    c = load_config("thresholds.yaml").v_conf_ece  # type: ignore[attr-defined]
    d, desc = _f10(), "Error de calibración (V-CONF-ECE)"
    um = f"ECE ≤ {c.ece_max} (acierto: TVD ≤ {c.tvd_acierto})"
    if d is None:
        return _sin_f10("G10.2", desc, um)
    return Check("G10.2", desc, d["ece"] <= c.ece_max, f"{d['ece']:.3f}", um)


def _g10_3() -> Check:
    d, desc = _f10(), "La confianza baja con el tamaño del territorio y del subgrupo"
    um = "confianza total > subgrupos; Spearman(confianza, datos) > 0 en subgrupos y en CCAA"
    if d is None:
        return _sin_f10("G10.3", desc, um)
    rs, rt = d["spearman_confianza_n_subgrupo"], d["spearman_confianza_n_ccaa"]
    ct, cs = d["confianza_media_total"], d["confianza_media_subgrupos"]
    ok = rs is not None and rt is not None and cs is not None and ct > cs and rs > 0 and rt > 0
    return Check(
        "G10.3",
        desc,
        ok,
        f"confianza media total {ct:.2f}, subgrupos {cs:.2f}; Spearman subgrupos {rs:.2f}, "
        f"CCAA {rt:.2f}",
        um,
    )


PHASES: dict[int | str, list[Callable[[], Check]]] = {
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
    5: [_g5_1, _g5_2, _g5_3, _g5_4, _g5_5, _g5_6_human],
    6: [_g6_1, _g6_2, _g6_3, _g6_4, _g6_5, _g6_6],
    7: [_g7_1, _g7_2, _g7_3, _g7_4, _g7_5, _g7_6, _g7_7_human],
    "8a": [_g8a_1, _g8a_2, _g8a_3, _g8a_4, _g8a_5, _g8a_6, _g8a_7_human],
    "8c": [_g8c_1, _g8c_2, _g8c_3],
    9: [_g9_1, _g9_2, _g9_3, _g9_4, _g9_5, _g9_6, _g9_7],
    10: [_g10_1, _g10_2, _g10_3],
    "8b": [
        _g8b_1,
        _g8b_2,
        _g8b_3,
        _g8b_4,
        _g8b_5,
        _g8b_6,
        _g8b_7,
        _g8b_8,
        _g8b_latentes,
        _g8b_9_human,
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


def run_checks(phase: int | str) -> list[Check]:
    if phase not in PHASES:
        raise NotImplementedError(f"La puerta de la fase {phase} aún no está implementada")
    return [f() for f in PHASES[phase]]


def _icon(ok: bool | None) -> str:
    return {True: "✅", False: "❌", None: "⏸️"}[ok]


def write_gate_report(phase: int | str, checks: list[Check]) -> str:
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
    nombre = f"{phase:02d}" if isinstance(phase, int) else f"0{phase}"
    path = REPORTS_DIR / f"fase_{nombre}_puerta.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(path)


def run_phase(phase: int | str) -> bool:
    checks = run_checks(phase)
    for c in checks:
        print(f"{_icon(c.ok)} {c.id} {c.descripcion}: {c.valor} (umbral: {c.umbral})")
    path = write_gate_report(phase, checks)
    ok = all(c.ok is not False for c in checks)
    print(f"\nPuerta F{phase}: {'SUPERADA' if ok else 'FALLIDA'} · informe: {path}")
    return ok
