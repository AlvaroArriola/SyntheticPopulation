# Ficha de datos · 2026-01-01_ES_1000000_s1

## Identificación
- Territorio: ES (pais)
- Tamaño: 999.974 personas. 398.469 hogares
- Modo: representativo
- Fecha de referencia: 2026-01-01 (datos con corte en junio de 2026)
- Semilla: 1 · Versión del código: git:e911ae6-dirty

## Fuentes
| Fuente | Edición | Uso |
| --- | --- | --- |
| censo2021_personas | Censo 2021, microdatos de hogares (muestra) | donantes / objetivos |
| ecv | ECV 2025 (INE) | enriquecimiento |
| epa | EPA 2T 2026 (INE) | enriquecimiento |
| tic_h | TIC-H 2025 (INE) | enriquecimiento |
| atlas_renta | Atlas de distribución de renta de los hogares 2023 (INE) | enriquecimiento |
| censo_anual | Censo Anual exhaustivo 2025 (INE) | enriquecimiento |

Objetivos de calibración: actividad_nacionalidad, actividad_tramo, edad5_sexo, edad5_sexo_colectivos, edad5_sexo_familiares, estado_civil_edad, estudios_edad, nacimiento_nacionalidad, nacionalidad, nacionalidad_edad, nacionalidad_top, nacionalidad_top_edad, nacionalidad_top_sexo, sin_estudios_edad, tamano_hogar, tipo_hogar, urbanizacion.

## Variables
| Variable | Prioridad | Fuente | % de valores por método |
| --- | --- | --- | --- |
| edad | P0 | censo / padron_continuo | observada 100.0 % |
| edad_5 | P0 | censo / padron_continuo | observada 100.0 % |
| edad_4 | P0 | censo / padron_continuo | observada 100.0 % |
| sexo | P0 | censo / padron_continuo | observada 100.0 % |
| nacionalidad_grupo | P0 | censo / padron_continuo | observada 99.2 %, modelada 0.8 % |
| nacionalidad_esp_ext | P1 | censo / encuestas | observada 99.2 %, modelada 0.8 % |
| nacionalidad_top | P1 | padron_continuo | observada 99.2 %, modelada 0.8 % |
| pais_nacimiento_grupo | P1 | censo / padron_continuo | observada 99.2 %, modelada 0.8 % |
| anio_llegada_espana | P2 | censo_anual | observada 99.2 %, modelada 0.8 % |
| estado_civil | P1 | censo_anual | observada 99.2 %, modelada 0.8 % |
| nivel_estudios | P0 | censo_anual | observada 99.2 %, modelada 0.8 % |
| estudios_3 | P0 | censo_anual | observada 99.2 %, modelada 0.8 % |
| relacion_actividad | P0 | censo_anual / epa | observada 99.1 %, modelada 0.9 % |
| ocupacion | P1 | censo_anual / epa | observada 99.2 %, modelada 0.8 % |
| sector_actividad | P2 | epa / censo | observada 99.2 %, modelada 0.8 % |
| situacion_profesional | P1 | epa / censo | observada 99.2 %, modelada 0.8 % |
| tipo_residencia | P0 | ecp | observada 100.0 % |
| relacion_persona_ref | P0 | censo2021 | observada 99.2 %, modelada 0.8 % |
| tipo_hogar | P0 | censo2021 | observada 99.2 %, modelada 0.8 % |
| tamano_hogar | P0 | censo2021 | observada 99.2 %, modelada 0.8 % |
| tamano_hogar_4 | P0 | ecp | observada 99.2 %, modelada 0.8 % |
| n_personas_hogar | — | — | observada 99.2 %, modelada 0.8 % |
| n_menores_hogar | P1 | censo2021 | observada 99.2 %, modelada 0.8 % |
| n_mayores_65_hogar | P1 | censo2021 | observada 99.2 %, modelada 0.8 % |
| n_mayores_80_hogar | P1 | censo2021 | observada 99.2 %, modelada 0.8 % |
| ccaa | P0 | censo | observada 94.5 %, modelada 5.5 % |
| provincia | P0 | censo | observada 94.5 %, modelada 5.5 % |
| municipio | P2 | padron_continuo | observada 93.8 %, modelada 6.2 % |
| tamano_municipio | P0 | censo / padron_continuo | observada 93.8 %, modelada 6.2 % |
| grado_urbanizacion | P0 | censo | observada 93.8 %, modelada 6.2 % |
| salud_autopercibida | P1 | ecv / encuesta_salud | emparejada 85.6 %, observada 13.6 %, extrapolada 0.7 % |
| discapacidad_limitacion | P1 | ecv / encuesta_salud | emparejada 85.6 %, observada 13.6 %, extrapolada 0.7 % |
| privacion_material | P1 | ecv | emparejada 85.6 %, observada 13.6 %, extrapolada 0.7 % |
| privacion_material_n | P1 | ecv | emparejada 85.6 %, observada 13.6 %, extrapolada 0.7 % |
| tipo_jornada | P2 | epa | observada 53.7 %, emparejada 46.0 %, extrapolada 0.3 % |
| sector_publico | P2 | epa | observada 53.7 %, emparejada 46.0 %, extrapolada 0.3 % |
| cursa_formacion | P2 | epa | observada 59.9 %, emparejada 39.6 %, extrapolada 0.5 % |
| uso_internet | P1 | tic_h | emparejada 85.6 %, observada 13.6 %, extrapolada 0.7 % |
| compra_online | P2 | tic_h | emparejada 85.6 %, observada 13.6 %, extrapolada 0.7 % |
| teletrabajo | P2 | epa / tic_h | emparejada 85.6 %, observada 13.6 %, extrapolada 0.7 % |
| renta_hogar_decil | P1 | ecv + atlas_renta | emparejada 99.2 %, observada 0.8 % |
| renta_hogar_decil_ccaa | P1 | ecv + atlas_renta | emparejada 99.2 %, observada 0.8 % |
| tenencia_vivienda | P1 | censo2021 / ecv | emparejada 99.2 %, observada 0.8 % |
| dificultad_fin_mes | P2 | ecv | emparejada 99.2 %, observada 0.8 % |
| vehiculo_hogar | P2 | ecv / censo2021 | emparejada 99.2 %, observada 0.8 % |
| ctx_renta_municipio | P1 | atlas_renta | observada 74.7 %, modelada 25.3 % |
| ctx_envejecimiento | P1 | padron_continuo | observada 74.7 %, modelada 25.3 % |

## Calidad
- Validación: F4, F5 y F6 superadas (`reports/fase_04.md`, `fase_05.md`, `fase_06.md`); auditoría de F7 en `reports/fase_07.md`.
- Donantes locales: 94.5 %
- Confianza esperada del territorio: alta (país)

## Grupos vigilados
| Grupo | Semáforo | Ratio | Sintética | Oficial | Peor TVD de perfil | Donantes | Top 5 | Referencia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Personas de 85 años o más | verde | 1,001 | 0,033 | 0,033 | 0,001 | 29393 | 0,00 | ECP 2026 (residentes por edad y sexo) |
| Personas de 65+ que viven solas | verde | 0,989 | 0,049 | 0,050 | — | 48352 | 0,00 | Censo 2021 (hogares unipersonales de 65+) sobre residentes en viviendas familiares ECP 2026 |
| Nacidos fuera de España con nacionalidad española | verde | 0,991 | 0,062 | 0,062 | 0,022 | 38635 | 0,00 | Censo Anual exhaustivo a 01/01/2025 (microdatos) |
| Residentes en Ceuta y Melilla | verde | 0,997 | 0,003 | 0,003 | — | 1102 | 0,02 | ECP 2026 (residentes por provincia) |
| Residentes en municipios de menos de 2.000 habitantes | verde | 1,029 | 0,056 | 0,055 | 0,009 | 25124 | 0,00 | Padrón 2025 (población por tamaño de municipio) |
| Residentes en islas no capitalinas | no_medible | — | — | — | — | None | — | Insularidad. No medible en la población base, porque los microdatos del Censo no identifican los municipios de menos de 10.000 habitantes; se puede construir como territorio por lista de municipios (F5) |
| Hogares monoparentales | verde | 1,000 | 0,118 | 0,118 | — | 45810 | 0,00 | Censo 2021 (tipo de hogar por tamaño) sobre hogares ECP 2026 |
| Personas de 16+ con limitación grave (GALI) | verde | 1,000 | 0,041 | 0,041 | 0,042 | 33642 | 0,00 | ECV 2025 (16+, viviendas familiares) |
| Jóvenes de 20 a 24 que ni estudian ni trabajan | verde | 1,002 | 0,115 | 0,115 | 0,031 | 5923 | 0,00 | EPA 2T 2026 (20-24, viviendas familiares) |
| Personas en paro (16+) | verde | 0,993 | 0,058 | 0,059 | 0,024 | 42500 | 0,00 | EPA 2T 2026 con el reparto del Censo Anual 2024 (objetivo actividad_sexo, D-046) |
| Personas de 15+ sin estudios (analfabetas o con primaria incompleta) | verde | 1,017 | 0,038 | 0,037 | 0,005 | 26776 | 0,00 | Censo Anual a 01/01/2024, tabla 66601 («Sin estudios», 15+) |
| Personas de 16+ en carencia material y social severa | rojo | 1,004 | 0,077 | 0,077 | 0,083 | 58285 | 0,00 | ECV 2025 (16+, viviendas familiares; vrMATSOCDEP) |
| Personas de 16+ que nunca usan internet | rojo | 1,115 | 0,092 | 0,083 | 0,015 | 69024 | 0,00 | TIC-H 2025 (16+, viviendas familiares) |
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

## Limitaciones conocidas
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
