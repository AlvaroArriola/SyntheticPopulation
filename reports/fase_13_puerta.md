# Puerta de la fase F13

**Resultado:** superada  
**Fecha:** 2026-10-23 · **Versión del código:** git:fab659d-dirty  
**Comando:** `sinpop validate --phase 13`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G13.1 | Servicio y CLI devuelven el mismo resultado en las preguntas y eventos de ejemplo | ✅ | 4/4 idénticos | JSON idéntico salvo tiempos |
| G13.2 | Respuestas del servicio con esquema §2.8, marca, aviso, intervalos y confianza | ✅ | 0 fallos | 0 fallos de formato |
| G13.3 | Ninguna ruta devuelve microdatos ni datos de evaluación | ✅ | 1 tests pasan | test pasa |
| G13.4 | El presupuesto del LLM se respeta igual que en la CLI | ✅ | 2 tests pasan | tests pasan |
