# Población sintética de España

Proyecto para construir una **población sintética de las personas adultas residentes en España**, fiel a la realidad, de **tamaño variable** y generable **para toda España o para cualquier territorio** (comunidad autónoma, provincia o agrupación de municipios).

Sobre esa población se añaden después una capa de opinión y valores, una **capa política** anclada en resultados electorales reales, una **dimensión temporal** y una capa de predicción. Juntas permiten estimar cómo reaccionaría la sociedad ante una pregunta o un evento, y con qué confianza.

## Objetivo principal

> Construir una población sintética **lo más fehaciente posible a la realidad**, anclada en datos oficiales, que **no caiga en sesgos ni generalizaciones** y en la que **las minorías estén correctamente representadas**, tanto a escala nacional como territorial.

La calidad de todo lo demás depende de esto. Una población mal construida produce predicciones sesgadas aunque el modelo de IA sea excelente. Por eso:

- **Los datos y las variables son la decisión más importante del proyecto.** Cada variable tiene una fuente oficial, una justificación y una validación.
- **Nada se da por bueno sin medirlo.** Cada fase termina con una validación automática y un informe. Si no se supera, no se avanza.
- **La diversidad dentro de cada grupo es un requisito, no un adorno.** Dos personas con la misma edad, sexo y municipio deben poder ser distintas, igual que en la realidad.

## Qué produce el sistema

| Producto | Descripción |
| --- | --- |
| Población nacional | Personas y hogares sintéticos de toda España, del tamaño que se pida (por ejemplo, de 10.000 a 1.000.000 de personas) |
| Población territorial | La población de cualquier territorio, **construida y calibrada para ese territorio**, no filtrada de la nacional |
| Informe de validación | Para cada población generada: cuánto se parece a la realidad, por variable, por cruce y por grupo minoritario |
| Ficha de datos | Qué variables tiene cada persona, de qué fuente sale cada una y con qué limitaciones |
| Capa de opinión y valores *(F8A)* | Rasgos de actitud y valores (religiosidad, identidad territorial, clase subjetiva…) asignados a cada persona a partir de encuestas reales (CIS, ESS) |
| Capa política *(F8B)* | Recuerdo de voto calibrado con resultados electorales oficiales, ideología, identidad, implicación y confianza institucional |
| Dimensión temporal *(F8C)* | Evolución de las opiniones de cada tipo de persona y banco de efectos de eventos pasados |
| Capa de predicción *(F9–F10)* | Distribución de respuestas ante una pregunta o un evento nuevo, en total y por subgrupos, con intervalo y confianza |

## Documentación

| Documento | Contenido |
| --- | --- |
| [`CLAUDE.md`](CLAUDE.md) | Reglas de trabajo para el agente de código |
| [`DECISIONS.md`](DECISIONS.md) | Registro de decisiones, con las de partida ya incluidas |
| [`docs/01_vision_y_requisitos.md`](docs/01_vision_y_requisitos.md) | Problema, objetivo, alcance, requisitos y definición de éxito |
| [`docs/02_datos_y_variables.md`](docs/02_datos_y_variables.md) | Fuentes, diccionario de variables, armonización, geografía y dimensión temporal. **Es el documento más importante** |
| [`docs/03_arquitectura.md`](docs/03_arquitectura.md) | Métodos, estructura del repositorio, formatos de entrada y salida, CLI y operación de los modelos de lenguaje |
| [`docs/04_fases.md`](docs/04_fases.md) | Fases del proyecto con tareas, entregables y puertas de salida, y riesgos principales |
| [`docs/05_validacion.md`](docs/05_validacion.md) | Métricas, umbrales y pruebas de cada fase |
| [`docs/06_sesgos_y_minorias.md`](docs/06_sesgos_y_minorias.md) | Cómo evitar sesgos y garantizar que las minorías estén bien representadas |
| [`docs/07_plantillas.md`](docs/07_plantillas.md) | Plantillas de decisiones, informes de fase, ficha de datos y configuraciones |
| [`docs/08_uso_y_licencias.md`](docs/08_uso_y_licencias.md) | Condiciones de uso de las fuentes y principios de trabajo con los datos |

## Fases

| Bloque | Fases |
| --- | --- |
| **Núcleo: la población** | F0 Preparación · F1 Datos · F2 Armonización · F3 Objetivos de calibración · F4 Población nacional · F5 Generador territorial · F6 Enriquecimiento · F7 Auditoría de sesgos y minorías |
| **Extensión: opinión, política y predicción** | F8A Opinión y valores · F8B Política · F8C Dimensión temporal · F9 Predicción · F10 Confianza · F11 Evaluación final · F12 Empaquetado |

El núcleo es la prioridad absoluta. Las fases de extensión no empiezan hasta que la población haya superado la auditoría de F7. Las capas de opinión y política se guardan en ficheros separados de la población base, para que su calidad no dependa de ellas.

## Cómo arrancar con el agente de código

1. Copiar esta carpeta en la raíz de un repositorio vacío.
2. Abrir el agente en esa carpeta y darle esta primera instrucción:

   > Lee `CLAUDE.md`, `DECISIONS.md` y todos los documentos de `docs/` en orden. Después resume en un máximo de 15 líneas el objetivo, las fases y las reglas que vas a seguir, señala cualquier contradicción o duda que encuentres en la documentación y empieza la fase F0. No pases a F1 hasta que la puerta de F0 esté superada.

3. En cada puerta marcada como «revisión humana», el agente se detiene y entrega su informe en `reports/`. Revisarlo, responder a sus preguntas y autorizar la fase siguiente.

## Glosario

- **Microdatos:** ficheros con una fila por persona u hogar, anonimizados, publicados por organismos oficiales.
- **Marginal:** distribución de una variable (por ejemplo, la edad). **Cruce:** distribución conjunta de dos o más variables (por ejemplo, edad × estudios).
- **Calibración:** ajustar los pesos de unas personas de partida para que, en conjunto, reproduzcan cifras oficiales conocidas.
- **Donante:** hogar o persona real de los microdatos que sirve de base para generar personas sintéticas.
- **Emparejamiento estadístico (*statistical matching*):** unir información de dos fuentes distintas buscando personas con perfil parecido.
- **MRP:** regresión multinivel con postestratificación; técnica estándar para estimar opiniones por territorio con pocos datos locales.
- **Puerta de fase:** conjunto de comprobaciones que deben superarse para dar una fase por terminada.
- **Recuerdo de voto:** lo que una persona declara haber votado en una elección pasada. En las encuestas está sesgado; aquí se calibra con los resultados oficiales.
- **Familia de partidos:** agrupación estable de candidaturas que cambian de nombre o de coalición entre elecciones.
- **Pseudopanel:** seguimiento en el tiempo de tipos de persona (por cohorte y perfil) a partir de encuestas sucesivas a personas distintas.
- **TVD (distancia de variación total):** porcentaje de la población que habría que cambiar de categoría para que dos distribuciones coincidan. Es la métrica principal de validación.
