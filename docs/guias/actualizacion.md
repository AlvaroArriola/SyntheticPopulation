# Guía de actualización

Qué cambiar y qué revalidar cuando sale una edición nueva de una fuente, cuando hay elecciones o cuando llega un barómetro nuevo del CIS. La regla es la misma en todos los casos:

1. Se cambia lo mínimo.
2. Se registra la decisión en `DECISIONS.md`.
3. Se repite la cadena **desde la primera fase afectada**, con sus puertas.

Nunca se relaja un umbral para que una puerta pase.

## 1. Edición nueva de una fuente

Por ejemplo, la ECV 2026, la EPA del trimestre siguiente o la ECP a 1 de enero de 2027.

1. **Descargar y registrar.**
   - Ejecuta `sinpop ingest --source <id> --url <url oficial>`, o `--ine-table <id>` para las tablas del INE.
   - El manifiesto `data/raw/MANIFEST.yaml` guarda la edición, la URL y el SHA-256.
   - Actualiza `edicion` y `url_oficial` de la fuente en `configs/sources.yaml`.
2. **Comprobar el diseño de registro** contra el de la edición anterior (regla 2).
   - Si cambia un código, una categoría o un nombre de variable, se actualiza su recodificación en `configs/variables.yaml`, verificada contra el diseño de registro nuevo.
   - Un código no documentado detiene el proceso y se registra como duda.
   - Los generadores de recodificaciones están en `tools/generar_recodificaciones_*.py`.
3. **Armonizar y validar:**

   ```bash
   sinpop harmonize --source <id> && sinpop harmonize --check && sinpop validate --phase 2
   ```

   `--check` reproduce cifras oficiales de la edición nueva (G2.4). Si no cuadran, revisa primero los códigos y el universo, no el método (`CLAUDE.md`, «Cuando algo no cuadre»).
4. **Repetir desde la fase afectada:**

   | Fuente | Primera fase que se repite |
   | --- | --- |
   | ECP, Padrón, Censo Anual (tablas) | F3 (objetivos) y todo lo posterior |
   | Censo 2021 / Censo Anual (microdatos) | F2, F3 y todo lo posterior |
   | ECV, EPA, TIC-H, ESdE, Atlas de renta | F6 (enriquecimiento), F7 y las capas que usan esas variables |
   | CIS (barómetros) | F8A y todo lo posterior (ver la sección 3) |
   | ESS | F8B (actitudes por donantes) |

5. **Comprobar la reproducibilidad.** Genera dos veces la misma población con la misma semilla y comprueba que dan el mismo hash (V-REPRO, en la puerta de F4).
6. **Comprobar las citas.** Ejecuta `python -m sinpop.audit.citas`, que regenera `docs/guias/fuentes_y_citas.md` con las ediciones nuevas.

## 2. Después de unas elecciones

La capa política se calibra contra **resultados oficiales**, nunca contra el recuerdo declarado en el CIS (regla 10).

1. **Resultados oficiales.**
   - Añade la elección a `configs/elecciones.yaml`: `id`, `tipo`, `fecha`, `ambito`, `fuente`, `url_oficial`, `uso: calibrar` y lo que haya que verificar.
   - Descarga los resultados oficiales del escrutinio general.
   - Las autonómicas tienen un lector por comunidad en `src/sinpop/harmonize/autonomicas/ccaa_XX.py`, con su constante `ELECCION`.
   - La puerta G2.6 exige 0 diferencias con los totales oficiales.
2. **Candidaturas nuevas.**
   - Asigna cada candidatura de `configs/partidos.yaml` a una familia, con sus códigos del CIS si existen.
   - Cada correspondencia entre elecciones o estudios se documenta en `DECISIONS.md` (regla 10). Un partido nuevo que no encaje en ninguna familia es una decisión humana, no una suposición.
   - G2.7 exige 0 códigos del CIS sin asignar.
3. **Objetivos electorales.**
   - Ejecuta `sinpop targets --territory all`.
   - El censo electoral de residentes resta el CERA (D-067) y se compara con los españoles de 18+ (G3.6).
4. **Recuerdo de voto.**
   - Para unas **generales**, cambia la elección de referencia en `src/sinpop/politics/recuerdo.py` (`ELECCION`). Recalcula el derecho a voto en esa fecha (`politics/derecho.py`): solo recibe recuerdo quien podía votar.
   - Los estudios postelectorales del CIS de la nueva elección entran en `configs/partidos.yaml` (`recuerdo_cis_*`).
   - Las autonómicas solo cambian el recuerdo autonómico de su comunidad.
5. **Validar:**

   ```bash
   sinpop politics --run <run_id> && python -m sinpop.validate.fase8b && sinpop validate --phase 8b
   ```

   F8B tiene **revisión humana** (G8B.9).
6. **Banco de eventos.** Añade la elección a `configs/eventos.yaml`, con su fuente oficial, y ejecuta `python -c "from sinpop.temporal import eventos as E; E.construir()"`.

## 3. Actualización mensual: un barómetro nuevo del CIS

Hay dos casos, y la diferencia importa.

### a) El barómetro es de **después** de la fecha de corte (el caso normal)

- **No entra en la construcción.** Va a la ventana de evaluación (`src/sinpop/evaluate/`, D-069) y sirve para medir, no para ajustar.
- **Descarga.** Ejecuta `python tools/descargar_cis.py --solo-fichas --fichas <estudio>`. El script guarda en la ventana de evaluación, y no en `data/raw/`, los estudios con trabajo de campo posterior al corte. Ningún módulo de construcción los lee (regla 5).
- **Uso.** Se añade a `EVALUACION_FINAL` en `src/sinpop/evaluate/validacion.py` y se usa en la siguiente evaluación limpia.

### b) Mover la fecha de corte (incorporar meses nuevos a la construcción)

Es un cambio mayor y se registra en `DECISIONS.md`.

1. **Fecha nueva.** Cambia `fecha_corte_construccion` en `configs/llm.yaml`. Sigue siendo el último día con datos.
2. **Constantes de cada capa.** Cambia las que dependen de esa fecha:
   - `CORTE` en `opinion/cis.py` y `politics/recuerdo.py`;
   - `FECHA_REFERENCIA` en `politics/derecho.py`, `politics/run.py` y `opinion/run.py`;
   - `periodo.hasta` en `configs/temporal.yaml`.

   `tests/unit/test_corte.py` falla si alguna queda desalineada.
3. **Modelos de lenguaje.** Comprueba que sus fechas de corte de conocimiento no son posteriores a la fecha nueva; `configs/llm.yaml` lo rechaza al cargar si lo son. Si un modelo conoce el periodo de evaluación, la evaluación con LLM deja de ser limpia.
4. **Ventanas.** Los barómetros que pasen a quedar antes del corte salen de las ventanas de `evaluate/validacion.py` y entran en la construcción. El test comprueba que las ventanas siguen siendo posteriores.
5. **Cadena y puertas.** Repite F8A, F8B y F8C, y después F9 (`calibracion.construir`) y F10 (*backtest* de confianza), con sus puertas.
6. **Ventana limpia.** Las preguntas ya usadas para validar no sirven como evaluación final: hace falta una ventana nueva y limpia para F11.

## 4. Cambiar de modelo de lenguaje

- Cambiar el modelo de una tarea en `configs/llm.yaml` (`tareas`) es una decisión registrada.
- Obliga a repetir `python -m sinpop.evaluate.llm`, con la misma ventana de validación.
- El modelo nuevo debe declararse con su precio y su fecha de corte.
- La caché no se reutiliza entre modelos: la clave incluye el modelo y el prompt.
