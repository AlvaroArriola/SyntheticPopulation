# Fase 04 · Tablas de validación

Generado por `python -m sinpop.validate.fase4` (git:907688d-dirty, 2026-10-16). Resumen en `fase_04_validacion.json`; detalle por población en `fase_04/`.

## Curva de error frente a tamaño (España; media de 5 semillas)

| n | tvd_media_calibradas | sd_calibradas | tvd_media_reservadas | sd_reservadas |
| --- | --- | --- | --- | --- |
| 10000 | 0.0254 | 0.0014 | 0.0213 | 0.0011 |
| 50000 | 0.0079 | 0.0004 | 0.0154 | 0.0002 |
| 100000 | 0.0041 | 0.0002 | 0.0149 | 0.0003 |
| 500000 | 0.0015 | 0.0001 | 0.0141 | 0.0001 |
| 1000000 | 0.0010 | 0.0001 | 0.0141 | 0.0000 |

## TVD por marginal calibrada (España; media de 5 semillas)

| objetivo | 1000000 | 50000 | 10000 | 500000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| actividad_sexo | 0.0008 | 0.0049 | 0.0095 | 0.0013 | 0.0028 |
| edad5_sexo | 0.0007 | 0.0026 | 0.0052 | 0.0010 | 0.0017 |
| edad5_sexo_colectivos | 0.0078 | 0.0737 | 0.2582 | 0.0108 | 0.0357 |
| edad5_sexo_familiares | 0.0007 | 0.0029 | 0.0054 | 0.0010 | 0.0018 |
| estudios_edad | 0.0006 | 0.0025 | 0.0055 | 0.0009 | 0.0018 |
| nacionalidad | 0.0002 | 0.0007 | 0.0019 | 0.0004 | 0.0004 |
| nacionalidad_edad | 0.0006 | 0.0026 | 0.0058 | 0.0009 | 0.0018 |
| nacionalidad_top | 0.0003 | 0.0008 | 0.0025 | 0.0004 | 0.0007 |
| tamano_hogar | 0.0002 | 0.0011 | 0.0027 | 0.0003 | 0.0007 |
| tipo_hogar | 0.0004 | 0.0022 | 0.0060 | 0.0006 | 0.0015 |
| tipo_residencia (implícito) | 0.0000 | 0.0001 | 0.0010 | 0.0000 | 0.0000 |
| urbanizacion | 0.0001 | 0.0007 | 0.0014 | 0.0001 | 0.0003 |

## TVD por cruce reservado (España; media de 5 semillas)

| objetivo | 1000000 | 10000 | 50000 | 100000 | 500000 |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | 0.0228 | 0.0282 | 0.0235 | 0.0241 | 0.0227 |
| adultos_nacionalidad | 0.0012 | 0.0028 | 0.0011 | 0.0011 | 0.0011 |
| estado_civil_edad | 0.0250 | 0.0260 | 0.0254 | 0.0260 | 0.0248 |
| estudios_sexo_edad | 0.0068 | 0.0177 | 0.0091 | 0.0080 | 0.0070 |
| nacionalidad_top_sexo_edad | 0.0077 | 0.0195 | 0.0124 | 0.0100 | 0.0084 |
| provincia_si_calibra_ccaa | 0.0091 | 0.0248 | 0.0108 | 0.0103 | 0.0090 |
| tamano_municipio | 0.0102 | 0.0145 | 0.0106 | 0.0099 | 0.0100 |
| tipo_hogar_edad4_ref | 0.0300 | 0.0369 | 0.0305 | 0.0297 | 0.0299 |

## Fallos por tamaño

| N | semilla | v_marg | v_cruce | v_cruce_excepciones | v_cruce_estricto | comprobaciones_cruce |
| --- | --- | --- | --- | --- | --- | --- |
| 10000 | 1 | 0 | 9 | 1 | 32 | 511 |
| 10000 | 2 | 0 | 12 | 0 | 35 | 511 |
| 10000 | 3 | 0 | 11 | 0 | 28 | 511 |
| 10000 | 4 | 0 | 4 | 0 | 21 | 511 |
| 10000 | 5 | 0 | 10 | 0 | 32 | 511 |
| 50000 | 1 | 0 | 2 | 1 | 13 | 511 |
| 50000 | 2 | 0 | 4 | 1 | 13 | 511 |
| 50000 | 3 | 0 | 4 | 1 | 9 | 511 |
| 50000 | 4 | 0 | 3 | 0 | 10 | 511 |
| 50000 | 5 | 0 | 4 | 1 | 11 | 511 |
| 100000 | 1 | 0 | 2 | 0 | 4 | 511 |
| 100000 | 2 | 0 | 2 | 1 | 5 | 511 |
| 100000 | 3 | 0 | 0 | 0 | 5 | 511 |
| 100000 | 4 | 0 | 0 | 0 | 4 | 511 |
| 100000 | 5 | 0 | 0 | 0 | 5 | 511 |
| 500000 | 1 | 0 | 1 | 0 | 1 | 511 |
| 500000 | 2 | 0 | 0 | 1 | 1 | 511 |
| 500000 | 3 | 0 | 1 | 0 | 1 | 511 |
| 500000 | 4 | 0 | 0 | 0 | 0 | 511 |
| 500000 | 5 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 1 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 2 | 0 | 1 | 0 | 2 | 511 |
| 1000000 | 3 | 0 | 1 | 1 | 2 | 511 |
| 1000000 | 4 | 0 | 1 | 0 | 1 | 511 |
| 1000000 | 5 | 0 | 0 | 1 | 1 | 511 |

### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas

| nivel | territorio | objetivo | tvd | umbral | excepcion | N | semilla |
| --- | --- | --- | --- | --- | --- | --- | --- |
| espana | ES | tipo_hogar_edad4_ref | 0.0302 | 0.0300 | ❌ | 500000 | 1 |
| provincia | PROV:40 | tamano_municipio | 0.0859 | 0.0800 | ✅ | 500000 | 2 |
| espana | ES | tipo_hogar_edad4_ref | 0.0307 | 0.0300 | ❌ | 500000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0800 | 0.0800 | ✅ | 1000000 | 1 |
| espana | ES | tipo_hogar_edad4_ref | 0.0302 | 0.0300 | ❌ | 1000000 | 2 |
| espana | ES | tipo_hogar_edad4_ref | 0.0300 | 0.0300 | ❌ | 1000000 | 3 |
| provincia | PROV:40 | tamano_municipio | 0.0833 | 0.0800 | ✅ | 1000000 | 3 |
| espana | ES | tipo_hogar_edad4_ref | 0.0301 | 0.0300 | ❌ | 1000000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0801 | 0.0800 | ✅ | 1000000 | 5 |

## V-SEMILLAS

| n | proporciones | fuera | razon_media | razon_max |
| --- | --- | --- | --- | --- |
| 10000 | 244 | 1 | 0.2915 | 1.5856 |
| 50000 | 244 | 0 | 0.2320 | 0.6965 |
| 100000 | 244 | 0 | 0.2171 | 0.4867 |
| 500000 | 244 | 0 | 0.2510 | 0.6008 |
| 1000000 | 244 | 0 | 0.2521 | 0.6381 |

## V-PESOS (calibración por comunidades)

| bloque | desviacion_max | proporcion_en_rango | kish_ratio | no_positivos | factor_min | factor_max | proporcion_local | ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 0.0000 | 1.0000 | 0.8626 | 0 | 0.2002 | 4.9981 | 0.9994 | ✅ |
| CCAA:02 | 0.0000 | 1.0000 | 0.8550 | 0 | 0.2018 | 4.9849 | 1.0000 | ✅ |
| CCAA:03 | 0.0000 | 1.0000 | 0.8402 | 0 | 0.2003 | 4.9547 | 0.9988 | ✅ |
| CCAA:04 | 0.0000 | 1.0000 | 0.7040 | 0 | 0.2000 | 4.9785 | 1.0000 | ✅ |
| CCAA:05 | 0.0000 | 1.0000 | 0.8102 | 0 | 0.2011 | 4.9986 | 1.0000 | ✅ |
| CCAA:06 | 0.0000 | 1.0000 | 0.8375 | 0 | 0.2058 | 4.8478 | 0.9999 | ✅ |
| CCAA:07 | 0.0000 | 1.0000 | 0.8582 | 0 | 0.2001 | 4.9959 | 0.9991 | ✅ |
| CCAA:08 | 0.0000 | 1.0000 | 0.8464 | 0 | 0.2037 | 4.9714 | 1.0000 | ✅ |
| CCAA:09 | 0.0000 | 1.0000 | 0.8291 | 0 | 0.2000 | 4.9985 | 1.0000 | ✅ |
| CCAA:10 | 0.0000 | 1.0000 | 0.8051 | 0 | 0.2015 | 4.9991 | 1.0000 | ✅ |
| CCAA:11 | 0.0000 | 1.0000 | 0.8834 | 0 | 0.2060 | 4.8702 | 0.9996 | ✅ |
| CCAA:12 | 0.0000 | 1.0000 | 0.8501 | 0 | 0.2011 | 4.9995 | 0.9990 | ✅ |
| CCAA:13 | 0.0000 | 1.0000 | 0.8256 | 0 | 0.2003 | 4.9997 | 1.0000 | ✅ |
| CCAA:14 | 0.0000 | 1.0000 | 0.8333 | 0 | 0.2001 | 4.9314 | 1.0000 | ✅ |
| CCAA:15 | 0.0000 | 1.0000 | 0.8727 | 0 | 0.2000 | 4.9669 | 1.0000 | ✅ |
| CCAA:16 | 0.0000 | 1.0000 | 0.8624 | 0 | 0.2051 | 4.9835 | 0.9999 | ✅ |
| CCAA:17 | 0.0000 | 1.0000 | 0.8560 | 0 | 0.2009 | 4.4942 | 0.9994 | ✅ |
| CCAA:18 | 0.0000 | 1.0000 | 0.7952 | 0 | 0.2012 | 4.0257 | 0.9931 | ✅ |
| CCAA:19 | 0.0000 | 1.0000 | 0.7839 | 0 | 0.2002 | 3.3071 | 0.9875 | ✅ |

## Ampliación de donantes

| bloque | objetivo | clave | locales | razon_inicial | anadidas |
| --- | --- | --- | --- | --- | --- |
| CCAA:01 | nacionalidad_top | nacionalidad_top=peru | 322 | 3.9510 | 19 |
| CCAA:03 | nacionalidad_top | nacionalidad_top=peru | 50 | 3.5617 | 1 |
| CCAA:03 | nacionalidad_top | nacionalidad_top=ucrania | 42 | 5.4382 | 7 |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 3 | 1.8881 | 1 |
| CCAA:07 | nacionalidad_top | nacionalidad_top=peru | 187 | 3.8136 | 7 |
| CCAA:11 | nacionalidad_top | nacionalidad_top=peru | 36 | 3.7553 | 2 |
| CCAA:12 | nacionalidad_top | nacionalidad_top=peru | 207 | 3.7108 | 7 |
| CCAA:12 | nacionalidad_top | nacionalidad_top=ucrania | 40 | 3.5008 | 4 |
| CCAA:16 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 8 | 4.4910 | 2 |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 8.1332 | 1 |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.9987 | 1 |
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
| actividad_edad | relacion_actividad × edad_actividad | 0.6136 | 0.6125 | 0.0011 | ✅ |
| adultos_nacionalidad | nacionalidad_esp_ext × es_adulto | 0.0028 | 0.0059 | 0.0031 | ✅ |
| estado_civil_edad | estado_civil × edad_estado_civil | 0.6242 | 0.6320 | 0.0079 | ✅ |
| estudios_sexo_edad | estudios_3 × sexo | 0.0391 | 0.0343 | 0.0048 | ✅ |
| estudios_sexo_edad | estudios_3 × edad_estudios | 0.6228 | 0.6229 | 0.0000 | ✅ |
| estudios_sexo_edad | sexo × edad_estudios | 0.0713 | 0.0705 | 0.0009 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × sexo | 0.0420 | 0.0447 | 0.0027 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × edad_nacionalidad | 0.1056 | 0.1069 | 0.0013 | ✅ |
| nacionalidad_top_sexo_edad | sexo × edad_nacionalidad | 0.0575 | 0.0566 | 0.0009 | ✅ |
| tipo_hogar_edad4_ref | tipo_hogar × edad_4 | 0.1810 | 0.1867 | 0.0057 | ✅ |

## Minorías, primera pasada (2026-01-01_ES_1000000_s1)

| grupo | unidad | esperado | observado | ratio | ok_representacion | donantes_distintos | top5 | ok_concentracion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mayores_85 | persona | 32798.2593 | 32776.0000 | 0.9993 | ✅ | 29385 | 0.0015 | ✅ |
| municipios_menos_2000 | persona | 54720.5868 | 56188.0000 | 1.0268 | ✅ | 25216 | 0.0019 | ✅ |
| parados | persona | 50477.7990 | 50740.0000 | 1.0052 | ✅ | 44848 | 0.0007 | ✅ |
| monoparentales | hogar | 46941.8606 | 46913.0000 | 0.9994 | ✅ | 46728 | 0.0004 | ✅ |
| mayores_solos | persona | 47337.8585 | 49216.0000 | 1.0397 | ✅ | 49071 | 0.0002 | ✅ |
| ceuta_melilla | persona | 3450.0330 | 3459.0000 | 1.0026 | ✅ | 1101 | 0.0185 | ✅ |
| nacionalidad_alemania | persona | 2750.5327 | 2789.0000 | 1.0140 | ✅ | 2039 | 0.0100 | ✅ |
| nacionalidad_argentina | persona | 3115.1697 | 3092.0000 | 0.9926 | ✅ | 2103 | 0.0107 | ✅ |
| nacionalidad_china | persona | 4968.6554 | 5003.0000 | 1.0069 | ✅ | 1581 | 0.0110 | ✅ |
| nacionalidad_colombia | persona | 14243.4673 | 14178.0000 | 0.9954 | ✅ | 6907 | 0.0047 | ✅ |
| nacionalidad_ecuador | persona | 2768.4181 | 2763.0000 | 0.9980 | ✅ | 1822 | 0.0141 | ✅ |
| nacionalidad_francia | persona | 2657.0437 | 2682.0000 | 1.0094 | ✅ | 1979 | 0.0112 | ✅ |
| nacionalidad_honduras | persona | 3667.8065 | 3680.0000 | 1.0033 | ✅ | 1766 | 0.0141 | ✅ |
| nacionalidad_italia | persona | 7188.0235 | 7185.0000 | 0.9996 | ✅ | 4601 | 0.0058 | ✅ |
| nacionalidad_marruecos | persona | 20303.5344 | 20256.0000 | 0.9977 | ✅ | 7982 | 0.0042 | ✅ |
| nacionalidad_paraguay | persona | 2555.2022 | 2555.0000 | 0.9999 | ✅ | 1356 | 0.0184 | ✅ |
| nacionalidad_peru | persona | 5439.5223 | 5398.0000 | 0.9924 | ✅ | 2634 | 0.0122 | ✅ |
| nacionalidad_reino_unido | persona | 5616.5321 | 5600.0000 | 0.9971 | ✅ | 3592 | 0.0059 | ✅ |
| nacionalidad_rumania | persona | 12833.1711 | 12854.0000 | 1.0016 | ✅ | 5771 | 0.0038 | ✅ |
| nacionalidad_ucrania | persona | 4259.9460 | 4230.0000 | 0.9930 | ✅ | 1790 | 0.0113 | ✅ |
| nacionalidad_venezuela | persona | 7938.7077 | 7893.0000 | 0.9942 | ✅ | 3794 | 0.0066 | ✅ |

## Reglas blandas (media de 5 semillas; nº de semillas dentro)

| regla | N | frecuencia_donantes | exceso_relativo | ok_estricto | ok |
| --- | --- | --- | --- | --- | --- |
| casado_menor_20 | 10000 | 0.000057 | -0.644805 | 4 | 5 |
| casado_menor_20 | 50000 | 0.000057 | 0.133602 | 3 | 5 |
| casado_menor_20 | 100000 | 0.000057 | -0.185585 | 4 | 5 |
| casado_menor_20 | 500000 | 0.000057 | -0.072628 | 4 | 5 |
| casado_menor_20 | 1000000 | 0.000057 | -0.016024 | 5 | 5 |
| estudiante_50_o_mas | 10000 | 0.000333 | 0.084284 | 3 | 5 |
| estudiante_50_o_mas | 50000 | 0.000333 | 0.010112 | 3 | 5 |
| estudiante_50_o_mas | 100000 | 0.000333 | 0.039843 | 4 | 5 |
| estudiante_50_o_mas | 500000 | 0.000333 | 0.079078 | 3 | 5 |
| estudiante_50_o_mas | 1000000 | 0.000333 | -0.033942 | 5 | 5 |
| hogar_8_o_mas | 10000 | 0.017379 | -0.139329 | 4 | 5 |
| hogar_8_o_mas | 50000 | 0.017379 | -0.078898 | 5 | 5 |
| hogar_8_o_mas | 100000 | 0.017379 | 0.005789 | 5 | 5 |
| hogar_8_o_mas | 500000 | 0.017379 | -0.017934 | 5 | 5 |
| hogar_8_o_mas | 1000000 | 0.017379 | 0.000475 | 5 | 5 |
| incapacidad_menor_25 | 10000 | 0.000171 | 0.055317 | 3 | 5 |
| incapacidad_menor_25 | 50000 | 0.000171 | 0.077085 | 4 | 4 |
| incapacidad_menor_25 | 100000 | 0.000171 | -0.063765 | 4 | 5 |
| incapacidad_menor_25 | 500000 | 0.000171 | -0.068832 | 5 | 5 |
| incapacidad_menor_25 | 1000000 | 0.000171 | 0.015332 | 5 | 5 |
| jubilado_menor_50 | 10000 | 0.000009 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 50000 | 0.000009 | 0.294539 | 2 | 5 |
| jubilado_menor_50 | 100000 | 0.000009 | -0.784284 | 5 | 5 |
| jubilado_menor_50 | 500000 | 0.000009 | -0.180669 | 4 | 5 |
| jubilado_menor_50 | 1000000 | 0.000009 | 0.228913 | 2 | 5 |
| ocupado_75_o_mas | 10000 | 0.001983 | -0.019122 | 4 | 5 |
| ocupado_75_o_mas | 50000 | 0.001983 | -0.018968 | 5 | 5 |
| ocupado_75_o_mas | 100000 | 0.001983 | -0.002112 | 5 | 5 |
| ocupado_75_o_mas | 500000 | 0.001983 | 0.010192 | 5 | 5 |
| ocupado_75_o_mas | 1000000 | 0.001983 | -0.015592 | 5 | 5 |
| superior_20_21 | 10000 | 0.003120 | 0.002762 | 4 | 5 |
| superior_20_21 | 50000 | 0.003120 | 0.030387 | 4 | 5 |
| superior_20_21 | 100000 | 0.003120 | -0.043044 | 5 | 5 |
| superior_20_21 | 500000 | 0.003120 | 0.007983 | 5 | 5 |
| superior_20_21 | 1000000 | 0.003120 | 0.000678 | 5 | 5 |
| viudo_menor_30 | 10000 | 0.000039 | 0.554787 | 2 | 5 |
| viudo_menor_30 | 50000 | 0.000039 | -0.172544 | 4 | 5 |
| viudo_menor_30 | 100000 | 0.000039 | 0.137403 | 3 | 5 |
| viudo_menor_30 | 500000 | 0.000039 | -0.080112 | 5 | 5 |
| viudo_menor_30 | 1000000 | 0.000039 | 0.074848 | 3 | 5 |

## G4.7 · Sobremuestreo (edad>=85:10000, 2026-01-01_ES_100000_s1_sm7d9288)

Miembros del grupo: 9882 (mínimo pedido 10000); α = 0.8705, β = 3.0490; suma de pesos 100103.

| objetivo | tvd | n_efectivo | umbral | ok |
| --- | --- | --- | --- | --- |
| actividad_sexo | 0.0034 | 90945.0158 | 0.0091 | ✅ |
| edad5_sexo | 0.0027 | 90945.0158 | 0.0134 | ✅ |
| edad5_sexo_colectivos | 0.0421 | 818.0836 | 0.1193 | ✅ |
| edad5_sexo_familiares | 0.0028 | 90142.4832 | 0.0133 | ✅ |
| estudios_edad | 0.0027 | 90945.0158 | 0.0121 | ✅ |
| nacionalidad | 0.0005 | 90945.0158 | 0.0054 | ✅ |
| nacionalidad_edad | 0.0022 | 90945.0158 | 0.0124 | ✅ |
| nacionalidad_top | 0.0009 | 90945.0158 | 0.0059 | ✅ |
| tamano_hogar | 0.0002 | 36586.9100 | 0.0093 | ✅ |
| tipo_hogar | 0.0011 | 36586.9100 | 0.0122 | ✅ |
| urbanizacion | 0.0006 | 90945.0158 | 0.0061 | ✅ |

## V-DONANTES (2026-01-01_ES_1000000_s1)

| territorio | personas | hogares_donantes | kish | proporcion_local | ok | confianza_reducida |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 176456 | 70175 | 53714.747 | 0.998 | ✅ | ❌ |
| CCAA:02 | 27862 | 11726 | 8877.173 | 1.000 | ✅ | ❌ |
| CCAA:03 | 20605 | 9339 | 7054.350 | 0.996 | ✅ | ❌ |
| CCAA:04 | 25400 | 9566 | 7092.008 | 1.000 | ✅ | ❌ |
| CCAA:05 | 45871 | 17674 | 12990.095 | 1.000 | ✅ | ❌ |
| CCAA:06 | 12032 | 5061 | 3793.738 | 1.000 | ✅ | ❌ |
| CCAA:07 | 48823 | 21886 | 16322.922 | 0.997 | ✅ | ❌ |
| CCAA:08 | 43451 | 17388 | 13143.440 | 1.000 | ✅ | ❌ |
| CCAA:09 | 165380 | 65551 | 49242.818 | 1.000 | ✅ | ❌ |
| CCAA:10 | 111476 | 45055 | 34000.095 | 1.000 | ✅ | ❌ |
| CCAA:11 | 21273 | 9106 | 7001.261 | 0.998 | ✅ | ❌ |
| CCAA:12 | 55031 | 23169 | 17463.978 | 0.997 | ✅ | ❌ |
| CCAA:13 | 144559 | 56080 | 42354.450 | 1.000 | ✅ | ❌ |
| CCAA:14 | 32364 | 11967 | 9058.606 | 1.000 | ✅ | ❌ |
| CCAA:15 | 13928 | 5508 | 4066.007 | 1.000 | ✅ | ❌ |
| CCAA:16 | 45415 | 19566 | 14799.852 | 1.000 | ✅ | ❌ |
| CCAA:17 | 6645 | 2831 | 2104.572 | 0.999 | ✅ | ❌ |
| CCAA:18 | 1704 | 550 | 388.184 | 0.996 | ✅ | ❌ |
| CCAA:19 | 1755 | 551 | 402.460 | 0.975 | ✅ | ❌ |
| ES | 1000030 | 402639 | 302661.079 | 0.999 | ✅ | ❌ |

## V-RAREZA

| nivel | combinaciones | sin_donante | personas_afectadas | ok |
| --- | --- | --- | --- | --- |
| persona | 25202 | 0 | 0 | ✅ |
| persona_y_hogar | 159272 | 0 | 0 | ✅ |

## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)

### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)

| ccaa | sint_ocupado | ref_ocupado | sint_parado | ref_parado | paro_sint | paro_epa | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.4936 | 0.4935 | 0.0856 | 0.0841 | 0.1477 | 0.1456 | 0.0017 | ✅ |
| 02 | 0.5448 | 0.5414 | 0.0458 | 0.0482 | 0.0775 | 0.0817 | 0.0034 | ✅ |
| 03 | 0.4706 | 0.4763 | 0.0532 | 0.0478 | 0.1016 | 0.0912 | 0.0058 | ✅ |
| 04 | 0.5837 | 0.6297 | 0.0371 | 0.0410 | 0.0598 | 0.0611 | 0.0498 | ✅ |
| 05 | 0.5266 | 0.5206 | 0.0712 | 0.0683 | 0.1190 | 0.1160 | 0.0089 | ✅ |
| 06 | 0.5117 | 0.5149 | 0.0485 | 0.0408 | 0.0866 | 0.0734 | 0.0077 | ✅ |
| 07 | 0.5011 | 0.4991 | 0.0461 | 0.0456 | 0.0842 | 0.0837 | 0.0025 | ✅ |
| 08 | 0.5250 | 0.5227 | 0.0688 | 0.0700 | 0.1159 | 0.1181 | 0.0023 | ✅ |
| 09 | 0.5683 | 0.5717 | 0.0481 | 0.0490 | 0.0780 | 0.0790 | 0.0044 | ✅ |
| 10 | 0.5213 | 0.5245 | 0.0640 | 0.0640 | 0.1093 | 0.1088 | 0.0033 | ✅ |
| 11 | 0.4821 | 0.4761 | 0.0757 | 0.0725 | 0.1356 | 0.1322 | 0.0091 | ✅ |
| 12 | 0.4922 | 0.4881 | 0.0429 | 0.0421 | 0.0802 | 0.0794 | 0.0050 | ✅ |
| 13 | 0.5862 | 0.5908 | 0.0470 | 0.0485 | 0.0742 | 0.0758 | 0.0060 | ✅ |
| 14 | 0.5470 | 0.5530 | 0.0644 | 0.0672 | 0.1053 | 0.1083 | 0.0088 | ✅ |
| 15 | 0.5445 | 0.5368 | 0.0506 | 0.0471 | 0.0850 | 0.0807 | 0.0112 | ✅ |
| 16 | 0.5221 | 0.5170 | 0.0448 | 0.0396 | 0.0791 | 0.0711 | 0.0104 | ✅ |
| 17 | 0.5425 | 0.5373 | 0.0467 | 0.0516 | 0.0792 | 0.0877 | 0.0052 | ✅ |
| 18 | 0.4786 | 0.5361 | 0.1518 | 0.1548 | 0.2408 | 0.2241 | 0.0605 | ✅ |
| 19 | 0.4848 | 0.4116 | 0.1234 | 0.1077 | 0.2029 | 0.2074 | 0.0888 | ✅ |

### ECV 2025: personas por tamaño del hogar

| ccaa | sint_1 | sint_2 | sint_3 | sint_4 | sint_5+ | ref_1 | ref_2 | ref_3 | ref_4 | ref_5+ | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.1083 | 0.2257 | 0.2406 | 0.2666 | 0.1587 | 0.1071 | 0.2233 | 0.2409 | 0.2579 | 0.1708 | 0.0124 | ✅ |
| 02 | 0.1304 | 0.2443 | 0.2417 | 0.2508 | 0.1328 | 0.1283 | 0.2440 | 0.2449 | 0.2330 | 0.1499 | 0.0202 | ✅ |
| 03 | 0.1558 | 0.2906 | 0.2637 | 0.1876 | 0.1022 | 0.1546 | 0.2897 | 0.2655 | 0.1834 | 0.1068 | 0.0064 | ✅ |
| 04 | 0.0967 | 0.2067 | 0.2310 | 0.2401 | 0.2255 | 0.0970 | 0.2062 | 0.2313 | 0.2235 | 0.2420 | 0.0171 | ✅ |
| 05 | 0.1059 | 0.2099 | 0.2433 | 0.2232 | 0.2177 | 0.1053 | 0.2082 | 0.2429 | 0.1773 | 0.2663 | 0.0486 | ✅ |
| 06 | 0.1319 | 0.2498 | 0.2491 | 0.2292 | 0.1400 | 0.1295 | 0.2462 | 0.2512 | 0.2192 | 0.1539 | 0.0160 | ✅ |
| 07 | 0.1586 | 0.2625 | 0.2442 | 0.2186 | 0.1162 | 0.1573 | 0.2606 | 0.2455 | 0.2055 | 0.1311 | 0.0163 | ✅ |
| 08 | 0.1151 | 0.2223 | 0.2357 | 0.2589 | 0.1679 | 0.1150 | 0.2211 | 0.2357 | 0.2707 | 0.1574 | 0.0118 | ✅ |
| 09 | 0.1047 | 0.2356 | 0.2357 | 0.2419 | 0.1821 | 0.1040 | 0.2350 | 0.2371 | 0.2288 | 0.1951 | 0.0144 | ✅ |
| 10 | 0.1149 | 0.2363 | 0.2407 | 0.2447 | 0.1634 | 0.1147 | 0.2369 | 0.2428 | 0.2297 | 0.1760 | 0.0152 | ✅ |
| 11 | 0.1357 | 0.2524 | 0.2490 | 0.2590 | 0.1039 | 0.1335 | 0.2483 | 0.2488 | 0.2437 | 0.1257 | 0.0218 | ✅ |
| 12 | 0.1302 | 0.2451 | 0.2522 | 0.2237 | 0.1489 | 0.1296 | 0.2435 | 0.2530 | 0.2226 | 0.1513 | 0.0033 | ✅ |
| 13 | 0.1006 | 0.2222 | 0.2338 | 0.2534 | 0.1901 | 0.0985 | 0.2196 | 0.2330 | 0.2468 | 0.2020 | 0.0120 | ✅ |
| 14 | 0.0895 | 0.1978 | 0.2237 | 0.2738 | 0.2151 | 0.0888 | 0.1939 | 0.2219 | 0.2586 | 0.2368 | 0.0217 | ✅ |
| 15 | 0.1164 | 0.2219 | 0.2241 | 0.2516 | 0.1859 | 0.1152 | 0.2216 | 0.2264 | 0.2519 | 0.1848 | 0.0026 | ✅ |
| 16 | 0.1362 | 0.2665 | 0.2344 | 0.2404 | 0.1225 | 0.1337 | 0.2655 | 0.2360 | 0.2353 | 0.1295 | 0.0086 | ✅ |
| 17 | 0.1377 | 0.2537 | 0.2409 | 0.2382 | 0.1294 | 0.1364 | 0.2489 | 0.2398 | 0.2354 | 0.1396 | 0.0101 | ✅ |
| 18 | 0.0705 | 0.1435 | 0.1865 | 0.2319 | 0.3676 | 0.0587 | 0.1663 | 0.2109 | 0.2097 | 0.3543 | 0.0473 | ✅ |
| 19 | 0.0641 | 0.1397 | 0.1871 | 0.2102 | 0.3990 | 0.0733 | 0.1110 | 0.1503 | 0.2119 | 0.4536 | 0.0655 | ✅ |

### Padrón 01/01/2022: proporción de extranjeros por provincia

| provincia | sint_extranjera | ref_extranjera | tvd | dentro |
| --- | --- | --- | --- | --- |
| 01 | 0.1201 | 0.0987 | 0.0214 | ✅ |
| 02 | 0.0950 | 0.0714 | 0.0236 | ✅ |
| 03 | 0.2643 | 0.2044 | 0.0599 | ✅ |
| 04 | 0.2590 | 0.2189 | 0.0401 | ✅ |
| 05 | 0.1076 | 0.0663 | 0.0413 | ✅ |
| 06 | 0.0436 | 0.0319 | 0.0116 | ✅ |
| 07 | 0.2163 | 0.1887 | 0.0276 | ✅ |
| 08 | 0.1794 | 0.1548 | 0.0246 | ✅ |
| 09 | 0.1094 | 0.0835 | 0.0260 | ✅ |
| 10 | 0.0544 | 0.0357 | 0.0187 | ✅ |
| 11 | 0.0552 | 0.0419 | 0.0133 | ✅ |
| 12 | 0.2010 | 0.1540 | 0.0471 | ✅ |
| 13 | 0.0785 | 0.0644 | 0.0141 | ✅ |
| 14 | 0.0363 | 0.0279 | 0.0083 | ✅ |
| 15 | 0.0655 | 0.0416 | 0.0239 | ✅ |
| 16 | 0.1423 | 0.1164 | 0.0259 | ✅ |
| 17 | 0.2355 | 0.2046 | 0.0309 | ✅ |
| 18 | 0.0977 | 0.0750 | 0.0227 | ✅ |
| 19 | 0.1867 | 0.1388 | 0.0479 | ✅ |
| 20 | 0.0986 | 0.0847 | 0.0140 | ✅ |
| 21 | 0.1097 | 0.0968 | 0.0129 | ✅ |
| 22 | 0.1671 | 0.1321 | 0.0349 | ✅ |
| 23 | 0.0365 | 0.0283 | 0.0082 | ✅ |
| 24 | 0.0702 | 0.0456 | 0.0246 | ✅ |
| 25 | 0.2059 | 0.1887 | 0.0173 | ✅ |
| 26 | 0.1535 | 0.1305 | 0.0230 | ✅ |
| 27 | 0.0759 | 0.0520 | 0.0238 | ✅ |
| 28 | 0.1670 | 0.1407 | 0.0262 | ✅ |
| 29 | 0.1977 | 0.1673 | 0.0303 | ✅ |
| 30 | 0.1631 | 0.1480 | 0.0151 | ✅ |
| 31 | 0.1340 | 0.1106 | 0.0233 | ✅ |
| 32 | 0.0743 | 0.0543 | 0.0200 | ✅ |
| 33 | 0.0752 | 0.0454 | 0.0298 | ✅ |
| 34 | 0.0696 | 0.0473 | 0.0224 | ✅ |
| 35 | 0.1485 | 0.1265 | 0.0221 | ✅ |
| 36 | 0.0703 | 0.0412 | 0.0292 | ✅ |
| 37 | 0.0770 | 0.0487 | 0.0284 | ✅ |
| 38 | 0.1547 | 0.1389 | 0.0158 | ✅ |
| 39 | 0.0848 | 0.0636 | 0.0212 | ✅ |
| 40 | 0.1385 | 0.1185 | 0.0200 | ✅ |
| 41 | 0.0557 | 0.0411 | 0.0145 | ✅ |
| 42 | 0.1619 | 0.0996 | 0.0624 | ✅ |
| 43 | 0.1963 | 0.1681 | 0.0282 | ✅ |
| 44 | 0.1349 | 0.1161 | 0.0188 | ✅ |
| 45 | 0.1468 | 0.1042 | 0.0426 | ✅ |
| 46 | 0.1625 | 0.1170 | 0.0455 | ✅ |
| 47 | 0.0872 | 0.0568 | 0.0304 | ✅ |
| 48 | 0.1023 | 0.0785 | 0.0238 | ✅ |
| 49 | 0.0627 | 0.0379 | 0.0247 | ✅ |
| 50 | 0.1558 | 0.1235 | 0.0323 | ✅ |
| 51 | 0.0681 | 0.0591 | 0.0090 | ✅ |
| 52 | 0.1328 | 0.1371 | 0.0043 | ✅ |

## V-REPRO

2026-01-01_ES_10000_s1 generado de nuevo en otro directorio: mismos hashes.

- `persons.parquet`: `3c217218771cff1bb282bc58036fb4e00816821801c61beb136dd704261eb976`
- `households.parquet`: `8deada7f04373a0d9f75126560f6d2a8dc2871545dccc8fc312110ef6c0a818c`
- `lineage.parquet`: `1615e9b3c7e9c960915be667d2e0799461a8752501e8dae3f425db32ce5bd0dd`
