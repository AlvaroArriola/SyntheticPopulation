"""Informe de F7 (`reports/fase_07.md`) y ficha de datos de la población nacional
(`reports/<run_id>/ficha.md`, docs/07 §3), generados desde la auditoría y los metadatos.

Comando: `python -m sinpop.validate.informe_f7` (tras `python -m sinpop.validate.fase7`).
"""

from __future__ import annotations

import datetime as dt
import json
from collections import Counter

import polars as pl

from sinpop import REPORTS_DIR
from sinpop.config import load_config
from sinpop.repro import code_version
from sinpop.validate import fase7 as F7
from sinpop.validate import poblacion as V

INFORME = REPORTS_DIR / "fase_07.md"

LIMITACIONES = """\
### Grupos no observables (docs/06 §2)

Ninguna fuente oficial de las usadas los identifica o los cubre. No se inventan: la población no
permite analizarlos.

- **Personas sin hogar.** La población parte de hogares y establecimientos colectivos
  empadronados. La Encuesta a las Personas sin Hogar del INE no está integrada.
- **Población no empadronada,** incluida parte de la población migrante en situación
  irregular. Los totales son los de la Estadística Continua de Población (ECP), que parte del
  Padrón.
- **Grupos étnicos** (por ejemplo, la población gitana), **orientación sexual** e **identidad de
  género**: no figuran en el Censo ni en las encuestas de referencia.
- **Residentes en establecimientos colectivos** (residencias, centros penitenciarios,
  religiosos…). Están en la población con sus atributos del Censo, pero las encuestas (ECV, EPA,
  TIC-H) no los cubren. Sus variables de encuesta están extrapoladas (`extrapolada`) desde los
  hogares con las mismas llaves, y las del hogar no proceden (NP).
- **Población de las islas no capitalinas:** no se puede medir aparte con las fuentes usadas
  (grupo `no_medible` de la lista de vigilancia).

### Diferencias de composición o de definición con las encuestas (D-048, D-051)

La población está calibrada al Censo Anual, a la ECP y a la EPA. Las variables de encuesta
heredan la medida de cada encuesta y su muestra ponderada no siempre tiene la misma
composición que las cifras oficiales:

- **Personas que nunca usan internet:** 9,2 % frente al 8,3 % de la TIC-H 2025 (ratio 1,11).
  Reponderada a la composición por edad × estudios de la TIC-H, el ratio baja a 1,04. El Censo
  Anual 2024 tiene más personas con estudios obligatorios o menos que la muestra ponderada de la
  TIC-H (25-34 años: 27,5 % frente a 15,5 %).
- **Carencia material y social severa:** representación dentro del intervalo de la ECV (ratio
  0,95). El perfil de actividad difiere (TVD 0,085 con ocupado, parado e inactivo) porque la ECV
  mide el paro según lo que declara cada persona y la población usa el paro de la OIT de la EPA.
- **Tenencia de la vivienda, vehículo, tipo de jornada, sector público y teletrabajo:** sus
  marginales regionales difieren algo de las encuestas por patrones regionales o por la fecha de
  la encuesta (D-048).

### Desfase de los donantes de 2021

Los hogares donantes son los del Censo 2021. Lo que se calibra a 2026 refleja 2026:

- edad, sexo, nacionalidad (también por edad), país de nacimiento, estudios, actividad (EPA,
  también por nacionalidad), estado civil, tamaño y tipo de hogar, y territorio.

El resto conserva la estructura de 2021 dentro de lo calibrado, por ejemplo la composición
detallada de los hogares o la ocupación.

### Grupos pequeños en territorios pequeños

En las poblaciones de provincias y comunidades pequeñas (50.000-100.000 personas), las
nacionalidades minoritarias de unas decenas de personas salen de pocos hogares donantes, a
veces copiados dos o tres veces. Su número está calibrado, pero su variedad interna es menor que
la real (semáforo rojo o ámbar en la tabla por territorio). Estos grupos no deben analizarse por
separado en esos territorios. Para estudiarlos conviene generar el territorio con más personas o
usar la población nacional.

### Capas pendientes

Las capas de opinión (F8A) y política (F8B) aún no existen. Los grupos de la lista de vigilancia
que dependen de ellas figuran como `pendiente`.
"""

LIMITES_USO = """\
- La población describe **distribuciones**, no personas. No se debe usar para tomar decisiones
  sobre individuos reales.
- No sustituye a una encuesta cuando la decisión es crítica o afecta a derechos de las personas.
- No debe usarse para dirigir acciones a grupos vulnerables sin una validación específica para
  ese grupo.
- Los grupos marcados en ámbar o rojo, y los no observables, no deben analizarse por separado
  sin advertir de su baja fiabilidad.
- Las estimaciones por provincia o municipio tienen una confianza menor que las nacionales y
  autonómicas, y así debe comunicarse.
"""


def _resumen() -> dict:
    return json.loads(F7.RESUMEN.read_text("utf-8"))


def _f(x: float | None, d: int = 3) -> str:
    return "—" if x is None else f"{x:.{d}f}".replace(".", ",")


def _tabla(filas: list[list[str]], cabecera: list[str]) -> str:
    out = ["| " + " | ".join(cabecera) + " |", "| " + " | ".join("---" for _ in cabecera) + " |"]
    out += ["| " + " | ".join(f) + " |" for f in filas]
    return "\n".join(out)


def tabla_grupos(pob: dict) -> str:
    filas = []
    for g in pob["grupos"]:
        perfil = g.get("perfil_tvd") or {}
        peor = max(perfil.values()) if perfil else None
        filas.append(
            [
                g["nombre"],
                g["semaforo"],
                _f(g.get("ratio")),
                _f(g.get("proporcion_sintetica")),
                _f(g.get("proporcion_oficial")),
                _f(peor),
                str(g.get("donantes_distintos", "—")),
                _f(g.get("top5"), 2),
                g.get("fuente") or g.get("motivo") or "",
            ]
        )
    return _tabla(
        filas,
        [
            "Grupo",
            "Semáforo",
            "Ratio",
            "Sintética",
            "Oficial",
            "Peor TVD de perfil",
            "Donantes",
            "Top 5",
            "Referencia",
        ],
    )


def ficha(run_id: str = F7.NACIONAL) -> str:
    """Ficha de datos de una población (docs/07 §3)."""
    p, lin, meta = V.cargar(run_id)
    var_cfg = load_config("variables.yaml").variables  # type: ignore[attr-defined]
    res = _resumen()
    pob = next(x for x in res["poblaciones"] if x["run_id"] == run_id)
    calidades = [c for c in p.columns if c.endswith("__calidad")]
    filas_v = []
    for c in calidades:
        v = c.removesuffix("__calidad")
        cnt = p[c].cast(pl.Utf8).value_counts(normalize=True).sort("proportion", descending=True)
        pct = ", ".join(f"{k} {100 * x:.1f} %" for k, x in cnt.iter_rows())
        cfg = var_cfg.get(v)
        filas_v.append(
            [
                v,
                getattr(cfg, "prioridad", "—") if cfg else "—",
                getattr(cfg, "fuente_principal", "—") if cfg else "—",
                pct,
            ]
        )
    fuentes = [f for f in meta["fuentes"] if not f["id"].startswith("objetivos")]
    enr = meta.get("enriquecimiento", {}).get("fuentes", {})
    filas_f = [[f["id"], f.get("edicion", ""), "donantes / objetivos"] for f in fuentes]
    filas_f += [[k, v, "enriquecimiento"] for k, v in enr.items()]
    don = meta.get("donantes", {})
    out = [
        f"# Ficha de datos · {run_id}",
        "",
        "## Identificación",
        f"- Territorio: {meta['territorio']['codigo']} ({meta['territorio']['tipo']})",
        f"- Tamaño: {meta['tamano_obtenido']:,} personas, {meta['hogares']:,} hogares".replace(
            ",", "."
        ),
        f"- Modo: {meta['modo']}",
        f"- Fecha de referencia: {meta['fecha_referencia']} (datos con corte en junio de 2026)",
        f"- Semilla: {meta['semilla']} · Versión del código: {meta['version_codigo']}",
        "",
        "## Fuentes",
        _tabla(filas_f, ["Fuente", "Edición", "Uso"]),
        "",
        "Objetivos de calibración: " + ", ".join(meta["objetivos_calibrados"]) + ".",
        "",
        "## Variables",
        _tabla(filas_v, ["Variable", "Prioridad", "Fuente", "% de valores por método"]),
        "",
        "## Calidad",
        "- Validación: F4, F5 y F6 superadas (`reports/fase_04.md`, `fase_05.md`, `fase_06.md`); "
        "auditoría de F7 en `reports/fase_07.md`.",
        f"- Donantes locales: {100 * don.get('proporcion_local', 0):.1f} %"
        if don.get("proporcion_local") is not None
        else "- Donantes locales: —",
        "- Confianza esperada del territorio: alta (país)",
        "",
        "## Grupos vigilados",
        tabla_grupos(pob),
        "",
        "## Limitaciones conocidas",
        LIMITACIONES,
        "## Límites de uso",
        LIMITES_USO,
    ]
    texto = "\n".join(out)
    destino = REPORTS_DIR / run_id
    destino.mkdir(parents=True, exist_ok=True)
    (destino / "ficha.md").write_text(texto, "utf-8")
    del p, lin
    return texto


def informe() -> str:
    res = _resumen()
    nac = res["poblaciones"][0]
    filas_t = []
    for x in res["poblaciones"]:
        c = Counter(g["semaforo"] for g in x["grupos"])
        rojos = [g["grupo"] for g in x["grupos"] if g["semaforo"] == "rojo"]
        filas_t.append(
            [
                x["territorio"]
                .replace("MUNIS:configs/territorios/", "MUNIS:")
                .removesuffix(".yaml"),
                str(c.get("verde", 0)),
                str(c.get("ambar", 0)),
                str(c.get("rojo", 0)),
                ", ".join(rojos) or "—",
            ]
        )
    div = nac.get("v_diversidad", [])
    filas_d = [
        [
            d["atributo"],
            str(d["grupos"]),
            _f(d["proporcion_ok"]),
            _f(d["ratio_mediano"]),
            "✅" if d["ok"] else "❌",
        ]
        for d in div
    ]
    rar = nac.get("v_rareza", [])
    filas_r = [[r["nivel"], str(r["combinaciones"]), str(r["sin_donante"])] for r in rar]
    out = [
        "# Fase 07 · Auditoría de sesgos y minorías",
        "",
        "**Estado:** pendiente de revisión humana (G7.7)",
        f"**Fecha:** {dt.date.today().isoformat()} · **Versión del código:** {code_version()}",
        "**Comando para reproducir:** `python -m sinpop.validate.fase7 && "
        "python -m sinpop.validate.informe_f7 && sinpop validate --phase 7` "
        "(tras la cadena F3-F6 de `reports/fase_06.md`)",
        "",
        "## Resumen",
        "Se auditan la población nacional de 1.000.000 de personas y los 30 territorios de la serie"
        " de F5 con la lista de vigilancia (`configs/watchlist.yaml`): representación, perfil"
        " interno, concentración de donantes, diversidad dentro de grupos y combinaciones sin"
        " donante. La auditoría destapó desfases de los datos de entrada (D-049, D-050), que se"
        " corrigieron en origen y obligaron a repetir F3-F6. Los criterios para grupos pequeños"
        " incluyen el margen de muestreo (D-051).",
        "",
        "## Puerta de salida",
        "Ver `reports/fase_07_puerta.md` (`sinpop validate --phase 7`).",
        "",
        "## Resultados principales",
        "",
        f"### Población nacional ({nac['run_id']})",
        tabla_grupos(nac),
        "",
        "Diversidad dentro de grupos (V-DIVERSIDAD):",
        _tabla(filas_d, ["Atributo", "Grupos", "Proporción dentro", "Ratio mediano", ""]),
        "",
        "Combinaciones sin donante (V-RAREZA):",
        _tabla(filas_r, ["Nivel", "Combinaciones", "Sin donante"]),
        "",
        "### Semáforo por población",
        _tabla(filas_t, ["Población", "Verde", "Ámbar", "Rojo", "Grupos en rojo"]),
        "",
        "Detalle por población en `reports/fase_07/` y ficha de datos de la población nacional en"
        f" `reports/{nac['run_id']}/ficha.md`.",
        "",
        "## Decisiones tomadas",
        "- D-049: la relación con la actividad, de la EPA 2T 2026, con la situación de inactividad"
        " por prioridad (SIDI1-3 y CURSR); nuevos objetivos «sin estudios» y nacidos fuera ×"
        " nacionalidad; celdas sin donantes.",
        "- D-050: estado civil y nacionalidad × edad calibrados; actividad por sexo, por"
        " nacionalidad y con 16-19 y 20-24 por separado; atributo `cursa_formacion` y jóvenes"
        " ni-ni de Eurostat; referencia de tipo de hogar × edad con tasas de jefatura; reglas de"
        " fusión para celdas sin solución; correcciones de código.",
        "- D-051: márgenes de muestreo en V-MINORIAS-PERFIL, V-CONCENTRACION y V-DIVERSIDAD;"
        " limitaciones de composición; ampliación propia de los donantes de cada nacionalidad.",
        "",
        "## Limitaciones",
        LIMITACIONES,
        "## Límites de uso",
        LIMITES_USO,
        "## Problemas abiertos y riesgos",
        "- Los grupos en rojo o ámbar de la tabla por población (casi todos, nacionalidades"
        " minoritarias en territorios pequeños) no deben analizarse por separado.",
        "- Las capas de opinión y política (F8) se apoyarán en esta población: sus sesgos se"
        " heredan.",
        "",
        "## Qué necesita revisión humana",
        "1. ¿Se aprueba la población (G7.7) con las limitaciones de esta sección?",
        "2. ¿Se aprueban D-049 y D-050, en vigor y pendientes de aprobación expresa en esta"
        " revisión?",
        "3. Si quedan grupos en rojo en territorios pequeños, ¿se aceptan como limitación"
        " declarada o se exige otra medida correctora?",
    ]
    texto = "\n".join(out) + "\n"
    INFORME.write_text(texto, "utf-8")
    return texto


if __name__ == "__main__":
    ficha()
    informe()
    print(f"Informe: {INFORME}")
