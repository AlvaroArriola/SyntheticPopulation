# 04 · Fases del proyecto

El proyecto tiene **13 fases** (la fase 8 se divide en tres subfases). Cada una tiene un objetivo, entradas, tareas, entregables y una **puerta de salida**: comprobaciones que deben superarse para darla por terminada. Las métricas y los umbrales de cada comprobación están en `05_validacion.md` y en `configs/thresholds.yaml`.

| Fase | Nombre | Bloque | Revisión humana |
| --- | --- | --- | --- |
| F0 | Preparación del proyecto | Núcleo | No |
| F1 | Inventario y adquisición de datos | Núcleo | **Sí** |
| F2 | Comprensión y armonización | Núcleo | **Sí** |
| F3 | Objetivos de calibración por territorio | Núcleo | No |
| F4 | Población nacional base | Núcleo | **Sí** |
| F5 | Generador territorial | Núcleo | **Sí** |
| F6 | Enriquecimiento | Núcleo | No |
| F7 | Auditoría de sesgos y minorías | Núcleo | **Sí** |
| F8A | Capa de opinión y valores | Extensión | **Sí** |
| F8B | Capa política | Extensión | **Sí** |
| F8C | Dimensión temporal | Extensión | No |
| F9 | Capa de predicción con IA | Extensión | No |
| F10 | Modelo de confianza | Extensión | No |
| F11 | Evaluación final sin contaminación | Extensión | **Sí** |
| F12 | Empaquetado y documentación final | Extensión | **Sí** |

Reglas generales para todas las fases:

- Al cerrar una fase se escribe `reports/fase_XX.md` con la plantilla de `07_plantillas.md`.
- `sinpop validate --phase N` ejecuta todas las comprobaciones automáticas de la fase y devuelve un código de salida distinto de cero si alguna falla.
- Si una comprobación no se puede superar, se documenta la causa, se proponen alternativas y se pide decisión humana. **Nunca se cambia un umbral en silencio.**
- Una fase posterior que descubra un problema de una anterior **reabre** esa fase: se corrige allí y se vuelven a pasar las puertas afectadas.

---

## F0 · Preparación del proyecto

**Objetivo:** dejar un repositorio listo para trabajar de forma reproducible.

**Tareas**

1. Crear la estructura de `03_arquitectura.md`, sección 3.
2. Configurar `pyproject.toml`, entorno, linter, formateador y pytest.
3. Revisar `DECISIONS.md`, que ya contiene las decisiones de partida (D-002 a D-006; D-001 está sustituida por D-004).
4. Crear los esquemas de configuración (pydantic) para `sources.yaml`, `variables.yaml`, `targets.yaml`, `territories.yaml`, `watchlist.yaml`, `thresholds.yaml`, `partidos.yaml`, `elecciones.yaml`, `eventos.yaml` y `llm.yaml`, con los umbrales iniciales de `05_validacion.md`.
5. Crear `tests/test_no_leakage.py`.
6. Esqueleto de CLI con los comandos de `03_arquitectura.md`, sección 5, aunque aún no hagan nada.

**Entregables:** repositorio, configuraciones vacías pero válidas, `DECISIONS.md`, CLI.

**Puerta F0**

- [ ] G0.1 `pytest` se ejecuta sin errores.
- [ ] G0.2 Las configuraciones de ejemplo pasan la validación de esquema.
- [ ] G0.3 `test_no_leakage.py` existe y falla si se añade a propósito una lectura de `data/eval/` desde otro módulo (se comprueba con un test del propio test).
- [ ] G0.4 `sinpop --help` muestra todos los comandos.

---

## F1 · Inventario y adquisición de datos

**Objetivo:** tener todas las fuentes descargadas, documentadas y verificadas, y saber exactamente qué contienen.

**Tareas**

1. Para cada fuente de `02_datos_y_variables.md`, sección 2: localizar la edición más reciente en la web oficial, descargar los microdatos o tablas, el diseño de registro, la metodología y el cuestionario.
2. Registrar cada fichero en `MANIFEST.yaml` (URL, fecha, edición, SHA-256, condiciones de uso).
3. Las que no se puedan descargar automáticamente van a `MANUAL_DOWNLOADS.md`.
4. **Informe de inventario** por fuente: universo, tamaño de muestra, unidad (persona u hogar), variable de peso, fecha de referencia o de campo, **nivel geográfico real disponible**, variables presentes del diccionario y su codificación original.
5. **Verificaciones críticas** (registrar el resultado en `DECISIONS.md`):
   - Nivel geográfico de los microdatos del Censo 2021 y del Censo Anual (¿CCAA?, ¿provincia?, ¿tamaño de municipio?).
   - Cobertura de la población en establecimientos colectivos (residencias de mayores, etc.) en la muestra de hogares del Censo 2021.
   - Universo de edad de la TIC-H en la última edición.
   - Si la ronda 12 de la ESS está publicada.
   - Edición más reciente con microdatos de la encuesta de salud.
   - Fuentes electorales: resultados oficiales de las generales de 2023, las europeas de 2024 y las últimas autonómicas de cada comunidad, al nivel más fino disponible; censo electoral por territorio; estudios preelectorales y postelectorales del CIS disponibles y su representatividad territorial.
   - Qué variables políticas y de valores (sección 3.5 de `02`) aparecen en cada barómetro y con qué codificación, porque cambian entre estudios.
6. **Matriz de cobertura:** filas = variables del diccionario; columnas = fuentes; celdas = variable original o «no disponible».

**Entregables:** `data/raw/` completo, `MANIFEST.yaml`, `reports/fase_01.md` con el inventario y la matriz de cobertura.

**Puerta F1**

- [ ] G1.1 Todas las fuentes P0 descargadas y con hash verificado.
- [ ] G1.2 Cada fichero tiene su diseño de registro o documentación en `data/raw/`.
- [ ] G1.3 La matriz de cobertura no tiene ninguna variable P0 sin fuente.
- [ ] G1.4 El número de registros leídos de cada fichero coincide con el que declara la documentación oficial.
- [ ] G1.5 Las 7 verificaciones críticas están resueltas y registradas.
- [ ] G1.6 **Revisión humana:** se aprueba el inventario y las decisiones derivadas (por ejemplo, qué hacer si no hay provincia en los microdatos).

---

## F2 · Comprensión y armonización

**Objetivo:** convertir cada fuente a variables y códigos comunes sin perder ni alterar información.

**Tareas**

1. Escribir `configs/variables.yaml` con todas las variables P0, P1 y P2: categorías, tipo y, para cada fuente, variable original y tabla de recodificación.
2. Implementar lectores por fuente (ancho fijo, CSV, SPSS…) que apliquen el diseño de registro oficial.
3. Implementar la armonización: recodificación, valores especiales (NS, NC, NP), universo y pesos.
4. **Reproducir cifras oficiales publicadas** con los microdatos armonizados, para comprobar que la lectura es correcta. Por ejemplo, la distribución por sexo y edad del Censo 2021 frente a sus tablas publicadas, o la tasa de paro de la EPA del trimestre frente a la nota de prensa del INE.
5. Escribir `data/interim/<fuente>.parquet`.
6. Escribir `configs/partidos.yaml`: cada candidatura de cada elección de referencia, su código en los microdatos del CIS y su familia estable. Documentar las coaliciones y los cambios de nombre.
7. Escribir `configs/elecciones.yaml` y cargar los resultados oficiales con su censo electoral, CERA aparte.

**Entregables:** `variables.yaml`, `partidos.yaml`, `elecciones.yaml`, lectores, ficheros armonizados, `reports/fase_02.md` con las cifras reproducidas.

**Puerta F2**

- [ ] G2.1 Cada variable armonizada solo contiene valores de su dominio declarado (0 valores fuera de dominio).
- [ ] G2.2 Ningún código especial (NS, NC, NP) ha quedado como valor numérico de una escala.
- [ ] G2.3 Los totales ponderados se conservan antes y después de armonizar (diferencia < 0,01 %).
- [ ] G2.4 Se reproducen al menos 3 cifras oficiales publicadas por cada fuente P0 y P1 dentro de la tolerancia de redondeo de la publicación.
- [ ] G2.5 Tests unitarios por cada tabla de recodificación.
- [ ] G2.6 Los resultados electorales cargados reproducen los totales oficiales nacionales y provinciales (votos por candidatura, abstención, blancos y nulos) sin diferencias.
- [ ] G2.7 Cada código de partido de cada estudio del CIS usado tiene correspondencia en `partidos.yaml` (0 códigos sin asignar).
- [ ] G2.8 **Revisión humana:** muestra de 20 registros por fuente comparados a mano con el fichero original y su diseño de registro.

---

## F3 · Objetivos de calibración por territorio

**Objetivo:** tener, para cualquier territorio, las cifras oficiales que la población debe reproducir, separadas en **calibradas** y **reservadas para validar**.

**Tareas**

1. Construir objetivos desde la capa A (Padrón, Censo Anual, tablas del Censo 2021, Atlas de renta) para España, CCAA, provincias y municipios.
2. Definir en `targets.yaml` qué cruces se usan para calibrar y cuáles se reservan. Propuesta inicial:

   | Uso | Objetivos |
   | --- | --- |
   | Calibrar (persona) | edad_5 × sexo; nacionalidad_grupo; nivel_estudios (agregado) × edad_4; relacion_actividad × sexo; grado_urbanizacion o tamano_municipio |
   | Calibrar (hogar) | tipo_hogar; tamano_hogar |
   | Reservar para validar | estudios_3 × sexo × edad_4; relacion_actividad × edad_4; tipo_hogar × edad_4 de la persona de referencia; nacionalidad_top; estado_civil × edad_4; distribuciones provinciales cuando se calibra por CCAA |

3. Implementar la **agregación de territorios definidos por lista de municipios** (sumar objetivos municipales disponibles; documentar los que solo existen a nivel superior).
4. Resolver incoherencias entre fuentes (por ejemplo, Padrón frente a Censo Anual) con la regla de prioridad de `02_datos_y_variables.md` y registrar cada caso.
5. Construir los **objetivos electorales** por territorio para F8B: distribución de voto por familia, blanco, nulo y abstención sobre el censo electoral residente, para cada elección de referencia. Reservar al menos una elección (por ejemplo, las europeas de 2024) solo para validar.

**Entregables:** `data/processed/targets/`, `targets.yaml`, `reports/fase_03.md`.

**Puerta F3**

- [ ] G3.1 Para cada territorio, la suma de las marginales coincide con la población total oficial (diferencia < 0,1 %).
- [ ] G3.2 Las marginales de distintos cruces son coherentes entre sí (por ejemplo, el total por sexo es igual en edad × sexo y en actividad × sexo, salvo redondeos documentados).
- [ ] G3.3 La suma de los objetivos de las 19 comunidades reproduce el objetivo nacional.
- [ ] G3.4 Ninguna variable reservada para validar aparece en la lista de calibración (test automático).
- [ ] G3.5 Cada objetivo registra su fuente, edición y fecha de referencia.
- [ ] G3.6 Los objetivos electorales de cada territorio suman el 100 % del censo electoral residente y son coherentes con la población con derecho a voto de los objetivos demográficos (diferencia documentada y < 5 %, que se explica por la diferencia entre censo electoral y padrón).

---

## F4 · Población nacional base

**Objetivo:** generar la población sintética de España, de tamaño N, con atributos P0 y hogares completos, que supere la validación.

**Tareas**

1. Preparar los donantes: hogares completos de los microdatos censales, con sus personas.
2. Implementar y comparar al menos dos métodos de calibración (`03_arquitectura.md`, sección 2.1) sobre los objetivos nacionales. Elegir uno con evidencia y registrarlo.
3. Implementar la integerización y el muestreo a tamaño N, con semilla.
4. Implementar el modo de sobremuestreo con pesos.
5. Generar poblaciones de 10.000, 50.000, 100.000, 500.000 y 1.000.000 de personas y 5 semillas por tamaño.
6. Ejecutar la validación de la población (`05_validacion.md`, sección 4) y una primera pasada de la auditoría de minorías (sección 6), para detectar problemas pronto.

**Entregables:** `src/sinpop/synth/`, poblaciones de prueba, `reports/fase_04.md` con:

- tabla de error por marginal y cruce, calibrados y reservados;
- **curva de error frente a tamaño** de la población;
- variabilidad entre semillas;
- diagnóstico de pesos (distribución, extremos, tamaño efectivo).

**Puerta F4**

- [ ] G4.1 Marginales calibradas dentro del umbral **ajustado al tamaño** (V-MARG).
- [ ] G4.2 Cruces reservados dentro de umbral (V-CRUCE).
- [ ] G4.3 0 violaciones de las reglas de coherencia duras (V-REGLAS).
- [ ] G4.4 Diagnóstico de pesos dentro de umbral (V-PESOS).
- [ ] G4.5 Variabilidad entre semillas dentro de lo esperado por el muestreo (V-SEMILLAS).
- [ ] G4.6 Reproducibilidad: misma semilla, mismo hash (V-REPRO).
- [ ] G4.7 Modo de sobremuestreo: las estimaciones ponderadas coinciden con las del modo representativo dentro del error de muestreo.
- [ ] G4.8 **Revisión humana** del informe.

---

## F5 · Generador territorial

**Objetivo:** generar automáticamente la población de cualquier territorio, del tamaño que se pida, construida y calibrada para él.

**Tareas**

1. Implementar `territories.yaml`: códigos de CCAA, provincias, agrupaciones por lista de municipios, y la **jerarquía de donantes** para territorios con pocos donantes.
2. Generalizar la síntesis de F4 para recibir territorio, objetivos y conjunto de donantes.
3. Añadir al informe de cada población: proporción de donantes locales, tamaño efectivo de donantes y nivel de confianza esperado del territorio.
4. Generar y validar:
   - las 19 comunidades y ciudades autónomas;
   - al menos 10 provincias de perfiles distintos (por ejemplo, Madrid, Barcelona, Soria, Teruel, Almería, Las Palmas, Gipuzkoa, Ourense, Ceuta, Melilla);
   - al menos 2 agrupaciones por lista de municipios (una urbana y una rural).
5. **Prueba de coherencia entre niveles:** combinar las 19 comunidades con sus pesos poblacionales y comparar con la nacional.
6. **Prueba de territorio reservado:** calibrar una comunidad solo con sus objetivos demográficos y comprobar contra objetivos socioeconómicos reservados de esa comunidad.

**Entregables:** generador territorial, `reports/fase_05.md` con una tabla resumen por territorio y un anexo por territorio.

**Puerta F5**

- [ ] G5.1 Todos los territorios de la lista superan V-MARG y V-REGLAS.
- [ ] G5.2 Los cruces reservados por CCAA superan V-CRUCE (umbral territorial).
- [ ] G5.3 La agregación de las 19 comunidades reproduce la nacional dentro de umbral (V-COHERENCIA).
- [ ] G5.4 Cada territorio con donantes no locales informa del porcentaje y supera el tamaño efectivo mínimo de donantes (V-DONANTES).
- [ ] G5.5 Ceuta, Melilla y al menos dos provincias de menos de 150.000 habitantes se generan sin errores y con su confianza declarada.
- [ ] G5.6 **Revisión humana** del informe.

---

## F6 · Enriquecimiento

**Objetivo:** añadir las variables P1 y P2 que no están en los donantes censales (renta, privación, salud, discapacidad, uso digital, empleo detallado, consumo) sin romper la estructura de la población.

**Tareas**

1. Para cada fuente de enriquecimiento, definir las variables llave comunes y los bloques de variables que se heredan juntos.
2. Implementar el emparejamiento (`03_arquitectura.md`, sección 2.3) y, opcionalmente, la imputación múltiple.
3. Tratar los universos no cubiertos (por ejemplo, mayores de 74 en TIC-H) con un método documentado y marcado en `__calidad`.
4. Calibrar la renta del hogar al Atlas de renta en territorios donde sea posible.
5. Validar con la sección 5 de `05_validacion.md`.

**Entregables:** `src/sinpop/enrich/`, poblaciones enriquecidas, `reports/fase_06.md`.

**Puerta F6**

- [ ] G6.1 Las distribuciones de cada variable enriquecida, por CCAA y por tramo de edad, reproducen las de su encuesta de origen (V-ENRIQ-MARG).
- [ ] G6.2 Las relaciones entre variables enriquecidas y variables llave se conservan (V-ENRIQ-ASOC).
- [ ] G6.3 Las relaciones internas de cada bloque heredado se conservan (V-ENRIQ-BLOQUE).
- [ ] G6.4 Validación con variable llave reservada: se empareja sin una variable llave y se comprueba que se recupera su asociación (V-ENRIQ-HOLDOUT).
- [ ] G6.5 Las variables enriquecidas no alteran las variables P0 (test de igualdad).
- [ ] G6.6 La renta media por territorio queda dentro de umbral respecto al Atlas de renta donde se calibró, y se informa el error donde no.

---

## F7 · Auditoría de sesgos y minorías

**Objetivo:** demostrar que la población no introduce sesgos, que las minorías están bien representadas y que la diversidad dentro de los grupos es real. Detalle en `06_sesgos_y_minorias.md`.

**Tareas**

1. Completar `watchlist.yaml` con los grupos vigilados.
2. Ejecutar `sinpop audit` sobre la población nacional y sobre todos los territorios de F5.
3. Analizar los fallos, corregir en la fase correspondiente (F4, F5 o F6) y repetir.
4. Redactar la **sección de limitaciones**: grupos que no se pueden representar bien y por qué.

**Entregables:** `reports/fase_07.md` con la auditoría completa, la sección de limitaciones y la ficha de datos de la población (`07_plantillas.md`).

**Puerta F7**

- [ ] G7.1 Todos los grupos de la lista de vigilancia dentro de su rango de representación (V-MINORIAS).
- [ ] G7.2 Diversidad dentro de grupos dentro de umbral (V-DIVERSIDAD).
- [ ] G7.3 Concentración de donantes por grupo dentro de umbral (V-CONCENTRACION).
- [ ] G7.4 Perfil interno de cada grupo vigilado dentro de umbral, donde haya referencia oficial (V-MINORIAS-PERFIL).
- [ ] G7.5 No hay combinaciones de atributos sospechosas sin explicar (V-RAREZA).
- [ ] G7.6 La sección de limitaciones está escrita y cubre al menos los grupos no observables de `06_sesgos_y_minorias.md`.
- [ ] G7.7 **Revisión humana:** aprobación expresa de la población antes de iniciar la capa de opinión.

---

## F8A · Capa de opinión y valores

**Objetivo:** asignar a cada persona rasgos de actitud y valores basados en encuestas reales, con su variabilidad dentro de los grupos.

**Tareas**

1. Seleccionar estudios del CIS (y la ESS) anteriores a la fecha de corte, sobre los temas del proyecto.
2. Armonizar en formato largo (pregunta, opciones, respuesta, perfil, peso, fecha de campo). Construir el **banco de preguntas** con enunciado, opciones, escala y resultados.
3. Asignar las variables observadas de valores (religiosidad, identidad territorial, lengua, clase subjetiva, medios) por modelo condicionado al perfil y al territorio.
4. Estimar el modelo de rasgos latentes y el modelo multinivel (`03_arquitectura.md`, sección 2.4).
5. Asignar rasgos a la población por extracción condicionada.
6. Guardar en `data/eval/` los estudios posteriores a la fecha de corte (ventanas de validación y evaluación).

**Entregables:** `src/sinpop/opinion/`, `opinion.parquet`, banco de preguntas, `reports/fase_08a.md`.

**Puerta F8A**

- [ ] G8A.1 Ajuste del modelo latente dentro de umbral (V-LATENTE).
- [ ] G8A.2 Validación cruzada por pregunta: prediciendo respuestas a preguntas del CIS no usadas en el ajuste, el error es menor que el de la distribución histórica ingenua (V-OPINION-CV).
- [ ] G8A.3 Varianza de los rasgos dentro de los grupos comparable a la real (V-DIVERSIDAD aplicada a rasgos).
- [ ] G8A.4 Distribución de las variables de valores por CCAA y edad frente al CIS (V-ENRIQ-MARG aplicado a valores).
- [ ] G8A.5 Las respuestas simuladas por CCAA se comparan con el Barómetro Sanitario por comunidad, en preguntas anteriores al corte, y se informa el error.
- [ ] G8A.6 `test_no_leakage.py` pasa.
- [ ] G8A.7 **Revisión humana** del informe.

---

## F8B · Capa política

**Objetivo:** asignar a cada persona un perfil político realista (comportamiento electoral pasado, ideología, identidad, implicación y confianza), anclado en resultados electorales oficiales y coherente con su perfil y sus valores.

**Requisito previo:** F8A superada. Los valores (religiosidad, identidad territorial, clase subjetiva) se usan como predictores del perfil político.

**Tareas**

1. Calcular el derecho a voto de cada persona para cada elección de referencia.
2. Entrenar el modelo de recuerdo de voto con los estudios del CIS (`03_arquitectura.md`, sección 2.5), usando como contexto los resultados reales del territorio.
3. Asignar el recuerdo de voto de generales y calibrarlo a los resultados oficiales por provincia (o CCAA), abstención incluida.
4. Asignar el recuerdo de autonómicas y europeas condicionado al de generales.
5. Asignar ideología, eje territorial, cercanía a partido, interés, participación, confianza institucional y satisfacción con la democracia, condicionados al perfil, los valores y el recuerdo de voto.
6. Estimar los rasgos políticos latentes.
7. Comprobar que el perfil político no altera la población base ni la capa de opinión (solo se añade).
8. Ejecutar las pruebas de sesgo político de `06_sesgos_y_minorias.md`, sección 6.

**Entregables:** `src/sinpop/politics/`, `politics.parquet`, `reports/fase_08b.md`.

**Puerta F8B**

- [ ] G8B.1 Recuerdo de voto de generales por territorio frente a resultados oficiales, abstención incluida (V-POL-RECUERDO).
- [ ] G8B.2 Elección reservada (por ejemplo, europeas de 2024) frente a resultados oficiales por CCAA, sin haberla usado para calibrar (V-POL-RESERVADA).
- [ ] G8B.3 Perfil de cada electorado (edad, sexo, estudios, tamaño de municipio dentro de los votantes de cada familia) frente a los postelectorales del CIS (V-POL-PERFIL).
- [ ] G8B.4 Coherencia entre recuerdo de voto e ideología: la distribución de la autoubicación dentro de cada electorado reproduce la del CIS, incluida su dispersión (V-POL-COHERENCIA).
- [ ] G8B.5 Voto dual: la matriz de transferencia entre generales y autonómicas reproduce la del CIS en las comunidades donde hay datos (V-POL-TRANSFERENCIA).
- [ ] G8B.6 Ninguna variable política aparece en la población base (test automático).
- [ ] G8B.7 Pruebas de sesgo político superadas (V-POL-SESGO).
- [ ] G8B.8 Ninguna persona sin derecho a voto en una elección tiene recuerdo de voto de esa elección (test automático).
- [ ] G8B.9 **Revisión humana** del informe.

---

## F8C · Dimensión temporal

**Objetivo:** describir cómo han evolucionado las opiniones de cada tipo de persona y dejar preparado un banco de efectos de eventos.

**Tareas**

1. Añadir efectos de periodo a los modelos de F8A y F8B (`03_arquitectura.md`, sección 2.6).
2. Generar `trajectories.parquet` para un periodo configurable (por ejemplo, de enero de 2023 a junio de 2026).
3. Completar `configs/eventos.yaml` con eventos relevantes del periodo, con fecha y fuente.
4. Estimar el efecto de cada evento sobre los indicadores disponibles, por grupo, comparando barómetros anteriores y posteriores.

**Entregables:** `src/sinpop/temporal/`, `trajectories.parquet`, banco de efectos de eventos, `reports/fase_08c.md`.

**Puerta F8C**

- [ ] G8C.1 *Backtest* temporal: entrenando hasta el mes t, la predicción de los indicadores del mes t+1 a t+3 mejora a la de repetir el último valor observado (V-TEMPORAL).
- [ ] G8C.2 Las series agregadas de la población reproducen las series publicadas del CIS en el periodo de construcción (V-TEMPORAL-SERIES).
- [ ] G8C.3 Cada evento del banco tiene fecha, fuente y efecto estimado con su incertidumbre.

---

## F9 · Capa de predicción con IA

**Objetivo:** ante una pregunta cerrada nueva, devolver la distribución de respuestas en total y por subgrupos.

**Tareas**

1. Añadir *embeddings* al banco de preguntas de F8A para recuperar las parecidas.
2. Implementar la operación de modelos de lenguaje (`03_arquitectura.md`, sección 2.9): configuración, prompts versionados, caché, registro y presupuesto.
3. Implementar la traducción de pregunta a parámetros con el LLM (salida estructurada y validada).
4. Implementar el estimador de simulación sobre una submuestra estratificada.
5. Implementar la combinación de estimadores y el cálculo de intervalos de incertidumbre.
6. Implementar el modo **evento** (antes, después y cambio) usando el banco de efectos de F8C.
7. Implementar los baselines: B0 (distribución histórica de preguntas parecidas), B1 (modelo clásico entrenado en el CIS) y B2 (LLM con perfil demográfico sin anclaje).
8. Medir en la ventana de validación, también por territorio y con preguntas políticas.

**Entregables:** `src/sinpop/predict/`, `prompts/`, `reports/fase_09.md`.

**Puerta F9**

- [ ] G9.1 Salida en el formato de `03_arquitectura.md`, sección 2.8, validada por esquema (V-FORMATO).
- [ ] G9.2 Resultados de los tres baselines y del sistema en la ventana de validación, en total, por subgrupo y por CCAA.
- [ ] G9.3 Coste por pregunta (llamadas, tokens, euros, tiempo) informado y dentro del presupuesto.
- [ ] G9.4 Prueba de reformulación neutra: cambios de redacción sin carga no alteran la distribución más allá de umbral (V-REFORMULACION).
- [ ] G9.5 Cobertura de los intervalos: en la ventana de validación, el valor real cae dentro del intervalo del 80 % en torno al 80 % de los casos (V-COBERTURA).
- [ ] G9.6 Modo evento probado con al menos 3 eventos pasados con datos antes y después: se acierta la dirección del cambio y se informa el error de magnitud (V-EVENTO).
- [ ] G9.7 Pruebas de estereotipos de la capa de IA superadas (`06_sesgos_y_minorias.md`, sección 5).

---

## F10 · Modelo de confianza

**Objetivo:** que cada predicción indique cuánto fiarse de ella, y que esa confianza sea cierta.

**Tareas**

1. *Backtest*: ocultar cada pregunta histórica, predecirla con el resto y medir el error (solo componente estadístico, para evitar la contaminación del LLM).
2. Entrenar el modelo de confianza con las señales de `03_arquitectura.md`, sección 2.7.
3. Calibrar en la ventana de validación.

**Entregables:** `src/sinpop/confidence/`, `reports/fase_10.md` con diagrama de calibración.

**Puerta F10**

- [ ] G10.1 Correlación de rangos entre confianza y error real dentro de umbral (V-CONF-CORR).
- [ ] G10.2 Error de calibración dentro de umbral (V-CONF-ECE).
- [ ] G10.3 La confianza disminuye con el tamaño del territorio y del subgrupo, como se espera.

---

## F11 · Evaluación final sin contaminación

**Objetivo:** medir el sistema completo una sola vez, con preguntas reales posteriores a la fecha de corte, con el código congelado.

**Tareas**

1. Congelar el código (etiqueta git).
2. Ejecutar sobre la ventana de evaluación de `data/eval/`, por primera vez.
3. Informar de los resultados frente a baselines, por subgrupo y por territorio, con la confianza declarada.
4. Informar por separado de las preguntas políticas y de las de vida cotidiana.
5. Si hay una elección real posterior a la congelación del código, registrar antes de ella una estimación de participación y de distribución por familias, con fecha, y compararla con el resultado. Es la prueba más limpia posible: ni el modelo ni el equipo conocen el resultado.
6. Análisis de errores: dónde falla más, hipótesis y al menos una hipótesis comprobada.

**Puerta F11**

- [ ] G11.1 Evaluación ejecutada desde la etiqueta congelada, sin cambios.
- [ ] G11.2 Informe completo con baselines, subgrupos, territorios y calibración de la confianza.
- [ ] G11.3 **Revisión humana.**

---

## F12 · Empaquetado y documentación final

**Objetivo:** dejar el sistema usable, mantenible y honesto sobre sus límites.

**Tareas**

1. Ficha de datos y ficha de modelo finales.
2. Guía de uso con ejemplos de la CLI.
3. Guía de actualización de fuentes (qué cambiar y qué revalidar cuando sale una nueva edición), incluida la **actualización tras unas elecciones**: nuevos resultados, nuevas candidaturas en `partidos.yaml` y recalibración del recuerdo de voto.
4. Sección de **límites de uso** (`06_sesgos_y_minorias.md`, sección 7).
5. Guía de **actualización mensual**: incorporar un barómetro nuevo del CIS, revalidar la capa de opinión y mover la fecha de corte si cambian los modelos.

**Puerta F12**

- [ ] G12.1 Una persona ajena al proyecto genera y valida una población siguiendo solo la guía.
- [ ] G12.2 La guía de actualización se prueba sustituyendo una fuente por una edición distinta.
- [ ] G12.3 Lista de comprobación de `08_uso_y_licencias.md` completada.
- [ ] G12.4 **Revisión humana** final.

---

## Riesgos principales y plan alternativo

| Riesgo | Cuándo se detecta | Plan alternativo |
| --- | --- | --- |
| Los microdatos del Censo no traen provincia | F1 | Donantes por CCAA y tamaño de municipio; calibración a objetivos provinciales del Padrón y del Censo Anual; confianza provincial declarada como menor |
| La muestra de hogares del Censo no cubre establecimientos colectivos | F1 | Módulo aparte para residencias con las tablas del Censo 2021 (recuentos por edad, sexo y territorio) y atributos modelados; si no es viable, declararlo como limitación |
| La calibración no converge o produce pesos extremos en territorios pequeños | F4–F5 | Acotar pesos (GREG acotado), reducir el número de objetivos calibrados al nivel más fiable, ampliar donantes jerárquicamente |
| Pocos casos en el CIS para un grupo o una familia de partidos | F8A–F8B | Modelos multinivel que tomen prestada información de grupos parecidos; agrupar familias; apilar más estudios; declarar la menor confianza |
| Las variables cambian de codificación entre barómetros | F2 | Tabla de correspondencia por estudio en `variables.yaml`; excluir los estudios que no se puedan armonizar con seguridad |
| El LLM no mejora a los baselines estadísticos | F9 | Es un resultado válido: se documenta, se usa el estimador estadístico como principal y el LLM solo para explicar y para preguntas sin análogos |
| Fuga de datos de evaluación | Cualquiera | `test_no_leakage.py`; congelación del código antes de F11 |
