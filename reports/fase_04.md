# Fase 04 · Población nacional base

**Estado:** superada (G4.8 aprobada por el responsable el 16/10/2026, D-040)
**Fecha:** 2026-10-16 · **Versión del código:** ver `fase_04_puerta.md`
**Comando para reproducir:**

```bash
sinpop targets --territory all                     # objetivos (F3)
python -m sinpop.validate.fase4                    # 25 poblaciones, validación y tablas (≈ 2 h)
sinpop validate --phase 4                          # reports/fase_04_puerta.md
sinpop build --territory ES --size 100000 --seed 42   # una población cualquiera
sinpop validate --run 2026-01-01_ES_100000_s42        # su informe de validación
```

## Resumen

La población nacional base ya se genera para cualquier tamaño y semilla: hogares completos del Censo 2021, residentes en colectivos, 49,6 millones de residentes a 01/01/2026, calibrada por comunidades a las cifras de F3.

En 25 poblaciones de prueba (10.000 a 1.000.000 de personas, 5 semillas por tamaño):

- **V-MARG:** 0 fallos en 5.481 comprobaciones de marginales calibradas (España y comunidades).
- **V-REGLAS:** 0 violaciones de las reglas duras.
- **V-PESOS:** 100 % de los factores en [0,2; 5].
- **V-SEMILLAS:** variabilidad entre semillas ≤ 0,31 veces la de una muestra aleatoria simple (media).
- **V-REPRO:** misma semilla, mismo hash.
- **G4.7:** el sobremuestreo da estimaciones ponderadas dentro del error de muestreo.
- **V-RAREZA:** 0 combinaciones sin donante.
- **Minorías:** las 21 vigiladas que tienen referencia, representadas con ratio entre 0,99 y 1,04 y sin concentración de donantes.

**G4.2 (V-CRUCE)** se supera con los criterios que aprobó el responsable:

- umbral con el margen de V-MARG (D-038 A);
- Segovia como limitación aceptada de los datos (D-038 B);
- separación de azar y sesgo (D-039).

Quedan 59 fallos por azar en poblaciones de 10.000 a 100.000 personas, que no superan el 2,3 % de las comprobaciones de ninguna población, y ningún fallo sistemático. Con el criterio original habrían sido 207.

## Repetición con D-042 (16/10/2026)

En F5 se añadió el objetivo calibrado `nacionalidad_edad`, española/extranjera × edad quinquenal (D-042 A), y una excepción documentada para Ceuta en `tipo_hogar_edad4_ref` (D-042 C). Con esos cambios se repitió la serie de 25 poblaciones, y la puerta F4 se sigue superando (`fase_04_puerta.md`):

| Comprobación | Resultado |
| --- | --- |
| V-MARG | 0 fallos en 5.981 comprobaciones |
| V-CRUCE | 66 fallos por azar en 12.775 comprobaciones (máximo 2,3 % por población) y 0 sistemáticos |
| Excepciones (Segovia y Ceuta) | 14 |
| V de Cramér | 0 fallos |
| V-PESOS | Kish/n mínimo 0,836 |
| V-SEMILLAS | 0 fuera |
| V-REPRO | hashes iguales |
| G4.7 | 0 marginales fuera |

Las cifras de las secciones siguientes son las de la serie original.

## Repetición con la actividad de la EPA (D-046, 17/10/2026)

Con ocupados, parados e inactivos calibrados a la EPA del 2T 2026 y la corrección del grado de urbanización de las unidades importadas, la serie de 25 poblaciones (ya enriquecidas) supera de nuevo la puerta (`fase_04_puerta.md`). V-SEMILLAS tiene un fallo estricto por azar (mujeres de 35-39 en colectivos con N = 10.000) que no se repite en ningún otro tamaño (D-047).

## Cómo se construye la población

1. **Donantes.** Los 1.853.662 hogares de la muestra del Censo 2021 (4.707.186 personas), completos, más un módulo de **colectivos** (D-021): 386.003 residentes en establecimientos colectivos a 01/01/2026, representados por personas donantes de su misma provincia, sexo y edad quinquenal (atributos distintos de edad, sexo y territorio marcados `modelada`; sin `household_id`). La actividad, la ocupación, el sector y la situación profesional son NP por debajo de 16 años, como en las tablas oficiales (D-038.1).
2. **Calibración por comunidades** (D-038.2 y 3). España se calibra como la unión de sus 19 comunidades, cada una con sus objetivos de F3 y sus donantes. Método: **logit acotado** de Deville y Särndal (factores de ajuste en [0,2; 5]), resuelto por Newton. Objetivos calibrados: edad × sexo (viviendas familiares y colectivos), nacionalidad (7 grupos y 15 nacionalidades una a una), estudios × edad, actividad × sexo, grado de urbanización, tamaño y tipo de hogar. Los electorales se calibrarán en F8B sobre el recuerdo de voto.
3. **Ampliación de donantes** (D-038.5 y 6) cuando una comunidad no tiene donantes suficientes en una celda (sobre todo nacionalidades que han crecido mucho desde 2021, y Ceuta y Melilla), y fusión con «otras extranjeras» de las nacionalidades con menos de 100 personas en una comunidad.
4. **Integerización** (D-038.9): TRS con muestreo sistemático ordenado (estratificación implícita por comunidad, provincia, urbanización, tamaño de municipio, residencia, tipo y tamaño de hogar, nacionalidad y edad de la persona de referencia), seguido de un **equilibrado** que intercambia unidades del mismo tipo dentro de cada comunidad para acercar la muestra a los recuentos esperados de las celdas calibradas.
5. **Salidas** en `data/populations/<run_id>/`: `persons.parquet` (P0 y P1 del Censo, con `__calidad` por variable), `households.parquet`, `lineage.parquet` (donante de cada persona, aparte) y `metadata.json` (fuentes, configuración, semilla, hashes, método, equilibrado y referencia de las reglas blandas). Ninguna variable de opinión ni política (test de capas).
6. **Sobremuestreo** (`--oversample "edad>=85:2000"`): las unidades con miembros del grupo se multiplican por β y el resto por α, manteniendo el tamaño esperado; cada persona lleva `peso` = 1 / factor.

## Comparación de métodos de calibración

| | Raking | Logit acotado (elegido) |
| --- | --- | --- |
| Convergencia | sí (4-6 iteraciones) | sí (4-6 iteraciones) |
| Factores en [0,2; 5] | 99,90 %; Canarias 98,2 % (incumple V-PESOS) | 100 % en las 19 comunidades |
| Factor mínimo / máximo | 0,007 / 78 | 0,20 / 5,0 |
| Kish / n | 0,910 | 0,919 |
| TVD de los cruces reservados (pesos) | prácticamente iguales (diferencias < 0,0015) | |

Calibrar solo con marginales nacionales dejaba el reparto por provincias (reservado) en TVD 0,022; calibrando por comunidades, 0,006.

## Puerta de salida

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G4.1 | Marginales calibradas (V-MARG) | ✅ | 25 poblaciones, 5.481 comprobaciones, 0 fallos | TVD ≤ 1,2 × TVD_ref(N) + 0,002 |
| G4.2 | Cruces reservados (V-CRUCE) | ✅ | 59 fallos por azar de 12.775 (máx. 2,3 % por población), 0 sistemáticos; 12 excepciones de Segovia (D-038 B); V de Cramér: 0 fallos, Δ máx. 0,019 | máx(1,2 × TVD_ref + 0,002, 0,03 / 0,05 / 0,08); ≤ 5 % por población y ningún fallo en todas las semillas (D-039); Δ Cramér ≤ 0,03 |
| G4.3 | Reglas duras (V-REGLAS) | ✅ | 0 violaciones | 0 |
| G4.4 | Diagnóstico de pesos (V-PESOS) | ✅ | 19 comunidades; 100 % en rango; Kish/n ≥ 0,838 | ≥ 99 %; Kish/n ≥ 0,30 |
| G4.5 | Variabilidad entre semillas (V-SEMILLAS) | ✅ | 1.030 proporciones, 0 fuera | sd ≤ 1,5 × sd MAS |
| G4.6 | Reproducibilidad (V-REPRO) | ✅ | mismos hashes | iguales |
| G4.7 | Sobremuestreo | ✅ | 85+: 9.872 miembros (pedidos 10.000); 10 marginales ponderadas dentro | V-MARG con n efectivo |
| G4.8 | Revisión humana | ✅ | aprobada (D-040) | aprobación |

Detalle automático: [`fase_04_puerta.md`](fase_04_puerta.md). Todas las tablas: [`fase_04_validacion.md`](fase_04_validacion.md).

## Resultados principales

### Curva de error frente a tamaño (España; media de 5 semillas)

| N | TVD media, calibradas | TVD media, reservadas |
| ---: | ---: | ---: |
| 10.000 | 0,0266 | 0,0201 |
| 50.000 | 0,0092 | 0,0152 |
| 100.000 | 0,0043 | 0,0142 |
| 500.000 | 0,0016 | 0,0136 |
| 1.000.000 | 0,0010 | 0,0135 |

- **Calibradas:** el error de las marginales calibradas baja con el tamaño, como en una muestra aleatoria. Con 10.000 personas lo domina el módulo de colectivos (78 personas).
- **Reservadas:** el de los cruces reservados se estabiliza en 0,0135 a partir de 100.000 personas. Ese suelo no es ruido de muestreo; son diferencias de estructura entre los donantes de 2021 y las tablas de validación:
  - `tipo_hogar_edad4_ref` 0,029: la población envejece de 2021 a 2026;
  - `estado_civil_edad` 0,025;
  - `actividad_edad` 0,014.
- **Recomendación de tamaño:** 100.000 personas o más para análisis nacionales y por comunidad, y 500.000 o más para provincias pequeñas.

### Fallos de V-CRUCE por tamaño

| N | Fallos (de 2.555 comprobaciones, 5 semillas) | Con el margen propuesto |
| ---: | ---: | ---: |
| 10.000 | 137 | 46 |
| 50.000 | 47 | 14 |
| 100.000 | 16 | 5 |
| 500.000 | 3 | 2 |
| 1.000.000 | 4 | 4 |

Por objetivo, los fallos se concentran en `tamano_municipio` (81), `estado_civil_edad` (45) y `adultos_nacionalidad` (30), que son las variables que comparten todos los miembros de un hogar y por eso varían más al muestrear hogares completos. Con N ≥ 500.000 solo fallan Segovia (tamaño de municipio, sistemático: D-038 B) y, una vez, sus estudios por sexo y edad (justo en el límite).

### Calibración y donantes

- **Calibración:** logit acotado en las 19 comunidades, convergencia < 1e-8, 100 % de factores en [0,2; 5] y Kish/n entre 0,84 (Melilla) y 0,93.
- **Donantes ampliados:** solo en 17 celdas, sobre todo peruanos (5 comunidades) y ucranianos (Asturias y Galicia), además de Ceuta y Melilla. Proporción de donantes locales ≥ 99 % en todas las comunidades.
- **V-DONANTES:** tamaño efectivo de los hogares donantes usados de 303.378 para 1 millón de personas (umbral 200).

### Minorías (primera pasada; 1.000.000 de personas)

- **Representación:** ratio entre 0,986 (francesa) y 1,035 (mayores de 65 que viven solos) en los 21 grupos con referencia: mayores de 85, municipios de menos de 2.000 habitantes, parados, hogares monoparentales, mayores que viven solos, Ceuta y Melilla, y las 15 nacionalidades una a una.
- **Concentración de donantes:** ningún grupo depende de pocos hogares; los 5 donantes más usados aportan como mucho el 2,1 % del grupo.
- **Mayores que viven solos (1,035):** su referencia es la estructura de 2021, así que el exceso es coherente con el envejecimiento.
- **Grupos sin evaluar todavía**, porque no tienen referencia en F3 o pertenecen a otras capas: nacidos fuera con nacionalidad española, sin estudios, islas no capitalinas, limitación grave, ni-ni, privación y brecha digital. Se auditan en F6 y F7.

### Validación externa (no es puerta)

- **EPA 2T 2026:** hay menos ocupados en la población que en la EPA (47,7 % frente a 52,3 %), porque el objetivo calibrado es el Censo Anual a 01/01/2024 (D-038 C). Superan el doble del umbral Baleares (TVD 0,17, por la estacionalidad) y Ceuta (0,11, con una muestra EPA pequeña). El paro censal es mayor que el de la EPA en casi todas las comunidades, como se esperaba (actividad declarada frente a definición de la OIT).
- **ECV 2025 (personas por tamaño de hogar):** las 19 comunidades dentro.
- **Padrón 2022 (extranjeros por provincia):** las 52 provincias dentro. La población tiene más extranjeros, coherente con el crecimiento 2022-2026.

### Reglas blandas (informativo)

Con 1 millón de personas, las frecuencias de los casos raros (jubilados menores de 50, viudos menores de 30, casados menores de 20…) coinciden con las de los donantes calibrados. Con N pequeño superan a veces el 10 % por azar: 4 de 200 casos fuera aun con el margen de muestreo y 44 sin él.

## Decisiones tomadas

- D-038 · Síntesis de la población nacional base (método, calibración por comunidades, nacionalidades, ampliación de donantes, colectivos, integerización y equilibrado). Pendiente de aprobación.
- D-037 · Aprobada por el responsable (familias de las candidaturas autonómicas).

## Problemas abiertos y riesgos

1. **Fechas de las fuentes:**
   - Los donantes son de 2021.
   - Las estructuras de estudios, actividad y estado civil, de 2024.
   - La urbanización y la nacionalidad, de 2025.
   - Los efectivos, de 2026.

   La calibración corrige lo calibrado. Lo reservado conserva diferencias de fecha: el tipo de hogar por edad de la persona de referencia, y el tamaño de municipio en Segovia.
2. **Inmigración reciente:** los llegados después de 2021 se representan con residentes de su nacionalidad en 2021. El perfil por sexo y edad de cada nacionalidad se valida (`nacionalidad_top_sexo_edad`, TVD 0,012 con 1 millón).
3. **Colectivos:** sus atributos, salvo edad, sexo y territorio, son `modelada` (D-021). La ficha de cada población debe advertirlo.
4. **Recursos:** construir y validar una población de 1 millón requiere unos 8 GB de memoria; la calibración nacional, unos 3 minutos.
5. **Pendiente para F5:** V-COHERENCIA (las 19 poblaciones autonómicas frente a la nacional) y los territorios por municipios.

## Qué necesita revisión humana

Nada: F4 aprobada (D-040).
