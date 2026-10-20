# Puerta de la fase F7

**Resultado:** fallida  
**Fecha:** 2026-10-20 · **Versión del código:** git:402e437-dirty  
**Comando:** `sinpop validate --phase 7`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G7.1 | Grupos vigilados dentro de su rango de representación (V-MINORIAS) | ❌ | 819 grupos × población; fuera: 50 [('ES', 'nunca_internet'), ('CCAA:01', 'nunca_internet'), ('CCAA:05', 'municipios_menos_2000'), ('CCAA:13', 'municipios_menos_2000'), ('CCAA:18', 'nacionalidad_alemania'), ('CCAA:18', 'nacionalidad_ecuador')] | ratio en [0,9; 1,1] si el esperado es ≥ 200; si no, IC 95 % de MAS (o IC de la encuesta) |
| G7.2 | Diversidad dentro de grupos (V-DIVERSIDAD) | ✅ | 216 atributo × población; fuera: 0 | entropía ≥ 0,9 × la de los donantes ponderados en ≥ 95 % de los grupos (≥ 100 personas) |
| G7.3 | Concentración de donantes por grupo (V-CONCENTRACION) | ❌ | 864 grupos × población; fuera: 184 [('CCAA:02', 'nacionalidad_argentina'), ('CCAA:02', 'nacionalidad_honduras'), ('CCAA:02', 'nacionalidad_paraguay'), ('CCAA:02', 'nacionalidad_reino_unido'), ('CCAA:03', 'nacionalidad_alemania'), ('CCAA:03', 'nacionalidad_argentina')] | 5 donantes más usados ≤ 20 %; donantes distintos ≥ mín(50, tamaño / 3) |
| G7.4 | Perfil interno de cada grupo frente al oficial (V-MINORIAS-PERFIL) | ❌ | 819 grupos × población; fuera: 84 [('ES', 'privacion_severa'), ('CCAA:01', 'privacion_severa'), ('CCAA:02', 'nacionalidad_paraguay'), ('CCAA:03', 'nacionalidad_honduras'), ('CCAA:05', 'nacionalidad_paraguay'), ('CCAA:06', 'nacionalidad_francia')] | TVD ≤ 0,08 en sexo, edad, estudios y actividad, donde hay referencia |
| G7.5 | Combinaciones de atributos P0 sin donante (V-RAREZA) | ✅ | combinaciones nuevas: 0 | 0 con el método base |
| G7.6 | Sección de limitaciones con los grupos no observables (docs/06 §2) | ✅ | faltan: 0 | personas sin hogar, no empadronados, grupos étnicos, orientación sexual, identidad de género |
| G7.7 | Revisión humana: aprobación expresa de la población | ⏸️ | pendiente (reports/fase_07.md) | aprobación |
