# Puerta de la fase F4

**Resultado:** superada  
**Fecha:** 2026-10-20 · **Versión del código:** git:6162e0f-dirty  
**Comando:** `sinpop validate --phase 4`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G4.1 | Marginales calibradas dentro del umbral ajustado al tamaño (V-MARG) | ✅ | 25 poblaciones, 8981 comprobaciones; fallos estrictos: 1 (2026-01-01_ES_10000_s1 CCAA:15 tipo_residencia (implícito) 0.0214>0.0189); repetidos en ≥ 2 poblaciones: 0 | TVD ≤ 1,2 × TVD_ref(N) + 0,002 (España y comunidades); fallo si la misma marginal queda fuera en ≥ 2 poblaciones de la serie (D-056) |
| G4.2 | Cruces reservados dentro de umbral (V-CRUCE) | ✅ | 12775 comprobaciones; fallos por azar: 63 (máximo por población 2.7 %, 2026-01-01_ES_10000_s3); sistemáticos: 0; excepciones aceptadas (D-038 B): 8; fallos Cramér: 0 | TVD ≤ máx(1,2 × TVD_ref + 0,002, 0,03 / 0,05 / 0,08) (D-038 A); por población ≤ 5 % de fallos y ningún cruce fallido en todas las semillas (D-039); |Δ V de Cramér| ≤ 0,03 |
| G4.3 | 0 violaciones de las reglas de coherencia duras (V-REGLAS) | ✅ | violaciones duras: 0; reglas blandas (informativo): 0 fuera con margen de muestreo, 31 fuera sin él | 0 |
| G4.4 | Diagnóstico de pesos dentro de umbral (V-PESOS) | ✅ | 19 bloques (logit); en rango mín 100.00 %; Kish/n mín 0.589; bloques fuera: 0 | desviación ≤ 0,1 %; ≥ 99 % de factores en [0,2; 5]; Kish/n ≥ 0,30; 0 pesos ≤ 0 |
| G4.5 | Variabilidad entre semillas dentro de lo esperado (V-SEMILLAS) | ✅ | 2635 proporciones; fuera (estricto): 2; repetidos en ≥ 2 tamaños: 0; razón media sd/sd_MAS máx 0.31 | sd entre 5 semillas ≤ 1.5 × sd de muestra aleatoria simple; fallo si la misma proporción lo supera en ≥ 2 tamaños (D-047) |
| G4.6 | Reproducibilidad: misma semilla, mismo hash (V-REPRO) | ✅ | 2026-01-01_ES_10000_s1: iguales (persons, households, lineage) | hashes iguales |
| G4.7 | Modo de sobremuestreo: estimaciones ponderadas dentro del error de muestreo | ✅ | edad>=85:10000: 9907 miembros (mínimo 10000); marginales fuera: 0 | TVD ponderada ≤ 1,2 × TVD_ref(n efectivo) + 0,002; mínimo alcanzado |
| G4.8 | Revisión humana del informe | ✅ | aprobada | aprobación |
