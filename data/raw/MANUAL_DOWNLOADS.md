# Descargas manuales

Ficheros que no se han podido descargar automáticamente (CLAUDE.md, «Descarga de datos»).

**Motivo (2026-10-14):** la política de red del entorno de ejecución deniega `www.ine.es`, `servicios.ine.es`, `www.cis.es`, `infoelectoral.interior.gob.es` y `www.europeansocialsurvey.org` (decisión D-014). Además, el CIS y la ESS piden registro o aceptación de condiciones.

## Cómo completar una descarga

1. Descargar desde la **web oficial** indicada el fichero de datos **y** su diseño de registro, metodología o cuestionario. Nunca de copias no oficiales.
2. Colocarlos en `data/raw/<fuente>/<edicion>/` (por ejemplo `data/raw/censo2021_micro_hogares/2021/`).
3. Registrar cada fichero:

   ```bash
   sinpop ingest --source <fuente> --edition <edicion> --register data/raw/<fuente>/<edicion>/<fichero> --url <URL oficial exacta> --tipo datos|diseno_registro|metodologia|cuestionario
   sinpop ingest --verify
   ```

Alternativa: añadir los dominios anteriores a *Allowed domains* en la configuración de red del entorno; entonces `sinpop ingest --source <fuente> --edition <ed> --url <URL>` descarga y registra directamente.

## Fuentes pendientes

| Prioridad | Fuente (`id`) | Organismo | Qué descargar | Página oficial | Carpeta esperada | A verificar en F1 |
| --- | --- | --- | --- | --- | --- | --- |
| P0 | `censo2021_micro_hogares` | INE | Censo 2021, microdatos de personas y hogares (muestra del 10 % de hogares) (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/censo2021_micro_hogares/2021/` | nivel geográfico del fichero nacional (CCAA, provincia, tamaño de municipio); cobertura de la población en establecimientos colectivos; grado de urbanización añadido el 17/06/2026; variable de peso y número de registros |
| P0 | `censo2021_tablas` | INE | Censo de Población y Viviendas 2021 (tablas) (tablas) + diseño de registro / metodología | https://www.ine.es/dyngs/INEbase/listaoperaciones.htm | `data/raw/censo2021_tablas/2021/` | tablas de hogares por tipo y tamaño, tenencia, establecimientos colectivos |
| P0 | `censo_anual_micro_completo` | INE | Censo Anual de Población, microdatos de todas las variables (muestra del 10 %) (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/censo_anual_micro_completo/<edicion>/` | si permite reconstruir hogares o solo personas; edición vigente de cada bloque de variables |
| P0 | `censo_anual_micro_demograficas` | INE | Censo Anual de Población, microdatos de variables demográficas (exhaustivo) (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/censo_anual_micro_demograficas/<edicion>/` | exhaustividad declarada por el INE; grado de urbanización añadido el 29/04/2026; nivel geográfico del fichero |
| P0 | `censo_anual_tablas` | INE | Censo Anual de Población (tablas) (tablas) + diseño de registro / metodología | https://www.ine.es/dyngs/INEbase/listaoperaciones.htm | `data/raw/censo_anual_tablas/<edicion>/` | ediciones vigentes por bloque (estudios y actividad, ocupación, llegada, estado civil); nivel geográfico por variable |
| P0 | `degurba` | INE y Eurostat | Grado de urbanización (DEGURBA) (tablas) + diseño de registro / metodología | https://www.ine.es/dyngs/INEbase/listaoperaciones.htm | `data/raw/degurba/<edicion>/` | usar la clasificación que traen los microdatos censales |
| P0 | `padron_continuo` | INE | Estadística del Padrón Continuo (tablas) + diseño de registro / metodología | https://www.ine.es/dyngs/INEbase/listaoperaciones.htm | `data/raw/padron_continuo/<edicion>/` | edición más reciente publicada (1 de enero); tablas por edad, sexo, nacionalidad y país de nacimiento a nivel municipal |
| P1 | `atlas_renta` | INE (estadística experimental) | Atlas de Distribución de Renta de los Hogares (tablas) + diseño de registro / metodología | https://www.ine.es/dyngs/INEbase/listaoperaciones.htm | `data/raw/atlas_renta/<edicion>/` | último año de renta disponible |
| P1 | `censo2021_micro_viviendas` | INE | Censo 2021, microdatos de viviendas (muestra del 10 %) (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/censo2021_micro_viviendas/2021/` | muestra independiente de la de hogares; variables de enlace |
| P1 | `ecv` | INE | Encuesta de Condiciones de Vida (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/ecv/<edicion>/` | edición más reciente; tamaño de muestra; variables de peso |
| P1 | `encuesta_salud` | INE y Ministerio de Sanidad | Encuesta Europea de Salud en España / Encuesta Nacional de Salud (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/encuesta_salud/<edicion>/` | edición más reciente con microdatos |
| P1 | `epa` | INE | Encuesta de Población Activa (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/epa/<edicion>/` | trimestre de referencia; factor de elevación |
| P1 | `tic_h` | INE | Encuesta sobre Equipamiento y Uso de TIC en los Hogares (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/tic_h/<edicion>/` | universo de edad de la última edición |
| P2 | `encuesta_sin_hogar` | INE | Encuesta a las personas sin hogar (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/encuesta_sin_hogar/<edicion>/` | solo para documentar el hueco |
| P2 | `epf` | INE | Encuesta de Presupuestos Familiares (microdatos) + diseño de registro / metodología | https://www.ine.es/prodyser/microdatos.htm | `data/raw/epf/<edicion>/` | — |
| P3 | `cis_barometro_sanitario_2026` | CIS y Ministerio de Sanidad | Barómetro Sanitario 2026 (microdatos) + diseño de registro / metodología | https://www.cis.es/ | `data/raw/cis_barometro_sanitario_2026/2026/` | — |
| P3 | `cis_barometros` | CIS | Barómetros y estudios del CIS (microdatos) + diseño de registro / metodología | https://www.cis.es/ | `data/raw/cis_barometros/<edicion>/` | variables políticas y de valores presentes por estudio y su codificación |
| P3 | `ess` | ESS ERIC | European Social Survey, ronda 11 (y 12 si está publicada) (microdatos) + diseño de registro / metodología | https://ess.sikt.no/ | `data/raw/ess/R11/` | si la ronda 12 está publicada |
| P3-POL | `censo_electoral` | INE (Oficina del Censo Electoral) | Censo electoral (tablas) + diseño de registro / metodología | https://www.ine.es/dyngs/INEbase/listaoperaciones.htm | `data/raw/censo_electoral/<edicion>/` | — |
| P3-POL | `centros_autonomicos` | Centros autonómicos de opinión | Estudios de centros autonómicos (CEO, Euskobarómetro, Sociómetro y otros) (microdatos) + diseño de registro / metodología | https://ceo.gencat.cat/ | `data/raw/centros_autonomicos/<edicion>/` | — |
| P3-POL | `cis_electorales` | CIS | Estudios preelectorales y postelectorales del CIS (microdatos) + diseño de registro / metodología | https://www.cis.es/ | `data/raw/cis_electorales/<edicion>/` | estudios disponibles para 23J 2023 y posteriores; representatividad territorial |
| P3-POL | `cis_series` | CIS | Series temporales del CIS (tablas) + diseño de registro / metodología | https://www.cis.es/ | `data/raw/cis_series/<edicion>/` | — |
| P3-POL | `infoelectoral_resultados` | Ministerio del Interior (Infoelectoral) | Resultados electorales oficiales (generales, europeas, municipales) (resultados) + diseño de registro / metodología | https://infoelectoral.interior.gob.es/ | `data/raw/infoelectoral_resultados/<edicion>/` | generales 2023-07-23; europeas 2024-06-09; nivel más fino disponible |
| P3-POL | `resultados_autonomicas` | Juntas electorales y gobiernos autonómicos | Resultados de las últimas elecciones autonómicas de cada comunidad (resultados) + diseño de registro / metodología | https://infoelectoral.interior.gob.es/ | `data/raw/resultados_autonomicas/<edicion>/` | última elección de cada comunidad y su fuente oficial |
