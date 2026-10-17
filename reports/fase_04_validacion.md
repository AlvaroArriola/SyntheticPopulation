# Fase 04 · Tablas de validación

Generado por `python -m sinpop.validate.fase4` (git:fcb7dee-dirty, 2026-10-17). Resumen en `fase_04_validacion.json`; detalle por población en `fase_04/`.

## Curva de error frente a tamaño (España; media de 5 semillas)

| n | tvd_media_calibradas | sd_calibradas | tvd_media_reservadas | sd_reservadas |
| --- | --- | --- | --- | --- |
| 10000 | 0.0210 | 0.0022 | 0.0199 | 0.0004 |
| 50000 | 0.0071 | 0.0009 | 0.0142 | 0.0004 |
| 100000 | 0.0038 | 0.0003 | 0.0137 | 0.0002 |
| 500000 | 0.0015 | 0.0001 | 0.0130 | 0.0002 |
| 1000000 | 0.0011 | 0.0001 | 0.0128 | 0.0001 |

## TVD por marginal calibrada (España; media de 5 semillas)

| objetivo | 1000000 | 10000 | 500000 | 50000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| actividad_tramo | 0.0029 | 0.0096 | 0.0036 | 0.0060 | 0.0052 |
| edad5_sexo | 0.0007 | 0.0051 | 0.0010 | 0.0024 | 0.0018 |
| edad5_sexo_colectivos | 0.0078 | 0.2435 | 0.0104 | 0.0754 | 0.0350 |
| edad5_sexo_familiares | 0.0007 | 0.0055 | 0.0010 | 0.0026 | 0.0018 |
| estudios_edad | 0.0007 | 0.0053 | 0.0010 | 0.0025 | 0.0018 |
| nacimiento_nacionalidad | 0.0003 | 0.0028 | 0.0004 | 0.0009 | 0.0009 |
| nacionalidad | 0.0002 | 0.0020 | 0.0003 | 0.0007 | 0.0006 |
| nacionalidad_edad | 0.0006 | 0.0057 | 0.0008 | 0.0023 | 0.0016 |
| nacionalidad_top | 0.0003 | 0.0028 | 0.0004 | 0.0009 | 0.0007 |
| sin_estudios_edad | 0.0003 | 0.0032 | 0.0004 | 0.0012 | 0.0008 |
| tamano_hogar | 0.0001 | 0.0022 | 0.0003 | 0.0010 | 0.0009 |
| tipo_hogar | 0.0004 | 0.0047 | 0.0006 | 0.0024 | 0.0018 |
| tipo_residencia (implícito) | 0.0000 | 0.0005 | 0.0000 | 0.0001 | 0.0001 |
| urbanizacion | 0.0001 | 0.0011 | 0.0003 | 0.0009 | 0.0007 |

## TVD por cruce reservado (España; media de 5 semillas)

| objetivo | 1000000 | 10000 | 100000 | 500000 | 50000 |
| --- | --- | --- | --- | --- | --- |
| actividad_edad | 0.0080 | 0.0154 | 0.0089 | 0.0082 | 0.0109 |
| actividad_sexo | 0.0140 | 0.0162 | 0.0145 | 0.0142 | 0.0141 |
| adultos_nacionalidad | 0.0017 | 0.0025 | 0.0018 | 0.0017 | 0.0023 |
| estado_civil_edad | 0.0278 | 0.0323 | 0.0281 | 0.0280 | 0.0267 |
| estudios_sexo_edad | 0.0068 | 0.0157 | 0.0090 | 0.0072 | 0.0099 |
| nacionalidad_top_sexo_edad | 0.0075 | 0.0214 | 0.0100 | 0.0080 | 0.0119 |
| provincia_si_calibra_ccaa | 0.0096 | 0.0234 | 0.0101 | 0.0096 | 0.0123 |
| tamano_municipio | 0.0105 | 0.0170 | 0.0104 | 0.0107 | 0.0098 |
| tipo_hogar_edad4_ref | 0.0297 | 0.0355 | 0.0302 | 0.0298 | 0.0298 |

## Fallos por tamaño

| N | semilla | v_marg | v_cruce | v_cruce_excepciones | v_cruce_estricto | comprobaciones_cruce |
| --- | --- | --- | --- | --- | --- | --- |
| 10000 | 1 | 0 | 5 | 0 | 18 | 583 |
| 10000 | 2 | 0 | 10 | 0 | 30 | 583 |
| 10000 | 3 | 0 | 8 | 0 | 26 | 583 |
| 10000 | 4 | 0 | 17 | 1 | 45 | 583 |
| 10000 | 5 | 0 | 7 | 0 | 19 | 583 |
| 50000 | 1 | 0 | 4 | 1 | 12 | 583 |
| 50000 | 2 | 0 | 1 | 0 | 11 | 583 |
| 50000 | 3 | 0 | 3 | 1 | 7 | 583 |
| 50000 | 4 | 0 | 2 | 0 | 5 | 583 |
| 50000 | 5 | 0 | 3 | 1 | 11 | 583 |
| 100000 | 1 | 0 | 3 | 1 | 9 | 583 |
| 100000 | 2 | 0 | 2 | 0 | 7 | 583 |
| 100000 | 3 | 0 | 2 | 1 | 8 | 583 |
| 100000 | 4 | 0 | 2 | 1 | 5 | 583 |
| 100000 | 5 | 0 | 1 | 1 | 5 | 583 |
| 500000 | 1 | 0 | 0 | 1 | 1 | 583 |
| 500000 | 2 | 0 | 0 | 0 | 0 | 583 |
| 500000 | 3 | 0 | 0 | 0 | 0 | 583 |
| 500000 | 4 | 0 | 1 | 0 | 1 | 583 |
| 500000 | 5 | 0 | 0 | 0 | 0 | 583 |
| 1000000 | 1 | 0 | 0 | 0 | 0 | 583 |
| 1000000 | 2 | 0 | 0 | 1 | 1 | 583 |
| 1000000 | 3 | 0 | 0 | 0 | 0 | 583 |
| 1000000 | 4 | 0 | 0 | 1 | 1 | 583 |
| 1000000 | 5 | 0 | 1 | 0 | 1 | 583 |

### Fallos de V-CRUCE con 500.000 y 1.000.000 de personas

| nivel | territorio | objetivo | tvd | umbral | excepcion | N | semilla |
| --- | --- | --- | --- | --- | --- | --- | --- |
| provincia | PROV:40 | tamano_municipio | 0.0818 | 0.0800 | ✅ | 500000 | 1 |
| espana | ES | tipo_hogar_edad4_ref | 0.0304 | 0.0300 | ❌ | 500000 | 4 |
| provincia | PROV:40 | tamano_municipio | 0.0802 | 0.0800 | ✅ | 1000000 | 2 |
| provincia | PROV:40 | tamano_municipio | 0.0810 | 0.0800 | ✅ | 1000000 | 4 |
| espana | ES | tipo_hogar_edad4_ref | 0.0301 | 0.0300 | ❌ | 1000000 | 5 |

## V-SEMILLAS

| n | proporciones | fuera | razon_media | razon_max |
| --- | --- | --- | --- | --- |
| 10000 | 294 | 0 | 0.2829 | 1.2053 |
| 50000 | 294 | 0 | 0.2320 | 0.5646 |
| 100000 | 294 | 0 | 0.2230 | 0.5613 |
| 500000 | 294 | 0 | 0.2600 | 0.5895 |
| 1000000 | 294 | 0 | 0.2528 | 0.6436 |

## V-PESOS (calibración por comunidades)

| bloque | desviacion_max | proporcion_en_rango | kish_ratio | no_positivos | factor_min | factor_max | proporcion_local | ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 0.0000 | 1.0000 | 0.8165 | 0 | 0.2000 | 4.9998 | 0.9950 | ✅ |
| CCAA:02 | 0.0000 | 1.0000 | 0.7968 | 0 | 0.2000 | 4.9987 | 0.9996 | ✅ |
| CCAA:03 | 0.0000 | 1.0000 | 0.6621 | 0 | 0.2000 | 4.9871 | 0.9976 | ✅ |
| CCAA:04 | 0.0000 | 1.0000 | 0.6464 | 0 | 0.2000 | 4.9995 | 0.9997 | ✅ |
| CCAA:05 | 0.0000 | 1.0000 | 0.6367 | 0 | 0.2000 | 4.9899 | 0.9956 | ✅ |
| CCAA:06 | 0.0000 | 1.0000 | 0.7981 | 0 | 0.2003 | 4.9797 | 0.9996 | ✅ |
| CCAA:07 | 0.0000 | 1.0000 | 0.8293 | 0 | 0.2000 | 4.9989 | 0.9984 | ✅ |
| CCAA:08 | 0.0000 | 1.0000 | 0.7295 | 0 | 0.2001 | 4.9954 | 0.9996 | ✅ |
| CCAA:09 | 0.0000 | 1.0000 | 0.7628 | 0 | 0.2000 | 4.9998 | 0.9995 | ✅ |
| CCAA:10 | 0.0000 | 1.0000 | 0.7502 | 0 | 0.2000 | 4.9999 | 0.9993 | ✅ |
| CCAA:11 | 0.0000 | 1.0000 | 0.7951 | 0 | 0.2025 | 4.9442 | 0.9994 | ✅ |
| CCAA:12 | 0.0000 | 1.0000 | 0.8005 | 0 | 0.2000 | 4.9999 | 0.9948 | ✅ |
| CCAA:13 | 0.0000 | 1.0000 | 0.7721 | 0 | 0.2000 | 5.0000 | 0.9995 | ✅ |
| CCAA:14 | 0.0000 | 1.0000 | 0.7822 | 0 | 0.2000 | 4.9976 | 0.9985 | ✅ |
| CCAA:15 | 0.0000 | 1.0000 | 0.7565 | 0 | 0.2000 | 4.9900 | 0.9965 | ✅ |
| CCAA:16 | 0.0000 | 1.0000 | 0.7768 | 0 | 0.2000 | 4.9944 | 0.9933 | ✅ |
| CCAA:17 | 0.0000 | 1.0000 | 0.8041 | 0 | 0.2002 | 4.6186 | 0.9991 | ✅ |
| CCAA:18 | 0.0000 | 1.0000 | 0.7178 | 0 | 0.2000 | 4.5223 | 0.9867 | ✅ |
| CCAA:19 | 0.0000 | 1.0000 | 0.7139 | 0 | 0.2000 | 3.9108 | 0.9844 | ✅ |

## Ampliación de donantes

| bloque | objetivo | clave | locales | razon_inicial | anadidas | motivo |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | 523 | 8.7635 | 1307 | None |
| CCAA:01 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 52 | 15.1822 | 150 | None |
| CCAA:01 | nacionalidad_top | nacionalidad_top=peru | 322 | 3.9510 | 186 | None |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 9 | 8.0403 | 20 | None |
| CCAA:02 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 4 | 14.7850 | 1 | None |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | 1 | 51.0967 | 4 | None |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 10 | 15.1662 | 51 | None |
| CCAA:03 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 4 | 31.6831 | 1 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=peru | 50 | 3.5617 | 19 | None |
| CCAA:03 | nacionalidad_top | nacionalidad_top=ucrania | 42 | 5.4382 | 33 | None |
| CCAA:04 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 9 | 6.1548 | 14 | None |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | 110 | 9.2814 | 298 | None |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 4 | 41.5857 | 1 | None |
| CCAA:05 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 14 | 14.9145 | 70 | None |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 1 | 23.7012 | 4 | None |
| CCAA:06 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 0 | None | 5 | None |
| CCAA:06 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 3 | 1.8881 | 2 | None |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 18 | 4.6602 | 16 | None |
| CCAA:07 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 10 | 16.2022 | 55 | None |
| CCAA:07 | nacionalidad_top | nacionalidad_top=peru | 187 | 3.8136 | 96 | None |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 4 | 30.7750 | 1 | None |
| CCAA:08 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 8 | 11.8672 | 30 | None |
| CCAA:09 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 17 | 23.1970 | 141 | None |
| CCAA:10 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 26 | 15.6834 | 138 | None |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 4 | 20.0396 | 1 | None |
| CCAA:11 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 7 | 5.7614 | 10 | None |
| CCAA:11 | nacionalidad_top | nacionalidad_top=peru | 36 | 3.7553 | 17 | None |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | 173 | 8.4316 | 409 | None |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 13 | 10.2904 | 41 | None |
| CCAA:12 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 7 | 10.0625 | 22 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=peru | 207 | 3.7108 | 93 | None |
| CCAA:12 | nacionalidad_top | nacionalidad_top=ucrania | 40 | 3.5008 | 18 | None |
| CCAA:13 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 20 | 19.2757 | 135 | None |
| CCAA:14 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 7 | 31.6254 | 82 | None |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | 64 | 5.8992 | 88 | None |
| CCAA:15 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 4 | 20.4672 | 1 | None |
| CCAA:15 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 5 | 16.3738 | 3 | reparacion 1 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | 53 | 5.2033 | 56 | None |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | 228 | 8.5081 | 550 | None |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 4 | 18.1971 | 1 | None |
| CCAA:16 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 11 | 7.3319 | 22 | None |
| CCAA:16 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 8 | 4.4910 | 7 | None |
| CCAA:17 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 1 | 25.4427 | 4 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 8.1332 | 4 | None |
| CCAA:17 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.9987 | 3 | None |
| CCAA:17 | nacionalidad_top | nacionalidad_top=paraguay | 4 | 4.3333 | 1 | None |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=45-54 | 4 | 2.0889 | 1 | None |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | 8 | 4.9688 | 8 | None |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | 1 | 3.7044 | 4 | None |
| CCAA:18 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 0 | None | 5 | None |
| CCAA:18 | estudios_edad | estudios_3=superior;edad_estudios=90+ | 3 | 2.0488 | 2 | None |
| CCAA:18 | nacionalidad | nacionalidad_grupo=otros | 0 | None | 5 | None |
| CCAA:18 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.5142 | 1 | None |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=85-89 | 1 | 1.9579 | 4 | None |
| CCAA:18 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.3251 | 3 | None |
| CCAA:18 | nacionalidad_top | nacionalidad_top=china | 1 | 2.3948 | 4 | None |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | 0 | None | 5 | None |
| CCAA:19 | actividad_tramo | relacion_actividad=parado;edad_tramo_epa=65+ | 1 | 7.9095 | 4 | None |
| CCAA:19 | estudios_edad | estudios_3=secundaria_2a_etapa;edad_estudios=90+ | 2 | 1.3648 | 3 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=america_latina | 18 | 4.7103 | 15 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=asia | 2 | 1.6472 | 3 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=otros | 2 | 3.0749 | 3 | None |
| CCAA:19 | nacionalidad | nacionalidad_grupo=resto_europa | 4 | 1.6564 | 1 | None |
| CCAA:19 | nacionalidad_edad | nacionalidad_esp_ext=extranjera;edad_5=90+ | 2 | 0.8079 | 3 | None |
| CCAA:19 | nacionalidad_top | nacionalidad_top=colombia | 1 | 17.6844 | 4 | None |
| CCAA:19 | nacionalidad_top | nacionalidad_top=venezuela | 5 | 4.2542 | 4 | None |

## Nacionalidades fusionadas con «otras extranjeras»

| bloque | objetivo | clave | fusionada_en |
| --- | --- | --- | --- |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:01 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:01 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:01 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:02 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:02 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:02 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:03 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:03 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:03 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:04 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:04 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:05 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:05 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:05 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:05 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:05 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:06 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:06 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:06 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:07 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:07 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:08 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:08 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:08 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:09 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:09 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:09 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:10 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:10 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:10 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:11 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:11 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:12 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:12 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:12 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:12 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:13 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:13 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:14 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:14 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:15 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:15 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:15 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:15 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:16 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:16 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:16 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:17 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
| CCAA:17 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:18 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:18 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:18 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=35-44 | relacion_actividad=otra_inactividad;edad_tramo_epa=35-44 |
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
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=55-64 | relacion_actividad=otra_inactividad;edad_tramo_epa=55-64 |
| CCAA:19 | actividad_tramo | relacion_actividad=estudiante;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=incapacidad_permanente;edad_tramo_epa=65+ | relacion_actividad=otra_inactividad;edad_tramo_epa=65+ |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=16-24 | relacion_actividad=otra_inactividad;edad_tramo_epa=16-24 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=25-34 | relacion_actividad=otra_inactividad;edad_tramo_epa=25-34 |
| CCAA:19 | actividad_tramo | relacion_actividad=jubilado_pensionista;edad_tramo_epa=45-54 | relacion_actividad=otra_inactividad;edad_tramo_epa=45-54 |
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
| actividad_edad | relacion_actividad × edad_actividad | 0.6145 | 0.6170 | 0.0026 | ✅ |
| actividad_sexo | relacion_actividad × sexo | 0.2209 | 0.1945 | 0.0263 | ✅ |
| adultos_nacionalidad | nacionalidad_esp_ext × es_adulto | 0.0028 | 0.0046 | 0.0019 | ✅ |
| estado_civil_edad | estado_civil × edad_estado_civil | 0.6242 | 0.6326 | 0.0085 | ✅ |
| estudios_sexo_edad | estudios_3 × sexo | 0.0391 | 0.0354 | 0.0038 | ✅ |
| estudios_sexo_edad | estudios_3 × edad_estudios | 0.6228 | 0.6228 | 0.0001 | ✅ |
| estudios_sexo_edad | sexo × edad_estudios | 0.0713 | 0.0712 | 0.0001 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × sexo | 0.0420 | 0.0425 | 0.0005 | ✅ |
| nacionalidad_top_sexo_edad | nacionalidad_top × edad_nacionalidad | 0.1056 | 0.1055 | 0.0002 | ✅ |
| nacionalidad_top_sexo_edad | sexo × edad_nacionalidad | 0.0575 | 0.0573 | 0.0002 | ✅ |
| tipo_hogar_edad4_ref | tipo_hogar × edad_4 | 0.1810 | 0.1871 | 0.0062 | ✅ |

## Minorías, primera pasada (2026-01-01_ES_1000000_s1)

| grupo | unidad | esperado | observado | ratio | ok_representacion | donantes_distintos | top5 | ok_concentracion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mayores_85 | persona | 32792.9133 | 32784.0000 | 0.9997 | ✅ | 29027 | 0.0022 | ✅ |
| municipios_menos_2000 | persona | 54711.6676 | 55964.0000 | 1.0229 | ✅ | 25153 | 0.0015 | ✅ |
| parados | persona | 50993.1206 | 51276.0000 | 1.0055 | ✅ | 44377 | 0.0016 | ✅ |
| monoparentales | hogar | 46940.9181 | 46916.0000 | 0.9995 | ✅ | 46550 | 0.0011 | ✅ |
| mayores_solos | persona | 47330.1427 | 49615.0000 | 1.0483 | ✅ | 49098 | 0.0005 | ✅ |
| ceuta_melilla | persona | 3449.4706 | 3448.0000 | 0.9996 | ✅ | 1087 | 0.0183 | ✅ |
| nacionalidad_alemania | persona | 2750.0843 | 2735.0000 | 0.9945 | ✅ | 1963 | 0.0106 | ✅ |
| nacionalidad_argentina | persona | 3114.6619 | 3139.0000 | 1.0078 | ✅ | 2156 | 0.0115 | ✅ |
| nacionalidad_china | persona | 4967.8455 | 4960.0000 | 0.9984 | ✅ | 1590 | 0.0113 | ✅ |
| nacionalidad_colombia | persona | 14241.1457 | 14177.0000 | 0.9955 | ✅ | 7077 | 0.0047 | ✅ |
| nacionalidad_ecuador | persona | 2767.9668 | 2785.0000 | 1.0062 | ✅ | 1875 | 0.0140 | ✅ |
| nacionalidad_francia | persona | 2656.6106 | 2657.0000 | 1.0001 | ✅ | 1933 | 0.0098 | ✅ |
| nacionalidad_honduras | persona | 3667.2087 | 3658.0000 | 0.9975 | ✅ | 1710 | 0.0139 | ✅ |
| nacionalidad_italia | persona | 7186.8519 | 7202.0000 | 1.0021 | ✅ | 4625 | 0.0061 | ✅ |
| nacionalidad_marruecos | persona | 20300.2251 | 20237.0000 | 0.9969 | ✅ | 8149 | 0.0042 | ✅ |
| nacionalidad_paraguay | persona | 2554.7857 | 2538.0000 | 0.9934 | ✅ | 1395 | 0.0181 | ✅ |
| nacionalidad_peru | persona | 5438.6357 | 5385.0000 | 0.9901 | ✅ | 2671 | 0.0115 | ✅ |
| nacionalidad_reino_unido | persona | 5615.6166 | 5655.0000 | 1.0070 | ✅ | 3582 | 0.0067 | ✅ |
| nacionalidad_rumania | persona | 12831.0794 | 12851.0000 | 1.0016 | ✅ | 5712 | 0.0053 | ✅ |
| nacionalidad_ucrania | persona | 4259.2516 | 4216.0000 | 0.9898 | ✅ | 1847 | 0.0128 | ✅ |
| nacionalidad_venezuela | persona | 7937.4137 | 7906.0000 | 0.9960 | ✅ | 3889 | 0.0071 | ✅ |

## Reglas blandas (media de 5 semillas; nº de semillas dentro)

| regla | N | frecuencia_donantes | exceso_relativo | ok_estricto | ok |
| --- | --- | --- | --- | --- | --- |
| casado_menor_20 | 10000 | 0.000050 | 0.193365 | 3 | 4 |
| casado_menor_20 | 50000 | 0.000050 | -0.285134 | 3 | 5 |
| casado_menor_20 | 100000 | 0.000050 | 0.191103 | 2 | 4 |
| casado_menor_20 | 500000 | 0.000050 | 0.119256 | 2 | 5 |
| casado_menor_20 | 1000000 | 0.000050 | 0.051616 | 3 | 5 |
| estudiante_50_o_mas | 10000 | 0.000620 | -0.450190 | 5 | 5 |
| estudiante_50_o_mas | 50000 | 0.000620 | -0.218959 | 5 | 5 |
| estudiante_50_o_mas | 100000 | 0.000620 | -0.057677 | 5 | 5 |
| estudiante_50_o_mas | 500000 | 0.000620 | 0.026443 | 5 | 5 |
| estudiante_50_o_mas | 1000000 | 0.000620 | -0.026609 | 5 | 5 |
| hogar_8_o_mas | 10000 | 0.016754 | -0.093684 | 4 | 5 |
| hogar_8_o_mas | 50000 | 0.016754 | -0.105195 | 5 | 5 |
| hogar_8_o_mas | 100000 | 0.016754 | -0.092272 | 5 | 5 |
| hogar_8_o_mas | 500000 | 0.016754 | -0.037971 | 5 | 5 |
| hogar_8_o_mas | 1000000 | 0.016754 | 0.002772 | 5 | 5 |
| incapacidad_menor_25 | 10000 | 0.000064 | -1.000000 | 5 | 5 |
| incapacidad_menor_25 | 50000 | 0.000064 | -0.496163 | 5 | 5 |
| incapacidad_menor_25 | 100000 | 0.000064 | -0.118413 | 5 | 5 |
| incapacidad_menor_25 | 500000 | 0.000064 | -0.011767 | 5 | 5 |
| incapacidad_menor_25 | 1000000 | 0.000064 | -0.024509 | 5 | 5 |
| jubilado_menor_50 | 10000 | 0.000050 | -0.595821 | 4 | 5 |
| jubilado_menor_50 | 50000 | 0.000050 | -0.031367 | 3 | 5 |
| jubilado_menor_50 | 100000 | 0.000050 | -0.192891 | 4 | 5 |
| jubilado_menor_50 | 500000 | 0.000050 | -0.096420 | 4 | 5 |
| jubilado_menor_50 | 1000000 | 0.000050 | -0.072362 | 5 | 5 |
| ocupado_75_o_mas | 10000 | 0.001716 | -0.158238 | 4 | 5 |
| ocupado_75_o_mas | 50000 | 0.001716 | 0.096637 | 2 | 5 |
| ocupado_75_o_mas | 100000 | 0.001716 | -0.007299 | 5 | 5 |
| ocupado_75_o_mas | 500000 | 0.001716 | 0.013511 | 5 | 5 |
| ocupado_75_o_mas | 1000000 | 0.001716 | 0.008575 | 5 | 5 |
| superior_20_21 | 10000 | 0.003328 | 0.109115 | 3 | 5 |
| superior_20_21 | 50000 | 0.003328 | 0.023697 | 4 | 5 |
| superior_20_21 | 100000 | 0.003328 | -0.010104 | 5 | 5 |
| superior_20_21 | 500000 | 0.003328 | 0.011122 | 5 | 5 |
| superior_20_21 | 1000000 | 0.003328 | -0.014276 | 5 | 5 |
| viudo_menor_30 | 10000 | 0.000040 | -0.003176 | 3 | 5 |
| viudo_menor_30 | 50000 | 0.000040 | 0.393291 | 2 | 5 |
| viudo_menor_30 | 100000 | 0.000040 | 0.293637 | 2 | 4 |
| viudo_menor_30 | 500000 | 0.000040 | 0.014527 | 3 | 5 |
| viudo_menor_30 | 1000000 | 0.000040 | -0.015443 | 5 | 5 |

## G4.7 · Sobremuestreo (edad>=85:10000, 2026-01-01_ES_100000_s1_sm7d9288)

Miembros del grupo: 9900 (mínimo pedido 10000); α = 0.8707, β = 3.0490; suma de pesos 100236.

| objetivo | tvd | n_efectivo | umbral | ok |
| --- | --- | --- | --- | --- |
| actividad_tramo | 0.0069 | 91046.3573 | 0.0108 | ✅ |
| edad5_sexo | 0.0026 | 91046.3573 | 0.0131 | ✅ |
| edad5_sexo_colectivos | 0.0438 | 807.0816 | 0.1224 | ✅ |
| edad5_sexo_familiares | 0.0027 | 90254.4184 | 0.0134 | ✅ |
| estudios_edad | 0.0022 | 91046.3573 | 0.0118 | ✅ |
| nacimiento_nacionalidad | 0.0012 | 91046.3573 | 0.0051 | ✅ |
| nacionalidad | 0.0007 | 91046.3573 | 0.0053 | ✅ |
| nacionalidad_edad | 0.0024 | 91046.3573 | 0.0125 | ✅ |
| nacionalidad_top | 0.0009 | 91046.3573 | 0.0060 | ✅ |
| sin_estudios_edad | 0.0016 | 91046.3573 | 0.0097 | ✅ |
| tamano_hogar | 0.0006 | 36610.4982 | 0.0093 | ✅ |
| tipo_hogar | 0.0011 | 36610.4982 | 0.0123 | ✅ |
| urbanizacion | 0.0007 | 91046.3573 | 0.0059 | ✅ |

## V-DONANTES (2026-01-01_ES_1000000_s1)

| territorio | personas | hogares_donantes | kish | proporcion_local | ok | confianza_reducida |
| --- | --- | --- | --- | --- | --- | --- |
| CCAA:01 | 176438 | 70188 | 53853.923 | 0.990 | ✅ | ❌ |
| CCAA:02 | 27880 | 11734 | 8549.965 | 0.997 | ✅ | ❌ |
| CCAA:03 | 20604 | 9293 | 6872.670 | 0.990 | ✅ | ❌ |
| CCAA:04 | 25384 | 9568 | 7059.485 | 0.999 | ✅ | ❌ |
| CCAA:05 | 45877 | 17620 | 11938.101 | 0.989 | ✅ | ❌ |
| CCAA:06 | 12046 | 5059 | 3774.087 | 0.998 | ✅ | ❌ |
| CCAA:07 | 48770 | 21899 | 16315.098 | 0.995 | ✅ | ❌ |
| CCAA:08 | 43440 | 17333 | 12468.177 | 0.997 | ✅ | ❌ |
| CCAA:09 | 165341 | 65577 | 49353.326 | 0.999 | ✅ | ❌ |
| CCAA:10 | 111456 | 45105 | 34225.935 | 0.999 | ✅ | ❌ |
| CCAA:11 | 21302 | 9082 | 6891.043 | 0.997 | ✅ | ❌ |
| CCAA:12 | 55008 | 23137 | 17419.949 | 0.989 | ✅ | ❌ |
| CCAA:13 | 144498 | 56047 | 42378.064 | 0.999 | ✅ | ❌ |
| CCAA:14 | 32374 | 11949 | 9136.744 | 0.997 | ✅ | ❌ |
| CCAA:15 | 13903 | 5511 | 4042.865 | 0.991 | ✅ | ❌ |
| CCAA:16 | 45451 | 19583 | 14819.709 | 0.987 | ✅ | ❌ |
| CCAA:17 | 6647 | 2814 | 2095.850 | 0.997 | ✅ | ❌ |
| CCAA:18 | 1694 | 544 | 385.393 | 0.988 | ✅ | ❌ |
| CCAA:19 | 1754 | 544 | 393.920 | 0.975 | ✅ | ❌ |
| ES | 999867 | 401444 | 296699.503 | 0.995 | ✅ | ❌ |

## V-RAREZA

| nivel | combinaciones | sin_donante | personas_afectadas | ok |
| --- | --- | --- | --- | --- |
| persona | 25693 | 0 | 0 | ✅ |
| persona_y_hogar | 158882 | 0 | 0 | ✅ |

## Validación externa (no es puerta; se investiga si TVD > 2 × V-CRUCE)

### EPA 2T 2026: ocupados, parados e inactivos de 16+ (viviendas familiares)

| ccaa | sint_ocupado | ref_ocupado | sint_parado | ref_parado | paro_sint | paro_epa | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.4974 | 0.4935 | 0.0862 | 0.0841 | 0.1477 | 0.1456 | 0.0060 | ✅ |
| 02 | 0.5518 | 0.5414 | 0.0461 | 0.0482 | 0.0772 | 0.0817 | 0.0104 | ✅ |
| 03 | 0.4785 | 0.4763 | 0.0529 | 0.0478 | 0.0995 | 0.0912 | 0.0073 | ✅ |
| 04 | 0.5927 | 0.6297 | 0.0382 | 0.0410 | 0.0606 | 0.0611 | 0.0397 | ✅ |
| 05 | 0.5299 | 0.5206 | 0.0728 | 0.0683 | 0.1208 | 0.1160 | 0.0138 | ✅ |
| 06 | 0.5117 | 0.5149 | 0.0497 | 0.0408 | 0.0885 | 0.0734 | 0.0089 | ✅ |
| 07 | 0.5034 | 0.4991 | 0.0476 | 0.0456 | 0.0863 | 0.0837 | 0.0063 | ✅ |
| 08 | 0.5300 | 0.5227 | 0.0697 | 0.0700 | 0.1162 | 0.1181 | 0.0073 | ✅ |
| 09 | 0.5751 | 0.5717 | 0.0486 | 0.0490 | 0.0779 | 0.0790 | 0.0034 | ✅ |
| 10 | 0.5275 | 0.5245 | 0.0649 | 0.0640 | 0.1096 | 0.1088 | 0.0039 | ✅ |
| 11 | 0.4860 | 0.4761 | 0.0765 | 0.0725 | 0.1360 | 0.1322 | 0.0139 | ✅ |
| 12 | 0.4958 | 0.4881 | 0.0432 | 0.0421 | 0.0802 | 0.0794 | 0.0089 | ✅ |
| 13 | 0.5928 | 0.5908 | 0.0476 | 0.0485 | 0.0744 | 0.0758 | 0.0020 | ✅ |
| 14 | 0.5499 | 0.5530 | 0.0665 | 0.0672 | 0.1078 | 0.1083 | 0.0038 | ✅ |
| 15 | 0.5482 | 0.5368 | 0.0514 | 0.0471 | 0.0857 | 0.0807 | 0.0156 | ✅ |
| 16 | 0.5253 | 0.5170 | 0.0441 | 0.0396 | 0.0775 | 0.0711 | 0.0129 | ✅ |
| 17 | 0.5492 | 0.5373 | 0.0476 | 0.0516 | 0.0797 | 0.0877 | 0.0120 | ✅ |
| 18 | 0.4857 | 0.5361 | 0.1507 | 0.1548 | 0.2368 | 0.2241 | 0.0545 | ✅ |
| 19 | 0.4902 | 0.4116 | 0.1320 | 0.1077 | 0.2122 | 0.2074 | 0.1029 | ❌ |

### ECV 2025: personas por tamaño del hogar

| ccaa | sint_1 | sint_2 | sint_3 | sint_4 | sint_5+ | ref_1 | ref_2 | ref_3 | ref_4 | ref_5+ | tvd | dentro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 0.1082 | 0.2261 | 0.2408 | 0.2660 | 0.1589 | 0.1071 | 0.2233 | 0.2409 | 0.2579 | 0.1708 | 0.0121 | ✅ |
| 02 | 0.1303 | 0.2434 | 0.2436 | 0.2489 | 0.1338 | 0.1283 | 0.2440 | 0.2449 | 0.2330 | 0.1499 | 0.0180 | ✅ |
| 03 | 0.1556 | 0.2895 | 0.2662 | 0.1876 | 0.1011 | 0.1546 | 0.2897 | 0.2655 | 0.1834 | 0.1068 | 0.0060 | ✅ |
| 04 | 0.0969 | 0.2065 | 0.2304 | 0.2404 | 0.2258 | 0.0970 | 0.2062 | 0.2313 | 0.2235 | 0.2420 | 0.0172 | ✅ |
| 05 | 0.1063 | 0.2093 | 0.2433 | 0.2215 | 0.2196 | 0.1053 | 0.2082 | 0.2429 | 0.1773 | 0.2663 | 0.0467 | ✅ |
| 06 | 0.1315 | 0.2482 | 0.2504 | 0.2306 | 0.1393 | 0.1295 | 0.2462 | 0.2512 | 0.2192 | 0.1539 | 0.0154 | ✅ |
| 07 | 0.1593 | 0.2627 | 0.2430 | 0.2182 | 0.1168 | 0.1573 | 0.2606 | 0.2455 | 0.2055 | 0.1311 | 0.0169 | ✅ |
| 08 | 0.1155 | 0.2229 | 0.2341 | 0.2554 | 0.1721 | 0.1150 | 0.2211 | 0.2357 | 0.2707 | 0.1574 | 0.0169 | ✅ |
| 09 | 0.1048 | 0.2361 | 0.2357 | 0.2392 | 0.1842 | 0.1040 | 0.2350 | 0.2371 | 0.2288 | 0.1951 | 0.0123 | ✅ |
| 10 | 0.1147 | 0.2367 | 0.2408 | 0.2427 | 0.1651 | 0.1147 | 0.2369 | 0.2428 | 0.2297 | 0.1760 | 0.0131 | ✅ |
| 11 | 0.1357 | 0.2522 | 0.2457 | 0.2570 | 0.1094 | 0.1335 | 0.2483 | 0.2488 | 0.2437 | 0.1257 | 0.0194 | ✅ |
| 12 | 0.1305 | 0.2450 | 0.2518 | 0.2228 | 0.1499 | 0.1296 | 0.2435 | 0.2530 | 0.2226 | 0.1513 | 0.0026 | ✅ |
| 13 | 0.1008 | 0.2222 | 0.2339 | 0.2529 | 0.1902 | 0.0985 | 0.2196 | 0.2330 | 0.2468 | 0.2020 | 0.0118 | ✅ |
| 14 | 0.0895 | 0.1969 | 0.2228 | 0.2729 | 0.2179 | 0.0888 | 0.1939 | 0.2219 | 0.2586 | 0.2368 | 0.0189 | ✅ |
| 15 | 0.1156 | 0.2239 | 0.2277 | 0.2520 | 0.1808 | 0.1152 | 0.2216 | 0.2264 | 0.2519 | 0.1848 | 0.0040 | ✅ |
| 16 | 0.1358 | 0.2666 | 0.2339 | 0.2404 | 0.1233 | 0.1337 | 0.2655 | 0.2360 | 0.2353 | 0.1295 | 0.0083 | ✅ |
| 17 | 0.1379 | 0.2503 | 0.2400 | 0.2491 | 0.1226 | 0.1364 | 0.2489 | 0.2398 | 0.2354 | 0.1396 | 0.0170 | ✅ |
| 18 | 0.0710 | 0.1443 | 0.1912 | 0.2381 | 0.3554 | 0.0587 | 0.1663 | 0.2109 | 0.2097 | 0.3543 | 0.0417 | ✅ |
| 19 | 0.0647 | 0.1457 | 0.1769 | 0.2058 | 0.4069 | 0.0733 | 0.1110 | 0.1503 | 0.2119 | 0.4536 | 0.0613 | ✅ |

### Padrón 01/01/2022: proporción de extranjeros por provincia

| provincia | sint_extranjera | ref_extranjera | tvd | dentro |
| --- | --- | --- | --- | --- |
| 01 | 0.1260 | 0.0987 | 0.0273 | ✅ |
| 02 | 0.0944 | 0.0714 | 0.0230 | ✅ |
| 03 | 0.2620 | 0.2044 | 0.0576 | ✅ |
| 04 | 0.2549 | 0.2189 | 0.0360 | ✅ |
| 05 | 0.1048 | 0.0663 | 0.0385 | ✅ |
| 06 | 0.0442 | 0.0319 | 0.0123 | ✅ |
| 07 | 0.2165 | 0.1887 | 0.0278 | ✅ |
| 08 | 0.1794 | 0.1548 | 0.0246 | ✅ |
| 09 | 0.1110 | 0.0835 | 0.0275 | ✅ |
| 10 | 0.0533 | 0.0357 | 0.0177 | ✅ |
| 11 | 0.0546 | 0.0419 | 0.0127 | ✅ |
| 12 | 0.1984 | 0.1540 | 0.0444 | ✅ |
| 13 | 0.0739 | 0.0644 | 0.0095 | ✅ |
| 14 | 0.0376 | 0.0279 | 0.0097 | ✅ |
| 15 | 0.0657 | 0.0416 | 0.0241 | ✅ |
| 16 | 0.1411 | 0.1164 | 0.0247 | ✅ |
| 17 | 0.2312 | 0.2046 | 0.0266 | ✅ |
| 18 | 0.1016 | 0.0750 | 0.0266 | ✅ |
| 19 | 0.1919 | 0.1388 | 0.0530 | ✅ |
| 20 | 0.0980 | 0.0847 | 0.0134 | ✅ |
| 21 | 0.1080 | 0.0968 | 0.0113 | ✅ |
| 22 | 0.1652 | 0.1321 | 0.0330 | ✅ |
| 23 | 0.0407 | 0.0283 | 0.0124 | ✅ |
| 24 | 0.0663 | 0.0456 | 0.0207 | ✅ |
| 25 | 0.2115 | 0.1887 | 0.0228 | ✅ |
| 26 | 0.1536 | 0.1305 | 0.0231 | ✅ |
| 27 | 0.0773 | 0.0520 | 0.0253 | ✅ |
| 28 | 0.1670 | 0.1407 | 0.0263 | ✅ |
| 29 | 0.1919 | 0.1673 | 0.0246 | ✅ |
| 30 | 0.1629 | 0.1480 | 0.0149 | ✅ |
| 31 | 0.1352 | 0.1106 | 0.0245 | ✅ |
| 32 | 0.0795 | 0.0543 | 0.0251 | ✅ |
| 33 | 0.0747 | 0.0454 | 0.0293 | ✅ |
| 34 | 0.0712 | 0.0473 | 0.0239 | ✅ |
| 35 | 0.1467 | 0.1265 | 0.0203 | ✅ |
| 36 | 0.0676 | 0.0412 | 0.0265 | ✅ |
| 37 | 0.0757 | 0.0487 | 0.0271 | ✅ |
| 38 | 0.1568 | 0.1389 | 0.0179 | ✅ |
| 39 | 0.0850 | 0.0636 | 0.0215 | ✅ |
| 40 | 0.1446 | 0.1185 | 0.0261 | ✅ |
| 41 | 0.0578 | 0.0411 | 0.0167 | ✅ |
| 42 | 0.1517 | 0.0996 | 0.0521 | ✅ |
| 43 | 0.1965 | 0.1681 | 0.0284 | ✅ |
| 44 | 0.1455 | 0.1161 | 0.0294 | ✅ |
| 45 | 0.1466 | 0.1042 | 0.0423 | ✅ |
| 46 | 0.1653 | 0.1170 | 0.0484 | ✅ |
| 47 | 0.0864 | 0.0568 | 0.0296 | ✅ |
| 48 | 0.1006 | 0.0785 | 0.0221 | ✅ |
| 49 | 0.0703 | 0.0379 | 0.0324 | ✅ |
| 50 | 0.1559 | 0.1235 | 0.0324 | ✅ |
| 51 | 0.0685 | 0.0591 | 0.0094 | ✅ |
| 52 | 0.1317 | 0.1371 | 0.0054 | ✅ |

## V-REPRO

2026-01-01_ES_10000_s1 generado de nuevo en otro directorio: mismos hashes.

- `persons.parquet`: `c5efdeefe6222743eb71018eb34c93864eaa2b716f309765391ceb0a2ed336e6`
- `households.parquet`: `65c9030ee8b5aa64ff499336d5cc64fb23b829bcce7e0224fc658ec2ff84bfee`
- `lineage.parquet`: `2c5e7545c40f079a57818fecc4132e8487bf35d125942d99c09520147d0194ae`
