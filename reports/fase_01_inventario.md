# Inventario de microdatos (F1)

Generado por `sinpop ingest --inventory`. Totales ponderados con el peso oficial;
los censos no tienen peso y se marcan sin ponderar.

| Fuente | Edición | Fichero | Unidad | Registros | Peso | Total ponderado | Edad | Geo (valores) |
| --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| `censo2021_micro_hogares` | 2021 | `md_CensoPersonas_2021.parquet` | persona | 4.707.186 | — | sin ponderar | 0–100 | CPRO (52) |
| `censo_anual_micro_completo` | 2023 | `md_Censo_muestra_2023.txt` | persona | 4.807.670 | — | sin ponderar | 0–100 | CPRO (52) |
| `censo_anual_micro_completo` | 2024 | `md_Censo_muestra_2024.txt` | persona | 4.861.970 | — | sin ponderar | 0–100 | CPRO (52) |
| `censo_anual_micro_completo` | 2025 | `md_Censo_muestra_2025.txt` | persona | 4.912.830 | — | sin ponderar | 0–100 | CPRO (52) |
| `censo_anual_micro_demograficas` | 2025 | `md_CensoAnual_2025.parquet` | persona | 49.128.297 | — | sin ponderar | 0–100 | CPRO (52) |
| `ecv` | 2025 | `md_ECV_Tr_2025.parquet` | persona | 71.398 | RB050 | 48.702.184 | -1–86 | — |
| `ecv` | 2025 | `md_ECV_Tp_2025.parquet` | persona 16+ | 60.825 | PB040 | 41.873.122 | — | — |
| `ecv` | 2025 | `md_ECV_Td_2025.parquet` | hogar | 29.369 | DB090 | 19.508.513 | — | DB040 (19) |
| `ecv` | 2025 | `md_ECV_Th_2025.parquet` | hogar | 29.369 | — | sin ponderar | — | — |
| `epa` | 2T2026 | `md_EPA_2026T2.parquet` | persona | 114.021 | FACTOREL | 49.345.143 | — | PROV (52) |
| `tic_h` | 2025 | `md_TICHcuestionario_2025.parquet` | persona 16+ | 16.938 | FACTOR_P | 42.057.112 | 16–104 | CCAA (19) |
| `tic_h` | 2025 | `md_TICHmiembros_2025.parquet` | miembro del hogar | 40.662 | — | sin ponderar | 0–106 | CCAA (19) |
| `encuesta_salud` | 2023 | `md_ESdEadulto_2023.parquet` | persona 15+ | 21.032 | FACTORADULTO | 41.929.276 | 15–103 | CCAA (19) |

## Recuento de registros (G1.4)

| Fichero | Registros | Referencia oficial | Valor | Regla | Resultado |
| --- | ---: | --- | ---: | --- | --- |
| `md_CensoPersonas_2021.parquet` | 4.707.186 | Censo 2021, tabla 67988 a 01/01/2021 (población total, incluye establecimientos colectivos) | 47.400.798 | 10 % de los hogares: sin cifra exacta declarada; se informa el cociente | ⚠️ no declarado |
| `md_Censo_muestra_2023.txt` | 4.807.670 | Censo Anual 2023, tabla 67988 (población total) | 48.085.361 | registros = población / 10 (±1 por redondeo) | ❌ |
| `md_Censo_muestra_2024.txt` | 4.861.970 | Censo Anual 2024, tabla 67988 (población total) | 48.619.695 | registros = población / 10 (±1 por redondeo) | ✅ |
| `md_Censo_muestra_2025.txt` | 4.912.830 | Censo Anual 2025, tabla 67988 (población total) | 49.128.297 | registros = población / 10 (±1 por redondeo) | ✅ |
| `md_CensoAnual_2025.parquet` | 49.128.297 | Censo Anual 2025, tabla 67988 (población total) | 49.128.297 | fichero exhaustivo: registros = población oficial | ✅ |
