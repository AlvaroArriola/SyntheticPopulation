# Puerta de la fase F6

**Resultado:** fallida  
**Fecha:** 2026-10-16 · **Versión del código:** git:3110b14-dirty  
**Comando:** `sinpop validate --phase 6`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G6.1 | Distribuciones por CCAA × edad_4 frente a la encuesta (V-ENRIQ-MARG) | ❌ | 14 variables; en IC global 92.1 %; por debajo del 90 %: ['uso_internet', 'sector_publico', 'tipo_jornada', 'tenencia_vivienda', 'vehiculo_hogar'] (mínimo tenencia_vivienda 69.1 %); TVD > 0,02: ['vehiculo_hogar', 'compra_online', 'teletrabajo'] | ≥ 90 % de las celdas de cada variable en el IC 95 % (bootstrap); TVD nacional ≤ 0,02 |
| G6.2 | Asociación con las variables llave (V-ENRIQ-ASOC) | ✅ | 81 pares; fuera: 0; Δ máx. 0.049 | |Δ V de Cramér| ≤ 0,05 |
| G6.3 | Relaciones internas de cada bloque (V-ENRIQ-BLOQUE) | ✅ | 19 pares; Δ máx. 0.020, medio 0.007 | |Δ| máx. ≤ 0,05 y medio ≤ 0,02 |
| G6.4 | Emparejar sin una llave y recuperar su asociación (V-ENRIQ-HOLDOUT) | ❌ | llave reservada estudios_3; 14 variables; fuera: ['renta_hogar_decil', 'renta_hogar_decil_ccaa', 'dificultad_fin_mes', 'salud_autopercibida', 'privacion_material', 'carencias', 'sector_publico', 'uso_internet', 'compra_online']; Δ máx. 0.211 (compra_online) | |Δ V de Cramér| ≤ 0,05 y menor que la de la independencia |
| G6.5 | El enriquecimiento no altera las variables de los donantes (igualdad) | ✅ | persons: idénticas (64 columnas); households: idénticas (15 columnas); lineage: idénticas (9 columnas) | columnas idénticas con y sin enriquecimiento |
| G6.6 | Renta media por territorio frente al Atlas de renta | ✅ | 52 provincias; fuera: 0; error máx. 2.76 %; municipios identificados (no calibrados): 334, correlación de la renta relativa con el Atlas 0.58 | |error relativo| ≤ máx(2 %, 2 errores típicos) donde se calibra (D-044.5, por confirmar) |
