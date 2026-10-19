# F5 · Anexo por territorio

Generado desde `fase_05_validacion.json` (`python -m sinpop.validate.fase5 --anexo`). Semilla 1. Detalle de cada comprobación en `reports/fase_05/`.

## CCAA:01

- Población `2026-01-01_CCAA_01_100000_s1`: 99.978 personas (pedidas 100.000) de 8.751.219 residentes (1 por 87,5).
- Donantes: 99,6 % locales; personas por nivel: ccaa_parecidas 388, mismo_territorio 99.590; 39.790 unidades donantes, Kish 30.451 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0033). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 64 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0130 | 0,0092 | 0,050 | ✅ |
| actividad_sexo | 0,0069 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0102 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0056 | 0,0096 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0174 | 0,0047 | 0,050 | ✅ |
| tamano_municipio | 0,0115 | 0,0044 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0158 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,612 | 0,615 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,251 | 0,249 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,015 | 0,018 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,034 | 0,009 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,065 | 0,066 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,045 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,086 | 0,085 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,189 | 0,001 | ✅ |

## CCAA:02

- Población `2026-01-01_CCAA_02_100000_s1`: 100.019 personas (pedidas 100.000) de 1.382.035 residentes (1 por 13,8).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 196, mismo_territorio 99.823; 37.892 unidades donantes, Kish 23.096 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0086 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0047 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0008 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0095 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0093 | 0,0099 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0069 | 0,0027 | 0,050 | ✅ |
| tamano_municipio | 0,0102 | 0,0036 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0155 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,614 | 0,618 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,253 | 0,257 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,022 | 0,021 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,036 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,627 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,078 | 0,079 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,050 | 0,047 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,124 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,062 | 0,063 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,184 | 0,187 | 0,004 | ✅ |

## CCAA:03

- Población `2026-01-01_CCAA_03_100000_s1`: 99.998 personas (pedidas 100.000) de 1.021.627 residentes (1 por 10,2).
- Donantes: 99,3 % locales; personas por nivel: ccaa_parecidas 711, mismo_territorio 99.287; 36.139 unidades donantes, Kish 20.231 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0126 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0085 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0016 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0121 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0073 | 0,0087 | 0,050 | ✅ |
| tamano_municipio | 0,0055 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0214 | 0,0102 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,617 | 0,001 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,292 | 0,289 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,035 | 0,033 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,051 | 0,012 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,635 | 0,634 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,088 | 0,088 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,031 | 0,038 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,102 | 0,103 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,069 | 0,070 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,170 | 0,004 | ✅ |

## CCAA:04

- Población `2026-01-01_CCAA_04_100000_s1`: 100.025 personas (pedidas 100.000) de 1.260.336 residentes (1 por 12,6).
- Donantes: 99,6 % locales; personas por nivel: ccaa_parecidas 357, mismo_territorio 99.668; 28.643 unidades donantes, Kish 14.475 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0086 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0045 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0032 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0072 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0074 | 0,0112 | 0,050 | ✅ |
| tamano_municipio | 0,0176 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0199 | 0,0119 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,601 | 0,601 | 0,000 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,167 | 0,170 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,034 | 0,037 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,058 | 0,051 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,060 | 0,061 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,046 | 0,053 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,106 | 0,107 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,049 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,152 | 0,011 | ✅ |

## CCAA:05

- Población `2026-01-01_CCAA_05_100000_s1`: 99.966 personas (pedidas 100.000) de 2.276.245 residentes (1 por 22,8).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 265, mismo_territorio 99.701; 36.701 unidades donantes, Kish 24.432 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0130 | 0,0095 | 0,050 | ✅ |
| actividad_sexo | 0,0092 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0022 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0096 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0068 | 0,0103 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0001 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0068 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0167 | 0,0117 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,605 | 0,609 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,206 | 0,187 | 0,019 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,009 | 0,012 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,056 | 0,056 | 0,000 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,057 | 0,058 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,041 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,077 | 0,077 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,043 | 0,045 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,146 | 0,145 | 0,001 | ✅ |

## CCAA:06

- Población `2026-01-01_CCAA_06_100000_s1`: 99.992 personas (pedidas 100.000) de 597.088 residentes (1 por 6,0).
- Donantes: 99,5 % locales; personas por nivel: ccaa_parecidas 524, mismo_territorio 99.468; 21.971 unidades donantes, Kish 11.968 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0017). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0092 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0051 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0126 | 0,0110 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0078 | 0,0092 | 0,050 | ✅ |
| tamano_municipio | 0,0058 | 0,0039 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0191 | 0,0107 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,621 | 0,623 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,255 | 0,010 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,017 | 0,015 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,040 | 0,036 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,633 | 0,632 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,081 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,030 | 0,035 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,095 | 0,099 | 0,004 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,059 | 0,059 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,169 | 0,003 | ✅ |

## CCAA:07

- Población `2026-01-01_CCAA_07_100000_s1`: 99.998 personas (pedidas 100.000) de 2.419.181 residentes (1 por 24,2).
- Donantes: 99,2 % locales; personas por nivel: ccaa_parecidas 760, espana 15, mismo_territorio 99.223; 43.551 unidades donantes, Kish 30.321 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 71 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0115 | 0,0086 | 0,050 | ✅ |
| actividad_sexo | 0,0070 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0008 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0084 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0066 | 0,0089 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0122 | 0,0049 | 0,050 | ✅ |
| tamano_municipio | 0,0091 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0165 | 0,0100 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,619 | 0,619 | 0,001 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,277 | 0,264 | 0,014 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,041 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,054 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,632 | 0,632 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,080 | 0,080 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,032 | 0,042 | 0,010 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,111 | 0,110 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,166 | 0,004 | ✅ |

## CCAA:08

- Población `2026-01-01_CCAA_08_100000_s1`: 100.008 personas (pedidas 100.000) de 2.155.201 residentes (1 por 21,6).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 207, mismo_territorio 99.801; 38.176 unidades donantes, Kish 25.928 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 43 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0087 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0045 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0097 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0084 | 0,0100 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0196 | 0,0038 | 0,050 | ✅ |
| tamano_municipio | 0,0132 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0150 | 0,0112 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,611 | 0,613 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,302 | 0,311 | 0,009 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,024 | 0,021 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,043 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,621 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,067 | 0,067 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,040 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,104 | 0,103 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,053 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,189 | 0,001 | ✅ |

## CCAA:09

- Población `2026-01-01_CCAA_09_100000_s1`: 99.978 personas (pedidas 100.000) de 8.202.041 residentes (1 por 82,0).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.978; 39.675 unidades donantes, Kish 29.790 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0118 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0081 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0031 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0074 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0090 | 0,0104 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0062 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0242 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0201 | 0,0115 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,609 | 0,612 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,174 | 0,171 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,018 | 0,021 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,042 | 0,037 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,076 | 0,078 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,065 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,125 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,065 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,191 | 0,188 | 0,004 | ✅ |

## CCAA:10

- Población `2026-01-01_CCAA_10_100000_s1`: 99.999 personas (pedidas 100.000) de 5.529.081 residentes (1 por 55,3).
- Donantes: 98,7 % locales; personas por nivel: ccaa_parecidas 1.293, mismo_territorio 98.706; 40.434 unidades donantes, Kish 30.584 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0156 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0107 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0012 | 0,0032 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0092 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0080 | 0,0110 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0142 | 0,0032 | 0,050 | ✅ |
| tamano_municipio | 0,0223 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0138 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,611 | 0,610 | 0,001 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,222 | 0,223 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,001 | 0,002 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,033 | 0,010 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,066 | 0,068 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,050 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,117 | 0,117 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,055 | 0,056 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,193 | 0,189 | 0,004 | ✅ |

## CCAA:11

- Población `2026-01-01_CCAA_11_100000_s1`: 99.967 personas (pedidas 100.000) de 1.055.386 residentes (1 por 10,6).
- Donantes: 99,6 % locales; personas por nivel: ccaa_parecidas 439, mismo_territorio 99.528; 35.215 unidades donantes, Kish 22.229 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0106 | 0,0091 | 0,050 | ✅ |
| actividad_sexo | 0,0058 | 0,0059 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0008 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0101 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0056 | 0,0084 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0110 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0122 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0199 | 0,0107 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,618 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,285 | 0,282 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,019 | 0,018 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,054 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,629 | 0,629 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,072 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,037 | 0,010 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,067 | 0,068 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,048 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,196 | 0,198 | 0,002 | ✅ |

## CCAA:12

- Población `2026-01-01_CCAA_12_100000_s1`: 99.977 personas (pedidas 100.000) de 2.728.430 residentes (1 por 27,3).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 1.107, mismo_territorio 98.870; 41.280 unidades donantes, Kish 29.867 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0133 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0058 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0009 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0096 | 0,0104 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0046 | 0,0087 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0109 | 0,0038 | 0,050 | ✅ |
| tamano_municipio | 0,0115 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0153 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,623 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,198 | 0,200 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,021 | 0,021 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,053 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,641 | 0,641 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,081 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,029 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,090 | 0,090 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,065 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,181 | 0,181 | 0,000 | ✅ |

## CCAA:13

- Población `2026-01-01_CCAA_13_100000_s1`: 99.971 personas (pedidas 100.000) de 7.168.876 residentes (1 por 71,7).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 97, mismo_territorio 99.874; 38.821 unidades donantes, Kish 29.304 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0122 | 0,0085 | 0,050 | ✅ |
| actividad_sexo | 0,0065 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0007 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0082 | 0,0111 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0059 | 0,0104 | 0,050 | ✅ |
| tamano_municipio | 0,0169 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0169 | 0,0113 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,615 | 0,616 | 0,001 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,195 | 0,181 | 0,014 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,018 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,032 | 0,036 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,074 | 0,075 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,035 | 0,050 | 0,014 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,118 | 0,119 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,065 | 0,002 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,180 | 0,178 | 0,002 | ✅ |

## CCAA:14

- Población `2026-01-01_CCAA_14_100000_s1`: 100.021 personas (pedidas 100.000) de 1.605.913 residentes (1 por 16,1).
- Donantes: 99,6 % locales; personas por nivel: ccaa_parecidas 357, mismo_territorio 99.664; 33.205 unidades donantes, Kish 21.009 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0077 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0048 | 0,0059 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0090 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0153 | 0,0102 | 0,050 | ✅ |
| tamano_municipio | 0,0102 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0145 | 0,0121 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,604 | 0,607 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,229 | 0,221 | 0,008 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,020 | 0,025 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,041 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,614 | 0,614 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,062 | 0,063 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,090 | 0,028 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,110 | 0,110 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,191 | 0,004 | ✅ |

## CCAA:15

- Población `2026-01-01_CCAA_15_100000_s1`: 100.033 personas (pedidas 100.000) de 690.044 residentes (1 por 6,9).
- Donantes: 100,0 % locales; personas por nivel: ccaa_parecidas 46, mismo_territorio 99.987; 22.955 unidades donantes, Kish 11.550 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0017). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0104 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0055 | 0,0058 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0012 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0113 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0107 | 0,0096 | 0,050 | ✅ |
| tamano_municipio | 0,0118 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0234 | 0,0112 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,621 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,220 | 0,209 | 0,011 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,014 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,044 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,630 | 0,630 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,071 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,041 | 0,051 | 0,010 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,108 | 0,110 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,177 | 0,189 | 0,012 | ✅ |

## CCAA:16

- Población `2026-01-01_CCAA_16_100000_s1`: 99.987 personas (pedidas 100.000) de 2.253.019 residentes (1 por 22,5).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 109, mismo_territorio 99.878; 41.553 unidades donantes, Kish 28.828 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0256 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0111 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0109 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0053 | 0,0093 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0113 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0126 | 0,0039 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0193 | 0,0107 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,617 | 0,625 | 0,007 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,225 | 0,220 | 0,005 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,010 | 0,004 | 0,006 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,064 | 0,016 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,645 | 0,646 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,084 | 0,084 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,049 | 0,052 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,121 | 0,121 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,066 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,192 | 0,002 | ✅ |

## CCAA:17

- Población `2026-01-01_CCAA_17_100000_s1`: 100.011 personas (pedidas 100.000) de 329.550 residentes (1 por 3,3).
- Donantes: 99,5 % locales; personas por nivel: ccaa_parecidas 478, mismo_territorio 99.533; 12.962 unidades donantes, Kish 6.775 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0015). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0083 | 0,0085 | 0,050 | ✅ |
| actividad_sexo | 0,0037 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0158 | 0,0111 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0122 | 0,0096 | 0,050 | ✅ |
| tamano_municipio | 0,0020 | 0,0036 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0206 | 0,0101 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,619 | 0,622 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,233 | 0,224 | 0,009 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,037 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,046 | 0,038 | 0,008 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,624 | 0,623 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,070 | 0,069 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,038 | 0,051 | 0,012 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,116 | 0,119 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,049 | 0,048 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,195 | 0,005 | ✅ |

## CCAA:18

- Población `2026-01-01_CCAA_18_100000_s1`: 100.001 personas (pedidas 100.000) de 84.196 residentes (1 por 0,8).
- Donantes: 99,4 % locales; personas por nivel: ccaa_parecidas 574, mismo_territorio 99.427; 2.524 unidades donantes, Kish 990 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0008). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0218 | 0,0092 | 0,050 | ✅ |
| actividad_sexo | 0,0068 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0006 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0214 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0093 | 0,0072 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0417 | 0,0132 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,589 | 0,593 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,262 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,087 | 0,090 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,069 | 0,093 | 0,024 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,054 | 0,053 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,029 | 0,032 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,079 | 0,084 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,040 | 0,040 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,167 | 0,020 | ✅ |

## CCAA:19

- Población `2026-01-01_CCAA_19_100000_s1`: 100.009 personas (pedidas 100.000) de 86.908 residentes (1 por 0,9).
- Donantes: 97,9 % locales; personas por nivel: ccaa_parecidas 2.097, mismo_territorio 97.912; 2.651 unidades donantes, Kish 1.245 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0008). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0179 | 0,0094 | 0,050 | ✅ |
| actividad_sexo | 0,0050 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0046 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0196 | 0,0104 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0318 | 0,0082 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0263 | 0,0132 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,596 | 0,599 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,231 | 0,218 | 0,013 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,107 | 0,112 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,046 | 0,015 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,618 | 0,618 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,067 | 0,061 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,092 | 0,117 | 0,024 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,030 | 0,030 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,192 | 0,002 | ✅ |

## PROV:28

- Población `2026-01-01_PROV_28_50000_s1`: 49.997 personas (pedidas 50.000) de 7.168.876 residentes (1 por 143,4).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 41, mismo_territorio 49.956; 19.451 unidades donantes, Kish 14.743 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0035). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0128 | 0,0124 | 0,080 | ✅ |
| actividad_sexo | 0,0067 | 0,0078 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0007 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0089 | 0,0156 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0066 | 0,0151 | 0,080 | ✅ |
| tamano_municipio | 0,0156 | 0,0055 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0177 | 0,0165 | 0,080 | ✅ |

## PROV:08

- Población `2026-01-01_PROV_08_50000_s1`: 49.989 personas (pedidas 50.000) de 6.008.837 residentes (1 por 120,2).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 10, misma_ccaa_mismo_grado_urbanizacion 30, mismo_territorio 49.949; 19.892 unidades donantes, Kish 15.055 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0030). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0118 | 0,0123 | 0,080 | ✅ |
| actividad_sexo | 0,0087 | 0,0073 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0022 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0129 | 0,0155 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0102 | 0,0154 | 0,080 | ✅ |
| tamano_municipio | 0,0248 | 0,0060 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0252 | 0,0162 | 0,080 | ✅ |

## PROV:42

- Población `2026-01-01_PROV_42_50000_s1`: 50.008 personas (pedidas 50.000) de 90.824 residentes (1 por 1,8).
- Donantes: 97,5 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 1.234, mismo_territorio 48.774; 3.834 unidades donantes, Kish 1.783 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0017). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0199 | 0,0124 | 0,080 | ✅ |
| actividad_sexo | 0,0074 | 0,0078 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0027 | 0,0043 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0271 | 0,0154 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0311 | 0,0135 | 0,080 | ✅ |
| tamano_municipio | 0,0142 | 0,0048 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0343 | 0,0147 | 0,080 | ✅ |

## PROV:44

- Población `2026-01-01_PROV_44_50000_s1`: 50.016 personas (pedidas 50.000) de 137.173 residentes (1 por 2,7).
- Donantes: 99,5 % locales; personas por nivel: ccaa_parecidas 14, misma_ccaa_mismo_grado_urbanizacion 248, mismo_territorio 49.754; 5.487 unidades donantes, Kish 3.103 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0016). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0209 | 0,0126 | 0,080 | ✅ |
| actividad_sexo | 0,0157 | 0,0078 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0042 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0178 | 0,0149 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0386 | 0,0132 | 0,080 | ✅ |
| tamano_municipio | 0,0034 | 0,0047 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0193 | 0,0151 | 0,080 | ✅ |

## PROV:04

- Población `2026-01-01_PROV_04_50000_s1`: 49.971 personas (pedidas 50.000) de 782.945 residentes (1 por 15,7).
- Donantes: 98,6 % locales; personas por nivel: ccaa_parecidas 190, misma_ccaa_mismo_grado_urbanizacion 523, mismo_territorio 49.258; 17.292 unidades donantes, Kish 10.239 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0042). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0128 | 0,0127 | 0,080 | ✅ |
| actividad_sexo | 0,0054 | 0,0080 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0047 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0094 | 0,0145 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0114 | 0,0149 | 0,080 | ✅ |
| tamano_municipio | 0,0149 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0168 | 0,0161 | 0,080 | ✅ |

## PROV:35

- Población `2026-01-01_PROV_35_50000_s1`: 49.987 personas (pedidas 50.000) de 1.181.260 residentes (1 por 23,6).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 63, misma_ccaa_mismo_grado_urbanizacion 32, mismo_territorio 49.892; 18.193 unidades donantes, Kish 12.068 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0040). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0141 | 0,0134 | 0,080 | ✅ |
| actividad_sexo | 0,0082 | 0,0076 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0023 | 0,0042 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0118 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0106 | 0,0141 | 0,080 | ✅ |
| tamano_municipio | 0,0049 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0175 | 0,0165 | 0,080 | ✅ |

## PROV:20

- Población `2026-01-01_PROV_20_50000_s1`: 49.978 personas (pedidas 50.000) de 735.369 residentes (1 por 14,7).
- Donantes: 99,1 % locales; personas por nivel: ccaa_parecidas 272, misma_ccaa_mismo_grado_urbanizacion 202, mismo_territorio 49.504; 19.435 unidades donantes, Kish 12.136 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0251 | 0,0125 | 0,080 | ✅ |
| actividad_sexo | 0,0093 | 0,0078 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0012 | 0,0043 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0125 | 0,0155 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0086 | 0,0132 | 0,080 | ✅ |
| tamano_municipio | 0,0201 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0188 | 0,0152 | 0,080 | ✅ |

## PROV:32

- Población `2026-01-01_PROV_32_50000_s1`: 49.975 personas (pedidas 50.000) de 306.524 residentes (1 por 6,1).
- Donantes: 97,5 % locales; personas por nivel: ccaa_parecidas 620, misma_ccaa_mismo_grado_urbanizacion 639, mismo_territorio 48.716; 12.429 unidades donantes, Kish 6.884 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0172 | 0,0127 | 0,080 | ✅ |
| actividad_sexo | 0,0079 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0038 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0162 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0112 | 0,0123 | 0,080 | ✅ |
| tamano_municipio | 0,0096 | 0,0054 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0143 | 0,0148 | 0,080 | ✅ |

## PROV:51

- Población `2026-01-01_PROV_51_50000_s1`: 49.973 personas (pedidas 50.000) de 84.196 residentes (1 por 1,7).
- Donantes: 99,4 % locales; personas por nivel: ccaa_parecidas 286, mismo_territorio 49.687; 2.523 unidades donantes, Kish 990 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0010). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0222 | 0,0134 | 0,080 | ✅ |
| actividad_sexo | 0,0074 | 0,0083 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0007 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0218 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0092 | 0,0100 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0419 | 0,0186 | 0,080 | ✅ |

## PROV:52

- Población `2026-01-01_PROV_52_50000_s1`: 50.007 personas (pedidas 50.000) de 86.908 residentes (1 por 1,7).
- Donantes: 97,9 % locales; personas por nivel: ccaa_parecidas 1.049, mismo_territorio 48.958; 2.650 unidades donantes, Kish 1.240 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0015). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0185 | 0,0132 | 0,080 | ✅ |
| actividad_sexo | 0,0052 | 0,0083 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0049 | 0,0047 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0206 | 0,0150 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0325 | 0,0115 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0268 | 0,0188 | 0,080 | ✅ |

## MUNIS:ejemplo_valencia_urbano

- Población `2026-01-01_MUNIS_ejemplo_valencia_urbano_20000_s1`: 19.992 personas (pedidas 20.000) de 1.273.589 residentes (1 por 63,7).
- Donantes: 98,5 % locales; personas por nivel: misma_provincia 300, mismo_territorio 19.692; 8.078 unidades donantes, Kish 6.165 (mínimo 200).
- Confianza esperada: baja.
- V-MARG: 0 fallos de 7 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 2 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0009 | 0,0073 | 0,080 | ✅ |
| tamano_municipio | 0,0262 | 0,0070 | 0,080 | ✅ |

## MUNIS:ejemplo_teruel_rural

- Población `2026-01-01_MUNIS_ejemplo_teruel_rural_20000_s1`: 19.999 personas (pedidas 20.000) de 53.706 residentes (1 por 2,7).
- Donantes: 0,0 % locales; personas por nivel: ccaa_parecidas 5, misma_ccaa_mismo_grado_urbanizacion 93, misma_provincia 19.901; 2.346 unidades donantes, Kish 1.159 (mínimo 200).
- Confianza esperada: baja (reducida: menos del 50 % de donantes locales).
- V-MARG: 0 fallos de 6 (TVD media 0,0016). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 1 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0029 | 0,0066 | 0,080 | ✅ |
