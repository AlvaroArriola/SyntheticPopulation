# Puerta de la fase F0

**Resultado:** superada  
**Fecha:** 2026-10-14 · **Versión del código:** git:af9dae0  
**Comando:** `sinpop validate --phase 0`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G0.1 | pytest se ejecuta sin errores | ✅ | 43 passed in 2.15s | 0 fallos |
| G0.2 | Las configuraciones pasan la validación de esquema | ✅ | 10/10 válidas | 10/10 |
| G0.3 | test_no_leakage.py existe y detecta accesos a los datos de evaluación | ✅ | 7 passed in 0.22s; 6 autotests del detector | existe y sus autotests pasan |
| G0.4 | `sinpop --help` muestra todos los comandos | ✅ | 11/11 comandos | 11/11 |
