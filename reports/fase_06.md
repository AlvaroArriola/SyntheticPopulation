# Fase 06 · Enriquecimiento

**Estado:** superada (G6.1-G6.6). En G6.1, cinco variables se aceptan como limitación declarada (D-048, aprobada el 17/10/2026): cuatro por patrones regionales y una por la fecha de la encuesta.
**Fecha:** 2026-10-16 · **Versión del código:** ver `fase_06_puerta.md`
**Comando para reproducir** (cadena completa tras D-046, ≈ 5 h):

```bash
sinpop harmonize --source ecv                # ECV con carencias (13 conceptos UE) y tenencia detallada
sinpop targets --territory all               # objetivos con la actividad de la EPA 2T 2026 (D-046 A2)
for m in configs/territorios/*.yaml; do sinpop targets --territory "MUNIS:$m"; done
python -m sinpop.validate.fase4 && sinpop validate --phase 4
python -m sinpop.validate.fase5 && sinpop validate --phase 5
python -m sinpop.validate.fase6 && sinpop validate --phase 6
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

**Método** (D-044, D-045): hot-deck aleatorio ponderado por celdas.

- Cada persona u hogar hereda el bloque completo de un donante real de la encuesta, sorteado con su peso oficial entre los de su celda de llaves.
- Las llaves van ordenadas por su importancia en la propia encuesta. Algunas son estructurales y no se quitan nunca, por ejemplo la situación profesional en el empleo.
- Si la celda tiene menos de 5 donantes, primero se quitan las llaves secundarias manteniendo la comunidad, después se amplía la geografía (zona NUTS-1, España) y por último se quitan las principales.
- Los hogares con algún adulto extranjero toman la tenencia de la ECV 2025.
- La renta de cada provincia se lleva a la del Atlas inclinando el sorteo, sin reescalar valores.
- Los residentes en colectivos, fuera del universo de las encuestas, reciben los bloques personales por extrapolación (`extrapolada`).

**Cambio de composición (D-046 A2):** ocupados, parados e inactivos están calibrados a la EPA del 2T 2026, la última foto oficial del mercado de trabajo antes del corte de junio de 2026; dentro de los inactivos se mantiene el reparto del Censo Anual. Las puertas F3, F4 y F5 se repitieron (F4: un fallo por azar en V-SEMILLAS, D-047; F5: superada).

| Puerta | Criterio | Resultado | |
| --- | --- | --- | --- |
| G6.1 | V-ENRIQ-MARG: ≥ 90 % de las celdas CCAA × edad_4 en el IC 95 % de la encuesta; TVD nacional ≤ 0,02 | 92,6 % de las celdas en global; 5 variables por debajo del 90 %; 2 con TVD > 0,02 | ✅ con limitaciones (D-048) |
| G6.2 | V-ENRIQ-ASOC: \|Δ V de Cramér\| ≤ 0,05 con cada llave | 0 de 81 pares fuera; máx. 0.049 | ✅ |
| G6.3 | V-ENRIQ-BLOQUE: máx. ≤ 0,05, media ≤ 0,02 | máx. 0.022, media 0.007 | ✅ |
| G6.4 | V-ENRIQ-HOLDOUT: mejor que la independencia (D-046 B1) | 54 pares con 4 llaves reservadas; 0 peor que la independencia | ✅ |
| G6.5 | El enriquecimiento no cambia las variables de los donantes | personas, hogares y trazabilidad idénticos | ✅ |
| G6.6 | Renta media por provincia frente al Atlas: máx(2 %, 2 errores típicos) (D-046 C) | 52 de 52 dentro (error máx. 3,26 %) | ✅ |

## G6.1

| Bloque | Variable | Celdas en IC 95 % | TVD nacional | Celdas en IC, composición de la encuesta | TVD, composición de la encuesta |
| --- | --- | ---: | ---: | ---: | ---: |
| digital | `compra_online` | 98,7 % | 0,0150 | 100,0 % | 0,0065 |
| digital | `teletrabajo` | 89,4 % ❌ | 0,0325 ❌ | 100,0 % | 0,0016 |
| digital | `uso_internet` | 93,1 % | 0,0112 | 97,3 % | 0,0017 |
| empleo | `sector_publico` | 85,5 % ❌ | 0,0041 | 89,5 % ❌ | 0,0025 |
| empleo | `tipo_jornada` | 86,8 % ❌ | 0,0036 | 84,1 % ❌ | 0,0030 |
| hogar | `dificultad_fin_mes` | 95,6 % | 0,0024 | 94,9 % | 0,0042 |
| hogar | `renta_hogar_decil` | 95,3 % | 0,0044 | 95,9 % | 0,0076 |
| hogar | `renta_hogar_decil_ccaa` | 95,5 % | 0,0084 | 96,0 % | 0,0085 |
| hogar | `tenencia_vivienda` | 65,1 % ❌ | 0,0200 ❌ | 64,1 % ❌ | 0,0190 |
| hogar | `vehiculo_hogar` | 81,2 % ❌ | 0,0148 | 82,4 % ❌ | 0,0106 |
| persona_ecv | `carencias` | 97,5 % | 0,0090 | 99,1 % | 0,0068 |
| persona_ecv | `discapacidad_limitacion` | 94,4 % | 0,0031 | 97,0 % | 0,0014 |
| persona_ecv | `privacion_material` | 96,0 % | 0,0024 | 98,2 % | 0,0035 |
| persona_ecv | `salud_autopercibida` | 96,0 % | 0,0084 | 98,2 % | 0,0041 |

Las dos últimas columnas reponderan la población, dentro de cada comunidad × edad_4, a la composición de la encuesta por relación con la actividad y estudios. Es un diagnóstico, no la puerta (`v_marg_ajustada`).

- **Teletrabajo** (TVD 0.033): la diferencia es de fecha. La población tiene los ocupados de la EPA del 2T 2026 (54,7 % de los adultos en viviendas familiares) y la TIC-H es de 2025 (52,1 %), así que su categoría «no procede» (no ocupados) es menor. Con la composición de la TIC-H, la TVD es 0.002 y el 100 % de las celdas entra en el IC.
- **Tenencia** (TVD 0.020, 65 % de celdas), **vehículo** (81 %), **jornada** (87 %) y **sector público** (86 %): siguen por debajo con la composición ajustada. Son **patrones regionales** que las llaves no recogen del todo:
  - La tenencia de los hogares sin extranjeros es la del Censo 2021 (D-045.3), que por comunidad no coincide con la muestra de la ECV 2025.
  - La EPA, con su muestra grande, da intervalos muy estrechos por comunidad.
  - La diferencia nacional es pequeña en todas: TVD ajustada ≤ 0.019.

## G6.4

| Llave reservada | Pares | Peor que la independencia | \|Δ\| > 0,05 | Asociación recuperada (mín. - máx.) |
| --- | ---: | ---: | ---: | --- |
| `sexo` | 14 | 0 | 1 | 19 % - 109 % |
| `nacionalidad_esp_ext` | 14 | 0 | 1 | 48 % - 116 % |
| `relacion_actividad` | 12 | 0 | 4 | 41 % - 120 % |
| `estudios_3` | 14 | 0 | 9 | 18 % - 99 % |

Ninguna asociación queda peor que la independencia. La que tiene una variable enriquecida con una variable que no es llave solo se recupera en parte, por la hipótesis de independencia condicional de todo emparejamiento estadístico. Por eso las llaves incluyen las variables que más importan para cada bloque.

## G6.6

- 52 provincias dentro de máx(2 %, 2 errores típicos); error máximo 3,26 %.
- No calibrado (se informa): en los 326 municipios identificados con 200 hogares o más, la renta relativa a su provincia se correlaciona 0,63 con la del Atlas (error medio 7,6 %).

## Otros resultados

- **Calidad** de la salud autopercibida: 856.203 emparejadas, 7.347 extrapoladas (colectivos) y 136.480 NP observados (menores de 16).
- **Contexto:** renta media del municipio y proporción de 65+, del municipio (`observada`) o de su provincia y clase de tamaño (`modelada`). Sin valores vacíos tras la corrección de las unidades importadas (`pesos._tiene_grado`).
- **Triangulación con la ESdE 2023** (informativa, en `fase_06_validacion.json`): diferencias por cuestionario y fecha entre la ECV y la ESdE.
- **Huecos declarados (P2):**
  - competencias digitales: la TIC-H no trae el indicador; hay que construir el DSI de Eurostat;
  - consumo: la EPF no tiene variable en el diccionario;
  - precio de la vivienda: sin fuente oficial descargada.
