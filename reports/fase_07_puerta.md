# Puerta de la fase F7

**Resultado:** fallida  
**Fecha:** 2026-10-20 · **Versión del código:** git:60b1978-dirty  
**Comando:** `sinpop validate --phase 7`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G7.1 | Grupos vigilados dentro de su rango de representación (V-MINORIAS) | ❌ | 819 grupos × población; fuera: 49 [('ES', 'nunca_internet'), ('CCAA:01', 'nunca_internet'), ('CCAA:05', 'municipios_menos_2000'), ('CCAA:14', 'municipios_menos_2000'), ('CCAA:18', 'nacionalidad_alemania'), ('CCAA:18', 'nacionalidad_ecuador')] | ratio en [0,9; 1,1] si el esperado es ≥ 200; si no, IC 95 % de MAS (o IC de la encuesta) |
| G7.2 | Diversidad dentro de grupos (V-DIVERSIDAD) | ❌ | 218 atributo × población; fuera: [('ES', 'tamano_municipio', 0.895), ('CCAA:04', 'tamano_municipio', 0.5), ('CCAA:14', 'tamano_municipio', 0.583), ('CCAA:15', 'tamano_municipio', 0.583), ('CCAA:17', 'tamano_municipio', 0.708), ('CCAA:18', 'tamano_municipio', 0.0), ('CCAA:19', 'tamano_municipio', 0.0)] | entropía ≥ 0,9 × la de los donantes ponderados en ≥ 95 % de los grupos (≥ 100 personas) |
| G7.3 | Concentración de donantes por grupo (V-CONCENTRACION) | ❌ | 864 grupos × población; fuera: 185 [('CCAA:02', 'nacionalidad_argentina'), ('CCAA:02', 'nacionalidad_honduras'), ('CCAA:02', 'nacionalidad_paraguay'), ('CCAA:02', 'nacionalidad_reino_unido'), ('CCAA:03', 'nacionalidad_alemania'), ('CCAA:03', 'nacionalidad_argentina')] | 5 donantes más usados ≤ 20 %; donantes distintos ≥ mín(50, tamaño / 3) |
| G7.4 | Perfil interno de cada grupo frente al oficial (V-MINORIAS-PERFIL) | ❌ | 819 grupos × población; fuera: 98 [('ES', 'privacion_severa'), ('ES', 'nacionalidad_paraguay'), ('CCAA:01', 'privacion_severa'), ('CCAA:02', 'nacionalidad_paraguay'), ('CCAA:03', 'nacionalidad_honduras'), ('CCAA:04', 'nacionalidad_paraguay')] | TVD ≤ 0,08 en sexo, edad, estudios y actividad, donde hay referencia |
| G7.5 | Combinaciones de atributos P0 sin donante (V-RAREZA) | ✅ | combinaciones nuevas: 0 | 0 con el método base |
| G7.6 | Sección de limitaciones con los grupos no observables (docs/06 §2) | ❌ | falta reports/fase_07.md | personas sin hogar, no empadronados, grupos étnicos, orientación sexual, identidad de género |
| G7.7 | Revisión humana: aprobación expresa de la población | ⏸️ | pendiente (reports/fase_07.md) | aprobación |
