# Puerta de la fase F7

**Resultado:** superada  
**Fecha:** 2026-10-21 · **Versión del código:** git:eada33e-dirty  
**Comando:** `sinpop validate --phase 7`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G7.1 | Grupos vigilados dentro de su rango de representación (V-MINORIAS) | ✅ | 819 grupos × población; fuera en estricto: 50; aceptados como limitación (D-059, D-061, D-062): 50; fuera: 0  | ratio en [0,9; 1,1] si el esperado es ≥ 200; si no, IC 95 % de MAS (o IC de la encuesta) |
| G7.2 | Diversidad dentro de grupos (V-DIVERSIDAD) | ✅ | 216 atributo × población; fuera: 0 | entropía ≥ 0,9 × la de los donantes ponderados en ≥ 95 % de los grupos (≥ 100 personas) |
| G7.3 | Concentración de donantes por grupo (V-CONCENTRACION) | ✅ | 864 grupos × población; fuera en estricto: 184; aceptados como limitación (D-059, D-061, D-062): 184; fuera: 0  | 5 donantes más usados ≤ 20 %; donantes distintos ≥ mín(50, tamaño / 3) |
| G7.4 | Perfil interno de cada grupo frente al oficial (V-MINORIAS-PERFIL) | ✅ | 819 grupos × población; fuera en estricto: 85; aceptados como limitación (D-059, D-061, D-062): 85; fuera: 0  | TVD ≤ 0,08 en sexo, edad, estudios y actividad, donde hay referencia |
| G7.5 | Combinaciones de atributos P0 sin donante (V-RAREZA) | ✅ | combinaciones nuevas: 0 | 0 con el método base |
| G7.6 | Sección de limitaciones con los grupos no observables (docs/06 §2) | ✅ | faltan: 0 | personas sin hogar, no empadronados, grupos étnicos, orientación sexual, identidad de género |
| G7.7 | Revisión humana: aprobación expresa de la población | ✅ | aprobada | aprobación |
