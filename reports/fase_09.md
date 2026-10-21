# Fase 09 · Capa de predicción (sin modelo de lenguaje)

**Estado:** puerta automática **fallida** en G9.6 (modo evento). G9.2 (B2) y G9.7 quedan pendientes del modelo de lenguaje (D-069). F9 no tiene revisión humana obligatoria en `docs/04`, pero el fallo de G9.6 necesita una decisión humana (ver «Qué hace falta para cerrar la puerta»).
**Fecha:** 2026-10-21 · **Decisión:** D-069
**Comando para reproducir** (tras la cadena de `reports/fase_08c.md`):

```
python -c "from sinpop.predict import calibracion as C; C.construir()" \
  && python -m sinpop.evaluate.validacion && sinpop validate --phase 9
```

## Resumen

- **Predictor estadístico** (`src/sinpop/predict/`), sin LLM y con coste 0 €:
  - recupera preguntas análogas del banco del CIS (2.738 preguntas cerradas anteriores al corte);
  - alinea sus opciones sin inventar;
  - estima con tres métodos:
    - **sistema:** multinomial ponderada aplicada a 100.000 adultos sintéticos;
    - **B0:** historial de las análogas;
    - **B1:** perfil posestratificado.
- **Salidas** en el formato de `docs/03` §2.8 con intervalos del 80 % y del 95 %, desglose por subgrupo y comunidad, y preguntas similares.
  - Ejemplo de entrada: `preguntas/Q001_ejemplo.json`.
- **Ventana de validación:** barómetros de julio (3571) y septiembre (3577) de 2026, posteriores al corte. Solo los lee `src/sinpop/evaluate/` (regla 5).
  - 107 preguntas evaluables; otras 14 no tienen ninguna análoga alineable.
- **Hallazgo principal:** para lo que mide el CIS a escala nacional, el mejor predictor es el historial reciente de preguntas parecidas. La combinación aprendida da todo el peso a B0, y el modelo con la población empata con él. La población aporta:
  - el modo `total` (la población real, no la muestra del CIS);
  - los subgrupos;
  - los territorios sin muestra propia.

## Puerta de salida

| ID | Resultado | Valor |
| --- | --- | --- |
| G9.1 V-FORMATO | ✅ | 107/107 salidas válidas por esquema |
| G9.2 Sistema y baselines | ⏸️ | TVD media: medición CIS 0,067; B0 0,067; B1 0,066 (107 preguntas). B2 pendiente del LLM |
| G9.3 Coste | ✅ | 0 llamadas, 0 € |
| G9.4 V-REFORMULACION | ✅ | TVD máxima 0,0026 (umbral 0,03) |
| G9.5 V-COBERTURA | ✅ | IC80 0,76; IC95 0,95 (632 opciones) |
| G9.6 V-EVENTO | ❌ | 6/15 eventos con dirección correcta (14/26 evento × indicador); error de magnitud 4,3 pp |
| G9.7 Estereotipos de la IA | ⏸️ | No aplica sin modelo de lenguaje |

Puerta generada en `reports/fase_09_puerta.md`.

## Error por tipo de pregunta (TVD media, ventana de validación)

| Grupo | Preguntas | Medición CIS | B0 | B1 |
| --- | --- | --- | --- | --- |
| Todas | 107 | 0,067 | 0,067 | 0,066 |
| Recurrentes (mismo enunciado ya preguntado) | 86 | 0,049 | 0,049 | 0,048 |
| Nuevas | 21 | 0,143 | 0,143 | 0,140 |
| Políticas | 32 | 0,057 | 0,057 | 0,056 |

Subgrupos (edad, sexo, estudios, comunidad): sistema 0,077 frente a B1 0,074. Comunidades: 0,087 frente a 0,086.

Detalle por pregunta: `reports/fase_09/validacion_preguntas.csv`. *Backtest* de construcción (167 preguntas de abril a junio de 2026, antes del corte): `reports/fase_09/backtest_construccion.json`.

## Intervalos

- Calibración conformal en el *backtest* de construcción, por tramo de similitud de la mejor análoga, con σ ≥ 0,01:

  | Tramo | q80 | q95 |
  | --- | --- | --- |
  | 0-0,4 | 2,18 | 15,7 |
  | 0,4-0,7 | 1,51 | 3,18 |
  | 0,7-1 | 0,97 | 2,10 |

- En la validación, la cobertura queda dentro de los umbrales (IC80 0,76; IC95 0,95).

## G9.6: por qué falla el modo evento

- Sin modelo de lenguaje, el cambio que se predice es la media de los eventos del banco del mismo tipo y ámbito (dejando fuera el evento que se predice).
- 13 de los 16 eventos son de tipo `politico`, sobre todo elecciones. El tipo no dice qué partido gana o pierde, y el efecto sobre la cercanía a cada partido cambia de signo de una elección a otra.
  - Ejemplos: e005 (Galicia), e007 (Cataluña), e016.
- Hay aciertos donde el signo es estable entre eventos: la caída de «ninguno» en cercanía tras las elecciones, y «política» como problema.
- Varios «fallos» son efectos reales no significativos (el IC 95 % del cambio observado incluye 0: e003 ideología, e004 problema político, e013 y e014). Contarlos como fallos o aciertos es azar.
- No se ha ajustado el método a estos 15 eventos: con tan pocos casos, cualquier regla elegida mirando el resultado sería sobreajuste.

## Qué hace falta para cerrar la puerta (decisión humana)

1. **Información del evento que el tipo no tiene:** quién gana o pierde y en qué dirección. Es el primer caso en que un modelo de lenguaje aporta una ventaja real (D-069): leer la descripción del evento y proponer la dirección por partido. También podría darla un analista como parte de la pregunta.
   - Propuesta: un piloto pequeño con un modelo declarado en `configs/llm.yaml` (menos de 5 $ o un modelo local), con *backtest* sobre estos 16 eventos y la misma métrica.
2. **Definición de la métrica:** contar solo los pares evento × indicador cuyo efecto observado sea significativo. Cambiar la definición de V-EVENTO es relajar una puerta, así que no se ha hecho sin aprobación.

## Limitaciones

- **Preguntas sin precedentes:** cuando la similitud de la mejor análoga es < 0,4, ningún método acierta (TVD ≈ 0,24-0,29). Es el segundo caso candidato a un LLM.
- **Recuperación por TF-IDF:** los *embeddings* neuronales no se pueden descargar en este entorno.
- **Confianza:** la de las salidas es provisional; la sustituye el modelo de F10.
