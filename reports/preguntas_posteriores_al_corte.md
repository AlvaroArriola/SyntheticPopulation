# Preguntas del CIS posteriores al corte (junio de 2026)

Preguntas reales que el sistema no vio al construirse. Los estudios están en `data/eval/cis/` y solo los lee `src/sinpop/evaluate/` (regla 5). Aquí solo van los enunciados y las opciones, que son el cuestionario público; nunca respuestas individuales.

| Estudio | Mes | Uso | Preguntas |
| --- | --- | --- | --- |
| 3571 | julio de 2026 | validación (F9-F10) | 80 |
| 3577 | septiembre de 2026 | validación (F9-F10) | 42 |
| 3582 | octubre de 2026 | evaluación final (F11), una sola vez | se añade tras F11 |

**Columna «Error»:** TVD entre lo que predijo el sistema y lo que midió el CIS. 0 es perfecto; 0,10 equivale a desviarse 10 puntos en total. Va con el método que se usó:
- **análogas:** preguntas parecidas del banco;
- **LLM anclado:** preguntas sin precedentes.

«—» indica que la pregunta no se evaluó (sin análogas alineables o con menos casos de los necesarios).

**Duda abierta (D-089):** en las escalas de valoración de líderes y ministros (1-10), el estudio 3571 solo trae etiquetadas las opciones extremas («1 Muy mal / 10 Muy bien»), y el 3577 trae la escala completa.
- En 3571 la comparación se hace sobre dos categorías, y su error bajo no es fiable.
- En 3577 los errores de Sánchez (0,36), Feijóo (0,49) y Abascal (0,30) son anómalos.
- Hay que revisar la armonización de esas escalas antes de sacar conclusiones de ellas.

Generado con `python -m sinpop.evaluate.preguntas_posteriores [--final]` (consulta de solo lectura a través de `sinpop.evaluate.validacion`).

## Estudio 3571 · 2026-07 · validación (F9-F10) · 80 preguntas

| Pregunta | Opciones | Tipo | Error (TVD) |
| --- | --- | --- | --- |
| Conocimiento de la reciente visita el papa León XIV a España | Sí / No | vida cotidiana | 0.415 (análogas) |
| Valoración de la visita del papa León XIV a España | Muy positiva / Positiva / Ni positiva ni negativa / Negativa / Muy negativa | vida cotidiana | 0.168 (LLM anclado) |
| Efectos de la visita del papa León XIV en la imagen de España | La ha mejorado / La ha empeorado / Ni mejorado, ni empeorado / En algunos aspectos la ha mejorado y en otros la ha empeorado | vida cotidiana | 0.242 (LLM anclado) |
| Conocimiento de la opinión del papa León XIV sobre la inmigración | Sí / No | vida cotidiana | 0.206 (análogas) |
| Grado de acuerdo con las manifestaciones del papa León XIV sobre la inmigración | Muy de acuerdo / De acuerdo / Ni de acuerdo, ni en desacuerdo / En desacuerdo / Muy en desacuerdo | vida cotidiana | 0.061 (análogas) |
| Conocimiento de la opinión del papa León XIV sobre la polarización política | Sí / No | vida cotidiana | 0.373 (análogas) |
| Grado de acuerdo con las manifestaciones del papa León XIV sobre la polarización política | Muy de acuerdo / De acuerdo / Ni de acuerdo, ni en desacuerdo / En desacuerdo / Muy en desacuerdo | vida cotidiana | 0.039 (análogas) |
| Consideración del papa León XIV como referente ético y moral para los/as católicos/as o la sociedad en su conjunto | Es un referente ético y moral solamente para los/as católicos/as / Es un referente ético y moral también para la sociedad en su conjunto / No es un referente | vida cotidiana | 0.178 (LLM anclado) |
| Evolución de la imagen que tiene del papa León XIV tras su visita a España | Mucho mejor / Algo mejor / Igual / Algo peor / Mucho peor | vida cotidiana | 0.415 (análogas) |
| Grado de preocupación por el cambio climático | Mucho / Bastante / Regular / Poco / Nada | vida cotidiana | 0.119 (análogas) |
| Grado de preocupación por la invasión de Rusia a Ucrania | Muy preocupado/a / Bastante preocupado/a / Algo preocupado/a / Poco preocupado/a / Nada preocupado/a / No tiene criterio / Le es indiferente | vida cotidiana | 0.117 (análogas) |
| Grado de preocupación por el conflicto en Oriente Próximo | Muy preocupado/a / Bastante preocupado/a / Algo preocupado/a / Poco preocupado/a / Nada preocupado/a / No tiene criterio / Le es indiferente / No tiene información, no sabe de qué guerra se trata | vida cotidiana | 0.099 (análogas) |
| Valoración de la situación económica general de España | Muy buena / Buena / Regular / Mala / Muy mala | vida cotidiana | 0.035 (análogas) |
| Escala de probabilidad (0-10) de ir a votar en elecciones generales | 0 Con toda seguridad no iría a votar / 10 Con toda seguridad, iría a votar | política | 0.012 (análogas) |
| Preferencia personal como presidente del Gobierno central | Pedro Sánchez / Alberto Núñez Feijóo / Santiago Abascal / Yolanda Díaz / Alberto Garzón / Inés Arrimadas / Íñigo Errejón / Isabel Díaz Ayuso / Irene Montero / Ione Belarra / Pablo Iglesias / Alvise Pérez / Gabriel Rufián / Juan Manuel Moreno Bonilla / Emiliano García-Page / Otro/a / Ninguno/a de ellos/as | política | 0.040 (análogas) |
| Pedro Sánchez | Conoce / No conoce | política | 0.001 (análogas) |
| Alberto Núñez Feijóo | Conoce / No conoce | política | 0.004 (análogas) |
| Yolanda Díaz | Conoce / No conoce | política | 0.006 (análogas) |
| Santiago Abascal | Conoce / No conoce | política | 0.006 (análogas) |
| Pedro Sánchez | 1 Muy mal / 10 Muy bien | política | 0.019 (análogas) |
| Alberto Núñez Feijóo | 1 Muy mal / 10 Muy bien | política | 0.033 (análogas) |
| Yolanda Díaz | 1 Muy mal / 10 Muy bien | política | 0.047 (análogas) |
| Santiago Abascal | 1 Muy mal / 10 Muy bien | política | 0.003 (análogas) |
| Grado de confianza en el presidente del Gobierno central: Pedro Sánchez | Mucha confianza / Bastante confianza / Poca confianza / Ninguna confianza | política | 0.039 (análogas) |
| Grado de confianza en el líder del principal partido de la oposición (PP): Alberto Núñez Feijóo | Mucha confianza / Bastante confianza / Poca confianza / Ninguna confianza | política | 0.019 (análogas) |
| Sara Aagesen | Conoce / No conoce | vida cotidiana | 0.021 (análogas) |
| José Manuel Albares | Conoce / No conoce | vida cotidiana | 0.022 (análogas) |
| Félix Bolaños | Conoce / No conoce | vida cotidiana | 0.008 (análogas) |
| Pablo Bustinduy | Conoce / No conoce | vida cotidiana | 0.004 (análogas) |
| Carlos Cuerpo | Conoce / No conoce | vida cotidiana | 0.025 (análogas) |
| Yolanda Díaz | Conoce / No conoce | vida cotidiana | 0.003 (análogas) |
| Arcadi España | Conoce / No conoce | vida cotidiana | 0.014 (análogas) |
| Mónica García | Conoce / No conoce | vida cotidiana | 0.004 (análogas) |
| Fernando Grande-Marlaska | Conoce / No conoce | vida cotidiana | 0.002 (análogas) |
| Jordi Hereu | Conoce / No conoce | vida cotidiana | 0.012 (análogas) |
| Óscar López | Conoce / No conoce | vida cotidiana | 0.038 (análogas) |
| Diana Morant | Conoce / No conoce | vida cotidiana | 0.008 (análogas) |
| Luis Planas | Conoce / No conoce | vida cotidiana | 0.031 (análogas) |
| Óscar Puente | Conoce / No conoce | vida cotidiana | 0.022 (análogas) |
| Ana Redondo | Conoce / No conoce | vida cotidiana | 0.001 (análogas) |
| Sira Rego | Conoce / No conoce | vida cotidiana | 0.012 (análogas) |
| Margarita Robles | Conoce / No conoce | vida cotidiana | 0.010 (análogas) |
| Isabel Rodríguez | Conoce / No conoce | vida cotidiana | 0.003 (análogas) |
| Elma Saiz | Conoce / No conoce | vida cotidiana | 0.041 (análogas) |
| Milagros Tolón | Conoce / No conoce | vida cotidiana | 0.011 (análogas) |
| Ángel Víctor Torres | Conoce / No conoce | vida cotidiana | 0.030 (análogas) |
| Ernest Urtasun | Conoce / No conoce | vida cotidiana | 0.008 (análogas) |
| Sara Aagesen | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.115 (análogas) |
| José Manuel Albares | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.042 (análogas) |
| Félix Bolaños | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.046 (análogas) |
| Pablo Bustinduy | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.069 (análogas) |
| Carlos Cuerpo | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.103 (análogas) |
| Yolanda Díaz | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.031 (análogas) |
| Arcadi España | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.237 (análogas) |
| Mónica García | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.037 (análogas) |
| Fernando Grande-Marlaska | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.041 (análogas) |
| Jordi Hereu | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.031 (análogas) |
| Óscar López | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.049 (análogas) |
| Diana Morant | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.093 (análogas) |
| Luis Planas | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.071 (análogas) |
| Óscar Puente | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.024 (análogas) |
| Ana Redondo | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.081 (análogas) |
| Sira Rego | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.030 (análogas) |
| Margarita Robles | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.079 (análogas) |
| Isabel Rodríguez | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.099 (análogas) |
| Elma Saiz | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.111 (análogas) |
| Milagros Tolón | 1 Muy mal / 10 Muy bien | vida cotidiana | — |
| Ángel Víctor Torres | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.029 (análogas) |
| Ernest Urtasun | 1 Muy mal / 10 Muy bien | vida cotidiana | 0.022 (análogas) |
| Participación electoral en las elecciones generales de 2023 | Votó / No votó / No tenía edad para votar / No tenía derecho a voto / N.R. | política | 0.012 (análogas) |
| Recuerdo de voto en las elecciones generales de 2023 de los votantes | PSOE / PP / VOX / PACMA / Sumar / CCa / ERC / Junts / BNG / UPN / EAJ-PNV / EH Bildu / Otros partidos / En blanco / Voto nulo / N.R. | política | 0.051 (análogas) |
| Momento de la decisión del voto | Lo decide mucho antes del inicio de la campaña electoral / Lo decide al comienzo de la campaña electoral / Lo decide durante la última semana de la campaña electoral / Lo decide durante la jornada de reflexión, la víspera de las elecciones / Lo decide el mismo día de las elecciones / Aún no ha votado en ningunas elecciones | vida cotidiana | 0.096 (análogas) |
| Consistencia del voto respecto a las elecciones generales de 2023 | Sí / No / No votó en 2023 | vida cotidiana | 0.054 (análogas) |
| Fidelidad de voto | Votan siempre por el mismo partido / Por lo general suele votar por el mismo partido / Según lo que más le convenza en ese momento votan por un partido u otro o no votan / Votan en blanco o nulo / No suelen votar / Es la primera vez que votan | vida cotidiana | 0.066 (análogas) |
| Ha expresado deseo de abandonar la entrevista antes de finalizarla | Sí / No | vida cotidiana | 0.001 (análogas) |
| Se ha sentido incómoda por el tema de la entrevista | Sí / No | vida cotidiana | 0.006 (análogas) |
| Ha tenido prisa por acabar la entrevista | Sí / No | vida cotidiana | 0.005 (análogas) |
| Detección de terceras personas en el transcurso de la entrevista | Sí / No | vida cotidiana | 0.006 (análogas) |
| Voto+simpatía en supuestas elecciones generales [recodificada] | PSOE / PP / VOX / PACMA / Podemos / Sumar / Se Acabó la Fiesta / Coalición de izquierdas / Adelante Andalucía / CCa / ERC / Junts / Aliança Catalana / BNG / UPN / EAJ-PNV / EH Bildu / Otro partido / En blanco / Voto nulo / Ninguno | política | 0.092 (análogas) |
| Participación + Recuerdo de voto en las elecciones generales de 2023 | PSOE / PP / VOX / PACMA / Sumar / CCa / ERC / Junts / BNG / UPN / EAJ-PNV / EH Bildu / Otro partido / En blanco / Nulo / No tenía edad / No tenía derecho a voto / No votó / N.R. | política | 0.059 (análogas) |

## Estudio 3577 · 2026-09 · validación (F9-F10) · 42 preguntas

| Pregunta | Opciones | Tipo | Error (TVD) |
| --- | --- | --- | --- |
| Conocimiento del cruce de la frontera en Ceuta ocurrido en el verano del 2026 | Sí, está informado/a / No, no está informado/a | vida cotidiana | 0.331 (LLM anclado) |
| Necesidad de refuerzo de las fronteras para evitar entradas masivas de personas | Sí, cree que es necesario / No, cree que no es necesario / N.S., no tiene información suficiente | vida cotidiana | 0.190 (LLM anclado) |
| Grado de importancia del entendimiento entre España y Marruecos para garantizar la seguridad de las fronteras | Mucha importancia / Bastante importancia / Ni mucha ni poca importancia / Poca importancia / Ninguna importancia | vida cotidiana | 0.205 (LLM anclado) |
| Colaboración o no de la Unión Europea con España para gestionar la situación de Ceuta | Sí, debería colaborar más / No, la colaboración actual es suficiente | vida cotidiana | 0.174 (LLM anclado) |
| Opinión sobre la situación de integración territorial de Ceuta y Melilla | Son territorios tan españoles como cualquier otro territorio de la península / Tienen una situación ambigua y especial que debe ser objeto de acuerdos y entendimiento con Marruecos / Otra respuesta / N.S., no tiene información suficiente o tiene dudas | vida cotidiana | 0.116 (LLM anclado) |
| Grado de importancia de mantener una política amistosa entre España y Marruecos | Mucha importancia / Bastante importancia / Ni mucha ni poca importancia / Poca importancia / Ninguna importancia | vida cotidiana | 0.189 (LLM anclado) |
| Existencia de actores que han interferido en las relaciones entre España y Marruecos con motivo de los incidentes fronterizos del verano del 2026 | Sí / No / N.S. o no tiene información | vida cotidiana | 0.119 (análogas) |
| Primer actor | Estados Unidos, algunos sectores de Estados Unidos / La Unión Europea, algunos sectores de la Unión Europea / Marruecos, algunos sectores de la sociedad marroquí / Israel, algunos sectores de Israel / Donald Trump / Giorgia Meloni / Rusia, algunos sectores de Rusia / Netanyahu / La derecha y/o la ultraderecha internacional / España, algunos sectores de España / Sectores de la derecha y ultraderecha española / Pedro Sánchez / Mohamed VI de Marruecos / Otros países / Putin / Todos o casi todos los/as mencionados anteriormente / Otra respuesta / Ninguno / N.S., no tiene información suficiente | vida cotidiana | 0.399 (LLM anclado) |
| Segundo actor | Estados Unidos, algunos sectores de Estados Unidos / La Unión Europea, algunos sectores de la Unión Europea / Marruecos, algunos sectores de la sociedad marroquí / Israel, algunos sectores de Israel / Donald Trump / Giorgia Meloni / Rusia, algunos sectores de Rusia / Netanyahu / La derecha y/o la ultraderecha internacional / España, algunos sectores de España / Sectores de la derecha y ultraderecha española / Pedro Sánchez / Mohamed VI de Marruecos / Otros países / Putin / Todos o casi todos los/as mencionados anteriormente / Otra respuesta / Ninguno / N.S., no tiene información suficiente | vida cotidiana | 0.585 (LLM anclado) |
| Tercer actor | Estados Unidos, algunos sectores de Estados Unidos / La Unión Europea, algunos sectores de la Unión Europea / Marruecos, algunos sectores de la sociedad marroquí / Israel, algunos sectores de Israel / Donald Trump / Giorgia Meloni / Rusia, algunos sectores de Rusia / Netanyahu / La derecha y/o la ultraderecha internacional / España, algunos sectores de España / Sectores de la derecha y ultraderecha española / Pedro Sánchez / Mohamed VI de Marruecos / Otros países / Putin / Todos o casi todos los/as mencionados anteriormente / Otra respuesta / Ninguno / N.S., no tiene información suficiente | vida cotidiana | 0.458 (LLM anclado) |
| Grado de preocupación por los incendios | Mucho / Bastante / Regular / Poco / Nada | vida cotidiana | 0.453 (análogas) |
| Afectación personal o familiar por los incendios del verano del 2026 | Sí / No | vida cotidiana | 0.013 (análogas) |
| Afectación personal o familiar futura por algún incendio | Sí / No | vida cotidiana | 0.055 (análogas) |
| Atribución de competencias en la prevención y lucha contra los incendios | Deben continuar en las comunidades autónomas / Deben pasar a ser competencia del Gobierno central / De ambos en colaboración / Otras respuestas | vida cotidiana | 0.039 (LLM anclado) |
| Necesidad de un pacto de Estado para hacer frente a las emergencias del cambio climático | Sí es necesario / No es necesario / Depende de la evolución de la situación / Otras respuestas | vida cotidiana | 0.064 (LLM anclado) |
| Grado de preocupación por el cambio climático | Mucho / Bastante / Regular / Poco / Nada | vida cotidiana | 0.171 (análogas) |
| Grado de preocupación por la invasión de Rusia a Ucrania | Muy preocupado/a / Bastante preocupado/a / Algo preocupado/a / Poco preocupado/a / Nada preocupado/a / No tiene criterio / Le es indiferente | vida cotidiana | 0.061 (análogas) |
| Grado de preocupación por el conflicto en Oriente Próximo | Muy preocupado/a / Bastante preocupado/a / Algo preocupado/a / Poco preocupado/a / Nada preocupado/a / No tiene criterio / Le es indiferente / No tiene información, no sabe de qué guerra se trata | vida cotidiana | 0.052 (análogas) |
| Valoración de la situación económica general de España | Muy buena / Buena / Regular / Mala / Muy mala | vida cotidiana | 0.033 (análogas) |
| Escala de probabilidad (0-10) de ir a votar en elecciones generales | 0 Con toda seguridad no iría a votar / 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 Con toda seguridad, iría a votar | política | 0.053 (análogas) |
| Preferencia personal como presidente del Gobierno central | Pedro Sánchez / Alberto Núñez Feijóo / Santiago Abascal / Yolanda Díaz / Alberto Garzón / Inés Arrimadas / Íñigo Errejón / Isabel Díaz Ayuso / Irene Montero / Ione Belarra / Pablo Iglesias / Alvise Pérez / Gabriel Rufián / Juan Manuel Moreno Bonilla / Emiliano García-Page / Otro/a / Ninguno/a de ellos/as | política | 0.061 (análogas) |
| Pedro Sánchez | Conoce / No conoce | política | 0.000 (análogas) |
| Alberto Núñez Feijóo | Conoce / No conoce | política | 0.001 (análogas) |
| Yolanda Díaz | Conoce / No conoce | política | 0.002 (análogas) |
| Santiago Abascal | Conoce / No conoce | política | 0.005 (análogas) |
| Pedro Sánchez | 1 Muy mal / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 Muy bien | política | 0.364 (análogas) |
| Alberto Núñez Feijóo | 1 Muy mal / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 Muy bien | política | 0.493 (análogas) |
| Yolanda Díaz | 1 Muy mal / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 Muy bien | política | 0.045 (análogas) |
| Santiago Abascal | 1 Muy mal / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 Muy bien | política | 0.300 (análogas) |
| Grado de confianza en el presidente del Gobierno central: Pedro Sánchez | Mucha confianza / Bastante confianza / Poca confianza / Ninguna confianza | política | 0.026 (análogas) |
| Grado de confianza en el líder del principal partido de la oposición (PP): Alberto Núñez Feijóo | Mucha confianza / Bastante confianza / Poca confianza / Ninguna confianza | política | 0.021 (análogas) |
| Participación electoral en las elecciones generales de 2023 | Votó / No votó / No tenía edad para votar / No tenía derecho a voto / N.R. | política | 0.018 (análogas) |
| Recuerdo de voto en las elecciones generales de 2023 de los votantes | PSOE / PP / VOX / PACMA / Sumar / CCa / ERC / Junts / BNG / UPN / EAJ-PNV / EH Bildu / Otros partidos / En blanco / Voto nulo / N.R. | política | 0.026 (análogas) |
| Momento de la decisión del voto | Lo decide mucho antes del inicio de la campaña electoral / Lo decide al comienzo de la campaña electoral / Lo decide durante la última semana de la campaña electoral / Lo decide durante la jornada de reflexión, la víspera de las elecciones / Lo decide el mismo día de las elecciones / Aún no ha votado en ningunas elecciones | vida cotidiana | 0.086 (análogas) |
| Consistencia del voto respecto a las elecciones generales de 2023 | Sí / No / No votó en 2023 | vida cotidiana | 0.049 (análogas) |
| Fidelidad de voto | Votan siempre por el mismo partido / Por lo general suele votar por el mismo partido / Según lo que más le convenza en ese momento votan por un partido u otro o no votan / Votan en blanco o nulo / No suelen votar / Es la primera vez que votan | vida cotidiana | 0.053 (análogas) |
| Ha expresado deseo de abandonar la entrevista antes de finalizarla | Sí / No | vida cotidiana | 0.001 (análogas) |
| Se ha sentido incómoda por el tema de la entrevista | Sí / No | vida cotidiana | 0.007 (análogas) |
| Ha tenido prisa por acabar la entrevista | Sí / No | vida cotidiana | 0.003 (análogas) |
| Detección de terceras personas en el transcurso de la entrevista | Sí / No | vida cotidiana | 0.004 (análogas) |
| Voto+simpatía en supuestas elecciones generales [recodificada] | PSOE / PP / VOX / PACMA / Podemos / Sumar / Se Acabó la Fiesta / Coalición de izquierdas / Adelante Andalucía / CCa / ERC / Junts / BNG / UPN / EAJ-PNV / EH Bildu / Otro partido / En blanco / Voto nulo / Ninguno | política | 0.061 (análogas) |
| Participación + Recuerdo de voto en las elecciones generales de 2023 | PSOE / PP / VOX / PACMA / Sumar / CCa / ERC / Junts / BNG / UPN / EAJ-PNV / EH Bildu / Otro partido / En blanco / Nulo / No tenía edad / No tenía derecho a voto / No votó / N.R. | política | 0.038 (análogas) |
