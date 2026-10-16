# Fase 04 · Tablas de validación

Generado por `python -m sinpop.validate.fase4` (git:dc48a0b-dirty, 2026-10-16). Resumen en `fase_04_validacion.json`; detalle por población en `fase_04/`.

## Curva de error frente a tamaño (España; media de 5 semillas)

| n | tvd_media_calibradas | sd_calibradas | tvd_media_reservadas | sd_reservadas |
| --- | --- | --- | --- | --- |
| 10000 | 0.0228 | 0.0025 | 0.0196 | 0.0004 |
| 50000 | 0.0081 | 0.0005 | 0.0140 | 0.0008 |
| 100000 | 0.0040 | 0.0005 | 0.0131 | 0.0002 |
| 500000 | 0.0015 | 0.0001 | 0.0125 | 0.0001 |
| 1000000 | 0.0010 | 0.0001 | 0.0124 | 0.0001 |

## TVD por marginal calibrada (España; media de 5 semillas)

| objetivo | 100000 | 10000 | 50000 | 500000 | 1000000 |
| --- | --- | --- | --- | --- | --- |
| actividad_sexo | 0.0020 | 0.0048 | 0.0025 | 0.0010 | 0.0005 |
| edad5_sexo | 0.0018 | 0.0054 | 0.0024 | 0.0010 | 0.0006 |
| edad5_sexo_colectivos | 0.0343 | 0.2307 | 0.0779 | 0.0108 | 0.0072 |
| edad5_sexo_familiares | 0.0018 | 0.0055 | 0.0024 | 0.0010 | 0.0006 |
| estudios_edad | 0.0019 | 0.0054 | 0.0026 | 0.0010 | 0.0007 |
| nacionalidad | 0.0004 | 0.0017 | 0.0006 | 0.0003 | 0.0002 |
| nacionalidad_edad | 0.0017 | 0.0056 | 0.0025 | 0.0010 | 0.0006 |
| nacionalidad_top | 0.0008 | 0.0025 | 0.0009 | 0.0004 | 0.0002 |
| tamano_hogar | 0.0007 | 0.0034 | 0.0015 | 0.0003 | 0.0002 |
| tipo_hogar | 0.0017 | 0.0062 | 0.0026 | 0.0007 | 0.0004 |
| tipo_residencia (implícito) | 0.0001 | 0.0003 | 0.0002 | 0.0000 | 0.0000 |
| urbanizacion | 0.0005 | 0.0016 | 0.0009 | 0.0002 | 0.0001 |

## TVD por cruce reservado (España; media de 5 semillas)

| objetivo | 50000 | 100000 | 10000 | 1000000 | 500000 |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | 0.0160 | 0.0143 | 0.0215 | 0.0136 | 0.0139 |
| adultos_nacionalidad | 0.0014 | 0.0013 | 0.0033 | 0.0014 | 0.0015 |
| estado_civil_edad | 0.0262 | 0.0253 | 0.0257 | 0.0258 | 0.0254 |
| estudios_sexo_edad | 0.0098 | 0.0081 | 0.0151 | 0.0066 | 0.0070 |
| nacionalidad_top_sexo_edad | 0.0107 | 0.0088 | 0.0215 | 0.0065 | 0.0065 |
| provincia_si_calibra_ccaa | 0.0092 | 0.0073 | 0.0236 | 0.0063 | 0.0065 |
| tamano_municipio | 0.0094 | 0.0094 | 0.0097 | 0.0094 | 0.0092 |
| tipo_hogar_edad4_ref | 0.0294 | 0.0305 | 0.0367 | 0.0297 | 0.0300 |

## Fallos por tamaño

| N | semilla | v_marg | v_cruce | v_cruce_excepciones | v_cruce_estricto | comprobaciones_cruce |
| --- | --- | --- | --- | --- | --- | --- |
| 10000 | 1 | 0 | 11 | 1 | 27 | 511 |
| 10000 | 2 | 0 | 5 | 0 | 21 | 511 |
| 10000 | 3 | 0 | 3 | 0 | 19 | 511 |
| 10000 | 4 | 0 | 12 | 0 | 26 | 511 |
| 10000 | 5 | 0 | 7 | 0 | 16 | 511 |
| 50000 | 1 | 0 | 2 | 0 | 6 | 511 |
| 50000 | 2 | 0 | 3 | 1 | 7 | 511 |
| 50000 | 3 | 0 | 3 | 0 | 8 | 511 |
| 50000 | 4 | 0 | 5 | 0 | 11 | 511 |
| 50000 | 5 | 0 | 2 | 0 | 9 | 511 |
| 100000 | 1 | 0 | 3 | 1 | 6 | 511 |
| 100000 | 2 | 0 | 1 | 1 | 3 | 511 |
| 100000 | 3 | 0 | 1 | 0 | 3 | 511 |
| 100000 | 4 | 0 | 2 | 1 | 4 | 511 |
| 100000 | 5 | 0 | 2 | 1 | 7 | 511 |
| 500000 | 1 | 0 | 1 | 0 | 1 | 511 |
| 500000 | 2 | 0 | 1 | 1 | 2 | 511 |
| 500000 | 3 | 0 | 1 | 1 | 2 | 511 |
| 500000 | 4 | 0 | 0 | 1 | 1 | 511 |
| 500000 | 5 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 1 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 2 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 3 | 0 | 1 | 1 | 2 | 511 |
| 1000000 | 4 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 5 | 0 | 0 | 1 | 1 | 511 |

### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas

| nivel | territorio | objetivo | tvd | umbral | excepcion | N | semilla |
| --- | --- | --- | --- | --- | --- | --- | --- |
| espana | ES | tipo_hogar_edad4_ref | 0.0303 | 0.0300 | ❌ | 500000 | 1 |
| espana | ES | tipo_hogar_edad4_ref | 0.0301 | 0.0300 | ❌ | 500000 | 2 |
| provincia | PROV:40 | tamano_municipio | 0.0908 | 0.0800 | ✅ | 500000 | 2 |
| espana | ES | tipo_hogar_edad4_ref | 0.0304 | 0.0300 | ❌ | 500000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0868 | 0.0800 | ✅ | 500000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0842 | 0.0800 | ✅ | 500000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0850 | 0.0800 | ✅ | 500000 | 5 |
| provincia | PROV:40 | tamano_municipio | 0.0820 | 0.0800 | ✅ | 1000000 | 1 |
| provincia | PROV:40 | tamano_municipio | 0.0835 | 0.0800 | ✅ | 1000000 | 2 |
| espana | ES | tipo_hogar_edad4_ref | 0.0302 | 0.0300 | ❌ | 1000000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0820 | 0.0800 | ✅ | 1000000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0861 | 0.0800 | ✅ | 1000000 | 5 |

## V-SEMILLAS

| n | proporciones | fuera | razon_media | razon_max |
| --- | --- | --- | --- | --- |
| 10000 | 244 | 0 | 0.2931 | 1.0872 |
| 50000 | 244 | 0 | 0.2353 | 0.5670 |
| 100000 | 244 | 0 | 0.2325 | 0.6176 |
| 500000 | 244 | 0 | 0.2842 | 0.6855 |
| 1000000 | 244 | 0 | 0.2473 | 0.5381 |

## V-PESOS (calibración por comunidades)

| bloque | desviacion_max | proporcion_en_rango | kish_ratio | no_positivos | factor_min | factor_max | proporcion_local | ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 0.0000 | 1.0000 | 0.9213 | 0 | 0.2038 | 4.9957 | 0.9994 | ✅ |
| CCAA:02 | 0.0000 | 1.0000 | 0.8987 | 0 | 0.2016 | 4.9710 | 1.0000 | ✅ |
| CCAA:03 | 0.0000 | 1.0000 | 0.8965 | 0 | 0.2081 | 4.9529 | 0.9988 | ✅ |
| CCAA:04 | 0.0000 | 1.0000 | 0.8552 | 0 | 0.2003 | 4.9927 | 1.0000 | ✅ |
| CCAA:05 | 0.0000 | 1.0000 | 0.8849 | 0 | 0.2149 | 4.9979 | 1.0000 | ✅ |
| CCAA:06 | 0.0000 | 1.0000 | 0.9086 | 0 | 0.2462 | 4.8195 | 0.9999 | ✅ |
| CCAA:07 | 0.0000 | 1.0000 | 0.8974 | 0 | 0.2014 | 4.9936 | 0.9991 | ✅ |
| CCAA:08 | 0.0000 | 1.0000 | 0.9007 | 0 | 0.2119 | 4.9655 | 1.0000 | ✅ |
| CCAA:09 | 0.0000 | 1.0000 | 0.9134 | 0 | 0.2022 | 4.9924 | 1.0000 | ✅ |
| CCAA:10 | 0.0000 | 1.0000 | 0.8814 | 0 | 0.2084 | 4.9989 | 1.0000 | ✅ |
| CCAA:11 | 0.0000 | 1.0000 | 0.9233 | 0 | 0.2179 | 4.8834 | 0.9996 | ✅ |
| CCAA:12 | 0.0000 | 1.0000 | 0.9015 | 0 | 0.2088 | 4.9949 | 0.9990 | ✅ |
| CCAA:13 | 0.0000 | 1.0000 | 0.9097 | 0 | 0.2061 | 4.9692 | 1.0000 | ✅ |
| CCAA:14 | 0.0000 | 1.0000 | 0.9132 | 0 | 0.2071 | 4.7590 | 1.0000 | ✅ |
| CCAA:15 | 0.0000 | 1.0000 | 0.9122 | 0 | 0.2045 | 4.8936 | 1.0000 | ✅ |
| CCAA:16 | 0.0000 | 1.0000 | 0.9078 | 0 | 0.2167 | 4.9681 | 0.9999 | ✅ |
| CCAA:17 | 0.0000 | 1.0000 | 0.9011 | 0 | 0.2005 | 4.3861 | 0.9994 | ✅ |
| CCAA:18 | 0.0000 | 1.0000 | 0.8706 | 0 | 0.2003 | 3.1970 | 0.9931 | ✅ |
| CCAA:19 | 0.0000 | 1.0000 | 0.8355 | 0 | 0.2057 | 2.6378 | 0.9875 | ✅ |

## Ampliación de donantes

| bloque | objetivo | clave | locales | razon_inicial | anadidas |
| --- | --- | --- | --- | --- | --- |
| CCAA:01 | nacionalidad_top | nacionalidad_top=peru | 322 | 3.9510 | 186 |
| CCAA:03 | nacionalidad_top | nacionalidad_top=peru | 50 | 3.5617 | 19 |
| CCAA:03 | nacionalidad_top | nacionalidad_top=ucrania | 42 | 5.4382 | 33 |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 3 | 1.8881 | 2 |
| CCAA:07 | nacionalidad_top | nacionalidad_top=peru | 187 | 3.8136 | 96 |
| CCAA:11 | nacionalidad_top | nacionalidad_top=peru | 36 | 3.7553 | 17 |
| CCAA:12 | nacionalidad_top | nacionalidad_top=peru | 207 | 3.7108 | 93 |
| CCAA:12 | nacionalidad_top | nacionalidad_top=ucrania | 40 | 3.5008 | 18 |
| CCAA:16 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 8 | 4.4910 | 7 |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 8.1332 | 4 |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.9987 | 3 |
| CCAA:17 | nacionalidad_top | nacionalidad_top=paraguay | 4 | 4.3333 | 1 |
| CCAA:18 | estudios_edad | estudios_3=superior;edad_estudios=90+ | 3 | 2.0488 | 2 |
| CCAA:18 | nacionalidad | nacionalidad_grupo=otros | 0 | None | 5 |
| CCAA:18 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.5142 | 1 |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 1.9579 | 4 |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.3251 | 3 |
| CCAA:18 | nacionalidad_top | nacionalidad_top=china | 1 | 2.3948 | 4 |
| CCAA:19 | estudios_edad | estudios_3=secundaria_2a_etapa;edad_estudios=90+ | 2 | 1.3648 | 3 |
| CCAA:19 | nacionalidad | nacionalidad_grupo=america_latina | 18 | 4.7103 | 15 |
| CCAA:19 | nacionalidad | nacionalidad_grupo=asia | 2 | 1.6472 | 3 |
| CCAA:19 | nacionalidad | nacionalidad_grupo=otros | 2 | 3.0749 | 3 |
| CCAA:19 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.6564 | 1 |
| CCAA:19 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.8079 | 3 |
| CCAA:19 | nacionalidad_top | nacionalidad_top=colombia | 1 | 17.6844 | 4 |
| CCAA:19 | nacionalidad_top | nacionalidad_top=venezuela | 5 | 4.2542 | 4 |

## Nacionalidades fusionadas con «otras extranjeras»

| bloque | objetivo | clave | fusionada_en |
| --- | --- | --- | --- |
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

## V de Cramér (2026-01-01_ES_1000000_s1)

| objetivo | par | v_oficial | v_sintetica | dif | ok |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | relacion_actividad × edad_actividad | 0.6110 | 0.6115 | 0.0005 | ✅ |
| adultos_nacionalidad | nacionalidad_esp_ext × es_adulto | 0.0028 | 0.0051 | 0.0024 | ✅ |
| estado_civil_edad | estado_civil × edad_estado_civil | 0.6242 | 0.6324 | 0.0082 | ✅ |
| estudios_sexo_edad | estudios_3 × sexo | 0.0391 | 0.0355 | 0.0036 | ✅ |
| estudios_sexo_edad | estudios_3 × edad_estudios | 0.6228 | 0.6228 | 0.0001 | ✅ |
| estudios_sexo_edad | sexo × edad_estudios | 0.0713 | 0.0718 | 0.0004 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × sexo | 0.0420 | 0.0447 | 0.0027 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × edad_nacionalidad | 0.1056 | 0.1068 | 0.0011 | ✅ |
| nacionalidad_top_sexo_edad | sexo × edad_nacionalidad | 0.0575 | 0.0577 | 0.0002 | ✅ |
| tipo_hogar_edad4_ref | tipo_hogar × edad_4 | 0.1810 | 0.1865 | 0.0055 | ✅ |

## Minorías, primera pasada (2026-01-01_ES_1000000_s1)

| grupo | unidad | esperado | observado | ratio | ok_representacion | donantes_distintos | top5 | ok_concentracion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mayores_85 | persona | 32795.9963 | 32825.0000 | 1.0009 | ✅ | 29425 | 0.0012 | ✅ |
| municipios_menos_2000 | persona | 54716.8112 | 55735.0000 | 1.0186 | ✅ | 25133 | 0.0017 | ✅ |
| parados | persona | 54474.2937 | 54596.0000 | 1.0022 | ✅ | 48404 | 0.0007 | ✅ |
| monoparentales | hogar | 46942.6852 | 46948.0000 | 1.0001 | ✅ | 46754 | 0.0005 | ✅ |
| mayores_solos | persona | 47334.5923 | 49363.0000 | 1.0429 | ✅ | 49224 | 0.0002 | ✅ |
| ceuta_melilla | persona | 3449.7949 | 3445.0000 | 0.9986 | ✅ | 1095 | 0.0232 | ✅ |
| nacionalidad_alemania | persona | 2750.3429 | 2770.0000 | 1.0071 | ✅ | 2008 | 0.0105 | ✅ |
| nacionalidad_argentina | persona | 3114.9547 | 3110.0000 | 0.9984 | ✅ | 2081 | 0.0122 | ✅ |
| nacionalidad_china | persona | 4968.3126 | 4972.0000 | 1.0007 | ✅ | 1602 | 0.0135 | ✅ |
| nacionalidad_colombia | persona | 14242.4845 | 14145.0000 | 0.9932 | ✅ | 6811 | 0.0044 | ✅ |
| nacionalidad_ecuador | persona | 2768.2271 | 2782.0000 | 1.0050 | ✅ | 1824 | 0.0144 | ✅ |
| nacionalidad_francia | persona | 2656.8604 | 2681.0000 | 1.0091 | ✅ | 1931 | 0.0123 | ✅ |
| nacionalidad_honduras | persona | 3667.5535 | 3659.0000 | 0.9977 | ✅ | 1720 | 0.0131 | ✅ |
| nacionalidad_italia | persona | 7187.5275 | 7201.0000 | 1.0019 | ✅ | 4614 | 0.0054 | ✅ |
| nacionalidad_marruecos | persona | 20302.1335 | 20273.0000 | 0.9986 | ✅ | 8047 | 0.0042 | ✅ |
| nacionalidad_paraguay | persona | 2555.0259 | 2541.0000 | 0.9945 | ✅ | 1331 | 0.0181 | ✅ |
| nacionalidad_peru | persona | 5439.1470 | 5410.0000 | 0.9946 | ✅ | 2572 | 0.0146 | ✅ |
| nacionalidad_reino_unido | persona | 5616.1446 | 5616.0000 | 1.0000 | ✅ | 3622 | 0.0061 | ✅ |
| nacionalidad_rumania | persona | 12832.2857 | 12878.0000 | 1.0036 | ✅ | 5738 | 0.0043 | ✅ |
| nacionalidad_ucrania | persona | 4259.6521 | 4263.0000 | 1.0008 | ✅ | 1774 | 0.0110 | ✅ |
| nacionalidad_venezuela | persona | 7938.1600 | 7897.0000 | 0.9948 | ✅ | 3815 | 0.0068 | ✅ |

## Reglas blandas (media de 5 semillas; nº de semillas dentro)

| regla | N | frecuencia_donantes | exceso_relativo | ok_estricto | ok |
| --- | --- | --- | --- | --- | --- |
| casado_menor_20 | 10000 | 0.000051 | 0.170408 | 2 | 5 |
| casado_menor_20 | 50000 | 0.000051 | -0.144164 | 3 | 5 |
| casado_menor_20 | 100000 | 0.000051 | 0.089143 | 2 | 5 |
| casado_menor_20 | 500000 | 0.000051 | -0.004533 | 2 | 5 |
| casado_menor_20 | 1000000 | 0.000051 | 0.069410 | 3 | 5 |
| estudiante_50_o_mas | 10000 | 0.000453 | -0.115078 | 3 | 5 |
| estudiante_50_o_mas | 50000 | 0.000453 | 0.024181 | 3 | 5 |
| estudiante_50_o_mas | 100000 | 0.000453 | -0.002608 | 4 | 5 |
| estudiante_50_o_mas | 500000 | 0.000453 | 0.055285 | 3 | 5 |
| estudiante_50_o_mas | 1000000 | 0.000453 | -0.035546 | 5 | 5 |
| hogar_8_o_mas | 10000 | 0.017743 | -0.260544 | 5 | 5 |
| hogar_8_o_mas | 50000 | 0.017743 | -0.095560 | 5 | 5 |
| hogar_8_o_mas | 100000 | 0.017743 | -0.031473 | 5 | 5 |
| hogar_8_o_mas | 500000 | 0.017743 | 0.006168 | 5 | 5 |
| hogar_8_o_mas | 1000000 | 0.017743 | -0.022003 | 5 | 5 |
| incapacidad_menor_25 | 10000 | 0.000179 | -0.438031 | 3 | 5 |
| incapacidad_menor_25 | 50000 | 0.000179 | -0.014190 | 3 | 5 |
| incapacidad_menor_25 | 100000 | 0.000179 | 0.019283 | 3 | 5 |
| incapacidad_menor_25 | 500000 | 0.000179 | 0.050282 | 2 | 5 |
| incapacidad_menor_25 | 1000000 | 0.000179 | -0.079548 | 5 | 5 |
| jubilado_menor_50 | 10000 | 0.000012 | 2.303578 | 4 | 4 |
| jubilado_menor_50 | 50000 | 0.000012 | 0.320196 | 2 | 5 |
| jubilado_menor_50 | 100000 | 0.000012 | 0.320045 | 2 | 5 |
| jubilado_menor_50 | 500000 | 0.000012 | -0.043212 | 4 | 5 |
| jubilado_menor_50 | 1000000 | 0.000012 | 0.022866 | 3 | 5 |
| ocupado_75_o_mas | 10000 | 0.001613 | -0.179416 | 5 | 5 |
| ocupado_75_o_mas | 50000 | 0.001613 | -0.010337 | 4 | 5 |
| ocupado_75_o_mas | 100000 | 0.001613 | -0.009270 | 4 | 5 |
| ocupado_75_o_mas | 500000 | 0.001613 | -0.017327 | 5 | 5 |
| ocupado_75_o_mas | 1000000 | 0.001613 | 0.009510 | 5 | 5 |
| superior_20_21 | 10000 | 0.003369 | -0.065155 | 4 | 5 |
| superior_20_21 | 50000 | 0.003369 | -0.008062 | 4 | 5 |
| superior_20_21 | 100000 | 0.003369 | 0.003035 | 5 | 5 |
| superior_20_21 | 500000 | 0.003369 | -0.000531 | 5 | 5 |
| superior_20_21 | 1000000 | 0.003369 | -0.001004 | 5 | 5 |
| viudo_menor_30 | 10000 | 0.000037 | -1.000000 | 5 | 5 |
| viudo_menor_30 | 50000 | 0.000037 | -0.252096 | 5 | 5 |
| viudo_menor_30 | 100000 | 0.000037 | 0.014818 | 4 | 5 |
| viudo_menor_30 | 500000 | 0.000037 | -0.049649 | 4 | 5 |
| viudo_menor_30 | 1000000 | 0.000037 | 0.003809 | 4 | 5 |

## G4.7 · Sobremuestreo (edad>=85:10000, 2026-01-01_ES_100000_s1_sm7d9288)

Miembros del grupo: 9898 (mínimo pedido 10000); α = 0.8712, β = 3.0490; suma de pesos 100213.

| objetivo | tvd | n_efectivo | umbral | ok |
| --- | --- | --- | --- | --- |
| actividad_sexo | 0.0023 | 91060.5536 | 0.0090 | ✅ |
| edad5_sexo | 0.0026 | 91060.5536 | 0.0136 | ✅ |
| edad5_sexo_colectivos | 0.0437 | 814.0699 | 0.1211 | ✅ |
| edad5_sexo_familiares | 0.0025 | 90262.8993 | 0.0131 | ✅ |
| estudios_edad | 0.0027 | 91060.5536 | 0.0122 | ✅ |
| nacionalidad | 0.0004 | 91060.5536 | 0.0054 | ✅ |
| nacionalidad_edad | 0.0025 | 91060.5536 | 0.0126 | ✅ |
| nacionalidad_top | 0.0006 | 91060.5536 | 0.0058 | ✅ |
| tamano_hogar | 0.0016 | 36603.2390 | 0.0093 | ✅ |
| tipo_hogar | 0.0022 | 36603.2390 | 0.0123 | ✅ |
| urbanizacion | 0.0006 | 91060.5536 | 0.0059 | ✅ |

## V-DONANTES (2026-01-01_ES_1000000_s1)

| territorio | personas | hogares_donantes | kish | proporcion_local | ok | confianza_reducida |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 176471 | 70228 | 53868.572 | 0.998 | ✅ | ❌ |
| CCAA:02 | 27870 | 11716 | 8802.948 | 1.000 | ✅ | ❌ |
| CCAA:03 | 20608 | 9358 | 7134.044 | 0.997 | ✅ | ❌ |
| CCAA:04 | 25398 | 9564 | 7103.698 | 1.000 | ✅ | ❌ |
| CCAA:05 | 45875 | 17685 | 13000.869 | 1.000 | ✅ | ❌ |
| CCAA:06 | 12028 | 5064 | 3805.376 | 1.000 | ✅ | ❌ |
| CCAA:07 | 48792 | 21850 | 16291.156 | 0.997 | ✅ | ❌ |
| CCAA:08 | 43464 | 17368 | 13123.258 | 1.000 | ✅ | ❌ |
| CCAA:09 | 165348 | 65601 | 49321.443 | 1.000 | ✅ | ❌ |
| CCAA:10 | 111468 | 45099 | 34130.618 | 1.000 | ✅ | ❌ |
| CCAA:11 | 21289 | 9100 | 6993.404 | 0.999 | ✅ | ❌ |
| CCAA:12 | 54983 | 23185 | 17555.823 | 0.997 | ✅ | ❌ |
| CCAA:13 | 144530 | 56144 | 42334.970 | 1.000 | ✅ | ❌ |
| CCAA:14 | 32392 | 11976 | 9104.681 | 1.000 | ✅ | ❌ |
| CCAA:15 | 13921 | 5542 | 4123.720 | 1.000 | ✅ | ❌ |
| CCAA:16 | 45429 | 19612 | 14881.163 | 1.000 | ✅ | ❌ |
| CCAA:17 | 6650 | 2822 | 2103.429 | 0.999 | ✅ | ❌ |
| CCAA:18 | 1694 | 548 | 378.980 | 0.998 | ✅ | ❌ |
| CCAA:19 | 1751 | 547 | 382.724 | 0.981 | ✅ | ❌ |
| ES | 999961 | 402888 | 303169.184 | 0.999 | ✅ | ❌ |

## V-RAREZA

| nivel | combinaciones | sin_donante | personas_afectadas | ok |
| --- | --- | --- | --- | --- |
| persona | 25629 | 0 | 0 | ✅ |
| persona_y_hogar | 164777 | 0 | 0 | ✅ |

## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)

### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)

| ccaa | sint_ocupado | ref_ocupado | sint_parado | ref_parado | paro_sint | paro_epa | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.4503 | 0.4935 | 0.0936 | 0.0841 | 0.1720 | 0.1456 | 0.0431 | ✅ |
| 02 | 0.5145 | 0.5414 | 0.0444 | 0.0482 | 0.0794 | 0.0817 | 0.0308 | ✅ |
| 03 | 0.4295 | 0.4763 | 0.0611 | 0.0478 | 0.1245 | 0.0912 | 0.0469 | ✅ |
| 04 | 0.4681 | 0.6297 | 0.0311 | 0.0410 | 0.0623 | 0.0611 | 0.1715 | ❌ |
| 05 | 0.4826 | 0.5206 | 0.0854 | 0.0683 | 0.1503 | 0.1160 | 0.0380 | ✅ |
| 06 | 0.4643 | 0.5149 | 0.0606 | 0.0408 | 0.1155 | 0.0734 | 0.0507 | ✅ |
| 07 | 0.4697 | 0.4991 | 0.0513 | 0.0456 | 0.0985 | 0.0837 | 0.0294 | ✅ |
| 08 | 0.4920 | 0.5227 | 0.0733 | 0.0700 | 0.1297 | 0.1181 | 0.0307 | ✅ |
| 09 | 0.5106 | 0.5717 | 0.0487 | 0.0490 | 0.0870 | 0.0790 | 0.0614 | ✅ |
| 10 | 0.4670 | 0.5245 | 0.0692 | 0.0640 | 0.1290 | 0.1088 | 0.0575 | ✅ |
| 11 | 0.4508 | 0.4761 | 0.0871 | 0.0725 | 0.1619 | 0.1322 | 0.0254 | ✅ |
| 12 | 0.4546 | 0.4881 | 0.0523 | 0.0421 | 0.1032 | 0.0794 | 0.0335 | ✅ |
| 13 | 0.5328 | 0.5908 | 0.0475 | 0.0485 | 0.0819 | 0.0758 | 0.0589 | ✅ |
| 14 | 0.4867 | 0.5530 | 0.0628 | 0.0672 | 0.1143 | 0.1083 | 0.0707 | ✅ |
| 15 | 0.5141 | 0.5368 | 0.0536 | 0.0471 | 0.0944 | 0.0807 | 0.0227 | ✅ |
| 16 | 0.4906 | 0.5170 | 0.0530 | 0.0396 | 0.0975 | 0.0711 | 0.0264 | ✅ |
| 17 | 0.5120 | 0.5373 | 0.0482 | 0.0516 | 0.0860 | 0.0877 | 0.0288 | ✅ |
| 18 | 0.4431 | 0.5361 | 0.1431 | 0.1548 | 0.2441 | 0.2241 | 0.1047 | ❌ |
| 19 | 0.4492 | 0.4116 | 0.1255 | 0.1077 | 0.2184 | 0.2074 | 0.0554 | ✅ |

### ECV 2025: personas por tamaño del hogar

| ccaa | sint_1 | sint_2 | sint_3 | sint_4 | sint_5+ | ref_1 | ref_2 | ref_3 | ref_4 | ref_5+ | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.1082 | 0.2257 | 0.2409 | 0.2674 | 0.1578 | 0.1071 | 0.2233 | 0.2409 | 0.2579 | 0.1708 | 0.0131 | ✅ |
| 02 | 0.1304 | 0.2443 | 0.2433 | 0.2502 | 0.1318 | 0.1283 | 0.2440 | 0.2449 | 0.2330 | 0.1499 | 0.0196 | ✅ |
| 03 | 0.1552 | 0.2916 | 0.2616 | 0.1896 | 0.1021 | 0.1546 | 0.2897 | 0.2655 | 0.1834 | 0.1068 | 0.0087 | ✅ |
| 04 | 0.0968 | 0.2074 | 0.2300 | 0.2394 | 0.2264 | 0.0970 | 0.2062 | 0.2313 | 0.2235 | 0.2420 | 0.0171 | ✅ |
| 05 | 0.1058 | 0.2102 | 0.2434 | 0.2229 | 0.2177 | 0.1053 | 0.2082 | 0.2429 | 0.1773 | 0.2663 | 0.0486 | ✅ |
| 06 | 0.1309 | 0.2499 | 0.2520 | 0.2316 | 0.1357 | 0.1295 | 0.2462 | 0.2512 | 0.2192 | 0.1539 | 0.0182 | ✅ |
| 07 | 0.1588 | 0.2628 | 0.2439 | 0.2184 | 0.1160 | 0.1573 | 0.2606 | 0.2455 | 0.2055 | 0.1311 | 0.0167 | ✅ |
| 08 | 0.1150 | 0.2229 | 0.2340 | 0.2593 | 0.1688 | 0.1150 | 0.2211 | 0.2357 | 0.2707 | 0.1574 | 0.0131 | ✅ |
| 09 | 0.1047 | 0.2358 | 0.2362 | 0.2440 | 0.1793 | 0.1040 | 0.2350 | 0.2371 | 0.2288 | 0.1951 | 0.0166 | ✅ |
| 10 | 0.1148 | 0.2361 | 0.2408 | 0.2456 | 0.1627 | 0.1147 | 0.2369 | 0.2428 | 0.2297 | 0.1760 | 0.0160 | ✅ |
| 11 | 0.1355 | 0.2515 | 0.2475 | 0.2596 | 0.1060 | 0.1335 | 0.2483 | 0.2488 | 0.2437 | 0.1257 | 0.0211 | ✅ |
| 12 | 0.1305 | 0.2449 | 0.2522 | 0.2239 | 0.1485 | 0.1296 | 0.2435 | 0.2530 | 0.2226 | 0.1513 | 0.0036 | ✅ |
| 13 | 0.1007 | 0.2226 | 0.2336 | 0.2531 | 0.1901 | 0.0985 | 0.2196 | 0.2330 | 0.2468 | 0.2020 | 0.0119 | ✅ |
| 14 | 0.0899 | 0.1962 | 0.2217 | 0.2757 | 0.2165 | 0.0888 | 0.1939 | 0.2219 | 0.2586 | 0.2368 | 0.0205 | ✅ |
| 15 | 0.1159 | 0.2222 | 0.2266 | 0.2520 | 0.1834 | 0.1152 | 0.2216 | 0.2264 | 0.2519 | 0.1848 | 0.0014 | ✅ |
| 16 | 0.1361 | 0.2671 | 0.2334 | 0.2411 | 0.1223 | 0.1337 | 0.2655 | 0.2360 | 0.2353 | 0.1295 | 0.0098 | ✅ |
| 17 | 0.1380 | 0.2514 | 0.2381 | 0.2435 | 0.1290 | 0.1364 | 0.2489 | 0.2398 | 0.2354 | 0.1396 | 0.0122 | ✅ |
| 18 | 0.0704 | 0.1443 | 0.1876 | 0.2453 | 0.3524 | 0.0587 | 0.1663 | 0.2109 | 0.2097 | 0.3543 | 0.0472 | ✅ |
| 19 | 0.0648 | 0.1435 | 0.1823 | 0.2292 | 0.3802 | 0.0733 | 0.1110 | 0.1503 | 0.2119 | 0.4536 | 0.0819 | ✅ |

### Padrón 01/01/2022: proporción de extranjeros por provincia

| provincia | sint_extranjera | ref_extranjera | tvd | dentro |
| --- | --- | --- | --- | --- |
| 01 | 0.1244 | 0.0987 | 0.0257 | ✅ |
| 02 | 0.0958 | 0.0714 | 0.0243 | ✅ |
| 03 | 0.2661 | 0.2044 | 0.0617 | ✅ |
| 04 | 0.2533 | 0.2189 | 0.0344 | ✅ |
| 05 | 0.1114 | 0.0663 | 0.0451 | ✅ |
| 06 | 0.0432 | 0.0319 | 0.0113 | ✅ |
| 07 | 0.2162 | 0.1887 | 0.0276 | ✅ |
| 08 | 0.1804 | 0.1548 | 0.0256 | ✅ |
| 09 | 0.1130 | 0.0835 | 0.0296 | ✅ |
| 10 | 0.0556 | 0.0357 | 0.0199 | ✅ |
| 11 | 0.0572 | 0.0419 | 0.0153 | ✅ |
| 12 | 0.1981 | 0.1540 | 0.0441 | ✅ |
| 13 | 0.0800 | 0.0644 | 0.0156 | ✅ |
| 14 | 0.0356 | 0.0279 | 0.0076 | ✅ |
| 15 | 0.0651 | 0.0416 | 0.0235 | ✅ |
| 16 | 0.1402 | 0.1164 | 0.0238 | ✅ |
| 17 | 0.2352 | 0.2046 | 0.0306 | ✅ |
| 18 | 0.0996 | 0.0750 | 0.0246 | ✅ |
| 19 | 0.1840 | 0.1388 | 0.0451 | ✅ |
| 20 | 0.1004 | 0.0847 | 0.0157 | ✅ |
| 21 | 0.1030 | 0.0968 | 0.0062 | ✅ |
| 22 | 0.1626 | 0.1321 | 0.0304 | ✅ |
| 23 | 0.0370 | 0.0283 | 0.0086 | ✅ |
| 24 | 0.0608 | 0.0456 | 0.0152 | ✅ |
| 25 | 0.2011 | 0.1887 | 0.0125 | ✅ |
| 26 | 0.1535 | 0.1305 | 0.0230 | ✅ |
| 27 | 0.0800 | 0.0520 | 0.0279 | ✅ |
| 28 | 0.1669 | 0.1407 | 0.0262 | ✅ |
| 29 | 0.2043 | 0.1673 | 0.0370 | ✅ |
| 30 | 0.1633 | 0.1480 | 0.0153 | ✅ |
| 31 | 0.1347 | 0.1106 | 0.0241 | ✅ |
| 32 | 0.0798 | 0.0543 | 0.0255 | ✅ |
| 33 | 0.0748 | 0.0454 | 0.0294 | ✅ |
| 34 | 0.0742 | 0.0473 | 0.0270 | ✅ |
| 35 | 0.1466 | 0.1265 | 0.0201 | ✅ |
| 36 | 0.0684 | 0.0412 | 0.0272 | ✅ |
| 37 | 0.0794 | 0.0487 | 0.0307 | ✅ |
| 38 | 0.1571 | 0.1389 | 0.0182 | ✅ |
| 39 | 0.0851 | 0.0636 | 0.0216 | ✅ |
| 40 | 0.1459 | 0.1185 | 0.0275 | ✅ |
| 41 | 0.0545 | 0.0411 | 0.0134 | ✅ |
| 42 | 0.1466 | 0.0996 | 0.0471 | ✅ |
| 43 | 0.1936 | 0.1681 | 0.0255 | ✅ |
| 44 | 0.1345 | 0.1161 | 0.0184 | ✅ |
| 45 | 0.1483 | 0.1042 | 0.0441 | ✅ |
| 46 | 0.1619 | 0.1170 | 0.0449 | ✅ |
| 47 | 0.0880 | 0.0568 | 0.0312 | ✅ |
| 48 | 0.0995 | 0.0785 | 0.0209 | ✅ |
| 49 | 0.0641 | 0.0379 | 0.0261 | ✅ |
| 50 | 0.1576 | 0.1235 | 0.0341 | ✅ |
| 51 | 0.0667 | 0.0591 | 0.0076 | ✅ |
| 52 | 0.1365 | 0.1371 | 0.0006 | ✅ |

## V-REPRO

2026-01-01_ES_10000_s1 generado de nuevo en otro directorio: mismos hashes.

- `persons.parquet`: `32ee417dca7e752a33dd841bf28341ee55674b09c2ec7a278c3bd6236a251c22`
- `households.parquet`: `5b8c0328533ffe7ae2f6354281c623f0f003f07557859a9d2330accb59f4b1d7`
- `lineage.parquet`: `51080b9cf2605f612cb4d91054871d1b3b3855f1576a4d5a5073003bc4944923`
