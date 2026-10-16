# Fase 04 · Tablas de validación

Generado por `python -m sinpop.validate.fase4` (git:d7710dd-dirty, 2026-10-16). Resumen en `fase_04_validacion.json`; detalle por población en `fase_04/`.

## Curva de error frente a tamaño (España; media de 5 semillas)

| n | tvd_media_calibradas | sd_calibradas | tvd_media_reservadas | sd_reservadas |
| --- | --- | --- | --- | --- |
| 10000 | 0.0266 | 0.0021 | 0.0201 | 0.0010 |
| 50000 | 0.0092 | 0.0006 | 0.0152 | 0.0006 |
| 100000 | 0.0043 | 0.0004 | 0.0142 | 0.0005 |
| 500000 | 0.0016 | 0.0002 | 0.0136 | 0.0002 |
| 1000000 | 0.0010 | 0.0001 | 0.0135 | 0.0001 |

## TVD por marginal calibrada (España; media de 5 semillas)

| objetivo | 100000 | 1000000 | 50000 | 500000 | 10000 |
| --- | --- | --- | --- | --- | --- |
| actividad_sexo | 0.0017 | 0.0005 | 0.0024 | 0.0008 | 0.0060 |
| edad5_sexo | 0.0019 | 0.0007 | 0.0028 | 0.0010 | 0.0048 |
| edad5_sexo_colectivos | 0.0352 | 0.0069 | 0.0834 | 0.0115 | 0.2533 |
| edad5_sexo_familiares | 0.0019 | 0.0007 | 0.0030 | 0.0010 | 0.0053 |
| estudios_edad | 0.0021 | 0.0008 | 0.0028 | 0.0012 | 0.0054 |
| nacionalidad | 0.0007 | 0.0003 | 0.0008 | 0.0004 | 0.0021 |
| nacionalidad_top | 0.0009 | 0.0003 | 0.0011 | 0.0004 | 0.0032 |
| tamano_hogar | 0.0006 | 0.0002 | 0.0014 | 0.0004 | 0.0041 |
| tipo_hogar | 0.0015 | 0.0004 | 0.0026 | 0.0008 | 0.0057 |
| tipo_residencia (implícito) | 0.0001 | 0.0000 | 0.0001 | 0.0000 | 0.0004 |
| urbanizacion | 0.0004 | 0.0001 | 0.0006 | 0.0002 | 0.0020 |

## TVD por cruce reservado (España; media de 5 semillas)

| objetivo | 100000 | 10000 | 500000 | 50000 | 1000000 |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | 0.0146 | 0.0227 | 0.0143 | 0.0167 | 0.0141 |
| adultos_nacionalidad | 0.0050 | 0.0021 | 0.0058 | 0.0053 | 0.0057 |
| estado_civil_edad | 0.0256 | 0.0269 | 0.0252 | 0.0254 | 0.0254 |
| estudios_sexo_edad | 0.0082 | 0.0155 | 0.0066 | 0.0101 | 0.0066 |
| nacionalidad_top_sexo_edad | 0.0134 | 0.0216 | 0.0127 | 0.0152 | 0.0122 |
| provincia_si_calibra_ccaa | 0.0078 | 0.0239 | 0.0064 | 0.0101 | 0.0064 |
| tamano_municipio | 0.0096 | 0.0115 | 0.0093 | 0.0093 | 0.0092 |
| tipo_hogar_edad4_ref | 0.0293 | 0.0366 | 0.0287 | 0.0294 | 0.0288 |

## Fallos por tamaño

| N | semilla | v_marg | v_cruce | v_cruce_propuesta | comprobaciones_cruce |
| --- | --- | --- | --- | --- | --- |
| 10000 | 1 | 0 | 30 | 12 | 511 |
| 10000 | 2 | 0 | 30 | 13 | 511 |
| 10000 | 3 | 0 | 33 | 9 | 511 |
| 10000 | 4 | 0 | 26 | 8 | 511 |
| 10000 | 5 | 0 | 18 | 4 | 511 |
| 50000 | 1 | 0 | 15 | 4 | 511 |
| 50000 | 2 | 0 | 11 | 3 | 511 |
| 50000 | 3 | 0 | 6 | 2 | 511 |
| 50000 | 4 | 0 | 8 | 1 | 511 |
| 50000 | 5 | 0 | 7 | 4 | 511 |
| 100000 | 1 | 0 | 4 | 3 | 511 |
| 100000 | 2 | 0 | 1 | 0 | 511 |
| 100000 | 3 | 0 | 1 | 0 | 511 |
| 100000 | 4 | 0 | 6 | 1 | 511 |
| 100000 | 5 | 0 | 4 | 1 | 511 |
| 500000 | 1 | 0 | 0 | 0 | 511 |
| 500000 | 2 | 0 | 1 | 0 | 511 |
| 500000 | 3 | 0 | 0 | 0 | 511 |
| 500000 | 4 | 0 | 1 | 1 | 511 |
| 500000 | 5 | 0 | 1 | 1 | 511 |
| 1000000 | 1 | 0 | 1 | 1 | 511 |
| 1000000 | 2 | 0 | 1 | 1 | 511 |
| 1000000 | 3 | 0 | 0 | 0 | 511 |
| 1000000 | 4 | 0 | 1 | 1 | 511 |
| 1000000 | 5 | 0 | 1 | 1 | 511 |

### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas

| nivel | territorio | objetivo | tvd | umbral | N | semilla |
| --- | --- | --- | --- | --- | --- | --- |
| provincia | PROV:40 | estudios_sexo_edad | 0.0869 | 0.0842 | 500000 | 2 |
| provincia | PROV:40 | tamano_municipio | 0.0879 | 0.0800 | 500000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0953 | 0.0800 | 500000 | 5 |
| provincia | PROV:40 | tamano_municipio | 0.0890 | 0.0800 | 1000000 | 1 |
| provincia | PROV:40 | tamano_municipio | 0.0887 | 0.0800 | 1000000 | 2 |
| provincia | PROV:40 | tamano_municipio | 0.0860 | 0.0800 | 1000000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0846 | 0.0800 | 1000000 | 5 |

## V-SEMILLAS

| n | proporciones | fuera | razon_media | razon_max |
| --- | --- | --- | --- | --- |
| 10000 | 206 | 0 | 0.3066 | 1.4603 |
| 50000 | 206 | 0 | 0.2456 | 0.6830 |
| 100000 | 206 | 0 | 0.2455 | 0.5551 |
| 500000 | 206 | 0 | 0.2776 | 0.5765 |
| 1000000 | 206 | 0 | 0.2673 | 0.6525 |

## V-PESOS (calibración por comunidades)

| bloque | desviacion_max | proporcion_en_rango | kish_ratio | no_positivos | factor_min | factor_max | proporcion_local | ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 0.0000 | 1.0000 | 0.9243 | 0 | 0.2048 | 4.9979 | 0.9995 | ✅ |
| CCAA:02 | 0.0000 | 1.0000 | 0.9072 | 0 | 0.2023 | 4.9917 | 1.0000 | ✅ |
| CCAA:03 | 0.0000 | 1.0000 | 0.9027 | 0 | 0.2098 | 4.9719 | 0.9992 | ✅ |
| CCAA:04 | 0.0000 | 1.0000 | 0.8604 | 0 | 0.2002 | 4.9818 | 1.0000 | ✅ |
| CCAA:05 | 0.0000 | 1.0000 | 0.8884 | 0 | 0.2147 | 4.9483 | 1.0000 | ✅ |
| CCAA:06 | 0.0000 | 1.0000 | 0.9121 | 0 | 0.2535 | 4.8920 | 1.0000 | ✅ |
| CCAA:07 | 0.0000 | 1.0000 | 0.9043 | 0 | 0.2014 | 4.9877 | 0.9990 | ✅ |
| CCAA:08 | 0.0000 | 1.0000 | 0.9076 | 0 | 0.2147 | 4.9639 | 1.0000 | ✅ |
| CCAA:09 | 0.0000 | 1.0000 | 0.9235 | 0 | 0.2099 | 5.0000 | 1.0000 | ✅ |
| CCAA:10 | 0.0000 | 1.0000 | 0.8866 | 0 | 0.2105 | 4.9999 | 1.0000 | ✅ |
| CCAA:11 | 0.0000 | 1.0000 | 0.9262 | 0 | 0.2199 | 4.9825 | 0.9996 | ✅ |
| CCAA:12 | 0.0000 | 1.0000 | 0.9030 | 0 | 0.2080 | 4.9945 | 0.9990 | ✅ |
| CCAA:13 | 0.0000 | 1.0000 | 0.9151 | 0 | 0.2044 | 4.9805 | 1.0000 | ✅ |
| CCAA:14 | 0.0000 | 1.0000 | 0.9238 | 0 | 0.2120 | 4.7726 | 1.0000 | ✅ |
| CCAA:15 | 0.0000 | 1.0000 | 0.9229 | 0 | 0.2287 | 4.8758 | 1.0000 | ✅ |
| CCAA:16 | 0.0000 | 1.0000 | 0.9167 | 0 | 0.2248 | 4.9601 | 1.0000 | ✅ |
| CCAA:17 | 0.0000 | 1.0000 | 0.9127 | 0 | 0.2034 | 4.6185 | 0.9999 | ✅ |
| CCAA:18 | 0.0000 | 1.0000 | 0.8940 | 0 | 0.2358 | 2.8478 | 0.9957 | ✅ |
| CCAA:19 | 0.0000 | 1.0000 | 0.8382 | 0 | 0.2562 | 2.5300 | 0.9899 | ✅ |

## Ampliación de donantes

| bloque | objetivo | clave | locales | razon_inicial | anadidas |
| --- | --- | --- | --- | --- | --- |
| CCAA:01 | nacionalidad_top | nacionalidad_top=peru | 322 | 3.9510 | 168 |
| CCAA:03 | nacionalidad_top | nacionalidad_top=peru | 50 | 3.5617 | 15 |
| CCAA:03 | nacionalidad_top | nacionalidad_top=ucrania | 42 | 5.4382 | 20 |
| CCAA:07 | nacionalidad_top | nacionalidad_top=peru | 187 | 3.8136 | 101 |
| CCAA:11 | nacionalidad_top | nacionalidad_top=peru | 36 | 3.7553 | 16 |
| CCAA:12 | nacionalidad_top | nacionalidad_top=peru | 207 | 3.7108 | 105 |
| CCAA:12 | nacionalidad_top | nacionalidad_top=ucrania | 40 | 3.5008 | 10 |
| CCAA:17 | nacionalidad_top | nacionalidad_top=paraguay | 4 | 4.3333 | 1 |
| CCAA:18 | estudios_edad | estudios_3=superior;edad_estudios=90+ | 3 | 2.0488 | 2 |
| CCAA:18 | nacionalidad | nacionalidad_grupo=otros | 0 | None | 5 |
| CCAA:18 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.5142 | 1 |
| CCAA:18 | nacionalidad_top | nacionalidad_top=china | 1 | 2.3948 | 4 |
| CCAA:19 | estudios_edad | estudios_3=secundaria_2a_etapa;edad_estudios=90+ | 2 | 1.3648 | 3 |
| CCAA:19 | nacionalidad | nacionalidad_grupo=america_latina | 18 | 4.7103 | 12 |
| CCAA:19 | nacionalidad | nacionalidad_grupo=asia | 2 | 1.6472 | 3 |
| CCAA:19 | nacionalidad | nacionalidad_grupo=otros | 2 | 3.0749 | 3 |
| CCAA:19 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.6564 | 1 |
| CCAA:19 | nacionalidad_top | nacionalidad_top=colombia | 1 | 17.6844 | 4 |
| CCAA:19 | nacionalidad_top | nacionalidad_top=venezuela | 5 | 4.2542 | 3 |

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
| actividad_edad | relacion_actividad × edad_actividad | 0.6110 | 0.6111 | 0.0002 | ✅ |
| adultos_nacionalidad | nacionalidad_esp_ext × es_adulto | 0.0028 | 0.0213 | 0.0186 | ✅ |
| estado_civil_edad | estado_civil × edad_estado_civil | 0.6242 | 0.6324 | 0.0082 | ✅ |
| estudios_sexo_edad | estudios_3 × sexo | 0.0391 | 0.0362 | 0.0030 | ✅ |
| estudios_sexo_edad | estudios_3 × edad_estudios | 0.6228 | 0.6229 | 0.0000 | ✅ |
| estudios_sexo_edad | sexo × edad_estudios | 0.0713 | 0.0717 | 0.0004 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × sexo | 0.0420 | 0.0412 | 0.0008 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × edad_nacionalidad | 0.1056 | 0.1093 | 0.0037 | ✅ |
| nacionalidad_top_sexo_edad | sexo × edad_nacionalidad | 0.0575 | 0.0580 | 0.0005 | ✅ |
| tipo_hogar_edad4_ref | tipo_hogar × edad_4 | 0.1810 | 0.1845 | 0.0035 | ✅ |

## Minorías, primera pasada (2026-01-01_ES_1000000_s1)

| grupo | unidad | esperado | observado | ratio | ok_representacion | donantes_distintos | top5 | ok_concentracion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mayores_85 | persona | 32795.9307 | 32870.0000 | 1.0023 | ✅ | 29500 | 0.0010 | ✅ |
| municipios_menos_2000 | persona | 54716.7017 | 55841.0000 | 1.0205 | ✅ | 25122 | 0.0019 | ✅ |
| parados | persona | 54474.1848 | 54656.0000 | 1.0033 | ✅ | 48679 | 0.0005 | ✅ |
| monoparentales | hogar | 46940.8003 | 46956.0000 | 1.0003 | ✅ | 46777 | 0.0004 | ✅ |
| mayores_solos | persona | 47334.4976 | 49005.0000 | 1.0353 | ✅ | 48875 | 0.0002 | ✅ |
| ceuta_melilla | persona | 3449.7880 | 3452.0000 | 1.0006 | ✅ | 1104 | 0.0183 | ✅ |
| nacionalidad_alemania | persona | 2750.3374 | 2747.0000 | 0.9988 | ✅ | 1960 | 0.0124 | ✅ |
| nacionalidad_argentina | persona | 3114.9485 | 3108.0000 | 0.9978 | ✅ | 2048 | 0.0119 | ✅ |
| nacionalidad_china | persona | 4968.3026 | 5002.0000 | 1.0068 | ✅ | 1568 | 0.0122 | ✅ |
| nacionalidad_colombia | persona | 14242.4561 | 14176.0000 | 0.9953 | ✅ | 6784 | 0.0035 | ✅ |
| nacionalidad_ecuador | persona | 2768.2215 | 2798.0000 | 1.0108 | ✅ | 1766 | 0.0172 | ✅ |
| nacionalidad_francia | persona | 2656.8550 | 2619.0000 | 0.9858 | ✅ | 1863 | 0.0115 | ✅ |
| nacionalidad_honduras | persona | 3667.5461 | 3657.0000 | 0.9971 | ✅ | 1681 | 0.0137 | ✅ |
| nacionalidad_italia | persona | 7187.5131 | 7169.0000 | 0.9974 | ✅ | 4515 | 0.0052 | ✅ |
| nacionalidad_marruecos | persona | 20302.0929 | 20340.0000 | 1.0019 | ✅ | 7661 | 0.0043 | ✅ |
| nacionalidad_paraguay | persona | 2555.0207 | 2538.0000 | 0.9933 | ✅ | 1309 | 0.0209 | ✅ |
| nacionalidad_peru | persona | 5439.1362 | 5422.0000 | 0.9968 | ✅ | 2512 | 0.0148 | ✅ |
| nacionalidad_reino_unido | persona | 5616.1334 | 5579.0000 | 0.9934 | ✅ | 3567 | 0.0068 | ✅ |
| nacionalidad_rumania | persona | 12832.2600 | 12820.0000 | 0.9990 | ✅ | 5550 | 0.0043 | ✅ |
| nacionalidad_ucrania | persona | 4259.6435 | 4234.0000 | 0.9940 | ✅ | 1754 | 0.0154 | ✅ |
| nacionalidad_venezuela | persona | 7938.1441 | 7907.0000 | 0.9961 | ✅ | 3721 | 0.0071 | ✅ |

## Reglas blandas (media de 5 semillas; nº de semillas dentro)

| regla | N | frecuencia_donantes | exceso_relativo | ok_estricto | ok |
| --- | --- | --- | --- | --- | --- |
| casado_menor_20 | 10000 | 0.000056 | -0.278507 | 3 | 5 |
| casado_menor_20 | 50000 | 0.000056 | 0.438840 | 1 | 5 |
| casado_menor_20 | 100000 | 0.000056 | 0.222545 | 3 | 4 |
| casado_menor_20 | 500000 | 0.000056 | -0.014885 | 4 | 5 |
| casado_menor_20 | 1000000 | 0.000056 | -0.047316 | 4 | 5 |
| estudiante_50_o_mas | 10000 | 0.000455 | 0.190122 | 1 | 5 |
| estudiante_50_o_mas | 50000 | 0.000455 | -0.014930 | 4 | 4 |
| estudiante_50_o_mas | 100000 | 0.000455 | -0.010906 | 5 | 5 |
| estudiante_50_o_mas | 500000 | 0.000455 | 0.005652 | 5 | 5 |
| estudiante_50_o_mas | 1000000 | 0.000455 | 0.021411 | 5 | 5 |
| hogar_8_o_mas | 10000 | 0.017719 | -0.250657 | 5 | 5 |
| hogar_8_o_mas | 50000 | 0.017719 | -0.078921 | 5 | 5 |
| hogar_8_o_mas | 100000 | 0.017719 | -0.018856 | 5 | 5 |
| hogar_8_o_mas | 500000 | 0.017719 | -0.019766 | 5 | 5 |
| hogar_8_o_mas | 1000000 | 0.017719 | -0.000301 | 5 | 5 |
| incapacidad_menor_25 | 10000 | 0.000172 | 0.285758 | 1 | 5 |
| incapacidad_menor_25 | 50000 | 0.000172 | 0.049498 | 4 | 5 |
| incapacidad_menor_25 | 100000 | 0.000172 | 0.084147 | 3 | 5 |
| incapacidad_menor_25 | 500000 | 0.000172 | 0.002397 | 4 | 5 |
| incapacidad_menor_25 | 1000000 | 0.000172 | 0.008167 | 5 | 5 |
| jubilado_menor_50 | 10000 | 0.000012 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 50000 | 0.000012 | -0.020348 | 3 | 5 |
| jubilado_menor_50 | 100000 | 0.000012 | -0.183960 | 3 | 5 |
| jubilado_menor_50 | 500000 | 0.000012 | -0.020930 | 3 | 5 |
| jubilado_menor_50 | 1000000 | 0.000012 | 0.207512 | 2 | 4 |
| ocupado_75_o_mas | 10000 | 0.001618 | -0.194108 | 4 | 5 |
| ocupado_75_o_mas | 50000 | 0.001618 | -0.035154 | 5 | 5 |
| ocupado_75_o_mas | 100000 | 0.001618 | -0.031825 | 5 | 5 |
| ocupado_75_o_mas | 500000 | 0.001618 | -0.004269 | 5 | 5 |
| ocupado_75_o_mas | 1000000 | 0.001618 | -0.002228 | 5 | 5 |
| superior_20_21 | 10000 | 0.003377 | 0.033370 | 3 | 5 |
| superior_20_21 | 50000 | 0.003377 | 0.003779 | 5 | 5 |
| superior_20_21 | 100000 | 0.003377 | -0.077175 | 5 | 5 |
| superior_20_21 | 500000 | 0.003377 | -0.007185 | 5 | 5 |
| superior_20_21 | 1000000 | 0.003377 | -0.002333 | 5 | 5 |
| viudo_menor_30 | 10000 | 0.000038 | -0.472289 | 4 | 5 |
| viudo_menor_30 | 50000 | 0.000038 | 0.369184 | 3 | 5 |
| viudo_menor_30 | 100000 | 0.000038 | 0.052834 | 4 | 4 |
| viudo_menor_30 | 500000 | 0.000038 | -0.052583 | 3 | 5 |
| viudo_menor_30 | 1000000 | 0.000038 | 0.073685 | 2 | 5 |

## G4.7 · Sobremuestreo (edad>=85:10000, 2026-01-01_ES_100000_s1_sm7d9288)

Miembros del grupo: 9872 (mínimo pedido 10000); α = 0.8707, β = 3.0490; suma de pesos 100224.

| objetivo | tvd | n_efectivo | umbral | ok |
| --- | --- | --- | --- | --- |
| actividad_sexo | 0.0019 | 91045.4785 | 0.0090 | ✅ |
| edad5_sexo | 0.0022 | 91045.4785 | 0.0133 | ✅ |
| edad5_sexo_colectivos | 0.0410 | 801.3659 | 0.1206 | ✅ |
| edad5_sexo_familiares | 0.0023 | 90258.5888 | 0.0133 | ✅ |
| estudios_edad | 0.0025 | 91045.4785 | 0.0119 | ✅ |
| nacionalidad | 0.0009 | 91045.4785 | 0.0053 | ✅ |
| nacionalidad_top | 0.0014 | 91045.4785 | 0.0058 | ✅ |
| tamano_hogar | 0.0010 | 36604.4614 | 0.0093 | ✅ |
| tipo_hogar | 0.0016 | 36604.4614 | 0.0123 | ✅ |
| urbanizacion | 0.0003 | 91045.4785 | 0.0059 | ✅ |

## V-DONANTES (2026-01-01_ES_1000000_s1)

| territorio | personas | hogares_donantes | kish | proporcion_local | ok | confianza_reducida |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 176447 | 70204 | 53769.654 | 0.998 | ✅ | ❌ |
| CCAA:02 | 27883 | 11742 | 8861.477 | 1.000 | ✅ | ❌ |
| CCAA:03 | 20599 | 9344 | 7115.980 | 0.997 | ✅ | ❌ |
| CCAA:04 | 25398 | 9574 | 7108.238 | 1.000 | ✅ | ❌ |
| CCAA:05 | 45892 | 17708 | 13023.137 | 1.000 | ✅ | ❌ |
| CCAA:06 | 12037 | 5052 | 3788.254 | 1.000 | ✅ | ❌ |
| CCAA:07 | 48757 | 21864 | 16382.704 | 0.997 | ✅ | ❌ |
| CCAA:08 | 43486 | 17388 | 13132.898 | 1.000 | ✅ | ❌ |
| CCAA:09 | 165370 | 65648 | 49251.760 | 1.000 | ✅ | ❌ |
| CCAA:10 | 111446 | 45064 | 34127.271 | 1.000 | ✅ | ❌ |
| CCAA:11 | 21275 | 9116 | 6985.071 | 0.999 | ✅ | ❌ |
| CCAA:12 | 55044 | 23169 | 17533.605 | 0.997 | ✅ | ❌ |
| CCAA:13 | 144498 | 56132 | 42407.500 | 1.000 | ✅ | ❌ |
| CCAA:14 | 32399 | 11972 | 9141.536 | 1.000 | ✅ | ❌ |
| CCAA:15 | 13929 | 5537 | 4118.296 | 1.000 | ✅ | ❌ |
| CCAA:16 | 45413 | 19616 | 14895.816 | 1.000 | ✅ | ❌ |
| CCAA:17 | 6634 | 2818 | 2112.613 | 0.999 | ✅ | ❌ |
| CCAA:18 | 1701 | 551 | 393.928 | 0.988 | ✅ | ❌ |
| CCAA:19 | 1751 | 553 | 409.510 | 0.981 | ✅ | ❌ |
| ES | 999959 | 402954 | 303377.690 | 0.999 | ✅ | ❌ |

## V-RAREZA

| nivel | combinaciones | sin_donante | personas_afectadas | ok |
| --- | --- | --- | --- | --- |
| persona | 25407 | 0 | 0 | ✅ |
| persona_y_hogar | 163758 | 0 | 0 | ✅ |

## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)

### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)

| ccaa | sint_ocupado | ref_ocupado | sint_parado | ref_parado | paro_sint | paro_epa | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.4501 | 0.4935 | 0.0935 | 0.0841 | 0.1719 | 0.1456 | 0.0433 | ✅ |
| 02 | 0.5144 | 0.5414 | 0.0443 | 0.0482 | 0.0793 | 0.0817 | 0.0309 | ✅ |
| 03 | 0.4278 | 0.4763 | 0.0613 | 0.0478 | 0.1253 | 0.0912 | 0.0485 | ✅ |
| 04 | 0.4671 | 0.6297 | 0.0313 | 0.0410 | 0.0627 | 0.0611 | 0.1723 | ❌ |
| 05 | 0.4840 | 0.5206 | 0.0853 | 0.0683 | 0.1499 | 0.1160 | 0.0366 | ✅ |
| 06 | 0.4587 | 0.5149 | 0.0584 | 0.0408 | 0.1129 | 0.0734 | 0.0562 | ✅ |
| 07 | 0.4696 | 0.4991 | 0.0517 | 0.0456 | 0.0992 | 0.0837 | 0.0295 | ✅ |
| 08 | 0.4905 | 0.5227 | 0.0742 | 0.0700 | 0.1314 | 0.1181 | 0.0322 | ✅ |
| 09 | 0.5107 | 0.5717 | 0.0483 | 0.0490 | 0.0865 | 0.0790 | 0.0616 | ✅ |
| 10 | 0.4661 | 0.5245 | 0.0695 | 0.0640 | 0.1298 | 0.1088 | 0.0584 | ✅ |
| 11 | 0.4487 | 0.4761 | 0.0870 | 0.0725 | 0.1624 | 0.1322 | 0.0274 | ✅ |
| 12 | 0.4534 | 0.4881 | 0.0524 | 0.0421 | 0.1037 | 0.0794 | 0.0347 | ✅ |
| 13 | 0.5325 | 0.5908 | 0.0477 | 0.0485 | 0.0822 | 0.0758 | 0.0591 | ✅ |
| 14 | 0.4866 | 0.5530 | 0.0630 | 0.0672 | 0.1146 | 0.1083 | 0.0705 | ✅ |
| 15 | 0.5120 | 0.5368 | 0.0535 | 0.0471 | 0.0947 | 0.0807 | 0.0248 | ✅ |
| 16 | 0.4935 | 0.5170 | 0.0538 | 0.0396 | 0.0984 | 0.0711 | 0.0234 | ✅ |
| 17 | 0.5113 | 0.5373 | 0.0478 | 0.0516 | 0.0855 | 0.0877 | 0.0298 | ✅ |
| 18 | 0.4398 | 0.5361 | 0.1451 | 0.1548 | 0.2481 | 0.2241 | 0.1059 | ❌ |
| 19 | 0.4512 | 0.4116 | 0.1181 | 0.1077 | 0.2074 | 0.2074 | 0.0499 | ✅ |

### ECV 2025: personas por tamaño del hogar

| ccaa | sint_1 | sint_2 | sint_3 | sint_4 | sint_5+ | ref_1 | ref_2 | ref_3 | ref_4 | ref_5+ | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.1082 | 0.2261 | 0.2406 | 0.2671 | 0.1580 | 0.1071 | 0.2233 | 0.2409 | 0.2579 | 0.1708 | 0.0132 | ✅ |
| 02 | 0.1302 | 0.2434 | 0.2433 | 0.2500 | 0.1330 | 0.1283 | 0.2440 | 0.2449 | 0.2330 | 0.1499 | 0.0190 | ✅ |
| 03 | 0.1556 | 0.2914 | 0.2644 | 0.1861 | 0.1025 | 0.1546 | 0.2897 | 0.2655 | 0.1834 | 0.1068 | 0.0054 | ✅ |
| 04 | 0.0970 | 0.2064 | 0.2305 | 0.2409 | 0.2252 | 0.0970 | 0.2062 | 0.2313 | 0.2235 | 0.2420 | 0.0176 | ✅ |
| 05 | 0.1059 | 0.2100 | 0.2429 | 0.2219 | 0.2193 | 0.1053 | 0.2082 | 0.2429 | 0.1773 | 0.2663 | 0.0470 | ✅ |
| 06 | 0.1303 | 0.2506 | 0.2536 | 0.2294 | 0.1361 | 0.1295 | 0.2462 | 0.2512 | 0.2192 | 0.1539 | 0.0178 | ✅ |
| 07 | 0.1589 | 0.2626 | 0.2438 | 0.2200 | 0.1147 | 0.1573 | 0.2606 | 0.2455 | 0.2055 | 0.1311 | 0.0181 | ✅ |
| 08 | 0.1154 | 0.2217 | 0.2345 | 0.2583 | 0.1701 | 0.1150 | 0.2211 | 0.2357 | 0.2707 | 0.1574 | 0.0136 | ✅ |
| 09 | 0.1047 | 0.2361 | 0.2358 | 0.2436 | 0.1799 | 0.1040 | 0.2350 | 0.2371 | 0.2288 | 0.1951 | 0.0166 | ✅ |
| 10 | 0.1147 | 0.2366 | 0.2411 | 0.2453 | 0.1623 | 0.1147 | 0.2369 | 0.2428 | 0.2297 | 0.1760 | 0.0156 | ✅ |
| 11 | 0.1356 | 0.2520 | 0.2483 | 0.2590 | 0.1051 | 0.1335 | 0.2483 | 0.2488 | 0.2437 | 0.1257 | 0.0212 | ✅ |
| 12 | 0.1304 | 0.2443 | 0.2516 | 0.2233 | 0.1504 | 0.1296 | 0.2435 | 0.2530 | 0.2226 | 0.1513 | 0.0023 | ✅ |
| 13 | 0.1008 | 0.2226 | 0.2337 | 0.2535 | 0.1894 | 0.0985 | 0.2196 | 0.2330 | 0.2468 | 0.2020 | 0.0126 | ✅ |
| 14 | 0.0898 | 0.1962 | 0.2225 | 0.2738 | 0.2177 | 0.0888 | 0.1939 | 0.2219 | 0.2586 | 0.2368 | 0.0191 | ✅ |
| 15 | 0.1160 | 0.2220 | 0.2256 | 0.2516 | 0.1848 | 0.1152 | 0.2216 | 0.2264 | 0.2519 | 0.1848 | 0.0012 | ✅ |
| 16 | 0.1362 | 0.2667 | 0.2348 | 0.2390 | 0.1233 | 0.1337 | 0.2655 | 0.2360 | 0.2353 | 0.1295 | 0.0074 | ✅ |
| 17 | 0.1396 | 0.2517 | 0.2382 | 0.2380 | 0.1325 | 0.1364 | 0.2489 | 0.2398 | 0.2354 | 0.1396 | 0.0087 | ✅ |
| 18 | 0.0707 | 0.1425 | 0.1868 | 0.2395 | 0.3605 | 0.0587 | 0.1663 | 0.2109 | 0.2097 | 0.3543 | 0.0479 | ✅ |
| 19 | 0.0637 | 0.1424 | 0.1824 | 0.2085 | 0.4030 | 0.0733 | 0.1110 | 0.1503 | 0.2119 | 0.4536 | 0.0636 | ✅ |

### Padrón 01/01/2022: proporción de extranjeros por provincia

| provincia | sint_extranjera | ref_extranjera | tvd | dentro |
| --- | --- | --- | --- | --- |
| 01 | 0.1261 | 0.0987 | 0.0274 | ✅ |
| 02 | 0.0938 | 0.0714 | 0.0224 | ✅ |
| 03 | 0.2658 | 0.2044 | 0.0614 | ✅ |
| 04 | 0.2597 | 0.2189 | 0.0408 | ✅ |
| 05 | 0.1127 | 0.0663 | 0.0464 | ✅ |
| 06 | 0.0446 | 0.0319 | 0.0127 | ✅ |
| 07 | 0.2161 | 0.1887 | 0.0274 | ✅ |
| 08 | 0.1794 | 0.1548 | 0.0246 | ✅ |
| 09 | 0.1117 | 0.0835 | 0.0282 | ✅ |
| 10 | 0.0527 | 0.0357 | 0.0170 | ✅ |
| 11 | 0.0548 | 0.0419 | 0.0129 | ✅ |
| 12 | 0.2021 | 0.1540 | 0.0482 | ✅ |
| 13 | 0.0836 | 0.0644 | 0.0193 | ✅ |
| 14 | 0.0339 | 0.0279 | 0.0060 | ✅ |
| 15 | 0.0653 | 0.0416 | 0.0237 | ✅ |
| 16 | 0.1440 | 0.1164 | 0.0276 | ✅ |
| 17 | 0.2362 | 0.2046 | 0.0315 | ✅ |
| 18 | 0.0969 | 0.0750 | 0.0219 | ✅ |
| 19 | 0.1897 | 0.1388 | 0.0508 | ✅ |
| 20 | 0.1025 | 0.0847 | 0.0178 | ✅ |
| 21 | 0.1031 | 0.0968 | 0.0063 | ✅ |
| 22 | 0.1576 | 0.1321 | 0.0254 | ✅ |
| 23 | 0.0384 | 0.0283 | 0.0101 | ✅ |
| 24 | 0.0627 | 0.0456 | 0.0172 | ✅ |
| 25 | 0.2024 | 0.1887 | 0.0137 | ✅ |
| 26 | 0.1535 | 0.1305 | 0.0229 | ✅ |
| 27 | 0.0768 | 0.0520 | 0.0247 | ✅ |
| 28 | 0.1669 | 0.1407 | 0.0261 | ✅ |
| 29 | 0.2009 | 0.1673 | 0.0336 | ✅ |
| 30 | 0.1639 | 0.1480 | 0.0159 | ✅ |
| 31 | 0.1353 | 0.1106 | 0.0247 | ✅ |
| 32 | 0.0801 | 0.0543 | 0.0258 | ✅ |
| 33 | 0.0748 | 0.0454 | 0.0293 | ✅ |
| 34 | 0.0718 | 0.0473 | 0.0246 | ✅ |
| 35 | 0.1456 | 0.1265 | 0.0191 | ✅ |
| 36 | 0.0673 | 0.0412 | 0.0261 | ✅ |
| 37 | 0.0777 | 0.0487 | 0.0290 | ✅ |
| 38 | 0.1570 | 0.1389 | 0.0181 | ✅ |
| 39 | 0.0849 | 0.0636 | 0.0214 | ✅ |
| 40 | 0.1542 | 0.1185 | 0.0358 | ✅ |
| 41 | 0.0568 | 0.0411 | 0.0157 | ✅ |
| 42 | 0.1545 | 0.0996 | 0.0549 | ✅ |
| 43 | 0.1978 | 0.1681 | 0.0297 | ✅ |
| 44 | 0.1432 | 0.1161 | 0.0271 | ✅ |
| 45 | 0.1445 | 0.1042 | 0.0403 | ✅ |
| 46 | 0.1604 | 0.1170 | 0.0434 | ✅ |
| 47 | 0.0848 | 0.0568 | 0.0280 | ✅ |
| 48 | 0.0975 | 0.0785 | 0.0189 | ✅ |
| 49 | 0.0587 | 0.0379 | 0.0208 | ✅ |
| 50 | 0.1570 | 0.1235 | 0.0335 | ✅ |
| 51 | 0.0682 | 0.0591 | 0.0091 | ✅ |
| 52 | 0.1296 | 0.1371 | 0.0074 | ✅ |

## V-REPRO

2026-01-01_ES_10000_s1 generado de nuevo en otro directorio: mismos hashes.

- `persons.parquet`: `230fc34797e9823ce3b8bd89a6b9a03eefe40be11d245f6e8d4371047b7afeeb`
- `households.parquet`: `427a09f11400f9289b32365a3b6a5b39267415d94dd919eb426034e6610a3fb2`
- `lineage.parquet`: `b1ee4eba4023126323582ee43b602d679125339f5c72c7bdbb362789ea600436`
