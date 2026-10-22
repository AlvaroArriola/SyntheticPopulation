# Guía de uso

Cómo instalar el proyecto, generar y validar una población, y usar las capas de opinión, política, tiempo y predicción. Todos los comandos se ejecutan desde la raíz del repositorio. Las decisiones que explican cada paso están en `DECISIONS.md`, y los resultados de cada fase en `reports/fase_XX.md`.

## 1. Instalación

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"            # núcleo y tests
pip install -e ".[dev,llm]"        # además, la capa opcional de modelo de lenguaje
sinpop --help
sinpop validate --phase 0          # comprueba la instalación (tests, configuraciones, fugas)
```

## 2. Datos de entrada

Los microdatos oficiales **no están en el repositorio**: sus condiciones no permiten redistribuirlos, y la regla 8 de `CLAUDE.md` los deja en local.

- **Descarga automática** (INE, Ministerio del Interior, CIS):

  ```bash
  sinpop ingest --source all     # descarga y registra cada fichero en data/raw/MANIFEST.yaml (URL y SHA-256)
  sinpop ingest --verify         # comprueba los hashes de lo descargado
  python tools/descargar_cis.py --tipos barometro,sanitario --fichas-barometro 2023-2026
  ```

- **Descarga manual:** algunas fuentes exigen registrarse, como la ESS en https://ess.sikt.no/. La lista de ficheros esperados y sus rutas está en `data/raw/MANIFEST.yaml` y `data/raw/MANUAL_DOWNLOADS.md`.
- **Citas y condiciones de cada fuente:** `docs/guias/fuentes_y_citas.md`.

## 3. Cadena completa desde cero

Cada paso tiene su puerta: `sinpop validate --phase N`. Si una puerta falla, **no se sigue**: el informe `reports/fase_XX_puerta.md` dice qué comprobación falla. Los tiempos son orientativos, en un equipo de 4 núcleos y 16 GB.

```bash
# F2 · armonización (≈ 30 min)
sinpop harmonize --source all && sinpop harmonize --check && sinpop validate --phase 2

# F3 · objetivos de calibración de España, las 19 comunidades, las 52 provincias y los municipios de ejemplo
sinpop targets --territory all
for m in configs/territorios/*.yaml; do sinpop targets --territory "MUNIS:$m"; done
sinpop validate --phase 3

# F4-F7 · poblaciones, enriquecimiento y auditoría (≈ 5 h; ver reports/fase_06.md y fase_07.md)
python -m sinpop.validate.fase4 && sinpop validate --phase 4
python -m sinpop.validate.fase5 && sinpop validate --phase 5
python -m sinpop.validate.fase6 && sinpop validate --phase 6
python -m sinpop.validate.fase7 && python -m sinpop.validate.informe_f7 && sinpop validate --phase 7

# F8A-F8C · opinión, política y tiempo, sobre la población nacional de 1 millón
RUN=2026-01-01_ES_1000000_s1
python -c "from sinpop.opinion import cis, lengua, ess; cis.armonizar(); lengua.armonizar(); ess.armonizar()"
sinpop opinion --run $RUN && python -m sinpop.validate.fase8a && sinpop validate --phase 8a
sinpop politics --run $RUN && python -m sinpop.validate.fase8b && sinpop validate --phase 8b
sinpop temporal --run $RUN
python -c "from sinpop.temporal import eventos as E; E.construir()"
python -m sinpop.validate.fase8c && sinpop validate --phase 8c

# F9-F10 · predicción y confianza (≈ 4 h)
python -c "from sinpop.predict import calibracion as C; C.construir()"
python -m sinpop.evaluate.validacion && sinpop validate --phase 9
python -c "from sinpop.confidence.run import construir; construir(rehacer_backtest=True)"
python -m sinpop.evaluate.confianza && python -m sinpop.confidence.diagrama && sinpop validate --phase 10
```

## 4. Generar una población

```bash
sinpop build --territory ES --size 100000 --seed 42            # España
sinpop build --territory CCAA:12 --size 50000 --seed 7         # Galicia (códigos INE de comunidad)
sinpop build --territory PROV:44 --size 20000 --seed 7         # Teruel (códigos INE de provincia)
sinpop build --territory ES --size 100000 --seed 42 --oversample "edad_5>=85:2000"
sinpop validate --run 2026-01-01_ES_100000_s42                 # informe en reports/<run_id>/
sinpop audit --run 2026-01-01_ES_100000_s42                    # sesgos y minorías (F7)
```

- **Reproducibilidad:** la misma configuración y la misma semilla dan ficheros idénticos (mismo SHA-256).
- **Identificador:** cada población se guarda en `data/populations/<run_id>/`. El `run_id` es `<fecha>_<territorio>_<tamaño>_s<semilla>`.
- **Ficheros:**
  - `persons.parquet` y `households.parquet`;
  - `lineage.parquet`: de qué donante viene cada hogar;
  - `metadata.json`: fuentes, configuración, semilla, fecha y versión del código.
- **Capas de opinión, política y tiempo:**
  - Se añaden con `sinpop opinion`, `sinpop politics` y `sinpop temporal` sobre el `run_id`.
  - Crean `opinion.parquet`, `politics.parquet` y `trajectories.parquet`, unidos por `person_id`.
  - Ninguna variable de opinión ni de política entra en `persons.parquet` (regla 9).
- **Municipios:** los territorios por lista de municipios (`MUNIS:<yaml>`) tienen objetivos (`sinpop targets`), pero el comando `build` aún no los genera directamente: la serie de F5 los construye con `python -m sinpop.validate.fase5`.

## 5. Predecir una pregunta o un evento

Las salidas son **resultados simulados**: lo indican el campo `resultado_simulado` y el campo `aviso`.

- **Pregunta cerrada:** `preguntas/<id>.json`, con el formato de `docs/03` §2.8. Hay un ejemplo en `preguntas/Q001_ejemplo.json`.

  ```bash
  sinpop predict --run 2026-01-01_ES_1000000_s1 --question preguntas/Q001_ejemplo.json
  # → reports/fase_09/predicciones/Q001_<run_id>.json
  ```

  La salida trae:
  - la distribución con intervalos del 80 % y del 95 %, en total y por subgrupo;
  - dos versiones: `total` (la población) y `medicion_cis` (lo que mediría un barómetro del CIS);
  - la confianza del modelo de F10: la probabilidad de que el error sea ≤ 0,10;
  - las preguntas del banco en las que se apoya.

- **Evento:** `preguntas/<id>.json` con `"tipo": "evento"`. Hay un ejemplo en `preguntas/E001_ejemplo.json`; los indicadores disponibles están en `configs/temporal.yaml`.

  ```bash
  sinpop predict --run 2026-01-01_ES_1000000_s1 --event preguntas/E001_ejemplo.json
  ```

  Devuelve el nivel antes, el de después y el cambio por categoría. Sin LLM, el cambio es la media de los eventos análogos del banco (`configs/eventos.yaml`), que no sabe quién gana o pierde (`reports/fase_09.md`).

## 6. Capa opcional de modelo de lenguaje

Está **desactivada** por defecto y todo funciona sin ella (D-069, D-071). Se usa solo donde el método gratuito no llega:
- preguntas sin precedentes en el banco;
- la dirección del cambio en el modo evento;
- el baseline B2.

Para activarla:

1. Pon la clave del proveedor en el entorno, **nunca** en un fichero del repositorio: `export ANTHROPIC_API_KEY=…`.
2. En `configs/llm.yaml`, cambia `activo: false` por `activo: true`.
3. Antes de gastar nada, consulta la cota de coste: `python -m sinpop.evaluate.llm --estimar`.

Garantías:
- **Presupuesto:** cada ejecución se detiene antes de enviar si la cota superior supera 10 € por ejecución o 15 € en total (`presupuesto` en `configs/llm.yaml`).
- **Caché:** las respuestas se guardan en `logs/llm/cache/`, así que repetir una predicción no vuelve a pagar.
- **Registro de gasto:** `logs/llm/gasto.jsonl`.
- **Privacidad:** al modelo solo le llegan enunciados públicos y agregados, nunca microdatos.

## 7. Comprobar que todo está bien

```bash
python -m pytest -q                      # tests (los de integración necesitan los datos en local)
python -m pytest -q tests/test_no_leakage.py   # nadie fuera de src/sinpop/evaluate/ lee la ventana de evaluación
sinpop validate --phase N                # puerta de cualquier fase
```

Antes de usar los resultados, lee los límites de uso (`docs/guias/limites_de_uso.md`).
