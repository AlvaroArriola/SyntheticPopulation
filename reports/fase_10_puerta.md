# Puerta de la fase F10

**Resultado:** superada  
**Fecha:** 2026-10-23 · **Versión del código:** git:fab659d-dirty  
**Comando:** `sinpop validate --phase 10`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G10.1 | Correlación de rangos entre confianza y error real (V-CONF-CORR) | ✅ | 0.815 (2825 casos; confianza publicada: calibrado_en_validacion) | Spearman(confianza, −error) ≥ 0.4 |
| G10.2 | Error de calibración (V-CONF-ECE) | ✅ | 0.029 | ECE ≤ 0.05 (acierto: TVD ≤ 0.1) |
| G10.3 | La confianza baja con el tamaño del territorio y del subgrupo | ✅ | confianza media total 0.89, subgrupos 0.64; Spearman subgrupos 0.50, CCAA 0.40 | confianza total > subgrupos; Spearman(confianza, datos) > 0 en subgrupos y en CCAA |
