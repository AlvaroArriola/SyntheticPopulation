# F5 · Anexo por territorio

Generado desde `fase_05_validacion.json` (`python -m sinpop.validate.fase5 --anexo`). Semilla 1. Detalle de cada comprobación en `reports/fase_05/`.

## CCAA:01

- Población `2026-01-01_CCAA_01_100000_s1`: 100.012 personas (pedidas 100.000) de 8.751.219 residentes (1 por 87,5).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 252, mismo_territorio 99.760; 39.798 unidades donantes, Kish 30.490 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0034). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 64 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0144 | 0,0093 | 0,050 | ✅ |
| actividad_sexo | 0,0076 | 0,0059 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0022 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0077 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0067 | 0,0099 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0190 | 0,0047 | 0,050 | ✅ |
| tamano_municipio | 0,0127 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0313 | 0,0115 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,620 | 0,005 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,251 | 0,250 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,015 | 0,017 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,038 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,065 | 0,065 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,042 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,086 | 0,086 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,189 | 0,002 | ✅ |

## CCAA:02

- Población `2026-01-01_CCAA_02_100000_s1`: 100.007 personas (pedidas 100.000) de 1.382.035 residentes (1 por 13,8).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 212, mismo_territorio 99.795; 38.134 unidades donantes, Kish 23.717 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0100 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0051 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0013 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0104 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0113 | 0,0097 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0052 | 0,0027 | 0,050 | ✅ |
| tamano_municipio | 0,0102 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0280 | 0,0110 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,621 | 0,005 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,254 | 0,257 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,022 | 0,020 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,038 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,627 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,078 | 0,080 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,050 | 0,044 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,125 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,062 | 0,063 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,183 | 0,187 | 0,005 | ✅ |

## CCAA:03

- Población `2026-01-01_CCAA_03_100000_s1`: 99.990 personas (pedidas 100.000) de 1.021.627 residentes (1 por 10,2).
- Donantes: 99,3 % locales; personas por nivel: ccaa_parecidas 653, mismo_territorio 99.337; 36.313 unidades donantes, Kish 20.844 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0018). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0143 | 0,0091 | 0,050 | ✅ |
| actividad_sexo | 0,0084 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0121 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0073 | 0,0087 | 0,050 | ✅ |
| tamano_municipio | 0,0048 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0305 | 0,0102 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,618 | 0,622 | 0,005 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,293 | 0,290 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,035 | 0,034 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,052 | 0,012 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,635 | 0,635 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,088 | 0,089 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,031 | 0,038 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,102 | 0,104 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,069 | 0,069 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,171 | 0,005 | ✅ |

## CCAA:04

- Población `2026-01-01_CCAA_04_100000_s1`: 99.995 personas (pedidas 100.000) de 1.260.336 residentes (1 por 12,6).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 145, mismo_territorio 99.850; 28.953 unidades donantes, Kish 14.981 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0123 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0047 | 0,0051 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0020 | 0,0032 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0083 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0103 | 0,0112 | 0,050 | ✅ |
| tamano_municipio | 0,0182 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0406 | 0,0118 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,603 | 0,610 | 0,007 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,167 | 0,173 | 0,006 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,034 | 0,034 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,058 | 0,051 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,060 | 0,060 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,046 | 0,052 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,106 | 0,106 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,049 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,152 | 0,010 | ✅ |

## CCAA:05

- Población `2026-01-01_CCAA_05_100000_s1`: 99.963 personas (pedidas 100.000) de 2.276.245 residentes (1 por 22,8).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 112, mismo_territorio 99.851; 37.082 unidades donantes, Kish 24.712 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0026). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0150 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0098 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0027 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0087 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0066 | 0,0102 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0014 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0064 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0499 | 0,0121 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,606 | 0,613 | 0,007 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,206 | 0,184 | 0,022 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,009 | 0,008 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,056 | 0,057 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,057 | 0,056 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,041 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,077 | 0,077 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,043 | 0,044 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,148 | 0,146 | 0,003 | ✅ |

## CCAA:06

- Población `2026-01-01_CCAA_06_100000_s1`: 99.996 personas (pedidas 100.000) de 597.088 residentes (1 por 6,0).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 56, mismo_territorio 99.940; 21.956 unidades donantes, Kish 12.399 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0017). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0112 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0051 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0113 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0079 | 0,0089 | 0,050 | ✅ |
| tamano_municipio | 0,0065 | 0,0039 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0375 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,623 | 0,628 | 0,006 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,255 | 0,010 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,017 | 0,017 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,040 | 0,034 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,633 | 0,632 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,081 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,030 | 0,036 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,095 | 0,097 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,059 | 0,058 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,168 | 0,002 | ✅ |

## CCAA:07

- Población `2026-01-01_CCAA_07_100000_s1`: 99.998 personas (pedidas 100.000) de 2.419.181 residentes (1 por 24,2).
- Donantes: 99,2 % locales; personas por nivel: ccaa_parecidas 786, espana 19, mismo_territorio 99.193; 43.808 unidades donantes, Kish 30.944 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 71 (todos los niveles); excepciones 1.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0106 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0044 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0012 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0100 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0075 | 0,0089 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0135 | 0,0049 | 0,050 | ✅ |
| tamano_municipio | 0,0082 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0245 | 0,0103 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,625 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,278 | 0,275 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,042 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,049 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,632 | 0,633 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,080 | 0,080 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,032 | 0,043 | 0,010 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,111 | 0,111 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,167 | 0,005 | ✅ |

## CCAA:08

- Población `2026-01-01_CCAA_08_100000_s1`: 99.980 personas (pedidas 100.000) de 2.155.201 residentes (1 por 21,6).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 124, mismo_territorio 99.856; 38.649 unidades donantes, Kish 26.622 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 43 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0091 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0041 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0090 | 0,0105 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0091 | 0,0094 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0188 | 0,0040 | 0,050 | ✅ |
| tamano_municipio | 0,0139 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0292 | 0,0110 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,617 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,302 | 0,309 | 0,007 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,024 | 0,021 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,044 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,067 | 0,067 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,043 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,104 | 0,103 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,189 | 0,000 | ✅ |

## CCAA:09

- Población `2026-01-01_CCAA_09_100000_s1`: 100.004 personas (pedidas 100.000) de 8.202.041 residentes (1 por 82,0).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.004; 39.708 unidades donantes, Kish 29.848 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0133 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0085 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0027 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0112 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0118 | 0,0108 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0066 | 0,0030 | 0,050 | ✅ |
| tamano_municipio | 0,0243 | 0,0043 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0318 | 0,0121 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,620 | 0,006 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,174 | 0,171 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,018 | 0,022 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,042 | 0,039 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,076 | 0,076 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,063 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,125 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,065 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,191 | 0,188 | 0,003 | ✅ |

## CCAA:10

- Población `2026-01-01_CCAA_10_100000_s1`: 99.975 personas (pedidas 100.000) de 5.529.081 residentes (1 por 55,3).
- Donantes: 99,1 % locales; personas por nivel: ccaa_parecidas 903, mismo_territorio 99.072; 40.383 unidades donantes, Kish 30.504 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0026). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0161 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0114 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0031 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0089 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0096 | 0,0110 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0141 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0220 | 0,0044 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0298 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,614 | 0,615 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,222 | 0,224 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,001 | 0,002 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,031 | 0,012 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,621 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,066 | 0,065 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,051 | 0,008 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,117 | 0,117 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,055 | 0,054 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,193 | 0,189 | 0,004 | ✅ |

## CCAA:11

- Población `2026-01-01_CCAA_11_100000_s1`: 100.041 personas (pedidas 100.000) de 1.055.386 residentes (1 por 10,5).
- Donantes: 99,5 % locales; personas por nivel: ccaa_parecidas 463, mismo_territorio 99.578; 35.514 unidades donantes, Kish 23.245 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0110 | 0,0093 | 0,050 | ✅ |
| actividad_sexo | 0,0049 | 0,0058 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0087 | 0,0105 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0053 | 0,0080 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0141 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0115 | 0,0043 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0255 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,623 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,284 | 0,282 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,019 | 0,019 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,055 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,629 | 0,628 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,071 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,034 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,067 | 0,068 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,048 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,196 | 0,198 | 0,001 | ✅ |

## CCAA:12

- Población `2026-01-01_CCAA_12_100000_s1`: 100.018 personas (pedidas 100.000) de 2.728.430 residentes (1 por 27,3).
- Donantes: 99,2 % locales; personas por nivel: ccaa_parecidas 778, mismo_territorio 99.240; 41.535 unidades donantes, Kish 30.459 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0028). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0122 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0064 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0083 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0061 | 0,0084 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0111 | 0,0037 | 0,050 | ✅ |
| tamano_municipio | 0,0108 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0267 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,622 | 0,626 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,198 | 0,204 | 0,006 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,021 | 0,020 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,055 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,641 | 0,640 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,082 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,029 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,090 | 0,091 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,064 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,182 | 0,182 | 0,001 | ✅ |

## CCAA:13

- Población `2026-01-01_CCAA_13_100000_s1`: 99.994 personas (pedidas 100.000) de 7.168.876 residentes (1 por 71,7).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.994; 38.827 unidades donantes, Kish 29.360 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0028). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0098 | 0,0086 | 0,050 | ✅ |
| actividad_sexo | 0,0029 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0015 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0082 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0088 | 0,0104 | 0,050 | ✅ |
| tamano_municipio | 0,0152 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0355 | 0,0113 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,618 | 0,621 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,195 | 0,192 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,016 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,032 | 0,037 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,074 | 0,074 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,035 | 0,048 | 0,012 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,118 | 0,118 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,063 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,178 | 0,179 | 0,001 | ✅ |

## CCAA:14

- Población `2026-01-01_CCAA_14_100000_s1`: 99.986 personas (pedidas 100.000) de 1.605.913 residentes (1 por 16,1).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 119, mismo_territorio 99.867; 33.760 unidades donantes, Kish 21.915 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0026). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0097 | 0,0091 | 0,050 | ✅ |
| actividad_sexo | 0,0046 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0033 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0079 | 0,0103 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0121 | 0,0101 | 0,050 | ✅ |
| tamano_municipio | 0,0107 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0340 | 0,0114 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,606 | 0,611 | 0,005 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,228 | 0,220 | 0,007 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,020 | 0,026 | 0,006 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,040 | 0,009 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,614 | 0,614 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,062 | 0,062 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,080 | 0,018 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,110 | 0,111 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,192 | 0,005 | ✅ |

## CCAA:15

- Población `2026-01-01_CCAA_15_100000_s1`: 99.974 personas (pedidas 100.000) de 690.044 residentes (1 por 6,9).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 54, mismo_territorio 99.920; 23.345 unidades donantes, Kish 12.712 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0121 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0058 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0109 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0087 | 0,0096 | 0,050 | ✅ |
| tamano_municipio | 0,0122 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0385 | 0,0117 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,623 | 0,626 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,220 | 0,210 | 0,010 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,014 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,043 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,630 | 0,630 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,071 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,041 | 0,046 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,108 | 0,109 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,051 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,176 | 0,189 | 0,013 | ✅ |

## CCAA:16

- Población `2026-01-01_CCAA_16_100000_s1`: 100.019 personas (pedidas 100.000) de 2.253.019 residentes (1 por 22,5).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 113, mismo_territorio 99.906; 42.081 unidades donantes, Kish 29.757 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0238 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0071 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0016 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0115 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0070 | 0,0091 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0121 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0133 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0332 | 0,0113 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,621 | 0,631 | 0,011 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,224 | 0,223 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,010 | 0,006 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,063 | 0,015 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,645 | 0,645 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,084 | 0,083 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,049 | 0,048 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,121 | 0,121 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,066 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,195 | 0,006 | ✅ |

## CCAA:17

- Población `2026-01-01_CCAA_17_100000_s1`: 100.017 personas (pedidas 100.000) de 329.550 residentes (1 por 3,3).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 311, mismo_territorio 99.706; 12.955 unidades donantes, Kish 6.955 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0015). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0076 | 0,0085 | 0,050 | ✅ |
| actividad_sexo | 0,0037 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0027 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0144 | 0,0110 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0122 | 0,0098 | 0,050 | ✅ |
| tamano_municipio | 0,0023 | 0,0034 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0353 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,621 | 0,625 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,234 | 0,222 | 0,011 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,036 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,046 | 0,035 | 0,011 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,624 | 0,624 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,070 | 0,070 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,038 | 0,046 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,116 | 0,119 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,049 | 0,048 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,194 | 0,006 | ✅ |

## CCAA:18

- Población `2026-01-01_CCAA_18_100000_s1`: 100.002 personas (pedidas 100.000) de 84.196 residentes (1 por 0,8).
- Donantes: 99,3 % locales; personas por nivel: ccaa_parecidas 727, mismo_territorio 99.275; 2.527 unidades donantes, Kish 1.154 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0006). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 1.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0295 | 0,0093 | 0,050 | ✅ |
| actividad_sexo | 0,0056 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0020 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0230 | 0,0105 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0093 | 0,0073 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0552 | 0,0129 | 0,050 | ❌ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,594 | 0,605 | 0,010 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,266 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,087 | 0,091 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,069 | 0,090 | 0,021 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,054 | 0,054 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,029 | 0,045 | 0,016 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,079 | 0,087 | 0,008 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,040 | 0,040 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,174 | 0,014 | ✅ |

## CCAA:19

- Población `2026-01-01_CCAA_19_100000_s1`: 100.022 personas (pedidas 100.000) de 86.908 residentes (1 por 0,9).
- Donantes: 97,3 % locales; personas por nivel: ccaa_parecidas 2.674, mismo_territorio 97.348; 2.666 unidades donantes, Kish 1.427 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 16 (TVD media 0,0007). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0165 | 0,0095 | 0,050 | ✅ |
| actividad_sexo | 0,0051 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0047 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0202 | 0,0102 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0191 | 0,0080 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0301 | 0,0131 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,601 | 0,604 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,231 | 0,225 | 0,006 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,107 | 0,109 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,048 | 0,013 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,618 | 0,618 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,052 | 0,051 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,067 | 0,062 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,092 | 0,112 | 0,019 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,030 | 0,030 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,192 | 0,004 | ✅ |

## PROV:28

- Población `2026-01-01_PROV_28_50000_s1`: 49.986 personas (pedidas 50.000) de 7.168.876 residentes (1 por 143,4).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 49.986; 19.474 unidades donantes, Kish 14.682 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0031). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0087 | 0,0126 | 0,080 | ✅ |
| actividad_sexo | 0,0041 | 0,0075 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0011 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0105 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0095 | 0,0153 | 0,080 | ✅ |
| tamano_municipio | 0,0151 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0360 | 0,0162 | 0,080 | ✅ |

## PROV:08

- Población `2026-01-01_PROV_08_50000_s1`: 49.972 personas (pedidas 50.000) de 6.008.837 residentes (1 por 120,2).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 49.972; 19.895 unidades donantes, Kish 15.038 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0036). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0135 | 0,0122 | 0,080 | ✅ |
| actividad_sexo | 0,0087 | 0,0079 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0022 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0125 | 0,0154 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0125 | 0,0150 | 0,080 | ✅ |
| tamano_municipio | 0,0258 | 0,0059 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0343 | 0,0161 | 0,080 | ✅ |

## PROV:42

- Población `2026-01-01_PROV_42_50000_s1`: 50.004 personas (pedidas 50.000) de 90.824 residentes (1 por 1,8).
- Donantes: 97,9 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 1.048, mismo_territorio 48.956; 3.848 unidades donantes, Kish 2.020 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0017). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0264 | 0,0126 | 0,080 | ✅ |
| actividad_sexo | 0,0111 | 0,0076 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0027 | 0,0043 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0272 | 0,0154 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0296 | 0,0137 | 0,080 | ✅ |
| tamano_municipio | 0,0148 | 0,0048 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0350 | 0,0152 | 0,080 | ✅ |

## PROV:44

- Población `2026-01-01_PROV_44_50000_s1`: 50.005 personas (pedidas 50.000) de 137.173 residentes (1 por 2,7).
- Donantes: 97,3 % locales; personas por nivel: ccaa_parecidas 172, misma_ccaa_mismo_grado_urbanizacion 1.168, mismo_territorio 48.665; 5.480 unidades donantes, Kish 2.706 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0018). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0165 | 0,0128 | 0,080 | ✅ |
| actividad_sexo | 0,0061 | 0,0076 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0161 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0222 | 0,0133 | 0,080 | ✅ |
| tamano_municipio | 0,0155 | 0,0049 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0297 | 0,0149 | 0,080 | ✅ |

## PROV:04

- Población `2026-01-01_PROV_04_50000_s1`: 49.998 personas (pedidas 50.000) de 782.945 residentes (1 por 15,7).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 194, misma_ccaa_mismo_grado_urbanizacion 339, mismo_territorio 49.465; 17.616 unidades donantes, Kish 10.798 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0037). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0122 | 0,0129 | 0,080 | ✅ |
| actividad_sexo | 0,0056 | 0,0075 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0089 | 0,0149 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0121 | 0,0149 | 0,080 | ✅ |
| tamano_municipio | 0,0153 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0342 | 0,0164 | 0,080 | ✅ |

## PROV:35

- Población `2026-01-01_PROV_35_50000_s1`: 49.978 personas (pedidas 50.000) de 1.181.260 residentes (1 por 23,6).
- Donantes: 100,0 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 14, mismo_territorio 49.964; 18.487 unidades donantes, Kish 12.400 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0042). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0173 | 0,0136 | 0,080 | ✅ |
| actividad_sexo | 0,0092 | 0,0079 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0035 | 0,0042 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0129 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0103 | 0,0142 | 0,080 | ✅ |
| tamano_municipio | 0,0052 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0521 | 0,0167 | 0,080 | ✅ |

## PROV:20

- Población `2026-01-01_PROV_20_50000_s1`: 50.015 personas (pedidas 50.000) de 735.369 residentes (1 por 14,7).
- Donantes: 99,0 % locales; personas por nivel: ccaa_parecidas 265, misma_ccaa_mismo_grado_urbanizacion 212, mismo_territorio 49.538; 19.714 unidades donantes, Kish 12.628 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0031). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0229 | 0,0123 | 0,080 | ✅ |
| actividad_sexo | 0,0079 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0003 | 0,0043 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0127 | 0,0148 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0106 | 0,0134 | 0,080 | ✅ |
| tamano_municipio | 0,0166 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0330 | 0,0146 | 0,080 | ✅ |

## PROV:32

- Población `2026-01-01_PROV_32_50000_s1`: 49.980 personas (pedidas 50.000) de 306.524 residentes (1 por 6,1).
- Donantes: 98,0 % locales; personas por nivel: ccaa_parecidas 543, misma_ccaa_mismo_grado_urbanizacion 453, mismo_territorio 48.984; 12.441 unidades donantes, Kish 6.939 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0180 | 0,0124 | 0,080 | ✅ |
| actividad_sexo | 0,0077 | 0,0079 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0025 | 0,0038 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0155 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0120 | 0,0122 | 0,080 | ✅ |
| tamano_municipio | 0,0106 | 0,0054 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0195 | 0,0152 | 0,080 | ✅ |

## PROV:51

- Población `2026-01-01_PROV_51_50000_s1`: 50.003 personas (pedidas 50.000) de 84.196 residentes (1 por 1,7).
- Donantes: 99,2 % locales; personas por nivel: ccaa_parecidas 377, mismo_territorio 49.626; 2.519 unidades donantes, Kish 1.154 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0013). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0303 | 0,0135 | 0,080 | ✅ |
| actividad_sexo | 0,0060 | 0,0082 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0026 | 0,0042 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0235 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0095 | 0,0102 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0551 | 0,0179 | 0,080 | ✅ |

## PROV:52

- Población `2026-01-01_PROV_52_50000_s1`: 50.001 personas (pedidas 50.000) de 86.908 residentes (1 por 1,7).
- Donantes: 97,3 % locales; personas por nivel: ccaa_parecidas 1.345, mismo_territorio 48.656; 2.661 unidades donantes, Kish 1.429 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 16 (TVD media 0,0013). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0165 | 0,0128 | 0,080 | ✅ |
| actividad_sexo | 0,0054 | 0,0081 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0044 | 0,0047 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0206 | 0,0149 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0190 | 0,0112 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0300 | 0,0190 | 0,080 | ✅ |

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

- Población `2026-01-01_MUNIS_ejemplo_teruel_rural_20000_s1`: 20.003 personas (pedidas 20.000) de 53.706 residentes (1 por 2,7).
- Donantes: 0,0 % locales; personas por nivel: ccaa_parecidas 12, misma_ccaa_mismo_grado_urbanizacion 111, misma_provincia 19.880; 2.353 unidades donantes, Kish 1.154 (mínimo 200).
- Confianza esperada: baja (reducida: menos del 50 % de donantes locales).
- V-MARG: 0 fallos de 6 (TVD media 0,0017). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 1 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0031 | 0,0066 | 0,080 | ✅ |
