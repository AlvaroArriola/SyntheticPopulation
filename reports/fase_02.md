# Fase 02 · Comprensión y armonización

**Estado:** superada (aprobada por el responsable el 2026-10-16, D-035)
**Fecha:** 2026-10-15 · **Versión del código:** ver `fase_02_puerta.md`
**Comando para reproducir:**

```bash
sinpop harmonize --source all      # data/interim/*.parquet y data/interim/metadata.json
sinpop harmonize --check           # reports/fase_02_cifras_oficiales.{md,json} (G2.4) y fase_02_calidad.md
sinpop harmonize --samples         # data/interim/muestras_g28/ (G2.8, solo en local)
sinpop validate --phase 2          # reports/fase_02_puerta.md
```

## Resumen

Todas las fuentes del núcleo y de enriquecimiento se leen con su diseño de registro y se armonizan a `configs/variables.yaml` en 17 ficheros de `data/interim/`. La armonización es determinista: dos ejecuciones desde cero dan ficheros con el mismo SHA-256. Se reproducen **111 cifras oficiales** de las 14 fuentes P0 y P1, todas dentro de tolerancia. No queda ningún valor fuera de dominio ni ningún código especial como número, y los totales ponderados se conservan exactamente. `partidos.yaml` asigna familia a las 72 candidaturas de las generales de 2023 y a todos los códigos de partido de los estudios 3567 y 3411 del CIS. Las 19 autonómicas se leen de sus boletines; 15 sin ninguna diferencia.

Segunda ronda (D-032), tras las decisiones del responsable: se cargan los resultados oficiales definitivos de las generales del BOE (cuadran con su «Total estatal»), se cierra el hueco de Illes Balears con el BOIB nº 78, la transcripción de Navarra queda confirmada por la web oficial, se explican los totales de la Comunitat Valenciana (Alicante) y de Galicia, y se descartan los 4 ocupados sin ocupación (D-026). **Todas las comprobaciones automáticas de la puerta se superan**; falta la revisión humana G2.8.

Tercera ronda (D-033, D-034), a raíz de la revisión G2.8: cada celda vacía de los ficheros armonizados tiene ahora un motivo y una condición exacta, comprobados por G2.1. Esta comprobación ha destapado y corregido dos errores: `edad_4` de la EPA en los menores de 16 y el universo del fichero de adultos de la ECV. El nuevo informe de calidad ([`fase_02_calidad.md`](fase_02_calidad.md)) ha detectado que, en la Encuesta de Salud, el código 99 de estudios agrupa sobre todo a quienes no terminaron primaria. Se recodifica con la evidencia de la tabla oficial 71335 (D-034, aprobada). El responsable revisa las muestras y aprueba la fase (D-035).

## Puerta de salida

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G2.1 | Dominio declarado y vacíos documentados | ✅ | 139 columnas categóricas en 19 ficheros; 0 fuera de dominio; 0 vacíos sin documentar | 0 y 0 |
| G2.2 | Ningún NS/NC/NP como valor numérico | ✅ | 0 | 0 |
| G2.3 | Totales ponderados conservados | ✅ | 14 totales; diferencia máxima 0 % | < 0,01 % |
| G2.4 | ≥3 cifras oficiales por fuente P0/P1 | ✅ | 14/14 fuentes; 114 cifras (incluido el nivel de estudios de la ESdE frente a la tabla 71335) | ≥3 por fuente (tolerancias D-027, aprobadas) |
| G2.5 | Tests por tabla de recodificación | ✅ | 72 tablas, cada una con su test; 214 tests en total, 0 fallos | 1 por tabla, 0 fallos |
| G2.6 | Resultados electorales = totales oficiales | ✅ | generales (BOE): 52 provincias, 59 candidaturas, 0 diferencias; autonómicas: 19/19 (descuadres de 4 boletines aceptados, D-031) | sin diferencias |
| G2.7 | Códigos de partido del CIS en `partidos.yaml` | ✅ | 0 sin asignar (138 en 3567, 113 en 3411) | 0 |
| G2.8 | Revisión humana de 20 registros por fuente | ✅ | aprobada por el responsable (D-035) | aprobación |

Detalle automático: [`fase_02_puerta.md`](fase_02_puerta.md).

## Resultados principales

### Ficheros armonizados (`data/interim/`)

| Fichero | Filas | Fuente |
| --- | ---: | --- |
| `censo2021_personas` | 4.707.186 | Censo 2021, personas en viviendas familiares (con hogar y parentescos) |
| `censo_anual_muestra_2023` / `2024` / `2025` | 4.807.666 / 4.861.970 / 4.912.830 | Censo Anual, muestras del 10 % (2023: 4 descartados, D-026) |
| `censo_anual_exhaustivo_2025` | 3.315.988 celdas (49.128.297 personas) | Censo Anual exhaustivo |
| `ecv` | 71.398 | ECV 2025 (con deciles de renta equivalente) |
| `epa` | 114.021 | EPA 2T2026 |
| `tic_h` | 16.938 | TIC-H 2025 |
| `encuesta_salud` | 21.032 | ESdE 2023 |
| `ecp_viviendas_familiares`, `ecp_total`, `ecp_colectivos`, `ecp_hogares` | 3.952, 10.504, 1.976, 208 | ECP a 01/01/2026 |
| `elecciones_generales_2023_provincias` / `_provincias_votos` | 52 / 550 | Congreso 2023, resultado oficial definitivo (BOE, con CERA) |
| `elecciones_generales_2023_municipios` / `_votos` | 8.131 / 90.389 | Congreso 2023, escrutinio provisional por municipio (residentes, sin CERA) |
| `elecciones_autonomicas_circunscripciones` / `_votos` | 63 / 795 | últimas autonómicas, por circunscripción |

`data/interim/metadata.json` guarda, para cada fichero, sus entradas con el SHA-256 del manifiesto, el SHA-256 de `variables.yaml`, la versión del código, la fecha y el SHA-256 de la salida.

### Cifras oficiales reproducidas (G2.4)

Detalle: [`fase_02_cifras_oficiales.md`](fase_02_cifras_oficiales.md).

| Fuente | Cifras | Ejemplos |
| --- | ---: | --- |
| `censo_anual_micro_demograficas` | 4 | población total, por sexo y por provincia: exactas |
| `censo_anual_micro_completo` | 31 | estudios, actividad, estado civil (2024) y ocupación (2023): dentro de 3 · EE |
| `censo2021_micro_hogares` | 21 | estudios, actividad, estado civil: dentro de 3 · EE + cobertura (D-027) |
| `censo2021_micro_viviendas` | 5 | total de viviendas, principales, propiedad y alquiler (nota de prensa) |
| `censo_anual_tablas`, `censo2021_tablas` | 6 + 6 | totales = suma de desagregaciones |
| `ecp` | 4 | familiares, total, colectivos y hogares: exactas |
| `padron_continuo` | 4 | 52 provincias y 8.132 municipios: exactos |
| `degurba` | 4 | población por grado de urbanización (tabla 79341): exacta |
| `atlas_renta` | 13 | renta neta media nacional, 6 provincias y 6 municipios de la nota de prensa: exactas |
| `epa` | 4 | ocupados, parados, tasa de paro, sector público |
| `ecv` | 3 | AROPE, carencia material severa, mucha dificultad |
| `tic_h` | 3 | uso de internet, uso diario, compra en línea |
| `encuesta_salud` | 3 | fumadores, enfermedad crónica, visita al médico de familia |

### Resultados electorales (G2.6)

- **Generales 2023, oficial (BOE-A-2023-18907):** 52 provincias, 59 candidaturas, 350 escaños; 37.469.458 electores y 24.952.447 votantes. Cada columna y cada partido reproducen el «Total estatal» publicado.
- **Generales 2023, detalle municipal (Interior, provisional, sin CERA):** 8.131 municipios con código INE (D-029), sin descuadres internos. Respecto al BOE faltan 2.323.396 electores (el CERA) y 208.835 votantes (CERA y escrutinio definitivo); es el voto de los residentes, el universo de la población sintética.
- **Autonómicas** (D-031, D-032): 19/19 comunidades.

| Comunidad | Circunscripciones | Notas |
| --- | ---: | --- |
| Andalucía | 8 | el BOJA descuadra en 3 votos (Granada): aceptado |
| Aragón | 3 | sin cifra de electores en el informe |
| Asturias | 3 | OCR con doble lectura y cifras en letra |
| Illes Balears | 4 | BOIB nº 78 (resultado general); CERA aparte |
| Canarias | 8 | 7 islas + circunscripción autonómica; el BOC descuadra en 2 votos (El Hierro): aceptado |
| Cantabria, Castilla-La Mancha, Cataluña, Extremadura, Madrid, País Vasco, La Rioja, Ceuta, Melilla | 1, 5, 4, 2, 1, 3, 1, 1, 1 | sin diferencias |
| Castilla y León | 9 | el BOCyL no publica votantes: se dejan vacíos |
| Comunitat Valenciana | 3 | el total de electores impreso omite Alicante: se deja vacío |
| Galicia | 4 | errata de 100 en los votos a candidaturas del total: aceptada |
| Región de Murcia | 1 | el BORM descuadra en 51 votantes: aceptado |
| Navarra | 1 | transcripción del BON confirmada por la web oficial |

### Partidos (G2.7)

`configs/partidos.yaml` (D-030, D-032): 72 candidaturas, con sus siglas en el BOE (`codigo_boe`) y su nombre completo, de las generales de 2023 (5 izquierda estatal, 6 socialdemócrata, 1 centro-derecha, 1 derecha radical, 44 nacionalistas y regionalistas, 15 otros) y el catálogo completo de códigos de partido de los estudios 3567 y 3411 del CIS, con sus códigos especiales (blanco, nulo, no votó, no tenía edad, sin derecho, NS, NC) como opciones legítimas.

## Decisiones tomadas

- D-025 · Recodificaciones del Censo 2021 y del Censo Anual (grupos de país, top 15, tipo de hogar, tamaño de municipio con el Padrón 2025, 85-89 y 90+, universos).
- D-026 · Cuatro ocupados con ocupación en blanco → NC.
- D-027 · Tolerancias de G2.4, incluida la cota de cobertura del Censo 2021.
- D-028 · Armonización de ECV, EPA, TIC-H y ESdE.
- D-029 · Código INE de los municipios de las generales de 2023.
- D-030 · Familias de partidos y códigos del CIS.
- D-031 · Lectura de las autonómicas: descuadres, cifras no publicadas y transcripción de Navarra.
- D-032 · Segunda ronda: BOE de las generales, Baleares, Navarra, Alicante y Galicia.

- D-033 · Celdas vacías documentadas e informe de calidad.
- D-034 · ESdE: el código 99 de NIVEST no es «no contesta».

- D-035 · Aprobación de F2.

D-025 y D-027 a D-035: aprobadas. D-026: aprobada con cambio (se descartan los 4 registros).

## Problemas abiertos y riesgos

1. **Atlas de renta:** falta la tabla 30824 (límite de volumen de la API) y dos tablas (31151, 31160) siguen sin metadatos por un error transitorio. No afecta a G2.4; se resuelve en F6, donde se usa.
2. **Muestra del Censo 2021:** excluye los establecimientos colectivos (D-021); su sesgo de cobertura (≈ 0,8 %) se corrige en F4–F5 con el módulo de colectivos.
3. **Candidaturas autonómicas en `partidos.yaml`:** los resultados están cargados (795 filas); su familia se asigna con los criterios aprobados de D-030 en F3, al construir los objetivos electorales.

## Qué necesita revisión humana

Nada: fase aprobada (D-035).
