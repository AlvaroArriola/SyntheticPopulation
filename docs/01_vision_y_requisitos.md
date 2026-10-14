# 01 · Visión y requisitos

## 1. Problema

Saber cómo recibirá la sociedad una iniciativa, un producto, un cambio de precio o una campaña exige hoy encuestas o pilotos: semanas de trabajo y miles de euros por pregunta. Los modelos estadísticos clásicos son rápidos, pero solo aprenden de lo que ya ha pasado y no saben qué hacer con preguntas nuevas.

La alternativa es una **población sintética**: un conjunto de personas simuladas, basadas en datos reales, sobre las que se pueden plantear preguntas y obtener en minutos una estimación de la reacción de la sociedad.

Los sistemas de este tipo suelen fallar por la base, no por el modelo:

- **Poblaciones poco fieles:** reproducen bien los totales, pero mal las combinaciones (por ejemplo, la proporción correcta de universitarios, mal repartida entre jóvenes y mayores).
- **Homogeneidad:** todas las personas de un mismo grupo acaban pareciéndose, cuando en la realidad hay mucha variedad.
- **Estereotipos:** se asignan rasgos por tópico («mayor de pueblo» implica X) en lugar de por evidencia.
- **Minorías mal representadas:** grupos pequeños que desaparecen, se duplican a partir de muy pocos casos reales o se describen con datos de otros grupos.

Este proyecto pone el foco en resolver esos problemas.

## 2. Objetivo

Construir un sistema que genere **poblaciones sintéticas de adultos residentes en España**:

1. **Fehacientes:** reproducen la estructura real de la población (individual y de hogares) según las fuentes oficiales más recientes, en marginales, en cruces y en grupos minoritarios.
2. **De tamaño variable:** de unas miles a cientos de miles o millones de personas, con un comportamiento medido del error según el tamaño.
3. **Territoriales:** para toda España o para cualquier territorio, **construidas y calibradas para ese territorio** con sus cifras oficiales.
4. **Diversas sin estereotipos:** conservan la variabilidad dentro de cada grupo observada en los datos reales.
5. **Trazables y honestas:** cada atributo tiene fuente, cada población lleva su informe de validación y el sistema dice explícitamente qué no puede representar bien.

Sobre esa base (fases 8 a 12), el sistema:

- asignará a cada persona **actitudes, valores y un perfil político** (recuerdo de voto, ideología, identidad territorial, implicación y confianza institucional) anclados en encuestas reales y calibrados con resultados electorales oficiales;
- describirá cómo han evolucionado las opiniones de cada tipo de persona **en el tiempo**;
- estimará la distribución de respuestas ante una **pregunta o un evento**, en total y por subgrupos, con una estimación de su fiabilidad.

## 3. Alcance

### Dentro del alcance

- Población: personas de **18 años o más** residentes en España. Se generan también los hogares completos (incluidos los menores que conviven con ellos), porque la composición del hogar es un atributo clave de cada adulto. El universo de salida para preguntas es 18+.
- Territorios: España, las 17 comunidades autónomas y las 2 ciudades autónomas, las 52 provincias y agrupaciones definidas por el usuario (por ejemplo, «municipios rurales de Castilla y León» o «área metropolitana de Valencia»), siempre que haya datos oficiales para calibrar.
- Atributos sociodemográficos, socioeconómicos, de hogar, de vivienda, de uso digital y de salud (detalle en `02_datos_y_variables.md`).
- Capa de opinión y valores, capa política, dimensión temporal de las opiniones y capa de predicción (fases 8 a 12).
- Preguntas sobre vida cotidiana, valores, actitudes y política, incluidas preguntas de opinión política e intención de voto.

### Fuera del alcance (por ahora)

- Individuos identificables o reidentificación de personas reales.
- Proyecciones demográficas a futuro (la población describe el presente de referencia).
- Simulación de dinámicas demográficas en el tiempo (nacimientos, migraciones, envejecimiento). La evolución de las **opiniones** sí está dentro del alcance.

## 4. Requisitos funcionales

| ID | Requisito |
| --- | --- |
| RF-01 | Generar una población nacional de tamaño N configurable, con semilla |
| RF-02 | Generar la población de un territorio dado por código oficial (CCAA, provincia) o por una lista de municipios |
| RF-03 | Cada persona tiene un identificador, un hogar y todos los atributos del diccionario de variables |
| RF-04 | Cada población incluye un peso por persona. En modo representativo los pesos son iguales; en modo con sobremuestreo de minorías, los pesos corrigen el sobremuestreo |
| RF-05 | Modo de sobremuestreo configurable: garantizar un mínimo de personas de grupos concretos (por ejemplo, 85+ o nacionalidades minoritarias) sin sesgar las estimaciones agregadas |
| RF-06 | Cada población generada produce automáticamente su informe de validación |
| RF-07 | Cada población lleva una ficha de datos con fuentes, versiones, fecha de referencia y limitaciones |
| RF-08 | Consultar cualquier subgrupo definido por combinación de atributos |
| RF-09 *(F8A)* | Asignar a cada persona rasgos de actitud y valores derivados de encuestas reales |
| RF-10 *(F8B)* | Asignar a cada persona un perfil político (recuerdo de voto, ideología, identidad, implicación, confianza institucional), con el recuerdo de voto calibrado a resultados electorales oficiales por territorio |
| RF-11 *(F8C)* | Describir la evolución temporal de las opiniones por tipo de persona y fechar los rasgos |
| RF-12 *(F9)* | Dada una pregunta cerrada, devolver la distribución de respuestas en total y por subgrupos, con intervalo de incertidumbre |
| RF-13 *(F9)* | Dado un evento (descripción y fecha), estimar el cambio en la distribución de respuestas respecto a la situación previa |
| RF-14 *(F10)* | Acompañar cada predicción de una confianza calibrada |
| RF-15 | Registrar cada predicción (pregunta, versión de prompts y modelos, población, resultado) para poder auditarla |

## 5. Requisitos no funcionales

| ID | Requisito |
| --- | --- |
| RNF-01 | **Reproducibilidad:** misma configuración y semilla, mismos ficheros (hash idéntico) |
| RNF-02 | **Trazabilidad:** cada atributo de cada persona se puede rastrear hasta su fuente y su variable original |
| RNF-03 | **Rendimiento:** población nacional de 1.000.000 de personas en menos de 15 minutos en un portátil normal; población territorial de 50.000 en menos de 2 minutos (objetivo orientativo) |
| RNF-04 | **Formato abierto:** Parquet para datos, JSON para metadatos, Markdown para informes |
| RNF-05 | **Privacidad:** ningún microdato original sale del entorno local; al LLM solo llegan perfiles sintéticos o agregados |
| RNF-06 | **Mantenibilidad:** actualizar una fuente (por ejemplo, una nueva edición del Censo Anual o un nuevo barómetro del CIS) no exige reescribir código, solo configuración y revalidación |
| RNF-07 | **Uso de las fuentes:** uso no comercial, citando cada fuente según sus condiciones (`08_uso_y_licencias.md`) |
| RNF-08 | **Coste controlado:** cada predicción informa de su coste (llamadas al modelo, tokens, euros, tiempo) y existe un presupuesto configurable |

## 6. Definición de éxito

**La población está lista** cuando:

1. Supera todas las puertas de las fases F0 a F7 (`04_fases.md`).
2. Reproduce las distribuciones objetivo dentro de los umbrales de `05_validacion.md`, **incluidas las que no se usaron para construirla** (validación con datos reservados).
3. Ningún grupo minoritario de la lista de vigilancia (`06_sesgos_y_minorias.md`) está fuera de su rango de representación.
4. La variabilidad dentro de los grupos es comparable a la real.
5. La ficha de datos documenta con honestidad qué grupos no se pueden representar bien y por qué.

**El sistema completo está listo** cuando, además:

6. La capa política reproduce los resultados electorales oficiales por territorio, incluida una elección que no se usó para construirla.
7. En la evaluación final (F11), con preguntas reales posteriores a la fecha de corte, el sistema mejora a los baselines y su confianza declarada se corresponde con su acierto real.

## 7. Principios de diseño

1. **Personas reales como base.** Las personas sintéticas parten de registros reales anonimizados (donantes), no de atributos inventados por separado. Así se conservan las combinaciones que existen de verdad.
2. **Calibrar a la verdad oficial.** Las cifras de referencia son las estadísticas oficiales más recientes y de mayor cobertura (registros y censos antes que encuestas).
3. **Validar con lo que no se ha usado.** Una población que solo cuadra con las cifras con las que se calibró no demuestra nada. Siempre se reservan distribuciones para validar.
4. **Mejor un hueco declarado que un dato inventado.** Si un grupo no se puede representar con datos, se dice.
5. **La diversidad se mide.** La variabilidad dentro de cada grupo es una métrica más, con su umbral.
6. **La política se ancla en lo que pasó.** El perfil político de la población se calibra con resultados electorales reales, no solo con lo que la gente declara en encuestas.
7. **Lo volátil no es identidad.** Lo que cambia mes a mes (intención de voto, valoración de líderes) se predice como respuesta, no se fija como atributo de la persona.
