# Puerta de la fase F9

**Resultado:** fallida  
**Fecha:** 2026-10-21 · **Versión del código:** git:c17ec2f-dirty  
**Comando:** `sinpop validate --phase 9`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G9.1 | Salidas en el formato de §2.8 validadas por esquema (V-FORMATO) | ✅ | 107/107 | 100 % |
| G9.2 | Sistema y baselines en la ventana de validación (total, subgrupo, CCAA) | ⏸️ | TVD media: medición CIS 0.067, B0 0.067, B1 0.066 (107 preguntas); B2 pendiente del modelo de lenguaje (D-069) | B0, B1, B2 y sistema informados |
| G9.3 | Coste por pregunta informado y dentro del presupuesto | ✅ | 0 llamadas, 0.0 € | ≤ 1.0 € por predicción |
| G9.4 | Reformulación neutra (V-REFORMULACION) | ✅ | 107 preguntas; TVD media 0.0001, máx. 0.0026; por encima: 0 | TVD ≤ 0.03 en cada pregunta |
| G9.5 | Cobertura de los intervalos (V-COBERTURA) | ✅ | IC80 0.76, IC95 0.95 (632 opciones) | IC80 en (0.7, 0.9), IC95 en (0.88, 0.99) |
| G9.6 | Modo evento con eventos pasados (V-EVENTO) | ❌ | 6/15 eventos (14/26 evento × indicador); error de magnitud 4.3 pp | dirección correcta en ≥ 2 de cada 3 eventos; magnitud informada |
| G9.7 | Pruebas de estereotipos de la capa de IA | ⏸️ | no aplica mientras no intervenga un modelo de lenguaje (docs/06 §5, D-069) | pruebas superadas |
