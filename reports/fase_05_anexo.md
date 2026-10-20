# F5 · Anexo por territorio

Generado desde `fase_05_validacion.json` (`python -m sinpop.validate.fase5 --anexo`). Semilla 1. Detalle de cada comprobación en `reports/fase_05/`.

## CCAA:01

- Población `2026-01-01_CCAA_01_100000_s1`: 100.008 personas (pedidas 100.000) de 8.751.219 residentes (1 por 87,5).
- Donantes: 91,2 % locales; personas por nivel: ccaa_parecidas 7.227, espana 1.562, mismo_territorio 91.219; 39.793 unidades donantes, Kish 30.547 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 64 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0142 | 0,0092 | 0,050 | ✅ |
| actividad_sexo | 0,0077 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0095 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0063 | 0,0095 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0164 | 0,0046 | 0,050 | ✅ |
| tamano_municipio | 0,0187 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0174 | 0,0114 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,612 | 0,615 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,251 | 0,250 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,015 | 0,019 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,042 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,065 | 0,066 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,044 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,086 | 0,086 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,052 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,188 | 0,001 | ✅ |

## CCAA:02

- Población `2026-01-01_CCAA_02_100000_s1`: 99.988 personas (pedidas 100.000) de 1.382.035 residentes (1 por 13,8).
- Donantes: 97,1 % locales; personas por nivel: ccaa_parecidas 2.889, mismo_territorio 97.099; 38.428 unidades donantes, Kish 24.326 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0087 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0054 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0011 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0090 | 0,0110 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0086 | 0,0099 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0055 | 0,0027 | 0,050 | ✅ |
| tamano_municipio | 0,0080 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0149 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,614 | 0,618 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,253 | 0,257 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,022 | 0,019 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,038 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,627 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,078 | 0,077 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,050 | 0,046 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,125 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,062 | 0,063 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,184 | 0,187 | 0,003 | ✅ |

## CCAA:03

- Población `2026-01-01_CCAA_03_100000_s1`: 100.020 personas (pedidas 100.000) de 1.021.627 residentes (1 por 10,2).
- Donantes: 95,6 % locales; personas por nivel: ccaa_parecidas 4.374, mismo_territorio 95.646; 37.030 unidades donantes, Kish 22.637 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0021). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0130 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0086 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0115 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0058 | 0,0087 | 0,050 | ✅ |
| tamano_municipio | 0,0087 | 0,0039 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0206 | 0,0102 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,618 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,292 | 0,290 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,035 | 0,033 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,051 | 0,012 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,635 | 0,635 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,088 | 0,088 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,031 | 0,032 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,102 | 0,103 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,069 | 0,070 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,168 | 0,002 | ✅ |

## CCAA:04

- Población `2026-01-01_CCAA_04_100000_s1`: 100.025 personas (pedidas 100.000) de 1.260.336 residentes (1 por 12,6).
- Donantes: 81,2 % locales; personas por nivel: ccaa_parecidas 18.783, mismo_territorio 81.242; 32.395 unidades donantes, Kish 18.826 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0026). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0084 | 0,0087 | 0,050 | ✅ |
| actividad_sexo | 0,0050 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0015 | 0,0032 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0090 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0075 | 0,0112 | 0,050 | ✅ |
| tamano_municipio | 0,0244 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0201 | 0,0123 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,601 | 0,600 | 0,000 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,167 | 0,171 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,034 | 0,037 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,058 | 0,050 | 0,008 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,060 | 0,061 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,046 | 0,058 | 0,012 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,106 | 0,106 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,048 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,157 | 0,005 | ✅ |

## CCAA:05

- Población `2026-01-01_CCAA_05_100000_s1`: 99.970 personas (pedidas 100.000) de 2.276.245 residentes (1 por 22,8).
- Donantes: 98,3 % locales; personas por nivel: ccaa_parecidas 1.681, mismo_territorio 98.289; 36.949 unidades donantes, Kish 24.668 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0124 | 0,0095 | 0,050 | ✅ |
| actividad_sexo | 0,0099 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0096 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0060 | 0,0101 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0008 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0107 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0162 | 0,0117 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,605 | 0,609 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,206 | 0,183 | 0,023 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,009 | 0,011 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,056 | 0,058 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,057 | 0,056 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,039 | 0,000 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,077 | 0,077 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,043 | 0,043 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,146 | 0,145 | 0,001 | ✅ |

## CCAA:06

- Población `2026-01-01_CCAA_06_100000_s1`: 100.003 personas (pedidas 100.000) de 597.088 residentes (1 por 6,0).
- Donantes: 90,6 % locales; personas por nivel: ccaa_parecidas 9.435, mismo_territorio 90.568; 23.724 unidades donantes, Kish 14.886 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0090 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0050 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0016 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0106 | 0,0111 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0050 | 0,0089 | 0,050 | ✅ |
| tamano_municipio | 0,0148 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0197 | 0,0105 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,621 | 0,623 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,255 | 0,010 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,017 | 0,012 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,040 | 0,037 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,633 | 0,633 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,082 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,030 | 0,032 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,095 | 0,098 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,059 | 0,059 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,169 | 0,003 | ✅ |

## CCAA:07

- Población `2026-01-01_CCAA_07_100000_s1`: 100.021 personas (pedidas 100.000) de 2.419.181 residentes (1 por 24,2).
- Donantes: 96,5 % locales; personas por nivel: ccaa_parecidas 3.111, espana 340, mismo_territorio 96.570; 43.958 unidades donantes, Kish 31.403 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 71 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0111 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0073 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0006 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0092 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0054 | 0,0089 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0114 | 0,0047 | 0,050 | ✅ |
| tamano_municipio | 0,0118 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0169 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,619 | 0,619 | 0,001 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,277 | 0,265 | 0,013 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,040 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,049 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,632 | 0,632 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,080 | 0,080 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,032 | 0,039 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,111 | 0,111 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,053 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,165 | 0,003 | ✅ |

## CCAA:08

- Población `2026-01-01_CCAA_08_100000_s1`: 99.995 personas (pedidas 100.000) de 2.155.201 residentes (1 por 21,6).
- Donantes: 96,7 % locales; personas por nivel: ccaa_parecidas 3.257, espana 29, mismo_territorio 96.709; 38.638 unidades donantes, Kish 26.954 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 43 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0084 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0044 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0009 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0114 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0078 | 0,0099 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0175 | 0,0040 | 0,050 | ✅ |
| tamano_municipio | 0,0160 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0146 | 0,0115 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,611 | 0,613 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,302 | 0,311 | 0,009 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,024 | 0,023 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,043 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,621 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,067 | 0,068 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,043 | 0,001 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,104 | 0,103 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,188 | 0,001 | ✅ |

## CCAA:09

- Población `2026-01-01_CCAA_09_100000_s1`: 99.953 personas (pedidas 100.000) de 8.202.041 residentes (1 por 82,1).
- Donantes: 97,3 % locales; personas por nivel: ccaa_parecidas 2.286, espana 389, mismo_territorio 97.278; 39.705 unidades donantes, Kish 29.914 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0101 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0081 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0097 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0087 | 0,0110 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0072 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0303 | 0,0043 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0177 | 0,0117 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,609 | 0,612 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,174 | 0,171 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,018 | 0,022 | 0,004 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,042 | 0,034 | 0,008 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,076 | 0,075 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,059 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,125 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,065 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,191 | 0,186 | 0,005 | ✅ |

## CCAA:10

- Población `2026-01-01_CCAA_10_100000_s1`: 99.979 personas (pedidas 100.000) de 5.529.081 residentes (1 por 55,3).
- Donantes: 93,2 % locales; personas por nivel: ccaa_parecidas 6.632, espana 181, mismo_territorio 93.166; 40.363 unidades donantes, Kish 30.415 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0150 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0109 | 0,0058 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0011 | 0,0032 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0094 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0082 | 0,0109 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0141 | 0,0032 | 0,050 | ✅ |
| tamano_municipio | 0,0331 | 0,0044 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0144 | 0,0114 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,222 | 0,224 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,001 | 0,001 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,033 | 0,010 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,066 | 0,065 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,049 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,117 | 0,117 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,055 | 0,054 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,193 | 0,189 | 0,004 | ✅ |

## CCAA:11

- Población `2026-01-01_CCAA_11_100000_s1`: 100.026 personas (pedidas 100.000) de 1.055.386 residentes (1 por 10,6).
- Donantes: 94,6 % locales; personas por nivel: ccaa_parecidas 5.365, mismo_territorio 94.661; 36.248 unidades donantes, Kish 25.031 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 22 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0104 | 0,0091 | 0,050 | ✅ |
| actividad_sexo | 0,0055 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0010 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0081 | 0,0105 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0035 | 0,0081 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0124 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0096 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0220 | 0,0105 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,619 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,285 | 0,283 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,019 | 0,018 | 0,001 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,056 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,629 | 0,629 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,071 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,030 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,067 | 0,068 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,047 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,196 | 0,197 | 0,001 | ✅ |

## CCAA:12

- Población `2026-01-01_CCAA_12_100000_s1`: 100.007 personas (pedidas 100.000) de 2.728.430 residentes (1 por 27,3).
- Donantes: 96,4 % locales; personas por nivel: ccaa_parecidas 3.045, espana 543, mismo_territorio 96.419; 41.572 unidades donantes, Kish 30.608 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 36 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0121 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0061 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0011 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0079 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0043 | 0,0087 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0109 | 0,0037 | 0,050 | ✅ |
| tamano_municipio | 0,0135 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0147 | 0,0107 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,623 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,198 | 0,200 | 0,002 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,021 | 0,019 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,051 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,641 | 0,641 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,083 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,033 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,090 | 0,091 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,064 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,181 | 0,181 | 0,001 | ✅ |

## CCAA:13

- Población `2026-01-01_CCAA_13_100000_s1`: 99.984 personas (pedidas 100.000) de 7.168.876 residentes (1 por 71,7).
- Donantes: 95,9 % locales; personas por nivel: ccaa_parecidas 3.722, espana 379, mismo_territorio 95.883; 38.830 unidades donantes, Kish 29.377 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0106 | 0,0086 | 0,050 | ✅ |
| actividad_sexo | 0,0062 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0009 | 0,0031 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0090 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0052 | 0,0104 | 0,050 | ✅ |
| tamano_municipio | 0,0268 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0168 | 0,0118 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,615 | 0,616 | 0,001 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,195 | 0,181 | 0,013 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,018 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,032 | 0,036 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,627 | 0,001 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,074 | 0,074 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,035 | 0,043 | 0,008 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,118 | 0,118 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,064 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,180 | 0,177 | 0,002 | ✅ |

## CCAA:14

- Población `2026-01-01_CCAA_14_100000_s1`: 100.005 personas (pedidas 100.000) de 1.605.913 residentes (1 por 16,1).
- Donantes: 90,4 % locales; personas por nivel: ccaa_parecidas 9.612, mismo_territorio 90.393; 34.682 unidades donantes, Kish 23.464 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0084 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0041 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0026 | 0,0031 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0088 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0135 | 0,0102 | 0,050 | ✅ |
| tamano_municipio | 0,0076 | 0,0034 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0149 | 0,0120 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,604 | 0,607 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,229 | 0,221 | 0,008 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,020 | 0,026 | 0,006 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,038 | 0,011 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,614 | 0,614 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,062 | 0,063 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,079 | 0,018 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,110 | 0,111 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,054 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,190 | 0,004 | ✅ |

## CCAA:15

- Población `2026-01-01_CCAA_15_100000_s1`: 99.998 personas (pedidas 100.000) de 690.044 residentes (1 por 6,9).
- Donantes: 90,1 % locales; personas por nivel: ccaa_parecidas 9.931, mismo_territorio 90.067; 24.899 unidades donantes, Kish 14.718 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0018). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0095 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0056 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0015 | 0,0032 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0101 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0079 | 0,0098 | 0,050 | ✅ |
| tamano_municipio | 0,0249 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0236 | 0,0112 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,621 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,220 | 0,208 | 0,012 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,013 | 0,003 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,043 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,630 | 0,630 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,072 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,041 | 0,050 | 0,009 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,108 | 0,109 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,177 | 0,185 | 0,008 | ✅ |

## CCAA:16

- Población `2026-01-01_CCAA_16_100000_s1`: 100.027 personas (pedidas 100.000) de 2.253.019 residentes (1 por 22,5).
- Donantes: 97,9 % locales; personas por nivel: ccaa_parecidas 2.146, mismo_territorio 97.881; 41.880 unidades donantes, Kish 29.669 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 29 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0252 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0111 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0028 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0119 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0050 | 0,0091 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0082 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0150 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0193 | 0,0107 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,617 | 0,624 | 0,007 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,225 | 0,219 | 0,007 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,010 | 0,004 | 0,006 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,064 | 0,016 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,645 | 0,646 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,084 | 0,084 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,049 | 0,051 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,121 | 0,122 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,066 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,195 | 0,004 | ✅ |

## CCAA:17

- Población `2026-01-01_CCAA_17_100000_s1`: 99.978 personas (pedidas 100.000) de 329.550 residentes (1 por 3,3).
- Donantes: 87,9 % locales; personas por nivel: ccaa_parecidas 12.094, mismo_territorio 87.884; 14.487 unidades donantes, Kish 8.627 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0016). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0083 | 0,0086 | 0,050 | ✅ |
| actividad_sexo | 0,0041 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0026 | 0,0029 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0125 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0103 | 0,0095 | 0,050 | ✅ |
| tamano_municipio | 0,0197 | 0,0036 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0194 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,619 | 0,622 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,233 | 0,223 | 0,010 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,036 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,046 | 0,042 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,624 | 0,624 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,070 | 0,070 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,038 | 0,040 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,116 | 0,118 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,049 | 0,048 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,192 | 0,002 | ✅ |

## CCAA:18

- Población `2026-01-01_CCAA_18_100000_s1`: 99.960 personas (pedidas 100.000) de 84.196 residentes (1 por 0,8).
- Donantes: 99,4 % locales; personas por nivel: ccaa_parecidas 573, mismo_territorio 99.387; 2.533 unidades donantes, Kish 994 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0007). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0220 | 0,0096 | 0,050 | ✅ |
| actividad_sexo | 0,0071 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0006 | 0,0027 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0221 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0091 | 0,0072 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0421 | 0,0132 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,589 | 0,593 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,262 | 0,003 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,087 | 0,090 | 0,002 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,069 | 0,094 | 0,024 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,054 | 0,054 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,029 | 0,035 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,079 | 0,085 | 0,006 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,040 | 0,040 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,168 | 0,020 | ✅ |

## CCAA:19

- Población `2026-01-01_CCAA_19_100000_s1`: 100.019 personas (pedidas 100.000) de 86.908 residentes (1 por 0,9).
- Donantes: 97,4 % locales; personas por nivel: ccaa_parecidas 2.588, mismo_territorio 97.431; 2.740 unidades donantes, Kish 1.315 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 17 (TVD media 0,0008). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 12 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0190 | 0,0094 | 0,050 | ✅ |
| actividad_sexo | 0,0051 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0044 | 0,0030 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0207 | 0,0104 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0297 | 0,0083 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0297 | 0,0132 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,596 | 0,599 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,231 | 0,219 | 0,012 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,107 | 0,112 | 0,005 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,039 | 0,021 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,618 | 0,618 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,052 | 0,051 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,067 | 0,052 | 0,014 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,092 | 0,104 | 0,012 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,030 | 0,030 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,190 | 0,187 | 0,003 | ✅ |

## PROV:28

- Población `2026-01-01_PROV_28_50000_s1`: 49.967 personas (pedidas 50.000) de 7.168.876 residentes (1 por 143,5).
- Donantes: 95,8 % locales; personas por nivel: ccaa_parecidas 1.884, espana 195, mismo_territorio 47.888; 19.454 unidades donantes, Kish 14.705 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0033). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0121 | 0,0122 | 0,080 | ✅ |
| actividad_sexo | 0,0070 | 0,0078 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0003 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0095 | 0,0153 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0066 | 0,0152 | 0,080 | ✅ |
| tamano_municipio | 0,0271 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0163 | 0,0161 | 0,080 | ✅ |

## PROV:08

- Población `2026-01-01_PROV_08_50000_s1`: 49.987 personas (pedidas 50.000) de 6.008.837 residentes (1 por 120,2).
- Donantes: 97,3 % locales; personas por nivel: ccaa_parecidas 984, espana 141, misma_ccaa_mismo_grado_urbanizacion 235, mismo_territorio 48.627; 19.897 unidades donantes, Kish 15.086 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0033). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0116 | 0,0123 | 0,080 | ✅ |
| actividad_sexo | 0,0079 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0024 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0117 | 0,0155 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0100 | 0,0151 | 0,080 | ✅ |
| tamano_municipio | 0,0357 | 0,0060 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0201 | 0,0161 | 0,080 | ✅ |

## PROV:42

- Población `2026-01-01_PROV_42_50000_s1`: 50.000 personas (pedidas 50.000) de 90.824 residentes (1 por 1,8).
- Donantes: 94,4 % locales; personas por nivel: ccaa_parecidas 262, misma_ccaa_mismo_grado_urbanizacion 2.524, mismo_territorio 47.214; 3.972 unidades donantes, Kish 1.929 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0179 | 0,0122 | 0,080 | ✅ |
| actividad_sexo | 0,0071 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0021 | 0,0043 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0256 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0262 | 0,0134 | 0,080 | ✅ |
| tamano_municipio | 0,0176 | 0,0049 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0298 | 0,0151 | 0,080 | ✅ |

## PROV:44

- Población `2026-01-01_PROV_44_50000_s1`: 50.013 personas (pedidas 50.000) de 137.173 residentes (1 por 2,7).
- Donantes: 94,7 % locales; personas por nivel: ccaa_parecidas 464, misma_ccaa_mismo_grado_urbanizacion 2.192, mismo_territorio 47.357; 5.637 unidades donantes, Kish 2.720 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0138 | 0,0131 | 0,080 | ✅ |
| actividad_sexo | 0,0061 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0022 | 0,0044 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0174 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0173 | 0,0132 | 0,080 | ✅ |
| tamano_municipio | 0,0245 | 0,0049 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0269 | 0,0151 | 0,080 | ✅ |

## PROV:04

- Población `2026-01-01_PROV_04_50000_s1`: 50.004 personas (pedidas 50.000) de 782.945 residentes (1 por 15,7).
- Donantes: 88,2 % locales; personas por nivel: ccaa_parecidas 899, misma_ccaa_mismo_grado_urbanizacion 5.011, mismo_territorio 44.094; 18.094 unidades donantes, Kish 11.666 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0045). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0130 | 0,0128 | 0,080 | ✅ |
| actividad_sexo | 0,0057 | 0,0075 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0047 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0085 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0129 | 0,0149 | 0,080 | ✅ |
| tamano_municipio | 0,0554 | 0,0054 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0150 | 0,0160 | 0,080 | ✅ |

## PROV:35

- Población `2026-01-01_PROV_35_50000_s1`: 49.973 personas (pedidas 50.000) de 1.181.260 residentes (1 por 23,6).
- Donantes: 97,4 % locales; personas por nivel: ccaa_parecidas 885, misma_ccaa_mismo_grado_urbanizacion 426, mismo_territorio 48.662; 18.372 unidades donantes, Kish 12.369 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0034). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0139 | 0,0132 | 0,080 | ✅ |
| actividad_sexo | 0,0088 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0028 | 0,0042 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0105 | 0,0154 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0068 | 0,0144 | 0,080 | ✅ |
| tamano_municipio | 0,0119 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0175 | 0,0167 | 0,080 | ✅ |

## PROV:20

- Población `2026-01-01_PROV_20_50000_s1`: 50.007 personas (pedidas 50.000) de 735.369 residentes (1 por 14,7).
- Donantes: 97,4 % locales; personas por nivel: ccaa_parecidas 707, misma_ccaa_mismo_grado_urbanizacion 584, mismo_territorio 48.716; 19.548 unidades donantes, Kish 12.252 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0236 | 0,0122 | 0,080 | ✅ |
| actividad_sexo | 0,0099 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0005 | 0,0043 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0126 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0090 | 0,0131 | 0,080 | ✅ |
| tamano_municipio | 0,0209 | 0,0055 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0206 | 0,0152 | 0,080 | ✅ |

## PROV:32

- Población `2026-01-01_PROV_32_50000_s1`: 50.009 personas (pedidas 50.000) de 306.524 residentes (1 por 6,1).
- Donantes: 94,5 % locales; personas por nivel: ccaa_parecidas 1.677, misma_ccaa_mismo_grado_urbanizacion 1.062, mismo_territorio 47.270; 12.773 unidades donantes, Kish 7.592 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0164 | 0,0122 | 0,080 | ✅ |
| actividad_sexo | 0,0079 | 0,0078 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0013 | 0,0038 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0133 | 0,0153 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0105 | 0,0123 | 0,080 | ✅ |
| tamano_municipio | 0,0037 | 0,0054 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0105 | 0,0142 | 0,080 | ✅ |

## PROV:51

- Población `2026-01-01_PROV_51_50000_s1`: 50.025 personas (pedidas 50.000) de 84.196 residentes (1 por 1,7).
- Donantes: 99,4 % locales; personas por nivel: ccaa_parecidas 276, mismo_territorio 49.749; 2.524 unidades donantes, Kish 995 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0012). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0224 | 0,0132 | 0,080 | ✅ |
| actividad_sexo | 0,0069 | 0,0081 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0008 | 0,0045 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0224 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0092 | 0,0105 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0420 | 0,0186 | 0,080 | ✅ |

## PROV:52

- Población `2026-01-01_PROV_52_50000_s1`: 50.016 personas (pedidas 50.000) de 86.908 residentes (1 por 1,7).
- Donantes: 97,4 % locales; personas por nivel: ccaa_parecidas 1.281, mismo_territorio 48.735; 2.728 unidades donantes, Kish 1.316 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 17 (TVD media 0,0014). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 6 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0192 | 0,0131 | 0,080 | ✅ |
| actividad_sexo | 0,0049 | 0,0080 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0040 | 0,0047 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0205 | 0,0147 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0299 | 0,0117 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0296 | 0,0188 | 0,080 | ✅ |

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

- Población `2026-01-01_MUNIS_ejemplo_teruel_rural_20000_s1`: 19.994 personas (pedidas 20.000) de 53.706 residentes (1 por 2,7).
- Donantes: 0,0 % locales; personas por nivel: ccaa_parecidas 9, misma_ccaa_mismo_grado_urbanizacion 80, misma_provincia 19.905; 2.343 unidades donantes, Kish 1.175 (mínimo 200).
- Confianza esperada: baja (reducida: menos del 50 % de donantes locales).
- V-MARG: 0 fallos de 6 (TVD media 0,0017). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 1 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0022 | 0,0063 | 0,080 | ✅ |
