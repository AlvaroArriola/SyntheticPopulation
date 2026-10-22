"""Interfaz de línea de comandos `sinpop` (docs/03_arquitectura.md, sección 5).

Los comandos de fases aún no implementadas terminan con código 2 y un mensaje que
indica la fase en la que se implementan.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from sinpop import REPORTS_DIR

app = typer.Typer(
    help="Población sintética de las personas adultas residentes en España.",
    no_args_is_help=True,
    add_completion=False,
)

# Comandos documentados en docs/03 · sección 5 (G0.4 comprueba que todos aparecen en --help)
COMMANDS = (
    "ingest",
    "harmonize",
    "targets",
    "build",
    "validate",
    "audit",
    "opinion",
    "politics",
    "temporal",
    "predict",
    "evaluate",
)


def _pendiente(comando: str, fase: str) -> None:
    typer.echo(f"`sinpop {comando}` se implementa en la fase {fase}.", err=True)
    raise typer.Exit(code=2)


@app.command()
def ingest(
    source: Annotated[
        str, typer.Option(help="Id de fuente de configs/sources.yaml o 'all'")
    ] = "all",
    url: Annotated[str | None, typer.Option(help="URL oficial del fichero a descargar")] = None,
    register: Annotated[
        Path | None,
        typer.Option(help="Registra un fichero ya colocado en data/raw/<fuente>/<edicion>/"),
    ] = None,
    edition: Annotated[str | None, typer.Option(help="Edición del fichero")] = None,
    tipo: Annotated[
        str, typer.Option(help="datos | diseno_registro | metodologia | cuestionario | otro")
    ] = "datos",
    verify: Annotated[bool, typer.Option(help="Verifica los hashes del manifiesto")] = False,
    ine_table: Annotated[
        int | None, typer.Option(help="Id de tabla de INEbase (API Tempus) a descargar en JSON")
    ] = None,
    date: Annotated[str | None, typer.Option(help="Periodo AAAAMMDD de la tabla INE")] = None,
    metadata: Annotated[
        bool, typer.Option(help="Tabla INE con códigos de dimensiones (tip=AM)")
    ] = False,
    inventory: Annotated[bool, typer.Option(help="Genera el inventario de F1")] = False,
    extract: Annotated[
        list[str] | None, typer.Option(help="Patrón de ficheros a extraer del ZIP registrado")
    ] = None,
) -> None:
    """Descarga o registra fuentes oficiales en data/raw/MANIFEST.yaml (F1)."""
    from sinpop.config import load_config
    from sinpop.ingest import manifest

    if inventory:
        from sinpop.ingest.inventory import run as _inventory

        data = _inventory()
        typer.echo(f"{len(data['perfiles'])} ficheros perfilados · reports/fase_01_inventario.md")
        return
    if verify:
        res = manifest.verify()
        for f, estado in res.items():
            typer.echo(f"{estado:>14}  {f}")
        sin = manifest.unregistered_files()
        for f in sin:
            typer.echo(f"{'sin registrar':>14}  {f}")
        typer.echo(f"{len(res)} ficheros en el manifiesto; {len(sin)} sin registrar.")
        raise typer.Exit(code=0 if all(v == "ok" for v in res.values()) and not sin else 1)

    fuentes = {f.id: f for f in load_config("sources.yaml").fuentes}  # type: ignore[attr-defined]
    if source not in fuentes:
        typer.echo(f"Fuente desconocida: {source}. Usa un id de configs/sources.yaml.", err=True)
        raise typer.Exit(code=2)
    f = fuentes[source]
    if edition is None:
        typer.echo("Indica --edition.", err=True)
        raise typer.Exit(code=2)
    if extract:
        from sinpop.ingest.extract import extract as _extract

        for e in _extract(source, edition, extract):
            typer.echo(f"Extraído {e.fichero} · sha256 {e.sha256[:12]} · {e.bytes} bytes")
        return
    if ine_table is not None:
        from sinpop.ingest.download import download_ine_table

        e = download_ine_table(
            ine_table, source, edition, f.condiciones, fecha=date, metadatos=metadata
        )
        from sinpop.ingest.download import download_ine_table_meta

        download_ine_table_meta(ine_table, source, edition, f.condiciones)
    elif register is not None:
        e = manifest.register_file(
            register,
            source,
            edition,
            url or f.url_oficial,
            f.condiciones,
            tipo=tipo,  # type: ignore[arg-type]
        )
    elif url is not None:
        from sinpop.ingest.download import download

        e = download(url, source, edition, f.condiciones, tipo=tipo)
    else:
        typer.echo(
            "Indica --url (descarga desde la web oficial) o --register (fichero ya colocado). "
            "Ver data/raw/MANUAL_DOWNLOADS.md.",
            err=True,
        )
        raise typer.Exit(code=2)
    typer.echo(f"Registrado {e.fichero} · sha256 {e.sha256} · {e.bytes} bytes")


@app.command()
def harmonize(
    source: Annotated[str, typer.Option(help="Id de fuente o 'all'")] = "all",
    check: Annotated[
        bool, typer.Option("--check", help="Reproduce las cifras oficiales publicadas (G2.4)")
    ] = False,
    samples: Annotated[
        bool, typer.Option("--samples", help="Muestras de 20 registros por fuente (G2.8)")
    ] = False,
) -> None:
    """Lee cada fuente con su diseño de registro y la armoniza a configs/variables.yaml (F2)."""
    if samples:
        from sinpop.harmonize import muestras

        res = muestras.muestras()
        typer.echo(f"{len(res)} muestras en data/interim/muestras_g28/ · {muestras.informe(res)}")
        return
    if check:
        from sinpop.harmonize import checks, oficiales

        res = oficiales.informe(oficiales.todas(), REPORTS_DIR / "fase_02_cifras_oficiales")
        for f, n, k in res.iter_rows():
            typer.echo(f"{f}: {k}/{n} cifras dentro de tolerancia")
        cal = checks.informe_calidad(REPORTS_DIR / "fase_02_calidad.md")
        typer.echo(f"calidad: {cal.height} variables; {int(cal['revisar'].sum())} para revisar")
        return
    from sinpop.harmonize.run import ejecutar

    for nombre, info in ejecutar(source).items():
        typer.echo(f"{nombre}: {info['filas']} filas · sha256 {info['sha256'][:12]}")


@app.command()
def targets(
    territory: Annotated[
        str,
        typer.Option(help="ES, CCAA:XX, PROV:XX, MUNIS:<yaml> o 'all' (España, CCAA y provincias)"),
    ] = "ES",
    date: Annotated[str, typer.Option(help="Fecha de referencia AAAA-MM-DD")] = "2026-01-01",
) -> None:
    """Construye los objetivos de calibración y los reservados de un territorio (F3)."""
    from sinpop.config import load_config
    from sinpop.targets import run

    fecha = str(load_config("targets.yaml").fecha_referencia)  # type: ignore[attr-defined]
    if date != fecha:
        typer.echo(f"Solo hay objetivos para la fecha de targets.yaml ({fecha}).", err=True)
        raise typer.Exit(code=2)
    terr = run.territorios_estandar() if territory == "all" else [territory]
    for t, info in run.ejecutar(terr).items():
        typer.echo(f"{t}: {info['filas']} filas · sha256 {info['sha256'][:12]}")


@app.command()
def build(
    territory: Annotated[str, typer.Option(help="ES, CCAA:XX, PROV:XX o MUNIS:<yaml>")] = "ES",
    size: Annotated[int, typer.Option(help="Número de personas")] = 100_000,
    seed: Annotated[int, typer.Option(help="Semilla (obligatoria para reproducibilidad)")] = 42,
    oversample: Annotated[
        str | None, typer.Option(help="Sobremuestreo, p. ej. 'edad_5>=85:2000'")
    ] = None,
) -> None:
    """Genera una población sintética (F4 nacional, F5 territorial)."""
    if territory.startswith("MUNIS:"):
        _pendiente("build --territory MUNIS:…", "F5")
    from sinpop.synth.poblacion import construir

    meta = construir(territory, size, seed, oversample)
    typer.echo(
        f"{meta['run_id']}: {meta['tamano_obtenido']} personas, {meta['hogares']} hogares "
        f"· data/populations/{meta['run_id']}/"
    )


@app.command()
def validate(
    phase: Annotated[
        str | None, typer.Option(help="Ejecuta la puerta de la fase N (0-7, 8a, 8b, 8c…)")
    ] = None,
    run: Annotated[str | None, typer.Option(help="Valida la población <run_id>")] = None,
) -> None:
    """Ejecuta las comprobaciones de una puerta de fase o de una población."""
    from sinpop.validate.phases import run_phase

    if phase is None and run is None:
        typer.echo("Indica --phase N o --run <run_id>.", err=True)
        raise typer.Exit(code=2)
    if run is not None:
        from sinpop.validate.fase4 import validar_poblacion

        ok = validar_poblacion(run)
        typer.echo(
            f"{run}: validación {'superada' if ok else 'fallida'} · reports/{run}/validacion.md"
        )
        raise typer.Exit(code=0 if ok else 1)
    ok = run_phase(int(phase) if phase.isdigit() else phase.lower())  # type: ignore[union-attr]
    raise typer.Exit(code=0 if ok else 1)


@app.command()
def audit(run: Annotated[str, typer.Option(help="run_id de la población")]) -> None:
    """Auditoría de sesgos y minorías de una población (F7)."""
    import json

    from sinpop import POPULATIONS_DIR, REPORTS_DIR
    from sinpop.audit import auditoria as A
    from sinpop.validate import poblacion as V

    if not (POPULATIONS_DIR / run / "persons.parquet").exists():
        typer.echo(f"No existe la población {run}", err=True)
        raise typer.Exit(code=1)
    p, lin, meta = V.cargar(run)
    a = A.auditar(p, lin, meta["territorio"]["codigo"])
    out = REPORTS_DIR / run
    out.mkdir(parents=True, exist_ok=True)
    (out / "auditoria.json").write_text(
        json.dumps(a.to_dicts(), ensure_ascii=False, indent=1, default=float), "utf-8"
    )
    for fila in a.select("grupo", "semaforo", "ratio").to_dicts():
        r = f"{fila['ratio']:.3f}" if fila["ratio"] is not None else "-"
        typer.echo(f"{fila['semaforo']:<12} {fila['grupo']:<40} ratio {r}")
    typer.echo(f"Auditoría: {out / 'auditoria.json'}")


@app.command()
def opinion(run: Annotated[str, typer.Option(help="run_id de la población")]) -> None:
    """Asigna la capa de opinión y valores (F8A)."""
    from sinpop import POPULATIONS_DIR
    from sinpop.opinion import run as OR

    if not (POPULATIONS_DIR / run / "persons.parquet").exists():
        typer.echo(f"No existe la población {run}", err=True)
        raise typer.Exit(code=1)
    m = OR.construir(run)
    typer.echo(f"{run}: opinion.parquet con {m['personas']} adultos · {list(m['variables'])}")


@app.command()
def politics(
    run: Annotated[str, typer.Option(help="run_id de la población")],
    election: Annotated[str, typer.Option(help="Elección de referencia")] = "generales-2023",
) -> None:
    """Asigna la capa política calibrada a resultados oficiales (F8B)."""
    from sinpop import POPULATIONS_DIR

    if election != "generales-2023":
        typer.echo(
            "Solo está calibrada la elección generales-2023 (D-067). Para otra, sigue la guía de "
            "actualización tras unas elecciones (docs/guias/actualizacion.md).",
            err=True,
        )
        raise typer.Exit(code=2)
    if not (POPULATIONS_DIR / run / "opinion.parquet").exists():
        typer.echo(f"{run}: falta opinion.parquet (sinpop opinion --run {run})", err=True)
        raise typer.Exit(code=1)
    from sinpop.politics.run import construir

    m = construir(run)
    typer.echo(f"{run}: politics.parquet · {m.get('personas', '')} adultos")


@app.command()
def temporal(
    run: Annotated[str, typer.Option(help="run_id de la población")],
    from_: Annotated[str, typer.Option("--from", help="Periodo inicial AAAA-MM")] = "2023-01",
    to: Annotated[str, typer.Option(help="Periodo final AAAA-MM")] = "2026-06",
) -> None:
    """Genera las trayectorias temporales de los rasgos (F8C)."""
    import yaml

    from sinpop import CONFIGS_DIR

    periodo = yaml.safe_load((CONFIGS_DIR / "temporal.yaml").read_text("utf-8"))["periodo"]
    desde, hasta = periodo["desde"], periodo["hasta"]
    if (from_, to) != (desde, hasta):
        typer.echo(
            f"El periodo lo fija configs/temporal.yaml ({desde} a {hasta}); cambiarlo es una "
            "decisión registrada que obliga a revalidar F8C.",
            err=True,
        )
        raise typer.Exit(code=2)
    from sinpop.temporal.trayectorias import construir

    m = construir(run)
    typer.echo(f"{run}: trajectories.parquet · {m.get('filas', '')} filas")


@app.command()
def predict(
    run: Annotated[str, typer.Option(help="run_id de la población")],
    question: Annotated[Path | None, typer.Option(help="preguntas/<id>.json")] = None,
    event: Annotated[Path | None, typer.Option(help="preguntas/<id>.json de tipo evento")] = None,
) -> None:
    """Predice la distribución de respuestas a una pregunta o el efecto de un evento (F9).

    Las salidas son resultados simulados (docs/08), no una encuesta."""
    import json

    if (question is None) == (event is None):
        typer.echo("Indica --question o --event (uno de los dos).", err=True)
        raise typer.Exit(code=2)
    if question is not None:
        from sinpop.predict.salida import predecir_fichero

        destino = predecir_fichero(question, run)
        typer.echo(f"Predicción (resultado simulado): {destino}")
        return
    import datetime as dt

    from sinpop.predict import evento as V
    from sinpop.predict.salida import PREDICCIONES_DIR

    e = json.loads(event.read_text("utf-8"))  # type: ignore[union-attr]
    ev = e["evento"]
    fecha = dt.date.fromisoformat(ev["fecha"])
    if "indicador" in ev:  # indicador de configs/temporal.yaml
        out = V.predecir(
            ev["indicador"],
            fecha,
            ev["tipo"],
            ev.get("ambito", "ES"),
            ev.get("descripcion"),
            e["id"],
        )
    else:  # efecto sobre la pregunta del fichero (docs/03 §2.8)
        from sinpop.predict import estimador as E
        from sinpop.predict import opciones as O

        q = E.Pregunta(
            e["id"],
            e["enunciado"],
            e["opciones"],
            e.get("escala") or O.escala_probable(e["opciones"]),
            ev["fecha"][:7],
            [],
        )
        out = V.predecir_pregunta(q, ev["descripcion"], fecha, ev.get("ambito", "ES"), run)
    out = {"id": e["id"], "resultado_simulado": True, **out}
    PREDICCIONES_DIR.mkdir(parents=True, exist_ok=True)
    destino = PREDICCIONES_DIR / f"{e['id']}_evento.json"
    destino.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), "utf-8")
    typer.echo(f"Evento (resultado simulado): {destino}")


@app.command()
def evaluate(tag: Annotated[str, typer.Option(help="Etiqueta git congelada")]) -> None:
    """Evaluación final sin contaminación, una sola vez (F11)."""
    # La CLI no importa sinpop.evaluate: solo ese paquete toca la ventana de evaluación (regla 5,
    # tests/test_no_leakage.py). La evaluación se lanza como módulo propio.
    typer.echo(
        f"La evaluación final se ejecuta aislada: python -m sinpop.evaluate.final --tag {tag}",
        err=True,
    )
    raise typer.Exit(code=2)


if __name__ == "__main__":  # pragma: no cover
    app()
