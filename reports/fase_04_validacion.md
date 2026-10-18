# Fase 04 · Tablas de validación

Generado por `python -m sinpop.validate.fase4` (git:086a688-dirty, 2026-10-18). Resumen en `fase_04_validacion.json`; detalle por población en `fase_04/`.

## Curva de error frente a tamaño (España; media de 5 semillas)

| n | tvd_media_calibradas | sd_calibradas | tvd_media_reservadas | sd_reservadas |
| --- | --- | --- | --- | --- |
| 10000 | 0.0188 | 0.0025 | 0.0168 | 0.0011 |
| 50000 | 0.0060 | 0.0003 | 0.0098 | 0.0005 |
| 100000 | 0.0033 | 0.0001 | 0.0089 | 0.0001 |
| 500000 | 0.0012 | 0.0001 | 0.0081 | 0.0002 |
| 1000000 | 0.0008 | 0.0000 | 0.0079 | 0.0001 |

## TVD por marginal calibrada (España; media de 5 semillas)

| objetivo | 50000 | 1000000 | 100000 | 10000 | 500000 |
| --- | --- | --- | --- | --- | --- |
| actividad_nacionalidad | 0.0029 | 0.0007 | 0.0022 | 0.0064 | 0.0011 |
| actividad_tramo | 0.0031 | 0.0008 | 0.0024 | 0.0067 | 0.0014 |
| edad5_sexo | 0.0022 | 0.0007 | 0.0014 | 0.0055 | 0.0009 |
| edad5_sexo_colectivos | 0.0748 | 0.0074 | 0.0368 | 0.2510 | 0.0114 |
| edad5_sexo_familiares | 0.0023 | 0.0007 | 0.0015 | 0.0058 | 0.0009 |
| estado_civil_edad | 0.0026 | 0.0006 | 0.0020 | 0.0063 | 0.0009 |
| estudios_edad | 0.0024 | 0.0006 | 0.0018 | 0.0048 | 0.0009 |
| nacimiento_nacionalidad | 0.0009 | 0.0004 | 0.0009 | 0.0032 | 0.0005 |
| nacionalidad | 0.0005 | 0.0002 | 0.0003 | 0.0021 | 0.0002 |
| nacionalidad_edad | 0.0021 | 0.0005 | 0.0015 | 0.0057 | 0.0007 |
| nacionalidad_top | 0.0003 | 0.0002 | 0.0002 | 0.0020 | 0.0002 |
| nacionalidad_top_edad | 0.0011 | 0.0003 | 0.0010 | 0.0034 | 0.0004 |
| sin_estudios_edad | 0.0012 | 0.0003 | 0.0009 | 0.0032 | 0.0004 |
| tamano_hogar | 0.0015 | 0.0002 | 0.0007 | 0.0037 | 0.0002 |
| tipo_hogar | 0.0027 | 0.0004 | 0.0016 | 0.0065 | 0.0006 |
| tipo_residencia (implícito) | 0.0001 | 0.0000 | 0.0001 | 0.0008 | 0.0000 |
| urbanizacion | 0.0007 | 0.0002 | 0.0003 | 0.0019 | 0.0002 |

## TVD por cruce reservado (España; media de 5 semillas)

| objetivo | 500000 | 50000 | 10000 | 1000000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | 0.0110 | 0.0127 | 0.0172 | 0.0110 | 0.0114 |
| actividad_sexo | 0.0056 | 0.0066 | 0.0087 | 0.0052 | 0.0065 |
| adultos_nacionalidad | 0.0018 | 0.0019 | 0.0029 | 0.0018 | 0.0018 |
| estudios_sexo_edad | 0.0071 | 0.0090 | 0.0178 | 0.0070 | 0.0090 |
| nacionalidad_top_sexo_edad | 0.0051 | 0.0081 | 0.0156 | 0.0047 | 0.0066 |
| provincia_si_calibra_ccaa | 0.0090 | 0.0123 | 0.0246 | 0.0090 | 0.0104 |
| tamano_municipio | 0.0113 | 0.0107 | 0.0166 | 0.0111 | 0.0109 |
| tipo_hogar_edad4_ref | 0.0139 | 0.0171 | 0.0308 | 0.0137 | 0.0149 |

## Fallos por tamaño

| N | semilla | v_marg | v_cruce | v_cruce_excepciones | v_cruce_estricto | comprobaciones_cruce |
| --- | --- | --- | --- | --- | --- | --- |
| 10000 | 1 | 0 | 10 | 1 | 28 | 511 |
| 10000 | 2 | 0 | 5 | 0 | 21 | 511 |
| 10000 | 3 | 0 | 9 | 1 | 25 | 511 |
| 10000 | 4 | 0 | 9 | 0 | 28 | 511 |
| 10000 | 5 | 0 | 6 | 0 | 24 | 511 |
| 50000 | 1 | 0 | 3 | 1 | 7 | 511 |
| 50000 | 2 | 0 | 2 | 1 | 4 | 511 |
| 50000 | 3 | 0 | 5 | 0 | 7 | 511 |
| 50000 | 4 | 0 | 3 | 1 | 6 | 511 |
| 50000 | 5 | 0 | 1 | 0 | 5 | 511 |
| 100000 | 1 | 0 | 1 | 0 | 3 | 511 |
| 100000 | 2 | 0 | 0 | 1 | 1 | 511 |
| 100000 | 3 | 0 | 0 | 1 | 6 | 511 |
| 100000 | 4 | 0 | 0 | 0 | 4 | 511 |
| 100000 | 5 | 0 | 3 | 1 | 5 | 511 |
| 500000 | 1 | 0 | 0 | 0 | 1 | 511 |
| 500000 | 2 | 0 | 0 | 0 | 1 | 511 |
| 500000 | 3 | 0 | 0 | 1 | 1 | 511 |
| 500000 | 4 | 0 | 0 | 0 | 1 | 511 |
| 500000 | 5 | 0 | 0 | 0 | 1 | 511 |
| 1000000 | 1 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 2 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 3 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 4 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 5 | 0 | 0 | 1 | 1 | 511 |

### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas

| nivel | territorio | objetivo | tvd | umbral | excepcion | N | semilla |
| --- | --- | --- | --- | --- | --- | --- | --- |
| provincia | PROV:40 | tamano_municipio | 0.0937 | 0.0800 | ✅ | 500000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0803 | 0.0800 | ✅ | 1000000 | 2 |
| provincia | PROV:40 | tamano_municipio | 0.0807 | 0.0800 | ✅ | 1000000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0823 | 0.0800 | ✅ | 1000000 | 5 |

## V-SEMILLAS

| n | proporciones | fuera | razon_media | razon_max |
| --- | --- | --- | --- | --- |
| 10000 | 475 | 1 | 0.3239 | 1.5429 |
| 50000 | 475 | 0 | 0.2228 | 1.0329 |
| 100000 | 475 | 0 | 0.2153 | 0.5682 |
| 500000 | 475 | 0 | 0.2261 | 0.5556 |
| 1000000 | 475 | 0 | 0.2164 | 0.5201 |

## V-PESOS (calibración por comunidades)

| bloque | desviacion_max | proporcion_en_rango | kish_ratio | no_positivos | factor_min | factor_max | proporcion_local | ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 0.0000 | 1.0000 | 0.7600 | 0 | 0.2000 | 5.0000 | 0.9988 | ✅ |
| CCAA:02 | 0.0000 | 1.0000 | 0.7714 | 0 | 0.2000 | 4.9999 | 0.9994 | ✅ |
| CCAA:03 | 0.0000 | 1.0000 | 0.7535 | 0 | 0.2000 | 5.0000 | 0.9977 | ✅ |
| CCAA:04 | 0.0005 | 1.0000 | 0.5822 | 0 | 0.2000 | 5.0000 | 0.9996 | ✅ |
| CCAA:05 | 0.0000 | 1.0000 | 0.6804 | 0 | 0.2000 | 4.9999 | 0.9997 | ✅ |
| CCAA:06 | 0.0000 | 1.0000 | 0.7526 | 0 | 0.2000 | 4.9998 | 0.9986 | ✅ |
| CCAA:07 | 0.0000 | 1.0000 | 0.7806 | 0 | 0.2000 | 5.0000 | 0.9973 | ✅ |
| CCAA:08 | 0.0000 | 1.0000 | 0.7406 | 0 | 0.2000 | 5.0000 | 0.9996 | ✅ |
| CCAA:09 | 0.0000 | 1.0000 | 0.6864 | 0 | 0.2000 | 5.0000 | 1.0000 | ✅ |
| CCAA:10 | 0.0000 | 1.0000 | 0.6739 | 0 | 0.2000 | 5.0000 | 0.9967 | ✅ |
| CCAA:11 | 0.0000 | 1.0000 | 0.7970 | 0 | 0.2000 | 4.9991 | 0.9984 | ✅ |
| CCAA:12 | 0.0000 | 1.0000 | 0.7671 | 0 | 0.2000 | 5.0000 | 0.9975 | ✅ |
| CCAA:13 | 0.0000 | 1.0000 | 0.7122 | 0 | 0.2000 | 5.0000 | 1.0000 | ✅ |
| CCAA:14 | 0.0000 | 1.0000 | 0.7166 | 0 | 0.2000 | 5.0000 | 0.9990 | ✅ |
| CCAA:15 | 0.0000 | 1.0000 | 0.7436 | 0 | 0.2000 | 4.9999 | 0.9998 | ✅ |
| CCAA:16 | 0.0000 | 1.0000 | 0.7644 | 0 | 0.2000 | 5.0000 | 0.9997 | ✅ |
| CCAA:17 | 0.0000 | 1.0000 | 0.7659 | 0 | 0.2000 | 4.9686 | 0.9992 | ✅ |
| CCAA:18 | 0.0000 | 1.0000 | 0.6338 | 0 | 0.2000 | 4.9989 | 0.9914 | ✅ |
| CCAA:19 | 0.0000 | 1.0000 | 0.6175 | 0 | 0.2000 | 4.9640 | 0.9868 | ✅ |

## Ampliación de donantes

| bloque | objetivo | clave | locales | razon_inicial | anadidas | motivo |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | nacionalidad_top | nacionalidad_top=peru | 322 | 3.9510 | 186 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 54 | 5.6104 | 64 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 109 | 4.2454 | 92 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 73 | 4.2210 | 51 | None |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 24 | 3.6771 | 7 | None |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 31 | 4.4712 | 22 | None |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 6 | 4.7396 | 6 | None |
| CCAA:03 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 4 | 3.4299 | 1 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=peru | 50 | 3.5617 | 19 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=ucrania | 42 | 5.4382 | 33 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 8 | 6.5015 | 13 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | 20 | 3.8740 | 10 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 9 | 3.7148 | 5 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 4 | 2.8214 | 1 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 4 | 19.8492 | 1 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | 16 | 5.7400 | 20 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 4 | 6.8324 | 1 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | 5 | 4.3403 | 4 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | 3 | 4.1838 | 2 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 18 | 3.6435 | 8 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 5 | 4.4893 | 5 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 14 | 3.5343 | 6 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 15 | 4.5170 | 12 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | 17 | 3.6002 | 8 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-24 | 57 | 3.7805 | 29 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 3 | 1.8881 | 2 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 5 | 4.1204 | 4 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=peru | 187 | 3.8136 | 96 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | 5 | 3.6604 | 3 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | 4 | 3.7549 | 1 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | 4 | 4.8767 | 1 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 44 | 5.0595 | 43 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 43 | 3.8667 | 22 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 10 | 3.7457 | 6 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 6 | 5.8690 | 9 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | 71 | 3.7543 | 39 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | 129 | 3.5244 | 56 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=paraguay | 101 | 2.2089 | 3 | reparacion 1 |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 62 | 3.8319 | 33 | None |
| CCAA:10 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 247 | 3.9260 | 143 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 532 | 3.5074 | 220 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 46 | 4.7211 | 37 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 52 | 3.8889 | 29 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 323 | 3.9135 | 180 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 99 | 4.1809 | 64 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 7 | 4.0999 | 5 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=peru | 36 | 3.7553 | 17 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 41 | 3.9237 | 27 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 19 | 3.6215 | 9 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=todas | 36 | 3.7553 | 13 | None |
| CCAA:12 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | 4 | 3.5585 | 1 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=peru | 207 | 3.7108 | 93 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=ucrania | 40 | 3.5008 | 18 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | 2 | 3.6488 | 3 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 94 | 4.1935 | 61 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 47 | 4.6418 | 44 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 78 | 3.7693 | 49 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 14 | 4.4851 | 13 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 2 | 11.0122 | 3 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 63 | 4.0051 | 38 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | 5 | 3.8028 | 3 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | 24 | 3.5464 | 8 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 12 | 3.7354 | 7 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | 2 | 2.6115 | 3 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | 6 | 3.6824 | 3 | None |
| CCAA:16 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 4 | 4.1474 | 1 | None |
| CCAA:16 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 4 | 4.5891 | 1 | None |
| CCAA:16 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 8 | 4.4910 | 7 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | 2 | 7.0517 | 3 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 7 | 5.9836 | 9 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 11 | 3.7788 | 5 | None |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | 3 | 4.4321 | 2 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 8.1332 | 4 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.9987 | 3 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=paraguay | 4 | 4.3333 | 1 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=todas | 4 | 4.3333 | 1 | None |
| CCAA:18 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 11 | 4.1869 | 7 | None |
| CCAA:18 | estudios_edad | estudios_3=superior;edad_estudios=90+ | 3 | 2.0488 | 2 | None |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 1.9579 | 4 | None |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.3251 | 3 | None |
| CCAA:18 | nacionalidad_top | nacionalidad_top=china | 1 | 2.3948 | 4 | None |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=todas | 1 | 2.3948 | 4 | None |
| CCAA:19 | estudios_edad | estudios_3=secundaria_2a_etapa;edad_estudios=90+ | 2 | 1.3648 | 3 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=america_latina | 18 | 4.7103 | 15 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.6564 | 1 | None |
| CCAA:19 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.8079 | 3 | None |
| CCAA:19 | nacionalidad_top | nacionalidad_top=colombia | 1 | 17.6844 | 4 | None |
| CCAA:19 | nacionalidad_top | nacionalidad_top=venezuela | 5 | 4.2542 | 4 | None |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=todas | 1 | 17.6844 | 4 | None |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=todas | 5 | 4.2542 | 4 | None |

## Nacionalidades fusionadas con «otras extranjeras»

| bloque | objetivo | clave | fusionada_en |
| --- | --- | --- | --- |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:01 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:01 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:01 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:02 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:02 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:02 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:02 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=00-19 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:02 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:02 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:03 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:03 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:03 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=00-19 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=20-34 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=35-49 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=50-64 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=00-19 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:03 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:03 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:05 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:05 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:05 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=00-19 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=00-19 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:05 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:05 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:06 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:06 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=00-19 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=20-34 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=35-49 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=50-64 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=00-19 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=20-34 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=35-49 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=00-19 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=20-34 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:06 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | estado_civil=soltero;edad_estado_civil=16-34 |
| CCAA:06 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:06 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:07 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:07 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:07 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:08 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:08 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:08 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:08 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:08 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:08 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:09 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:09 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:09 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:09 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:09 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:09 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:10 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:10 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:10 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:10 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:11 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=00-19 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=20-34 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=35-49 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=50-64 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=00-19 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=20-34 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=35-49 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=00-19 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=20-34 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:11 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | estado_civil=soltero;edad_estado_civil=16-34 |
| CCAA:11 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:12 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:12 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:12 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:12 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=00-19 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:12 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:12 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:13 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:13 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:13 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:14 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:14 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:15 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:15 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:15 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:15 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=20-34 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=35-49 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=00-19 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:15 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:15 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:16 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:16 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:17 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | nacionalidad_top=argentina;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=00-19 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=20-34 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=35-49 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=50-64 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=00-19 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=ecuador;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=20-34 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=35-49 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | nacionalidad_top=italia;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=00-19 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=paraguay;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | nacionalidad_top=peru;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=reino_unido;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=20-34 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | nacionalidad_top=ucrania;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=50-64 | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:17 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | estado_civil=soltero;edad_estado_civil=16-34 |
| CCAA:17 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:17 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:18 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:18 | nacionalidad_top | nacionalidad_top=alemania | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=argentina | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=colombia | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=ecuador | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=francia | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=honduras | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=italia | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=paraguay | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=peru | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=reino_unido | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=rumania | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=ucrania | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top | nacionalidad_top=venezuela | nacionalidad_top=otras_extranjeras |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=00-19 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=20-34 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=35-49 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=50-64 | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | nacionalidad_top=china;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | estado_civil_edad | estado_civil=NC;edad_estado_civil=35-54 | estado_civil=casado;edad_estado_civil=35-54 |
| CCAA:18 | estado_civil_edad | estado_civil=NC;edad_estado_civil=75+ | estado_civil=casado;edad_estado_civil=75+ |
| CCAA:18 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | estado_civil=soltero;edad_estado_civil=16-34 |
| CCAA:18 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-24 | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:18 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:18 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-24 | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:18 | nacionalidad | nacionalidad_grupo=otros | nacionalidad_grupo=espanola |
| CCAA:18 | nacionalidad | nacionalidad_grupo=resto_europa | nacionalidad_grupo=espanola |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:19 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:19 | nacionalidad_top | nacionalidad_top=argentina | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=china | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=ecuador | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=honduras | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=italia | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=paraguay | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=peru | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=reino_unido | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=rumania | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top | nacionalidad_top=ucrania | nacionalidad_top=otras_extranjeras |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=alemania;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | nacionalidad_top=colombia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | nacionalidad_top=colombia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | nacionalidad_top=colombia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | nacionalidad_top=colombia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | nacionalidad_top=colombia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=francia;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=50-64 | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | nacionalidad_top=venezuela;edad_nacionalidad=todas |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:19 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | estado_civil=soltero;edad_estado_civil=16-34 |
| CCAA:19 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:19 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:19 | nacionalidad | nacionalidad_grupo=asia | nacionalidad_grupo=espanola |
| CCAA:19 | nacionalidad | nacionalidad_grupo=otros | nacionalidad_grupo=espanola |

## V de Cramér (2026-01-01_ES_1000000_s1)

| objetivo | par | v_oficial | v_sintetica | dif | ok |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | relacion_actividad × edad_actividad | 0.6145 | 0.6188 | 0.0043 | ✅ |
| actividad_sexo | relacion_actividad × sexo | 0.2209 | 0.2190 | 0.0019 | ✅ |
| adultos_nacionalidad | nacionalidad_esp_ext × es_adulto | 0.0028 | 0.0059 | 0.0032 | ✅ |
| estudios_sexo_edad | estudios_3 × sexo | 0.0391 | 0.0352 | 0.0039 | ✅ |
| estudios_sexo_edad | estudios_3 × edad_estudios | 0.6228 | 0.6229 | 0.0000 | ✅ |
| estudios_sexo_edad | sexo × edad_estudios | 0.0713 | 0.0713 | 0.0001 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × sexo | 0.0420 | 0.0476 | 0.0055 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × edad_nacionalidad | 0.1056 | 0.1058 | 0.0002 | ✅ |
| nacionalidad_top_sexo_edad | sexo × edad_nacionalidad | 0.0575 | 0.0577 | 0.0002 | ✅ |
| tipo_hogar_edad4_ref | tipo_hogar × edad_4 | 0.1814 | 0.1800 | 0.0014 | ✅ |

## Minorías, primera pasada (2026-01-01_ES_1000000_s1)

| grupo | unidad | esperado | observado | ratio | ok_representacion | donantes_distintos | top5 | ok_concentracion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mayores_85 | persona | 32790.6831 | 32777.0000 | 0.9996 | ✅ | 29283 | 0.0015 | ✅ |
| municipios_menos_2000 | persona | 54707.9467 | 56110.0000 | 1.0256 | ✅ | 24993 | 0.0017 | ✅ |
| parados | persona | 50989.6526 | 50599.0000 | 0.9923 | ✅ | 43836 | 0.0008 | ✅ |
| monoparentales | hogar | 46941.2715 | 46870.0000 | 0.9985 | ✅ | 46529 | 0.0005 | ✅ |
| mayores_solos | persona | 49222.4890 | 48870.0000 | 0.9928 | ✅ | 48599 | 0.0003 | ✅ |
| ceuta_melilla | persona | 3449.2361 | 3448.0000 | 0.9996 | ✅ | 1077 | 0.0191 | ✅ |
| nacionalidad_alemania | persona | 2749.8973 | 2740.0000 | 0.9964 | ✅ | 1953 | 0.0117 | ✅ |
| nacionalidad_argentina | persona | 3114.4501 | 3119.0000 | 1.0015 | ✅ | 2165 | 0.0093 | ✅ |
| nacionalidad_china | persona | 4967.5077 | 4985.0000 | 1.0035 | ✅ | 1600 | 0.0134 | ✅ |
| nacionalidad_colombia | persona | 14240.1772 | 14148.0000 | 0.9935 | ✅ | 7308 | 0.0055 | ✅ |
| nacionalidad_ecuador | persona | 2767.7786 | 2779.0000 | 1.0041 | ✅ | 1813 | 0.0162 | ✅ |
| nacionalidad_francia | persona | 2656.4299 | 2658.0000 | 1.0006 | ✅ | 1910 | 0.0113 | ✅ |
| nacionalidad_honduras | persona | 3666.9593 | 3644.0000 | 0.9937 | ✅ | 1779 | 0.0148 | ✅ |
| nacionalidad_italia | persona | 7186.3631 | 7206.0000 | 1.0027 | ✅ | 4706 | 0.0062 | ✅ |
| nacionalidad_marruecos | persona | 20298.8445 | 20284.0000 | 0.9993 | ✅ | 8904 | 0.0037 | ✅ |
| nacionalidad_paraguay | persona | 2554.6119 | 2549.0000 | 0.9978 | ✅ | 1438 | 0.0161 | ✅ |
| nacionalidad_peru | persona | 5438.2659 | 5416.0000 | 0.9959 | ✅ | 2615 | 0.0164 | ✅ |
| nacionalidad_reino_unido | persona | 5615.2347 | 5642.0000 | 1.0048 | ✅ | 3553 | 0.0078 | ✅ |
| nacionalidad_rumania | persona | 12830.2068 | 12838.0000 | 1.0006 | ✅ | 5672 | 0.0045 | ✅ |
| nacionalidad_ucrania | persona | 4258.9620 | 4250.0000 | 0.9979 | ✅ | 1725 | 0.0141 | ✅ |
| nacionalidad_venezuela | persona | 7936.8739 | 7904.0000 | 0.9959 | ✅ | 3938 | 0.0068 | ✅ |

## Reglas blandas (media de 5 semillas; nº de semillas dentro)

| regla | N | frecuencia_donantes | exceso_relativo | ok_estricto | ok |
| --- | --- | --- | --- | --- | --- |
| casado_menor_20 | 10000 | 0.000054 | -0.254451 | 3 | 5 |
| casado_menor_20 | 50000 | 0.000054 | -0.108521 | 2 | 5 |
| casado_menor_20 | 100000 | 0.000054 | -0.034737 | 3 | 4 |
| casado_menor_20 | 500000 | 0.000054 | -0.116563 | 5 | 5 |
| casado_menor_20 | 1000000 | 0.000054 | 0.031882 | 3 | 5 |
| estudiante_50_o_mas | 10000 | 0.000577 | -0.547634 | 5 | 5 |
| estudiante_50_o_mas | 50000 | 0.000577 | -0.146196 | 5 | 5 |
| estudiante_50_o_mas | 100000 | 0.000577 | -0.056409 | 5 | 5 |
| estudiante_50_o_mas | 500000 | 0.000577 | -0.005874 | 5 | 5 |
| estudiante_50_o_mas | 1000000 | 0.000577 | -0.002097 | 5 | 5 |
| hogar_8_o_mas | 10000 | 0.016293 | -0.207973 | 5 | 5 |
| hogar_8_o_mas | 50000 | 0.016293 | -0.073674 | 4 | 5 |
| hogar_8_o_mas | 100000 | 0.016293 | -0.052890 | 5 | 5 |
| hogar_8_o_mas | 500000 | 0.016293 | -0.011179 | 5 | 5 |
| hogar_8_o_mas | 1000000 | 0.016293 | -0.025066 | 5 | 5 |
| incapacidad_menor_25 | 10000 | 0.000062 | -0.347744 | 3 | 5 |
| incapacidad_menor_25 | 50000 | 0.000062 | -0.544474 | 5 | 5 |
| incapacidad_menor_25 | 100000 | 0.000062 | -0.674777 | 5 | 5 |
| incapacidad_menor_25 | 500000 | 0.000062 | -0.030947 | 5 | 5 |
| incapacidad_menor_25 | 1000000 | 0.000062 | -0.021230 | 5 | 5 |
| jubilado_menor_50 | 10000 | 0.000009 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 50000 | 0.000009 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 100000 | 0.000009 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 500000 | 0.000009 | -0.692905 | 5 | 5 |
| jubilado_menor_50 | 1000000 | 0.000009 | -0.188388 | 5 | 5 |
| ocupado_75_o_mas | 10000 | 0.001496 | -0.007602 | 3 | 5 |
| ocupado_75_o_mas | 50000 | 0.001496 | -0.015452 | 4 | 5 |
| ocupado_75_o_mas | 100000 | 0.001496 | -0.015954 | 5 | 5 |
| ocupado_75_o_mas | 500000 | 0.001496 | 0.003992 | 5 | 5 |
| ocupado_75_o_mas | 1000000 | 0.001496 | 0.005423 | 5 | 5 |
| superior_20_21 | 10000 | 0.003350 | -0.143251 | 5 | 5 |
| superior_20_21 | 50000 | 0.003350 | -0.011622 | 5 | 5 |
| superior_20_21 | 100000 | 0.003350 | -0.009131 | 5 | 5 |
| superior_20_21 | 500000 | 0.003350 | -0.010438 | 5 | 5 |
| superior_20_21 | 1000000 | 0.003350 | -0.005400 | 5 | 5 |
| viudo_menor_30 | 10000 | 0.000062 | -0.675757 | 4 | 5 |
| viudo_menor_30 | 50000 | 0.000062 | 0.035717 | 3 | 5 |
| viudo_menor_30 | 100000 | 0.000062 | -0.223513 | 4 | 5 |
| viudo_menor_30 | 500000 | 0.000062 | -0.113612 | 5 | 5 |
| viudo_menor_30 | 1000000 | 0.000062 | -0.019828 | 5 | 5 |

## G4.7 · Sobremuestreo (edad>=85:10000, 2026-01-01_ES_100000_s1_sm7d9288)

Miembros del grupo: 9917 (mínimo pedido 10000); α = 0.8696, β = 3.0490; suma de pesos 100122.

| objetivo | tvd | n_efectivo | umbral | ok |
| --- | --- | --- | --- | --- |
| actividad_nacionalidad | 0.0038 | 90889.2969 | 0.0115 | ✅ |
| actividad_tramo | 0.0094 | 90889.2969 | 0.0136 | ✅ |
| edad5_sexo | 0.0019 | 90889.2969 | 0.0131 | ✅ |
| edad5_sexo_colectivos | 0.0380 | 813.8032 | 0.1211 | ✅ |
| edad5_sexo_familiares | 0.0019 | 90090.5149 | 0.0133 | ✅ |
| estado_civil_edad | 0.0021 | 90889.2969 | 0.0097 | ✅ |
| estudios_edad | 0.0022 | 90889.2969 | 0.0121 | ✅ |
| nacimiento_nacionalidad | 0.0011 | 90889.2969 | 0.0051 | ✅ |
| nacionalidad | 0.0006 | 90889.2969 | 0.0055 | ✅ |
| nacionalidad_edad | 0.0018 | 90889.2969 | 0.0126 | ✅ |
| nacionalidad_top | 0.0011 | 90889.2969 | 0.0058 | ✅ |
| nacionalidad_top_edad | 0.0020 | 90889.2969 | 0.0115 | ✅ |
| sin_estudios_edad | 0.0009 | 90889.2969 | 0.0098 | ✅ |
| tamano_hogar | 0.0008 | 36552.6838 | 0.0093 | ✅ |
| tipo_hogar | 0.0025 | 36552.6838 | 0.0122 | ✅ |
| urbanizacion | 0.0005 | 90889.2969 | 0.0058 | ✅ |

## V-DONANTES (2026-01-01_ES_1000000_s1)

| territorio | personas | hogares_donantes | kish | proporcion_local | ok | confianza_reducida |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 176436 | 70086 | 53692.938 | 0.997 | ✅ | ❌ |
| CCAA:02 | 27864 | 11674 | 8729.116 | 0.998 | ✅ | ❌ |
| CCAA:03 | 20611 | 9332 | 7053.302 | 0.994 | ✅ | ❌ |
| CCAA:04 | 25407 | 9518 | 7024.339 | 0.998 | ✅ | ❌ |
| CCAA:05 | 45847 | 17614 | 13007.181 | 0.999 | ✅ | ❌ |
| CCAA:06 | 12037 | 5036 | 3737.827 | 0.996 | ✅ | ❌ |
| CCAA:07 | 48764 | 21854 | 16261.558 | 0.992 | ✅ | ❌ |
| CCAA:08 | 43439 | 17314 | 13039.234 | 0.999 | ✅ | ❌ |
| CCAA:09 | 165355 | 65419 | 49158.454 | 1.000 | ✅ | ❌ |
| CCAA:10 | 111439 | 44978 | 34042.634 | 0.989 | ✅ | ❌ |
| CCAA:11 | 21266 | 9052 | 6902.783 | 0.995 | ✅ | ❌ |
| CCAA:12 | 54997 | 23083 | 17427.732 | 0.992 | ✅ | ❌ |
| CCAA:13 | 144525 | 56065 | 42455.858 | 1.000 | ✅ | ❌ |
| CCAA:14 | 32380 | 11908 | 9032.257 | 0.998 | ✅ | ❌ |
| CCAA:15 | 13922 | 5522 | 4091.663 | 1.000 | ✅ | ❌ |
| CCAA:16 | 45420 | 19560 | 14821.298 | 0.999 | ✅ | ❌ |
| CCAA:17 | 6642 | 2801 | 2078.011 | 0.998 | ✅ | ❌ |
| CCAA:18 | 1694 | 537 | 381.905 | 0.994 | ✅ | ❌ |
| CCAA:19 | 1754 | 540 | 390.818 | 0.978 | ✅ | ❌ |
| ES | 999799 | 401337 | 300738.170 | 0.997 | ✅ | ❌ |

## V-RAREZA

| nivel | combinaciones | sin_donante | personas_afectadas | ok |
| --- | --- | --- | --- | --- |
| persona | 24936 | 0 | 0 | ✅ |
| persona_y_hogar | 158833 | 0 | 0 | ✅ |

## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)

### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)

| ccaa | sint_ocupado | ref_ocupado | sint_parado | ref_parado | paro_sint | paro_epa | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.4972 | 0.4935 | 0.0851 | 0.0841 | 0.1461 | 0.1456 | 0.0048 | ✅ |
| 02 | 0.5502 | 0.5414 | 0.0456 | 0.0482 | 0.0766 | 0.0817 | 0.0087 | ✅ |
| 03 | 0.4773 | 0.4763 | 0.0525 | 0.0478 | 0.0992 | 0.0912 | 0.0057 | ✅ |
| 04 | 0.5928 | 0.6297 | 0.0377 | 0.0410 | 0.0598 | 0.0611 | 0.0401 | ✅ |
| 05 | 0.5308 | 0.5206 | 0.0710 | 0.0683 | 0.1180 | 0.1160 | 0.0130 | ✅ |
| 06 | 0.5129 | 0.5149 | 0.0486 | 0.0408 | 0.0865 | 0.0734 | 0.0078 | ✅ |
| 07 | 0.5036 | 0.4991 | 0.0460 | 0.0456 | 0.0837 | 0.0837 | 0.0050 | ✅ |
| 08 | 0.5296 | 0.5227 | 0.0694 | 0.0700 | 0.1159 | 0.1181 | 0.0069 | ✅ |
| 09 | 0.5751 | 0.5717 | 0.0478 | 0.0490 | 0.0767 | 0.0790 | 0.0035 | ✅ |
| 10 | 0.5277 | 0.5245 | 0.0638 | 0.0640 | 0.1078 | 0.1088 | 0.0032 | ✅ |
| 11 | 0.4859 | 0.4761 | 0.0763 | 0.0725 | 0.1357 | 0.1322 | 0.0135 | ✅ |
| 12 | 0.4963 | 0.4881 | 0.0431 | 0.0421 | 0.0799 | 0.0794 | 0.0092 | ✅ |
| 13 | 0.5926 | 0.5908 | 0.0470 | 0.0485 | 0.0735 | 0.0758 | 0.0018 | ✅ |
| 14 | 0.5497 | 0.5530 | 0.0643 | 0.0672 | 0.1047 | 0.1083 | 0.0062 | ✅ |
| 15 | 0.5467 | 0.5368 | 0.0497 | 0.0471 | 0.0834 | 0.0807 | 0.0124 | ✅ |
| 16 | 0.5262 | 0.5170 | 0.0439 | 0.0396 | 0.0770 | 0.0711 | 0.0135 | ✅ |
| 17 | 0.5494 | 0.5373 | 0.0452 | 0.0516 | 0.0761 | 0.0877 | 0.0121 | ✅ |
| 18 | 0.4832 | 0.5361 | 0.1557 | 0.1548 | 0.2437 | 0.2241 | 0.0529 | ✅ |
| 19 | 0.4924 | 0.4116 | 0.1295 | 0.1077 | 0.2082 | 0.2074 | 0.1025 | ❌ |

### ECV 2025: personas por tamaño del hogar

| ccaa | sint_1 | sint_2 | sint_3 | sint_4 | sint_5+ | ref_1 | ref_2 | ref_3 | ref_4 | ref_5+ | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.1084 | 0.2255 | 0.2406 | 0.2656 | 0.1599 | 0.1071 | 0.2233 | 0.2409 | 0.2579 | 0.1708 | 0.0113 | ✅ |
| 02 | 0.1311 | 0.2433 | 0.2414 | 0.2501 | 0.1341 | 0.1283 | 0.2440 | 0.2449 | 0.2330 | 0.1499 | 0.0199 | ✅ |
| 03 | 0.1560 | 0.2910 | 0.2623 | 0.1870 | 0.1037 | 0.1546 | 0.2897 | 0.2655 | 0.1834 | 0.1068 | 0.0063 | ✅ |
| 04 | 0.0966 | 0.2072 | 0.2300 | 0.2391 | 0.2271 | 0.0970 | 0.2062 | 0.2313 | 0.2235 | 0.2420 | 0.0166 | ✅ |
| 05 | 0.1060 | 0.2094 | 0.2442 | 0.2204 | 0.2200 | 0.1053 | 0.2082 | 0.2429 | 0.1773 | 0.2663 | 0.0464 | ✅ |
| 06 | 0.1313 | 0.2502 | 0.2491 | 0.2291 | 0.1403 | 0.1295 | 0.2462 | 0.2512 | 0.2192 | 0.1539 | 0.0158 | ✅ |
| 07 | 0.1590 | 0.2629 | 0.2439 | 0.2191 | 0.1151 | 0.1573 | 0.2606 | 0.2455 | 0.2055 | 0.1311 | 0.0177 | ✅ |
| 08 | 0.1159 | 0.2217 | 0.2343 | 0.2553 | 0.1729 | 0.1150 | 0.2211 | 0.2357 | 0.2707 | 0.1574 | 0.0168 | ✅ |
| 09 | 0.1048 | 0.2358 | 0.2361 | 0.2392 | 0.1841 | 0.1040 | 0.2350 | 0.2371 | 0.2288 | 0.1951 | 0.0119 | ✅ |
| 10 | 0.1150 | 0.2361 | 0.2407 | 0.2420 | 0.1662 | 0.1147 | 0.2369 | 0.2428 | 0.2297 | 0.1760 | 0.0126 | ✅ |
| 11 | 0.1362 | 0.2512 | 0.2485 | 0.2583 | 0.1057 | 0.1335 | 0.2483 | 0.2488 | 0.2437 | 0.1257 | 0.0203 | ✅ |
| 12 | 0.1302 | 0.2442 | 0.2535 | 0.2226 | 0.1494 | 0.1296 | 0.2435 | 0.2530 | 0.2226 | 0.1513 | 0.0019 | ✅ |
| 13 | 0.1005 | 0.2226 | 0.2340 | 0.2519 | 0.1911 | 0.0985 | 0.2196 | 0.2330 | 0.2468 | 0.2020 | 0.0110 | ✅ |
| 14 | 0.0896 | 0.1967 | 0.2234 | 0.2705 | 0.2198 | 0.0888 | 0.1939 | 0.2219 | 0.2586 | 0.2368 | 0.0170 | ✅ |
| 15 | 0.1155 | 0.2230 | 0.2249 | 0.2552 | 0.1814 | 0.1152 | 0.2216 | 0.2264 | 0.2519 | 0.1848 | 0.0049 | ✅ |
| 16 | 0.1364 | 0.2663 | 0.2335 | 0.2382 | 0.1256 | 0.1337 | 0.2655 | 0.2360 | 0.2353 | 0.1295 | 0.0064 | ✅ |
| 17 | 0.1395 | 0.2505 | 0.2357 | 0.2463 | 0.1280 | 0.1364 | 0.2489 | 0.2398 | 0.2354 | 0.1396 | 0.0157 | ✅ |
| 18 | 0.0715 | 0.1466 | 0.1857 | 0.2067 | 0.3894 | 0.0587 | 0.1663 | 0.2109 | 0.2097 | 0.3543 | 0.0479 | ✅ |
| 19 | 0.0641 | 0.1410 | 0.1802 | 0.2034 | 0.4113 | 0.0733 | 0.1110 | 0.1503 | 0.2119 | 0.4536 | 0.0600 | ✅ |

### Padrón 01/01/2022: proporción de extranjeros por provincia

| provincia | sint_extranjera | ref_extranjera | tvd | dentro |
| --- | --- | --- | --- | --- |
| 01 | 0.1302 | 0.0987 | 0.0315 | ✅ |
| 02 | 0.0995 | 0.0714 | 0.0280 | ✅ |
| 03 | 0.2545 | 0.2044 | 0.0500 | ✅ |
| 04 | 0.2572 | 0.2189 | 0.0383 | ✅ |
| 05 | 0.1009 | 0.0663 | 0.0345 | ✅ |
| 06 | 0.0469 | 0.0319 | 0.0150 | ✅ |
| 07 | 0.2167 | 0.1887 | 0.0280 | ✅ |
| 08 | 0.1803 | 0.1548 | 0.0255 | ✅ |
| 09 | 0.1096 | 0.0835 | 0.0262 | ✅ |
| 10 | 0.0497 | 0.0357 | 0.0141 | ✅ |
| 11 | 0.0506 | 0.0419 | 0.0088 | ✅ |
| 12 | 0.2090 | 0.1540 | 0.0550 | ✅ |
| 13 | 0.0738 | 0.0644 | 0.0094 | ✅ |
| 14 | 0.0364 | 0.0279 | 0.0085 | ✅ |
| 15 | 0.0650 | 0.0416 | 0.0234 | ✅ |
| 16 | 0.1463 | 0.1164 | 0.0299 | ✅ |
| 17 | 0.2287 | 0.2046 | 0.0241 | ✅ |
| 18 | 0.0973 | 0.0750 | 0.0222 | ✅ |
| 19 | 0.1914 | 0.1388 | 0.0525 | ✅ |
| 20 | 0.0994 | 0.0847 | 0.0147 | ✅ |
| 21 | 0.1104 | 0.0968 | 0.0136 | ✅ |
| 22 | 0.1649 | 0.1321 | 0.0328 | ✅ |
| 23 | 0.0435 | 0.0283 | 0.0151 | ✅ |
| 24 | 0.0686 | 0.0456 | 0.0230 | ✅ |
| 25 | 0.2141 | 0.1887 | 0.0254 | ✅ |
| 26 | 0.1530 | 0.1305 | 0.0224 | ✅ |
| 27 | 0.0796 | 0.0520 | 0.0276 | ✅ |
| 28 | 0.1670 | 0.1407 | 0.0263 | ✅ |
| 29 | 0.1919 | 0.1673 | 0.0246 | ✅ |
| 30 | 0.1632 | 0.1480 | 0.0151 | ✅ |
| 31 | 0.1348 | 0.1106 | 0.0241 | ✅ |
| 32 | 0.0786 | 0.0543 | 0.0243 | ✅ |
| 33 | 0.0753 | 0.0454 | 0.0299 | ✅ |
| 34 | 0.0680 | 0.0473 | 0.0207 | ✅ |
| 35 | 0.1476 | 0.1265 | 0.0212 | ✅ |
| 36 | 0.0689 | 0.0412 | 0.0278 | ✅ |
| 37 | 0.0765 | 0.0487 | 0.0279 | ✅ |
| 38 | 0.1560 | 0.1389 | 0.0171 | ✅ |
| 39 | 0.0846 | 0.0636 | 0.0210 | ✅ |
| 40 | 0.1503 | 0.1185 | 0.0319 | ✅ |
| 41 | 0.0597 | 0.0411 | 0.0185 | ✅ |
| 42 | 0.1550 | 0.0996 | 0.0554 | ✅ |
| 43 | 0.1938 | 0.1681 | 0.0257 | ✅ |
| 44 | 0.1302 | 0.1161 | 0.0141 | ✅ |
| 45 | 0.1424 | 0.1042 | 0.0381 | ✅ |
| 46 | 0.1680 | 0.1170 | 0.0510 | ✅ |
| 47 | 0.0883 | 0.0568 | 0.0315 | ✅ |
| 48 | 0.0979 | 0.0785 | 0.0193 | ✅ |
| 49 | 0.0635 | 0.0379 | 0.0255 | ✅ |
| 50 | 0.1575 | 0.1235 | 0.0340 | ✅ |
| 51 | 0.0691 | 0.0591 | 0.0100 | ✅ |
| 52 | 0.1317 | 0.1371 | 0.0054 | ✅ |

## V-REPRO

2026-01-01_ES_10000_s1 generado de nuevo en otro directorio: mismos hashes.

- `persons.parquet`: `bb38a3fdf2301e70c67a2a0cd509d477201b25345f8608996fd1d2dfec0dc018`
- `households.parquet`: `a3d7a8dd799dcd2ae5d231828b21cd4c62c129e0c4f620ce98095a476030ce34`
- `lineage.parquet`: `d1af7d4e8ea9ba241f1913c1a83897d77f4e17b6d7072bc0d9b73894c3a86407`
