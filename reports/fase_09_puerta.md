# Puerta de la fase F9

**Resultado:** fallida  
**Fecha:** 2026-10-23 · **Versión del código:** git:fab659d-dirty  
**Comando:** `sinpop validate --phase 9`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G9.1 | Salidas en el formato de §2.8 validadas por esquema (V-FORMATO) | ✅ | 108/108 | 100 % |
| G9.2 | Sistema y baselines en la ventana de validación (total, subgrupo, CCAA) | ✅ | TVD media: medición CIS 0.056, B0 0.056, B1 0.056 (108 preguntas); B2 0.258 (subgrupos 0.265, CCAA 0.266; 122 preguntas) | B0, B1, B2 y sistema informados |
| G9.3 | Coste por pregunta informado y dentro del presupuesto | ✅ | 0 llamadas, 0.0 € | ≤ 1.0 € por predicción |
| G9.4 | Reformulación neutra (V-REFORMULACION) | ✅ | 108 preguntas; TVD media 0.0002, máx. 0.0136; por encima: 0 | TVD ≤ 0.03 en cada pregunta |
| G9.5 | Cobertura de los intervalos (V-COBERTURA) | ✅ | IC80 0.78, IC95 0.94 (853 opciones) | IC80 en (0.7, 0.9), IC95 en (0.88, 0.99) |
| G9.6 | Modo evento con eventos pasados (V-EVENTO) | ❌ | sin LLM 6/15 eventos (14/26 evento × indicador), error 4.3 pp; con LLM 8/16 eventos, error 3.9 pp (contaminado: el modelo conoce lo que pasó después de estos eventos; cota superior) | dirección correcta en ≥ 2 de cada 3 eventos; magnitud informada |
| G9.7 | Pruebas de estereotipos de la capa de IA (docs/06 §5) | ✅ | razón mediana 0.72 en 265 pregunta × dimensión (frente a lo observado 0.60); homogeneidad: no aplica; justificaciones: 165 revisadas, 0 problemáticas | razón de brechas LLM/estadístico ≤ 1.25 (aprobado); auditoría |
