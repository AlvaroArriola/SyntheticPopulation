# F5 · Anexo por territorio

Generado desde `fase_05_validacion.json` (`python -m sinpop.validate.fase5 --anexo`). Semilla 1. Detalle de cada comprobación en `reports/fase_05/`.

## CCAA:01

- Población `2026-01-01_CCAA_01_100000_s1`: 100.039 personas (pedidas 100.000) de 8.751.219 residentes (1 por 87,5).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 173, mismo_territorio 99.866; 39.831 unidades donantes, Kish 30.460 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0041). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 64 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0285 | 0,0090 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0286 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0075 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0078 | 0,0096 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0214 | 0,0046 | 0,050 | ✅ |
| tamano_municipio | 0,0133 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0303 | 0,0116 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,617 | 0,614 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,015 | 0,018 | 0,002 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,630 | 0,641 | 0,011 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,038 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,065 | 0,067 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,040 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,086 | 0,089 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,054 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,194 | 0,007 | ✅ |

## CCAA:02

- Población `2026-01-01_CCAA_02_100000_s1`: 99.992 personas (pedidas 100.000) de 1.382.035 residentes (1 por 13,8).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.992; 39.252 unidades donantes, Kish 25.784 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0184 | 0,0087 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0012 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0183 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0100 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0140 | 0,0099 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0036 | 0,0027 | 0,050 | ✅ |
| tamano_municipio | 0,0110 | 0,0036 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0283 | 0,0110 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,615 | 0,613 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,022 | 0,016 | 0,005 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,627 | 0,632 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,041 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,627 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,078 | 0,078 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,050 | 0,051 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,125 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,062 | 0,062 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,183 | 0,192 | 0,009 | ✅ |

## CCAA:03

- Población `2026-01-01_CCAA_03_100000_s1`: 100.009 personas (pedidas 100.000) de 1.021.627 residentes (1 por 10,2).
- Donantes: 99,6 % locales; personas por nivel: ccaa_parecidas 418, mismo_territorio 99.591; 37.758 unidades donantes, Kish 23.208 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0193 | 0,0087 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0013 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0286 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0116 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0095 | 0,0087 | 0,050 | ✅ |
| tamano_municipio | 0,0043 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0310 | 0,0100 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,618 | 0,621 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,035 | 0,033 | 0,002 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,623 | 0,631 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,050 | 0,011 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,635 | 0,635 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,088 | 0,088 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,031 | 0,037 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,102 | 0,104 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,069 | 0,070 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,176 | 0,010 | ✅ |

## CCAA:04

- Población `2026-01-01_CCAA_04_100000_s1`: 99.994 personas (pedidas 100.000) de 1.260.336 residentes (1 por 12,6).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.994; 31.275 unidades donantes, Kish 17.352 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0323 | 0,0087 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0003 | 0,0032 | 0,050 | ✅ |
| estado_civil_edad | 0,0318 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0087 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0160 | 0,0112 | 0,050 | ✅ |
| tamano_municipio | 0,0155 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0391 | 0,0118 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,599 | 0,601 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,034 | 0,035 | 0,001 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,614 | 0,624 | 0,010 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,058 | 0,049 | 0,009 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,060 | 0,059 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,046 | 0,047 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,106 | 0,113 | 0,007 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,048 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,161 | 0,001 | ✅ |

## CCAA:05

- Población `2026-01-01_CCAA_05_100000_s1`: 99.977 personas (pedidas 100.000) de 2.276.245 residentes (1 por 22,8).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.977; 37.914 unidades donantes, Kish 26.419 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0038). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0258 | 0,0092 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0373 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0094 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0099 | 0,0103 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0012 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0068 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0468 | 0,0121 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,605 | 0,608 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,009 | 0,011 | 0,002 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,613 | 0,622 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,056 | 0,053 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,057 | 0,055 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,048 | 0,009 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,077 | 0,079 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,043 | 0,043 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,148 | 0,151 | 0,003 | ✅ |

## CCAA:06

- Población `2026-01-01_CCAA_06_100000_s1`: 100.002 personas (pedidas 100.000) de 597.088 residentes (1 por 6,0).
- Donantes: 100,0 % locales; personas por nivel: ccaa_parecidas 15, mismo_territorio 99.987; 22.986 unidades donantes, Kish 13.670 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0018). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0211 | 0,0084 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0013 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0236 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0102 | 0,0111 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0092 | 0,0089 | 0,050 | ✅ |
| tamano_municipio | 0,0059 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0358 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,624 | 0,623 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,017 | 0,016 | 0,001 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,623 | 0,630 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,040 | 0,038 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,633 | 0,633 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,081 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,030 | 0,037 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,095 | 0,098 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,059 | 0,059 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,172 | 0,006 | ✅ |

## CCAA:07

- Población `2026-01-01_CCAA_07_100000_s1`: 100.046 personas (pedidas 100.000) de 2.419.181 residentes (1 por 24,2).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 308, mismo_territorio 99.738; 44.229 unidades donantes, Kish 31.520 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0031). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 71 (todos los niveles); excepciones 1.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0194 | 0,0090 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0009 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0248 | 0,0064 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0077 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0083 | 0,0091 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0121 | 0,0047 | 0,050 | ✅ |
| tamano_municipio | 0,0075 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0249 | 0,0103 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,619 | 0,621 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,040 | 0,002 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,620 | 0,627 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,054 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,632 | 0,632 | 0,001 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,080 | 0,079 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,032 | 0,039 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,111 | 0,111 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,054 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,171 | 0,009 | ✅ |

## CCAA:08

- Población `2026-01-01_CCAA_08_100000_s1`: 100.008 personas (pedidas 100.000) de 2.155.201 residentes (1 por 21,6).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.008; 39.241 unidades donantes, Kish 27.839 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0033). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 43 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0307 | 0,0088 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0009 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0254 | 0,0058 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0102 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0103 | 0,0100 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0153 | 0,0038 | 0,050 | ✅ |
| tamano_municipio | 0,0130 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0265 | 0,0109 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,614 | 0,606 | 0,008 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,024 | 0,021 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,632 | 0,641 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,041 | 0,008 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,001 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,067 | 0,068 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,040 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,104 | 0,104 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,194 | 0,005 | ✅ |

## CCAA:09

- Población `2026-01-01_CCAA_09_100000_s1`: 99.970 personas (pedidas 100.000) de 8.202.041 residentes (1 por 82,0).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.970; 39.749 unidades donantes, Kish 29.988 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0030). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0271 | 0,0087 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0031 | 0,050 | ✅ |
| estado_civil_edad | 0,0294 | 0,0063 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0081 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0140 | 0,0105 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0069 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0217 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0317 | 0,0120 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,611 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,018 | 0,023 | 0,005 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,634 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,042 | 0,036 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,076 | 0,076 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,060 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,127 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,065 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,191 | 0,195 | 0,004 | ✅ |

## CCAA:10

- Población `2026-01-01_CCAA_10_100000_s1`: 100.022 personas (pedidas 100.000) de 5.529.081 residentes (1 por 55,3).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.022; 40.386 unidades donantes, Kish 30.446 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0035). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0297 | 0,0091 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0007 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0256 | 0,0065 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0108 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0129 | 0,0110 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0147 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0216 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0269 | 0,0110 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,607 | 0,606 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,001 | 0,002 | 0,001 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,636 | 0,010 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,030 | 0,013 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,066 | 0,068 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,046 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,117 | 0,122 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,055 | 0,056 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,193 | 0,197 | 0,005 | ✅ |

## CCAA:11

- Población `2026-01-01_CCAA_11_100000_s1`: 100.022 personas (pedidas 100.000) de 1.055.386 residentes (1 por 10,6).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 141, mismo_territorio 99.881; 37.326 unidades donantes, Kish 25.535 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0028). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0238 | 0,0090 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0011 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0292 | 0,0057 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0104 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0061 | 0,0081 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0105 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0106 | 0,0043 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0245 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,623 | 0,617 | 0,006 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,019 | 0,020 | 0,001 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,634 | 0,646 | 0,011 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,055 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,629 | 0,629 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,070 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,037 | 0,010 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,067 | 0,070 | 0,004 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,048 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,196 | 0,205 | 0,008 | ✅ |

## CCAA:12

- Población `2026-01-01_CCAA_12_100000_s1`: 100.033 personas (pedidas 100.000) de 2.728.430 residentes (1 por 27,3).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 343, mismo_territorio 99.690; 41.705 unidades donantes, Kish 30.719 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0030). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0166 | 0,0091 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0016 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0296 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0088 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0058 | 0,0084 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0116 | 0,0037 | 0,050 | ✅ |
| tamano_municipio | 0,0096 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0271 | 0,0107 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,625 | 0,628 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,021 | 0,018 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,622 | 0,628 | 0,006 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,050 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,641 | 0,641 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,082 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,031 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,090 | 0,090 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,064 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,182 | 0,188 | 0,005 | ✅ |

## CCAA:13

- Población `2026-01-01_CCAA_13_100000_s1`: 100.001 personas (pedidas 100.000) de 7.168.876 residentes (1 por 71,7).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.001; 38.912 unidades donantes, Kish 29.450 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0030). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0258 | 0,0084 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0006 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0228 | 0,0063 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0081 | 0,0110 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0106 | 0,0104 | 0,050 | ✅ |
| tamano_municipio | 0,0123 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0350 | 0,0113 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,615 | 0,612 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,018 | 0,002 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,621 | 0,628 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,032 | 0,038 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,074 | 0,074 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,035 | 0,051 | 0,015 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,118 | 0,117 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,064 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,178 | 0,183 | 0,005 | ✅ |

## CCAA:14

- Población `2026-01-01_CCAA_14_100000_s1`: 100.021 personas (pedidas 100.000) de 1.605.913 residentes (1 por 16,1).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.021; 35.100 unidades donantes, Kish 24.414 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0034). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0198 | 0,0088 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0026 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0250 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0064 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0134 | 0,0102 | 0,050 | ✅ |
| tamano_municipio | 0,0094 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0332 | 0,0114 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,608 | 0,607 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,020 | 0,025 | 0,005 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,631 | 0,640 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,044 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,614 | 0,614 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,062 | 0,063 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,077 | 0,015 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,110 | 0,116 | 0,006 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,197 | 0,011 | ✅ |

## CCAA:15

- Población `2026-01-01_CCAA_15_100000_s1`: 100.008 personas (pedidas 100.000) de 690.044 residentes (1 por 6,9).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.008; 24.753 unidades donantes, Kish 14.768 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0242 | 0,0086 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0012 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0128 | 0,0058 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0098 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0127 | 0,0095 | 0,050 | ✅ |
| tamano_municipio | 0,0123 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0358 | 0,0117 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,625 | 0,619 | 0,006 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,013 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,602 | 0,603 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,044 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,630 | 0,630 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,070 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,041 | 0,046 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,108 | 0,113 | 0,004 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,050 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,176 | 0,188 | 0,012 | ✅ |

## CCAA:16

- Población `2026-01-01_CCAA_16_100000_s1`: 100.042 personas (pedidas 100.000) de 2.253.019 residentes (1 por 22,5).
- Donantes: 100,0 % locales; personas por nivel: ccaa_parecidas 16, mismo_territorio 100.026; 42.600 unidades donantes, Kish 30.976 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0271 | 0,0089 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0015 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0245 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0107 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0090 | 0,0092 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0121 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0111 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0346 | 0,0113 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,623 | 0,628 | 0,005 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,010 | 0,005 | 0,005 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,624 | 0,628 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,060 | 0,013 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,645 | 0,645 | 0,001 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,084 | 0,084 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,049 | 0,045 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,121 | 0,121 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,066 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,199 | 0,010 | ✅ |

## CCAA:17

- Población `2026-01-01_CCAA_17_100000_s1`: 99.992 personas (pedidas 100.000) de 329.550 residentes (1 por 3,3).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 145, mismo_territorio 99.847; 13.111 unidades donantes, Kish 7.801 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0018). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0241 | 0,0084 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0196 | 0,0063 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0145 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0155 | 0,0095 | 0,050 | ✅ |
| tamano_municipio | 0,0019 | 0,0036 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0342 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,618 | 0,615 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,036 | 0,005 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,621 | 0,628 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,046 | 0,036 | 0,011 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,624 | 0,624 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,070 | 0,069 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,038 | 0,044 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,116 | 0,121 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,049 | 0,048 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,198 | 0,010 | ✅ |

## CCAA:18

- Población `2026-01-01_CCAA_18_100000_s1`: 99.997 personas (pedidas 100.000) de 84.196 residentes (1 por 0,8).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 319, mismo_territorio 99.678; 2.515 unidades donantes, Kish 1.448 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0008). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 1.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0389 | 0,0096 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0020 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0299 | 0,0057 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0204 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0096 | 0,0072 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0565 | 0,0129 | 0,050 | ❌ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,596 | 0,598 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,087 | 0,090 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,639 | 0,013 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,069 | 0,083 | 0,014 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,054 | 0,054 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,029 | 0,045 | 0,016 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,079 | 0,092 | 0,012 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,040 | 0,040 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,186 | 0,002 | ✅ |

## CCAA:19

- Población `2026-01-01_CCAA_19_100000_s1`: 99.999 personas (pedidas 100.000) de 86.908 residentes (1 por 0,9).
- Donantes: 97,8 % locales; personas por nivel: ccaa_parecidas 2.201, mismo_territorio 97.798; 2.649 unidades donantes, Kish 1.669 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 12 (TVD media 0,0009). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0327 | 0,0091 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0039 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0181 | 0,0057 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0171 | 0,0104 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0201 | 0,0082 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0312 | 0,0134 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,602 | 0,597 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,107 | 0,111 | 0,004 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,627 | 0,635 | 0,008 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,049 | 0,012 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,618 | 0,618 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,067 | 0,044 | 0,023 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,092 | 0,100 | 0,008 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,030 | 0,030 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,185 | 0,003 | ✅ |

## PROV:28

- Población `2026-01-01_PROV_28_50000_s1`: 49.991 personas (pedidas 50.000) de 7.168.876 residentes (1 por 143,4).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 49.991; 19.477 unidades donantes, Kish 14.757 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0046). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0256 | 0,0120 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0005 | 0,0044 | 0,080 | ✅ |
| estado_civil_edad | 0,0238 | 0,0084 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0090 | 0,0154 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0124 | 0,0151 | 0,080 | ✅ |
| tamano_municipio | 0,0107 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0348 | 0,0161 | 0,080 | ✅ |

## PROV:08

- Población `2026-01-01_PROV_08_50000_s1`: 49.974 personas (pedidas 50.000) de 6.008.837 residentes (1 por 120,2).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 49.974; 19.911 unidades donantes, Kish 14.995 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0041). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0255 | 0,0121 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0006 | 0,0045 | 0,080 | ✅ |
| estado_civil_edad | 0,0291 | 0,0086 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0116 | 0,0154 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0158 | 0,0151 | 0,080 | ✅ |
| tamano_municipio | 0,0230 | 0,0060 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0306 | 0,0157 | 0,080 | ✅ |

## PROV:42

- Población `2026-01-01_PROV_42_50000_s1`: 50.009 personas (pedidas 50.000) de 90.824 residentes (1 por 1,8).
- Donantes: 98,9 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 534, mismo_territorio 49.475; 3.814 unidades donantes, Kish 2.147 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0203 | 0,0119 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0043 | 0,080 | ✅ |
| estado_civil_edad | 0,0168 | 0,0086 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0265 | 0,0155 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0267 | 0,0135 | 0,080 | ✅ |
| tamano_municipio | 0,0132 | 0,0049 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0265 | 0,0148 | 0,080 | ✅ |

## PROV:44

- Población `2026-01-01_PROV_44_50000_s1`: 49.995 personas (pedidas 50.000) de 137.173 residentes (1 por 2,7).
- Donantes: 98,1 % locales; personas por nivel: ccaa_parecidas 17, misma_ccaa_mismo_grado_urbanizacion 921, mismo_territorio 49.057; 5.516 unidades donantes, Kish 3.222 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0255 | 0,0123 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0007 | 0,0042 | 0,080 | ✅ |
| estado_civil_edad | 0,0202 | 0,0084 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0133 | 0,0149 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0249 | 0,0132 | 0,080 | ✅ |
| tamano_municipio | 0,0190 | 0,0049 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0286 | 0,0149 | 0,080 | ✅ |

## PROV:04

- Población `2026-01-01_PROV_04_50000_s1`: 50.014 personas (pedidas 50.000) de 782.945 residentes (1 por 15,7).
- Donantes: 99,6 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 191, mismo_territorio 49.823; 18.355 unidades donantes, Kish 11.994 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0048). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0287 | 0,0128 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0012 | 0,0047 | 0,080 | ✅ |
| estado_civil_edad | 0,0229 | 0,0084 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0077 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0184 | 0,0150 | 0,080 | ✅ |
| tamano_municipio | 0,0149 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0323 | 0,0163 | 0,080 | ✅ |

## PROV:35

- Población `2026-01-01_PROV_35_50000_s1`: 50.006 personas (pedidas 50.000) de 1.181.260 residentes (1 por 23,6).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 50.006; 18.854 unidades donantes, Kish 13.131 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0050). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0287 | 0,0127 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0042 | 0,080 | ✅ |
| estado_civil_edad | 0,0384 | 0,0085 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0094 | 0,0153 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0114 | 0,0140 | 0,080 | ✅ |
| tamano_municipio | 0,0072 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0492 | 0,0166 | 0,080 | ✅ |

## PROV:20

- Población `2026-01-01_PROV_20_50000_s1`: 49.981 personas (pedidas 50.000) de 735.369 residentes (1 por 14,7).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 34, misma_ccaa_mismo_grado_urbanizacion 74, mismo_territorio 49.873; 20.314 unidades donantes, Kish 13.775 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0036). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0267 | 0,0124 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0006 | 0,0043 | 0,080 | ✅ |
| estado_civil_edad | 0,0217 | 0,0084 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0116 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0100 | 0,0131 | 0,080 | ✅ |
| tamano_municipio | 0,0137 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0360 | 0,0146 | 0,080 | ✅ |

## PROV:32

- Población `2026-01-01_PROV_32_50000_s1`: 50.010 personas (pedidas 50.000) de 306.524 residentes (1 por 6,1).
- Donantes: 98,8 % locales; personas por nivel: ccaa_parecidas 36, misma_ccaa_mismo_grado_urbanizacion 540, mismo_territorio 49.434; 12.945 unidades donantes, Kish 7.670 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0026). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0220 | 0,0123 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0038 | 0,080 | ✅ |
| estado_civil_edad | 0,0312 | 0,0089 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0165 | 0,0153 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0124 | 0,0123 | 0,080 | ✅ |
| tamano_municipio | 0,0120 | 0,0054 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0210 | 0,0152 | 0,080 | ✅ |

## PROV:51

- Población `2026-01-01_PROV_51_50000_s1`: 50.034 personas (pedidas 50.000) de 84.196 residentes (1 por 1,7).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 156, mismo_territorio 49.878; 2.513 unidades donantes, Kish 1.436 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0012). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0389 | 0,0130 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0023 | 0,0044 | 0,080 | ✅ |
| estado_civil_edad | 0,0294 | 0,0085 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0200 | 0,0149 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0091 | 0,0101 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0566 | 0,0179 | 0,080 | ✅ |

## PROV:52

- Población `2026-01-01_PROV_52_50000_s1`: 49.995 personas (pedidas 50.000) de 86.908 residentes (1 por 1,7).
- Donantes: 97,8 % locales; personas por nivel: ccaa_parecidas 1.103, mismo_territorio 48.892; 2.649 unidades donantes, Kish 1.664 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 12 (TVD media 0,0018). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0316 | 0,0129 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0037 | 0,0047 | 0,080 | ✅ |
| estado_civil_edad | 0,0182 | 0,0080 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0175 | 0,0149 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0203 | 0,0114 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0308 | 0,0190 | 0,080 | ✅ |

## MUNIS:ejemplo_valencia_urbano

- Población `2026-01-01_MUNIS_ejemplo_valencia_urbano_20000_s1`: 19.978 personas (pedidas 20.000) de 1.273.589 residentes (1 por 63,7).
- Donantes: 98,3 % locales; personas por nivel: misma_provincia 339, mismo_territorio 19.639; 8.014 unidades donantes, Kish 6.086 (mínimo 200).
- Confianza esperada: baja.
- V-MARG: 0 fallos de 7 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 2 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0010 | 0,0073 | 0,080 | ✅ |
| tamano_municipio | 0,0234 | 0,0069 | 0,080 | ✅ |

## MUNIS:ejemplo_teruel_rural

- Población `2026-01-01_MUNIS_ejemplo_teruel_rural_20000_s1`: 19.994 personas (pedidas 20.000) de 53.706 residentes (1 por 2,7).
- Donantes: 0,0 % locales; personas por nivel: ccaa_parecidas 6, misma_ccaa_mismo_grado_urbanizacion 79, misma_provincia 19.909; 2.358 unidades donantes, Kish 1.288 (mínimo 200).
- Confianza esperada: baja (reducida: menos del 50 % de donantes locales).
- V-MARG: 0 fallos de 6 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 1 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0024 | 0,0063 | 0,080 | ✅ |
