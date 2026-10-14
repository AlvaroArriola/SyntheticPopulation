# Puerta de la fase F1

**Resultado:** fallida  
**Fecha:** 2026-10-14 · **Versión del código:** git:b367e7a-dirty  
**Comando:** `sinpop validate --phase 1`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G1.1 | Fuentes P0 descargadas y con hash verificado | ✅ | 5/5 | 5/5 |
| G1.2 | Cada fichero tiene su diseño de registro o documentación | ✅ | ok | todas las fuentes descargadas |
| G1.3 | Matriz de cobertura sin variables P0 sin fuente | ✅ | 15/15 P0 cubiertas | 15/15 |
| G1.4 | Registros leídos = registros declarados por la documentación | ❌ | 3/4 con cifra declarada coinciden; no coinciden: md_Censo_muestra_2023.txt; sin cifra exacta declarada: md_CensoPersonas_2021.parquet | igualdad exacta |
| G1.5 | Las 7 verificaciones críticas resueltas y registradas | ❌ | 5/7; pendientes: 6, 7 | 7/7 |
| G1.6 | Revisión humana del inventario | ⏸️ | pendiente | aprobación |
