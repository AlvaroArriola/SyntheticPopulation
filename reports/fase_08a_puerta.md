# Puerta de la fase F8a

**Resultado:** superada  
**Fecha:** 2026-10-21 · **Versión del código:** git:da8b790  
**Comando:** `sinpop validate --phase 8a`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G8A.1 | Ajuste del modelo latente (V-LATENTE) | ✅ | rasgo_confianza_institucional: CFI 0.995, RMSEA 0.038, omega 0.80; rasgo_sensibilidad_precio: CFI 0.997, RMSEA 0.048, omega 0.82; rasgo_aislamiento_social: CFI 0.987, RMSEA 0.049, omega 0.74; fuera: 0 | CFI ≥ 0.9, RMSEA ≤ 0.08, omega ≥ 0.7 por rasgo |
| G8A.2 | Validación cruzada por pregunta completa frente a B0 (V-OPINION-CV) | ✅ | 21 preguntas; TVD modelo 0.1161 frente a B0 0.1688 | TVD media del modelo < TVD media de B0 (distribución histórica) |
| G8A.3 | Varianza de los rasgos dentro de los grupos frente a la real (V-DIVERSIDAD) | ✅ | 63 de 63 grupos dentro; ratio de 0.88 a 1.05 | ratio de varianzas en [0,8; 1,2] en cada grupo con ≥ 200 encuestados |
| G8A.4 | Variables de valores por CCAA × edad frente al CIS (V-ENRIQ-MARG) | ✅ | en IC global 93.4 %; clase_subjetiva 92.7 %; religiosidad 92.4 %; situacion_economica_personal 95.7 %; fuera: 0 | ≥ 90 % de las celdas en el IC 95 % del CIS y TVD nacional ≤ 0,02 |
| G8A.5 | Respuestas simuladas por CCAA frente al Barómetro Sanitario (se informa) | ✅ | oleada 3551 (ajuste con los 12 meses previos); 13 preguntas, 221 celdas pregunta × CCAA; TVD media simulada 0.072, B0 nacional 0.078, B1 directa 0.087, ruido muestral 0.054 | se informa el error (sin umbral) |
| G8A.6 | test_no_leakage.py pasa | ✅ | 7 passed in 5.32s; 6 autotests del detector | existe y sus autotests pasan |
| G8A.7 | Revisión humana del informe de F8A | ✅ | aprobada | aprobación |
