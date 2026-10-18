# Fase 04 · Tablas de validación

Generado por `python -m sinpop.validate.fase4` (git:0a2022f-dirty, 2026-10-18). Resumen en `fase_04_validacion.json`; detalle por población en `fase_04/`.

## Curva de error frente a tamaño (España; media de 5 semillas)

| n | tvd_media_calibradas | sd_calibradas | tvd_media_reservadas | sd_reservadas |
| --- | --- | --- | --- | --- |
| 10000 | 0.0186 | 0.0011 | 0.0167 | 0.0011 |
| 50000 | 0.0058 | 0.0003 | 0.0101 | 0.0003 |
| 100000 | 0.0032 | 0.0002 | 0.0089 | 0.0002 |
| 500000 | 0.0012 | 0.0001 | 0.0081 | 0.0001 |
| 1000000 | 0.0008 | 0.0000 | 0.0079 | 0.0000 |

## TVD por marginal calibrada (España; media de 5 semillas)

| objetivo | 500000 | 100000 | 50000 | 1000000 | 10000 |
| --- | --- | --- | --- | --- | --- |
| actividad_tramo | 0.0014 | 0.0026 | 0.0034 | 0.0009 | 0.0069 |
| edad5_sexo | 0.0008 | 0.0016 | 0.0020 | 0.0006 | 0.0045 |
| edad5_sexo_colectivos | 0.0113 | 0.0358 | 0.0737 | 0.0074 | 0.2533 |
| edad5_sexo_familiares | 0.0008 | 0.0016 | 0.0022 | 0.0006 | 0.0046 |
| estado_civil_edad | 0.0008 | 0.0018 | 0.0025 | 0.0006 | 0.0058 |
| estudios_edad | 0.0009 | 0.0018 | 0.0025 | 0.0006 | 0.0050 |
| nacimiento_nacionalidad | 0.0005 | 0.0009 | 0.0008 | 0.0003 | 0.0026 |
| nacionalidad | 0.0003 | 0.0005 | 0.0006 | 0.0002 | 0.0023 |
| nacionalidad_edad | 0.0007 | 0.0013 | 0.0016 | 0.0006 | 0.0052 |
| nacionalidad_top | 0.0002 | 0.0002 | 0.0003 | 0.0002 | 0.0016 |
| nacionalidad_top_edad | 0.0004 | 0.0009 | 0.0012 | 0.0003 | 0.0028 |
| sin_estudios_edad | 0.0004 | 0.0008 | 0.0012 | 0.0003 | 0.0025 |
| tamano_hogar | 0.0003 | 0.0007 | 0.0011 | 0.0002 | 0.0030 |
| tipo_hogar | 0.0008 | 0.0017 | 0.0022 | 0.0004 | 0.0066 |
| tipo_residencia (implícito) | 0.0000 | 0.0000 | 0.0001 | 0.0000 | 0.0007 |
| trabajo_nacionalidad | 0.0011 | 0.0023 | 0.0029 | 0.0008 | 0.0061 |
| urbanizacion | 0.0002 | 0.0003 | 0.0009 | 0.0002 | 0.0022 |

## TVD por cruce reservado (España; media de 5 semillas)

| objetivo | 10000 | 100000 | 50000 | 1000000 | 500000 |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | 0.0193 | 0.0119 | 0.0136 | 0.0110 | 0.0112 |
| actividad_sexo | 0.0091 | 0.0065 | 0.0070 | 0.0053 | 0.0056 |
| adultos_nacionalidad | 0.0026 | 0.0017 | 0.0019 | 0.0017 | 0.0017 |
| estudios_sexo_edad | 0.0163 | 0.0084 | 0.0104 | 0.0069 | 0.0074 |
| nacionalidad_top_sexo_edad | 0.0167 | 0.0065 | 0.0085 | 0.0048 | 0.0049 |
| provincia_si_calibra_ccaa | 0.0290 | 0.0101 | 0.0123 | 0.0091 | 0.0091 |
| tamano_municipio | 0.0159 | 0.0116 | 0.0110 | 0.0111 | 0.0111 |
| tipo_hogar_edad4_ref | 0.0250 | 0.0145 | 0.0158 | 0.0136 | 0.0139 |

## Fallos por tamaño

| N | semilla | v_marg | v_cruce | v_cruce_excepciones | v_cruce_estricto | comprobaciones_cruce |
| --- | --- | --- | --- | --- | --- | --- |
| 10000 | 1 | 0 | 16 | 1 | 33 | 511 |
| 10000 | 2 | 0 | 10 | 0 | 28 | 511 |
| 10000 | 3 | 0 | 13 | 0 | 28 | 511 |
| 10000 | 4 | 0 | 10 | 0 | 23 | 511 |
| 10000 | 5 | 0 | 12 | 0 | 26 | 511 |
| 50000 | 1 | 0 | 2 | 1 | 6 | 511 |
| 50000 | 2 | 0 | 2 | 1 | 4 | 511 |
| 50000 | 3 | 0 | 1 | 0 | 5 | 511 |
| 50000 | 4 | 0 | 2 | 0 | 6 | 511 |
| 50000 | 5 | 0 | 3 | 0 | 5 | 511 |
| 100000 | 1 | 0 | 1 | 0 | 1 | 511 |
| 100000 | 2 | 0 | 0 | 0 | 3 | 511 |
| 100000 | 3 | 0 | 0 | 1 | 2 | 511 |
| 100000 | 4 | 0 | 0 | 1 | 4 | 511 |
| 100000 | 5 | 0 | 0 | 0 | 1 | 511 |
| 500000 | 1 | 0 | 0 | 1 | 1 | 511 |
| 500000 | 2 | 0 | 0 | 1 | 1 | 511 |
| 500000 | 3 | 0 | 0 | 1 | 3 | 511 |
| 500000 | 4 | 0 | 0 | 0 | 0 | 511 |
| 500000 | 5 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 1 | 0 | 0 | 1 | 2 | 511 |
| 1000000 | 2 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 3 | 0 | 0 | 1 | 2 | 511 |
| 1000000 | 4 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 5 | 0 | 0 | 1 | 1 | 511 |

### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas

| nivel | territorio | objetivo | tvd | umbral | excepcion | N | semilla |
| --- | --- | --- | --- | --- | --- | --- | --- |
| provincia | PROV:40 | tamano_municipio | 0.0817 | 0.0800 | ✅ | 500000 | 1 |
| provincia | PROV:40 | tamano_municipio | 0.0822 | 0.0800 | ✅ | 500000 | 2 |
| provincia | PROV:40 | tamano_municipio | 0.0808 | 0.0800 | ✅ | 500000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0821 | 0.0800 | ✅ | 500000 | 5 |
| provincia | PROV:40 | tamano_municipio | 0.0837 | 0.0800 | ✅ | 1000000 | 1 |
| provincia | PROV:40 | tamano_municipio | 0.0837 | 0.0800 | ✅ | 1000000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0827 | 0.0800 | ✅ | 1000000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0832 | 0.0800 | ✅ | 1000000 | 5 |

## V-SEMILLAS

| n | proporciones | fuera | razon_media | razon_max |
| --- | --- | --- | --- | --- |
| 10000 | 463 | 0 | 0.3060 | 1.1438 |
| 50000 | 463 | 0 | 0.2221 | 1.0332 |
| 100000 | 463 | 0 | 0.2112 | 0.8944 |
| 500000 | 463 | 0 | 0.2311 | 0.7997 |
| 1000000 | 463 | 0 | 0.2267 | 0.5957 |

## V-PESOS (calibración por comunidades)

| bloque | desviacion_max | proporcion_en_rango | kish_ratio | no_positivos | factor_min | factor_max | proporcion_local | ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 0.0000 | 1.0000 | 0.7676 | 0 | 0.2000 | 5.0000 | 0.9988 | ✅ |
| CCAA:02 | 0.0000 | 1.0000 | 0.7777 | 0 | 0.2000 | 4.9998 | 0.9994 | ✅ |
| CCAA:03 | 0.0000 | 1.0000 | 0.7547 | 0 | 0.2000 | 5.0000 | 0.9977 | ✅ |
| CCAA:04 | 0.0005 | 1.0000 | 0.5845 | 0 | 0.2000 | 5.0000 | 0.9996 | ✅ |
| CCAA:05 | 0.0000 | 1.0000 | 0.6889 | 0 | 0.2000 | 4.9998 | 0.9997 | ✅ |
| CCAA:06 | 0.0000 | 1.0000 | 0.7584 | 0 | 0.2000 | 4.9997 | 0.9982 | ✅ |
| CCAA:07 | 0.0000 | 1.0000 | 0.7833 | 0 | 0.2000 | 5.0000 | 0.9973 | ✅ |
| CCAA:08 | 0.0000 | 1.0000 | 0.7449 | 0 | 0.2000 | 5.0000 | 0.9996 | ✅ |
| CCAA:09 | 0.0000 | 1.0000 | 0.7066 | 0 | 0.2000 | 5.0000 | 1.0000 | ✅ |
| CCAA:10 | 0.0000 | 1.0000 | 0.6916 | 0 | 0.2000 | 5.0000 | 0.9967 | ✅ |
| CCAA:11 | 0.0000 | 1.0000 | 0.8000 | 0 | 0.2000 | 4.9985 | 0.9984 | ✅ |
| CCAA:12 | 0.0000 | 1.0000 | 0.7693 | 0 | 0.2000 | 5.0000 | 0.9975 | ✅ |
| CCAA:13 | 0.0000 | 1.0000 | 0.7260 | 0 | 0.2000 | 5.0000 | 1.0000 | ✅ |
| CCAA:14 | 0.0000 | 1.0000 | 0.7311 | 0 | 0.2000 | 5.0000 | 0.9990 | ✅ |
| CCAA:15 | 0.0000 | 1.0000 | 0.7570 | 0 | 0.2000 | 4.9994 | 0.9998 | ✅ |
| CCAA:16 | 0.0000 | 1.0000 | 0.7708 | 0 | 0.2000 | 5.0000 | 0.9997 | ✅ |
| CCAA:17 | 0.0000 | 1.0000 | 0.7685 | 0 | 0.2001 | 4.9388 | 0.9989 | ✅ |
| CCAA:18 | 0.0000 | 1.0000 | 0.6261 | 0 | 0.2000 | 4.9998 | 0.9836 | ✅ |
| CCAA:19 | 0.0000 | 1.0000 | 0.6195 | 0 | 0.2000 | 4.9303 | 0.9817 | ✅ |

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
| CCAA:04 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | 4 | 1.1645 | 1 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | 3 | 4.1838 | 2 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 18 | 3.6435 | 8 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 5 | 4.4893 | 5 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 14 | 3.5343 | 6 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 15 | 4.5170 | 12 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | 17 | 3.6002 | 8 | None |
| CCAA:06 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | 0 | None | 5 | None |
| CCAA:06 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 2 | 2.9902 | 3 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 3 | 1.8881 | 2 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 5 | 4.1204 | 4 | None |
| CCAA:06 | trabajo_nacionalidad | trabaja=si;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-24 | 57 | 3.7805 | 29 | None |
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
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 532 | 3.5074 | 220 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 46 | 4.7211 | 37 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 52 | 3.8889 | 29 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 323 | 3.9135 | 180 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 99 | 4.1809 | 64 | None |
| CCAA:10 | trabajo_nacionalidad | trabaja=si;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 247 | 3.9260 | 143 | None |
| CCAA:11 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 4 | 2.2126 | 1 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=peru | 36 | 3.7553 | 17 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 41 | 3.9237 | 27 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 19 | 3.6215 | 9 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=todas | 36 | 3.7553 | 13 | None |
| CCAA:11 | trabajo_nacionalidad | trabaja=si;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 7 | 4.0999 | 5 | None |
| CCAA:12 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | 4 | 3.5585 | 1 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=peru | 207 | 3.7108 | 93 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=ucrania | 40 | 3.5008 | 18 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | 2 | 3.6488 | 3 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 94 | 4.1935 | 61 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 47 | 4.6418 | 44 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 78 | 3.7693 | 49 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 14 | 4.4851 | 13 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 2 | 11.0122 | 3 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | 5 | 3.8028 | 3 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | 24 | 3.5464 | 8 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 12 | 3.7354 | 7 | None |
| CCAA:14 | trabajo_nacionalidad | trabaja=si;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 63 | 4.0051 | 38 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | 2 | 2.6115 | 3 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | 6 | 3.6824 | 3 | None |
| CCAA:16 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 4 | 4.5891 | 1 | None |
| CCAA:16 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 8 | 4.4910 | 7 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | 2 | 7.0517 | 3 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 7 | 5.9836 | 9 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 11 | 3.7788 | 5 | None |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | 3 | 4.4321 | 2 | None |
| CCAA:17 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 1 | 5.7627 | 4 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 8.1332 | 4 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.9987 | 3 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=paraguay | 4 | 4.3333 | 1 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=todas | 4 | 4.3333 | 1 | None |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | 2 | 0.8481 | 3 | None |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | 1 | 1.1128 | 4 | None |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | 3 | 2.4142 | 2 | None |
| CCAA:18 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 4 | 0.6403 | 1 | None |
| CCAA:18 | estudios_edad | estudios_3=superior;edad_estudios=90+ | 3 | 2.0488 | 2 | None |
| CCAA:18 | nacionalidad | nacionalidad_grupo=otros | 0 | None | 5 | None |
| CCAA:18 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.5142 | 1 | None |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 1.9579 | 4 | None |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.3251 | 3 | None |
| CCAA:18 | nacionalidad_top | nacionalidad_top=china | 1 | 2.3948 | 4 | None |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=todas | 1 | 2.3948 | 4 | None |
| CCAA:18 | trabajo_nacionalidad | trabaja=si;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-24 | 2 | 3.2879 | 3 | None |
| CCAA:18 | trabajo_nacionalidad | trabaja=si;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 11 | 4.1869 | 7 | None |
| CCAA:18 | trabajo_nacionalidad | trabaja=si;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 2 | 2.5738 | 3 | None |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | 2 | 0.7449 | 3 | None |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=35-44 | 4 | 0.9478 | 1 | None |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | 4 | 2.1815 | 1 | None |
| CCAA:19 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 1 | 1.3271 | 4 | None |
| CCAA:19 | estudios_edad | estudios_3=secundaria_2a_etapa;edad_estudios=90+ | 2 | 1.3648 | 3 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=america_latina | 18 | 4.7103 | 15 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=asia | 2 | 1.6472 | 3 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=otros | 2 | 3.0749 | 3 | None |
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
| CCAA:04 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | nacionalidad_top=honduras;edad_nacionalidad=todas |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | nacionalidad_top=honduras;edad_nacionalidad=todas |
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
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
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
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=00-19 | nacionalidad_top=marruecos;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=20-34 | nacionalidad_top=marruecos;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=35-49 | nacionalidad_top=marruecos;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=50-64 | nacionalidad_top=marruecos;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=65+ | nacionalidad_top=marruecos;edad_nacionalidad=todas |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=reino_unido;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=35-49 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=50-64 | nacionalidad_top=otras_extranjeras;edad_nacionalidad=50-64 |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ |
| CCAA:18 | estado_civil_edad | estado_civil=NC;edad_estado_civil=35-54 | estado_civil=casado;edad_estado_civil=35-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
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

## V de Cramér (2026-01-01_ES_1000000_s1)

| objetivo | par | v_oficial | v_sintetica | dif | ok |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | relacion_actividad × edad_actividad | 0.6145 | 0.6187 | 0.0042 | ✅ |
| actividad_sexo | relacion_actividad × sexo | 0.2209 | 0.2185 | 0.0024 | ✅ |
| adultos_nacionalidad | nacionalidad_esp_ext × es_adulto | 0.0028 | 0.0048 | 0.0021 | ✅ |
| estudios_sexo_edad | estudios_3 × sexo | 0.0391 | 0.0349 | 0.0042 | ✅ |
| estudios_sexo_edad | estudios_3 × edad_estudios | 0.6228 | 0.6229 | 0.0001 | ✅ |
| estudios_sexo_edad | sexo × edad_estudios | 0.0713 | 0.0713 | 0.0000 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × sexo | 0.0420 | 0.0487 | 0.0067 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × edad_nacionalidad | 0.1056 | 0.1057 | 0.0001 | ✅ |
| nacionalidad_top_sexo_edad | sexo × edad_nacionalidad | 0.0575 | 0.0575 | 0.0000 | ✅ |
| tipo_hogar_edad4_ref | tipo_hogar × edad_4 | 0.1814 | 0.1803 | 0.0011 | ✅ |

## Minorías, primera pasada (2026-01-01_ES_1000000_s1)

| grupo | unidad | esperado | observado | ratio | ok_representacion | donantes_distintos | top5 | ok_concentracion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mayores_85 | persona | 32791.9622 | 32821.0000 | 1.0009 | ✅ | 29233 | 0.0015 | ✅ |
| municipios_menos_2000 | persona | 54710.0807 | 56156.0000 | 1.0264 | ✅ | 25043 | 0.0016 | ✅ |
| parados | persona | 50991.6416 | 50744.0000 | 0.9951 | ✅ | 44475 | 0.0007 | ✅ |
| monoparentales | hogar | 46941.0359 | 46907.0000 | 0.9993 | ✅ | 46541 | 0.0005 | ✅ |
| mayores_solos | persona | 49224.4091 | 48788.0000 | 0.9911 | ✅ | 48535 | 0.0002 | ✅ |
| ceuta_melilla | persona | 3449.3706 | 3453.0000 | 1.0011 | ✅ | 1069 | 0.0206 | ✅ |
| nacionalidad_alemania | persona | 2750.0046 | 2745.0000 | 0.9982 | ✅ | 1982 | 0.0098 | ✅ |
| nacionalidad_argentina | persona | 3114.5716 | 3093.0000 | 0.9931 | ✅ | 2121 | 0.0110 | ✅ |
| nacionalidad_china | persona | 4967.7014 | 4960.0000 | 0.9984 | ✅ | 1591 | 0.0117 | ✅ |
| nacionalidad_colombia | persona | 14240.7326 | 14166.0000 | 0.9948 | ✅ | 7200 | 0.0056 | ✅ |
| nacionalidad_ecuador | persona | 2767.8866 | 2777.0000 | 1.0033 | ✅ | 1811 | 0.0173 | ✅ |
| nacionalidad_francia | persona | 2656.5335 | 2660.0000 | 1.0013 | ✅ | 1935 | 0.0109 | ✅ |
| nacionalidad_honduras | persona | 3667.1023 | 3647.0000 | 0.9945 | ✅ | 1764 | 0.0140 | ✅ |
| nacionalidad_italia | persona | 7186.6434 | 7179.0000 | 0.9989 | ✅ | 4670 | 0.0057 | ✅ |
| nacionalidad_marruecos | persona | 20299.6363 | 20278.0000 | 0.9989 | ✅ | 8857 | 0.0037 | ✅ |
| nacionalidad_paraguay | persona | 2554.7116 | 2560.0000 | 1.0021 | ✅ | 1428 | 0.0156 | ✅ |
| nacionalidad_peru | persona | 5438.4780 | 5408.0000 | 0.9944 | ✅ | 2603 | 0.0168 | ✅ |
| nacionalidad_reino_unido | persona | 5615.4538 | 5631.0000 | 1.0028 | ✅ | 3549 | 0.0085 | ✅ |
| nacionalidad_rumania | persona | 12830.7072 | 12846.0000 | 1.0012 | ✅ | 5665 | 0.0046 | ✅ |
| nacionalidad_ucrania | persona | 4259.1281 | 4253.0000 | 0.9986 | ✅ | 1714 | 0.0165 | ✅ |
| nacionalidad_venezuela | persona | 7937.1835 | 7942.0000 | 1.0006 | ✅ | 3958 | 0.0078 | ✅ |

## Reglas blandas (media de 5 semillas; nº de semillas dentro)

| regla | N | frecuencia_donantes | exceso_relativo | ok_estricto | ok |
| --- | --- | --- | --- | --- | --- |
| casado_menor_20 | 10000 | 0.000051 | 1.339737 | 2 | 2 |
| casado_menor_20 | 50000 | 0.000051 | 0.010717 | 2 | 5 |
| casado_menor_20 | 100000 | 0.000051 | 0.088045 | 2 | 5 |
| casado_menor_20 | 500000 | 0.000051 | -0.028833 | 5 | 5 |
| casado_menor_20 | 1000000 | 0.000051 | 0.052638 | 3 | 5 |
| estudiante_50_o_mas | 10000 | 0.000578 | -0.652718 | 5 | 5 |
| estudiante_50_o_mas | 50000 | 0.000578 | -0.119633 | 5 | 5 |
| estudiante_50_o_mas | 100000 | 0.000578 | -0.092228 | 5 | 5 |
| estudiante_50_o_mas | 500000 | 0.000578 | -0.005240 | 5 | 5 |
| estudiante_50_o_mas | 1000000 | 0.000578 | -0.001878 | 5 | 5 |
| hogar_8_o_mas | 10000 | 0.016483 | -0.268336 | 5 | 5 |
| hogar_8_o_mas | 50000 | 0.016483 | -0.119039 | 5 | 5 |
| hogar_8_o_mas | 100000 | 0.016483 | -0.046256 | 5 | 5 |
| hogar_8_o_mas | 500000 | 0.016483 | -0.017949 | 5 | 5 |
| hogar_8_o_mas | 1000000 | 0.016483 | -0.005573 | 5 | 5 |
| incapacidad_menor_25 | 10000 | 0.000059 | -0.659730 | 4 | 5 |
| incapacidad_menor_25 | 50000 | 0.000059 | -0.932149 | 5 | 5 |
| incapacidad_menor_25 | 100000 | 0.000059 | -0.491114 | 5 | 5 |
| incapacidad_menor_25 | 500000 | 0.000059 | -0.057161 | 5 | 5 |
| incapacidad_menor_25 | 1000000 | 0.000059 | -0.013170 | 5 | 5 |
| jubilado_menor_50 | 10000 | 0.000008 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 50000 | 0.000008 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 100000 | 0.000008 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 500000 | 0.000008 | -0.617565 | 5 | 5 |
| jubilado_menor_50 | 1000000 | 0.000008 | -0.187401 | 5 | 5 |
| ocupado_75_o_mas | 10000 | 0.001497 | -0.249065 | 5 | 5 |
| ocupado_75_o_mas | 50000 | 0.001497 | 0.027246 | 4 | 5 |
| ocupado_75_o_mas | 100000 | 0.001497 | 0.050974 | 4 | 5 |
| ocupado_75_o_mas | 500000 | 0.001497 | -0.006043 | 5 | 5 |
| ocupado_75_o_mas | 1000000 | 0.001497 | 0.006153 | 5 | 5 |
| superior_20_21 | 10000 | 0.003334 | 0.011118 | 3 | 5 |
| superior_20_21 | 50000 | 0.003334 | -0.020208 | 5 | 5 |
| superior_20_21 | 100000 | 0.003334 | 0.004657 | 4 | 5 |
| superior_20_21 | 500000 | 0.003334 | -0.005387 | 5 | 5 |
| superior_20_21 | 1000000 | 0.003334 | 0.007769 | 5 | 5 |
| viudo_menor_30 | 10000 | 0.000061 | -0.013267 | 3 | 5 |
| viudo_menor_30 | 50000 | 0.000061 | 0.314011 | 2 | 5 |
| viudo_menor_30 | 100000 | 0.000061 | -0.179040 | 4 | 5 |
| viudo_menor_30 | 500000 | 0.000061 | 0.024231 | 4 | 5 |
| viudo_menor_30 | 1000000 | 0.000061 | -0.015265 | 5 | 5 |

## G4.7 · Sobremuestreo (edad>=85:10000, 2026-01-01_ES_100000_s1_sm7d9288)

Miembros del grupo: 9883 (mínimo pedido 10000); α = 0.8696, β = 3.0490; suma de pesos 100212.

| objetivo | tvd | n_efectivo | umbral | ok |
| --- | --- | --- | --- | --- |
| actividad_tramo | 0.0088 | 90946.0401 | 0.0134 | ✅ |
| edad5_sexo | 0.0027 | 90946.0401 | 0.0134 | ✅ |
| edad5_sexo_colectivos | 0.0367 | 815.7236 | 0.1192 | ✅ |
| edad5_sexo_familiares | 0.0027 | 90145.3138 | 0.0135 | ✅ |
| estado_civil_edad | 0.0020 | 90946.0401 | 0.0095 | ✅ |
| estudios_edad | 0.0021 | 90946.0401 | 0.0124 | ✅ |
| nacimiento_nacionalidad | 0.0009 | 90946.0401 | 0.0053 | ✅ |
| nacionalidad | 0.0008 | 90946.0401 | 0.0054 | ✅ |
| nacionalidad_edad | 0.0027 | 90946.0401 | 0.0125 | ✅ |
| nacionalidad_top | 0.0012 | 90946.0401 | 0.0059 | ✅ |
| nacionalidad_top_edad | 0.0023 | 90946.0401 | 0.0116 | ✅ |
| sin_estudios_edad | 0.0015 | 90946.0401 | 0.0098 | ✅ |
| tamano_hogar | 0.0002 | 36565.4187 | 0.0096 | ✅ |
| tipo_hogar | 0.0018 | 36565.4187 | 0.0124 | ✅ |
| trabajo_nacionalidad | 0.0028 | 90946.0401 | 0.0105 | ✅ |
| urbanizacion | 0.0009 | 90946.0401 | 0.0058 | ✅ |

## V-DONANTES (2026-01-01_ES_1000000_s1)

| territorio | personas | hogares_donantes | kish | proporcion_local | ok | confianza_reducida |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 176375 | 70146 | 53899.857 | 0.997 | ✅ | ❌ |
| CCAA:02 | 27867 | 11694 | 8782.837 | 0.998 | ✅ | ❌ |
| CCAA:03 | 20608 | 9310 | 6995.152 | 0.994 | ✅ | ❌ |
| CCAA:04 | 25398 | 9568 | 7128.978 | 0.999 | ✅ | ❌ |
| CCAA:05 | 45892 | 17605 | 12899.027 | 0.999 | ✅ | ❌ |
| CCAA:06 | 12036 | 5038 | 3765.865 | 0.996 | ✅ | ❌ |
| CCAA:07 | 48752 | 21817 | 16234.017 | 0.992 | ✅ | ❌ |
| CCAA:08 | 43449 | 17310 | 12992.269 | 0.999 | ✅ | ❌ |
| CCAA:09 | 165388 | 65493 | 49304.928 | 1.000 | ✅ | ❌ |
| CCAA:10 | 111471 | 45007 | 33958.672 | 0.989 | ✅ | ❌ |
| CCAA:11 | 21274 | 9069 | 6935.289 | 0.995 | ✅ | ❌ |
| CCAA:12 | 55001 | 23075 | 17394.387 | 0.992 | ✅ | ❌ |
| CCAA:13 | 144534 | 56003 | 42305.418 | 1.000 | ✅ | ❌ |
| CCAA:14 | 32368 | 11912 | 9053.955 | 0.997 | ✅ | ❌ |
| CCAA:15 | 13909 | 5522 | 4114.513 | 1.000 | ✅ | ❌ |
| CCAA:16 | 45436 | 19570 | 14832.807 | 0.999 | ✅ | ❌ |
| CCAA:17 | 6627 | 2789 | 2086.424 | 0.998 | ✅ | ❌ |
| CCAA:18 | 1696 | 531 | 357.585 | 0.993 | ✅ | ❌ |
| CCAA:19 | 1757 | 538 | 380.976 | 0.974 | ✅ | ❌ |
| ES | 999838 | 401448 | 300831.233 | 0.997 | ✅ | ❌ |

## V-RAREZA

| nivel | combinaciones | sin_donante | personas_afectadas | ok |
| --- | --- | --- | --- | --- |
| persona | 24956 | 0 | 0 | ✅ |
| persona_y_hogar | 157860 | 0 | 0 | ✅ |

## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)

### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)

| ccaa | sint_ocupado | ref_ocupado | sint_parado | ref_parado | paro_sint | paro_epa | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.4968 | 0.4935 | 0.0850 | 0.0841 | 0.1461 | 0.1456 | 0.0043 | ✅ |
| 02 | 0.5510 | 0.5414 | 0.0455 | 0.0482 | 0.0763 | 0.0817 | 0.0095 | ✅ |
| 03 | 0.4774 | 0.4763 | 0.0528 | 0.0478 | 0.0995 | 0.0912 | 0.0060 | ✅ |
| 04 | 0.5940 | 0.6297 | 0.0371 | 0.0410 | 0.0588 | 0.0611 | 0.0395 | ✅ |
| 05 | 0.5306 | 0.5206 | 0.0718 | 0.0683 | 0.1192 | 0.1160 | 0.0136 | ✅ |
| 06 | 0.5125 | 0.5149 | 0.0486 | 0.0408 | 0.0866 | 0.0734 | 0.0078 | ✅ |
| 07 | 0.5045 | 0.4991 | 0.0466 | 0.0456 | 0.0845 | 0.0837 | 0.0063 | ✅ |
| 08 | 0.5287 | 0.5227 | 0.0700 | 0.0700 | 0.1169 | 0.1181 | 0.0060 | ✅ |
| 09 | 0.5744 | 0.5717 | 0.0481 | 0.0490 | 0.0773 | 0.0790 | 0.0028 | ✅ |
| 10 | 0.5278 | 0.5245 | 0.0638 | 0.0640 | 0.1079 | 0.1088 | 0.0033 | ✅ |
| 11 | 0.4853 | 0.4761 | 0.0764 | 0.0725 | 0.1360 | 0.1322 | 0.0131 | ✅ |
| 12 | 0.4958 | 0.4881 | 0.0434 | 0.0421 | 0.0804 | 0.0794 | 0.0090 | ✅ |
| 13 | 0.5926 | 0.5908 | 0.0471 | 0.0485 | 0.0737 | 0.0758 | 0.0019 | ✅ |
| 14 | 0.5485 | 0.5530 | 0.0650 | 0.0672 | 0.1059 | 0.1083 | 0.0067 | ✅ |
| 15 | 0.5479 | 0.5368 | 0.0486 | 0.0471 | 0.0815 | 0.0807 | 0.0126 | ✅ |
| 16 | 0.5250 | 0.5170 | 0.0450 | 0.0396 | 0.0790 | 0.0711 | 0.0135 | ✅ |
| 17 | 0.5484 | 0.5373 | 0.0468 | 0.0516 | 0.0786 | 0.0877 | 0.0112 | ✅ |
| 18 | 0.4927 | 0.5361 | 0.1494 | 0.1548 | 0.2327 | 0.2241 | 0.0488 | ✅ |
| 19 | 0.4956 | 0.4116 | 0.1223 | 0.1077 | 0.1979 | 0.2074 | 0.0986 | ✅ |

### ECV 2025: personas por tamaño del hogar

| ccaa | sint_1 | sint_2 | sint_3 | sint_4 | sint_5+ | ref_1 | ref_2 | ref_3 | ref_4 | ref_5+ | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.1082 | 0.2260 | 0.2406 | 0.2664 | 0.1588 | 0.1071 | 0.2233 | 0.2409 | 0.2579 | 0.1708 | 0.0124 | ✅ |
| 02 | 0.1302 | 0.2444 | 0.2427 | 0.2508 | 0.1320 | 0.1283 | 0.2440 | 0.2449 | 0.2330 | 0.1499 | 0.0201 | ✅ |
| 03 | 0.1557 | 0.2914 | 0.2628 | 0.1888 | 0.1014 | 0.1546 | 0.2897 | 0.2655 | 0.1834 | 0.1068 | 0.0082 | ✅ |
| 04 | 0.0968 | 0.2067 | 0.2304 | 0.2370 | 0.2291 | 0.0970 | 0.2062 | 0.2313 | 0.2235 | 0.2420 | 0.0140 | ✅ |
| 05 | 0.1056 | 0.2103 | 0.2433 | 0.2219 | 0.2189 | 0.1053 | 0.2082 | 0.2429 | 0.1773 | 0.2663 | 0.0475 | ✅ |
| 06 | 0.1306 | 0.2510 | 0.2505 | 0.2291 | 0.1387 | 0.1295 | 0.2462 | 0.2512 | 0.2192 | 0.1539 | 0.0159 | ✅ |
| 07 | 0.1592 | 0.2628 | 0.2433 | 0.2202 | 0.1146 | 0.1573 | 0.2606 | 0.2455 | 0.2055 | 0.1311 | 0.0188 | ✅ |
| 08 | 0.1153 | 0.2224 | 0.2350 | 0.2557 | 0.1716 | 0.1150 | 0.2211 | 0.2357 | 0.2707 | 0.1574 | 0.0157 | ✅ |
| 09 | 0.1047 | 0.2357 | 0.2361 | 0.2392 | 0.1843 | 0.1040 | 0.2350 | 0.2371 | 0.2288 | 0.1951 | 0.0118 | ✅ |
| 10 | 0.1150 | 0.2362 | 0.2411 | 0.2421 | 0.1656 | 0.1147 | 0.2369 | 0.2428 | 0.2297 | 0.1760 | 0.0127 | ✅ |
| 11 | 0.1357 | 0.2528 | 0.2482 | 0.2551 | 0.1082 | 0.1335 | 0.2483 | 0.2488 | 0.2437 | 0.1257 | 0.0181 | ✅ |
| 12 | 0.1305 | 0.2439 | 0.2538 | 0.2217 | 0.1500 | 0.1296 | 0.2435 | 0.2530 | 0.2226 | 0.1513 | 0.0021 | ✅ |
| 13 | 0.1005 | 0.2222 | 0.2341 | 0.2517 | 0.1914 | 0.0985 | 0.2196 | 0.2330 | 0.2468 | 0.2020 | 0.0106 | ✅ |
| 14 | 0.0897 | 0.1972 | 0.2226 | 0.2727 | 0.2177 | 0.0888 | 0.1939 | 0.2219 | 0.2586 | 0.2368 | 0.0191 | ✅ |
| 15 | 0.1160 | 0.2215 | 0.2288 | 0.2514 | 0.1824 | 0.1152 | 0.2216 | 0.2264 | 0.2519 | 0.1848 | 0.0031 | ✅ |
| 16 | 0.1359 | 0.2668 | 0.2340 | 0.2388 | 0.1245 | 0.1337 | 0.2655 | 0.2360 | 0.2353 | 0.1295 | 0.0069 | ✅ |
| 17 | 0.1376 | 0.2544 | 0.2412 | 0.2402 | 0.1266 | 0.1364 | 0.2489 | 0.2398 | 0.2354 | 0.1396 | 0.0129 | ✅ |
| 18 | 0.0679 | 0.1514 | 0.1874 | 0.2282 | 0.3652 | 0.0587 | 0.1663 | 0.2109 | 0.2097 | 0.3543 | 0.0385 | ✅ |
| 19 | 0.0629 | 0.1454 | 0.1800 | 0.2147 | 0.3970 | 0.0733 | 0.1110 | 0.1503 | 0.2119 | 0.4536 | 0.0670 | ✅ |

### Padrón 01/01/2022: proporción de extranjeros por provincia

| provincia | sint_extranjera | ref_extranjera | tvd | dentro |
| --- | --- | --- | --- | --- |
| 01 | 0.1218 | 0.0987 | 0.0231 | ✅ |
| 02 | 0.0969 | 0.0714 | 0.0255 | ✅ |
| 03 | 0.2550 | 0.2044 | 0.0506 | ✅ |
| 04 | 0.2629 | 0.2189 | 0.0440 | ✅ |
| 05 | 0.0883 | 0.0663 | 0.0220 | ✅ |
| 06 | 0.0459 | 0.0319 | 0.0140 | ✅ |
| 07 | 0.2167 | 0.1887 | 0.0280 | ✅ |
| 08 | 0.1815 | 0.1548 | 0.0267 | ✅ |
| 09 | 0.1097 | 0.0835 | 0.0262 | ✅ |
| 10 | 0.0507 | 0.0357 | 0.0151 | ✅ |
| 11 | 0.0506 | 0.0419 | 0.0087 | ✅ |
| 12 | 0.2079 | 0.1540 | 0.0539 | ✅ |
| 13 | 0.0702 | 0.0644 | 0.0058 | ✅ |
| 14 | 0.0364 | 0.0279 | 0.0085 | ✅ |
| 15 | 0.0654 | 0.0416 | 0.0239 | ✅ |
| 16 | 0.1452 | 0.1164 | 0.0288 | ✅ |
| 17 | 0.2237 | 0.2046 | 0.0190 | ✅ |
| 18 | 0.0994 | 0.0750 | 0.0244 | ✅ |
| 19 | 0.1970 | 0.1388 | 0.0581 | ✅ |
| 20 | 0.1002 | 0.0847 | 0.0156 | ✅ |
| 21 | 0.1110 | 0.0968 | 0.0142 | ✅ |
| 22 | 0.1697 | 0.1321 | 0.0375 | ✅ |
| 23 | 0.0448 | 0.0283 | 0.0165 | ✅ |
| 24 | 0.0645 | 0.0456 | 0.0189 | ✅ |
| 25 | 0.2129 | 0.1887 | 0.0242 | ✅ |
| 26 | 0.1538 | 0.1305 | 0.0232 | ✅ |
| 27 | 0.0791 | 0.0520 | 0.0271 | ✅ |
| 28 | 0.1669 | 0.1407 | 0.0262 | ✅ |
| 29 | 0.1909 | 0.1673 | 0.0236 | ✅ |
| 30 | 0.1635 | 0.1480 | 0.0155 | ✅ |
| 31 | 0.1357 | 0.1106 | 0.0251 | ✅ |
| 32 | 0.0839 | 0.0543 | 0.0296 | ✅ |
| 33 | 0.0751 | 0.0454 | 0.0297 | ✅ |
| 34 | 0.0686 | 0.0473 | 0.0213 | ✅ |
| 35 | 0.1463 | 0.1265 | 0.0199 | ✅ |
| 36 | 0.0661 | 0.0412 | 0.0250 | ✅ |
| 37 | 0.0807 | 0.0487 | 0.0321 | ✅ |
| 38 | 0.1569 | 0.1389 | 0.0179 | ✅ |
| 39 | 0.0849 | 0.0636 | 0.0214 | ✅ |
| 40 | 0.1508 | 0.1185 | 0.0323 | ✅ |
| 41 | 0.0561 | 0.0411 | 0.0149 | ✅ |
| 42 | 0.1521 | 0.0996 | 0.0526 | ✅ |
| 43 | 0.1913 | 0.1681 | 0.0232 | ✅ |
| 44 | 0.1471 | 0.1161 | 0.0310 | ✅ |
| 45 | 0.1433 | 0.1042 | 0.0391 | ✅ |
| 46 | 0.1675 | 0.1170 | 0.0505 | ✅ |
| 47 | 0.0931 | 0.0568 | 0.0363 | ✅ |
| 48 | 0.1003 | 0.0785 | 0.0217 | ✅ |
| 49 | 0.0631 | 0.0379 | 0.0251 | ✅ |
| 50 | 0.1541 | 0.1235 | 0.0306 | ✅ |
| 51 | 0.0672 | 0.0591 | 0.0081 | ✅ |
| 52 | 0.1338 | 0.1371 | 0.0033 | ✅ |

## V-REPRO

2026-01-01_ES_10000_s1 generado de nuevo en otro directorio: mismos hashes.

- `persons.parquet`: `b2f0a3ecb24c9b20fedf00033118fb92a971c364510b16ed2b077e80d4783093`
- `households.parquet`: `bbffb8e9b7edaf2e8d4cfee0cfbf607eab240f8157428cd8976c9c1ee1b70b48`
- `lineage.parquet`: `d9caac312f7207359e73d03ec4e4e9f1191513c994d9a7da66515dfca34b829b`
