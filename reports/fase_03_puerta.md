# Puerta de la fase F3

**Resultado:** fallida  
**Fecha:** 2026-10-17 · **Versión del código:** git:e442556-dirty  
**Comando:** `sinpop validate --phase 3`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G3.1 | Las marginales suman el total oficial | ✅ | 75 territorios; fuera de umbral: 0 | < 0,1 % |
| G3.2 | Marginales coherentes entre cruces | ❌ | incoherencias: 432: CCAA:01 [residentes] relacion_actividad=jubilado_pensionista: diferencia relativa 2.81e-03; CCAA:01 [residentes] relacion_actividad=incapacidad_permanente: diferencia relativa 3.87e-03; CCAA:01 [residentes] relacion_actividad=otra_inactividad: diferencia relativa 1.04e-03 | diferencia relativa < 1e-6 (redondeo) |
| G3.3 | Las 19 comunidades suman España | ✅ | celdas distintas: 0 | |diferencia| < 0,001 personas |
| G3.4 | Ningún objetivo reservado se calibra (test automático) | ✅ | 17 calibrados, 11 reservados; ninguno repetido; test superado | 0 |
| G3.5 | Cada objetivo registra fuente, edición y fecha | ✅ | filas sin metadatos: 0 | 0 |
| G3.6 | Objetivos electorales al 100 % y coherentes con el derecho a voto | ✅ | censo de residentes 2023 frente a españoles 18+ 2026: España -1.46 %, máximo PROV:19 -4.02 %; incidencias: 0 | 100 % y diferencia < 5 % |
