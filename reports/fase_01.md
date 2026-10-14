# Fase 01 · Inventario y adquisición de datos

**Estado:** fallida (bloqueada por falta de acceso a las fuentes) · pendiente de decisión humana
**Fecha:** 2026-10-14 · **Versión del código:** git:af9dae0
**Comando para reproducir:** `sinpop ingest --verify && sinpop validate --phase 1`

## Resumen

La infraestructura de F1 está lista: catálogo de 24 fuentes en `configs/sources.yaml`, ingesta que solo admite dominios oficiales, manifiesto `data/raw/MANIFEST.yaml` con SHA-256, registro de ficheros colocados a mano y verificación de hashes, y la puerta F1 automatizada. **No se ha podido descargar ninguna fuente**: la política de red del entorno deniega `www.ine.es`, `servicios.ine.es`, `www.cis.es`, `infoelectoral.interior.gob.es`, `www.europeansocialsurvey.org`, `ess.sikt.no`, `www.sanidad.gob.es`, `ec.europa.eu`, `ceo.gencat.cat` y `www.ehu.eus` (D-014). Siguiendo `CLAUDE.md`, no se han buscado copias en sitios no oficiales y todas las fuentes figuran en `data/raw/MANUAL_DOWNLOADS.md`. Las tablas de este informe son el **plan** que se contrastará con la documentación oficial; ninguna cifra procede aún de los datos.

## Puerta de salida

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G1.1 | Fuentes P0 descargadas con hash verificado | ❌ | 0/7 | 7/7 |
| G1.2 | Documentación (diseño de registro) de cada fichero | ❌ | sin ficheros | todas |
| G1.3 | Matriz de cobertura sin variables P0 sin fuente | ❌ | 0/15 | 15/15 |
| G1.4 | Registros leídos = declarados | ❌ | sin ficheros | igualdad exacta |
| G1.5 | 7 verificaciones críticas resueltas | ❌ | 0/7 | 7/7 |
| G1.6 | Revisión humana | ⏸️ | pendiente | aprobación |

Detalle automático: [`fase_01_puerta.md`](fase_01_puerta.md).

## Verificaciones críticas (G1.5)

| # | Verificación | Estado | Plan alternativo documentado (docs/04, riesgos) |
| --- | --- | --- | --- |
| 1 | Nivel geográfico de los microdatos del Censo 2021 y del Censo Anual | pendiente | Si no hay provincia: donantes por CCAA × tamaño de municipio y calibración a objetivos provinciales del Padrón |
| 2 | Cobertura de establecimientos colectivos en la muestra de hogares del Censo 2021 | pendiente | Módulo aparte con tablas del Censo 2021 o limitación declarada |
| 3 | Universo de edad de la TIC-H en la última edición | pendiente | Tratamiento específico de 75+ marcado en `__calidad` |
| 4 | Publicación de la ronda 12 de la ESS | pendiente | Usar la ronda 11 |
| 5 | Edición más reciente con microdatos de la encuesta de salud | pendiente | — |
| 6 | Fuentes electorales (generales 2023, europeas 2024, autonómicas, censo electoral, estudios pre/postelectorales del CIS) | pendiente | — |
| 7 | Variables políticas y de valores en cada barómetro y su codificación | pendiente | Excluir estudios no armonizables |

## Inventario previsto por fuente

| Fuente | Capa | Prioridad | Unidad | Universo (plan) | Peso | Nivel geográfico (plan) | Edición | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `padron_continuo` | A | P0 | territorio | población residente empadronada | verificar | municipio | verificar | ❌ no descargada |
| `censo_anual_tablas` | A | P0 | territorio | población residente | verificar | verificar | verificar | ❌ no descargada |
| `censo_anual_micro_demograficas` | A | P0 | persona | toda la población residente | verificar | verificar | verificar | ❌ no descargada |
| `censo2021_tablas` | A | P0 | territorio | población residente y hogares | verificar | municipio y sección censal | 2021 | ❌ no descargada |
| `atlas_renta` | A | P1 | territorio | hogares | verificar | municipio, distrito y sección censal | verificar | ❌ no descargada |
| `degurba` | A | P0 | territorio | municipios | verificar | municipio | verificar | ❌ no descargada |
| `censo2021_micro_hogares` | B | P0 | persona_y_hogar | personas en hogares (verificar establecimientos colectivos) | verificar | verificar | 2021 | ❌ no descargada |
| `censo_anual_micro_completo` | B | P0 | persona | población residente | verificar | verificar | verificar | ❌ no descargada |
| `censo2021_micro_viviendas` | B | P1 | vivienda | viviendas | verificar | verificar | 2021 | ❌ no descargada |
| `ecv` | C | P1 | persona_y_hogar | hogares privados y sus miembros (16+ para el cuestionario individual) | verificar | CCAA | verificar | ❌ no descargada |
| `epa` | C | P1 | persona | población en viviendas familiares (16+ para actividad) | verificar | provincia (verificar) | verificar | ❌ no descargada |
| `tic_h` | C | P1 | persona_y_hogar | 16-74 (verificar ampliación a 75+) | verificar | CCAA | verificar | ❌ no descargada |
| `epf` | C | P2 | hogar | hogares privados | verificar | CCAA | verificar | ❌ no descargada |
| `encuesta_salud` | C | P1 | persona | población en viviendas familiares (15+ verificar) | verificar | CCAA | verificar | ❌ no descargada |
| `encuesta_sin_hogar` | C | P2 | persona | personas sin hogar usuarias de centros | verificar | verificar | verificar | ❌ no descargada |
| `cis_barometros` | C | P3 | persona | población residente de 18 años o más | verificar | CCAA y tamaño de municipio | verificar | ❌ no descargada |
| `cis_barometro_sanitario_2026` | C | P3 | persona | población residente de 18 años o más | verificar | CCAA | 2026 | ❌ no descargada |
| `ess` | C | P3 | persona | población residente de 15 años o más | verificar | NUTS2 | R11 | ❌ no descargada |
| `infoelectoral_resultados` | A-POL | P3-POL | mesa | censo electoral (CER y CERA) | verificar | mesa, municipio, provincia | verificar | ❌ no descargada |
| `resultados_autonomicas` | A-POL | P3-POL | mesa | censo electoral autonómico | verificar | verificar | verificar | ❌ no descargada |
| `censo_electoral` | A-POL | P3-POL | territorio | electores (incluidos extranjeros con derecho en municipales y europeas) | verificar | municipio y sección | verificar | ❌ no descargada |
| `cis_electorales` | A-POL | P3-POL | persona | población con derecho a voto | verificar | provincia (preelectorales de generales) | verificar | ❌ no descargada |
| `centros_autonomicos` | A-POL | P3-POL | persona | población residente de cada comunidad | verificar | CCAA y provincia | verificar | ❌ no descargada |
| `cis_series` | A-POL | P3-POL | territorio | población residente de 18 años o más | verificar | nacional | verificar | ❌ no descargada |

## Matriz de cobertura prevista (variables P0–P2)

Columna «Variable original» por verificar con el diseño de registro de cada fuente.

| Variable | Prioridad | Fuente prevista (docs/02) | Variable original | Estado |
| --- | --- | --- | --- | --- |
| `edad` | P0 | censo / padron_continuo | por verificar | sin fichero |
| `edad_5` | P0 | censo / padron_continuo | por verificar | sin fichero |
| `edad_4` | P0 | censo / padron_continuo | por verificar | sin fichero |
| `sexo` | P0 | censo / padron_continuo | por verificar | sin fichero |
| `nacionalidad_grupo` | P0 | censo / padron_continuo | por verificar | sin fichero |
| `pais_nacimiento_grupo` | P1 | censo / padron_continuo | por verificar | sin fichero |
| `nacionalidad_top` | P1 | padron_continuo | por verificar | sin fichero |
| `estado_civil` | P1 | censo_anual | por verificar | sin fichero |
| `nivel_estudios` | P0 | censo_anual | por verificar | sin fichero |
| `estudios_3` | P0 | censo_anual | por verificar | sin fichero |
| `relacion_actividad` | P0 | censo_anual / epa | por verificar | sin fichero |
| `ocupacion` | P1 | censo_anual / epa | por verificar | sin fichero |
| `sector_actividad` | P2 | epa / censo | por verificar | sin fichero |
| `situacion_profesional` | P1 | epa / censo | por verificar | sin fichero |
| `tipo_jornada` | P2 | epa | por verificar | sin fichero |
| `teletrabajo` | P2 | epa / tic_h | por verificar | sin fichero |
| `anio_llegada_espana` | P2 | censo_anual | por verificar | sin fichero |
| `discapacidad_limitacion` | P1 | ecv / encuesta_salud | por verificar | sin fichero |
| `salud_autopercibida` | P1 | ecv / encuesta_salud | por verificar | sin fichero |
| `uso_internet` | P1 | tic_h | por verificar | sin fichero |
| `competencias_digitales` | P2 | tic_h | por verificar | sin fichero |
| `compra_online` | P2 | tic_h | por verificar | sin fichero |
| `tipo_hogar` | P0 | censo2021 | por verificar | sin fichero |
| `tamano_hogar` | P0 | censo2021 | por verificar | sin fichero |
| `relacion_persona_ref` | P0 | censo2021 | por verificar | sin fichero |
| `n_menores_hogar` | P1 | censo2021 | por verificar | sin fichero |
| `n_mayores_65_hogar` | P1 | censo2021 | por verificar | sin fichero |
| `n_mayores_80_hogar` | P1 | censo2021 | por verificar | sin fichero |
| `tenencia_vivienda` | P1 | censo2021 / ecv | por verificar | sin fichero |
| `renta_hogar_decil` | P1 | ecv + atlas_renta | por verificar | sin fichero |
| `renta_hogar_decil_ccaa` | P1 | ecv + atlas_renta | por verificar | sin fichero |
| `privacion_material` | P1 | ecv | por verificar | sin fichero |
| `privacion_material_n` | P1 | ecv | por verificar | sin fichero |
| `dificultad_fin_mes` | P2 | ecv | por verificar | sin fichero |
| `vehiculo_hogar` | P2 | ecv / censo2021 | por verificar | sin fichero |
| `ccaa` | P0 | censo | por verificar | sin fichero |
| `provincia` | P0 | censo | por verificar | sin fichero |
| `tamano_municipio` | P0 | censo / padron_continuo | por verificar | sin fichero |
| `grado_urbanizacion` | P0 | censo | por verificar | sin fichero |
| `municipio` | P2 | padron_continuo | por verificar | sin fichero |
| `ctx_renta_municipio` | P1 | atlas_renta | por verificar | sin fichero |
| `ctx_envejecimiento` | P1 | padron_continuo | por verificar | sin fichero |
| `ctx_precio_vivienda` | P2 | pendiente | por verificar | sin fichero |

## Decisiones tomadas

- D-014 · Fuentes oficiales inaccesibles desde el entorno: descarga manual o ampliación de la red permitida (pendiente de decisión humana).

## Problemas abiertos y riesgos

- Sin datos no es posible ninguna fase posterior: F2 a F7 dependen de los microdatos del Censo 2021 y del Censo Anual y de las tablas del Padrón.
- El CIS y la ESS piden registro o aceptación de condiciones: aunque se abra la red, esas descargas serán manuales.

## Qué necesita revisión humana

1. **Acceso a las fuentes (D-014).** Elegir una vía:
   - añadir a *Allowed domains* de la red del entorno: `www.ine.es`, `servicios.ine.es`, `www.cis.es`, `infoelectoral.interior.gob.es`, `ess.sikt.no`, `www.europeansocialsurvey.org`, `www.sanidad.gob.es`, `ec.europa.eu` (DEGURBA), `ceo.gencat.cat`, `www.ehu.eus`; o
   - descargar los ficheros de `data/raw/MANUAL_DOWNLOADS.md` y colocarlos en `data/raw/<fuente>/<edicion>/` (como mínimo las 7 fuentes P0).
2. Aprobar o corregir las propuestas D-009, D-010, D-011 y D-012.
3. Cuando lleguen los datos, el agente completará el inventario, la matriz y las 7 verificaciones y volverá a pedir la revisión G1.6.
