# Fase 06 · Enriquecimiento

**Estado:** puerta fallida (G6.1 y G6.4); pendiente de decisión humana (D-046). La fase no tiene puerta de revisión humana, pero los criterios que fallan no se pueden arreglar dentro del enriquecimiento sin decidir antes sobre las variables censales (CLAUDE.md, regla 1).
**Fecha:** 2026-10-16 · **Versión del código:** ver `fase_06_puerta.md`
**Comando para reproducir:**

```bash
sinpop harmonize --source ecv                # ECV con carencias (13 conceptos) y tenencia detallada
python -m sinpop.validate.fase6              # España 1M enriquecida, V-ENRIQ-*, G6.5, G6.6 (≈ 40 min)
sinpop validate --phase 6                    # reports/fase_06_puerta.md
sinpop build --territory CCAA:12 --size 100000 --seed 1   # cualquier población sale enriquecida
```

## Resumen

El enriquecimiento es la etapa 5 de `sinpop build`: cada población sale con 14 variables de encuestas y 2 de contexto, cada una con su columna `__calidad`.

| Bloque | Fuente | Universo | Variables |
| --- | --- | --- | --- |
| Hogar | ECV 2025 | hogares familiares | renta equivalente, decil nacional y regional, tenencia, dificultad para llegar a fin de mes, vehículo |
| Persona | ECV 2025 | 16+ | salud autopercibida, limitación (GALI), carencia material y social severa y número de carencias |
| Empleo | EPA 2T 2026 | ocupados 16+ | jornada, sector público |
| Digital | TIC-H 2025 | 16+ | uso de internet, compra en línea, teletrabajo |
| Contexto | Atlas de renta 2023, Censo Anual 2025 | todos | renta media del municipio, proporción de 65+ |

El método es un **hot-deck aleatorio ponderado por celdas** (D-044, D-045): cada persona u hogar hereda el bloque completo de un donante real de la encuesta, sorteado con su peso oficial entre los de su celda de llaves (las variables comunes con la población). Si la celda tiene menos de 5 donantes, se quitan primero las llaves secundarias manteniendo la comunidad, después se amplía la geografía (zona NUTS-1, España) y por último se quitan las llaves principales. La renta de cada provincia se lleva a la del Atlas inclinando el sorteo, sin reescalar ningún valor. Los residentes en colectivos, fuera del universo de las encuestas, reciben los bloques personales por extrapolación (`extrapolada`) y las variables del hogar como NP.

| Puerta | Criterio | Resultado | |
| --- | --- | --- | --- |
| G6.1 | V-ENRIQ-MARG: ≥ 90 % de las celdas CCAA × edad_4 en el IC 95 % de la encuesta; TVD nacional ≤ 0,02 | 92,1 % de las celdas en global; 5 variables por debajo del 90 % y 3 con TVD > 0,02 | ❌ |
| G6.2 | V-ENRIQ-ASOC: \|Δ V de Cramér\| ≤ 0,05 con cada llave | 0 de 81 pares fuera; máx. 0,049 | ✅ |
| G6.3 | V-ENRIQ-BLOQUE: máx. ≤ 0,05, media ≤ 0,02 | máx. 0,020, media 0,007 | ✅ |
| G6.4 | V-ENRIQ-HOLDOUT: emparejar sin los estudios, \|Δ\| ≤ 0,05 y mejor que la independencia | todas mejor que la independencia; 9 de 14 con \|Δ\| > 0,05 | ❌ |
| G6.5 | El enriquecimiento no cambia las variables de los donantes | personas, hogares y trazabilidad idénticos | ✅ |
| G6.6 | Renta media por provincia frente al Atlas | 52 de 52 dentro (error máx. 2,8 %, dentro de 2 errores típicos) | ✅ (umbral por confirmar) |

## G6.1: qué falla y por qué

| Bloque | Variable | Celdas en IC 95 % | Con la composición de la encuesta | TVD nacional |
| --- | --- | ---: | ---: | ---: |
| digital | `compra_online` | 96,1 % | 100,0 % | 0,0207 ❌ |
| digital | `teletrabajo` | 92,8 % | 100,0 % | 0,0228 ❌ |
| digital | `uso_internet` | 89,6 % ❌ | 97,3 % | 0,0141 |
| empleo | `sector_publico` | 86,8 % ❌ | 86,8 % | 0,0006 |
| empleo | `tipo_jornada` | 84,8 % ❌ | 84,8 % | 0,0002 |
| hogar | `dificultad_fin_mes` | 94,3 % | 94,9 % | 0,0040 |
| hogar | `renta_hogar_decil` | 94,5 % | 94,6 % | 0,0123 |
| hogar | `renta_hogar_decil_ccaa` | 95,3 % | 95,4 % | 0,0151 |
| hogar | `tenencia_vivienda` | 69,1 % ❌ | 67,8 % | 0,0120 |
| hogar | `vehiculo_hogar` | 78,8 % ❌ | 81,2 % | 0,0217 ❌ |
| persona_ecv | `carencias` | 96,9 % | 99,1 % | 0,0106 |
| persona_ecv | `discapacidad_limitacion` | 93,4 % | 98,7 % | 0,0024 |
| persona_ecv | `privacion_material` | 95,1 % | 98,2 % | 0,0008 |
| persona_ecv | `salud_autopercibida` | 95,1 % | 98,2 % | 0,0061 |


La columna «con la composición de la encuesta» repondera la población, dentro de cada comunidad × edad_4, a la composición de la encuesta por relación con la actividad y estudios (diagnóstico, `v_marg_ajustada`). Con ella, salud, carencias y las variables digitales pasan del 90-96 % al 97-100 %: **su desajuste no es del emparejamiento, sino de la composición de la población**, que está calibrada a cifras censales que no coinciden con las encuestas:

| Adultos 18+ en viviendas familiares (España, 100.000 personas) | Población (Censo Anual 2024) | ECV 2025 / TIC-H 2025 |
| --- | ---: | ---: |
| Ocupados | 49,6 % | 52,0 % / 52,1 % |
| Otra inactividad | 19,0 % | 9,9 % / 10,2 % |
| Estudiantes | 4,0 % | 6,8 % / 6,4 % |
| Estudios hasta la obligatoria | 42,3 % | 38,5 % / 33,8 % |

Es la diferencia que D-038 C dejó para revisar en F6 (Censo Anual a 01/01/2024, declarada, frente a la EPA del 2T 2026, definición OIT). Lo que queda tras ajustar la composición (tenencia, vehículo, jornada, sector público) son **patrones regionales** que las llaves no recogen del todo: la tenencia por comunidad conserva además el régimen del Censo 2021 en los hogares sin extranjeros (D-045.3), y la EPA, con su muestra grande, tiene intervalos muy estrechos por comunidad.

## G6.4: qué falla y por qué

Se repitió el emparejamiento quitando cada llave por turno y se comparó su asociación con las variables enriquecidas:


| Llave reservada | Variables fuera de 0,05 | Peores |
| --- | ---: | --- |
| `sexo` | 1 de 14 | `tipo_jornada` 0,148 |
| `nacionalidad_esp_ext` | 1 de 14 | `sector_publico` 0,089 |
| `relacion_actividad` | 4 de 12 | `discapacidad_limitacion` 0,111, `privacion_material` 0,074, `salud_autopercibida` 0,066, `carencias` 0,058 |
| `estudios_3` | 9 de 14 | `compra_online` 0,211, `renta_hogar_decil_ccaa` 0,135, `renta_hogar_decil` 0,126, `carencias` 0,113 |


Ninguna variable queda peor que la independencia, pero la asociación con una variable que no es llave solo se recupera en parte, a través de las llaves que se le parecen. Es la hipótesis de independencia condicional de todo emparejamiento estadístico: **las relaciones entre una variable enriquecida y una variable de la población que no es llave salen atenuadas**. Con los estudios (la llave más informativa y la menos explicada por las demás) la pérdida es mayor: por ejemplo, compra en línea × estudios 0,409 en la TIC-H y 0,197 sin la llave.

## G6.6: renta y Atlas

- Objetivo de cada provincia: media de la renta equivalente de la ECV en su comunidad × (Atlas de la provincia / Atlas de la comunidad), con la media de la renta por unidad de consumo del Atlas 2023 (no se mezclan los niveles de las dos fuentes, solo la geografía relativa).
- 52 provincias dentro de máx(2 %, 2 errores típicos); error máximo 2,8 % (Gipuzkoa, tolerancia 3,0 %).
- No calibrado (se informa): en los 334 municipios identificados con 200 hogares o más, la renta relativa a su provincia se correlaciona 0,58 con la del Atlas (error medio 7,9 %).

## Otros resultados

- **Calidad:** salud autopercibida: 856.220 emparejadas, 7.326 extrapoladas (colectivos) y 136.415 NP observados (menores de 16).
- **Contexto:** `ctx_renta_municipio` y `ctx_envejecimiento` son del municipio en el 79 % de las personas y de su provincia y clase de tamaño (`modelada`) en el 21 %. Había 18 personas sin valor: hogares importados de otra comunidad a provincias sin ciudades (Ávila, Segovia, Soria) que conservaban el grado «ciudad». Corregido en la síntesis (las unidades importadas solo van a provincias con su grado de urbanización) y con un último recurso provincial en el contexto.
- **Triangulación con la ESdE 2023** (informativa): TVD de 0,03 a 0,10 por edad en salud y limitación, por diferencias de cuestionario y fecha entre la ECV y la ESdE.
- **Huecos declarados (P2):** competencias digitales (la TIC-H no trae el indicador; hay que construir el DSI de Eurostat), consumo (EPF, sin variable en el diccionario) y precio de la vivienda (sin fuente oficial descargada).

## Decisiones pendientes (D-046)

Ver `DECISIONS.md`.
