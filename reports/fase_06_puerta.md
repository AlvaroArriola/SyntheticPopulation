# Puerta de la fase F6

**Resultado:** fallida  
**Fecha:** 2026-10-16 · **Versión del código:** git:797ab7c-dirty  
**Comando:** `sinpop validate --phase 6`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G6.1 | Distribuciones por CCAA × edad_4 frente a la encuesta (V-ENRIQ-MARG) | ❌ | 14 variables; en IC global 92.6 %; por debajo del 90 %: ['teletrabajo', 'sector_publico', 'tipo_jornada', 'tenencia_vivienda', 'vehiculo_hogar'] (mínimo tenencia_vivienda 65.1 %); TVD > 0,02: ['tenencia_vivienda', 'teletrabajo'] | ≥ 90 % de las celdas de cada variable en el IC 95 % (bootstrap); TVD nacional ≤ 0,02 |
| G6.2 | Asociación con las variables llave (V-ENRIQ-ASOC) | ✅ | 81 pares; fuera: 0; Δ máx. 0.049 | |Δ V de Cramér| ≤ 0,05 |
| G6.3 | Relaciones internas de cada bloque (V-ENRIQ-BLOQUE) | ✅ | 19 pares; Δ máx. 0.022, medio 0.007 | |Δ| máx. ≤ 0,05 y medio ≤ 0,02 |
| G6.4 | Emparejar sin una llave y recuperar su asociación (V-ENRIQ-HOLDOUT) | ✅ | llaves reservadas sexo, nacionalidad_esp_ext, relacion_actividad, estudios_3; 54 pares; peor que la independencia: 0; |Δ| > 0.05: 15 (informativo) | mejor que la independencia (D-046 B1); se informa |Δ V de Cramér| frente a 0,05 |
| G6.5 | El enriquecimiento no altera las variables de los donantes (igualdad) | ✅ | persons: idénticas (64 columnas); households: idénticas (15 columnas); lineage: idénticas (9 columnas) | columnas idénticas con y sin enriquecimiento |
| G6.6 | Renta media por territorio frente al Atlas de renta | ✅ | 52 provincias; fuera: 0; error máx. 3.26 %; municipios identificados (no calibrados): 326, correlación de la renta relativa con el Atlas 0.63 | |error relativo| ≤ máx(2 %, 2 errores típicos) donde se calibra (D-046 C) |
