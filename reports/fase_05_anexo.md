# F5 · Anexo por territorio

Generado desde `fase_05_validacion.json` (`python -m sinpop.validate.fase5 --anexo`). Semilla 1. Detalle de cada comprobación en `reports/fase_05/`.

## CCAA:01

- Población `2026-01-01_CCAA_01_100000_s1`: 99.982 personas (pedidas 100.000) de 8.751.219 residentes (1 por 87,5).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 245, mismo_territorio 99.737; 39.802 unidades donantes, Kish 30.478 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0033). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 64 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0146 | 0,0092 | 0,050 | ✅ |
| actividad_sexo | 0,0074 | 0,0059 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0026 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0099 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0054 | 0,0095 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0188 | 0,0047 | 0,050 | ✅ |
| tamano_municipio | 0,0126 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0167 | 0,0115 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,619 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,251 | 0,248 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,015 | 0,018 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,041 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,065 | 0,066 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,045 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,086 | 0,085 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,187 | 0,000 | ✅ |

## CCAA:02

- Población `2026-01-01_CCAA_02_100000_s1`: 100.014 personas (pedidas 100.000) de 1.382.035 residentes (1 por 13,8).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 197, mismo_territorio 99.817; 37.842 unidades donantes, Kish 23.070 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0089 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0050 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0091 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0096 | 0,0098 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0061 | 0,0027 | 0,050 | ✅ |
| tamano_municipio | 0,0100 | 0,0036 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0163 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,620 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,254 | 0,257 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,022 | 0,019 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,038 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,627 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,078 | 0,078 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,050 | 0,047 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,124 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,062 | 0,063 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,184 | 0,187 | 0,003 | ✅ |

## CCAA:03

- Población `2026-01-01_CCAA_03_100000_s1`: 100.022 personas (pedidas 100.000) de 1.021.627 residentes (1 por 10,2).
- Donantes: 99,4 % locales; personas por nivel: ccaa_parecidas 634, mismo_territorio 99.388; 36.106 unidades donantes, Kish 20.342 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0138 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0087 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0105 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0073 | 0,0087 | 0,050 | ✅ |
| tamano_municipio | 0,0053 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0213 | 0,0102 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,618 | 0,622 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,293 | 0,287 | 0,005 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,035 | 0,032 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,050 | 0,011 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,635 | 0,635 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,088 | 0,090 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,031 | 0,035 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,102 | 0,104 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,069 | 0,070 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,170 | 0,004 | ✅ |

## CCAA:04

- Población `2026-01-01_CCAA_04_100000_s1`: 100.027 personas (pedidas 100.000) de 1.260.336 residentes (1 por 12,6).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 155, mismo_territorio 99.872; 28.562 unidades donantes, Kish 14.480 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0138 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0048 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0020 | 0,0032 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0089 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0080 | 0,0111 | 0,050 | ✅ |
| tamano_municipio | 0,0178 | 0,0039 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0188 | 0,0117 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,603 | 0,609 | 0,006 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,167 | 0,171 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,034 | 0,035 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,058 | 0,051 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,060 | 0,060 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,046 | 0,053 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,106 | 0,106 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,048 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,151 | 0,011 | ✅ |

## CCAA:05

- Población `2026-01-01_CCAA_05_100000_s1`: 99.959 personas (pedidas 100.000) de 2.276.245 residentes (1 por 22,8).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 108, mismo_territorio 99.851; 36.689 unidades donantes, Kish 24.187 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0031). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0165 | 0,0091 | 0,050 | ✅ |
| actividad_sexo | 0,0096 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0025 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0091 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0061 | 0,0101 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0008 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0061 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0168 | 0,0117 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,606 | 0,613 | 0,006 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,206 | 0,185 | 0,021 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,009 | 0,009 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,056 | 0,054 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,057 | 0,055 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,041 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,077 | 0,077 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,043 | 0,043 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,146 | 0,145 | 0,001 | ✅ |

## CCAA:06

- Población `2026-01-01_CCAA_06_100000_s1`: 100.006 personas (pedidas 100.000) de 597.088 residentes (1 por 6,0).
- Donantes: 99,5 % locales; personas por nivel: ccaa_parecidas 458, mismo_territorio 99.548; 21.952 unidades donantes, Kish 11.991 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0016). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0105 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0054 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0126 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0073 | 0,0089 | 0,050 | ✅ |
| tamano_municipio | 0,0058 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0178 | 0,0105 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,623 | 0,627 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,254 | 0,011 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,017 | 0,014 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,040 | 0,036 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,633 | 0,633 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,082 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,030 | 0,035 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,095 | 0,098 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,059 | 0,059 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,168 | 0,002 | ✅ |

## CCAA:07

- Población `2026-01-01_CCAA_07_100000_s1`: 99.973 personas (pedidas 100.000) de 2.419.181 residentes (1 por 24,2).
- Donantes: 99,2 % locales; personas por nivel: ccaa_parecidas 769, espana 19, mismo_territorio 99.185; 43.649 unidades donantes, Kish 30.517 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 71 (todos los niveles); excepciones 1.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0115 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0043 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0096 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0069 | 0,0088 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0124 | 0,0050 | 0,050 | ✅ |
| tamano_municipio | 0,0092 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0167 | 0,0100 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,625 | 0,005 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,278 | 0,273 | 0,005 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,040 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,054 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,632 | 0,632 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,080 | 0,079 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,032 | 0,041 | 0,009 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,111 | 0,110 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,054 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,165 | 0,003 | ✅ |

## CCAA:08

- Población `2026-01-01_CCAA_08_100000_s1`: 100.005 personas (pedidas 100.000) de 2.155.201 residentes (1 por 21,6).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 126, mismo_territorio 99.879; 38.228 unidades donantes, Kish 25.948 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 43 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0102 | 0,0091 | 0,050 | ✅ |
| actividad_sexo | 0,0038 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0032 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0096 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0075 | 0,0100 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0204 | 0,0040 | 0,050 | ✅ |
| tamano_municipio | 0,0140 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0152 | 0,0112 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,618 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,302 | 0,310 | 0,008 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,024 | 0,021 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,043 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,067 | 0,067 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,040 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,104 | 0,104 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,050 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,188 | 0,002 | ✅ |

## CCAA:09

- Población `2026-01-01_CCAA_09_100000_s1`: 99.991 personas (pedidas 100.000) de 8.202.041 residentes (1 por 82,0).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.991; 39.684 unidades donantes, Kish 29.873 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0134 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0082 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0024 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0101 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0086 | 0,0107 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0071 | 0,0030 | 0,050 | ✅ |
| tamano_municipio | 0,0238 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0185 | 0,0117 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,620 | 0,007 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,174 | 0,171 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,018 | 0,022 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,042 | 0,040 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,076 | 0,075 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,064 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,125 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,064 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,191 | 0,188 | 0,004 | ✅ |

## CCAA:10

- Población `2026-01-01_CCAA_10_100000_s1`: 99.998 personas (pedidas 100.000) de 5.529.081 residentes (1 por 55,3).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 1.073, mismo_territorio 98.925; 40.355 unidades donantes, Kish 30.477 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0164 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0108 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0031 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0080 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0085 | 0,0112 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0129 | 0,0032 | 0,050 | ✅ |
| tamano_municipio | 0,0230 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0141 | 0,0109 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,614 | 0,614 | 0,000 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,222 | 0,225 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,001 | 0,001 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,035 | 0,009 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,066 | 0,067 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,049 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,117 | 0,117 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,055 | 0,055 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,193 | 0,188 | 0,005 | ✅ |

## CCAA:11

- Población `2026-01-01_CCAA_11_100000_s1`: 100.029 personas (pedidas 100.000) de 1.055.386 residentes (1 por 10,6).
- Donantes: 99,5 % locales; personas por nivel: ccaa_parecidas 473, mismo_territorio 99.556; 35.318 unidades donantes, Kish 22.427 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0106 | 0,0093 | 0,050 | ✅ |
| actividad_sexo | 0,0050 | 0,0059 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0095 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0054 | 0,0080 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0124 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0124 | 0,0043 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0203 | 0,0107 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,623 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,284 | 0,282 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,019 | 0,017 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,056 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,629 | 0,629 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,071 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,038 | 0,010 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,067 | 0,068 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,047 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,196 | 0,198 | 0,002 | ✅ |

## CCAA:12

- Población `2026-01-01_CCAA_12_100000_s1`: 99.998 personas (pedidas 100.000) de 2.728.430 residentes (1 por 27,3).
- Donantes: 99,2 % locales; personas por nivel: ccaa_parecidas 791, mismo_territorio 99.207; 41.239 unidades donantes, Kish 29.847 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0131 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0058 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0071 | 0,0110 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0053 | 0,0086 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0099 | 0,0037 | 0,050 | ✅ |
| tamano_municipio | 0,0100 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0150 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,622 | 0,626 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,198 | 0,202 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,021 | 0,019 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,053 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,641 | 0,641 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,080 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,028 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,090 | 0,090 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,064 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,181 | 0,181 | 0,000 | ✅ |

## CCAA:13

- Población `2026-01-01_CCAA_13_100000_s1`: 100.008 personas (pedidas 100.000) de 7.168.876 residentes (1 por 71,7).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.008; 38.805 unidades donantes, Kish 29.291 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0100 | 0,0086 | 0,050 | ✅ |
| actividad_sexo | 0,0024 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0012 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0101 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0073 | 0,0103 | 0,050 | ✅ |
| tamano_municipio | 0,0154 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0160 | 0,0114 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,618 | 0,622 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,195 | 0,194 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,016 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,032 | 0,041 | 0,009 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,074 | 0,075 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,035 | 0,051 | 0,016 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,118 | 0,118 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,064 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,180 | 0,178 | 0,001 | ✅ |

## CCAA:14

- Población `2026-01-01_CCAA_14_100000_s1`: 99.991 personas (pedidas 100.000) de 1.605.913 residentes (1 por 16,1).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 262, mismo_territorio 99.729; 33.342 unidades donantes, Kish 21.222 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0028). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0086 | 0,0092 | 0,050 | ✅ |
| actividad_sexo | 0,0051 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0031 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0066 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0156 | 0,0102 | 0,050 | ✅ |
| tamano_municipio | 0,0107 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0153 | 0,0120 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,606 | 0,610 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,228 | 0,219 | 0,008 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,020 | 0,027 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,042 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,614 | 0,614 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,062 | 0,061 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,089 | 0,027 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,110 | 0,111 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,191 | 0,004 | ✅ |

## CCAA:15

- Población `2026-01-01_CCAA_15_100000_s1`: 99.977 personas (pedidas 100.000) de 690.044 residentes (1 por 6,9).
- Donantes: 100,0 % locales; personas por nivel: ccaa_parecidas 44, mismo_territorio 99.933; 23.141 unidades donantes, Kish 11.888 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0122 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0054 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0103 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0106 | 0,0097 | 0,050 | ✅ |
| tamano_municipio | 0,0123 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0241 | 0,0109 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,623 | 0,627 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,220 | 0,210 | 0,010 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,014 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,044 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,630 | 0,630 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,072 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,041 | 0,050 | 0,008 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,108 | 0,109 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,053 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,177 | 0,189 | 0,012 | ✅ |

## CCAA:16

- Población `2026-01-01_CCAA_16_100000_s1`: 100.007 personas (pedidas 100.000) de 2.253.019 residentes (1 por 22,5).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 107, mismo_territorio 99.900; 41.608 unidades donantes, Kish 28.923 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0232 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0070 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0112 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0058 | 0,0090 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0113 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0136 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0195 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,621 | 0,631 | 0,010 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,224 | 0,224 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,010 | 0,006 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,064 | 0,016 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,645 | 0,645 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,084 | 0,083 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,049 | 0,050 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,121 | 0,121 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,065 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,193 | 0,003 | ✅ |

## CCAA:17

- Población `2026-01-01_CCAA_17_100000_s1`: 100.013 personas (pedidas 100.000) de 329.550 residentes (1 por 3,3).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 237, mismo_territorio 99.776; 12.933 unidades donantes, Kish 6.706 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0013). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0085 | 0,0085 | 0,050 | ✅ |
| actividad_sexo | 0,0040 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0144 | 0,0110 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0128 | 0,0095 | 0,050 | ✅ |
| tamano_municipio | 0,0022 | 0,0036 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0205 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,621 | 0,625 | 0,005 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,234 | 0,224 | 0,009 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,038 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,046 | 0,039 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,624 | 0,623 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,070 | 0,070 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,038 | 0,049 | 0,011 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,116 | 0,118 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,049 | 0,049 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,194 | 0,005 | ✅ |

## CCAA:18

- Población `2026-01-01_CCAA_18_100000_s1`: 99.992 personas (pedidas 100.000) de 84.196 residentes (1 por 0,8).
- Donantes: 99,4 % locales; personas por nivel: ccaa_parecidas 552, mismo_territorio 99.440; 2.521 unidades donantes, Kish 1.075 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0007). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0317 | 0,0095 | 0,050 | ✅ |
| actividad_sexo | 0,0059 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0183 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0105 | 0,0073 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0399 | 0,0132 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,594 | 0,605 | 0,011 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,263 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,087 | 0,091 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,069 | 0,082 | 0,012 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,054 | 0,054 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,029 | 0,034 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,079 | 0,084 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,040 | 0,040 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,172 | 0,016 | ✅ |

## CCAA:19

- Población `2026-01-01_CCAA_19_100000_s1`: 100.011 personas (pedidas 100.000) de 86.908 residentes (1 por 0,9).
- Donantes: 97,9 % locales; personas por nivel: ccaa_parecidas 2.123, mismo_territorio 97.888; 2.651 unidades donantes, Kish 1.264 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0007). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0188 | 0,0095 | 0,050 | ✅ |
| actividad_sexo | 0,0051 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0051 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0198 | 0,0105 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0327 | 0,0081 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0266 | 0,0129 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,601 | 0,604 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,231 | 0,219 | 0,012 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,107 | 0,112 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,044 | 0,017 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,618 | 0,618 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,067 | 0,062 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,092 | 0,115 | 0,023 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,030 | 0,030 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,192 | 0,002 | ✅ |

## PROV:28

- Población `2026-01-01_PROV_28_50000_s1`: 49.993 personas (pedidas 50.000) de 7.168.876 residentes (1 por 143,4).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 49.993; 19.462 unidades donantes, Kish 14.721 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0036). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0107 | 0,0127 | 0,080 | ✅ |
| actividad_sexo | 0,0035 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0013 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0101 | 0,0156 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0088 | 0,0147 | 0,080 | ✅ |
| tamano_municipio | 0,0141 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0190 | 0,0170 | 0,080 | ✅ |

## PROV:08

- Población `2026-01-01_PROV_08_50000_s1`: 49.975 personas (pedidas 50.000) de 6.008.837 residentes (1 por 120,2).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 49.975; 19.851 unidades donantes, Kish 15.011 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0031). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0144 | 0,0123 | 0,080 | ✅ |
| actividad_sexo | 0,0087 | 0,0076 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0045 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0111 | 0,0155 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0107 | 0,0153 | 0,080 | ✅ |
| tamano_municipio | 0,0252 | 0,0059 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0220 | 0,0161 | 0,080 | ✅ |

## PROV:42

- Población `2026-01-01_PROV_42_50000_s1`: 49.999 personas (pedidas 50.000) de 90.824 residentes (1 por 1,8).
- Donantes: 97,9 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 1.072, mismo_territorio 48.927; 3.832 unidades donantes, Kish 1.892 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0230 | 0,0120 | 0,080 | ✅ |
| actividad_sexo | 0,0099 | 0,0076 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0027 | 0,0043 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0276 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0296 | 0,0135 | 0,080 | ✅ |
| tamano_municipio | 0,0133 | 0,0048 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0331 | 0,0153 | 0,080 | ✅ |

## PROV:44

- Población `2026-01-01_PROV_44_50000_s1`: 49.990 personas (pedidas 50.000) de 137.173 residentes (1 por 2,7).
- Donantes: 97,5 % locales; personas por nivel: ccaa_parecidas 103, misma_ccaa_mismo_grado_urbanizacion 1.122, mismo_territorio 48.765; 5.454 unidades donantes, Kish 2.502 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0016). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0160 | 0,0129 | 0,080 | ✅ |
| actividad_sexo | 0,0064 | 0,0078 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0026 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0161 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0221 | 0,0136 | 0,080 | ✅ |
| tamano_municipio | 0,0157 | 0,0049 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0280 | 0,0151 | 0,080 | ✅ |

## PROV:04

- Población `2026-01-01_PROV_04_50000_s1`: 50.008 personas (pedidas 50.000) de 782.945 residentes (1 por 15,7).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 211, misma_ccaa_mismo_grado_urbanizacion 363, mismo_territorio 49.434; 17.310 unidades donantes, Kish 10.203 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0041). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0140 | 0,0125 | 0,080 | ✅ |
| actividad_sexo | 0,0053 | 0,0080 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0047 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0076 | 0,0149 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0104 | 0,0149 | 0,080 | ✅ |
| tamano_municipio | 0,0158 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0162 | 0,0161 | 0,080 | ✅ |

## PROV:35

- Población `2026-01-01_PROV_35_50000_s1`: 49.991 personas (pedidas 50.000) de 1.181.260 residentes (1 por 23,6).
- Donantes: 100,0 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 11, mismo_territorio 49.980; 18.196 unidades donantes, Kish 12.032 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0037). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0165 | 0,0136 | 0,080 | ✅ |
| actividad_sexo | 0,0088 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0027 | 0,0042 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0109 | 0,0155 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0084 | 0,0141 | 0,080 | ✅ |
| tamano_municipio | 0,0052 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0175 | 0,0167 | 0,080 | ✅ |

## PROV:20

- Población `2026-01-01_PROV_20_50000_s1`: 50.024 personas (pedidas 50.000) de 735.369 residentes (1 por 14,7).
- Donantes: 99,0 % locales; personas por nivel: ccaa_parecidas 258, misma_ccaa_mismo_grado_urbanizacion 227, mismo_territorio 49.539; 19.387 unidades donantes, Kish 11.974 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0032). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0231 | 0,0121 | 0,080 | ✅ |
| actividad_sexo | 0,0085 | 0,0076 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0011 | 0,0043 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0130 | 0,0150 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0093 | 0,0129 | 0,080 | ✅ |
| tamano_municipio | 0,0204 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0189 | 0,0151 | 0,080 | ✅ |

## PROV:32

- Población `2026-01-01_PROV_32_50000_s1`: 49.999 personas (pedidas 50.000) de 306.524 residentes (1 por 6,1).
- Donantes: 98,1 % locales; personas por nivel: ccaa_parecidas 565, misma_ccaa_mismo_grado_urbanizacion 405, mismo_territorio 49.029; 12.408 unidades donantes, Kish 6.779 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0182 | 0,0127 | 0,080 | ✅ |
| actividad_sexo | 0,0080 | 0,0082 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0022 | 0,0038 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0152 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0127 | 0,0123 | 0,080 | ✅ |
| tamano_municipio | 0,0124 | 0,0054 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0140 | 0,0142 | 0,080 | ✅ |

## PROV:51

- Población `2026-01-01_PROV_51_50000_s1`: 49.991 personas (pedidas 50.000) de 84.196 residentes (1 por 1,7).
- Donantes: 99,4 % locales; personas por nivel: ccaa_parecidas 278, mismo_territorio 49.713; 2.521 unidades donantes, Kish 1.071 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0011). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0310 | 0,0131 | 0,080 | ✅ |
| actividad_sexo | 0,0059 | 0,0082 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0183 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0108 | 0,0103 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0400 | 0,0186 | 0,080 | ✅ |

## PROV:52

- Población `2026-01-01_PROV_52_50000_s1`: 50.005 personas (pedidas 50.000) de 86.908 residentes (1 por 1,7).
- Donantes: 97,9 % locales; personas por nivel: ccaa_parecidas 1.064, mismo_territorio 48.941; 2.647 unidades donantes, Kish 1.257 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0013). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0189 | 0,0130 | 0,080 | ✅ |
| actividad_sexo | 0,0054 | 0,0081 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0053 | 0,0045 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0199 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0329 | 0,0114 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0263 | 0,0194 | 0,080 | ✅ |

## MUNIS:ejemplo_valencia_urbano

- Población `2026-01-01_MUNIS_ejemplo_valencia_urbano_20000_s1`: 19.990 personas (pedidas 20.000) de 1.273.589 residentes (1 por 63,7).
- Donantes: 98,4 % locales; personas por nivel: misma_provincia 324, mismo_territorio 19.666; 8.096 unidades donantes, Kish 6.201 (mínimo 200).
- Confianza esperada: baja.
- V-MARG: 0 fallos de 7 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 2 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0008 | 0,0073 | 0,080 | ✅ |
| tamano_municipio | 0,0244 | 0,0068 | 0,080 | ✅ |

## MUNIS:ejemplo_teruel_rural

- Población `2026-01-01_MUNIS_ejemplo_teruel_rural_20000_s1`: 19.999 personas (pedidas 20.000) de 53.706 residentes (1 por 2,7).
- Donantes: 0,0 % locales; personas por nivel: ccaa_parecidas 6, misma_ccaa_mismo_grado_urbanizacion 93, misma_provincia 19.900; 2.348 unidades donantes, Kish 1.167 (mínimo 200).
- Confianza esperada: baja (reducida: menos del 50 % de donantes locales).
- V-MARG: 0 fallos de 6 (TVD media 0,0015). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 1 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0026 | 0,0066 | 0,080 | ✅ |
