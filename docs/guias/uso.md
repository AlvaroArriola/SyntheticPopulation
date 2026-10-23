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

Todo funciona sin ella (D-069, D-071): sin clave en el entorno, el sistema no llama a ningún modelo. Se usa solo donde el método gratuito no llega:
- preguntas sin precedentes en el banco;
- la dirección del cambio en el modo evento;
- el baseline B2.

Para activarla:

1. Pon la clave del proveedor en el entorno, **nunca** en un fichero del repositorio: `export SINPOP_ANTHROPIC_API_KEY=…`.
2. Comprueba que `configs/llm.yaml` tiene `activo: true` (con `false` se apaga aunque haya clave).
3. Antes de gastar nada, consulta la cota de coste: `python -m sinpop.evaluate.llm --estimar`.

Garantías:
- **Presupuesto:** cada ejecución se detiene antes de enviar si la cota superior supera 10 € por ejecución o 15 € en total (`presupuesto` en `configs/llm.yaml`).
- **Caché:** las respuestas se guardan en `logs/llm/cache/`, así que repetir una predicción no vuelve a pagar.
- **Registro de gasto:** `logs/llm/gasto.jsonl`.
- **Privacidad:** al modelo solo le llegan enunciados públicos y agregados, nunca microdatos.

## 7. Interfaz web en tu ordenador (paquete portable)

La interfaz (F13-F14) necesita las poblaciones y los modelos, pero **no** los microdatos. El paquete portable (`dist/paquete/`, D-076) lleva solo agregados y poblaciones sintéticas, así que basta con el repositorio:

```bash
git clone <url del repositorio> && cd SyntheticPopulation
python -m venv .venv && source .venv/bin/activate      # en Windows: .venv\Scripts\activate
pip install -e ".[web]"
sinpop serve --paquete dist/paquete                    # abre http://127.0.0.1:8000
```

En la interfaz:
- **Mapa:** elige España, una comunidad o una provincia (botones de nivel arriba del mapa). El fondo de OpenStreetMap necesita conexión a internet.
- **Tamaño:** número de personas de la población. En modo paquete solo se pueden usar las poblaciones que van dentro (las marcadas como listas); generar poblaciones nuevas necesita los datos originales (sección 4).
- **Pregunta:** escribe el enunciado y sus opciones. Mientras escribes, salen preguntas parecidas del banco del CIS. El resultado trae la distribución con intervalos del 80 % y del 95 %, la confianza, los subgrupos y las preguntas del CIS en las que se apoya.
- **Opciones de respuesta a medida:** escribe las tuyas una a una o pégalas separadas por «;» (por ejemplo, «Al Gobierno central; A la comunidad autónoma; Al ayuntamiento; A la Unión Europea»). También hay plantillas: acuerdo, valoración, responsable, confianza, frecuencia, prioridad… «N.S.» y «N.C.» se añaden por defecto, porque son respuestas legítimas (D-085).
- **Subgrupos y regiones:** debajo del resultado, cada pregunta se desglosa por edad, sexo, estudios, ideología, recuerdo de voto, religiosidad, clase, tamaño de municipio, nacionalidad… Las diferencias más grandes salen marcadas con una estrella. Una pregunta de España se desglosa por comunidades o provincias y el mapa se colorea con esos valores (D-081).
- **Evolución, retratos y cruces:** cuando el CIS ya hizo la pregunta, una gráfica muestra cómo ha cambiado hasta hoy. Los retratos son 24 personas sintéticas con su probabilidad de cada respuesta. El cruce enseña cómo responde a una segunda pregunta cada grupo de respuesta a la primera (D-083).
- **¿De qué depende la respuesta?:** cada resultado ordena las variables del perfil por cuánto separan las respuestas (fuerza η, D-090), con la mayor diferencia entre grupos. También va en el PDF.
- **Validación** (enlace en la cabecera, `/validacion.html`): las 211 preguntas reales del CIS posteriores al corte, con lo previsto frente a lo real en total y en ocho variables de grupo. Incluye el margen de muestreo de la encuesta, la importancia prevista y real de cada variable, y las fuentes de cada cifra (D-091; `reports/validacion.md`). Se regenera con `SINPOP_PAQUETE=dist/paquete python -m sinpop.evaluate.bateria`.
- **Evento:** describe un acontecimiento y su fecha para ver el antes y el cambio esperado sobre la pregunta.
- **Datos de la población (INE y otras fuentes):** si lo que preguntas ya es un atributo de la población (salud, uso de internet, situación laboral, llegar a fin de mes, vivienda, renta…), la interfaz lo propone arriba de las sugerencias. Se muestra como **dato, no como predicción**: proporción ponderada, margen de simulación, de dónde sale cada valor (registro censal, emparejado con la encuesta oficial…) y la fuente con su variable original (D-077).
- **¿Qué tamaño necesito?** (debajo de los tamaños): según el detalle que quieras ver y el margen de simulación que aceptes, recomienda un tamaño y te dice cuánta confianza puedes esperar en ese territorio. La confianza depende sobre todo de cuántos encuestados tiene el CIS allí; más personas sintéticas no la suben (D-079).
- **Exportar:** cada resultado se descarga como **informe PDF** (resumen automático y cuatro páginas de gráficos), **CSV** (para Excel en español) o **JSON** (D-078).
- **Comparar comunidades:** sobre una pregunta de España, repite la pregunta en cada comunidad con su propia población y colorea el mapa con esos valores (D-080).
- **Consultas recientes:** las últimas diez se guardan en tu navegador y se reabren sin recalcular.
- **Modelo de lenguaje (opcional):** con `SINPOP_ANTHROPIC_API_KEY` en el entorno, las preguntas sin precedentes y los eventos usan el modelo, con los topes de la sección 6. Cada respuesta tarda unos 30-40 segundos, cuesta unos 0,05 € y trae la justificación del modelo. La interfaz no enseña el gasto (D-088): se consulta en `/api/llm` o en `logs/llm/gasto.jsonl`, y el tope se aplica igual. Si el modelo falla, se muestra la estimación sin él, con un aviso. Sin clave, los resultados dicen «Estimador sin modelo de lenguaje».
- **Presentación, compartir y atajos:** «Presentación» deja solo el mapa y el resultado (Esc para salir); «Compartir» copia un enlace que rellena la pregunta, las opciones y el territorio; Ctrl + Intro pregunta y «/» lleva al enunciado.

Donde están los datos, el paquete se rehace con `python -m sinpop.paquete.exportar` (≈ 1-2 h) y la interfaz completa, que sí genera poblaciones, se abre con `sinpop serve`.

## 8. Comprobar que todo está bien

```bash
python -m pytest -q                      # tests (los de integración necesitan los datos en local)
python -m pytest -q tests/test_no_leakage.py   # nadie fuera de src/sinpop/evaluate/ lee la ventana de evaluación
sinpop validate --phase N                # puerta de cualquier fase
```

La evaluación final (F11) se ejecuta una sola vez, desde una etiqueta git congelada y sin cambios locales: `python -m sinpop.evaluate.final --tag <etiqueta>`. Si ya existe `reports/fase_11_evaluacion.json`, se niega a repetirse.

Antes de usar los resultados, lee los límites de uso (`docs/guias/limites_de_uso.md`).
