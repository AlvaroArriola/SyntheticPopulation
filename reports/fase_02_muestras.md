# F2 · Muestras para la revisión humana G2.8

Generadas el 2026-10-15 con `sinpop harmonize --samples` (semilla 2026). Los ficheros están en `data/interim/muestras_g28/` y **no se versionan**: contienen registros originales, que no pueden salir del entorno local (regla 8 de CLAUDE.md).

Cada fichero pone lado a lado los campos originales (`orig__…`) y los armonizados (`arm__…`). Para revisar: abrir el CSV, buscar cada código original en el diseño de registro indicado y comprobar que la categoría armonizada es la que fija `configs/variables.yaml` (o la regla de universo de D-025 a D-028).

| Fichero | Registros | Diseño de registro o documento de referencia |
| --- | ---: | --- |
| `censo2021_micro_hogares.csv` | 20 | dr_CensoPersonas_2021.xlsx |
| `censo_anual_micro_completo_2023.csv` | 20 | dr_CensoAnual_muestra_2022.xlsx |
| `censo_anual_micro_completo_2024.csv` | 20 | dr_CensoAnual_muestra_2022.xlsx |
| `censo_anual_micro_completo_2025.csv` | 20 | dr_CensoAnual_muestra_2022.xlsx |
| `censo_anual_micro_demograficas.csv` | 20 | dr_CensoAnual_2026.json |
| `ecv.csv` | 20 | disreg_ecv25 (diseños de los ficheros R, P, H y D) |
| `epa.csv` | 20 | dr_EPA_2026.json |
| `tic_h.csv` | 20 | dr_TICHcuestionario_2025.json |
| `encuesta_salud.csv` | 20 | dr_ESdEadulto_2023.json |
| `ecp_viviendas_familiares.csv` | 20 | INE, tabla 60129 (JSON de la API) |
| `ecp_total.csv` | 20 | INE, tabla 59589 |
| `ecp_hogares.csv` | 20 | INE, tabla 60133 |
| `elecciones_generales_2023_municipios.csv` | 20 | PDF de Interior: página del municipio |
