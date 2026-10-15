# Puerta de la fase F2

**Resultado:** fallida  
**Fecha:** 2026-10-15 · **Versión del código:** git:23503ab-dirty  
**Comando:** `sinpop validate --phase 2`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G2.1 | Valores dentro del dominio declarado | ✅ | 137 columnas categóricas en 17 ficheros; fuera de dominio: 0 | 0 |
| G2.2 | Ningún NS/NC/NP como valor numérico | ✅ | 0 columnas numéricas con códigos especiales | 0 |
| G2.3 | Totales ponderados conservados | ✅ | 14 totales; diferencia máxima 0.000000 % | < 0,01 % |
| G2.4 | ≥3 cifras oficiales por fuente P0/P1 | ✅ | 14/14 fuentes; 111 cifras | ≥3 por fuente dentro de tolerancia (D-027) |
| G2.5 | Tests por tabla de recodificación | ✅ | 72 tablas con test parametrizado; ...............................                                          [100%] | 1 test por tabla, 0 fallos |
| G2.6 | Resultados electorales = totales oficiales | ❌ | generales 2023: 8131 municipios, 0 descuadres internos; faltan los totales oficiales (BOE-A-2023-18907, descarga manual) · autonómicas: 14/19 sin diferencias; 01: 8 circunscripciones; 4 errores: Granada: válidos publicados 480675 ≠ 480678; 04: 4 circunscripciones; solo voto CERA; faltan los resultados generales (MANUAL_DOWNLOADS.md); 05: 8 circunscripciones; 3 errores: El Hierro: votantes 6473 ≠ candidaturas + blancos + nulos 6475; 12: 4 circunscripciones; 2 errores: Galicia: válidos publicados 1501857 ≠ 1501757; 14: 1 circunscripciones; 1 errores: Murcia: votantes 694906 ≠ candidaturas + blancos + nulos 694855 | sin diferencias (nacional y provincial) |
| G2.7 | Códigos de partido del CIS en partidos.yaml | ✅ | 0 códigos sin asignar | 0 |
| G2.8 | Revisión humana: 20 registros por fuente frente al original | ⏸️ | pendiente (reports/fase_02_muestras.md) | aprobación |
