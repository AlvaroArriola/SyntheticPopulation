# Puerta de la fase F8b

**Resultado:** fallida  
**Fecha:** 2026-10-21 · **Versión del código:** git:5886aac-dirty  
**Comando:** `sinpop validate --phase 8b`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G8B.1 | Recuerdo de generales por provincia frente al oficial (V-POL-RECUERDO) | ✅ | 52/52 provincias; TVD máx. 0.026 | TVD ≤ 1,2 × TVD_ref + 0,005 en cada provincia |
| G8B.2 | Mitad reservada de municipios frente al oficial (V-POL-RESERVADA) | ❌ | España 6/6; CCAA × tamaño 47/49 evaluables; fuera: ['15 de_10001_a_50000', '06 hasta_2000'] | TVD ≤ 0,04 España y ≤ 0,06 CCAA (+ ruido de muestreo); participación ≤ 3 puntos |
| G8B.3 | Perfil de cada electorado frente al postelectoral 3420 (V-POL-PERFIL) | ✅ | 24/24; TVD máx. 0.077 | TVD ≤ 0,08 por variable en electorados con ≥ 300 casos |
| G8B.4 | Ideología dentro de cada electorado frente al CIS (V-POL-COHERENCIA) | ✅ | 9/9 electorados; fuera: 0 | media ± 0,3; razón de desviaciones en [0,8; 1,2] |
| G8B.5 | Transferencia generales → autonómicas frente al CIS (V-POL-TRANSFERENCIA) | ✅ | 28/28 filas; TVD media 0.027 | TVD ≤ 0,10 por fila con ≥ 200 casos (CIS ajustado por IPF a los márgenes oficiales) |
| G8B.6 | Ninguna variable política en la población base ni en la de opinión | ✅ | base: 0; opinión: 0; sin cambios: True | 0 columnas; persons y opinion sin cambios (sha256) |
| G8B.7 | Pruebas de sesgo político (V-POL-SESGO) | ✅ | diversidad 63/63 (razón mín. 0.94); contrafactual 9/9 | razón de entropías ≥ 0,9; contrafactual de ideología ± 0,3 |
| G8B.8 | Sin recuerdo de voto sin derecho a voto en esa elección | ✅ | generales: 0 de 144533 sin derecho; autonómicas: 0 de 136913 | 0 personas |
| G8B.L | Ajuste de los rasgos políticos latentes (V-LATENTE, tarea 6) | ✅ | rasgo_izquierda_derecha: CFI 0.966, RMSEA 0.064, omega 0.72; rasgo_desafeccion: CFI 0.991, RMSEA 0.059, omega 0.85; rasgo_implicacion_politica: CFI 0.971, RMSEA 0.066, omega 0.75; rasgo_eje_territorial: CFI 0.999, RMSEA 0.030, omega 0.72; fuera: 0 | CFI ≥ 0.9, RMSEA ≤ 0.08, omega ≥ 0.7 por rasgo |
| G8B.9 | Revisión humana del informe de F8B | ⏸️ | pendiente (reports/fase_08b.md) | aprobación |
