# F5 · Anexo por territorio

Generado desde `fase_05_validacion.json` (`python -m sinpop.validate.fase5 --anexo`). Semilla 1. Detalle de cada comprobación en `reports/fase_05/`.

## CCAA:01

- Población `2026-01-01_CCAA_01_100000_s1`: 99.994 personas (pedidas 100.000) de 8.751.219 residentes (1 por 87,5).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 175, mismo_territorio 99.819; 39.855 unidades donantes, Kish 30.461 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0044). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 64 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0175 | 0,0092 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0308 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0088 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0093 | 0,0096 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0138 | 0,0046 | 0,050 | ✅ |
| tamano_municipio | 0,0099 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0309 | 0,0112 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,612 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,015 | 0,003 | 0,013 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,630 | 0,641 | 0,010 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,037 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,065 | 0,067 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,040 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,086 | 0,087 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,055 | 0,002 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,193 | 0,006 | ✅ |

## CCAA:02

- Población `2026-01-01_CCAA_02_100000_s1`: 100.004 personas (pedidas 100.000) de 1.382.035 residentes (1 por 13,8).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.004; 40.382 unidades donantes, Kish 27.588 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0030). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0131 | 0,0086 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0103 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0181 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0073 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0205 | 0,0099 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0024 | 0,0027 | 0,050 | ✅ |
| tamano_municipio | 0,0108 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0280 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,612 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,022 | 0,061 | 0,040 | ❌ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,627 | 0,633 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,041 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,627 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,078 | 0,078 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,050 | 0,045 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,130 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,062 | 0,063 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,183 | 0,189 | 0,006 | ✅ |

## CCAA:03

- Población `2026-01-01_CCAA_03_100000_s1`: 100.015 personas (pedidas 100.000) de 1.021.627 residentes (1 por 10,2).
- Donantes: 99,6 % locales; personas por nivel: ccaa_parecidas 393, mismo_territorio 99.622; 39.671 unidades donantes, Kish 25.696 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0143 | 0,0091 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0305 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0107 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0101 | 0,0089 | 0,050 | ✅ |
| tamano_municipio | 0,0035 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0289 | 0,0100 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,619 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,035 | 0,054 | 0,018 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,623 | 0,630 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,049 | 0,010 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,635 | 0,635 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,088 | 0,088 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,031 | 0,036 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,102 | 0,110 | 0,007 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,069 | 0,069 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,173 | 0,007 | ✅ |

## CCAA:04

- Población `2026-01-01_CCAA_04_100000_s1`: 100.024 personas (pedidas 100.000) de 1.260.336 residentes (1 por 12,6).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.024; 34.897 unidades donantes, Kish 21.381 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0185 | 0,0090 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0060 | 0,0032 | 0,050 | ✅ |
| estado_civil_edad | 0,0306 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0079 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0191 | 0,0113 | 0,050 | ✅ |
| tamano_municipio | 0,0087 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0383 | 0,0118 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,595 | 0,599 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,034 | 0,014 | 0,020 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,614 | 0,623 | 0,010 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,058 | 0,047 | 0,011 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,060 | 0,060 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,046 | 0,044 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,106 | 0,113 | 0,007 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,049 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,164 | 0,002 | ✅ |

## CCAA:05

- Población `2026-01-01_CCAA_05_100000_s1`: 100.012 personas (pedidas 100.000) de 2.276.245 residentes (1 por 22,8).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.012; 38.284 unidades donantes, Kish 27.643 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0037). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0256 | 0,0092 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0401 | 0,0062 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0079 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0115 | 0,0102 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0003 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0080 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0460 | 0,0118 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,605 | 0,607 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,009 | 0,009 | 0,000 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,613 | 0,622 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,056 | 0,055 | 0,000 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,057 | 0,054 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,043 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,077 | 0,080 | 0,004 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,043 | 0,042 | 0,002 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,148 | 0,151 | 0,003 | ✅ |

## CCAA:06

- Población `2026-01-01_CCAA_06_100000_s1`: 99.995 personas (pedidas 100.000) de 597.088 residentes (1 por 6,0).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.995; 23.744 unidades donantes, Kish 15.376 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0131 | 0,0091 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0023 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0243 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0110 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0107 | 0,0093 | 0,050 | ✅ |
| tamano_municipio | 0,0048 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0357 | 0,0110 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,621 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,017 | 0,034 | 0,017 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,623 | 0,630 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,040 | 0,036 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,633 | 0,632 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,082 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,030 | 0,039 | 0,009 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,095 | 0,101 | 0,006 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,059 | 0,060 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,170 | 0,004 | ✅ |

## CCAA:07

- Población `2026-01-01_CCAA_07_100000_s1`: 100.004 personas (pedidas 100.000) de 2.419.181 residentes (1 por 24,2).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 312, mismo_territorio 99.692; 44.373 unidades donantes, Kish 32.120 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 71 (todos los niveles); excepciones 1.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0124 | 0,0087 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0072 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0266 | 0,0064 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0087 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0129 | 0,0089 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0104 | 0,0049 | 0,050 | ✅ |
| tamano_municipio | 0,0067 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0246 | 0,0105 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,617 | 0,620 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,082 | 0,041 | ❌ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,620 | 0,628 | 0,008 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,050 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,632 | 0,632 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,080 | 0,081 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,032 | 0,035 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,111 | 0,116 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,170 | 0,008 | ✅ |

## CCAA:08

- Población `2026-01-01_CCAA_08_100000_s1`: 99.972 personas (pedidas 100.000) de 2.155.201 residentes (1 por 21,6).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.972; 39.554 unidades donantes, Kish 28.614 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0035). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 43 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0146 | 0,0091 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0071 | 0,0031 | 0,050 | ✅ |
| estado_civil_edad | 0,0256 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0095 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0144 | 0,0097 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0121 | 0,0040 | 0,050 | ✅ |
| tamano_municipio | 0,0122 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0274 | 0,0109 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,609 | 0,608 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,024 | 0,055 | 0,030 | ❌ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,632 | 0,641 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,043 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,001 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,067 | 0,067 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,041 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,104 | 0,109 | 0,006 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,051 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,192 | 0,003 | ✅ |

## CCAA:09

- Población `2026-01-01_CCAA_09_100000_s1`: 100.008 personas (pedidas 100.000) de 8.202.041 residentes (1 por 82,0).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.008; 39.796 unidades donantes, Kish 29.889 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0157 | 0,0087 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0112 | 0,0031 | 0,050 | ✅ |
| estado_civil_edad | 0,0243 | 0,0062 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0092 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0249 | 0,0108 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0050 | 0,0027 | 0,050 | ✅ |
| tamano_municipio | 0,0208 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0281 | 0,0120 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,612 | 0,610 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,018 | 0,023 | 0,005 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,634 | 0,008 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,042 | 0,035 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,076 | 0,077 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,055 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,134 | 0,009 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,065 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,191 | 0,192 | 0,001 | ✅ |

## CCAA:10

- Población `2026-01-01_CCAA_10_100000_s1`: 99.991 personas (pedidas 100.000) de 5.529.081 residentes (1 por 55,3).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 99.991; 40.438 unidades donantes, Kish 30.522 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0032). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0161 | 0,0089 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0082 | 0,0031 | 0,050 | ✅ |
| estado_civil_edad | 0,0247 | 0,0064 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0081 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0169 | 0,0109 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0065 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0180 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0270 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,607 | 0,606 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,001 | 0,030 | 0,029 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,635 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,034 | 0,009 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,066 | 0,065 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,041 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,117 | 0,120 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,055 | 0,054 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,193 | 0,194 | 0,002 | ✅ |

## CCAA:11

- Población `2026-01-01_CCAA_11_100000_s1`: 100.014 personas (pedidas 100.000) de 1.055.386 residentes (1 por 10,6).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 138, mismo_territorio 99.876; 38.770 unidades donantes, Kish 27.522 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0028). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0147 | 0,0090 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0013 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0309 | 0,0058 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0091 | 0,0105 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0062 | 0,0083 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0079 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0113 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0245 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,619 | 0,618 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,019 | 0,031 | 0,012 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,634 | 0,646 | 0,012 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,055 | 0,006 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,629 | 0,629 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,072 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,036 | 0,008 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,067 | 0,068 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,048 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,196 | 0,204 | 0,007 | ✅ |

## CCAA:12

- Población `2026-01-01_CCAA_12_100000_s1`: 100.048 personas (pedidas 100.000) de 2.728.430 residentes (1 por 27,3).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 318, mismo_territorio 99.730; 41.812 unidades donantes, Kish 31.098 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0031). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0145 | 0,0087 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0312 | 0,0065 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0101 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0065 | 0,0084 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0095 | 0,0037 | 0,050 | ✅ |
| tamano_municipio | 0,0109 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0258 | 0,0105 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,624 | 0,627 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,021 | 0,036 | 0,015 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,622 | 0,629 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,051 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,641 | 0,640 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,080 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,029 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,090 | 0,090 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,063 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,182 | 0,186 | 0,004 | ✅ |

## CCAA:13

- Población `2026-01-01_CCAA_13_100000_s1`: 100.021 personas (pedidas 100.000) de 7.168.876 residentes (1 por 71,7).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.021; 38.895 unidades donantes, Kish 29.367 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0031). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0141 | 0,0090 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0045 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0231 | 0,0062 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0086 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0127 | 0,0105 | 0,050 | ✅ |
| tamano_municipio | 0,0139 | 0,0039 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0343 | 0,0113 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,001 | 0,015 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,621 | 0,628 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,032 | 0,036 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,074 | 0,074 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,035 | 0,044 | 0,009 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,118 | 0,121 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,063 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,178 | 0,181 | 0,003 | ✅ |

## CCAA:14

- Población `2026-01-01_CCAA_14_100000_s1`: 100.024 personas (pedidas 100.000) de 1.605.913 residentes (1 por 16,1).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.024; 36.331 unidades donantes, Kish 26.661 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0032). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0169 | 0,0089 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0096 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0260 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0074 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0198 | 0,0101 | 0,050 | ✅ |
| tamano_municipio | 0,0073 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0320 | 0,0114 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,607 | 0,607 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,020 | 0,016 | 0,004 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,631 | 0,640 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,041 | 0,008 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,614 | 0,614 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,062 | 0,063 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,066 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,110 | 0,116 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,194 | 0,007 | ✅ |

## CCAA:15

- Población `2026-01-01_CCAA_15_100000_s1`: 100.028 personas (pedidas 100.000) de 690.044 residentes (1 por 6,9).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.028; 25.333 unidades donantes, Kish 16.126 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0151 | 0,0086 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0091 | 0,0033 | 0,050 | ✅ |
| estado_civil_edad | 0,0109 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0086 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0196 | 0,0099 | 0,050 | ✅ |
| tamano_municipio | 0,0117 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0329 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,619 | 0,619 | 0,000 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,053 | 0,037 | ❌ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,602 | 0,603 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,046 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,630 | 0,630 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,071 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,041 | 0,043 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,108 | 0,121 | 0,013 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,176 | 0,183 | 0,008 | ✅ |

## CCAA:16

- Población `2026-01-01_CCAA_16_100000_s1`: 100.022 personas (pedidas 100.000) de 2.253.019 residentes (1 por 22,5).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 100.022; 42.825 unidades donantes, Kish 31.763 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0030). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0223 | 0,0091 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0083 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0261 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0108 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0154 | 0,0091 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0077 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0104 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0329 | 0,0110 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,627 | 0,007 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,010 | 0,049 | 0,039 | ❌ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,624 | 0,628 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,058 | 0,011 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,645 | 0,646 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,084 | 0,085 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,049 | 0,040 | 0,009 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,121 | 0,126 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,066 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,193 | 0,004 | ✅ |

## CCAA:17

- Población `2026-01-01_CCAA_17_100000_s1`: 100.003 personas (pedidas 100.000) de 329.550 residentes (1 por 3,3).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 55, mismo_territorio 99.948; 13.128 unidades donantes, Kish 8.495 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0154 | 0,0087 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0064 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0191 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0126 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0206 | 0,0097 | 0,050 | ✅ |
| tamano_municipio | 0,0041 | 0,0035 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0304 | 0,0109 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,616 | 0,000 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,070 | 0,030 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,621 | 0,628 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,046 | 0,037 | 0,009 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,624 | 0,624 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,070 | 0,069 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,038 | 0,035 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,116 | 0,128 | 0,012 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,049 | 0,048 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,195 | 0,006 | ✅ |

## CCAA:18

- Población `2026-01-01_CCAA_18_100000_s1`: 99.999 personas (pedidas 100.000) de 84.196 residentes (1 por 0,8).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 203, mismo_territorio 99.796; 2.509 unidades donantes, Kish 1.719 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0008). Reglas duras: 0 violaciones.
- V-CRUCE: 1 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0295 | 0,0094 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0071 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0316 | 0,0057 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0200 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0172 | 0,0072 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0518 | 0,0129 | 0,050 | ❌ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,596 | 0,600 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,087 | 0,040 | 0,048 | ❌ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,640 | 0,014 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,069 | 0,077 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,054 | 0,054 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,029 | 0,044 | 0,015 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,079 | 0,080 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,040 | 0,040 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,189 | 0,002 | ✅ |

## CCAA:19

- Población `2026-01-01_CCAA_19_100000_s1`: 99.995 personas (pedidas 100.000) de 86.908 residentes (1 por 0,9).
- Donantes: 97,8 % locales; personas por nivel: ccaa_parecidas 2.187, mismo_territorio 97.808; 2.646 unidades donantes, Kish 1.901 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 11 (TVD media 0,0010). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0236 | 0,0094 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0142 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0203 | 0,0057 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0158 | 0,0104 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0323 | 0,0082 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0303 | 0,0134 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,598 | 0,596 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,107 | 0,049 | 0,058 | ❌ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,627 | 0,634 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,052 | 0,009 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,618 | 0,618 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,067 | 0,042 | 0,025 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,092 | 0,080 | 0,012 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,030 | 0,030 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,187 | 0,001 | ✅ |

## PROV:28

- Población `2026-01-01_PROV_28_50000_s1`: 50.011 personas (pedidas 50.000) de 7.168.876 residentes (1 por 143,3).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 50.011; 19.472 unidades donantes, Kish 14.750 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0043). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0148 | 0,0128 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0064 | 0,0044 | 0,080 | ✅ |
| estado_civil_edad | 0,0214 | 0,0087 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0099 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0148 | 0,0151 | 0,080 | ✅ |
| tamano_municipio | 0,0130 | 0,0055 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0317 | 0,0162 | 0,080 | ✅ |

## PROV:08

- Población `2026-01-01_PROV_08_50000_s1`: 50.015 personas (pedidas 50.000) de 6.008.837 residentes (1 por 120,1).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 50.015; 19.921 unidades donantes, Kish 15.002 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0034). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0159 | 0,0127 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0095 | 0,0046 | 0,080 | ✅ |
| estado_civil_edad | 0,0236 | 0,0089 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0114 | 0,0156 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0239 | 0,0151 | 0,080 | ✅ |
| tamano_municipio | 0,0217 | 0,0062 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0301 | 0,0161 | 0,080 | ✅ |

## PROV:42

- Población `2026-01-01_PROV_42_50000_s1`: 49.992 personas (pedidas 50.000) de 90.824 residentes (1 por 1,8).
- Donantes: 99,1 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 438, mismo_territorio 49.554; 3.805 unidades donantes, Kish 2.286 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0208 | 0,0127 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0077 | 0,0043 | 0,080 | ✅ |
| estado_civil_edad | 0,0159 | 0,0088 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0252 | 0,0156 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0306 | 0,0138 | 0,080 | ✅ |
| tamano_municipio | 0,0125 | 0,0048 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0276 | 0,0152 | 0,080 | ✅ |

## PROV:44

- Población `2026-01-01_PROV_44_50000_s1`: 49.993 personas (pedidas 50.000) de 137.173 residentes (1 por 2,7).
- Donantes: 98,3 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 856, mismo_territorio 49.137; 5.510 unidades donantes, Kish 3.461 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0219 | 0,0121 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0150 | 0,0042 | 0,080 | ✅ |
| estado_civil_edad | 0,0198 | 0,0084 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0122 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0331 | 0,0136 | 0,080 | ✅ |
| tamano_municipio | 0,0157 | 0,0047 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0261 | 0,0149 | 0,080 | ✅ |

## PROV:04

- Población `2026-01-01_PROV_04_50000_s1`: 50.022 personas (pedidas 50.000) de 782.945 residentes (1 por 15,7).
- Donantes: 99,6 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 211, mismo_territorio 49.811; 18.801 unidades donantes, Kish 13.119 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0057). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0162 | 0,0127 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0128 | 0,0046 | 0,080 | ✅ |
| estado_civil_edad | 0,0232 | 0,0083 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0075 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0266 | 0,0147 | 0,080 | ✅ |
| tamano_municipio | 0,0172 | 0,0054 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0307 | 0,0164 | 0,080 | ✅ |

## PROV:35

- Población `2026-01-01_PROV_35_50000_s1`: 50.006 personas (pedidas 50.000) de 1.181.260 residentes (1 por 23,6).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 50.006; 19.057 unidades donantes, Kish 13.706 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0043). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0274 | 0,0133 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0031 | 0,0042 | 0,080 | ✅ |
| estado_civil_edad | 0,0410 | 0,0085 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0089 | 0,0153 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0138 | 0,0140 | 0,080 | ✅ |
| tamano_municipio | 0,0083 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0494 | 0,0168 | 0,080 | ✅ |

## PROV:20

- Población `2026-01-01_PROV_20_50000_s1`: 49.996 personas (pedidas 50.000) de 735.369 residentes (1 por 14,7).
- Donantes: 100,0 % locales; personas por nivel: mismo_territorio 49.996; 20.685 unidades donantes, Kish 14.361 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0037). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0203 | 0,0128 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0093 | 0,0043 | 0,080 | ✅ |
| estado_civil_edad | 0,0201 | 0,0084 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0124 | 0,0147 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0165 | 0,0130 | 0,080 | ✅ |
| tamano_municipio | 0,0125 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0340 | 0,0146 | 0,080 | ✅ |

## PROV:32

- Población `2026-01-01_PROV_32_50000_s1`: 49.978 personas (pedidas 50.000) de 306.524 residentes (1 por 6,1).
- Donantes: 98,8 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 614, mismo_territorio 49.364; 13.254 unidades donantes, Kish 8.229 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0169 | 0,0125 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0039 | 0,080 | ✅ |
| estado_civil_edad | 0,0324 | 0,0089 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0145 | 0,0150 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0144 | 0,0123 | 0,080 | ✅ |
| tamano_municipio | 0,0080 | 0,0054 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0196 | 0,0152 | 0,080 | ✅ |

## PROV:51

- Población `2026-01-01_PROV_51_50000_s1`: 49.978 personas (pedidas 50.000) de 84.196 residentes (1 por 1,7).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 108, mismo_territorio 49.870; 2.508 unidades donantes, Kish 1.711 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0014). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0297 | 0,0134 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0070 | 0,0042 | 0,080 | ✅ |
| estado_civil_edad | 0,0313 | 0,0083 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0201 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0175 | 0,0106 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0519 | 0,0179 | 0,080 | ✅ |

## PROV:52

- Población `2026-01-01_PROV_52_50000_s1`: 49.993 personas (pedidas 50.000) de 86.908 residentes (1 por 1,7).
- Donantes: 97,8 % locales; personas por nivel: ccaa_parecidas 1.091, mismo_territorio 48.902; 2.646 unidades donantes, Kish 1.891 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 11 (TVD media 0,0016). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0241 | 0,0131 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0143 | 0,0047 | 0,080 | ✅ |
| estado_civil_edad | 0,0207 | 0,0083 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0166 | 0,0149 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0326 | 0,0113 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0304 | 0,0190 | 0,080 | ✅ |

## MUNIS:ejemplo_valencia_urbano

- Población `2026-01-01_MUNIS_ejemplo_valencia_urbano_20000_s1`: 19.992 personas (pedidas 20.000) de 1.273.589 residentes (1 por 63,7).
- Donantes: 98,4 % locales; personas por nivel: misma_provincia 320, mismo_territorio 19.672; 8.034 unidades donantes, Kish 6.124 (mínimo 200).
- Confianza esperada: baja.
- V-MARG: 0 fallos de 6 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 2 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0071 | 0,0073 | 0,080 | ✅ |
| tamano_municipio | 0,0277 | 0,0070 | 0,080 | ✅ |

## MUNIS:ejemplo_teruel_rural

- Población `2026-01-01_MUNIS_ejemplo_teruel_rural_20000_s1`: 19.998 personas (pedidas 20.000) de 53.706 residentes (1 por 2,7).
- Donantes: 0,0 % locales; personas por nivel: misma_ccaa_mismo_grado_urbanizacion 157, misma_provincia 19.841; 2.356 unidades donantes, Kish 1.292 (mínimo 200).
- Confianza esperada: baja (reducida: menos del 50 % de donantes locales).
- V-MARG: 0 fallos de 5 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 1 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0131 | 0,0066 | 0,080 | ✅ |
