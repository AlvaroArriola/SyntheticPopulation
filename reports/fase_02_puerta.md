# Puerta de la fase F2

**Resultado:** fallida  
**Fecha:** 2026-10-15 · **Versión del código:** git:8dd392e  
**Comando:** `sinpop validate --phase 2`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G2.1 | Valores dentro del dominio declarado y vacíos documentados | ✅ | 139 columnas categóricas en 19 ficheros; fuera de dominio: 0; vacíos sin documentar: 0 | 0 y 0 |
| G2.2 | Ningún NS/NC/NP como valor numérico | ✅ | 0 columnas numéricas con códigos especiales | 0 |
| G2.3 | Totales ponderados conservados | ✅ | 14 totales; diferencia máxima 0.000000 % | < 0,01 % |
| G2.4 | ≥3 cifras oficiales por fuente P0/P1 | ❌ | 13/14 fuentes; 114 cifras; fallan: encuesta_salud (5/6) | ≥3 por fuente dentro de tolerancia (D-027) |
| G2.5 | Tests por tabla de recodificación | ✅ | 72 tablas con test parametrizado; .................................                                        [100%] | 1 test por tabla, 0 fallos |
| G2.6 | Resultados electorales = totales oficiales | ✅ | generales 2023 (BOE): 52 provincias, 59 candidaturas, 0 diferencias con el Total estatal publicado; detalle municipal provisional: 8131 municipios sin descuadres · autonómicas: 19/19 sin diferencias | sin diferencias (nacional y provincial) |
| G2.7 | Códigos de partido del CIS en partidos.yaml | ✅ | 0 códigos sin asignar | 0 |
| G2.8 | Revisión humana: 20 registros por fuente frente al original | ⏸️ | pendiente (reports/fase_02_muestras.md) | aprobación |
