# Puerta de la fase F8c

**Resultado:** superada  
**Fecha:** 2026-10-21 · **Versión del código:** git:f4fdf9b  
**Comando:** `sinpop validate --phase 8c`

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G8C.1 | Backtest temporal frente a la persistencia (V-TEMPORAL) | ✅ | modelo 1.90 pp frente a persistencia 2.29 pp (870 predicciones, 11 orígenes) | error medio del modelo < error medio de repetir el último valor (t+1 a t+3) |
| G8C.2 | Series de la población frente a las del CIS (V-TEMPORAL-SERIES) | ✅ | 1.57 pp en 1170 mes × categoría | diferencia absoluta media ≤ 2.0 pp |
| G8C.3 | Cada evento del banco tiene fecha, fuente y efecto con su incertidumbre | ✅ | 16/16 eventos con efecto e IC 95 %; sin fuente: 0 | todos los eventos |
