# Puerta de la fase F6

**Resultado:** fallida  
**Fecha:** 2026-10-19 · **Versión del código:** git:7f9a7f4-dirty  
**Comando:** `sinpop validate --phase 6`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G6.1 | Distribuciones por CCAA × edad_4 frente a la encuesta (V-ENRIQ-MARG) | ✅ | 15 variables; en IC global 92.5 %; fuera del umbral estricto: ['teletrabajo', 'sector_publico', 'tipo_jornada', 'tenencia_vivienda', 'vehiculo_hogar']; aceptadas como limitación (D-048): ['teletrabajo', 'sector_publico', 'tipo_jornada', 'tenencia_vivienda', 'vehiculo_hogar']; fuera: 0 | ≥ 90 % de las celdas de cada variable en el IC 95 % y TVD nacional ≤ 0,02; o, con la composición de la encuesta, TVD ≤ 0,02 y limitación declarada (D-048) |
| G6.2 | Asociación con las variables llave (V-ENRIQ-ASOC) | ✅ | 86 pares; fuera: 0; Δ máx. 0.049 | |Δ V de Cramér| ≤ 0,05 |
| G6.3 | Relaciones internas de cada bloque (V-ENRIQ-BLOQUE) | ✅ | 19 pares; Δ máx. 0.022, medio 0.006 | |Δ| máx. ≤ 0,05 y medio ≤ 0,02 |
| G6.4 | Emparejar sin una llave y recuperar su asociación (V-ENRIQ-HOLDOUT) | ✅ | llaves reservadas sexo, nacionalidad_esp_ext, relacion_actividad, estudios_3; 60 pares; peor que la independencia: 0; |Δ| > 0.05: 18 (informativo) | mejor que la independencia (D-046 B1); se informa |Δ V de Cramér| frente a 0,05 |
| G6.5 | El enriquecimiento no altera las variables de los donantes (igualdad) | ✅ | persons: idénticas (64 columnas); households: idénticas (15 columnas); lineage: idénticas (9 columnas) | columnas idénticas con y sin enriquecimiento |
| G6.6 | Renta media por territorio frente al Atlas de renta | ❌ | 52 provincias; fuera: ['49']; error máx. 3.78 %; municipios identificados (no calibrados): 315, correlación de la renta relativa con el Atlas 0.60 | |error relativo| ≤ máx(2 %, 2 errores típicos) donde se calibra (D-046 C) |
