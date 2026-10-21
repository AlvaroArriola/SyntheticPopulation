# Fase 08A · Capa de opinión y valores

**Estado:** puertas automáticas G8A.1-G8A.6 superadas; **pendiente de revisión humana (G8A.7)**. F8B no se empieza hasta la aprobación.
**Fecha:** 2026-10-21 · **Versión del código:** ver `reports/fase_08a_validacion.json` (`version_codigo`)
**Comando para reproducir** (tras la cadena F3-F7 de `reports/fase_07.md`):

```
python tools/descargar_cis.py --tipos barometro,sanitario --fichas-barometro 2023-2026 \
  && python -c "from sinpop.opinion import cis; cis.armonizar()" \
  && sinpop opinion --run 2026-01-01_ES_1000000_s1 \
  && python -m sinpop.validate.fase8a && sinpop validate --phase 8a
```

Los estudios temáticos y autonómicos se descargan con `--solo-fichas --fichas <slug@AAAA-MM,...>`; la lista está en `data/raw/cis_catalogo/seleccion.json`.

## Resumen

A cada adulto de la población nacional (840.249 personas de 18 años y más) se le asignan, en `opinion.parquet` (unido por `person_id`):

- **Tres variables de valores:** religiosidad, clase social subjetiva y situación económica personal.
- **El estilo de respuesta NS/NC.**
- **Tres rasgos latentes:** confianza institucional, sensibilidad al precio y temor al aislamiento social.

Cada columna lleva su `__calidad` y la fecha de referencia (30/06/2026). Ninguna variable de opinión ni política entra en `persons.parquet` (D-005).

**Fuente:** microdatos del CIS anteriores al corte, armonizados por la **etiqueta** de cada respuesta y nunca por el código (D-063). Son 47 estudios y 179.543 encuestados:

- 37 barómetros mensuales de 2023-2026;
- 2 oleadas del Barómetro Sanitario;
- 4 estudios temáticos;
- 4 postelectorales autonómicos.

Los barómetros posteriores al corte están en `data/eval/cis/` y no se leen.

**Método:**
- **Modelo:** regresión multinomial (o lineal, para los rasgos) ponderada con los pesos del CIS, según sexo, edad, estudios, actividad, comunidad, tamaño de municipio y la interacción comunidad × edad. La regularización se elige por validación cruzada, al estilo MRP (D-064).
- **Asignación:** cada persona recibe una **extracción aleatoria** con la semilla, no la categoría más probable. En los rasgos, la predicción más un residuo real de su celda edad × estudios × sexo.
- **Calidad:** los extranjeros y los residentes en establecimientos colectivos están fuera del universo de los barómetros y se marcan `extrapolada`.

## Puerta de salida

Ver `reports/fase_08a_puerta.md` (`sinpop validate --phase 8a`).

| ID | Resultado | Valor |
| --- | --- | --- |
| G8A.1 V-LATENTE | ✅ | Confianza institucional: CFI 0,995, RMSEA 0,038, omega 0,80. Sensibilidad al precio: 0,997 / 0,048 / 0,82. Aislamiento social: 0,987 / 0,049 / 0,74 (ajuste del factorial conjunto de su estudio) |
| G8A.2 V-OPINION-CV | ✅ | 21 preguntas reservadas completas: TVD media del modelo 0,116 frente a 0,169 de B0; el modelo gana en las 21 |
| G8A.3 V-DIVERSIDAD (rasgos) | ✅ | 63 de 63 grupos edad × estudios × sexo con ratio de varianzas en [0,91; 1,07] |
| G8A.4 V-ENRIQ-MARG (valores) | ✅ | 93,4 % de celdas CCAA × edad en el IC 95 % del CIS (religiosidad 92,4 %, clase 92,7 %, situación económica 95,7 %); TVD nacional 0,004 / 0,006 / 0,011 |
| G8A.5 Barómetro Sanitario | ✅ (se informa) | Oleada de marzo de 2026, 13 preguntas, 221 celdas pregunta × comunidad: TVD simulada 0,072 frente a B0 nacional 0,078 y B1 directa 0,087; ruido muestral de la oleada 0,054 |
| G8A.6 Fugas | ✅ | `test_no_leakage.py`: 7 pasan |
| G8A.7 Revisión humana | ⏸️ | Este informe |

## Resultados principales

### Variables de valores (G8A.4)

- **Comparación:** se hace en el universo del CIS (españoles de 18+ en vivienda familiar) frente a los barómetros nacionales de los 12 meses anteriores al corte.
- **Tablas:** `reports/fase_08a/2026-01-01_ES_1000000_s1_v_marg_valores.csv`, con proporción sintética, del CIS e IC por celda.
- **Interacción comunidad × edad:** sin ella, religiosidad quedaba en el 89,5 %, porque el modelo aditivo no recoge el efecto de la edad propio de cada comunidad (D-064).
- **Efecto de la regularización:** con la regularización por validación cruzada, la proporción baja del 99 % al 93 %. El modelo se encoge en las comunidades con pocos encuestados en lugar de copiar su ruido muestral, que es lo que se busca.

### Rasgos latentes (G8A.1, G8A.3)

| Rasgo | Estudio | Ítems (carga) | Lectura |
| --- | --- | --- | --- |
| `rasgo_confianza_institucional` | 3535, Tendencias sociales V (nov. 2025) | Medios 0,44 · Justicia 0,74 · Constitución 0,70 · Tribunal Constitucional 0,77 · Organizaciones empresariales 0,66 | Confianza en instituciones no partidistas. Partidos, sindicatos, Gobierno y Parlamento forman otro factor (partidista), que se deja para la desafección de F8B |
| `rasgo_sensibilidad_precio` | 3554, Temores (mar. 2026) | Trabajo o pensión que no permitan vivir con dignidad 0,70 · Perder el trabajo 0,79 · No poder pagar la vivienda 0,84 · Crisis económica 0,56 | Presión del coste de vida (miedo a no llegar) |
| `rasgo_aislamiento_social` | 3554 | Temor a la soledad 0,81 · A no tener a quien amar 0,65 · A quedarse sin apoyo emocional 0,62 | Temor a la soledad, no la red social real. «Tiene con quién hablar» no carga (0,04) y se descarta |

- **Escala:** los rasgos están tipificados (media 0 y desviación 1 ponderadas en el CIS).
- **Factorial conjunto de 3554:** la correlación entre sensibilidad al precio y aislamiento es 0,58, así que son rasgos distintos.
- **Varianza dentro de los grupos:** cumple en los 63 grupos con al menos 200 encuestados (`..._v_diversidad_rasgos.csv`).

### Validación cruzada por pregunta (G8A.2)

- **Método:** se reserva el estudio más reciente de cada pregunta repetida; el modelo se ajusta con los anteriores y se compara por grupo edad × sexo × estudios (`reports/fase_08a/v_opinion_cv.csv`).
- **Resultado:** el modelo mejora a la distribución histórica nacional en las 21 preguntas.
- **Mayor mejora:** situación económica personal (0,067 frente a 0,144), clase subjetiva (0,087 frente a 0,166) y religiosidad (0,079 frente a 0,140).
- **Menor margen:** el primer problema de España (0,199 frente a 0,245), que depende sobre todo de la actualidad y poco del perfil.

### Barómetro Sanitario por comunidad (G8A.5)

- **Método:** la población sintética responde las preguntas de la oleada de marzo de 2026 con el modelo ajustado en los 12 meses previos.
- **Universo:** todos los adultos en vivienda familiar, extranjeros incluidos, como el Sanitario.
- **Resultado:** la TVD media por comunidad, 0,072, mejora a la nacional (0,078) y a la directa de la comunidad en la oleada previa (0,087).
- **Ruido:** queda 0,018 por encima del ruido muestral de la propia oleada de contraste (0,054), con unos 130 encuestados por comunidad.
- **Detalle:** `reports/fase_08a/2026-01-01_ES_1000000_s1_g8a5_sanitario.csv`.

## Limitaciones y huecos (D-063, D-065)

1. **Extranjeros y residentes en colectivos:** reciben la predicción del modelo de los españoles en vivienda familiar (`extrapolada`). En los extranjeros «otra religión» está previsiblemente infravalorada, y no hay fuente oficial con la que corregirlo.
2. **Rasgos de docs/02 §3.4 sin construir**, por falta de baterías adecuadas en los estudios disponibles. No se rellenan con suposiciones:
   - `rasgo_confianza_tecnologia` y `rasgo_preocupacion_ambiental`: solo hay ítems sueltos. Propuesta: estudios del CIS sobre inteligencia artificial y medio ambiente, o el módulo de cambio climático de la ESS.
   - `rasgo_confianza_interpersonal` y `rasgo_tradicion_apertura`: necesitan la ESS, que pide registro (`data/raw/MANUAL_DOWNLOADS.md`).
   - `estilo_aquiescencia`: necesita baterías equilibradas de acuerdo y desacuerdo.
   - `identidad_territorial` (Linz-Moreno) y `lengua_habitual`: no están en los barómetros 2023-2026; los postelectorales descargados solo cubren cuatro comunidades. Propuesta: estudios autonómicos del CIS y de los centros autonómicos.
   - `medio_informacion_principal`: no está en los estudios descargados.
3. **Índice de Confianza del Consumidor (3569):** descargado pero no usado, porque no lleva el perfil estándar del CIS.
4. **Una sola medición por rasgo:** cada rasgo latente procede de un único estudio, de noviembre de 2025 o marzo de 2026. No hay todavía serie temporal para fecharlos (F8C).
5. **Cambio de la clase subjetiva:** el dominio de `clase_subjetiva` incluye «otras» y «no cree en las clases», respuestas reales del CIS (D-063).

## Decisiones

D-063 (armonización y variables de valores), D-064 (modelo MRP, universos y validación) y D-065 (rasgos latentes y huecos).

## Para la revisión humana

- **Rasgos:** ¿se aceptan los tres rasgos construidos y los huecos declarados?
- **Desafección:** ¿se acepta que la confianza en partidos, Gobierno y Parlamento pase a `rasgo_desafeccion` (F8B)?
- **Descargas manuales:** ¿se descarga la ESS ronda 11 y se buscan estudios autonómicos de identidad y lengua para completar los huecos antes de F8B, o se aceptan como limitación?
