# 05 · Validación

Este documento define **cómo se comprueba que cada fase ha terminado bien**: las métricas, los umbrales y las pruebas. Los identificadores `V-…` se usan en las puertas de `04_fases.md`.

> Los umbrales son **valores iniciales razonables**, no verdades. Se guardan en `configs/thresholds.yaml`. Si la evidencia demuestra que uno es inalcanzable o demasiado laxo, se propone el cambio en `DECISIONS.md` con datos y se pide aprobación humana. Nunca se cambian en silencio.

## 1. Principios

1. **Validar con lo que no se ha usado.** Reproducir lo calibrado es condición necesaria, no suficiente. La prueba de verdad son las distribuciones **reservadas** (`targets.yaml`) y las fuentes independientes.
2. **Umbrales ajustados al tamaño.** Una población de 10.000 personas tiene más ruido de muestreo que una de 1.000.000. El error se compara con el que tendría una muestra aleatoria perfecta del mismo tamaño.
3. **Por grupos, no solo en total.** Cada métrica se calcula para el total, por CCAA y para los grupos de la lista de vigilancia.
4. **Todo queda en un informe.** Cada validación escribe tablas y gráficos en `reports/<run_id>/` y un resumen de superada o fallida por comprobación.

## 2. Métricas

| Métrica | Definición | Uso |
| --- | --- | --- |
| **TVD** (distancia de variación total) | ½ Σ \|p_i − q_i\| entre la distribución sintética p y la objetivo q. Se interpreta como el porcentaje de población que habría que cambiar de categoría | Métrica principal para marginales y cruces |
| **SRMSE** (error cuadrático medio relativo estandarizado) | √(Σ (p_i − q_i)² / K) / (1/K), con K celdas | Complemento para tablas con muchas celdas |
| **Hellinger** | √(½ Σ (√p_i − √q_i)²) | Sensible a celdas pequeñas: útil para minorías |
| **Ratio de representación** | proporción sintética / proporción oficial de un grupo | Minorías |
| **V de Cramér** | Asociación entre dos variables categóricas | Conservación de relaciones |
| **Correlación de Spearman** | Asociación entre variables ordinales | Conservación de relaciones |
| **Tamaño efectivo de Kish** | (Σ w)² / Σ w² | Diagnóstico de pesos y de donantes |
| **TVD de referencia por muestreo, `TVD_ref(N)`** | Percentil 95 de la TVD entre la distribución objetivo y 200 muestras aleatorias simples de tamaño N extraídas de ella | Umbral ajustado al tamaño |
| **Entropía condicionada** | Entropía de un atributo dentro de un grupo | Diversidad |

Implementación: `src/sinpop/validate/metrics.py`, con tests que comparen cada métrica con casos calculados a mano.

## 3. Validación de datos (F1 y F2)

| ID | Comprobación | Umbral |
| --- | --- | --- |
| V-REGISTROS | Registros leídos frente a los declarados por la documentación | Igualdad exacta |
| V-DOMINIO | Valores fuera del dominio declarado | 0 |
| V-ESPECIALES | Códigos NS, NC o NP tratados como valores de escala | 0 |
| V-TOTALES | Total ponderado antes y después de armonizar | Diferencia < 0,01 % |
| V-OFICIALES | Cifras oficiales publicadas reproducidas con los microdatos (al menos 3 por fuente) | Dentro del redondeo de la publicación |

## 4. Validación de la población (F3, F4 y F5)

### V-MARG · Marginales calibradas

Para cada marginal calibrada del territorio:

> TVD(sintética, objetivo) ≤ 1,2 × TVD_ref(N) + 0,002

En la práctica, la población no puede alejarse de la cifra oficial más de lo que lo haría una muestra aleatoria perfecta del mismo tamaño, con un pequeño margen para la integerización.

### V-CRUCE · Cruces reservados

| Nivel | Umbral de TVD |
| --- | --- |
| España | ≤ máx(TVD_ref(N), 0,03) |
| Comunidad autónoma | ≤ máx(TVD_ref(N), 0,05) |
| Provincia | ≤ máx(TVD_ref(N), 0,08) |

Además, la V de Cramér de cada par de variables del cruce difiere de la oficial en ≤ 0,03.

### V-REGLAS · Coherencia interna

**Reglas duras** (0 violaciones permitidas):

- Cada hogar tiene exactamente una persona de referencia.
- `tamano_hogar` coincide con el número de personas del hogar.
- Diferencia de edad entre padre o madre e hijo de al menos 12 años.
- Nadie menor de 16 años figura como ocupado.
- Nadie menor de 19 años tiene estudios superiores terminados.
- `es_adulto` coincide con `edad >= 18`.
- Ninguna persona pertenece a más de un hogar.
- Las categorías de `tipo_hogar` son coherentes con las relaciones de parentesco del hogar.

**Reglas blandas** (casos raros pero posibles, como una persona jubilada de 45 años): la frecuencia en la población sintética no supera en más de un 10 % relativo la frecuencia ponderada en los donantes.

### V-PESOS · Diagnóstico de la calibración

| Comprobación | Umbral |
| --- | --- |
| Convergencia: desviación relativa máxima frente a los objetivos tras calibrar (antes de integerizar) | ≤ 0,1 % |
| Factores de ajuste (peso calibrado / peso original) en el rango [0,2; 5] | ≥ 99 % de los donantes |
| Tamaño efectivo de Kish / número de donantes | ≥ 0,30 |
| Pesos negativos o nulos en donantes usados | 0 |

### V-SEMILLAS · Estabilidad

Con 5 semillas por tamaño, la desviación típica entre semillas de cada proporción marginal es ≤ 1,5 × la desviación típica teórica de una muestra aleatoria simple de tamaño N.

### V-REPRO · Reproducibilidad

Misma configuración y misma semilla producen ficheros con el mismo hash SHA-256.

### V-COHERENCIA · Coherencia entre niveles territoriales

La combinación ponderada de las 19 poblaciones autonómicas frente a la nacional: TVD ≤ 0,01 en marginales calibradas y ≤ 0,02 en cruces reservados.

### V-DONANTES · Suficiencia de donantes por territorio

| Comprobación | Umbral |
| --- | --- |
| Tamaño efectivo de Kish de los hogares donantes usados | ≥ 200 |
| Porcentaje de donantes locales | Se informa siempre. Si < 50 %, el territorio se marca como «confianza reducida» |

### Curva de error frente a tamaño

No es una puerta, pero el informe de F4 debe incluirla: TVD media de marginales y cruces reservados para N = 10.000, 50.000, 100.000, 500.000 y 1.000.000. Sirve para recomendar el tamaño mínimo por tipo de uso.

### Validación externa (triangulación)

Comparar indicadores de la población con fuentes **no usadas para construirla**, al menos:

- tasa de actividad y de paro por CCAA frente a la EPA del trimestre de referencia;
- distribución de tipo de hogar por CCAA frente a la ECV;
- proporción de población extranjera por provincia frente al Padrón (si se calibró con el Censo Anual).

Las diferencias se informan y se explican. No son puerta, salvo que superen el doble del umbral de V-CRUCE, en cuyo caso se investigan antes de cerrar F5.

## 5. Validación del enriquecimiento (F6)

| ID | Comprobación | Umbral |
| --- | --- | --- |
| V-ENRIQ-MARG | Distribución de cada variable enriquecida frente a la encuesta de origen, por CCAA × edad_4 | En el intervalo de confianza del 95 % de la encuesta (bootstrap) en ≥ 90 % de las celdas; TVD nacional ≤ 0,02 |
| V-ENRIQ-ASOC | Asociación de cada variable enriquecida con cada variable llave | \|Δ V de Cramér\| o \|Δ Spearman\| ≤ 0,05 |
| V-ENRIQ-BLOQUE | Matriz de correlaciones dentro de cada bloque heredado | Máximo \|Δ\| ≤ 0,05; media ≤ 0,02 |
| V-ENRIQ-HOLDOUT | Emparejar sin una variable llave y comprobar si se recupera su asociación con la variable enriquecida | \|Δ V de Cramér\| ≤ 0,05 y mejor que el caso de independencia |

## 6. Auditoría de sesgos y minorías (F7)

Definición de grupos y procedimiento en `06_sesgos_y_minorias.md`.

| ID | Comprobación | Umbral |
| --- | --- | --- |
| V-MINORIAS | Ratio de representación de cada grupo vigilado | En [0,9; 1,1] si el recuento esperado es ≥ 200; si es menor, dentro del intervalo del 95 % de una muestra aleatoria simple |
| V-MINORIAS-PERFIL | Distribución de edad, sexo, estudios y actividad **dentro** de cada grupo vigilado frente a la oficial, si existe | TVD ≤ 0,08 |
| V-DIVERSIDAD | Entropía de cada atributo dentro de los grupos definidos por edad_4 × sexo × estudios_3 × CCAA, frente a la de los donantes ponderados | ≥ 0,9 × la de referencia en ≥ 95 % de los grupos con al menos 100 personas |
| V-CONCENTRACION | Para cada grupo vigilado: proporción de personas que proceden de los 5 hogares donantes más usados | ≤ 20 %; además, número de hogares donantes distintos ≥ mín(50, tamaño del grupo / 3) |
| V-RAREZA | Combinaciones de atributos P0 que no existen en ningún donante | 0 con el método base; con métodos generativos ≤ 0,1 % y revisadas una a una |

## 7. Validación de la capa de opinión y valores (F8A)

| ID | Comprobación | Umbral |
| --- | --- | --- |
| V-LATENTE | Ajuste del modelo de rasgos | Si es factorial confirmatorio: CFI ≥ 0,90 y RMSEA ≤ 0,08. Fiabilidad (omega) ≥ 0,70 por rasgo |
| V-OPINION-CV | Validación cruzada dejando fuera preguntas completas | TVD media menor que la del baseline B0 |
| V-DIVERSIDAD (rasgos) | Varianza de cada rasgo dentro de los grupos frente a la estimada en los datos reales | Ratio en [0,8; 1,2] |

## 8. Validación de la capa política (F8B)

La capa política tiene una ventaja que las demás no tienen: **los resultados electorales son una verdad oficial, completa y con detalle territorial**. Se aprovecha al máximo.

| ID | Comprobación | Umbral |
| --- | --- | --- |
| V-POL-RECUERDO | Distribución del recuerdo de voto de generales (familias, blanco, nulo, abstención) frente al resultado oficial, sobre la población con derecho a voto, por provincia o CCAA según se haya calibrado | TVD ≤ 1,2 × TVD_ref(N_electores) + 0,005 |
| V-POL-RESERVADA | Elección no usada para calibrar (por ejemplo, europeas de 2024) frente a su resultado oficial | TVD ≤ 0,04 nacional y ≤ 0,06 por CCAA; error de participación ≤ 3 puntos |
| V-POL-PERFIL | Composición de cada electorado (edad_4, sexo, estudios_3, tamaño de municipio) frente al postelectoral del CIS, ponderado | TVD ≤ 0,08 por electorado con al menos 300 casos en el CIS |
| V-POL-COHERENCIA | Autoubicación ideológica dentro de cada electorado frente al CIS | Media dentro de ± 0,3 puntos; desviación típica con ratio en [0,8; 1,2] |
| V-POL-TRANSFERENCIA | Matriz de transferencia generales → autonómicas (y → europeas) frente al CIS | TVD ≤ 0,10 por fila con al menos 200 casos |
| V-POL-SESGO | Pruebas de sesgo político (`06_sesgos_y_minorias.md`, sección 6) | Diversidad no política dentro de cada electorado con ratio de entropía ≥ 0,9; sin diferencias contrafactuales injustificadas |

**Importante:** el recuerdo de voto declarado en las encuestas está sesgado (menos abstención y más voto al ganador de lo real). Por eso el umbral se mide contra **resultados oficiales**, no contra el recuerdo del CIS. Contra el CIS se comparan solo los perfiles y las relaciones entre variables.

## 9. Validación de la dimensión temporal (F8C)

| ID | Comprobación | Umbral |
| --- | --- | --- |
| V-TEMPORAL | *Backtest*: error medio prediciendo indicadores de 1 a 3 meses después del último dato usado, frente a repetir el último valor (persistencia) | Error medio menor que el de la persistencia |
| V-TEMPORAL-SERIES | Series agregadas de la población frente a las series publicadas del CIS en el periodo de construcción | Diferencia absoluta media ≤ 2 puntos porcentuales |

## 10. Validación de predicción y confianza (F9 y F10)

| ID | Comprobación | Umbral |
| --- | --- | --- |
| V-FORMATO | Salida conforme al esquema de `03_arquitectura.md`, sección 2.8: distribución que suma 1, todas las opciones, NS/NC incluido, para total y subgrupos | 100 % de las salidas |
| V-REFORMULACION | TVD entre predicciones de una pregunta y de una reformulación neutra | ≤ 0,03 |
| V-COBERTURA | Proporción de casos en que el valor real cae dentro del intervalo | Intervalo del 80 %: entre 0,70 y 0,90. Intervalo del 95 %: entre 0,88 y 0,99 |
| V-EVENTO | Eventos pasados con datos antes y después: dirección del cambio y error de magnitud | Dirección correcta en al menos 2 de cada 3 eventos; magnitud informada |
| V-CONF-CORR | Correlación de Spearman entre el error predicho y el error real | ≥ 0,40 |
| V-CONF-ECE | Error de calibración esperado, definiendo la confianza como la probabilidad prevista de que la TVD sea ≤ 0,10 | ≤ 0,05 |

## 11. Tests automáticos mínimos

| Tipo | Qué cubren |
| --- | --- |
| Unitarios | Cada recodificación, cada métrica, la calibración en casos pequeños con solución conocida, la integerización |
| Por propiedades (hypothesis) | La calibración conserva los totales; la integerización conserva el tamaño N; el muestreo con semilla es determinista |
| Integración | Pipeline completo sobre un territorio pequeño en menos de 2 minutos; reproducibilidad por hash |
| Fuga de datos | `test_no_leakage.py` |
| Separación de capas | Ninguna variable política ni de opinión aparece en `persons.parquet` |
| Esquemas | Las entradas y salidas de preguntas y eventos cumplen su esquema JSON; las salidas del LLM se validan antes de usarse |
| Regresión | Las métricas de una población de referencia no empeoran entre versiones más allá de un 10 % relativo |

## 12. Informe de validación de cada población

`reports/<run_id>/validacion.md` incluye:

1. Resumen: superada o fallida, con la lista de comprobaciones.
2. Tabla de marginales calibradas: objetivo, sintético, TVD, umbral.
3. Tabla de cruces reservados.
4. Reglas de coherencia.
5. Diagnóstico de pesos y donantes.
6. Grupos vigilados.
7. Limitaciones conocidas del territorio.
8. Gráficos: pirámide de edad sintética frente a oficial; distribuciones principales; curva de error frente a tamaño (si aplica).
