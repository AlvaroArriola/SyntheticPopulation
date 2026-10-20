# Fase 04 · Tablas de validación

Generado por `python -m sinpop.validate.fase4` (git:6162e0f-dirty, 2026-10-20). Resumen en `fase_04_validacion.json`; detalle por población en `fase_04/`.

## Curva de error frente a tamaño (España; media de 5 semillas)

| n | tvd_media_calibradas | sd_calibradas | tvd_media_reservadas | sd_reservadas |
| --- | --- | --- | --- | --- |
| 10000 | 0.0178 | 0.0025 | 0.0156 | 0.0014 |
| 50000 | 0.0054 | 0.0004 | 0.0094 | 0.0006 |
| 100000 | 0.0030 | 0.0001 | 0.0084 | 0.0004 |
| 500000 | 0.0011 | 0.0001 | 0.0077 | 0.0001 |
| 1000000 | 0.0008 | 0.0001 | 0.0076 | 0.0001 |

## TVD por marginal calibrada (España; media de 5 semillas)

| objetivo | 500000 | 50000 | 1000000 | 10000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| actividad_nacionalidad | 0.0012 | 0.0030 | 0.0008 | 0.0070 | 0.0020 |
| actividad_tramo | 0.0013 | 0.0032 | 0.0008 | 0.0063 | 0.0020 |
| edad5_sexo | 0.0007 | 0.0019 | 0.0006 | 0.0044 | 0.0015 |
| edad5_sexo_colectivos | 0.0099 | 0.0713 | 0.0075 | 0.2524 | 0.0354 |
| edad5_sexo_familiares | 0.0007 | 0.0020 | 0.0006 | 0.0049 | 0.0016 |
| estado_civil_edad | 0.0009 | 0.0024 | 0.0006 | 0.0062 | 0.0020 |
| estudios_edad | 0.0008 | 0.0027 | 0.0006 | 0.0062 | 0.0017 |
| nacimiento_nacionalidad | 0.0004 | 0.0009 | 0.0003 | 0.0027 | 0.0005 |
| nacionalidad | 0.0002 | 0.0006 | 0.0001 | 0.0016 | 0.0004 |
| nacionalidad_edad | 0.0007 | 0.0020 | 0.0005 | 0.0058 | 0.0013 |
| nacionalidad_top | 0.0001 | 0.0003 | 0.0001 | 0.0020 | 0.0001 |
| nacionalidad_top_edad | 0.0004 | 0.0011 | 0.0002 | 0.0038 | 0.0007 |
| nacionalidad_top_sexo | 0.0003 | 0.0006 | 0.0002 | 0.0027 | 0.0005 |
| sin_estudios_edad | 0.0004 | 0.0013 | 0.0003 | 0.0030 | 0.0008 |
| tamano_hogar | 0.0004 | 0.0008 | 0.0001 | 0.0027 | 0.0009 |
| tipo_hogar | 0.0007 | 0.0024 | 0.0004 | 0.0057 | 0.0020 |
| tipo_residencia (implícito) | 0.0000 | 0.0002 | 0.0000 | 0.0008 | 0.0001 |
| urbanizacion | 0.0003 | 0.0008 | 0.0002 | 0.0021 | 0.0005 |

## TVD por cruce reservado (España; media de 5 semillas)

| objetivo | 10000 | 1000000 | 500000 | 100000 | 50000 |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | 0.0186 | 0.0095 | 0.0093 | 0.0110 | 0.0120 |
| actividad_sexo | 0.0092 | 0.0050 | 0.0052 | 0.0056 | 0.0063 |
| adultos_nacionalidad | 0.0026 | 0.0015 | 0.0014 | 0.0016 | 0.0015 |
| estudios_sexo_edad | 0.0172 | 0.0073 | 0.0072 | 0.0081 | 0.0097 |
| nacionalidad_top_sexo_edad | 0.0163 | 0.0043 | 0.0044 | 0.0061 | 0.0073 |
| provincia_si_calibra_ccaa | 0.0246 | 0.0083 | 0.0085 | 0.0097 | 0.0118 |
| tamano_municipio | 0.0125 | 0.0111 | 0.0114 | 0.0110 | 0.0121 |
| tipo_hogar_edad4_ref | 0.0238 | 0.0138 | 0.0137 | 0.0143 | 0.0144 |

## Fallos por tamaño

| N | semilla | v_marg | v_cruce | v_cruce_excepciones | v_cruce_estricto | comprobaciones_cruce |
| --- | --- | --- | --- | --- | --- | --- |
| 10000 | 1 | 1 | 14 | 1 | 26 | 511 |
| 10000 | 2 | 0 | 7 | 0 | 17 | 511 |
| 10000 | 3 | 0 | 14 | 0 | 24 | 511 |
| 10000 | 4 | 0 | 7 | 0 | 23 | 511 |
| 10000 | 5 | 0 | 6 | 0 | 15 | 511 |
| 50000 | 1 | 0 | 4 | 0 | 9 | 511 |
| 50000 | 2 | 0 | 1 | 0 | 2 | 511 |
| 50000 | 3 | 0 | 2 | 1 | 8 | 511 |
| 50000 | 4 | 0 | 2 | 1 | 5 | 511 |
| 50000 | 5 | 0 | 1 | 0 | 5 | 511 |
| 100000 | 1 | 0 | 1 | 1 | 2 | 511 |
| 100000 | 2 | 0 | 1 | 1 | 6 | 511 |
| 100000 | 3 | 0 | 1 | 1 | 2 | 511 |
| 100000 | 4 | 0 | 1 | 0 | 4 | 511 |
| 100000 | 5 | 0 | 1 | 0 | 2 | 511 |
| 500000 | 1 | 0 | 0 | 0 | 0 | 511 |
| 500000 | 2 | 0 | 0 | 0 | 0 | 511 |
| 500000 | 3 | 0 | 0 | 0 | 0 | 511 |
| 500000 | 4 | 0 | 0 | 0 | 0 | 511 |
| 500000 | 5 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 1 | 0 | 0 | 1 | 1 | 511 |
| 1000000 | 2 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 3 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 4 | 0 | 0 | 0 | 0 | 511 |
| 1000000 | 5 | 0 | 0 | 1 | 1 | 511 |

### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas

| nivel | territorio | objetivo | tvd | umbral | excepcion | N | semilla |
| --- | --- | --- | --- | --- | --- | --- | --- |
| provincia | PROV:40 | tamano_municipio | 0.0815 | 0.0800 | ✅ | 1000000 | 1 |
| provincia | PROV:40 | tamano_municipio | 0.0815 | 0.0800 | ✅ | 1000000 | 5 |

## V-SEMILLAS

| n | proporciones | fuera | razon_media | razon_max |
| --- | --- | --- | --- | --- |
| 10000 | 527 | 2 | 0.3065 | 2.3106 |
| 50000 | 527 | 0 | 0.2324 | 0.7702 |
| 100000 | 527 | 0 | 0.2113 | 0.5651 |
| 500000 | 527 | 0 | 0.2193 | 0.7205 |
| 1000000 | 527 | 0 | 0.2230 | 0.5268 |

## V-PESOS (calibración por comunidades)

| bloque | desviacion_max | proporcion_en_rango | kish_ratio | no_positivos | factor_min | factor_max | proporcion_local | ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 0.0000 | 1.0000 | 0.7902 | 0 | 0.2000 | 4.9934 | 0.9058 | ✅ |
| CCAA:02 | 0.0000 | 1.0000 | 0.7915 | 0 | 0.2000 | 5.0000 | 0.9788 | ✅ |
| CCAA:03 | 0.0000 | 1.0000 | 0.7964 | 0 | 0.2000 | 4.9871 | 0.9725 | ✅ |
| CCAA:04 | 0.0000 | 1.0000 | 0.6538 | 0 | 0.2000 | 4.9812 | 0.8345 | ✅ |
| CCAA:05 | 0.0000 | 1.0000 | 0.6914 | 0 | 0.2000 | 4.9971 | 0.9890 | ✅ |
| CCAA:06 | 0.0000 | 1.0000 | 0.7877 | 0 | 0.2000 | 4.8772 | 0.8955 | ✅ |
| CCAA:07 | 0.0000 | 1.0000 | 0.8089 | 0 | 0.2000 | 4.9945 | 0.9739 | ✅ |
| CCAA:08 | 0.0000 | 1.0000 | 0.7612 | 0 | 0.2000 | 5.0000 | 0.9761 | ✅ |
| CCAA:09 | 0.0000 | 1.0000 | 0.6956 | 0 | 0.2000 | 5.0000 | 0.9825 | ✅ |
| CCAA:10 | 0.0000 | 1.0000 | 0.7278 | 0 | 0.2000 | 5.0000 | 0.9541 | ✅ |
| CCAA:11 | 0.0000 | 1.0000 | 0.8129 | 0 | 0.2000 | 4.9004 | 0.9403 | ✅ |
| CCAA:12 | 0.0000 | 1.0000 | 0.7973 | 0 | 0.2000 | 4.9983 | 0.9763 | ✅ |
| CCAA:13 | 0.0000 | 1.0000 | 0.7394 | 0 | 0.2000 | 5.0000 | 0.9703 | ✅ |
| CCAA:14 | 0.0000 | 1.0000 | 0.7431 | 0 | 0.2000 | 4.9896 | 0.8987 | ✅ |
| CCAA:15 | 0.0000 | 1.0000 | 0.7781 | 0 | 0.2000 | 4.9556 | 0.9010 | ✅ |
| CCAA:16 | 0.0000 | 1.0000 | 0.7831 | 0 | 0.2000 | 5.0000 | 0.9869 | ✅ |
| CCAA:17 | 0.0000 | 1.0000 | 0.7927 | 0 | 0.2000 | 4.9442 | 0.8796 | ✅ |
| CCAA:18 | 0.0000 | 1.0000 | 0.5888 | 0 | 0.2000 | 5.0000 | 0.9804 | ✅ |
| CCAA:19 | 0.0000 | 1.0000 | 0.6033 | 0 | 0.2000 | 4.9988 | 0.9518 | ✅ |

## Ampliación de donantes

| bloque | objetivo | clave | locales | razon_inicial | anadidas | motivo |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 1562 | 1.7730 | 752 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 205 | 2.0450 | 148 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 1106 | 2.8389 | 1512 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=25-34 | 4137 | 2.7135 | 5264 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=35-44 | 6363 | 1.8266 | 3321 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=45-54 | 4361 | 2.2171 | 3700 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 1871 | 2.6164 | 2184 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 274 | 3.2625 | 477 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 1914 | 1.5512 | 556 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 98 | 4.4167 | 263 | None |
| CCAA:01 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 448 | 2.3418 | 424 | None |
| CCAA:01 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=10-14 | 2499 | 1.5646 | 779 | None |
| CCAA:01 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=15-19 | 2474 | 1.6241 | 896 | None |
| CCAA:01 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 329 | 1.6527 | 125 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=argentina | 995 | 1.8651 | 573 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=colombia | 1459 | 2.8245 | 2021 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=honduras | 417 | 1.7440 | 217 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=italia | 1666 | 1.5275 | 539 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=paraguay | 655 | 1.7610 | 347 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=peru | 322 | 3.9510 | 709 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=ucrania | 840 | 1.7629 | 442 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=venezuela | 782 | 2.3822 | 817 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | 97 | 1.5763 | 34 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | 143 | 2.2999 | 127 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | 334 | 2.1119 | 262 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | 474 | 1.5654 | 153 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | 171 | 2.0202 | 117 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 292 | 3.1089 | 465 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 707 | 2.8294 | 939 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | 650 | 2.6800 | 801 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 301 | 2.8180 | 419 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | 70 | 2.7750 | 97 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | 18 | 2.0891 | 13 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | 83 | 2.2301 | 73 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=20-34 | 266 | 1.5878 | 92 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | 183 | 1.6025 | 64 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | 40 | 2.1699 | 38 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | 7 | 2.3102 | 8 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | 254 | 1.6866 | 107 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=20-34 | 458 | 1.5437 | 139 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | 404 | 1.5510 | 123 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | 222 | 1.5857 | 71 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=50-64 | 1451 | 1.5741 | 471 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=65+ | 376 | 1.6473 | 134 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=00-19 | 112 | 1.5302 | 31 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | 316 | 2.1227 | 222 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | 343 | 1.5163 | 98 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | 120 | 1.7788 | 55 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 54 | 5.6104 | 198 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 109 | 4.2454 | 287 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | 161 | 3.0706 | 276 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 73 | 4.2210 | 187 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 24 | 3.3542 | 44 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 128 | 1.8491 | 65 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 221 | 2.2106 | 194 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=20-34 | 279 | 1.5249 | 83 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | 392 | 1.7681 | 198 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 103 | 2.6772 | 118 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | 181 | 2.6222 | 211 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | 354 | 2.5480 | 384 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | 336 | 2.1636 | 288 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=50-64 | 162 | 2.2762 | 150 | None |
| CCAA:01 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | 92 | 2.1010 | 70 | None |
| CCAA:01 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=hombre | 156 | 4.2344 | 133 | None |
| CCAA:01 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=mujer | 228 | 3.7476 | 125 | None |
| CCAA:02 | nacionalidad_top | nacionalidad_top=argentina | 93 | 1.9503 | 65 | None |
| CCAA:02 | nacionalidad_top | nacionalidad_top=colombia | 446 | 2.6595 | 547 | None |
| CCAA:02 | nacionalidad_top | nacionalidad_top=italia | 148 | 1.7720 | 65 | None |
| CCAA:02 | nacionalidad_top | nacionalidad_top=peru | 104 | 3.2158 | 158 | None |
| CCAA:02 | nacionalidad_top | nacionalidad_top=ucrania | 110 | 2.1797 | 89 | None |
| CCAA:02 | nacionalidad_top | nacionalidad_top=venezuela | 214 | 2.4088 | 209 | None |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 24 | 3.6771 | 10 | None |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 31 | 4.4712 | 27 | None |
| CCAA:02 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 6 | 4.7396 | 6 | None |
| CCAA:02 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=hombre | 56 | 3.6143 | 24 | None |
| CCAA:03 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 11 | 3.8003 | 6 | None |
| CCAA:03 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 4 | 3.4299 | 1 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=alemania | 29 | 2.1481 | 1 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=argentina | 60 | 2.3379 | 66 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=colombia | 221 | 3.0519 | 350 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=honduras | 35 | 1.8352 | 18 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=italia | 112 | 1.7406 | 52 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=otras_extranjeras | 1108 | 1.5308 | 248 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=paraguay | 153 | 1.5401 | 40 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=peru | 50 | 3.5617 | 78 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=ucrania | 42 | 5.4382 | 107 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=venezuela | 154 | 2.8241 | 194 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 8 | 6.5015 | 12 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | 20 | 3.8740 | 11 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 9 | 3.7148 | 5 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 4 | 2.8214 | 1 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 4 | 19.8492 | 1 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=35-49 | 16 | 5.7400 | 17 | None |
| CCAA:03 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 4 | 6.8324 | 1 | None |
| CCAA:03 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=hombre | 23 | 4.2668 | 18 | None |
| CCAA:03 | nacionalidad_top_sexo | nacionalidad_top=ucrania;sexo=hombre | 15 | 8.2163 | 25 | None |
| CCAA:03 | nacionalidad_top_sexo | nacionalidad_top=ucrania;sexo=mujer | 35 | 4.3964 | 25 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 195 | 2.6553 | 237 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=20-24 | 1569 | 1.7069 | 661 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | 664 | 1.7447 | 300 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 30 | 4.0265 | 72 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 332 | 2.8624 | 444 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=25-34 | 1407 | 2.4718 | 1506 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=35-44 | 2075 | 1.9162 | 1228 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=45-54 | 1574 | 2.0795 | 1160 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 742 | 2.1703 | 591 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 115 | 1.9344 | 71 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | 5 | 4.3403 | 14 | None |
| CCAA:04 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 44 | 2.1433 | 34 | None |
| CCAA:04 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 69 | 1.8201 | 35 | None |
| CCAA:04 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 34 | 1.5160 | 10 | None |
| CCAA:04 | nacionalidad_top | nacionalidad_top=colombia | 791 | 2.1225 | 644 | None |
| CCAA:04 | nacionalidad_top | nacionalidad_top=honduras | 36 | 1.7207 | 13 | None |
| CCAA:04 | nacionalidad_top | nacionalidad_top=paraguay | 223 | 1.8421 | 131 | None |
| CCAA:04 | nacionalidad_top | nacionalidad_top=peru | 142 | 2.4244 | 144 | None |
| CCAA:04 | nacionalidad_top | nacionalidad_top=ucrania | 112 | 1.6066 | 42 | None |
| CCAA:04 | nacionalidad_top | nacionalidad_top=venezuela | 195 | 1.6387 | 80 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | 55 | 1.7122 | 23 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=50-64 | 111 | 1.5453 | 30 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | 43 | 1.9992 | 31 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 145 | 2.4332 | 149 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 426 | 1.9190 | 279 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | 336 | 2.1588 | 282 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 173 | 2.2032 | 146 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | 29 | 2.7177 | 43 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | 21 | 1.6792 | 8 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=todas | 36 | 1.7207 | 12 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=50-64 | 208 | 1.6161 | 81 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=65+ | 57 | 1.7156 | 25 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=00-19 | 34 | 1.9421 | 21 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | 114 | 1.9242 | 85 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=35-49 | 110 | 1.6898 | 47 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | 37 | 1.7254 | 16 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=65+ | 3 | 4.1838 | 2 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 18 | 3.6435 | 33 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 43 | 3.0376 | 68 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | 71 | 1.8870 | 42 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 36 | 1.9722 | 24 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 9 | 2.8248 | 12 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 18 | 2.0163 | 11 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 24 | 1.9298 | 15 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | 30 | 1.9852 | 20 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 5 | 4.4893 | 14 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | 46 | 1.6673 | 18 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | 92 | 1.7435 | 47 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | 80 | 1.5896 | 27 | None |
| CCAA:04 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | 19 | 1.5405 | 5 | None |
| CCAA:05 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 37 | 4.9266 | 32 | None |
| CCAA:05 | nacionalidad_top | nacionalidad_top=colombia | 942 | 2.0886 | 653 | None |
| CCAA:05 | nacionalidad_top | nacionalidad_top=paraguay | 74 | 1.6380 | 24 | None |
| CCAA:05 | nacionalidad_top | nacionalidad_top=peru | 123 | 2.0149 | 72 | None |
| CCAA:05 | nacionalidad_top | nacionalidad_top=ucrania | 83 | 3.3428 | 104 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 14 | 3.5343 | 6 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 15 | 4.5170 | 12 | None |
| CCAA:05 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=50-64 | 17 | 3.6002 | 8 | None |
| CCAA:05 | nacionalidad_top_sexo | nacionalidad_top=ucrania;sexo=hombre | 37 | 3.8523 | 18 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 152 | 1.7986 | 76 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 61 | 2.3087 | 56 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | 328 | 1.8038 | 164 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 7 | 4.0737 | 17 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 51 | 3.8916 | 117 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=25-34 | 287 | 2.1934 | 235 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=35-44 | 359 | 2.0768 | 253 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=45-54 | 242 | 2.2576 | 224 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 105 | 2.4085 | 111 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 15 | 1.8653 | 9 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 59 | 1.7584 | 28 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 6 | 4.3255 | 15 | None |
| CCAA:06 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 32 | 2.1618 | 26 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=10-14 | 139 | 1.6489 | 54 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=15-19 | 162 | 1.6460 | 67 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=20-24 | 223 | 1.6235 | 81 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=50-54 | 210 | 1.6080 | 78 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=55-59 | 163 | 1.5942 | 53 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=65-69 | 66 | 1.9173 | 39 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=70-74 | 46 | 1.7856 | 24 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=75-79 | 30 | 1.7146 | 12 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=80-84 | 16 | 1.6150 | 7 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 10 | 1.6910 | 5 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 3 | 1.8881 | 2 | None |
| CCAA:06 | nacionalidad_top | nacionalidad_top=alemania | 31 | 1.5475 | 8 | None |
| CCAA:06 | nacionalidad_top | nacionalidad_top=colombia | 204 | 2.3384 | 220 | None |
| CCAA:06 | nacionalidad_top | nacionalidad_top=honduras | 19 | 0.9950 | 11 | None |
| CCAA:06 | nacionalidad_top | nacionalidad_top=peru | 145 | 2.1523 | 115 | None |
| CCAA:06 | nacionalidad_top | nacionalidad_top=ucrania | 48 | 2.1689 | 42 | None |
| CCAA:06 | nacionalidad_top | nacionalidad_top=venezuela | 84 | 2.0659 | 59 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=todas | 31 | 1.5475 | 10 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 45 | 2.7887 | 55 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 112 | 2.0697 | 73 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | 78 | 2.5288 | 98 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 44 | 2.4048 | 46 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | 15 | 1.8159 | 8 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=20-34 | 42 | 1.5995 | 16 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=50-64 | 14 | 2.0508 | 9 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ | 65 | 1.7531 | 28 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 36 | 2.5162 | 38 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 65 | 2.0409 | 51 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | 56 | 2.4563 | 60 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 35 | 2.0672 | 28 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 5 | 4.1204 | 14 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=todas | 48 | 2.1689 | 33 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | 15 | 2.7059 | 17 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | 37 | 2.2489 | 31 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | 33 | 1.6872 | 17 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=50-64 | 23 | 1.5468 | 7 | None |
| CCAA:06 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | 6 | 3.0991 | 11 | None |
| CCAA:06 | nacionalidad_top_sexo | nacionalidad_top=honduras;sexo=hombre | 2 | 5.0070 | 3 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=argentina | 111 | 2.3310 | 114 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=colombia | 587 | 3.0045 | 910 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=ecuador | 156 | 1.5292 | 49 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=honduras | 186 | 1.7884 | 106 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=italia | 177 | 1.5429 | 59 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=paraguay | 100 | 2.2400 | 78 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=peru | 187 | 3.8136 | 410 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=ucrania | 81 | 2.4148 | 99 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=venezuela | 271 | 3.3548 | 535 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | 5 | 3.6604 | 3 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | 4 | 3.7549 | 1 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | 4 | 4.8767 | 1 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 44 | 5.0595 | 47 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 43 | 3.8667 | 24 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 10 | 3.7457 | 5 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 6 | 5.8690 | 8 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | 71 | 3.7543 | 42 | None |
| CCAA:07 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | 129 | 3.5244 | 56 | None |
| CCAA:07 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=hombre | 106 | 4.0322 | 81 | None |
| CCAA:07 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=mujer | 133 | 3.6485 | 79 | None |
| CCAA:07 | nacionalidad_top_sexo | nacionalidad_top=venezuela;sexo=hombre | 148 | 3.9853 | 101 | None |
| CCAA:08 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 35 | 3.8319 | 19 | None |
| CCAA:08 | nacionalidad_top | nacionalidad_top=argentina | 144 | 1.5455 | 43 | None |
| CCAA:08 | nacionalidad_top | nacionalidad_top=colombia | 714 | 2.5418 | 873 | None |
| CCAA:08 | nacionalidad_top | nacionalidad_top=honduras | 129 | 2.1878 | 104 | None |
| CCAA:08 | nacionalidad_top | nacionalidad_top=paraguay | 248 | 1.5763 | 78 | None |
| CCAA:08 | nacionalidad_top | nacionalidad_top=peru | 283 | 2.8099 | 421 | None |
| CCAA:08 | nacionalidad_top | nacionalidad_top=ucrania | 172 | 1.5248 | 50 | None |
| CCAA:08 | nacionalidad_top | nacionalidad_top=venezuela | 305 | 2.5318 | 373 | None |
| CCAA:08 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 62 | 3.8319 | 33 | None |
| CCAA:09 | nacionalidad_top | nacionalidad_top=argentina | 1793 | 1.6587 | 651 | None |
| CCAA:09 | nacionalidad_top | nacionalidad_top=colombia | 2949 | 2.2540 | 2418 | None |
| CCAA:09 | nacionalidad_top | nacionalidad_top=peru | 1662 | 2.1323 | 1289 | None |
| CCAA:09 | nacionalidad_top | nacionalidad_top=ucrania | 1111 | 1.7980 | 544 | None |
| CCAA:09 | nacionalidad_top | nacionalidad_top=venezuela | 1753 | 1.6124 | 577 | None |
| CCAA:10 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 247 | 3.9260 | 143 | None |
| CCAA:10 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 103 | 5.5185 | 123 | None |
| CCAA:10 | nacionalidad_top | nacionalidad_top=argentina | 890 | 2.2186 | 766 | None |
| CCAA:10 | nacionalidad_top | nacionalidad_top=colombia | 2506 | 2.9746 | 3988 | None |
| CCAA:10 | nacionalidad_top | nacionalidad_top=honduras | 602 | 1.5919 | 187 | None |
| CCAA:10 | nacionalidad_top | nacionalidad_top=italia | 2025 | 1.6895 | 859 | None |
| CCAA:10 | nacionalidad_top | nacionalidad_top=paraguay | 271 | 1.8623 | 126 | None |
| CCAA:10 | nacionalidad_top | nacionalidad_top=peru | 300 | 3.1463 | 451 | None |
| CCAA:10 | nacionalidad_top | nacionalidad_top=ucrania | 1045 | 2.9887 | 1569 | None |
| CCAA:10 | nacionalidad_top | nacionalidad_top=venezuela | 1140 | 2.4354 | 1180 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 532 | 3.5074 | 223 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 46 | 4.7211 | 39 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 52 | 3.8889 | 27 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 323 | 3.9135 | 177 | None |
| CCAA:10 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 99 | 4.1809 | 68 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=NP;nacionalidad_esp_ext=extranjera;edad_tramo_epa=00-15 | 340 | 1.5004 | 89 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 165 | 1.5285 | 46 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 133 | 2.6962 | 164 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 77 | 2.3738 | 79 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=25-34 | 223 | 2.8024 | 298 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=35-44 | 290 | 2.3453 | 267 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=45-54 | 221 | 2.3478 | 213 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 96 | 2.6995 | 118 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 7 | 4.0999 | 16 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | 7 | 3.1837 | 12 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 12 | 2.7439 | 15 | None |
| CCAA:11 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 28 | 2.0183 | 22 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=05-09 | 138 | 1.6184 | 49 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=10-14 | 135 | 1.7529 | 67 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=15-19 | 173 | 1.5142 | 51 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=25-29 | 269 | 1.6483 | 104 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=45-49 | 265 | 1.6392 | 104 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=55-59 | 163 | 1.5621 | 50 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=65-69 | 82 | 1.6136 | 29 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=70-74 | 45 | 1.9453 | 30 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=75-79 | 27 | 1.6599 | 10 | None |
| CCAA:11 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=80-84 | 14 | 1.5864 | 4 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=alemania | 15 | 1.7675 | 15 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=colombia | 107 | 3.0137 | 173 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=ecuador | 17 | 1.8137 | 13 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=honduras | 57 | 1.6655 | 28 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=paraguay | 27 | 1.7634 | 3 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=peru | 36 | 3.7553 | 68 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=ucrania | 15 | 3.0189 | 15 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=venezuela | 50 | 2.0707 | 52 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=todas | 15 | 1.7675 | 8 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 22 | 3.1030 | 35 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 41 | 3.9237 | 90 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | 59 | 2.1813 | 49 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 19 | 3.6215 | 39 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | 6 | 2.7640 | 6 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=todas | 17 | 1.8137 | 6 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=todas | 57 | 1.6655 | 19 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=65+ | 32 | 1.7366 | 15 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=00-19 | 88 | 1.6869 | 43 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=20-34 | 240 | 1.5365 | 80 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ | 64 | 1.5293 | 16 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=todas | 27 | 1.7634 | 14 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=todas | 36 | 3.7553 | 61 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 14 | 1.5341 | 5 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=todas | 15 | 3.0189 | 18 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | 17 | 1.9311 | 10 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | 23 | 2.4702 | 26 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | 23 | 2.0035 | 18 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=50-64 | 13 | 1.7694 | 8 | None |
| CCAA:11 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | 6 | 1.9327 | 5 | None |
| CCAA:11 | nacionalidad_top_sexo | nacionalidad_top=colombia;sexo=hombre | 48 | 3.6308 | 22 | None |
| CCAA:11 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=hombre | 16 | 4.5943 | 12 | None |
| CCAA:12 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 188 | 3.9202 | 107 | None |
| CCAA:12 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=65+ | 4 | 3.5585 | 1 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=argentina | 189 | 2.1464 | 133 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=colombia | 504 | 3.0576 | 733 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=ecuador | 47 | 1.6262 | 17 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=honduras | 49 | 1.8429 | 27 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=italia | 332 | 1.5410 | 97 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=paraguay | 97 | 1.6613 | 41 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=peru | 207 | 3.7108 | 433 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=ucrania | 40 | 3.5008 | 86 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=venezuela | 768 | 2.3582 | 687 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | 2 | 3.6488 | 3 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 94 | 4.1935 | 60 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 47 | 4.6418 | 45 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 78 | 3.7693 | 47 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 14 | 4.4851 | 9 | None |
| CCAA:12 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 2 | 11.0122 | 3 | None |
| CCAA:12 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=hombre | 120 | 3.8204 | 80 | None |
| CCAA:12 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=mujer | 139 | 3.6166 | 77 | None |
| CCAA:12 | nacionalidad_top_sexo | nacionalidad_top=ucrania;sexo=mujer | 34 | 3.5832 | 20 | None |
| CCAA:13 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 96 | 3.7782 | 49 | None |
| CCAA:13 | nacionalidad_top | nacionalidad_top=argentina | 846 | 1.7598 | 392 | None |
| CCAA:13 | nacionalidad_top | nacionalidad_top=colombia | 3680 | 2.1594 | 2986 | None |
| CCAA:13 | nacionalidad_top | nacionalidad_top=peru | 2462 | 2.3307 | 2383 | None |
| CCAA:13 | nacionalidad_top | nacionalidad_top=venezuela | 3391 | 1.9572 | 2133 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 337 | 1.8987 | 195 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | 794 | 1.7047 | 337 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 422 | 2.1938 | 353 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=25-34 | 1325 | 2.2445 | 1157 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=45-54 | 1693 | 1.6554 | 667 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 672 | 2.2251 | 578 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 63 | 4.0051 | 143 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 326 | 1.7032 | 138 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 33 | 3.7911 | 70 | None |
| CCAA:14 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 122 | 1.9390 | 76 | None |
| CCAA:14 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=75-79 | 263 | 1.5299 | 75 | None |
| CCAA:14 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=80-84 | 101 | 2.2563 | 85 | None |
| CCAA:14 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 49 | 1.5441 | 15 | None |
| CCAA:14 | nacionalidad_top | nacionalidad_top=argentina | 92 | 1.6454 | 39 | None |
| CCAA:14 | nacionalidad_top | nacionalidad_top=colombia | 464 | 2.3593 | 451 | None |
| CCAA:14 | nacionalidad_top | nacionalidad_top=honduras | 157 | 1.8275 | 68 | None |
| CCAA:14 | nacionalidad_top | nacionalidad_top=peru | 60 | 2.8325 | 88 | None |
| CCAA:14 | nacionalidad_top | nacionalidad_top=venezuela | 138 | 2.3993 | 155 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=00-19 | 7 | 1.7768 | 6 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=65+ | 41 | 1.6685 | 18 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=00-19 | 16 | 2.0037 | 8 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=20-34 | 34 | 1.6335 | 17 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=35-49 | 33 | 1.6578 | 14 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=argentina;edad_nacionalidad=65+ | 5 | 3.8028 | 9 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=50-64 | 42 | 1.5143 | 15 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 84 | 3.2800 | 139 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 218 | 2.2996 | 225 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | 212 | 2.2098 | 189 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 121 | 2.1083 | 92 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | 32 | 2.0111 | 21 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | 44 | 1.8039 | 21 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=65+ | 40 | 1.6157 | 14 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=00-19 | 24 | 3.5464 | 39 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=35-49 | 64 | 1.5541 | 21 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=50-64 | 12 | 2.8962 | 16 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=00-19 | 18 | 1.5332 | 5 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=35-49 | 59 | 1.5139 | 16 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=50-64 | 38 | 1.6303 | 15 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=65+ | 21 | 1.7238 | 9 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=65+ | 163 | 1.6897 | 65 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ | 253 | 1.5561 | 79 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=20-34 | 67 | 1.8611 | 42 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=50-64 | 19 | 1.8823 | 11 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 12 | 3.7354 | 22 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 24 | 2.8652 | 31 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | 25 | 2.5320 | 32 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 13 | 3.0465 | 21 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 6 | 1.6666 | 3 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 21 | 1.6237 | 9 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 82 | 1.7760 | 34 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 46 | 2.2037 | 41 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=00-19 | 40 | 2.7215 | 43 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | 70 | 2.4708 | 79 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=35-49 | 59 | 2.1965 | 55 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=50-64 | 29 | 2.1832 | 27 | None |
| CCAA:14 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | 14 | 2.3535 | 16 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 209 | 1.5888 | 70 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 198 | 1.9336 | 124 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 148 | 2.5525 | 162 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=25-34 | 555 | 2.0225 | 368 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=35-44 | 781 | 1.6466 | 281 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=45-54 | 534 | 1.8520 | 302 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 199 | 2.0325 | 142 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 18 | 2.3917 | 18 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 96 | 1.6983 | 41 | None |
| CCAA:15 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 18 | 2.3844 | 18 | None |
| CCAA:15 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=15-19 | 297 | 1.6378 | 118 | None |
| CCAA:15 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=65-69 | 97 | 2.0657 | 71 | None |
| CCAA:15 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=70-74 | 58 | 2.0925 | 46 | None |
| CCAA:15 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=75-79 | 40 | 1.8481 | 22 | None |
| CCAA:15 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=80-84 | 22 | 1.5771 | 8 | None |
| CCAA:15 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 6 | 2.3086 | 8 | None |
| CCAA:15 | nacionalidad_top | nacionalidad_top=alemania | 27 | 1.0322 | 3 | None |
| CCAA:15 | nacionalidad_top | nacionalidad_top=colombia | 294 | 2.1133 | 246 | None |
| CCAA:15 | nacionalidad_top | nacionalidad_top=honduras | 74 | 1.5813 | 30 | None |
| CCAA:15 | nacionalidad_top | nacionalidad_top=paraguay | 11 | 3.4220 | 19 | None |
| CCAA:15 | nacionalidad_top | nacionalidad_top=peru | 129 | 1.9567 | 96 | None |
| CCAA:15 | nacionalidad_top | nacionalidad_top=venezuela | 81 | 1.7280 | 44 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=50-64 | 15 | 2.0964 | 11 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=65+ | 2 | 2.6115 | 3 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 61 | 2.5615 | 71 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 160 | 1.8825 | 92 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | 124 | 2.1513 | 100 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 68 | 1.9682 | 47 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | 14 | 2.9685 | 22 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=50-64 | 38 | 1.5272 | 11 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=ecuador;edad_nacionalidad=65+ | 7 | 3.1637 | 12 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=todas | 74 | 1.5813 | 19 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ | 88 | 1.7653 | 42 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=todas | 11 | 3.4220 | 14 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=00-19 | 33 | 2.0654 | 27 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=20-34 | 62 | 1.9663 | 43 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=35-49 | 53 | 1.9549 | 34 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=50-64 | 33 | 1.7791 | 17 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 12 | 1.9660 | 8 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 19 | 1.7962 | 9 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=00-19 | 22 | 1.7618 | 13 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 8 | 2.6002 | 11 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=20-34 | 32 | 2.2667 | 28 | None |
| CCAA:15 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=65+ | 6 | 3.6824 | 14 | None |
| CCAA:15 | nacionalidad_top_sexo | nacionalidad_top=paraguay;sexo=hombre | 1 | 14.2829 | 4 | None |
| CCAA:16 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 4 | 4.1474 | 1 | None |
| CCAA:16 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | 4 | 4.5891 | 1 | None |
| CCAA:16 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 8 | 4.4910 | 7 | None |
| CCAA:16 | nacionalidad_top | nacionalidad_top=colombia | 822 | 2.2300 | 693 | None |
| CCAA:16 | nacionalidad_top | nacionalidad_top=peru | 173 | 2.7532 | 224 | None |
| CCAA:16 | nacionalidad_top | nacionalidad_top=ucrania | 120 | 2.1173 | 93 | None |
| CCAA:16 | nacionalidad_top | nacionalidad_top=venezuela | 317 | 2.0345 | 217 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=65+ | 2 | 7.0517 | 3 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=65+ | 7 | 5.9836 | 10 | None |
| CCAA:16 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=65+ | 11 | 3.7788 | 5 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 103 | 1.9969 | 67 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 49 | 2.1446 | 39 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 15 | 1.7936 | 9 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 95 | 1.9400 | 57 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=25-34 | 300 | 1.9270 | 186 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=35-44 | 446 | 1.5949 | 150 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=45-54 | 350 | 1.5937 | 119 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 135 | 2.0061 | 90 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | 11 | 2.4439 | 12 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=16-19 | 28 | 2.5887 | 33 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=20-24 | 81 | 1.5728 | 27 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | 6 | 3.2313 | 11 | None |
| CCAA:17 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | 27 | 1.5495 | 8 | None |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | 3 | 4.4321 | 2 | None |
| CCAA:17 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=16-19 | 8 | 4.5592 | 8 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=10-14 | 159 | 1.6768 | 63 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=15-19 | 159 | 1.6108 | 60 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=55-59 | 175 | 1.5550 | 52 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=65-69 | 61 | 1.9004 | 37 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=70-74 | 29 | 2.4138 | 29 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=75-79 | 16 | 1.8905 | 10 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=80-84 | 10 | 1.6753 | 5 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 8.1332 | 4 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.9987 | 3 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=alemania | 5 | 2.4840 | 25 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=argentina | 25 | 1.4492 | 5 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=china | 15 | 1.6549 | 15 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=colombia | 177 | 2.1157 | 173 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=francia | 16 | 1.6111 | 14 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=honduras | 26 | 1.9204 | 4 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=italia | 35 | 1.5531 | 12 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=paraguay | 4 | 4.3333 | 26 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=peru | 29 | 1.8440 | 1 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=reino_unido | 19 | 1.0184 | 11 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=ucrania | 14 | 2.4412 | 16 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=venezuela | 42 | 2.3450 | 37 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=alemania;edad_nacionalidad=todas | 5 | 2.4840 | 5 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=todas | 15 | 1.6549 | 4 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=00-19 | 46 | 2.2586 | 41 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=20-34 | 90 | 2.0151 | 66 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=35-49 | 87 | 2.0012 | 64 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=50-64 | 34 | 2.4138 | 35 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=65+ | 11 | 2.3067 | 11 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=francia;edad_nacionalidad=todas | 16 | 1.6111 | 6 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=honduras;edad_nacionalidad=todas | 26 | 1.9204 | 12 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=italia;edad_nacionalidad=todas | 35 | 1.5531 | 11 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=20-34 | 141 | 1.5048 | 39 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=marruecos;edad_nacionalidad=65+ | 17 | 1.5382 | 6 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=otras_extranjeras;edad_nacionalidad=65+ | 41 | 1.6673 | 17 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=paraguay;edad_nacionalidad=todas | 4 | 4.3333 | 1 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=peru;edad_nacionalidad=todas | 29 | 1.8440 | 19 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=rumania;edad_nacionalidad=65+ | 24 | 2.2476 | 25 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=ucrania;edad_nacionalidad=todas | 14 | 2.4412 | 16 | None |
| CCAA:17 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=todas | 42 | 2.3450 | 36 | None |
| CCAA:17 | nacionalidad_top_sexo | nacionalidad_top=honduras;sexo=hombre | 5 | 3.6159 | 3 | None |
| CCAA:17 | nacionalidad_top_sexo | nacionalidad_top=paraguay;sexo=todas | 4 | 4.3333 | 1 | None |
| CCAA:18 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=55-64 | 11 | 4.1869 | 7 | None |
| CCAA:18 | estudios_edad | estudios_3=superior;edad_estudios=90+ | 3 | 2.0488 | 2 | None |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 1.9579 | 4 | None |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.3251 | 3 | None |
| CCAA:18 | nacionalidad_top | nacionalidad_top=china | 1 | 2.3948 | 29 | None |
| CCAA:18 | nacionalidad_top_edad | nacionalidad_top=china;edad_nacionalidad=todas | 1 | 2.3948 | 4 | None |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=china;sexo=todas | 1 | 2.3948 | 4 | None |
| CCAA:18 | actividad_tramo | relacion_actividad=ocupado;sexo=hombre;edad_tramo_epa=16-19 | 10 | 1.0337 | 1 | reparacion 1 |
| CCAA:18 | actividad_tramo | relacion_actividad=ocupado;sexo=mujer;edad_tramo_epa=16-19 | 5 | 0.9539 | 1 | reparacion 1 |
| CCAA:19 | estudios_edad | estudios_3=secundaria_2a_etapa;edad_estudios=90+ | 2 | 1.3648 | 3 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=america_latina | 18 | 4.7103 | 15 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.6564 | 1 | None |
| CCAA:19 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.8079 | 3 | None |
| CCAA:19 | nacionalidad_top | nacionalidad_top=alemania | 8 | 0.7882 | 22 | None |
| CCAA:19 | nacionalidad_top | nacionalidad_top=colombia | 1 | 17.6844 | 29 | None |
| CCAA:19 | nacionalidad_top | nacionalidad_top=francia | 6 | 1.1177 | 24 | None |
| CCAA:19 | nacionalidad_top | nacionalidad_top=venezuela | 5 | 4.2542 | 25 | None |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=colombia;edad_nacionalidad=todas | 1 | 17.6844 | 4 | None |
| CCAA:19 | nacionalidad_top_edad | nacionalidad_top=venezuela;edad_nacionalidad=todas | 5 | 4.2542 | 5 | None |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=colombia;sexo=hombre | 0 | None | 5 | None |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=colombia;sexo=mujer | 1 | 6.0078 | 4 | None |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=venezuela;sexo=hombre | 3 | 4.9342 | 2 | None |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=venezuela;sexo=mujer | 3 | 3.5767 | 2 | None |

## Nacionalidades fusionadas con «otras extranjeras»

| bloque | objetivo | clave | fusionada_en |
| --- | --- | --- | --- |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:06 | sin_estudios_edad | sin_estudios=si;edad_estudios=40-49 | sin_estudios=no;edad_estudios=40-49 |
| CCAA:06 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | estado_civil=soltero;edad_estado_civil=16-34 |
| CCAA:06 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:06 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=55-64 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=55-64 |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:17 | nacionalidad_top_sexo | nacionalidad_top=alemania;sexo=hombre | nacionalidad_top=alemania;sexo=todas |
| CCAA:17 | nacionalidad_top_sexo | nacionalidad_top=alemania;sexo=mujer | nacionalidad_top=alemania;sexo=todas |
| CCAA:17 | nacionalidad_top_sexo | nacionalidad_top=paraguay;sexo=hombre | nacionalidad_top=paraguay;sexo=todas |
| CCAA:17 | nacionalidad_top_sexo | nacionalidad_top=paraguay;sexo=mujer | nacionalidad_top=paraguay;sexo=todas |
| CCAA:17 | nacionalidad_top_sexo | nacionalidad_top=reino_unido;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
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
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=45-54 |
| CCAA:18 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:18 | actividad_tramo | relacion_actividad=parado;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=parado;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
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
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=china;sexo=hombre | nacionalidad_top=china;sexo=todas |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=china;sexo=mujer | nacionalidad_top=china;sexo=todas |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=alemania;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=alemania;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=argentina;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=argentina;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=colombia;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=colombia;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=ecuador;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=ecuador;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=francia;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=francia;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=honduras;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=honduras;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=italia;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=italia;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=paraguay;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=paraguay;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=reino_unido;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=reino_unido;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=rumania;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=rumania;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=ucrania;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=ucrania;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=venezuela;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:18 | nacionalidad_top_sexo | nacionalidad_top=venezuela;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:18 | estado_civil_edad | estado_civil=NC;edad_estado_civil=35-54 | estado_civil=casado;edad_estado_civil=35-54 |
| CCAA:18 | estado_civil_edad | estado_civil=NC;edad_estado_civil=75+ | estado_civil=casado;edad_estado_civil=75+ |
| CCAA:18 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | estado_civil=soltero;edad_estado_civil=16-34 |
| CCAA:18 | actividad_nacionalidad | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 |
| CCAA:18 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 |
| CCAA:18 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:18 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:18 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 |
| CCAA:18 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=20-24 |
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
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=hombre;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;sexo=mujer;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=16-19 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=20-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=35-44 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=hombre;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;sexo=hombre;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=16-19 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=16-19 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;sexo=mujer;edad_tramo_epa=20-24 | relacion_actividad=otra_inactividad;sexo=mujer;edad_tramo_epa=20-24 |
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
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=alemania;sexo=hombre | nacionalidad_top=alemania;sexo=todas |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=alemania;sexo=mujer | nacionalidad_top=alemania;sexo=todas |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=francia;sexo=hombre | nacionalidad_top=francia;sexo=todas |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=francia;sexo=mujer | nacionalidad_top=francia;sexo=todas |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=argentina;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=argentina;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=china;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=china;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=ecuador;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=ecuador;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=honduras;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=honduras;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=italia;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=italia;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=paraguay;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=paraguay;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=peru;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=reino_unido;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=reino_unido;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=rumania;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=rumania;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=ucrania;sexo=hombre | nacionalidad_top=otras_extranjeras;sexo=hombre |
| CCAA:19 | nacionalidad_top_sexo | nacionalidad_top=ucrania;sexo=mujer | nacionalidad_top=otras_extranjeras;sexo=mujer |
| CCAA:19 | estado_civil_edad | estado_civil=viudo;edad_estado_civil=16-34 | estado_civil=soltero;edad_estado_civil=16-34 |
| CCAA:19 | actividad_nacionalidad | actividad_3=ocupado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 |
| CCAA:19 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=espanola;edad_tramo_epa=65+ |
| CCAA:19 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=16-19 |
| CCAA:19 | actividad_nacionalidad | actividad_3=parado;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ | actividad_3=inactivo;nacionalidad_esp_ext=extranjera;edad_tramo_epa=65+ |
| CCAA:19 | nacionalidad | nacionalidad_grupo=asia | nacionalidad_grupo=espanola |
| CCAA:19 | nacionalidad | nacionalidad_grupo=otros | nacionalidad_grupo=espanola |

## V de Cramér (2026-01-01_ES_1000000_s1)

| objetivo | par | v_oficial | v_sintetica | dif | ok |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | relacion_actividad × edad_actividad | 0.6114 | 0.6135 | 0.0022 | ✅ |
| actividad_sexo | relacion_actividad × sexo | 0.2209 | 0.2206 | 0.0003 | ✅ |
| adultos_nacionalidad | nacionalidad_esp_ext × es_adulto | 0.0028 | 0.0056 | 0.0029 | ✅ |
| estudios_sexo_edad | estudios_3 × sexo | 0.0391 | 0.0347 | 0.0044 | ✅ |
| estudios_sexo_edad | estudios_3 × edad_estudios | 0.6228 | 0.6228 | 0.0001 | ✅ |
| estudios_sexo_edad | sexo × edad_estudios | 0.0713 | 0.0712 | 0.0002 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × sexo | 0.0420 | 0.0427 | 0.0007 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × edad_nacionalidad | 0.1056 | 0.1055 | 0.0001 | ✅ |
| nacionalidad_top_sexo_edad | sexo × edad_nacionalidad | 0.0575 | 0.0572 | 0.0003 | ✅ |
| tipo_hogar_edad4_ref | tipo_hogar × edad_4 | 0.1814 | 0.1795 | 0.0019 | ✅ |

## Minorías, primera pasada (2026-01-01_ES_1000000_s1)

| grupo | unidad | esperado | observado | ratio | ok_representacion | donantes_distintos | top5 | ok_concentracion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mayores_85 | persona | 32796.4226 | 32824.0000 | 1.0008 | ✅ | 28983 | 0.0027 | ✅ |
| municipios_menos_2000 | persona | 54717.5225 | 56309.0000 | 1.0291 | ✅ | 24999 | 0.0020 | ✅ |
| parados | persona | 50863.1504 | 50503.0000 | 0.9929 | ✅ | 42445 | 0.0011 | ✅ |
| monoparentales | hogar | 46943.0386 | 46954.0000 | 1.0002 | ✅ | 45810 | 0.0009 | ✅ |
| mayores_solos | persona | 49231.1047 | 48694.0000 | 0.9891 | ✅ | 48352 | 0.0003 | ✅ |
| ceuta_melilla | persona | 3449.8398 | 3441.0000 | 0.9974 | ✅ | 1090 | 0.0183 | ✅ |
| nacionalidad_alemania | persona | 2750.3786 | 2745.0000 | 0.9980 | ✅ | 1864 | 0.0175 | ✅ |
| nacionalidad_argentina | persona | 3114.9952 | 3114.0000 | 0.9997 | ✅ | 1792 | 0.0250 | ✅ |
| nacionalidad_china | persona | 4968.3772 | 4966.0000 | 0.9995 | ✅ | 1542 | 0.0117 | ✅ |
| nacionalidad_colombia | persona | 14242.6697 | 14199.0000 | 0.9969 | ✅ | 5831 | 0.0095 | ✅ |
| nacionalidad_ecuador | persona | 2768.2630 | 2776.0000 | 1.0028 | ✅ | 1730 | 0.0173 | ✅ |
| nacionalidad_francia | persona | 2656.8949 | 2658.0000 | 1.0004 | ✅ | 1816 | 0.0162 | ✅ |
| nacionalidad_honduras | persona | 3667.6011 | 3662.0000 | 0.9985 | ✅ | 1634 | 0.0180 | ✅ |
| nacionalidad_italia | persona | 7187.6209 | 7178.0000 | 0.9987 | ✅ | 4379 | 0.0092 | ✅ |
| nacionalidad_marruecos | persona | 20302.3975 | 20250.0000 | 0.9974 | ✅ | 8387 | 0.0064 | ✅ |
| nacionalidad_paraguay | persona | 2555.0591 | 2542.0000 | 0.9949 | ✅ | 1257 | 0.0319 | ✅ |
| nacionalidad_peru | persona | 5439.2177 | 5439.0000 | 1.0000 | ✅ | 2266 | 0.0283 | ✅ |
| nacionalidad_reino_unido | persona | 5616.2176 | 5625.0000 | 1.0016 | ✅ | 3357 | 0.0116 | ✅ |
| nacionalidad_rumania | persona | 12832.4525 | 12846.0000 | 1.0011 | ✅ | 5369 | 0.0056 | ✅ |
| nacionalidad_ucrania | persona | 4259.7074 | 4261.0000 | 1.0003 | ✅ | 1599 | 0.0225 | ✅ |
| nacionalidad_venezuela | persona | 7938.2632 | 7941.0000 | 1.0003 | ✅ | 3437 | 0.0120 | ✅ |

## Reglas blandas (media de 5 semillas; nº de semillas dentro)

| regla | N | frecuencia_donantes | exceso_relativo | ok_estricto | ok |
| --- | --- | --- | --- | --- | --- |
| casado_menor_20 | 10000 | 0.000057 | -0.647528 | 4 | 5 |
| casado_menor_20 | 50000 | 0.000057 | 0.055998 | 3 | 5 |
| casado_menor_20 | 100000 | 0.000057 | 0.161459 | 2 | 5 |
| casado_menor_20 | 500000 | 0.000057 | -0.008024 | 5 | 5 |
| casado_menor_20 | 1000000 | 0.000057 | -0.004775 | 4 | 5 |
| estudiante_50_o_mas | 10000 | 0.000574 | -0.581029 | 5 | 5 |
| estudiante_50_o_mas | 50000 | 0.000574 | -0.114868 | 5 | 5 |
| estudiante_50_o_mas | 100000 | 0.000574 | 0.111623 | 3 | 5 |
| estudiante_50_o_mas | 500000 | 0.000574 | 0.135313 | 0 | 5 |
| estudiante_50_o_mas | 1000000 | 0.000574 | 0.128744 | 0 | 5 |
| hogar_8_o_mas | 10000 | 0.015992 | -0.244804 | 5 | 5 |
| hogar_8_o_mas | 50000 | 0.015992 | -0.048668 | 5 | 5 |
| hogar_8_o_mas | 100000 | 0.015992 | -0.110633 | 5 | 5 |
| hogar_8_o_mas | 500000 | 0.015992 | -0.036544 | 5 | 5 |
| hogar_8_o_mas | 1000000 | 0.015992 | 0.004357 | 5 | 5 |
| incapacidad_menor_25 | 10000 | 0.000077 | -0.740254 | 4 | 5 |
| incapacidad_menor_25 | 50000 | 0.000077 | -0.948158 | 5 | 5 |
| incapacidad_menor_25 | 100000 | 0.000077 | -0.352187 | 5 | 5 |
| incapacidad_menor_25 | 500000 | 0.000077 | -0.078086 | 5 | 5 |
| incapacidad_menor_25 | 1000000 | 0.000077 | -0.047262 | 5 | 5 |
| jubilado_menor_50 | 10000 | 0.000009 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 50000 | 0.000009 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 100000 | 0.000009 | -1.000000 | 5 | 5 |
| jubilado_menor_50 | 500000 | 0.000009 | -0.641746 | 5 | 5 |
| jubilado_menor_50 | 1000000 | 0.000009 | -0.328464 | 5 | 5 |
| ocupado_75_o_mas | 10000 | 0.001510 | 0.102367 | 2 | 5 |
| ocupado_75_o_mas | 50000 | 0.001510 | 0.057595 | 3 | 5 |
| ocupado_75_o_mas | 100000 | 0.001510 | -0.028548 | 5 | 5 |
| ocupado_75_o_mas | 500000 | 0.001510 | -0.004786 | 5 | 5 |
| ocupado_75_o_mas | 1000000 | 0.001510 | -0.012069 | 5 | 5 |
| superior_20_21 | 10000 | 0.003514 | -0.137880 | 5 | 5 |
| superior_20_21 | 50000 | 0.003514 | -0.036023 | 5 | 5 |
| superior_20_21 | 100000 | 0.003514 | 0.016385 | 5 | 5 |
| superior_20_21 | 500000 | 0.003514 | 0.007894 | 5 | 5 |
| superior_20_21 | 1000000 | 0.003514 | -0.010418 | 5 | 5 |
| viudo_menor_30 | 10000 | 0.000064 | -0.373204 | 4 | 5 |
| viudo_menor_30 | 50000 | 0.000064 | 0.063021 | 2 | 5 |
| viudo_menor_30 | 100000 | 0.000064 | -0.030749 | 4 | 5 |
| viudo_menor_30 | 500000 | 0.000064 | -0.087631 | 5 | 5 |
| viudo_menor_30 | 1000000 | 0.000064 | 0.018331 | 4 | 5 |

## G4.7 · Sobremuestreo (edad>=85:10000, 2026-01-01_ES_100000_s1_sm7d9288)

Miembros del grupo: 9907 (mínimo pedido 10000); α = 0.8691, β = 3.0490; suma de pesos 100192.

| objetivo | tvd | n_efectivo | umbral | ok |
| --- | --- | --- | --- | --- |
| actividad_nacionalidad | 0.0035 | 90900.9648 | 0.0119 | ✅ |
| actividad_tramo | 0.0092 | 90900.9648 | 0.0141 | ✅ |
| edad5_sexo | 0.0025 | 90900.9648 | 0.0132 | ✅ |
| edad5_sexo_colectivos | 0.0388 | 812.6729 | 0.1205 | ✅ |
| edad5_sexo_familiares | 0.0025 | 90104.2457 | 0.0134 | ✅ |
| estado_civil_edad | 0.0016 | 90900.9648 | 0.0100 | ✅ |
| estudios_edad | 0.0029 | 90900.9648 | 0.0122 | ✅ |
| nacimiento_nacionalidad | 0.0007 | 90900.9648 | 0.0050 | ✅ |
| nacionalidad | 0.0007 | 90900.9648 | 0.0055 | ✅ |
| nacionalidad_edad | 0.0025 | 90900.9648 | 0.0123 | ✅ |
| nacionalidad_top | 0.0005 | 90900.9648 | 0.0058 | ✅ |
| nacionalidad_top_edad | 0.0019 | 90900.9648 | 0.0117 | ✅ |
| nacionalidad_top_sexo | 0.0009 | 90900.9648 | 0.0088 | ✅ |
| sin_estudios_edad | 0.0015 | 90900.9648 | 0.0098 | ✅ |
| tamano_hogar | 0.0012 | 36513.4370 | 0.0095 | ✅ |
| tipo_hogar | 0.0024 | 36513.4370 | 0.0124 | ✅ |
| urbanizacion | 0.0006 | 90900.9648 | 0.0061 | ✅ |

## V-DONANTES (2026-01-01_ES_1000000_s1)

| territorio | personas | hogares_donantes | kish | proporcion_local | ok | confianza_reducida |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 176470 | 70162 | 53839.743 | 0.911 | ✅ | ❌ |
| CCAA:02 | 27869 | 11692 | 8825.621 | 0.970 | ✅ | ❌ |
| CCAA:03 | 20605 | 9327 | 7044.985 | 0.956 | ✅ | ❌ |
| CCAA:04 | 25393 | 9550 | 7069.682 | 0.812 | ✅ | ❌ |
| CCAA:05 | 45911 | 17629 | 12914.376 | 0.983 | ✅ | ❌ |
| CCAA:06 | 12030 | 5056 | 3821.518 | 0.909 | ✅ | ❌ |
| CCAA:07 | 48766 | 21823 | 16274.021 | 0.964 | ✅ | ❌ |
| CCAA:08 | 43438 | 17340 | 13085.020 | 0.966 | ✅ | ❌ |
| CCAA:09 | 165384 | 65445 | 49241.654 | 0.974 | ✅ | ❌ |
| CCAA:10 | 111434 | 44986 | 33888.806 | 0.932 | ✅ | ❌ |
| CCAA:11 | 21274 | 9056 | 6930.404 | 0.947 | ✅ | ❌ |
| CCAA:12 | 55009 | 23119 | 17424.094 | 0.966 | ✅ | ❌ |
| CCAA:13 | 144567 | 56021 | 42235.357 | 0.960 | ✅ | ❌ |
| CCAA:14 | 32388 | 11934 | 9068.438 | 0.906 | ✅ | ❌ |
| CCAA:15 | 13912 | 5511 | 4112.177 | 0.899 | ✅ | ❌ |
| CCAA:16 | 45439 | 19519 | 14801.267 | 0.979 | ✅ | ❌ |
| CCAA:17 | 6644 | 2802 | 2064.481 | 0.870 | ✅ | ❌ |
| CCAA:18 | 1696 | 537 | 377.185 | 0.996 | ✅ | ❌ |
| CCAA:19 | 1745 | 553 | 407.579 | 0.968 | ✅ | ❌ |
| ES | 999974 | 393962 | 277613.268 | 0.945 | ✅ | ❌ |

## V-RAREZA

| nivel | combinaciones | sin_donante | personas_afectadas | ok |
| --- | --- | --- | --- | --- |
| persona | 24607 | 0 | 0 | ✅ |
| persona_y_hogar | 153546 | 0 | 0 | ✅ |

## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)

### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)

| ccaa | sint_ocupado | ref_ocupado | sint_parado | ref_parado | paro_sint | paro_epa | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.4968 | 0.4935 | 0.0854 | 0.0841 | 0.1467 | 0.1456 | 0.0047 | ✅ |
| 02 | 0.5499 | 0.5414 | 0.0450 | 0.0482 | 0.0757 | 0.0817 | 0.0085 | ✅ |
| 03 | 0.4756 | 0.4763 | 0.0529 | 0.0478 | 0.1000 | 0.0912 | 0.0050 | ✅ |
| 04 | 0.5935 | 0.6297 | 0.0377 | 0.0410 | 0.0597 | 0.0611 | 0.0394 | ✅ |
| 05 | 0.5303 | 0.5206 | 0.0709 | 0.0683 | 0.1180 | 0.1160 | 0.0124 | ✅ |
| 06 | 0.5133 | 0.5149 | 0.0482 | 0.0408 | 0.0858 | 0.0734 | 0.0074 | ✅ |
| 07 | 0.5022 | 0.4991 | 0.0465 | 0.0456 | 0.0847 | 0.0837 | 0.0040 | ✅ |
| 08 | 0.5305 | 0.5227 | 0.0690 | 0.0700 | 0.1151 | 0.1181 | 0.0078 | ✅ |
| 09 | 0.5742 | 0.5717 | 0.0476 | 0.0490 | 0.0766 | 0.0790 | 0.0026 | ✅ |
| 10 | 0.5272 | 0.5245 | 0.0635 | 0.0640 | 0.1075 | 0.1088 | 0.0027 | ✅ |
| 11 | 0.4863 | 0.4761 | 0.0759 | 0.0725 | 0.1349 | 0.1322 | 0.0135 | ✅ |
| 12 | 0.4950 | 0.4881 | 0.0427 | 0.0421 | 0.0794 | 0.0794 | 0.0075 | ✅ |
| 13 | 0.5918 | 0.5908 | 0.0467 | 0.0485 | 0.0732 | 0.0758 | 0.0017 | ✅ |
| 14 | 0.5481 | 0.5530 | 0.0652 | 0.0672 | 0.1062 | 0.1083 | 0.0069 | ✅ |
| 15 | 0.5486 | 0.5368 | 0.0481 | 0.0471 | 0.0806 | 0.0807 | 0.0127 | ✅ |
| 16 | 0.5242 | 0.5170 | 0.0442 | 0.0396 | 0.0777 | 0.0711 | 0.0118 | ✅ |
| 17 | 0.5472 | 0.5373 | 0.0456 | 0.0516 | 0.0769 | 0.0877 | 0.0100 | ✅ |
| 18 | 0.4835 | 0.5361 | 0.1546 | 0.1548 | 0.2423 | 0.2241 | 0.0528 | ✅ |
| 19 | 0.4967 | 0.4116 | 0.1222 | 0.1077 | 0.1974 | 0.2074 | 0.0996 | ✅ |

### ECV 2025: personas por tamaño del hogar

| ccaa | sint_1 | sint_2 | sint_3 | sint_4 | sint_5+ | ref_1 | ref_2 | ref_3 | ref_4 | ref_5+ | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.1083 | 0.2258 | 0.2402 | 0.2639 | 0.1618 | 0.1071 | 0.2233 | 0.2409 | 0.2579 | 0.1708 | 0.0098 | ✅ |
| 02 | 0.1306 | 0.2440 | 0.2424 | 0.2498 | 0.1331 | 0.1283 | 0.2440 | 0.2449 | 0.2330 | 0.1499 | 0.0192 | ✅ |
| 03 | 0.1553 | 0.2916 | 0.2642 | 0.1882 | 0.1006 | 0.1546 | 0.2897 | 0.2655 | 0.1834 | 0.1068 | 0.0075 | ✅ |
| 04 | 0.0966 | 0.2071 | 0.2301 | 0.2384 | 0.2278 | 0.0970 | 0.2062 | 0.2313 | 0.2235 | 0.2420 | 0.0159 | ✅ |
| 05 | 0.1061 | 0.2090 | 0.2436 | 0.2209 | 0.2204 | 0.1053 | 0.2082 | 0.2429 | 0.1773 | 0.2663 | 0.0459 | ✅ |
| 06 | 0.1311 | 0.2489 | 0.2512 | 0.2336 | 0.1352 | 0.1295 | 0.2462 | 0.2512 | 0.2192 | 0.1539 | 0.0187 | ✅ |
| 07 | 0.1589 | 0.2630 | 0.2445 | 0.2171 | 0.1166 | 0.1573 | 0.2606 | 0.2455 | 0.2055 | 0.1311 | 0.0156 | ✅ |
| 08 | 0.1157 | 0.2227 | 0.2345 | 0.2547 | 0.1724 | 0.1150 | 0.2211 | 0.2357 | 0.2707 | 0.1574 | 0.0172 | ✅ |
| 09 | 0.1046 | 0.2359 | 0.2360 | 0.2386 | 0.1849 | 0.1040 | 0.2350 | 0.2371 | 0.2288 | 0.1951 | 0.0113 | ✅ |
| 10 | 0.1149 | 0.2365 | 0.2412 | 0.2432 | 0.1642 | 0.1147 | 0.2369 | 0.2428 | 0.2297 | 0.1760 | 0.0137 | ✅ |
| 11 | 0.1359 | 0.2517 | 0.2490 | 0.2554 | 0.1080 | 0.1335 | 0.2483 | 0.2488 | 0.2437 | 0.1257 | 0.0177 | ✅ |
| 12 | 0.1304 | 0.2445 | 0.2528 | 0.2225 | 0.1498 | 0.1296 | 0.2435 | 0.2530 | 0.2226 | 0.1513 | 0.0018 | ✅ |
| 13 | 0.1008 | 0.2223 | 0.2332 | 0.2517 | 0.1920 | 0.0985 | 0.2196 | 0.2330 | 0.2468 | 0.2020 | 0.0101 | ✅ |
| 14 | 0.0900 | 0.1961 | 0.2228 | 0.2735 | 0.2176 | 0.0888 | 0.1939 | 0.2219 | 0.2586 | 0.2368 | 0.0192 | ✅ |
| 15 | 0.1152 | 0.2238 | 0.2261 | 0.2513 | 0.1836 | 0.1152 | 0.2216 | 0.2264 | 0.2519 | 0.1848 | 0.0022 | ✅ |
| 16 | 0.1359 | 0.2667 | 0.2341 | 0.2385 | 0.1247 | 0.1337 | 0.2655 | 0.2360 | 0.2353 | 0.1295 | 0.0067 | ✅ |
| 17 | 0.1392 | 0.2512 | 0.2359 | 0.2382 | 0.1355 | 0.1364 | 0.2489 | 0.2398 | 0.2354 | 0.1396 | 0.0080 | ✅ |
| 18 | 0.0697 | 0.1477 | 0.1856 | 0.2306 | 0.3664 | 0.0587 | 0.1663 | 0.2109 | 0.2097 | 0.3543 | 0.0439 | ✅ |
| 19 | 0.0645 | 0.1440 | 0.1829 | 0.2091 | 0.3995 | 0.0733 | 0.1110 | 0.1503 | 0.2119 | 0.4536 | 0.0657 | ✅ |

### Padrón 01/01/2022: proporción de extranjeros por provincia

| provincia | sint_extranjera | ref_extranjera | tvd | dentro |
| --- | --- | --- | --- | --- |
| 01 | 0.1204 | 0.0987 | 0.0217 | ✅ |
| 02 | 0.0993 | 0.0714 | 0.0279 | ✅ |
| 03 | 0.2529 | 0.2044 | 0.0485 | ✅ |
| 04 | 0.2238 | 0.2189 | 0.0049 | ✅ |
| 05 | 0.0940 | 0.0663 | 0.0277 | ✅ |
| 06 | 0.0403 | 0.0319 | 0.0084 | ✅ |
| 07 | 0.2167 | 0.1887 | 0.0280 | ✅ |
| 08 | 0.1811 | 0.1548 | 0.0263 | ✅ |
| 09 | 0.1108 | 0.0835 | 0.0273 | ✅ |
| 10 | 0.0610 | 0.0357 | 0.0254 | ✅ |
| 11 | 0.0547 | 0.0419 | 0.0128 | ✅ |
| 12 | 0.2115 | 0.1540 | 0.0575 | ✅ |
| 13 | 0.0789 | 0.0644 | 0.0145 | ✅ |
| 14 | 0.0358 | 0.0279 | 0.0078 | ✅ |
| 15 | 0.0664 | 0.0416 | 0.0248 | ✅ |
| 16 | 0.1411 | 0.1164 | 0.0247 | ✅ |
| 17 | 0.2268 | 0.2046 | 0.0222 | ✅ |
| 18 | 0.0983 | 0.0750 | 0.0232 | ✅ |
| 19 | 0.1887 | 0.1388 | 0.0498 | ✅ |
| 20 | 0.0968 | 0.0847 | 0.0121 | ✅ |
| 21 | 0.1125 | 0.0968 | 0.0157 | ✅ |
| 22 | 0.1642 | 0.1321 | 0.0321 | ✅ |
| 23 | 0.0451 | 0.0283 | 0.0168 | ✅ |
| 24 | 0.0714 | 0.0456 | 0.0258 | ✅ |
| 25 | 0.2093 | 0.1887 | 0.0206 | ✅ |
| 26 | 0.1529 | 0.1305 | 0.0224 | ✅ |
| 27 | 0.0770 | 0.0520 | 0.0250 | ✅ |
| 28 | 0.1669 | 0.1407 | 0.0262 | ✅ |
| 29 | 0.1941 | 0.1673 | 0.0268 | ✅ |
| 30 | 0.1633 | 0.1480 | 0.0152 | ✅ |
| 31 | 0.1351 | 0.1106 | 0.0245 | ✅ |
| 32 | 0.0834 | 0.0543 | 0.0291 | ✅ |
| 33 | 0.0753 | 0.0454 | 0.0299 | ✅ |
| 34 | 0.0823 | 0.0473 | 0.0350 | ✅ |
| 35 | 0.1481 | 0.1265 | 0.0216 | ✅ |
| 36 | 0.0656 | 0.0412 | 0.0245 | ✅ |
| 37 | 0.0806 | 0.0487 | 0.0320 | ✅ |
| 38 | 0.1556 | 0.1389 | 0.0166 | ✅ |
| 39 | 0.0854 | 0.0636 | 0.0218 | ✅ |
| 40 | 0.1417 | 0.1185 | 0.0232 | ✅ |
| 41 | 0.0696 | 0.0411 | 0.0284 | ✅ |
| 42 | 0.1268 | 0.0996 | 0.0273 | ✅ |
| 43 | 0.1935 | 0.1681 | 0.0254 | ✅ |
| 44 | 0.1215 | 0.1161 | 0.0055 | ✅ |
| 45 | 0.1418 | 0.1042 | 0.0375 | ✅ |
| 46 | 0.1683 | 0.1170 | 0.0514 | ✅ |
| 47 | 0.0915 | 0.0568 | 0.0347 | ✅ |
| 48 | 0.1032 | 0.0785 | 0.0247 | ✅ |
| 49 | 0.0585 | 0.0379 | 0.0206 | ✅ |
| 50 | 0.1587 | 0.1235 | 0.0352 | ✅ |
| 51 | 0.0678 | 0.0591 | 0.0087 | ✅ |
| 52 | 0.1330 | 0.1371 | 0.0041 | ✅ |

## V-REPRO

2026-01-01_ES_10000_s1 generado de nuevo en otro directorio: mismos hashes.

- `persons.parquet`: `c3cb760c1b3d3ed4129f529063b4e824fac46e6b7c1b8088aac0338aecf6cc79`
- `households.parquet`: `45a7b1626838b7b32e89b93ad1acd3b8a3ed0fc0e51656dd56fc53bfea44e9b8`
- `lineage.parquet`: `85c0a499044874700c2e3fbd631d22770dc184b2b285c4054e387359008c633c`
