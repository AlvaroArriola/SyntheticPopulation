# Validación: previsto frente a real

**Fecha:** 2026-10-23 · **Decisiones:** D-089, D-090, D-091
**Comando:** `SINPOP_PAQUETE=dist/paquete python -m sinpop.evaluate.bateria` (unos 15 minutos). Después, `sinpop serve --paquete dist/paquete` y abrir `/validacion.html`.

Preguntas reales de los barómetros del CIS posteriores al corte de los datos (junio de 2026). El sistema las predijo sin ver esas encuestas. «Error» es la TVD × 100: los puntos de respuesta que habría que mover para que lo previsto coincidiera con lo real.

## Por estudio

| Estudio | Mes | Uso | Encuestados | Preguntas | Error medio | Mediana | < 10 puntos | Respuestas dentro del margen |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3571 | 2026-07 | validación (F9-F10) | 4020 | 79 | 5,4 | 3,2 | 85 % | 58 % |
| 3577 | 2026-09 | validación (F9-F10) | 4042 | 42 | 13,4 | 5,4 | 64 % | 43 % |
| 3582 | 2026-10 | evaluación final (F11) | 5024 | 90 | 15,8 | 8,5 | 52 % | 25 % |
| **Todas** | | | | 211 | **11,4** | 5,3 | 67 % | 39 % |
| **Sin las escalas 1-10 dudosas (D-089)** | | | | 156 | **7,9** | 4,4 | 75 % | 48 % |

**«Dentro del margen»** compara cada respuesta prevista con el margen de muestreo del 95 % de la encuesta real. Ese margen solo recoge el error de la encuesta, no el del modelo, así que es una prueba exigente.

## Por subgrupos (sin las escalas dudosas)

| Variable | Grupo × pregunta | Error medio | Ruido de muestreo esperado | Exceso sobre el ruido |
| --- | --- | --- | --- | --- |
| Situación laboral | 357 | 5,1 | 2,3 | 2,8 |
| Religiosidad | 714 | 5,5 | 3,1 | 2,5 |
| Tamaño del municipio | 595 | 5,6 | 2,8 | 2,8 |
| Clase social | 714 | 6,0 | 3,1 | 2,9 |
| Sexo | 312 | 8,2 | 1,6 | 6,7 |
| Estudios | 276 | 8,3 | 1,9 | 6,4 |
| Edad | 624 | 8,7 | 2,2 | 6,5 |
| Comunidad | 2640 | 10,7 | 4,9 | 5,9 |

- **Ruido de muestreo esperado:** lo que se equivocaría una predicción perfecta solo porque cada grupo del CIS tiene pocos cientos de encuestados. Por opción vale E|N(0, sd)| = sd·√(2/π), con la sd sacada del margen del 95 % del grupo.
- **Lectura:** el exceso sobre el ruido (2,5-6,7 puntos) es del orden del error del total en esas mismas preguntas (7,9). Los subgrupos arrastran el desvío del total, pero no añaden un fallo propio.
- **Situación laboral, tamaño del municipio, religiosidad y clase social** salen mejor porque solo las estima el modelo estadístico. El LLM anclado, usado en las preguntas sin precedentes, solo estima por edad, sexo, estudios y comunidad. Además, esas preguntas son las más difíciles.

## Importancia de las variables (D-090)

En las 156 preguntas sin escalas dudosas:
- la variable que más separa las respuestas en la encuesta real es también la primera prevista en el 58 %;
- está entre las tres primeras previstas en el 90 %;
- la fuerza prevista y la real difieren de media en 0,024 (en una escala de 0 a 1).

## En qué se basa

- **Lo real:** microdatos de los estudios 3571, 3577 y 3582 del CIS, descargados de su web oficial (`data/eval/MANIFEST.yaml`, con URL y huella de cada fichero). Se usan las respuestas de los españoles de 18 años o más, ponderadas con la variable de ponderación del CIS.
- **Lo previsto:** el sistema congelado de F11 (paquete portable), con el banco de preguntas del CIS anterior a cada mes. Cada pregunta de la interfaz enumera las preguntas del banco en que se apoyó y sus fuentes.
- **Pendiente:** la codificación de las escalas 1-10 de valoración (D-089).
