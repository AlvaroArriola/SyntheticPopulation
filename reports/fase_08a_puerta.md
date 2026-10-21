# Puerta de la fase F8a

**Resultado:** fallida  
**Fecha:** 2026-10-21 · **Versión del código:** git:eada33e-dirty  
**Comando:** `sinpop validate --phase 8a`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G8A.1 | Ajuste del modelo latente (V-LATENTE) | ❌ | falta reports/fase_08a_validacion.json (python -m sinpop.validate.fase8a) | CFI ≥ 0.9, RMSEA ≤ 0.08, omega ≥ 0.7 por rasgo |
| G8A.2 | Validación cruzada por pregunta completa frente a B0 (V-OPINION-CV) | ❌ | falta reports/fase_08a_validacion.json (python -m sinpop.validate.fase8a) | TVD media del modelo < TVD media de B0 (distribución histórica) |
| G8A.3 | Varianza de los rasgos dentro de los grupos frente a la real (V-DIVERSIDAD) | ❌ | falta reports/fase_08a_validacion.json (python -m sinpop.validate.fase8a) | ratio de varianzas en [0,8; 1,2] en cada grupo con ≥ 200 encuestados |
| G8A.4 | Variables de valores por CCAA × edad frente al CIS (V-ENRIQ-MARG) | ❌ | falta reports/fase_08a_validacion.json (python -m sinpop.validate.fase8a) | ≥ 90 % de las celdas en el IC 95 % del CIS y TVD nacional ≤ 0,02 |
| G8A.5 | Respuestas simuladas por CCAA frente al Barómetro Sanitario (se informa) | ❌ | falta reports/fase_08a_validacion.json (python -m sinpop.validate.fase8a) | se informa el error (sin umbral) |
| G8A.6 | test_no_leakage.py pasa | ❌ | 1 failed, 6 passed in 0.58s; 6 autotests del detector | existe y sus autotests pasan |
| G8A.7 | Revisión humana del informe de F8A | ⏸️ | pendiente (reports/fase_08a.md) | aprobación |
