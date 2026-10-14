# Puerta de la fase F1

**Resultado:** fallida  
**Fecha:** 2026-10-14 · **Versión del código:** git:desconocida  
**Comando:** `sinpop validate --phase 1`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G1.1 | Fuentes P0 descargadas y con hash verificado | ❌ | 0/7; faltan: padron_continuo, censo_anual_tablas, censo_anual_micro_demograficas, censo2021_tablas, degurba, censo2021_micro_hogares, censo_anual_micro_completo | 7/7 |
| G1.2 | Cada fichero tiene su diseño de registro o documentación | ❌ | sin ficheros | todas las fuentes descargadas |
| G1.3 | Matriz de cobertura sin variables P0 sin fuente | ❌ | 0/15 P0 cubiertas | 15/15 |
| G1.4 | Registros leídos = registros declarados por la documentación | ❌ | sin ficheros que leer | igualdad exacta |
| G1.5 | Las 7 verificaciones críticas resueltas y registradas | ❌ | 0/7 (requieren los ficheros y su documentación) | 7/7 |
| G1.6 | Revisión humana del inventario | ⏸️ | pendiente | aprobación |
