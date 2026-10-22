"""Prueba de la guía de actualización (G12.2): sustituir una fuente por otra edición.

Sigue `docs/guias/actualizacion.md` §1 con la EPA: la edición en uso (2T2026) se sustituye por la
anterior (1T2026, descargada y registrada en el manifiesto con `sinpop ingest`). Todo se escribe
en una carpeta temporal: los datos de producción (`data/interim/`) no se tocan.

Comprueba que:
1. el armonizador, sin cambios de código, lee la edición nueva solo con cambiar la edición;
2. los valores quedan dentro de los dominios declarados (G2.1);
3. se reproducen las cifras de la nota de prensa de la edición nueva (G2.4);
4. con la edición en uso se obtiene exactamente el mismo fichero que en producción (mismo
   SHA-256): el cambio de código para leer la edición de la configuración no altera nada.

Comando: `python tools/prueba_actualizacion.py` → `reports/fase_12/prueba_actualizacion.json`.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import polars as pl

from sinpop import INTERIM_DIR, REPORTS_DIR
from sinpop.harmonize import core, encuestas, oficiales, run
from sinpop.repro import sha256_file

NUEVA = "1T2026"
DESTINO = REPORTS_DIR / "fase_12" / "prueba_actualizacion.json"


def _armonizar(edicion: str, carpeta: Path) -> Path:
    original = encuestas.edicion_epa
    encuestas.edicion_epa = lambda: edicion  # equivale a cambiar `edicion` en sources.yaml
    try:
        run.ejecutar("epa", destino=carpeta)
    finally:
        encuestas.edicion_epa = original
    return carpeta / "epa.parquet"


def main() -> dict:
    en_uso = encuestas.edicion_epa()
    prod = INTERIM_DIR / "epa.parquet"
    sha_prod = sha256_file(prod)
    with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
        nueva = _armonizar(NUEVA, Path(t1))
        df = pl.read_parquet(nueva)
        armonizadas = [c for c in df.columns if c in core.variables().variables]
        fuera = core.comprobar_dominio(df, armonizadas)
        cifras = oficiales.cifras_epa(df, NUEVA)
        misma = sha256_file(_armonizar(en_uso, Path(t2))) == sha_prod
    ok_cifras = all(c.ok for c in cifras)
    res = {
        "fuente": "epa",
        "edicion_en_uso": en_uso,
        "edicion_nueva": NUEVA,
        "filas": df.height,
        "fuera_de_dominio": {k: v for k, v in fuera.items() if v},
        "cifras": [
            {
                "cifra": c.cifra,
                "oficial": c.oficial,
                "reproducida": c.reproducida,
                "diferencia": c.diferencia,
                "tolerancia": c.tolerancia,
            }
            for c in cifras
        ],
        "produccion_sin_cambios": sha256_file(prod) == sha_prod,
        "edicion_en_uso_reproduce_produccion": misma,
    }
    res["superada"] = bool(
        not res["fuera_de_dominio"] and ok_cifras and res["produccion_sin_cambios"] and misma
    )
    res["resumen"] = (
        f"EPA {en_uso} → {NUEVA}: {df.height} filas; fuera de dominio: "
        f"{len(res['fuera_de_dominio'])} columnas; cifras de la nota de prensa "
        f"{sum(c.ok for c in cifras)}/{len(cifras)}; "
        f"producción intacta: {res['produccion_sin_cambios']}; {en_uso} reproduce el fichero de "
        f"producción: {misma}"
    )
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    return res


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
