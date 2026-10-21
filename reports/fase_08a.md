# Fase 08A · Capa de opinión y valores

**Estado:** superada. Revisión humana G8A.7 aprobada el 2026-10-21. Los huecos que quedaban se completaron después (D-066) y la puerta se volvió a pasar con todo incluido.
**Fecha:** 2026-10-21 · **Versión del código:** ver `reports/fase_08a_validacion.json` (`version_codigo`)
**Comando para reproducir** (tras la cadena F3-F7 de `reports/fase_07.md`):

```
python tools/descargar_cis.py --tipos barometro,sanitario --fichas-barometro 2023-2026 \
  && python -c "from sinpop.opinion import cis, lengua, ess; cis.armonizar(); lengua.armonizar(); ess.armonizar()" \
  && sinpop opinion --run 2026-01-01_ES_1000000_s1 \
  && python -m sinpop.validate.fase8a && sinpop validate --phase 8a
```

- **Estudios temáticos y autonómicos del CIS:** se descargan con `--solo-fichas --fichas <slug@AAAA-MM,...>`; la lista está en `data/raw/cis_catalogo/seleccion.json`.
- **ECEPOV 2021:** la descarga `sinpop.ingest.download` desde el INE.
- **ESS ronda 11:** hay que descargarla a mano (`data/raw/MANUAL_DOWNLOADS.md`) y no se redistribuye.

## Resumen

A cada adulto de la población nacional (840.249 personas de 18 años y más) se le asigna en `opinion.parquet` (unido por `person_id`):

| Tipo | Variables | Fuente |
| --- | --- | --- |
| Valores observados | religiosidad, clase social subjetiva, situación económica personal | Barómetros del CIS (12 meses anteriores al corte) |
| | identidad territorial (Linz-Moreno) | Estudio 3409 del CIS (nacional, 2023) y postelectorales autonómicos de Andalucía, Aragón, Castilla y León, Cataluña, Galicia y País Vasco |
| | lengua habitual | ECEPOV 2021 del INE (352.786 adultos) |
| | medio de información principal | CIS 3511, Audiencias de medios II (2025) |
| Estilos de respuesta | `estilo_ns_nc` | Todos los estudios del CIS |
| | `estilo_aquiescencia` | ESS ronda 11 |
| Rasgos latentes | confianza institucional | CIS 3535 |
| | sensibilidad al precio, aislamiento social | CIS 3554 |
| | preocupación ambiental | CIS 3489 |
| | confianza en la tecnología | CIS 3495 |
| | confianza interpersonal, tradición/apertura | ESS ronda 11 |

- Cada columna lleva su `__calidad` y la fecha de referencia (30/06/2026).
- Ninguna variable de opinión ni política entra en `persons.parquet` (D-005).
- Están cubiertas todas las variables y todos los rasgos de `02_datos_y_variables.md` §3.4.

**Datos:**
- Microdatos del CIS anteriores al corte, armonizados por la **etiqueta** de cada respuesta y nunca por el código (D-063): 61 estudios descargados, de los que se armonizan 57 (252.288 encuestados).
- La ECEPOV 2021 del INE.
- La ESS ronda 11 (España, 1.793 adultos).
- Los estudios del CIS posteriores al corte están en `data/eval/cis/` y no se leen.

**Método:**
- Regresión multinomial (o lineal, para los rasgos) ponderada, según sexo, edad, estudios, actividad, comunidad, tamaño de municipio y la interacción comunidad × edad. La regularización se elige por validación cruzada, al estilo MRP (D-064).
- La lengua usa además la provincia, la nacionalidad y el país de nacimiento.
- Cada persona recibe una **extracción aleatoria** con la semilla. En los rasgos, la predicción más un residuo real de su celda edad × estudios × sexo.
- **Calidad (`__calidad`):**
  - con fuentes que solo entrevistan a españoles (barómetros y la mayoría de estudios del CIS), los extranjeros y los residentes en establecimientos colectivos se marcan `extrapolada`;
  - con la ECEPOV y la ESS, que entrevistan a todas las nacionalidades, solo los residentes en colectivos.

## Puerta de salida

Ver `reports/fase_08a_puerta.md` (`sinpop validate --phase 8a`): **superada**.

| ID | Resultado | Valor |
| --- | --- | --- |
| G8A.1 V-LATENTE | ✅ | Los siete rasgos cumplen CFI ≥ 0,90, RMSEA ≤ 0,08 y omega ≥ 0,70. Excepción aprobada: tradición/apertura, omega 0,68 (D-066) |
| G8A.2 V-OPINION-CV | ✅ | 21 preguntas reservadas completas: TVD media del modelo 0,116 frente a 0,169 de B0; el modelo gana en las 21 |
| G8A.3 V-DIVERSIDAD (rasgos) | ✅ | 79 de 79 grupos edad × estudios × sexo con ratio de varianzas en [0,88; 1,05] |
| G8A.4 V-ENRIQ-MARG (valores) | ✅ | 94,0 % de las celdas comunidad × edad dentro del IC 95 %; TVD nacional ≤ 0,011 en todas las variables (detalle abajo) |
| G8A.5 Barómetro Sanitario | ✅ (se informa) | Oleada de marzo de 2026, 13 preguntas, 221 celdas pregunta × comunidad: TVD simulada 0,072 frente a B0 nacional 0,078 y B1 directa 0,086; ruido muestral 0,054 |
| G8A.6 Fugas | ✅ | `test_no_leakage.py`: 7 pasan |
| G8A.7 Revisión humana | ✅ | Aprobada el 2026-10-21 |

**Reproducibilidad:** dos construcciones seguidas de `opinion.parquet` con la misma semilla dan el mismo SHA-256 (`f12b7331…`).

## Resultados principales

### Variables observadas (G8A.4)

| Variable | Celdas en el IC 95 % | TVD nacional | Referencia |
| --- | --- | --- | --- |
| religiosidad | 92,4 % | 0,004 | Barómetros CIS (españoles, 12 meses) |
| clase subjetiva | 92,7 % | 0,006 | Barómetros CIS |
| situación económica personal | 95,7 % | 0,011 | Barómetros CIS |
| identidad territorial | 96,4 % | 0,010 | CIS 3409 y postelectorales, reponderados al peso de cada comunidad |
| lengua habitual | 92,9 % | 0,004 | ECEPOV 2021, reponderada a la composición de 2026 |
| medio de información principal | 94,5 % | 0,008 | CIS 3511 |

- **Lengua:** la ECEPOV es de 2021, y la población adulta nacida fuera de España pasó del 16 % al 21 %. Sin reponderar la referencia por comunidad × edad × país de nacimiento, el cambio demográfico real parecía un error del modelo (78,7 % de celdas).
- **Identidad:** la referencia junta postelectorales autonómicos de miles de entrevistas con el estudio nacional. Sin reponderar por comunidad, la cifra «nacional» del CIS sobrerrepresenta seis comunidades (TVD 0,053, frente a 0,010 reponderada).

### Rasgos latentes (G8A.1, G8A.3)

| Rasgo | Fuente | Ítems | CFI · RMSEA · omega |
| --- | --- | --- | --- |
| `rasgo_confianza_institucional` | CIS 3535 (nov. 2025) | Confianza en medios, Justicia, Constitución, Tribunal Constitucional y organizaciones empresariales | 0,995 · 0,038 · 0,80 |
| `rasgo_sensibilidad_precio` | CIS 3554 (mar. 2026) | Miedo a no vivir con dignidad, a perder el trabajo, a no pagar la vivienda y a una crisis económica | 0,997 · 0,048 · 0,82 |
| `rasgo_aislamiento_social` | CIS 3554 | Temor a la soledad, a no tener a quien amar y a quedarse sin apoyo emocional | 0,987 · 0,049 · 0,74 (conjunto) |
| `rasgo_preocupacion_ambiental` | CIS 3489 (dic. 2024) | Preocupación por el cambio climático, importancia de las medidas, más recursos y atribución de la DANA al clima | 0,991 · 0,059 · 0,71 |
| `rasgo_confianza_tecnologia` | CIS 3495 (feb. 2025) | Asociar los avances tecnológicos con progreso, riqueza, eficacia y bienestar | 0,999 · 0,020 · 0,76 |
| `rasgo_confianza_interpersonal` | ESS 11 (2023) | Se puede confiar en la gente, la gente es justa, la gente ayuda | 0,960 · 0,045 · 0,70 (conjunto) |
| `rasgo_tradicion_apertura` | ESS 11 | Polo de conservación de Schwartz: seguridad, conformidad y tradición (6 ítems) | 0,943 · 0,069 · **0,68** (excepción aprobada) |

- Los rasgos están tipificados (media 0, desviación 1 ponderadas).
- Los rasgos de tres ítems se contrastan en el factorial conjunto de su estudio:
  - 3554: 13 grados de libertad, correlación entre factores 0,58;
  - ESS: 26 grados de libertad, correlación entre factores −0,12.
- **Contraste con cifras publicadas:** la media de «Progreso» en el 3495 reproduce la publicada por el CIS (7,68 frente a 7,67). La confianza interpersonal media de la ESS en España es 5,27 sobre 10.
- **Estilos de respuesta:** NS/NC (proporción de respuestas «No sabe» o «No contesta») y aquiescencia (media de las 21 escalas de valores de Schwartz, 4,29 sobre 6).

### Validación cruzada por pregunta (G8A.2)

- **Método:** se reserva el estudio más reciente de cada pregunta repetida en los estudios nacionales; el modelo se ajusta con los anteriores (`reports/fase_08a/v_opinion_cv.csv`).
- **Resultado:** el modelo mejora a la distribución histórica nacional en las 21 preguntas.
- **Mayor mejora:** situación económica personal (0,067 frente a 0,144) y clase subjetiva (0,087 frente a 0,166).
- **Menor margen:** el primer problema de España (0,199 frente a 0,245), que depende sobre todo de la actualidad.

### Barómetro Sanitario por comunidad (G8A.5)

- **Método:** la población sintética (todos los adultos en vivienda familiar) responde la oleada de marzo de 2026 con el modelo de los 12 meses previos.
- **Resultado:** la TVD por comunidad, 0,072, mejora a las referencias nacional (0,078) y directa (0,086).
- **Ruido:** queda a 0,018 del ruido muestral de la oleada (0,054), con unos 130 encuestados por comunidad.

## Limitaciones (D-063 a D-066)

1. **Extrapolados:** los extranjeros (en las variables del CIS) y los residentes en colectivos (en todas) reciben la predicción con su perfil y se marcan `extrapolada`. En los extranjeros, «otra religión» está previsiblemente infravalorada.
2. **Identidad territorial:**
   - En las comunidades sin estudio autonómico propio sale del estudio nacional 3409, con muestras pequeñas: de 1.198 en Madrid a 75 en La Rioja, 11 en Melilla y 8 en Ceuta.
   - El modelo conjunto regularizado las acerca al patrón general. Ahí la variable es menos fiable.
3. **Fechas distintas de los rasgos:** van de 2023 (ESS, 3409) a 2026 (3554), y hay una sola medición de cada uno. No hay serie temporal para fecharlos (F8C).
4. **Tradición/apertura:** se mide por el polo de conservación de Schwartz, con fiabilidad omega 0,68. Es una excepción aprobada; las escalas de Schwartz son anchas por diseño.
5. **Medio de información principal:** es un derivado, el de mayor frecuencia de uso. El CIS no pregunta un medio «principal».
6. **Lengua habitual:** es la más usada **en familia** (ECEPOV); en el trabajo o con los amigos puede ser otra.
7. **Estudios descargados que no se usan:**
   - las tres Encuestas Sociales Generales (3391, 3462, 3506), con perfil en el formato del ISSP;
   - el Índice de Confianza del Consumidor (3569);
   - el preelectoral de 2023 (3402).

   Ninguno se usa en los modelos nacionales; queda constancia en D-065 y D-066.

## Incidente de datos

El fichero de la ESS se subió al repositorio, que es público, lo que incumplía las condiciones de la ESS y la regla 8 de CLAUDE.md. Con la aprobación de la persona responsable, se reescribió el historial de la rama y el fichero queda solo en local (D-066).

## Tests

- **Batería:** `pytest tests` pasa entero salvo `tests/integration/test_poblacion.py` (F4, sin cambios en esta fase), que construye tres poblaciones con todo el banco de donantes y el contenedor (unos 14 GB) lo corta por memoria. Se ejecuta con `--deselect tests/integration/test_poblacion.py`.
- **Tests nuevos:** puntuación de ítems, escalas con extremos etiquetados, reglas de la lengua habitual y patrones de la escala Linz-Moreno (`tests/unit/test_latentes.py`).

## Decisiones

- D-063: armonización y variables de valores.
- D-064: modelo MRP, universos y validación.
- D-065: rasgos latentes.
- D-066: huecos completados, excepción de omega e incidente de la ESS.
