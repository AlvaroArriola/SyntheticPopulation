# Fase 07 · Auditoría de sesgos y minorías

**Estado:** pendiente de revisión humana (G7.7)
**Fecha:** 2026-10-20 · **Versión del código:** git:6162e0f-dirty
**Comando para reproducir:** `python -m sinpop.validate.fase7 && python -m sinpop.validate.informe_f7 && sinpop validate --phase 7` (tras la cadena F3-F6 de `reports/fase_06.md`)

## Resumen
Se auditan la población nacional de 1.000.000 de personas y los 30 territorios de la serie de F5 con la lista de vigilancia (`configs/watchlist.yaml`): representación, perfil interno, concentración de donantes, diversidad dentro de grupos y combinaciones sin donante. La auditoría destapó desfases de los datos de entrada (D-049, D-050), que se corrigieron en origen y obligaron a repetir F3-F6. Los criterios para grupos pequeños incluyen el margen de muestreo (D-051) y, con referencia de encuesta, el error de la propia encuesta (D-052). La limitación grave y la carencia severa se llevan a la prevalencia de la ECV de cada comunidad (D-053), y los donantes de las celdas de extranjeros se amplían para no clonar sus pocos hogares (D-054).

## Puerta de salida
Ver `reports/fase_07_puerta.md` (`sinpop validate --phase 7`).

## Resultados principales

### Población nacional (2026-01-01_ES_1000000_s1)
| Grupo | Semáforo | Ratio | Sintética | Oficial | Peor TVD de perfil | Donantes | Top 5 | Referencia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Personas de 85 años o más | verde | 1,001 | 0,033 | 0,033 | 0,001 | 29393 | 0,00 | ECP 2026 (residentes por edad y sexo) |
| Personas de 65+ que viven solas | verde | 0,989 | 0,049 | 0,050 | — | 48352 | 0,00 | Censo 2021 (hogares unipersonales de 65+) sobre residentes en viviendas familiares ECP 2026 |
| Nacidos fuera de España con nacionalidad española | verde | 0,991 | 0,062 | 0,062 | 0,022 | 38635 | 0,00 | Censo Anual exhaustivo a 01/01/2025 (microdatos) |
| Residentes en Ceuta y Melilla | verde | 0,997 | 0,003 | 0,003 | — | 1102 | 0,02 | ECP 2026 (residentes por provincia) |
| Residentes en municipios de menos de 2.000 habitantes | verde | 1,029 | 0,056 | 0,055 | 0,009 | 25124 | 0,00 | Padrón 2025 (población por tamaño de municipio) |
| Residentes en islas no capitalinas | no_medible | — | — | — | — | None | — | Insularidad. No medible en la población base, porque los microdatos del Censo no identifican los municipios de menos de 10.000 habitantes; se puede construir como territorio por lista de municipios (F5) |
| Hogares monoparentales | verde | 1,000 | 0,118 | 0,118 | — | 45810 | 0,00 | Censo 2021 (tipo de hogar por tamaño) sobre hogares ECP 2026 |
| Personas de 16+ con limitación grave (GALI) | verde | 1,000 | 0,041 | 0,041 | 0,042 | 33633 | 0,00 | ECV 2025 (16+, viviendas familiares) |
| Jóvenes de 20 a 24 que ni estudian ni trabajan | verde | 1,004 | 0,115 | 0,115 | 0,030 | 5940 | 0,00 | EPA 2T 2026 (20-24, viviendas familiares) |
| Personas en paro (16+) | verde | 0,993 | 0,058 | 0,059 | 0,024 | 42500 | 0,00 | EPA 2T 2026 con el reparto del Censo Anual 2024 (objetivo actividad_sexo, D-046) |
| Personas de 15+ sin estudios (analfabetas o con primaria incompleta) | verde | 1,017 | 0,038 | 0,037 | 0,005 | 26776 | 0,00 | Censo Anual a 01/01/2024, tabla 66601 («Sin estudios», 15+) |
| Personas de 16+ en carencia material y social severa | rojo | 1,004 | 0,077 | 0,077 | 0,083 | 58280 | 0,00 | ECV 2025 (16+, viviendas familiares; vrMATSOCDEP) |
| Personas de 16+ que nunca usan internet | rojo | 1,115 | 0,092 | 0,083 | 0,015 | 69032 | 0,00 | TIC-H 2025 (16+, viviendas familiares) |
| Abstencionistas en las generales de 2023 | pendiente | — | — | — | — | None | — | capa politica (F8) |
| Votantes de partidos pequeños y regionalistas | pendiente | — | — | — | — | None | — | capa politica (F8) |
| Residentes sin derecho a voto en generales | pendiente | — | — | — | — | None | — | capa politica (F8) |
| Personas sin ubicación ideológica | pendiente | — | — | — | — | None | — | capa politica (F8) |
| Nacionalidad alemania | verde | 0,998 | 0,003 | 0,003 | 0,004 | 1867 | 0,02 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad argentina | verde | 1,000 | 0,003 | 0,003 | 0,006 | 1800 | 0,02 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad china | verde | 1,000 | 0,005 | 0,005 | 0,004 | 1553 | 0,01 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad colombia | ambar | 0,997 | 0,014 | 0,014 | 0,003 | 5849 | 0,01 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad ecuador | verde | 1,003 | 0,003 | 0,003 | 0,003 | 1737 | 0,02 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad francia | verde | 1,000 | 0,003 | 0,003 | 0,008 | 1821 | 0,02 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad honduras | verde | 0,998 | 0,004 | 0,004 | 0,003 | 1645 | 0,02 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad italia | verde | 0,999 | 0,007 | 0,007 | 0,003 | 4394 | 0,01 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad marruecos | verde | 0,997 | 0,020 | 0,020 | 0,003 | 8453 | 0,01 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad paraguay | verde | 0,995 | 0,003 | 0,003 | 0,010 | 1261 | 0,03 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad peru | ambar | 1,000 | 0,005 | 0,005 | 0,006 | 2274 | 0,03 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad reino_unido | verde | 1,002 | 0,006 | 0,006 | 0,004 | 3369 | 0,01 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad rumania | verde | 1,001 | 0,013 | 0,013 | 0,004 | 5382 | 0,01 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad ucrania | verde | 1,000 | 0,004 | 0,004 | 0,006 | 1601 | 0,02 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |
| Nacionalidad venezuela | verde | 1,000 | 0,008 | 0,008 | 0,003 | 3458 | 0,01 | Censo Anual exhaustivo 2025 sobre extranjeros ECP 2026 (nacionalidad_top) |

Diversidad dentro de grupos (V-DIVERSIDAD):
| Atributo | Grupos | Proporción dentro | Ratio mediano |  |
| --- | --- | --- | --- | --- |
| nacionalidad_grupo | 410 | 0,988 | 0,996 | ✅ |
| pais_nacimiento_grupo | 410 | 0,998 | 0,996 | ✅ |
| estado_civil | 410 | 0,998 | 0,998 | ✅ |
| nivel_estudios | 410 | 0,998 | 1,000 | ✅ |
| relacion_actividad | 410 | 0,998 | 0,999 | ✅ |
| ocupacion | 410 | 1,000 | 0,997 | ✅ |
| situacion_profesional | 410 | 0,993 | 1,000 | ✅ |
| tipo_hogar | 410 | 1,000 | 0,999 | ✅ |
| tamano_hogar | 410 | 1,000 | 0,999 | ✅ |
| grado_urbanizacion | 408 | 1,000 | 0,999 | ✅ |
| tamano_municipio | 408 | 0,998 | 0,999 | ✅ |

Combinaciones sin donante (V-RAREZA):
| Nivel | Combinaciones | Sin donante |
| --- | --- | --- |
| persona | 24607 | 0 |
| persona_y_hogar | 153546 | 0 |

### Semáforo por población
| Población | Verde | Ámbar | Rojo | Rojo por representación | Rojo por perfil | Rojo por concentración | Grupos en rojo (nacionalidades sin prefijo) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ES | 23 | 2 | 2 | 1 | 1 | 0 | privacion_severa, nunca_internet |
| CCAA:01 | 15 | 10 | 2 | 1 | 1 | 0 | privacion_severa, nunca_internet |
| CCAA:02 | 21 | 2 | 4 | 0 | 1 | 4 | argentina, honduras, paraguay, reino_unido |
| CCAA:03 | 17 | 3 | 7 | 0 | 1 | 7 | alemania, argentina, china, ecuador, honduras, reino_unido, ucrania |
| CCAA:04 | 17 | 9 | 1 | 0 | 0 | 1 | honduras |
| CCAA:05 | 21 | 1 | 5 | 1 | 1 | 4 | municipios_menos_2000, ecuador, honduras, paraguay, peru |
| CCAA:06 | 13 | 7 | 7 | 0 | 2 | 7 | argentina, china, ecuador, francia, honduras, italia, paraguay |
| CCAA:07 | 17 | 3 | 7 | 0 | 1 | 6 | limitacion_grave, alemania, argentina, francia, paraguay, reino_unido, ucrania |
| CCAA:08 | 22 | 3 | 2 | 0 | 0 | 2 | francia, reino_unido |
| CCAA:09 | 27 | 0 | 0 | 0 | 0 | 0 | — |
| CCAA:10 | 20 | 6 | 1 | 0 | 1 | 0 | privacion_severa |
| CCAA:11 | 15 | 6 | 6 | 0 | 0 | 6 | alemania, argentina, china, ecuador, honduras, paraguay |
| CCAA:12 | 18 | 3 | 6 | 0 | 0 | 6 | alemania, china, ecuador, honduras, paraguay, ucrania |
| CCAA:13 | 26 | 0 | 1 | 1 | 0 | 0 | municipios_menos_2000 |
| CCAA:14 | 18 | 8 | 1 | 0 | 1 | 0 | nunca_internet |
| CCAA:15 | 15 | 4 | 8 | 0 | 1 | 7 | alemania, argentina, francia, honduras, italia, paraguay, reino_unido, ucrania |
| CCAA:16 | 23 | 1 | 3 | 0 | 0 | 3 | alemania, china, ucrania |
| CCAA:17 | 14 | 3 | 10 | 0 | 3 | 10 | alemania, argentina, china, ecuador, francia, honduras, paraguay, peru, reino_unido, ucrania |
| CCAA:18 | 13 | 0 | 14 | 11 | 10 | 10 | alemania, argentina, china, colombia, ecuador, francia, honduras, italia, paraguay, peru, reino_unido, rumania, ucrania, venezuela |
| CCAA:19 | 12 | 0 | 15 | 9 | 14 | 13 | privacion_severa, alemania, argentina, china, colombia, ecuador, francia, honduras, italia, paraguay, peru, reino_unido, rumania, ucrania, venezuela |
| PROV:28 | 27 | 0 | 0 | 0 | 0 | 0 | — |
| PROV:08 | 26 | 0 | 1 | 0 | 1 | 0 | privacion_severa |
| PROV:42 | 7 | 0 | 20 | 1 | 14 | 16 | nacidos_fuera_espanoles, limitacion_grave, jovenes_ni_ni, sin_estudios, privacion_severa, alemania, argentina, china, colombia, ecuador, francia, honduras, italia, marruecos, paraguay, peru, reino_unido, rumania, ucrania, venezuela |
| PROV:44 | 12 | 0 | 15 | 1 | 9 | 14 | jovenes_ni_ni, alemania, argentina, china, colombia, ecuador, francia, honduras, italia, marruecos, paraguay, peru, reino_unido, ucrania, venezuela |
| PROV:04 | 15 | 6 | 6 | 0 | 3 | 3 | jovenes_ni_ni, privacion_severa, nunca_internet, china, honduras, venezuela |
| PROV:35 | 20 | 0 | 7 | 0 | 1 | 7 | china, ecuador, honduras, paraguay, peru, rumania, ucrania |
| PROV:20 | 16 | 0 | 11 | 0 | 0 | 11 | alemania, argentina, china, ecuador, francia, italia, paraguay, peru, reino_unido, ucrania, venezuela |
| PROV:32 | 11 | 2 | 14 | 1 | 1 | 13 | nunca_internet, alemania, argentina, china, ecuador, francia, honduras, italia, marruecos, paraguay, peru, reino_unido, rumania, ucrania |
| PROV:51 | 14 | 0 | 13 | 9 | 6 | 8 | alemania, argentina, china, colombia, ecuador, francia, italia, paraguay, peru, reino_unido, rumania, ucrania, venezuela |
| PROV:52 | 13 | 1 | 13 | 6 | 10 | 12 | alemania, argentina, china, colombia, ecuador, francia, italia, paraguay, peru, reino_unido, rumania, ucrania, venezuela |
| MUNIS:ejemplo_valencia_urbano | 24 | 0 | 3 | 0 | 2 | 1 | jovenes_ni_ni, privacion_severa, paraguay |
| MUNIS:ejemplo_teruel_rural | 1 | 9 | 17 | 8 | 0 | 13 | jovenes_ni_ni, nunca_internet, alemania, argentina, china, colombia, ecuador, francia, honduras, italia, marruecos, paraguay, peru, reino_unido, rumania, ucrania, venezuela |

Un grupo puede estar en rojo por más de un criterio.

Detalle por población en `reports/fase_07/` y ficha de datos de la población nacional en `reports/2026-01-01_ES_1000000_s1/ficha.md`.

## Decisiones tomadas
- D-049: la relación con la actividad, de la EPA 2T 2026, con la situación de inactividad por prioridad (SIDI1-3 y CURSR); nuevos objetivos «sin estudios» y nacidos fuera × nacionalidad; celdas sin donantes.
- D-050: estado civil y nacionalidad × edad calibrados; actividad por sexo, por nacionalidad y con 16-19 y 20-24 por separado; atributo `cursa_formacion` y jóvenes ni-ni de Eurostat; referencia de tipo de hogar × edad con tasas de jefatura; reglas de fusión para celdas sin solución; correcciones de código.
- D-051: márgenes de muestreo en V-MINORIAS-PERFIL, V-CONCENTRACION y V-DIVERSIDAD; limitaciones de composición; ampliación propia de los donantes de cada nacionalidad.
- D-052 (propuesta, pendiente de aprobación): en V-MINORIAS-PERFIL con referencia de encuesta, el margen cuenta también el error de muestreo de la encuesta (réplicas bootstrap).
- D-053: inclinación del bloque personal de la ECV por comunidad hasta la prevalencia de la ECV de la limitación grave y la carencia material y social severa.
- D-056 (propuesta): un fallo aislado de V-MARG en N = 10.000 es azar si no se repite en otra población de la serie.
- D-057: tamaño de municipio sorteado (no la clase más frecuente) para los hogares añadidos desde otra provincia; referencia local en V-DIVERSIDAD.
- D-058: el sexo de cada nacionalidad principal, calibrado al Censo Anual 2025 (los donantes de 2021 tenían, p. ej., un 69 % de mujeres paraguayas frente al 61 %).
- D-054: ampliación de los donantes de las celdas de extranjeros por edad y actividad, con vuelta atrás si el territorio no converge sin fundir nacionalidades. Se probó y descartó calibrar las nacionalidades desde 5 personas (empeoraba Teruel y Ceuta).

## Limitaciones
### Grupos no observables (docs/06 §2)

Ninguna fuente oficial de las usadas los identifica o los cubre. No se inventan: la población no
permite analizarlos.

- **Personas sin hogar.** La población parte de hogares y establecimientos colectivos
  empadronados. La Encuesta a las Personas sin Hogar del INE no está integrada.
- **Población no empadronada,** incluida parte de la población migrante en situación
  irregular. Los totales son los de la Estadística Continua de Población (ECP), que parte del
  Padrón.
- **Grupos étnicos** (por ejemplo, la población gitana), **orientación sexual** e
  **identidad de género**: no figuran en el Censo ni en las encuestas de referencia.
- **Residentes en establecimientos colectivos** (residencias, centros penitenciarios,
  religiosos…). Están en la población con sus atributos del Censo, pero las encuestas (ECV, EPA,
  TIC-H) no los cubren. Sus variables de encuesta están extrapoladas (`extrapolada`) desde los
  hogares con las mismas llaves, y las del hogar no proceden (NP).
- **Población de las islas no capitalinas:** no se puede medir aparte con las fuentes usadas
  (grupo `no_medible` de la lista de vigilancia).

### Diferencias de composición o de definición con las encuestas (D-048, D-051, D-053)

La población está calibrada al Censo Anual, a la ECP y a la EPA. Las variables de encuesta
heredan la medida de cada encuesta y su muestra ponderada no siempre tiene la misma
composición que las cifras oficiales:

- **Personas que nunca usan internet:** 9,2 % frente al 8,3 % de la TIC-H 2025 (ratio 1,11).
  Reponderada a la composición por edad × estudios de la TIC-H, el ratio baja a 1,04. El Censo
  Anual 2024 tiene más personas con estudios obligatorios o menos que la muestra ponderada de la
  TIC-H (25-34 años: 27,5 % frente a 15,5 %).
- **Limitación grave y carencia material y social severa:** la actividad de la población es la
  de la EPA y la de la ECV, la declarada, con menos incapacidad permanente y menos paro en la
  población. Por eso, sin corregir, la limitación grave salía hasta un 20 % por debajo de la ECV
  en algunas comunidades. Desde D-053, el bloque de la ECV se inclina en cada comunidad hasta la
  prevalencia de la ECV (como la renta con el Atlas). El perfil de actividad de la carencia severa
  sigue difiriendo de la ECV por la misma diferencia de definición del paro.
- **Tenencia de la vivienda, vehículo, tipo de jornada, sector público y teletrabajo:** sus
  marginales regionales difieren algo de las encuestas por patrones regionales o por la fecha de
  la encuesta (D-048).

### Desfase de los donantes de 2021

Los hogares donantes son los del Censo 2021. Lo que se calibra a 2026 refleja 2026:

- edad, sexo, nacionalidad (también por edad y por sexo), país de nacimiento, estudios,
  actividad (EPA, también por nacionalidad), estado civil, tamaño y tipo de hogar, y territorio.

El resto conserva la estructura de 2021 dentro de lo calibrado, por ejemplo la composición
detallada de los hogares o la ocupación.

### Grupos pequeños en territorios pequeños

Los donantes son la muestra del 10 % de los hogares del Censo 2021. Una población de N personas
de un territorio de P habitantes copia cada hogar donante unas N / (0,1 · P) veces:

| Territorio | N | Copias |
| --- | --- | --- |
| La Rioja | 100.000 | 3 |
| Teruel | 50.000 | 3,7 |
| Soria | 50.000 | 5,5 |
| Ceuta y Melilla | 100.000 | unas 12 (más personas que las reales) |

Las nacionalidades minoritarias de unas decenas de personas salen así de pocos hogares donantes,
copiados varias veces. Su número está calibrado, pero su variedad interna es menor que la real
(rojo por concentración en la tabla por territorio).

D-051 y D-054 amplían con hogares de comunidades parecidas los donantes de las nacionalidades
y de las celdas de extranjeros que más han crecido desde 2021 (más grupos en ámbar por donantes
no locales). En las provincias rurales pequeñas y en Ceuta y Melilla, esa ampliación impide que
la calibración converja sin fundir nacionalidades, y se calibran sin ella.

Además, en Ceuta, Melilla y Teruel las nacionalidades con menos de 100 personas en la población
se calibran dentro de «otras extranjeras», y su número puede alejarse de la cifra oficial.

Estos grupos no deben analizarse por separado en esos territorios. Para estudiarlos conviene usar
la población nacional o la de su comunidad.

### Capas pendientes

Las capas de opinión (F8A) y política (F8B) aún no existen. Los grupos de la lista de vigilancia
que dependen de ellas figuran como `pendiente`.

## Límites de uso
- La población describe **distribuciones**, no personas. No se debe usar para tomar decisiones
  sobre individuos reales.
- No sustituye a una encuesta cuando la decisión es crítica o afecta a derechos de las personas.
- No debe usarse para dirigir acciones a grupos vulnerables sin una validación específica para
  ese grupo.
- Los grupos marcados en ámbar o rojo, y los no observables, no deben analizarse por separado
  sin advertir de su baja fiabilidad.
- Las estimaciones por provincia o municipio tienen una confianza menor que las nacionales y
  autonómicas, y así debe comunicarse.

## Problemas abiertos y riesgos
- Los grupos en rojo o ámbar de la tabla por población (casi todos, nacionalidades minoritarias en territorios pequeños) no deben analizarse por separado.
- Las capas de opinión y política (F8) se apoyarán en esta población: sus sesgos se heredan.

## Qué necesita revisión humana
1. ¿Se aprueba la población (G7.7) con las limitaciones de esta sección?
2. ¿Se aprueban D-049 y D-050, en vigor y pendientes de aprobación expresa en esta revisión?
3. ¿Se aprueba D-052 (umbral de perfil con el error de la encuesta de referencia)? Es un cambio de criterio aplicado de forma provisional: sin él, los grupos de encuesta vuelven a rojo en casi todas las comunidades por el ruido de la propia encuesta.
4. ¿Se aprueba D-056? G4.1 falla en 1 de 8.480 comprobaciones: el tipo de residencia de Navarra (139 personas) en una de las cinco poblaciones de 10.000; no se repite en otra semilla ni en otro tamaño.
5. Con D-058, G6.1 falla en estricto por la tenencia de la vivienda (TVD con la composición de la encuesta 0,0206, criterio de D-048 ≤ 0,02). ¿Se acepta como limitación o se vuelve a la versión sin D-058 (commit b9ec7a2)?
6. Si quedan grupos en rojo en territorios pequeños, ¿se aceptan como limitación declarada o se exige otra medida correctora?
