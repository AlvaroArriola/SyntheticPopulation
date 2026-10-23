# Validación: previsto frente a real

**Fecha:** 2026-10-23 · **Decisiones:** D-089, D-090, D-091
**Comando:** `SINPOP_PAQUETE=dist/paquete python -m sinpop.evaluate.bateria` (unos 15 minutos). Después, `sinpop serve --paquete dist/paquete` y abrir `/validacion.html`.

Preguntas reales de los barómetros del CIS posteriores al corte de los datos (junio de 2026). El sistema las predijo sin ver esas encuestas. «Error» es la TVD × 100: los puntos de respuesta que habría que mover para que lo previsto coincidiera con lo real.

**Escalas 1-10 corregidas (D-089).** Esta batería usa el sistema con las escalas de solo extremos etiquetados ya completadas en el banco. La corrección se hizo **después** de la evaluación final, así que el resultado oficial de F11 no cambia: 15,8 puntos en el barómetro de octubre, medido una sola vez con el código congelado (`f11-congelacion-2026-10-23`). El sistema corregido da 7,8 puntos en ese mismo barómetro.

## Por estudio

| Estudio | Mes | Uso | Encuestados | Preguntas | Error medio | Mediana | < 10 puntos | Respuestas dentro del margen |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3571 | 2026-07 | validación (F9-F10) | 4020 | 80 | 5,5 | 4,3 | 88 % | 67 % |
| 3577 | 2026-09 | validación (F9-F10) | 4042 | 42 | 10,9 | 4,8 | 71 % | 49 % |
| 3582 | 2026-10 | evaluación final (F11), sistema corregido | 5024 | 90 | 7,8 | 6,3 | 77 % | 53 % |
| **Todas** | | | | 212 | **7,5** | 5,4 | 80 % | 57 % |

- **Preguntas políticas** (intención y recuerdo de voto, valoración de líderes, ideología): unos 3 puntos de error en cada estudio (16 preguntas por estudio).
- **Dónde falla:** temas nuevos sin precedente en el banco, donde responde el LLM anclado: la visita del papa León XIV (julio, 17-28 puntos), los actores responsables de los incendios y el cruce de la frontera en Ceuta (septiembre, 33-59), y el conocimiento del desahucio de Maricarmen o de los decretos de vivienda (octubre, 22-48). Las preguntas de «conocimiento» de un hecho concreto son las más difíciles.
- **«Dentro del margen»** compara cada respuesta prevista con el margen de muestreo del 95 % de la encuesta real. Ese margen solo recoge el error de la encuesta, no el del modelo, así que es una prueba exigente.

## Por subgrupos

| Variable | Grupo × pregunta | Error medio | Ruido de muestreo esperado | Exceso sobre el ruido |
| --- | --- | --- | --- | --- |
| Situación laboral | 522 | 6,8 | 3,8 | 3,1 |
| Religiosidad | 1018 | 7,5 | 4,6 | 2,9 |
| Tamaño del municipio | 873 | 7,7 | 4,6 | 3,1 |
| Clase social | 1040 | 8,2 | 5,0 | 3,1 |
| Sexo | 424 | 8,2 | 2,4 | 5,8 |
| Estudios | 366 | 8,3 | 2,8 | 5,5 |
| Edad | 848 | 9,1 | 3,3 | 5,8 |
| Comunidad | 3442 | 12,0 | 6,7 | 5,4 |

- **Ruido de muestreo esperado:** lo que se equivocaría una predicción perfecta solo porque cada grupo del CIS tiene pocos cientos de encuestados. Por opción vale E|N(0, sd)| = sd·√(2/π), con la sd sacada del margen del 95 % del grupo.
- **Lectura:** el exceso sobre el ruido (2,9-5,8 puntos) es del orden del error del total en esas mismas preguntas (7,5). Los subgrupos arrastran el desvío del total, pero no añaden un fallo propio.
- **Situación laboral, tamaño del municipio, religiosidad y clase social** salen mejor porque solo las estima el modelo estadístico. El LLM anclado, usado en las preguntas sin precedentes, solo estima por edad, sexo, estudios y comunidad. Además, esas preguntas son las más difíciles.

## Importancia de las variables (D-090)

En las 212 preguntas:
- la variable que más separa las respuestas en la encuesta real es también la primera prevista en el 66 %;
- está entre las tres primeras previstas en el 92 %;
- la fuerza prevista y la real difieren de media en 0,023 (en una escala de 0 a 1).

## En qué se basa

- **Lo real:** microdatos de los estudios 3571, 3577 y 3582 del CIS, descargados de su web oficial (`data/eval/MANIFEST.yaml`, con URL y huella de cada fichero). Se usan las respuestas de los españoles de 18 años o más, ponderadas con la variable de ponderación del CIS.
- **Lo previsto:** el paquete portable con las escalas corregidas (D-089), con el banco de preguntas del CIS anterior a cada mes. Donde respondió el LLM anclado, se usa su salida en caché, sin llamadas nuevas. Cada pregunta de la interfaz enumera las preguntas del banco en que se apoyó y sus fuentes.
- **Separación de los datos de evaluación:** solo `sinpop.evaluate` lee `data/eval/`. Ningún resultado de esta batería se ha usado para ajustar el sistema. La corrección de D-089 viene del diseño de registro (datos de entrada), no de estos errores.
