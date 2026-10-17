# F5 · Anexo por territorio

Generado desde `fase_05_validacion.json` (`python -m sinpop.validate.fase5 --anexo`). Semilla 1. Detalle de cada comprobación en `reports/fase_05/`.

## CCAA:01

- Población `2026-01-01_CCAA_01_100000_s1`: 99.972 personas (pedidas 100.000) de 8.751.219 residentes (1 por 87,5).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 401, espana 674, mismo_territorio 98.897; 39.799 unidades donantes, Kish 30.479 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0037). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 73 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0097 | 0,0093 | 0,050 | ✅ |
| actividad_sexo | 0,0201 | 0,0059 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0016 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0279 | 0,0062 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0072 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0086 | 0,0096 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0214 | 0,0047 | 0,050 | ✅ |
| tamano_municipio | 0,0143 | 0,0044 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0309 | 0,0112 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,616 | 0,000 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,251 | 0,212 | 0,039 | ❌ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,015 | 0,017 | 0,002 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,630 | 0,638 | 0,008 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,039 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,065 | 0,068 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,043 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,086 | 0,088 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,054 | 0,002 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,196 | 0,009 | ✅ |

## CCAA:02

- Población `2026-01-01_CCAA_02_100000_s1`: 100.004 personas (pedidas 100.000) de 1.382.035 residentes (1 por 13,8).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 307, espana 6, mismo_territorio 99.691; 38.679 unidades donantes, Kish 21.621 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 33 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0095 | 0,0085 | 0,050 | ✅ |
| actividad_sexo | 0,0157 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0009 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0209 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0090 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0131 | 0,0099 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0048 | 0,0027 | 0,050 | ✅ |
| tamano_municipio | 0,0106 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0298 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,616 | 0,620 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,254 | 0,231 | 0,022 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,022 | 0,021 | 0,000 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,627 | 0,633 | 0,006 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,037 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,627 | 0,627 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,078 | 0,079 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,050 | 0,046 | 0,004 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,124 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,062 | 0,063 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,183 | 0,192 | 0,009 | ✅ |

## CCAA:03

- Población `2026-01-01_CCAA_03_100000_s1`: 100.019 personas (pedidas 100.000) de 1.021.627 residentes (1 por 10,2).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 972, espana 92, mismo_territorio 98.955; 36.795 unidades donantes, Kish 19.683 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 16 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0110 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0138 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0020 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0296 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0122 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0089 | 0,0089 | 0,050 | ✅ |
| tamano_municipio | 0,0058 | 0,0039 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0312 | 0,0099 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,618 | 0,622 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,293 | 0,276 | 0,016 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,035 | 0,035 | 0,001 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,623 | 0,630 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,039 | 0,054 | 0,014 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,635 | 0,635 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,088 | 0,088 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,031 | 0,035 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,102 | 0,102 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,069 | 0,069 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,176 | 0,010 | ✅ |

## CCAA:04

- Población `2026-01-01_CCAA_04_100000_s1`: 99.976 personas (pedidas 100.000) de 1.260.336 residentes (1 por 12,6).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 62, mismo_territorio 99.914; 29.951 unidades donantes, Kish 15.771 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0025). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 16 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0112 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0182 | 0,0051 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0024 | 0,0032 | 0,050 | ✅ |
| estado_civil_edad | 0,0350 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0079 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0157 | 0,0115 | 0,050 | ✅ |
| tamano_municipio | 0,0188 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0380 | 0,0118 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,603 | 0,611 | 0,008 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,167 | 0,118 | 0,048 | ❌ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,034 | 0,033 | 0,001 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,614 | 0,623 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,058 | 0,057 | 0,001 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,060 | 0,061 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,046 | 0,049 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,106 | 0,111 | 0,005 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,049 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,160 | 0,002 | ✅ |

## CCAA:05

- Población `2026-01-01_CCAA_05_100000_s1`: 99.968 personas (pedidas 100.000) de 2.276.245 residentes (1 por 22,8).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 1.110, mismo_territorio 98.858; 37.286 unidades donantes, Kish 21.813 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0033). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 25 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0119 | 0,0091 | 0,050 | ✅ |
| actividad_sexo | 0,0192 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0026 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0438 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0096 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0104 | 0,0103 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0019 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0077 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0456 | 0,0118 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,606 | 0,609 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,206 | 0,164 | 0,042 | ❌ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,009 | 0,010 | 0,001 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,613 | 0,623 | 0,010 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,056 | 0,054 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,615 | 0,615 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,057 | 0,057 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,039 | 0,036 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,077 | 0,079 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,043 | 0,043 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,148 | 0,151 | 0,003 | ✅ |

## CCAA:06

- Población `2026-01-01_CCAA_06_100000_s1`: 100.006 personas (pedidas 100.000) de 597.088 residentes (1 por 6,0).
- Donantes: 99,8 % locales; personas por nivel: ccaa_parecidas 220, mismo_territorio 99.786; 22.315 unidades donantes, Kish 12.837 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0019). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 16 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0107 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0067 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0018 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0261 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0122 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0097 | 0,0089 | 0,050 | ✅ |
| tamano_municipio | 0,0060 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0371 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,623 | 0,627 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,256 | 0,009 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,017 | 0,015 | 0,002 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,623 | 0,632 | 0,008 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,040 | 0,036 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,633 | 0,633 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,082 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,030 | 0,036 | 0,006 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,095 | 0,097 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,059 | 0,060 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,166 | 0,172 | 0,006 | ✅ |

## CCAA:07

- Población `2026-01-01_CCAA_07_100000_s1`: 99.991 personas (pedidas 100.000) de 2.419.181 residentes (1 por 24,2).
- Donantes: 99,5 % locales; personas por nivel: ccaa_parecidas 407, espana 123, mismo_territorio 99.461; 44.122 unidades donantes, Kish 31.426 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0029). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 81 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0120 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0126 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0015 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0279 | 0,0064 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0100 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0072 | 0,0088 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0130 | 0,0047 | 0,050 | ✅ |
| tamano_municipio | 0,0077 | 0,0040 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0267 | 0,0103 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,625 | 0,005 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,278 | 0,282 | 0,004 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,041 | 0,000 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,620 | 0,628 | 0,008 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,048 | 0,004 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,632 | 0,632 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,080 | 0,078 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,032 | 0,041 | 0,009 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,111 | 0,111 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,053 | 0,052 | 0,002 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,162 | 0,171 | 0,009 | ✅ |

## CCAA:08

- Población `2026-01-01_CCAA_08_100000_s1`: 99.972 personas (pedidas 100.000) de 2.155.201 residentes (1 por 21,6).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 285, mismo_territorio 99.687; 38.987 unidades donantes, Kish 24.830 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0031). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 49 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0111 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0199 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0013 | 0,0031 | 0,050 | ✅ |
| estado_civil_edad | 0,0268 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0107 | 0,0107 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0118 | 0,0097 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0169 | 0,0040 | 0,050 | ✅ |
| tamano_municipio | 0,0136 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0280 | 0,0112 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,616 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,302 | 0,301 | 0,001 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,024 | 0,022 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,632 | 0,642 | 0,010 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,042 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,067 | 0,065 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,038 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,104 | 0,104 | 0,000 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,051 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,196 | 0,006 | ✅ |

## CCAA:09

- Población `2026-01-01_CCAA_09_100000_s1`: 99.995 personas (pedidas 100.000) de 8.202.041 residentes (1 por 82,0).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 23, espana 64, mismo_territorio 99.908; 39.763 unidades donantes, Kish 29.965 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0030). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 41 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0089 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0135 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0022 | 0,0031 | 0,050 | ✅ |
| estado_civil_edad | 0,0343 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0077 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0138 | 0,0106 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0067 | 0,0029 | 0,050 | ✅ |
| tamano_municipio | 0,0239 | 0,0041 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0326 | 0,0121 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,613 | 0,617 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,174 | 0,139 | 0,035 | ❌ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,018 | 0,021 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,635 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,042 | 0,035 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,076 | 0,077 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,056 | 0,005 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,125 | 0,126 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,065 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,191 | 0,196 | 0,004 | ✅ |

## CCAA:10

- Población `2026-01-01_CCAA_10_100000_s1`: 99.993 personas (pedidas 100.000) de 5.529.081 residentes (1 por 55,3).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 55, espana 92, mismo_territorio 99.846; 40.434 unidades donantes, Kish 30.566 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0035). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 33 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0104 | 0,0089 | 0,050 | ✅ |
| actividad_sexo | 0,0227 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0014 | 0,0031 | 0,050 | ✅ |
| estado_civil_edad | 0,0280 | 0,0064 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0078 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0137 | 0,0108 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0142 | 0,0032 | 0,050 | ✅ |
| tamano_municipio | 0,0208 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0271 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,614 | 0,617 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,222 | 0,166 | 0,056 | ❌ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,001 | 0,001 | 0,000 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,635 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,043 | 0,035 | 0,008 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,066 | 0,066 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,043 | 0,043 | 0,000 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,117 | 0,119 | 0,002 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,055 | 0,055 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,193 | 0,196 | 0,004 | ✅ |

## CCAA:11

- Población `2026-01-01_CCAA_11_100000_s1`: 99.985 personas (pedidas 100.000) de 1.055.386 residentes (1 por 10,6).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 322, mismo_territorio 99.663; 36.255 unidades donantes, Kish 23.621 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0028). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 25 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0114 | 0,0091 | 0,050 | ✅ |
| actividad_sexo | 0,0146 | 0,0057 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0015 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0316 | 0,0062 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0097 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0058 | 0,0085 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0106 | 0,0028 | 0,050 | ✅ |
| tamano_municipio | 0,0112 | 0,0042 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0240 | 0,0106 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,620 | 0,624 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,284 | 0,304 | 0,020 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,019 | 0,020 | 0,001 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,634 | 0,648 | 0,014 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,056 | 0,005 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,629 | 0,629 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,073 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,035 | 0,008 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,067 | 0,067 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,048 | 0,049 | 0,002 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,196 | 0,206 | 0,010 | ✅ |

## CCAA:12

- Población `2026-01-01_CCAA_12_100000_s1`: 100.035 personas (pedidas 100.000) de 2.728.430 residentes (1 por 27,3).
- Donantes: 98,8 % locales; personas por nivel: ccaa_parecidas 843, espana 319, mismo_territorio 98.873; 41.631 unidades donantes, Kish 30.513 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0028). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 41 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0077 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0095 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0009 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0289 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0080 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0069 | 0,0084 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0122 | 0,0037 | 0,050 | ✅ |
| tamano_municipio | 0,0105 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0262 | 0,0108 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,622 | 0,622 | 0,000 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,198 | 0,189 | 0,009 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,021 | 0,021 | 0,000 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,622 | 0,629 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,052 | 0,048 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,641 | 0,640 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,081 | 0,080 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,028 | 0,028 | 0,000 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,090 | 0,091 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,064 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,182 | 0,188 | 0,005 | ✅ |

## CCAA:13

- Población `2026-01-01_CCAA_13_100000_s1`: 100.022 personas (pedidas 100.000) de 7.168.876 residentes (1 por 71,7).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 17, espana 84, mismo_territorio 99.921; 38.851 unidades donantes, Kish 29.318 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0027). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 16 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0075 | 0,0086 | 0,050 | ✅ |
| actividad_sexo | 0,0087 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0010 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0278 | 0,0062 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0060 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0106 | 0,0104 | 0,050 | ✅ |
| tamano_municipio | 0,0124 | 0,0039 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0352 | 0,0114 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,618 | 0,620 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,195 | 0,177 | 0,018 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,016 | 0,000 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,621 | 0,628 | 0,006 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,032 | 0,035 | 0,002 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,626 | 0,626 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,074 | 0,076 | 0,002 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,035 | 0,047 | 0,011 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,118 | 0,114 | 0,004 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,064 | 0,065 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,178 | 0,183 | 0,005 | ✅ |

## CCAA:14

- Población `2026-01-01_CCAA_14_100000_s1`: 100.045 personas (pedidas 100.000) de 1.605.913 residentes (1 por 16,1).
- Donantes: 99,7 % locales; personas por nivel: ccaa_parecidas 328, mismo_territorio 99.717; 34.382 unidades donantes, Kish 22.817 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 16 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0080 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0153 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0024 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0279 | 0,0059 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0072 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0141 | 0,0101 | 0,050 | ✅ |
| tamano_municipio | 0,0113 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0344 | 0,0114 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,606 | 0,609 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,228 | 0,209 | 0,019 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,020 | 0,024 | 0,004 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,631 | 0,640 | 0,009 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,041 | 0,007 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,614 | 0,614 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,062 | 0,062 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,061 | 0,080 | 0,018 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,110 | 0,113 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,198 | 0,012 | ✅ |

## CCAA:15

- Población `2026-01-01_CCAA_15_100000_s1`: 100.027 personas (pedidas 100.000) de 690.044 residentes (1 por 6,9).
- Donantes: 99,2 % locales; personas por nivel: ccaa_parecidas 778, mismo_territorio 99.249; 23.767 unidades donantes, Kish 12.580 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 16 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0066 | 0,0088 | 0,050 | ✅ |
| actividad_sexo | 0,0150 | 0,0054 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0030 | 0,050 | ✅ |
| estado_civil_edad | 0,0158 | 0,0062 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0104 | 0,0108 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0122 | 0,0099 | 0,050 | ✅ |
| tamano_municipio | 0,0121 | 0,0038 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0383 | 0,0111 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,623 | 0,624 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,220 | 0,200 | 0,020 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,016 | 0,013 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,602 | 0,603 | 0,000 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,049 | 0,045 | 0,003 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,630 | 0,630 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,071 | 0,071 | 0,001 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,041 | 0,044 | 0,003 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,108 | 0,111 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,176 | 0,189 | 0,013 | ✅ |

## CCAA:16

- Población `2026-01-01_CCAA_16_100000_s1`: 99.997 personas (pedidas 100.000) de 2.253.019 residentes (1 por 22,5).
- Donantes: 98,6 % locales; personas por nivel: ccaa_parecidas 1.248, espana 126, mismo_territorio 98.623; 41.993 unidades donantes, Kish 29.570 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0022). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 33 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0101 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0143 | 0,0053 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0029 | 0,050 | ✅ |
| estado_civil_edad | 0,0300 | 0,0060 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0124 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0076 | 0,0093 | 0,050 | ✅ |
| provincia_si_calibra_ccaa | 0,0118 | 0,0031 | 0,050 | ✅ |
| tamano_municipio | 0,0132 | 0,0037 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0361 | 0,0109 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,621 | 0,624 | 0,004 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,224 | 0,224 | 0,000 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,010 | 0,005 | 0,005 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,624 | 0,629 | 0,006 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,048 | 0,062 | 0,014 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,645 | 0,646 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,084 | 0,083 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,049 | 0,047 | 0,002 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,121 | 0,120 | 0,001 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,065 | 0,065 | 0,001 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,189 | 0,200 | 0,011 | ✅ |

## CCAA:17

- Población `2026-01-01_CCAA_17_100000_s1`: 100.004 personas (pedidas 100.000) de 329.550 residentes (1 por 3,3).
- Donantes: 99,6 % locales; personas por nivel: ccaa_parecidas 354, mismo_territorio 99.650; 13.017 unidades donantes, Kish 7.156 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0016). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 16 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0071 | 0,0084 | 0,050 | ✅ |
| actividad_sexo | 0,0088 | 0,0052 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0022 | 0,0028 | 0,050 | ✅ |
| estado_civil_edad | 0,0222 | 0,0061 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0148 | 0,0109 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0173 | 0,0097 | 0,050 | ✅ |
| tamano_municipio | 0,0018 | 0,0034 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0367 | 0,0109 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,621 | 0,623 | 0,002 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,234 | 0,219 | 0,014 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,041 | 0,038 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,621 | 0,628 | 0,007 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,046 | 0,036 | 0,010 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,624 | 0,623 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,070 | 0,070 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,038 | 0,045 | 0,007 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,116 | 0,120 | 0,003 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,049 | 0,049 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,201 | 0,013 | ✅ |

## CCAA:18

- Población `2026-01-01_CCAA_18_100000_s1`: 99.966 personas (pedidas 100.000) de 84.196 residentes (1 por 0,8).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 1.087, mismo_territorio 98.879; 2.534 unidades donantes, Kish 1.243 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0008). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 1.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0284 | 0,0095 | 0,050 | ✅ |
| actividad_sexo | 0,0160 | 0,0056 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0019 | 0,0027 | 0,050 | ✅ |
| estado_civil_edad | 0,0301 | 0,0057 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0201 | 0,0106 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0086 | 0,0072 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0571 | 0,0129 | 0,050 | ❌ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,594 | 0,602 | 0,007 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,265 | 0,236 | 0,029 | ✅ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,087 | 0,091 | 0,004 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,626 | 0,637 | 0,010 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,069 | 0,087 | 0,017 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,611 | 0,611 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,054 | 0,054 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,029 | 0,052 | 0,023 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,079 | 0,093 | 0,014 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,040 | 0,040 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,187 | 0,185 | 0,002 | ✅ |

## CCAA:19

- Población `2026-01-01_CCAA_19_100000_s1`: 99.984 personas (pedidas 100.000) de 86.908 residentes (1 por 0,9).
- Donantes: 97,5 % locales; personas por nivel: ccaa_parecidas 2.468, espana 62, mismo_territorio 97.454; 2.658 unidades donantes, Kish 1.458 (mínimo 200).
- Confianza esperada: media-alta.
- V-MARG: 0 fallos de 14 (TVD media 0,0011). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 14 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0142 | 0,0090 | 0,050 | ✅ |
| actividad_sexo | 0,0245 | 0,0055 | 0,050 | ✅ |
| adultos_nacionalidad | 0,0051 | 0,0032 | 0,050 | ✅ |
| estado_civil_edad | 0,0174 | 0,0057 | 0,050 | ✅ |
| estudios_sexo_edad | 0,0197 | 0,0104 | 0,050 | ✅ |
| nacionalidad_top_sexo_edad | 0,0234 | 0,0081 | 0,050 | ✅ |
| tipo_hogar_edad4_ref | 0,0346 | 0,0134 | 0,050 | ✅ |

| V de Cramér | Oficial | Sintética | Δ | |
| --- | ---: | ---: | ---: | --- |
| relacion_actividad × edad_actividad (actividad_edad) | 0,601 | 0,604 | 0,003 | ✅ |
| relacion_actividad × sexo (actividad_sexo) | 0,231 | 0,190 | 0,041 | ❌ |
| nacionalidad_esp_ext × es_adulto (adultos_nacionalidad) | 0,107 | 0,110 | 0,003 | ✅ |
| estado_civil × edad_estado_civil (estado_civil_edad) | 0,627 | 0,634 | 0,008 | ✅ |
| estudios_3 × sexo (estudios_sexo_edad) | 0,061 | 0,046 | 0,015 | ✅ |
| estudios_3 × edad_estudios (estudios_sexo_edad) | 0,618 | 0,618 | 0,000 | ✅ |
| sexo × edad_estudios (estudios_sexo_edad) | 0,052 | 0,052 | 0,000 | ✅ |
| nacionalidad_top × sexo (nacionalidad_top_sexo_edad) | 0,067 | 0,053 | 0,013 | ✅ |
| nacionalidad_top × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,092 | 0,102 | 0,010 | ✅ |
| sexo × edad_nacionalidad (nacionalidad_top_sexo_edad) | 0,030 | 0,030 | 0,000 | ✅ |
| tipo_hogar × edad_4 (tipo_hogar_edad4_ref) | 0,188 | 0,193 | 0,004 | ✅ |

## PROV:28

- Población `2026-01-01_PROV_28_50000_s1`: 50.001 personas (pedidas 50.000) de 7.168.876 residentes (1 por 143,4).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 16, espana 41, mismo_territorio 49.944; 19.465 unidades donantes, Kish 14.766 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0037). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 8 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0090 | 0,0123 | 0,080 | ✅ |
| actividad_sexo | 0,0090 | 0,0075 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0009 | 0,0044 | 0,080 | ✅ |
| estado_civil_edad | 0,0289 | 0,0086 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0114 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0122 | 0,0151 | 0,080 | ✅ |
| tamano_municipio | 0,0147 | 0,0056 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0361 | 0,0163 | 0,080 | ✅ |

## PROV:08

- Población `2026-01-01_PROV_08_50000_s1`: 49.948 personas (pedidas 50.000) de 6.008.837 residentes (1 por 120,3).
- Donantes: 99,9 % locales; personas por nivel: ccaa_parecidas 19, espana 34, mismo_territorio 49.895; 19.892 unidades donantes, Kish 15.038 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0035). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 8 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0105 | 0,0127 | 0,080 | ✅ |
| actividad_sexo | 0,0145 | 0,0075 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0028 | 0,0046 | 0,080 | ✅ |
| estado_civil_edad | 0,0311 | 0,0087 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0094 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0161 | 0,0151 | 0,080 | ✅ |
| tamano_municipio | 0,0258 | 0,0061 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0320 | 0,0161 | 0,080 | ✅ |

## PROV:42

- Población `2026-01-01_PROV_42_50000_s1`: 49.990 personas (pedidas 50.000) de 90.824 residentes (1 por 1,8).
- Donantes: 98,6 % locales; personas por nivel: ccaa_parecidas 54, misma_ccaa_mismo_grado_urbanizacion 670, mismo_territorio 49.266; 3.824 unidades donantes, Kish 2.002 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0018). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 8 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0201 | 0,0126 | 0,080 | ✅ |
| actividad_sexo | 0,0136 | 0,0079 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0024 | 0,0043 | 0,080 | ✅ |
| estado_civil_edad | 0,0215 | 0,0087 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0275 | 0,0156 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0304 | 0,0135 | 0,080 | ✅ |
| tamano_municipio | 0,0166 | 0,0048 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0278 | 0,0152 | 0,080 | ✅ |

## PROV:44

- Población `2026-01-01_PROV_44_50000_s1`: 49.993 personas (pedidas 50.000) de 137.173 residentes (1 por 2,7).
- Donantes: 97,6 % locales; personas por nivel: ccaa_parecidas 167, misma_ccaa_mismo_grado_urbanizacion 1.018, mismo_territorio 48.808; 5.504 unidades donantes, Kish 2.904 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0020). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 8 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0152 | 0,0129 | 0,080 | ✅ |
| actividad_sexo | 0,0135 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0016 | 0,0042 | 0,080 | ✅ |
| estado_civil_edad | 0,0227 | 0,0084 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0137 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0276 | 0,0136 | 0,080 | ✅ |
| tamano_municipio | 0,0184 | 0,0047 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0284 | 0,0149 | 0,080 | ✅ |

## PROV:04

- Población `2026-01-01_PROV_04_50000_s1`: 49.977 personas (pedidas 50.000) de 782.945 residentes (1 por 15,7).
- Donantes: 98,8 % locales; personas por nivel: ccaa_parecidas 20, misma_ccaa_mismo_grado_urbanizacion 560, mismo_territorio 49.397; 17.973 unidades donantes, Kish 11.227 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0046). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 8 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0090 | 0,0129 | 0,080 | ✅ |
| actividad_sexo | 0,0289 | 0,0080 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0028 | 0,0044 | 0,080 | ✅ |
| estado_civil_edad | 0,0252 | 0,0085 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0064 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0185 | 0,0150 | 0,080 | ✅ |
| tamano_municipio | 0,0157 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0328 | 0,0164 | 0,080 | ✅ |

## PROV:35

- Población `2026-01-01_PROV_35_50000_s1`: 50.000 personas (pedidas 50.000) de 1.181.260 residentes (1 por 23,6).
- Donantes: 98,7 % locales; personas por nivel: ccaa_parecidas 458, misma_ccaa_mismo_grado_urbanizacion 184, mismo_territorio 49.358; 18.548 unidades donantes, Kish 12.012 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0037). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 8 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0120 | 0,0135 | 0,080 | ✅ |
| actividad_sexo | 0,0133 | 0,0078 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0035 | 0,0042 | 0,080 | ✅ |
| estado_civil_edad | 0,0423 | 0,0084 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0115 | 0,0153 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0124 | 0,0145 | 0,080 | ✅ |
| tamano_municipio | 0,0078 | 0,0053 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0485 | 0,0168 | 0,080 | ✅ |

## PROV:20

- Población `2026-01-01_PROV_20_50000_s1`: 50.013 personas (pedidas 50.000) de 735.369 residentes (1 por 14,7).
- Donantes: 98,1 % locales; personas por nivel: ccaa_parecidas 729, misma_ccaa_mismo_grado_urbanizacion 231, mismo_territorio 49.053; 19.739 unidades donantes, Kish 12.745 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0037). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 8 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0107 | 0,0123 | 0,080 | ✅ |
| actividad_sexo | 0,0111 | 0,0077 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0006 | 0,0043 | 0,080 | ✅ |
| estado_civil_edad | 0,0251 | 0,0083 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0141 | 0,0148 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0107 | 0,0134 | 0,080 | ✅ |
| tamano_municipio | 0,0162 | 0,0052 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0370 | 0,0150 | 0,080 | ✅ |

## PROV:32

- Población `2026-01-01_PROV_32_50000_s1`: 50.005 personas (pedidas 50.000) de 306.524 residentes (1 por 6,1).
- Donantes: 97,5 % locales; personas por nivel: ccaa_parecidas 434, espana 9, misma_ccaa_mismo_grado_urbanizacion 817, mismo_territorio 48.745; 12.566 unidades donantes, Kish 7.135 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0023). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 8 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0145 | 0,0124 | 0,080 | ✅ |
| actividad_sexo | 0,0111 | 0,0082 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0027 | 0,0039 | 0,080 | ✅ |
| estado_civil_edad | 0,0278 | 0,0086 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0138 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0138 | 0,0123 | 0,080 | ✅ |
| tamano_municipio | 0,0091 | 0,0055 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0197 | 0,0152 | 0,080 | ✅ |

## PROV:51

- Población `2026-01-01_PROV_51_50000_s1`: 49.997 personas (pedidas 50.000) de 84.196 residentes (1 por 1,7).
- Donantes: 98,9 % locales; personas por nivel: ccaa_parecidas 553, mismo_territorio 49.444; 2.531 unidades donantes, Kish 1.237 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0015). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0280 | 0,0133 | 0,080 | ✅ |
| actividad_sexo | 0,0156 | 0,0081 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0017 | 0,0042 | 0,080 | ✅ |
| estado_civil_edad | 0,0304 | 0,0086 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0201 | 0,0152 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0089 | 0,0105 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0571 | 0,0179 | 0,080 | ✅ |

## PROV:52

- Población `2026-01-01_PROV_52_50000_s1`: 49.998 personas (pedidas 50.000) de 86.908 residentes (1 por 1,7).
- Donantes: 97,5 % locales; personas por nivel: ccaa_parecidas 1.239, espana 30, mismo_territorio 48.729; 2.657 unidades donantes, Kish 1.454 (mínimo 200).
- Confianza esperada: media.
- V-MARG: 0 fallos de 14 (TVD media 0,0017). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 7 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_edad | 0,0143 | 0,0129 | 0,080 | ✅ |
| actividad_sexo | 0,0244 | 0,0082 | 0,080 | ✅ |
| adultos_nacionalidad | 0,0051 | 0,0047 | 0,080 | ✅ |
| estado_civil_edad | 0,0177 | 0,0080 | 0,080 | ✅ |
| estudios_sexo_edad | 0,0194 | 0,0151 | 0,080 | ✅ |
| nacionalidad_top_sexo_edad | 0,0232 | 0,0115 | 0,080 | ✅ |
| tipo_hogar_edad4_ref | 0,0345 | 0,0190 | 0,080 | ✅ |

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

- Población `2026-01-01_MUNIS_ejemplo_teruel_rural_20000_s1`: 19.989 personas (pedidas 20.000) de 53.706 residentes (1 por 2,7).
- Donantes: 0,0 % locales; personas por nivel: ccaa_parecidas 5, misma_ccaa_mismo_grado_urbanizacion 90, misma_provincia 19.894; 2.350 unidades donantes, Kish 1.183 (mínimo 200).
- Confianza esperada: baja (reducida: menos del 50 % de donantes locales).
- V-MARG: 0 fallos de 6 (TVD media 0,0024). Reglas duras: 0 violaciones.
- V-CRUCE: 0 fallos de 1 (todos los niveles); excepciones 0.

| Cruce reservado (nivel del territorio) | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| adultos_nacionalidad | 0,0027 | 0,0066 | 0,080 | ✅ |
