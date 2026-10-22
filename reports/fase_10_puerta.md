# Puerta de la fase F10

**Resultado:** superada  
**Fecha:** 2026-10-22 · **Versión del código:** git:93e0c98-dirty  
**Comando:** `sinpop validate --phase 10`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G10.1 | Correlación de rangos entre confianza y error real (V-CONF-CORR) | ✅ | 0.743 (2588 casos; confianza publicada: calibrado_en_validacion) | Spearman(confianza, −error) ≥ 0.4 |
| G10.2 | Error de calibración (V-CONF-ECE) | ✅ | 0.028 | ECE ≤ 0.05 (acierto: TVD ≤ 0.1) |
| G10.3 | La confianza baja con el tamaño del territorio y del subgrupo | ✅ | confianza media total 0.86, subgrupos 0.69; Spearman subgrupos 0.45, CCAA 0.33 | confianza total > subgrupos; Spearman(confianza, datos) > 0 en subgrupos y en CCAA |
