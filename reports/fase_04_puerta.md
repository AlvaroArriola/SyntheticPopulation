# Puerta de la fase F4

**Resultado:** fallida  
**Fecha:** 2026-10-16 · **Versión del código:** git:4a8d978-dirty  
**Comando:** `sinpop validate --phase 4`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G4.1 | Marginales calibradas dentro del umbral ajustado al tamaño (V-MARG) | ✅ | 25 poblaciones, 5481 comprobaciones; fallos: 0 | TVD ≤ 1,2 × TVD_ref(N) + 0,002 (España y comunidades) |
| G4.2 | Cruces reservados dentro de umbral (V-CRUCE) | ❌ | 12775 comprobaciones; fallos TVD: 207 (2026-01-01_ES_10000_s1 CCAA:05 tamano_municipio 0.0799>0.0521; 2026-01-01_ES_10000_s1 CCAA:06 tamano_municipio 0.1184>0.1135; 2026-01-01_ES_10000_s1 CCAA:07 provincia_si_calibra_ccaa 0.0799>0.0731); con el margen propuesto en D-038: 71; fallos Cramér: 0 | TVD ≤ máx(TVD_ref, 0,03 / 0,05 / 0,08); |Δ V de Cramér| ≤ 0,03 (España) |
| G4.3 | 0 violaciones de las reglas de coherencia duras (V-REGLAS) | ✅ | violaciones duras: 0; reglas blandas (informativo): 4 fuera con margen de muestreo, 44 fuera sin él | 0 |
| G4.4 | Diagnóstico de pesos dentro de umbral (V-PESOS) | ✅ | 19 bloques (logit); en rango mín 100.00 %; Kish/n mín 0.838; bloques fuera: 0 | desviación ≤ 0,1 %; ≥ 99 % de factores en [0,2; 5]; Kish/n ≥ 0,30; 0 pesos ≤ 0 |
| G4.5 | Variabilidad entre semillas dentro de lo esperado (V-SEMILLAS) | ✅ | 1030 proporciones; fuera: 0; razón media sd/sd_MAS máx 0.31 | sd entre 5 semillas ≤ 1,5 × sd de muestra aleatoria simple |
| G4.6 | Reproducibilidad: misma semilla, mismo hash (V-REPRO) | ✅ | 2026-01-01_ES_10000_s1: iguales (persons, households, lineage) | hashes iguales |
| G4.7 | Modo de sobremuestreo: estimaciones ponderadas dentro del error de muestreo | ✅ | edad>=85:10000: 9872 miembros (mínimo 10000); marginales fuera: 0 | TVD ponderada ≤ 1,2 × TVD_ref(n efectivo) + 0,002; mínimo alcanzado |
| G4.8 | Revisión humana del informe | ⏸️ | pendiente (reports/fase_04.md) | aprobación |
