# Puerta de la fase F7

**Resultado:** fallida  
**Fecha:** 2026-10-20 · **Versión del código:** git:e911ae6-dirty  
**Comando:** `sinpop validate --phase 7`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G7.1 | Grupos vigilados dentro de su rango de representación (V-MINORIAS) | ✅ | 777 grupos × población; fuera en estricto: 42; aceptados como limitación (D-059): 42; fuera: 0  | ratio en [0,9; 1,1] si el esperado es ≥ 200; si no, IC 95 % de MAS (o IC de la encuesta) |
| G7.2 | Diversidad dentro de grupos (V-DIVERSIDAD) | ✅ | 216 atributo × población; fuera: 0 | entropía ≥ 0,9 × la de los donantes ponderados en ≥ 95 % de los grupos (≥ 100 personas) |
| G7.3 | Concentración de donantes por grupo (V-CONCENTRACION) | ❌ | 810 grupos × población; fuera en estricto: 170; aceptados como limitación (D-059): 168; fuera: 2 [('PROV:42', 'jovenes_ni_ni'), ('PROV:44', 'jovenes_ni_ni')] | 5 donantes más usados ≤ 20 %; donantes distintos ≥ mín(50, tamaño / 3) |
| G7.4 | Perfil interno de cada grupo frente al oficial (V-MINORIAS-PERFIL) | ❌ | 777 grupos × población; fuera en estricto: 83; aceptados como limitación (D-059): 80; fuera: 3 [('CCAA:07', 'limitacion_grave'), ('PROV:42', 'limitacion_grave'), ('PROV:04', 'jovenes_ni_ni')] | TVD ≤ 0,08 en sexo, edad, estudios y actividad, donde hay referencia |
| G7.5 | Combinaciones de atributos P0 sin donante (V-RAREZA) | ❌ | combinaciones nuevas: 560 | 0 con el método base |
| G7.6 | Sección de limitaciones con los grupos no observables (docs/06 §2) | ✅ | faltan: 0 | personas sin hogar, no empadronados, grupos étnicos, orientación sexual, identidad de género |
| G7.7 | Revisión humana: aprobación expresa de la población | ⏸️ | pendiente (reports/fase_07.md) | aprobación |
