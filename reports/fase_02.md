# Fase 02 · Comprensión y armonización

**Estado:** pendiente de revisión humana (G2.8) y de decisión sobre G2.6
**Fecha:** 2026-10-15 · **Versión del código:** ver `fase_02_puerta.md`
**Comando para reproducir:**

```bash
sinpop harmonize --source all      # data/interim/*.parquet y data/interim/metadata.json
sinpop harmonize --check           # reports/fase_02_cifras_oficiales.{md,json} (G2.4)
sinpop harmonize --samples         # data/interim/muestras_g28/ (G2.8, solo en local)
sinpop validate --phase 2          # reports/fase_02_puerta.md
```

## Resumen

Todas las fuentes del núcleo y de enriquecimiento se leen con su diseño de registro y se armonizan a `configs/variables.yaml` en 17 ficheros de `data/interim/`. La armonización es determinista: dos ejecuciones desde cero dan ficheros con el mismo SHA-256. Se reproducen **111 cifras oficiales** de las 14 fuentes P0 y P1, todas dentro de tolerancia. No queda ningún valor fuera de dominio ni ningún código especial como número, y los totales ponderados se conservan exactamente. `partidos.yaml` asigna familia a las 72 candidaturas de las generales de 2023 y a todos los códigos de partido de los estudios 3567 y 3411 del CIS. Las 19 autonómicas se leen de sus boletines; 15 sin ninguna diferencia.

La puerta **no se supera** por G2.6: faltan los totales oficiales de las generales (el BOE no es accesible desde el entorno), faltan los resultados generales de Illes Balears y cuatro boletines autonómicos tienen descuadres en sus propias cifras. Además, varias decisiones (D-025 a D-031) necesitan aprobación.

## Puerta de salida

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G2.1 | Valores dentro del dominio declarado | ✅ | 137 columnas categóricas en 17 ficheros; 0 fuera de dominio | 0 |
| G2.2 | Ningún NS/NC/NP como valor numérico | ✅ | 0 | 0 |
| G2.3 | Totales ponderados conservados | ✅ | 14 totales; diferencia máxima 0 % | < 0,01 % |
| G2.4 | ≥3 cifras oficiales por fuente P0/P1 | ✅ | 14/14 fuentes; 111 cifras | ≥3 por fuente (tolerancias D-027, **por aprobar**) |
| G2.5 | Tests por tabla de recodificación | ✅ | 72 tablas, cada una con su test; 205 tests en total, 0 fallos | 1 por tabla, 0 fallos |
| G2.6 | Resultados electorales = totales oficiales | ❌ | generales: faltan los totales del BOE; autonómicas: 14/19 (ver abajo) | sin diferencias |
| G2.7 | Códigos de partido del CIS en `partidos.yaml` | ✅ | 0 sin asignar (138 en 3567, 113 en 3411) | 0 |
| G2.8 | Revisión humana de 20 registros por fuente | ⏸️ | muestras preparadas | aprobación |

Detalle automático: [`fase_02_puerta.md`](fase_02_puerta.md).

## Resultados principales

### Ficheros armonizados (`data/interim/`)

| Fichero | Filas | Fuente |
| --- | ---: | --- |
| `censo2021_personas` | 4.707.186 | Censo 2021, personas en viviendas familiares (con hogar y parentescos) |
| `censo_anual_muestra_2023` / `2024` / `2025` | 4.807.670 / 4.861.970 / 4.912.830 | Censo Anual, muestras del 10 % |
| `censo_anual_exhaustivo_2025` | 3.315.988 celdas (49.128.297 personas) | Censo Anual exhaustivo |
| `ecv` | 71.398 | ECV 2025 (con deciles de renta equivalente) |
| `epa` | 114.021 | EPA 2T2026 |
| `tic_h` | 16.938 | TIC-H 2025 |
| `encuesta_salud` | 21.032 | ESdE 2023 |
| `ecp_viviendas_familiares`, `ecp_total`, `ecp_colectivos`, `ecp_hogares` | 3.952, 10.504, 1.976, 208 | ECP a 01/01/2026 |
| `elecciones_generales_2023_municipios` / `_votos` | 8.131 / 90.389 | Congreso 2023, escrutinio provisional por municipio |
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

- **Generales 2023:** 8.131 municipios, cada uno con su código INE (16 renombrados resueltos a mano, D-029) y sin ningún descuadre interno. Censo de residentes 35.146.062; votantes 24.743.612. Los totales oficiales provinciales (BOE-A-2023-18907) no se pueden descargar: `www.boe.es` está bloqueado en la red del entorno.
- **Autonómicas** (D-031):

| Comunidad | Circunscripciones | Estado |
| --- | ---: | --- |
| Aragón, Asturias, Cantabria, Castilla y León, Castilla-La Mancha, Cataluña, C. Valenciana, Extremadura, Madrid, Navarra, País Vasco, La Rioja, Ceuta, Melilla | 3, 3, 1, 9, 5, 4, 3, 2, 1, 1, 3, 1, 1, 1 | ✅ sin diferencias (Navarra transcrita a mano; Asturias por OCR; C. Valenciana con el total de electores publicado erróneo, ver D-031) |
| Andalucía | 8 | ❌ el boletín descuadra en 3 votos (Granada) |
| Canarias | 8 | ❌ el boletín descuadra en 2 votos (El Hierro) |
| Galicia | 4 | ❌ el total publicado tiene 100 válidos de más |
| Región de Murcia | 1 | ❌ el boletín descuadra en 51 votantes |
| Illes Balears | 4 | ⏸️ solo voto CERA: faltan los resultados generales |

### Partidos (G2.7)

`configs/partidos.yaml` (D-030): 72 candidaturas de las generales de 2023 (5 izquierda estatal, 6 socialdemócrata, 1 centro-derecha, 1 derecha radical, 44 nacionalistas y regionalistas, 15 otros) y el catálogo completo de códigos de partido de los estudios 3567 y 3411 del CIS, con sus códigos especiales (blanco, nulo, no votó, no tenía edad, sin derecho, NS, NC) como opciones legítimas.

## Decisiones tomadas

- D-025 · Recodificaciones del Censo 2021 y del Censo Anual (grupos de país, top 15, tipo de hogar, tamaño de municipio con el Padrón 2025, 85-89 y 90+, universos).
- D-026 · Cuatro ocupados con ocupación en blanco → NC.
- D-027 · Tolerancias de G2.4, incluida la cota de cobertura del Censo 2021.
- D-028 · Armonización de ECV, EPA, TIC-H y ESdE.
- D-029 · Código INE de los municipios de las generales de 2023.
- D-030 · Familias de partidos y códigos del CIS.
- D-031 · Lectura de las autonómicas: descuadres, cifras no publicadas y transcripción de Navarra.

## Problemas abiertos y riesgos

1. **Totales oficiales de las generales:** se necesita `BOE-A-2023-18907.pdf` (y su corrección `BOE-A-2023-19537`) en `data/raw/infoelectoral_resultados/generales-2023/`, o permitir `www.boe.es` en la red del entorno. Además, las hojas municipales son del escrutinio **provisional** sin CERA: diferirán ligeramente del BOE (definitivo, con CERA).
2. **Illes Balears:** faltan los resultados generales de las autonómicas de 2023.
3. **Candidaturas autonómicas en `partidos.yaml`:** los resultados están cargados (795 filas), pero su familia se asignará con los criterios de D-030 una vez aprobados.
4. **Atlas de renta:** sigue faltando la tabla 30824 (límite de volumen de la API); dos tablas (31151, 31160) se descargaron sin metadatos por un error transitorio. No afecta a G2.4 y se resuelve en F6.
5. **Muestra del Censo 2021:** excluye los establecimientos colectivos (D-021): su sesgo de cobertura (≈ 0,8 %) se corrige en F4–F5 con el módulo de colectivos.

## Qué necesita revisión humana

1. **G2.8:** revisar a mano las muestras de `data/interim/muestras_g28/` (20 registros por fuente; guía en [`fase_02_muestras.md`](fase_02_muestras.md)). Están solo en local porque contienen microdatos originales.
2. **D-027:** ¿se aceptan las tolerancias, en particular la cota de cobertura para la muestra del Censo 2021?
3. **D-030:** ¿se aceptan los criterios de familia de partidos y las asignaciones dudosas (Na+, Valents, Compromís, confluencias municipales, las 18 siglas sin nombre completo verificado)?
4. **D-031:** ¿se aceptan los descuadres de los boletines de Andalucía, Canarias, Galicia y Murcia como diferencias de la fuente, y la transcripción manual de Navarra?
5. **G2.6:** ¿cómo se obtienen los totales del BOE y los resultados generales de Illes Balears? Mientras no estén, ¿se da la puerta por superada con esos dos huecos documentados o se espera?
6. D-025, D-026, D-028 y D-029: aprobación.
