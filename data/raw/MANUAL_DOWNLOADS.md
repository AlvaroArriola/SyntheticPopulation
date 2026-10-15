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

| Fuente (`id`) | Organismo | Qué falta | Página oficial | Motivo |
| --- | --- | --- | --- | --- |
| `infoelectoral_resultados` | Ministerio del Interior | Resultados por municipio de las europeas del 09/06/2024 | https://infoelectoral.interior.gob.es/ | el servidor corta la conexión desde el entorno; las generales 2023 ya están (aportadas por el responsable) |
| `ess` | ESS ERIC | European Social Survey, ronda 11 (y 12 si está publicada) | https://ess.sikt.no/ | R12 no publicada: primera publicación prevista en enero de 2027 |
| `resultados_autonomicas` | Juntas electorales y gobiernos autonómicos | Resultados de las últimas elecciones autonómicas de cada comunidad | https://infoelectoral.interior.gob.es/ | última elección de cada comunidad y su fuente oficial; el servidor corta la conexión desde el entorno (no es una denegación de la política de red) |
| `centros_autonomicos` | Centros autonómicos de opinión | Estudios de centros autonómicos (CEO, Euskobarómetro, Sociómetro y otros) | https://ceo.gencat.cat/ | requiere registro o aceptación de condiciones |
