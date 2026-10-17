# Puerta de la fase F5

**Resultado:** fallida  
**Fecha:** 2026-10-17 · **Versión del código:** git:09a145e-dirty  
**Comando:** `sinpop validate --phase 5`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G5.1 | Todos los territorios superan V-MARG y V-REGLAS | ✅ | 31 territorios, 419 marginales; fallos V-MARG: 0 ; con violaciones: 0 | 0 fallos de V-MARG y 0 violaciones de reglas duras |
| G5.2 | Cruces reservados por CCAA dentro de V-CRUCE (umbral territorial) | ❌ | 19 comunidades; fallos: 0 (máximo 0.0 %, CCAA:01); Cramér fuera: 6 [('CCAA:01', 'relacion_actividad × sexo'), ('CCAA:04', 'relacion_actividad × sexo'), ('CCAA:05', 'relacion_actividad × sexo')] | máx(1,2 × TVD_ref + 0,002, 0,05 / 0,08) (D-038 A); ≤ 5 % de fallos por población (D-039); |Δ V de Cramér| ≤ 0,03 |
| G5.3 | La agregación de las 19 comunidades reproduce la nacional (V-COHERENCIA) | ✅ | 22 comparaciones; fuera: 0; máxima edad5_sexo_colectivos 0.0090 | TVD ≤ 0,01 (calibradas) y ≤ 0,02 (reservadas) |
| G5.4 | Donantes no locales informados y tamaño efectivo mínimo (V-DONANTES) | ✅ | Kish mínimo 1183 (MUNIS:configs/territorios/ejemplo_teruel_rural.yaml); local mínimo 0.0 % (MUNIS:configs/territorios/ejemplo_teruel_rural.yaml); confianza reducida: ['MUNIS:configs/territorios/ejemplo_teruel_rural.yaml']; bajo el mínimo: 0 | Kish de los hogares donantes ≥ 200; proporción local informada |
| G5.5 | Ceuta, Melilla y 2+ provincias de < 150.000 habitantes, con su confianza | ✅ | PROV:51 (84,196 hab.): confianza media; PROV:52 (86,908 hab.): confianza media; PROV:42 (90,824 hab.): confianza media; PROV:44 (137,173 hab.): confianza media | generadas sin errores, con confianza declarada |
| G5.6 | Revisión humana del informe | ✅ | aprobada | aprobación |
