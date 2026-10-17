# Fase 04 · Tablas de validación

Generado por `python -m sinpop.validate.fase4` (git:dfa5054-dirty, 2026-10-17). Resumen en `fase_04_validacion.json`; detalle por población en `fase_04/`.

## Curva de error frente a tamaño (España; media de 5 semillas)

| n | tvd_media_calibradas | sd_calibradas | tvd_media_reservadas | sd_reservadas |
| --- | --- | --- | --- | --- |
| 10000 | 0.0193 | 0.0014 | 0.0178 | 0.0013 |
| 50000 | 0.0070 | 0.0004 | 0.0123 | 0.0005 |
| 100000 | 0.0037 | 0.0003 | 0.0112 | 0.0001 |
| 500000 | 0.0016 | 0.0000 | 0.0105 | 0.0001 |
| 1000000 | 0.0012 | 0.0000 | 0.0103 | 0.0001 |

## TVD por marginal calibrada (España; media de 5 semillas)

| objetivo | 500000 | 50000 | 10000 | 1000000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| actividad_tramo | 0.0076 | 0.0102 | 0.0142 | 0.0070 | 0.0095 |
| edad5_sexo | 0.0008 | 0.0019 | 0.0048 | 0.0006 | 0.0016 |
| edad5_sexo_colectivos | 0.0110 | 0.0794 | 0.2364 | 0.0068 | 0.0342 |
| edad5_sexo_familiares | 0.0008 | 0.0022 | 0.0052 | 0.0006 | 0.0016 |
| estado_civil_edad | 0.0008 | 0.0026 | 0.0064 | 0.0006 | 0.0020 |
| estudios_edad | 0.0009 | 0.0023 | 0.0049 | 0.0006 | 0.0014 |
| nacimiento_nacionalidad | 0.0005 | 0.0008 | 0.0034 | 0.0004 | 0.0008 |
| nacionalidad | 0.0003 | 0.0007 | 0.0025 | 0.0003 | 0.0005 |
| nacionalidad_edad | 0.0007 | 0.0022 | 0.0061 | 0.0006 | 0.0015 |
| nacionalidad_top | 0.0003 | 0.0009 | 0.0032 | 0.0003 | 0.0005 |
| nacionalidad_top_edad | 0.0007 | 0.0026 | 0.0070 | 0.0006 | 0.0014 |
| sin_estudios_edad | 0.0004 | 0.0015 | 0.0026 | 0.0003 | 0.0007 |
| tamano_hogar | 0.0003 | 0.0013 | 0.0037 | 0.0002 | 0.0007 |
| tipo_hogar | 0.0006 | 0.0024 | 0.0063 | 0.0004 | 0.0016 |
| tipo_residencia (implícito) | 0.0000 | 0.0001 | 0.0005 | 0.0000 | 0.0001 |
| urbanizacion | 0.0003 | 0.0007 | 0.0012 | 0.0001 | 0.0004 |

## TVD por cruce reservado (España; media de 5 semillas)

| objetivo | 500000 | 100000 | 1000000 | 50000 | 10000 |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | 0.0112 | 0.0122 | 0.0110 | 0.0141 | 0.0198 |
| actividad_sexo | 0.0058 | 0.0073 | 0.0056 | 0.0081 | 0.0105 |
| adultos_nacionalidad | 0.0018 | 0.0019 | 0.0018 | 0.0019 | 0.0033 |
| estudios_sexo_edad | 0.0074 | 0.0084 | 0.0071 | 0.0099 | 0.0169 |
| nacionalidad_top_sexo_edad | 0.0063 | 0.0076 | 0.0060 | 0.0089 | 0.0178 |
| provincia_si_calibra_ccaa | 0.0095 | 0.0104 | 0.0096 | 0.0137 | 0.0291 |
| tamano_municipio | 0.0111 | 0.0108 | 0.0111 | 0.0113 | 0.0114 |
| tipo_hogar_edad4_ref | 0.0307 | 0.0306 | 0.0306 | 0.0309 | 0.0339 |

## Fallos por tamaño

| N | semilla | v_marg | v_cruce | v_cruce_excepciones | v_cruce_estricto | comprobaciones_cruce |
| --- | --- | --- | --- | --- | --- | --- |
| 10000 | 1 | 0 | 8 | 0 | 16 | 511 |
| 10000 | 2 | 0 | 16 | 1 | 38 | 511 |
| 10000 | 3 | 0 | 11 | 0 | 30 | 511 |
| 10000 | 4 | 0 | 8 | 0 | 24 | 511 |
| 10000 | 5 | 0 | 9 | 0 | 29 | 511 |
| 50000 | 1 | 0 | 1 | 0 | 1 | 511 |
| 50000 | 2 | 0 | 1 | 0 | 3 | 511 |
| 50000 | 3 | 0 | 3 | 0 | 9 | 511 |
| 50000 | 4 | 0 | 2 | 1 | 8 | 511 |
| 50000 | 5 | 0 | 4 | 0 | 12 | 511 |
| 100000 | 1 | 0 | 2 | 1 | 7 | 511 |
| 100000 | 2 | 0 | 0 | 0 | 2 | 511 |
| 100000 | 3 | 0 | 0 | 1 | 3 | 511 |
| 100000 | 4 | 0 | 2 | 1 | 6 | 511 |
| 100000 | 5 | 0 | 1 | 1 | 5 | 511 |
| 500000 | 1 | 1 | 1 | 1 | 4 | 511 |
| 500000 | 2 | 1 | 2 | 1 | 4 | 511 |
| 500000 | 3 | 1 | 2 | 0 | 2 | 511 |
| 500000 | 4 | 1 | 1 | 1 | 3 | 511 |
| 500000 | 5 | 1 | 1 | 1 | 2 | 511 |
| 1000000 | 1 | 3 | 1 | 0 | 1 | 511 |
| 1000000 | 2 | 2 | 1 | 1 | 2 | 511 |
| 1000000 | 3 | 2 | 1 | 0 | 1 | 511 |
| 1000000 | 4 | 2 | 1 | 1 | 2 | 511 |
| 1000000 | 5 | 3 | 1 | 0 | 1 | 511 |

### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas

| nivel | territorio | objetivo | tvd | umbral | excepcion | N | semilla |
| --- | --- | --- | --- | --- | --- | --- | --- |
| espana | ES | tipo_hogar_edad4_ref | 0.0307 | 0.0300 | ❌ | 500000 | 1 |
| provincia | PROV:40 | tamano_municipio | 0.0806 | 0.0800 | ✅ | 500000 | 1 |
| espana | ES | tipo_hogar_edad4_ref | 0.0307 | 0.0300 | ❌ | 500000 | 2 |
| ccaa | CCAA:05 | tipo_hogar_edad4_ref | 0.0507 | 0.0500 | ❌ | 500000 | 2 |
| provincia | PROV:40 | tamano_municipio | 0.0826 | 0.0800 | ✅ | 500000 | 2 |
| espana | ES | tipo_hogar_edad4_ref | 0.0312 | 0.0300 | ❌ | 500000 | 3 |
| ccaa | CCAA:05 | tipo_hogar_edad4_ref | 0.0522 | 0.0500 | ❌ | 500000 | 3 |
| espana | ES | tipo_hogar_edad4_ref | 0.0303 | 0.0300 | ❌ | 500000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0937 | 0.0800 | ✅ | 500000 | 4 |
| espana | ES | tipo_hogar_edad4_ref | 0.0303 | 0.0300 | ❌ | 500000 | 5 |
| provincia | PROV:40 | tamano_municipio | 0.0840 | 0.0800 | ✅ | 500000 | 5 |
| espana | ES | tipo_hogar_edad4_ref | 0.0304 | 0.0300 | ❌ | 1000000 | 1 |
| espana | ES | tipo_hogar_edad4_ref | 0.0304 | 0.0300 | ❌ | 1000000 | 2 |
| provincia | PROV:40 | tamano_municipio | 0.0851 | 0.0800 | ✅ | 1000000 | 2 |
| espana | ES | tipo_hogar_edad4_ref | 0.0305 | 0.0300 | ❌ | 1000000 | 3 |
| espana | ES | tipo_hogar_edad4_ref | 0.0308 | 0.0300 | ❌ | 1000000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0845 | 0.0800 | ✅ | 1000000 | 4 |
| espana | ES | tipo_hogar_edad4_ref | 0.0307 | 0.0300 | ❌ | 1000000 | 5 |

## V-SEMILLAS

| n | proporciones | fuera | razon_media | razon_max |
| --- | --- | --- | --- | --- |
| 10000 | 437 | 2 | 0.3143 | 2.3165 |
| 50000 | 437 | 0 | 0.2286 | 0.6443 |
| 100000 | 437 | 0 | 0.2141 | 0.8945 |
| 500000 | 437 | 0 | 0.2271 | 0.5723 |
| 1000000 | 437 | 0 | 0.2259 | 0.6733 |

## V-PESOS (calibración por comunidades)

| bloque | desviacion_max | proporcion_en_rango | kish_ratio | no_positivos | factor_min | factor_max | proporcion_local | ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 0.0000 | 1.0000 | 0.7920 | 0 | 0.2000 | 4.9997 | 0.9988 | ✅ |
| CCAA:02 | 0.0000 | 1.0000 | 0.7888 | 0 | 0.2000 | 4.9987 | 0.9994 | ✅ |
| CCAA:03 | 0.0000 | 1.0000 | 0.7759 | 0 | 0.2000 | 4.9987 | 0.9977 | ✅ |
| CCAA:04 | 0.0005 | 1.0000 | 0.6067 | 0 | 0.2000 | 5.0000 | 0.9996 | ✅ |
| CCAA:05 | 0.0000 | 1.0000 | 0.7158 | 0 | 0.2000 | 4.9935 | 0.9997 | ✅ |
| CCAA:06 | 0.0000 | 1.0000 | 0.7785 | 0 | 0.2001 | 4.9863 | 0.9994 | ✅ |
| CCAA:07 | 0.0000 | 1.0000 | 0.8007 | 0 | 0.2000 | 4.9998 | 0.9973 | ✅ |
| CCAA:08 | 0.0000 | 1.0000 | 0.7644 | 0 | 0.2000 | 4.9996 | 0.9996 | ✅ |
| CCAA:09 | 0.0000 | 1.0000 | 0.7245 | 0 | 0.2000 | 5.0000 | 1.0000 | ✅ |
| CCAA:10 | 0.0000 | 1.0000 | 0.7238 | 0 | 0.2000 | 5.0000 | 0.9974 | ✅ |
| CCAA:11 | 0.0000 | 1.0000 | 0.8170 | 0 | 0.2000 | 4.9399 | 0.9985 | ✅ |
| CCAA:12 | 0.0000 | 1.0000 | 0.7877 | 0 | 0.2000 | 4.9999 | 0.9975 | ✅ |
| CCAA:13 | 0.0000 | 1.0000 | 0.7374 | 0 | 0.2000 | 5.0000 | 1.0000 | ✅ |
| CCAA:14 | 0.0000 | 1.0000 | 0.7498 | 0 | 0.2000 | 4.9997 | 0.9997 | ✅ |
| CCAA:15 | 0.0000 | 1.0000 | 0.7833 | 0 | 0.2000 | 4.9897 | 0.9998 | ✅ |
| CCAA:16 | 0.0000 | 1.0000 | 0.7979 | 0 | 0.2000 | 4.9938 | 0.9997 | ✅ |
| CCAA:17 | 0.0000 | 1.0000 | 0.7834 | 0 | 0.2001 | 4.8974 | 0.9989 | ✅ |
| CCAA:18 | 0.0000 | 1.0000 | 0.6705 | 0 | 0.2000 | 4.7567 | 0.9882 | ✅ |
| CCAA:19 | 0.0000 | 1.0000 | 0.6842 | 0 | 0.2000 | 4.8447 | 0.9817 | ✅ |

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
| CCAA:11 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 4 | 2.2126 | 1 | None |
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
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | 5 | 3.8028 | 3 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | 24 | 3.5464 | 8 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 12 | 3.7354 | 7 | None |
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
| actividad_edad | relacion_actividad × edad_actividad | 0.6145 | 0.6189 | 0.0044 | ✅ |
| actividad_sexo | relacion_actividad × sexo | 0.2209 | 0.2188 | 0.0021 | ✅ |
| adultos_nacionalidad | nacionalidad_esp_ext × es_adulto | 0.0028 | 0.0054 | 0.0026 | ✅ |
| estudios_sexo_edad | estudios_3 × sexo | 0.0391 | 0.0352 | 0.0039 | ✅ |
| estudios_sexo_edad | estudios_3 × edad_estudios | 0.6228 | 0.6228 | 0.0000 | ✅ |
| estudios_sexo_edad | sexo × edad_estudios | 0.0713 | 0.0714 | 0.0001 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × sexo | 0.0420 | 0.0456 | 0.0036 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × edad_nacionalidad | 0.1056 | 0.1054 | 0.0002 | ✅ |
| nacionalidad_top_sexo_edad | sexo × edad_nacionalidad | 0.0575 | 0.0576 | 0.0001 | ✅ |
| tipo_hogar_edad4_ref | tipo_hogar × edad_4 | 0.1810 | 0.1811 | 0.0002 | ✅ |

## Minorías, primera pasada (2026-01-01_ES_1000000_s1)

| grupo | unidad | esperado | observado | ratio | ok_representacion | donantes_distintos | top5 | ok_concentracion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mayores_85 | persona | 32795.7011 | 32810.0000 | 1.0004 | ✅ | 29318 | 0.0013 | ✅ |
| municipios_menos_2000 | persona | 54716.3187 | 56263.0000 | 1.0283 | ✅ | 25105 | 0.0018 | ✅ |
| parados | persona | 50997.4556 | 50776.0000 | 0.9957 | ✅ | 44162 | 0.0007 | ✅ |
| monoparentales | hogar | 46940.0934 | 46951.0000 | 1.0002 | ✅ | 46615 | 0.0005 | ✅ |
| mayores_solos | persona | 47334.1663 | 48894.0000 | 1.0330 | ✅ | 48676 | 0.0002 | ✅ |
| ceuta_melilla | persona | 3449.7639 | 3443.0000 | 0.9980 | ✅ | 1081 | 0.0177 | ✅ |
| nacionalidad_alemania | persona | 2750.3181 | 2733.0000 | 0.9937 | ✅ | 1951 | 0.0110 | ✅ |
| nacionalidad_argentina | persona | 3114.9267 | 3113.0000 | 0.9994 | ✅ | 2116 | 0.0119 | ✅ |
| nacionalidad_china | persona | 4968.2678 | 4998.0000 | 1.0060 | ✅ | 1609 | 0.0114 | ✅ |
| nacionalidad_colombia | persona | 14242.3564 | 14183.0000 | 0.9958 | ✅ | 7097 | 0.0059 | ✅ |
| nacionalidad_ecuador | persona | 2768.2021 | 2783.0000 | 1.0053 | ✅ | 1826 | 0.0137 | ✅ |
| nacionalidad_francia | persona | 2656.8364 | 2655.0000 | 0.9993 | ✅ | 1882 | 0.0117 | ✅ |
| nacionalidad_honduras | persona | 3667.5205 | 3675.0000 | 1.0020 | ✅ | 1752 | 0.0163 | ✅ |
| nacionalidad_italia | persona | 7187.4628 | 7166.0000 | 0.9970 | ✅ | 4605 | 0.0053 | ✅ |
| nacionalidad_marruecos | persona | 20301.9508 | 20213.0000 | 0.9956 | ✅ | 8736 | 0.0039 | ✅ |
| nacionalidad_paraguay | persona | 2555.0029 | 2537.0000 | 0.9930 | ✅ | 1384 | 0.0158 | ✅ |
| nacionalidad_peru | persona | 5439.0981 | 5425.0000 | 0.9974 | ✅ | 2565 | 0.0144 | ✅ |
| nacionalidad_reino_unido | persona | 5616.0940 | 5623.0000 | 1.0012 | ✅ | 3512 | 0.0060 | ✅ |
| nacionalidad_rumania | persona | 12832.1702 | 12824.0000 | 0.9994 | ✅ | 5600 | 0.0051 | ✅ |
| nacionalidad_ucrania | persona | 4259.6137 | 4256.0000 | 0.9992 | ✅ | 1663 | 0.0160 | ✅ |
| nacionalidad_venezuela | persona | 7938.0885 | 7912.0000 | 0.9967 | ✅ | 3899 | 0.0075 | ✅ |

## Reglas blandas (media de 5 semillas; nº de semillas dentro)

| regla | N | frecuencia_donantes | exceso_relativo | ok_estricto | ok |
| --- | --- | --- | --- | --- | --- |
| casado_menor_20 | 10000 | 0.000049 | -0.186007 | 3 | 5 |
| casado_menor_20 | 50000 | 0.000049 | 0.381687 | 1 | 4 |
| casado_menor_20 | 100000 | 0.000049 | 0.178378 | 4 | 5 |
| casado_menor_20 | 500000 | 0.000049 | 0.047917 | 3 | 5 |
| casado_menor_20 | 1000000 | 0.000049 | 0.104668 | 2 | 5 |
| estudiante_50_o_mas | 10000 | 0.000580 | -0.618878 | 5 | 5 |
| estudiante_50_o_mas | 50000 | 0.000580 | -0.122975 | 5 | 5 |
| estudiante_50_o_mas | 100000 | 0.000580 | -0.060942 | 5 | 5 |
| estudiante_50_o_mas | 500000 | 0.000580 | -0.035104 | 5 | 5 |
| estudiante_50_o_mas | 1000000 | 0.000580 | 0.021743 | 5 | 5 |
| hogar_8_o_mas | 10000 | 0.016565 | -0.302133 | 5 | 5 |
| hogar_8_o_mas | 50000 | 0.016565 | -0.127615 | 5 | 5 |
| hogar_8_o_mas | 100000 | 0.016565 | -0.058023 | 5 | 5 |
| hogar_8_o_mas | 500000 | 0.016565 | -0.008300 | 5 | 5 |
| hogar_8_o_mas | 1000000 | 0.016565 | -0.007037 | 5 | 5 |
| incapacidad_menor_25 | 10000 | 0.000058 | -0.654560 | 4 | 5 |
| incapacidad_menor_25 | 50000 | 0.000058 | -0.793571 | 5 | 5 |
| incapacidad_menor_25 | 100000 | 0.000058 | -0.552882 | 5 | 5 |
| incapacidad_menor_25 | 500000 | 0.000058 | -0.044275 | 5 | 5 |
| incapacidad_menor_25 | 1000000 | 0.000058 | -0.027176 | 5 | 5 |
| jubilado_menor_50 | 10000 | 0.000007 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 50000 | 0.000007 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 100000 | 0.000007 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 500000 | 0.000007 | -0.724456 | 5 | 5 |
| jubilado_menor_50 | 1000000 | 0.000007 | -0.586689 | 5 | 5 |
| ocupado_75_o_mas | 10000 | 0.001523 | -0.012165 | 3 | 5 |
| ocupado_75_o_mas | 50000 | 0.001523 | 0.032672 | 3 | 5 |
| ocupado_75_o_mas | 100000 | 0.001523 | -0.006896 | 4 | 5 |
| ocupado_75_o_mas | 500000 | 0.001523 | -0.022536 | 5 | 5 |
| ocupado_75_o_mas | 1000000 | 0.001523 | 0.002582 | 5 | 5 |
| superior_20_21 | 10000 | 0.003310 | 0.060854 | 3 | 5 |
| superior_20_21 | 50000 | 0.003310 | -0.021665 | 5 | 5 |
| superior_20_21 | 100000 | 0.003310 | 0.001170 | 5 | 5 |
| superior_20_21 | 500000 | 0.003310 | 0.001844 | 5 | 5 |
| superior_20_21 | 1000000 | 0.003310 | -0.002115 | 5 | 5 |
| viudo_menor_30 | 10000 | 0.000058 | -0.312683 | 3 | 5 |
| viudo_menor_30 | 50000 | 0.000058 | 0.027944 | 4 | 5 |
| viudo_menor_30 | 100000 | 0.000058 | 0.164885 | 3 | 5 |
| viudo_menor_30 | 500000 | 0.000058 | 0.082164 | 3 | 5 |
| viudo_menor_30 | 1000000 | 0.000058 | -0.058320 | 5 | 5 |

## G4.7 · Sobremuestreo (edad>=85:10000, 2026-01-01_ES_100000_s1_sm7d9288)

Miembros del grupo: 9903 (mínimo pedido 10000); α = 0.8697, β = 3.0490; suma de pesos 100200.

| objetivo | tvd | n_efectivo | umbral | ok |
| --- | --- | --- | --- | --- |
| actividad_tramo | 0.0096 | 90944.7322 | 0.0134 | ✅ |
| edad5_sexo | 0.0025 | 90944.7322 | 0.0134 | ✅ |
| edad5_sexo_colectivos | 0.0364 | 814.0148 | 0.1211 | ✅ |
| edad5_sexo_familiares | 0.0025 | 90145.9635 | 0.0135 | ✅ |
| estado_civil_edad | 0.0021 | 90944.7322 | 0.0097 | ✅ |
| estudios_edad | 0.0026 | 90944.7322 | 0.0121 | ✅ |
| nacimiento_nacionalidad | 0.0009 | 90944.7322 | 0.0053 | ✅ |
| nacionalidad | 0.0009 | 90944.7322 | 0.0054 | ✅ |
| nacionalidad_edad | 0.0020 | 90944.7322 | 0.0124 | ✅ |
| nacionalidad_top | 0.0013 | 90944.7322 | 0.0059 | ✅ |
| nacionalidad_top_edad | 0.0021 | 90944.7322 | 0.0117 | ✅ |
| sin_estudios_edad | 0.0012 | 90944.7322 | 0.0098 | ✅ |
| tamano_hogar | 0.0007 | 36543.8960 | 0.0097 | ✅ |
| tipo_hogar | 0.0016 | 36543.8960 | 0.0127 | ✅ |
| urbanizacion | 0.0003 | 90944.7322 | 0.0061 | ✅ |

## V-DONANTES (2026-01-01_ES_1000000_s1)

| territorio | personas | hogares_donantes | kish | proporcion_local | ok | confianza_reducida |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 176467 | 70065 | 53619.601 | 0.997 | ✅ | ❌ |
| CCAA:02 | 27862 | 11703 | 8816.280 | 0.998 | ✅ | ❌ |
| CCAA:03 | 20603 | 9309 | 6959.090 | 0.994 | ✅ | ❌ |
| CCAA:04 | 25398 | 9548 | 7099.789 | 0.999 | ✅ | ❌ |
| CCAA:05 | 45888 | 17622 | 12923.532 | 0.999 | ✅ | ❌ |
| CCAA:06 | 12039 | 5067 | 3804.434 | 0.999 | ✅ | ❌ |
| CCAA:07 | 48817 | 21827 | 16169.871 | 0.993 | ✅ | ❌ |
| CCAA:08 | 43469 | 17300 | 12889.973 | 0.999 | ✅ | ❌ |
| CCAA:09 | 165328 | 65482 | 49297.240 | 1.000 | ✅ | ❌ |
| CCAA:10 | 111451 | 45033 | 34058.369 | 0.991 | ✅ | ❌ |
| CCAA:11 | 21268 | 9095 | 6982.307 | 0.995 | ✅ | ❌ |
| CCAA:12 | 55026 | 23102 | 17328.599 | 0.992 | ✅ | ❌ |
| CCAA:13 | 144528 | 56061 | 42383.619 | 1.000 | ✅ | ❌ |
| CCAA:14 | 32397 | 11949 | 9044.783 | 0.999 | ✅ | ❌ |
| CCAA:15 | 13907 | 5525 | 4123.679 | 0.999 | ✅ | ❌ |
| CCAA:16 | 45418 | 19548 | 14806.164 | 0.999 | ✅ | ❌ |
| CCAA:17 | 6643 | 2791 | 2065.889 | 0.999 | ✅ | ❌ |
| CCAA:18 | 1691 | 537 | 387.621 | 0.995 | ✅ | ❌ |
| CCAA:19 | 1752 | 544 | 398.120 | 0.977 | ✅ | ❌ |
| ES | 999952 | 401675 | 300908.350 | 0.997 | ✅ | ❌ |

## V-RAREZA

| nivel | combinaciones | sin_donante | personas_afectadas | ok |
| --- | --- | --- | --- | --- |
| persona | 25524 | 0 | 0 | ✅ |
| persona_y_hogar | 159066 | 0 | 0 | ✅ |

## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)

### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)

| ccaa | sint_ocupado | ref_ocupado | sint_parado | ref_parado | paro_sint | paro_epa | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.4969 | 0.4935 | 0.0853 | 0.0841 | 0.1466 | 0.1456 | 0.0047 | ✅ |
| 02 | 0.5511 | 0.5414 | 0.0454 | 0.0482 | 0.0761 | 0.0817 | 0.0096 | ✅ |
| 03 | 0.4778 | 0.4763 | 0.0526 | 0.0478 | 0.0992 | 0.0912 | 0.0063 | ✅ |
| 04 | 0.5918 | 0.6297 | 0.0376 | 0.0410 | 0.0597 | 0.0611 | 0.0412 | ✅ |
| 05 | 0.5304 | 0.5206 | 0.0716 | 0.0683 | 0.1189 | 0.1160 | 0.0131 | ✅ |
| 06 | 0.5110 | 0.5149 | 0.0484 | 0.0408 | 0.0865 | 0.0734 | 0.0076 | ✅ |
| 07 | 0.5035 | 0.4991 | 0.0463 | 0.0456 | 0.0842 | 0.0837 | 0.0051 | ✅ |
| 08 | 0.5289 | 0.5227 | 0.0695 | 0.0700 | 0.1162 | 0.1181 | 0.0062 | ✅ |
| 09 | 0.5742 | 0.5717 | 0.0486 | 0.0490 | 0.0780 | 0.0790 | 0.0025 | ✅ |
| 10 | 0.5270 | 0.5245 | 0.0640 | 0.0640 | 0.1083 | 0.1088 | 0.0026 | ✅ |
| 11 | 0.4870 | 0.4761 | 0.0752 | 0.0725 | 0.1338 | 0.1322 | 0.0136 | ✅ |
| 12 | 0.4947 | 0.4881 | 0.0433 | 0.0421 | 0.0805 | 0.0794 | 0.0079 | ✅ |
| 13 | 0.5924 | 0.5908 | 0.0471 | 0.0485 | 0.0737 | 0.0758 | 0.0017 | ✅ |
| 14 | 0.5488 | 0.5530 | 0.0645 | 0.0672 | 0.1052 | 0.1083 | 0.0069 | ✅ |
| 15 | 0.5471 | 0.5368 | 0.0488 | 0.0471 | 0.0819 | 0.0807 | 0.0119 | ✅ |
| 16 | 0.5245 | 0.5170 | 0.0444 | 0.0396 | 0.0780 | 0.0711 | 0.0123 | ✅ |
| 17 | 0.5480 | 0.5373 | 0.0467 | 0.0516 | 0.0785 | 0.0877 | 0.0107 | ✅ |
| 18 | 0.4923 | 0.5361 | 0.1463 | 0.1548 | 0.2291 | 0.2241 | 0.0523 | ✅ |
| 19 | 0.4960 | 0.4116 | 0.1233 | 0.1077 | 0.1991 | 0.2074 | 0.0999 | ✅ |

### ECV 2025: personas por tamaño del hogar

| ccaa | sint_1 | sint_2 | sint_3 | sint_4 | sint_5+ | ref_1 | ref_2 | ref_3 | ref_4 | ref_5+ | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.1082 | 0.2258 | 0.2406 | 0.2659 | 0.1595 | 0.1071 | 0.2233 | 0.2409 | 0.2579 | 0.1708 | 0.0117 | ✅ |
| 02 | 0.1300 | 0.2442 | 0.2427 | 0.2510 | 0.1321 | 0.1283 | 0.2440 | 0.2449 | 0.2330 | 0.1499 | 0.0199 | ✅ |
| 03 | 0.1559 | 0.2898 | 0.2648 | 0.1877 | 0.1018 | 0.1546 | 0.2897 | 0.2655 | 0.1834 | 0.1068 | 0.0057 | ✅ |
| 04 | 0.0970 | 0.2060 | 0.2306 | 0.2378 | 0.2286 | 0.0970 | 0.2062 | 0.2313 | 0.2235 | 0.2420 | 0.0143 | ✅ |
| 05 | 0.1059 | 0.2093 | 0.2439 | 0.2206 | 0.2204 | 0.1053 | 0.2082 | 0.2429 | 0.1773 | 0.2663 | 0.0459 | ✅ |
| 06 | 0.1307 | 0.2512 | 0.2492 | 0.2311 | 0.1378 | 0.1295 | 0.2462 | 0.2512 | 0.2192 | 0.1539 | 0.0180 | ✅ |
| 07 | 0.1587 | 0.2621 | 0.2442 | 0.2188 | 0.1162 | 0.1573 | 0.2606 | 0.2455 | 0.2055 | 0.1311 | 0.0163 | ✅ |
| 08 | 0.1158 | 0.2220 | 0.2337 | 0.2562 | 0.1723 | 0.1150 | 0.2211 | 0.2357 | 0.2707 | 0.1574 | 0.0165 | ✅ |
| 09 | 0.1046 | 0.2359 | 0.2362 | 0.2397 | 0.1835 | 0.1040 | 0.2350 | 0.2371 | 0.2288 | 0.1951 | 0.0124 | ✅ |
| 10 | 0.1149 | 0.2358 | 0.2411 | 0.2437 | 0.1645 | 0.1147 | 0.2369 | 0.2428 | 0.2297 | 0.1760 | 0.0143 | ✅ |
| 11 | 0.1364 | 0.2511 | 0.2493 | 0.2557 | 0.1075 | 0.1335 | 0.2483 | 0.2488 | 0.2437 | 0.1257 | 0.0182 | ✅ |
| 12 | 0.1306 | 0.2445 | 0.2526 | 0.2221 | 0.1501 | 0.1296 | 0.2435 | 0.2530 | 0.2226 | 0.1513 | 0.0020 | ✅ |
| 13 | 0.1006 | 0.2221 | 0.2339 | 0.2524 | 0.1910 | 0.0985 | 0.2196 | 0.2330 | 0.2468 | 0.2020 | 0.0111 | ✅ |
| 14 | 0.0902 | 0.1961 | 0.2228 | 0.2723 | 0.2187 | 0.0888 | 0.1939 | 0.2219 | 0.2586 | 0.2368 | 0.0182 | ✅ |
| 15 | 0.1167 | 0.2219 | 0.2266 | 0.2499 | 0.1848 | 0.1152 | 0.2216 | 0.2264 | 0.2519 | 0.1848 | 0.0020 | ✅ |
| 16 | 0.1363 | 0.2667 | 0.2338 | 0.2374 | 0.1258 | 0.1337 | 0.2655 | 0.2360 | 0.2353 | 0.1295 | 0.0059 | ✅ |
| 17 | 0.1374 | 0.2505 | 0.2415 | 0.2462 | 0.1245 | 0.1364 | 0.2489 | 0.2398 | 0.2354 | 0.1396 | 0.0151 | ✅ |
| 18 | 0.0681 | 0.1458 | 0.1934 | 0.2361 | 0.3566 | 0.0587 | 0.1663 | 0.2109 | 0.2097 | 0.3543 | 0.0381 | ✅ |
| 19 | 0.0637 | 0.1424 | 0.1858 | 0.2315 | 0.3767 | 0.0733 | 0.1110 | 0.1503 | 0.2119 | 0.4536 | 0.0865 | ✅ |

### Padrón 01/01/2022: proporción de extranjeros por provincia

| provincia | sint_extranjera | ref_extranjera | tvd | dentro |
| --- | --- | --- | --- | --- |
| 01 | 0.1283 | 0.0987 | 0.0296 | ✅ |
| 02 | 0.0962 | 0.0714 | 0.0248 | ✅ |
| 03 | 0.2591 | 0.2044 | 0.0546 | ✅ |
| 04 | 0.2472 | 0.2189 | 0.0283 | ✅ |
| 05 | 0.1025 | 0.0663 | 0.0361 | ✅ |
| 06 | 0.0460 | 0.0319 | 0.0141 | ✅ |
| 07 | 0.2163 | 0.1887 | 0.0276 | ✅ |
| 08 | 0.1808 | 0.1548 | 0.0260 | ✅ |
| 09 | 0.1110 | 0.0835 | 0.0275 | ✅ |
| 10 | 0.0514 | 0.0357 | 0.0157 | ✅ |
| 11 | 0.0554 | 0.0419 | 0.0135 | ✅ |
| 12 | 0.2014 | 0.1540 | 0.0474 | ✅ |
| 13 | 0.0766 | 0.0644 | 0.0122 | ✅ |
| 14 | 0.0358 | 0.0279 | 0.0079 | ✅ |
| 15 | 0.0671 | 0.0416 | 0.0255 | ✅ |
| 16 | 0.1473 | 0.1164 | 0.0309 | ✅ |
| 17 | 0.2253 | 0.2046 | 0.0207 | ✅ |
| 18 | 0.1024 | 0.0750 | 0.0274 | ✅ |
| 19 | 0.1857 | 0.1388 | 0.0468 | ✅ |
| 20 | 0.0979 | 0.0847 | 0.0132 | ✅ |
| 21 | 0.1149 | 0.0968 | 0.0181 | ✅ |
| 22 | 0.1683 | 0.1321 | 0.0362 | ✅ |
| 23 | 0.0382 | 0.0283 | 0.0098 | ✅ |
| 24 | 0.0640 | 0.0456 | 0.0184 | ✅ |
| 25 | 0.2085 | 0.1887 | 0.0198 | ✅ |
| 26 | 0.1528 | 0.1305 | 0.0223 | ✅ |
| 27 | 0.0742 | 0.0520 | 0.0221 | ✅ |
| 28 | 0.1669 | 0.1407 | 0.0262 | ✅ |
| 29 | 0.1939 | 0.1673 | 0.0266 | ✅ |
| 30 | 0.1631 | 0.1480 | 0.0151 | ✅ |
| 31 | 0.1355 | 0.1106 | 0.0249 | ✅ |
| 32 | 0.0793 | 0.0543 | 0.0249 | ✅ |
| 33 | 0.0754 | 0.0454 | 0.0300 | ✅ |
| 34 | 0.0663 | 0.0473 | 0.0190 | ✅ |
| 35 | 0.1459 | 0.1265 | 0.0194 | ✅ |
| 36 | 0.0678 | 0.0412 | 0.0266 | ✅ |
| 37 | 0.0778 | 0.0487 | 0.0291 | ✅ |
| 38 | 0.1575 | 0.1389 | 0.0186 | ✅ |
| 39 | 0.0845 | 0.0636 | 0.0209 | ✅ |
| 40 | 0.1516 | 0.1185 | 0.0332 | ✅ |
| 41 | 0.0566 | 0.0411 | 0.0155 | ✅ |
| 42 | 0.1450 | 0.0996 | 0.0455 | ✅ |
| 43 | 0.1957 | 0.1681 | 0.0277 | ✅ |
| 44 | 0.1343 | 0.1161 | 0.0182 | ✅ |
| 45 | 0.1445 | 0.1042 | 0.0402 | ✅ |
| 46 | 0.1663 | 0.1170 | 0.0493 | ✅ |
| 47 | 0.0889 | 0.0568 | 0.0321 | ✅ |
| 48 | 0.1000 | 0.0785 | 0.0214 | ✅ |
| 49 | 0.0704 | 0.0379 | 0.0324 | ✅ |
| 50 | 0.1557 | 0.1235 | 0.0322 | ✅ |
| 51 | 0.0680 | 0.0591 | 0.0089 | ✅ |
| 52 | 0.1318 | 0.1371 | 0.0052 | ✅ |

## V-REPRO

2026-01-01_ES_10000_s1 generado de nuevo en otro directorio: mismos hashes.

- `persons.parquet`: `36057cb057a76efc30e3743f2b9da87927a9728b75786f171a0db4e2ebbd8ac6`
- `households.parquet`: `15961296453b599a31bd70564113c763a02ed2398b2a838d80073a74f9780170`
- `lineage.parquet`: `4f2f4e250b36fb8661c6a1b7db3f90faef30aadba48a3baaca331a5364cee635`
