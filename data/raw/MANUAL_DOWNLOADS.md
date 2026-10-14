# Descargas manuales

Fuentes que no se pueden descargar automáticamente desde el entorno (CLAUDE.md, «Descarga de datos»). Actualizado el 2026-10-14 (D-019).

Todas las fuentes del núcleo (F1–F7) se han descargado automáticamente desde el INE: ver `MANIFEST.yaml`. Las de esta lista solo intervienen en las capas de opinión y política (F8A y F8B).

## Cómo completar una descarga

1. Descargar desde la **web oficial** el fichero de datos **y** su cuestionario o diseño de registro. Nunca de copias no oficiales.
2. Colocarlos en `data/raw/<fuente>/<edicion>/`.
3. Registrarlos:

   ```bash
   sinpop ingest --source <fuente> --edition <edicion> --register data/raw/<fuente>/<edicion>/<fichero> --url <URL oficial exacta> --tipo datos|diseno_registro|cuestionario
   sinpop ingest --verify
   ```

## Fuentes pendientes

| Fuente (`id`) | Organismo | Qué descargar | Página oficial | Motivo |
| --- | --- | --- | --- | --- |
| `cis_barometros` | CIS | Barómetros y estudios del CIS | https://www.cis.es/ | variables políticas y de valores presentes por estudio y su codificación; microdatos bajo petición en el catálogo del CIS; el servidor limita las peticiones automáticas (HTTP 429) |
| `cis_barometro_sanitario_2026` | CIS y Ministerio de Sanidad | Barómetro Sanitario 2026 | https://www.cis.es/ | microdatos bajo petición en el catálogo del CIS; el servidor limita las peticiones automáticas (HTTP 429) |
| `ess` | ESS ERIC | European Social Survey, ronda 11 (y 12 si está publicada) | https://ess.sikt.no/ | R12 no publicada: primera publicación prevista en enero de 2027 |
| `infoelectoral_resultados` | Ministerio del Interior (Infoelectoral) | Resultados electorales oficiales (generales, europeas, municipales) | https://infoelectoral.interior.gob.es/ | generales 2023-07-23; europeas 2024-06-09; nivel más fino disponible; el servidor corta la conexión desde el entorno (no es una denegación de la política de red) |
| `resultados_autonomicas` | Juntas electorales y gobiernos autonómicos | Resultados de las últimas elecciones autonómicas de cada comunidad | https://infoelectoral.interior.gob.es/ | última elección de cada comunidad y su fuente oficial; el servidor corta la conexión desde el entorno (no es una denegación de la política de red) |
| `cis_electorales` | CIS | Estudios preelectorales y postelectorales del CIS | https://www.cis.es/ | estudios disponibles para 23J 2023 y posteriores; representatividad territorial; microdatos bajo petición en el catálogo del CIS; el servidor limita las peticiones automáticas (HTTP 429) |
| `centros_autonomicos` | Centros autonómicos de opinión | Estudios de centros autonómicos (CEO, Euskobarómetro, Sociómetro y otros) | https://ceo.gencat.cat/ | requiere registro o aceptación de condiciones |
| `cis_series` | CIS | Series temporales del CIS | https://www.cis.es/ | microdatos bajo petición en el catálogo del CIS; el servidor limita las peticiones automáticas (HTTP 429) |
