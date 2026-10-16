# Fase 05 · Generador territorial

**Estado:** en revisión humana (G5.6). G5.1-G5.5 superadas (`fase_05_puerta.md`).
**Fecha:** 2026-10-16 · **Versión del código:** ver `fase_05_puerta.md`
**Comando para reproducir:**

```bash
sinpop targets --territory all              # objetivos (F3), con nacionalidad_edad (D-042 A)
for m in configs/territorios/*.yaml; do sinpop targets --territory "MUNIS:$m"; done
python tools/generar_territorios_ejemplo.py # listas de municipios de ejemplo (desde el Padrón)
python -m sinpop.validate.fase5             # 31 territorios, España a 1M, coherencia, reservado y anexo (≈ 1,5 h)
sinpop validate --phase 5                   # reports/fase_05_puerta.md
sinpop build --territory PROV:44 --size 20000 --seed 7   # un territorio cualquiera
```

La serie se puede partir en varios procesos con `--reanudar`, porque las poblaciones son deterministas con la semilla. `--coherencia` recalcula solo V-COHERENCIA y `--anexo` regenera solo el anexo.

## Resumen

El generador produce cualquier territorio con el mismo código que la población nacional. Los territorios pueden ser una comunidad, una provincia o una lista de municipios. Cada territorio se genera con sus objetivos de F3, sus donantes y la jerarquía de donantes de `territories.yaml` (D-041). Cada población informa en `metadata.json` de:

- la proporción de donantes locales;
- las personas por nivel de la jerarquía;
- el tamaño efectivo de Kish de los donantes;
- su confianza esperada.

| Puerta | Criterio | Resultado | |
| --- | --- | --- | --- |
| G5.1 | V-MARG y reglas duras en todos los territorios | 0 fallos en 361 marginales de 31 territorios; 0 violaciones | ✅ |
| G5.2 | Cruces reservados por comunidad (V-CRUCE, V de Cramér) | 0 fallos y 1 excepción documentada (Ceuta, D-042 C); V de Cramér 0 fuera, Δ máx. 0,022 | ✅ |
| G5.3 | V-COHERENCIA (19 comunidades frente a España a 1M) | 19 de 19 dentro; máx. 0,0024 sin contar los colectivos (0,0086) | ✅ |
| G5.4 | V-DONANTES | Kish mínimo 1.310 (≥ 200); proporción local informada; confianza reducida solo en Teruel rural | ✅ |
| G5.5 | Ceuta, Melilla y 2 provincias de menos de 150.000 habitantes | Ceuta, Melilla, Soria y Teruel generadas, con su confianza | ✅ |
| G5.6 | Revisión humana | pendiente | ⏸️ |

## Problemas encontrados y resueltos (D-042)

La primera serie F5 fallaba en G5.2 y G5.3. El responsable delegó la elección de la estrategia, con la indicación de que interesan los mayores de 18 años y de ceñirse a las instrucciones.

1. **A · Nacionalidad por edad, calibrada.**
   - **Problema:** solo se calibraba el total de cada nacionalidad. Los hogares extranjeros de 2021 se ponderaban hacia arriba con sus hijos, mientras que el crecimiento real desde 2021 ha sido de adultos. Resultado: demasiados niños extranjeros y **los extranjeros adultos entre un 0 % y un 8 % por debajo de la cifra oficial** (Ceuta −7,6 %, Melilla −7,1 %, Baleares −5,7 %, Cataluña −3,6 %). Eso inflaba el universo con derecho a voto.
   - **Solución:** se calibra española/extranjera × edad quinquenal, con las celdas oficiales de la ECP 2026.
   - **Resultado:** los extranjeros adultos quedan **a ±0,8 % de la cifra oficial** en las 19 comunidades, y la V de Cramér de nacionalidad × mayoría de edad, a ±0,006 de la oficial.
   - Las series F3 y F4 se rehicieron; la puerta F4 se sigue superando (`fase_04.md`).
2. **B · Margen de muestreo en V-COHERENCIA**, como en V-MARG y V-CRUCE (D-038 A). Los colectivos son pocos en cada población (unas 7.300 personas por lado). Dos muestras perfectas de ese tamaño ya difieren en 0,037 de media. Solo cambia su umbral (0,0568); el resto sigue con 0,01 y 0,02.
3. **C · Excepción documentada en Ceuta** para `tipo_hogar_edad4_ref` (0,054 frente a 0,05).
   - **Causa:** la edad de la persona de referencia del objetivo es la de 2021. El desfase es sistemático en todos los territorios (0,02-0,05), y Ceuta es la única comunidad que cruza el umbral.
   - **Sin fuente más reciente:** se buscó en el INE (API Tempus). La ECP y el Censo Anual solo publican hogares por tamaño.

Otros cambios de código, sin cambio de método:

- España se calibra componiendo, un bloque cada vez, las calibraciones de sus comunidades. Es el mismo cálculo; de otro modo no cabía en memoria a 1M.
- `construir` suelta los donantes tras ponderar.
- En la prueba del territorio reservado, V-MARG del resto ya no cuenta los objetivos retirados.

## Tabla resumen por territorio

Semilla 1. Comunidades con 100.000 personas, provincias con 50.000 y listas de municipios con 20.000. V-CRUCE cuenta todos los niveles; en las comunidades, el nivel propio usa el umbral 0,05, las provincias 0,08 y España 0,03 (D-041.6). «Cramér fuera» solo se exige en las comunidades.

| Territorio | Residentes | N pedido / obtenido | V-MARG | V-CRUCE | Cramér fuera | Reglas duras | Local | Kish donantes | Confianza |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| CCAA:01 | 8.751.219 | 100.000 / 100.011 | 0/12 | 0/64 | 0 | 0 | 99,9 % | 30.483 | media-alta |
| CCAA:02 | 1.382.035 | 100.000 / 100.050 | 0/12 | 0/29 | 0 | 0 | 100,0 % | 27.314 | media-alta |
| CCAA:03 | 1.021.627 | 100.000 / 99.994 | 0/12 | 0/14 | 0 | 0 | 99,6 % | 25.437 | media-alta |
| CCAA:04 | 1.260.336 | 100.000 / 100.002 | 0/12 | 0/14 | 0 | 0 | 100,0 % | 21.347 | media-alta |
| CCAA:05 | 2.276.245 | 100.000 / 99.980 | 0/12 | 0/22 | 0 | 0 | 100,0 % | 27.268 | media-alta |
| CCAA:06 | 597.088 | 100.000 / 99.997 | 0/12 | 0/14 | 0 | 0 | 100,0 % | 15.307 | media-alta |
| CCAA:07 | 2.419.181 | 100.000 / 99.982 | 0/12 | 0/71 (+1 exc.) | 0 | 0 | 99,7 % | 31.920 | media-alta |
| CCAA:08 | 2.155.201 | 100.000 / 99.975 | 0/12 | 0/43 | 0 | 0 | 100,0 % | 28.419 | media-alta |
| CCAA:09 | 8.202.041 | 100.000 / 100.034 | 0/12 | 0/36 | 0 | 0 | 100,0 % | 29.692 | media-alta |
| CCAA:10 | 5.529.081 | 100.000 / 99.992 | 0/12 | 0/29 | 0 | 0 | 100,0 % | 30.496 | media-alta |
| CCAA:11 | 1.055.386 | 100.000 / 100.038 | 0/12 | 0/22 | 0 | 0 | 99,9 % | 27.287 | media-alta |
| CCAA:12 | 2.728.430 | 100.000 / 100.004 | 0/12 | 0/36 | 0 | 0 | 99,7 % | 31.051 | media-alta |
| CCAA:13 | 7.168.876 | 100.000 / 99.993 | 0/12 | 0/14 | 0 | 0 | 100,0 % | 29.373 | media-alta |
| CCAA:14 | 1.605.913 | 100.000 / 99.999 | 0/12 | 0/14 | 0 | 0 | 100,0 % | 26.368 | media-alta |
| CCAA:15 | 690.044 | 100.000 / 99.975 | 0/12 | 0/14 | 0 | 0 | 100,0 % | 15.867 | media-alta |
| CCAA:16 | 2.253.019 | 100.000 / 100.012 | 0/12 | 0/29 | 0 | 0 | 100,0 % | 31.511 | media-alta |
| CCAA:17 | 329.550 | 100.000 / 100.003 | 0/12 | 0/14 | 0 | 0 | 99,8 % | 8.424 | media-alta |
| CCAA:18 | 84.196 | 100.000 / 99.976 | 0/12 | 0/12 (+1 exc.) | 0 | 0 | 99,7 % | 1.626 | media-alta |
| CCAA:19 | 86.908 | 100.000 / 100.009 | 0/12 | 0/12 | 0 | 0 | 97,8 % | 1.833 | media-alta |
| PROV:28 | 7.168.876 | 50.000 / 49.970 | 0/12 | 0/7 | — | 0 | 100,0 % | 14.733 | media |
| PROV:08 | 6.008.837 | 50.000 / 50.013 | 0/12 | 0/7 | — | 0 | 100,0 % | 15.040 | media |
| PROV:42 | 90.824 | 50.000 / 50.001 | 0/12 | 0/7 | — | 0 | 99,0 % | 2.250 | media |
| PROV:44 | 137.173 | 50.000 / 50.000 | 0/12 | 0/7 | — | 0 | 98,1 % | 3.385 | media |
| PROV:04 | 782.945 | 50.000 / 50.004 | 0/12 | 0/7 | — | 0 | 99,6 % | 12.855 | media |
| PROV:35 | 1.181.260 | 50.000 / 50.015 | 0/12 | 0/7 | — | 0 | 100,0 % | 13.593 | media |
| PROV:20 | 735.369 | 50.000 / 49.990 | 0/12 | 0/7 | — | 0 | 99,8 % | 14.486 | media |
| PROV:32 | 306.524 | 50.000 / 49.991 | 0/12 | 0/7 | — | 0 | 98,8 % | 8.244 | media |
| PROV:51 | 84.196 | 50.000 / 50.005 | 0/12 | 0/6 | — | 0 | 99,7 % | 1.616 | media |
| PROV:52 | 86.908 | 50.000 / 49.990 | 0/12 | 0/6 | — | 0 | 97,8 % | 1.822 | media |
| MUNIS:ejemplo_valencia_urbano | 1.273.589 | 20.000 / 19.987 | 0/7 | 0/2 | — | 0 | 98,5 % | 6.104 | baja |
| MUNIS:ejemplo_teruel_rural | 53.706 | 20.000 / 19.997 | 0/6 | 0/1 | — | 0 | 0,0 % | 1.310 | baja (reducida) |

Ceuta y Melilla se generan con 100.000 personas, más que sus residentes (84.196 y 86.908). La integerización (TRS) replica las unidades calibradas, así que hay hogares donantes repetidos. Es una prueba de estrés del método; en el uso normal, N es menor que los residentes.

## Prueba de coherencia entre niveles (V-COHERENCIA)

Las 19 poblaciones autonómicas, cada persona con peso = residentes de su comunidad / tamaño, frente a España con 1.000.000 de personas (`2026-01-01_ES_1000000_s1`). Umbral: máx(0,01 calibradas o 0,02 reservadas, 1,2 × TVD_ref de dos muestras + 0,002) (D-042 B).

| Uso | Objetivo | TVD | Umbral | |
| --- | --- | ---: | ---: | --- |
| calibrar | actividad_sexo | 0,0005 | 0,0100 | ✅ |
| calibrar | edad5_sexo | 0,0009 | 0,0100 | ✅ |
| calibrar | edad5_sexo_colectivos | 0,0086 | 0,0568 | ✅ |
| calibrar | edad5_sexo_familiares | 0,0009 | 0,0100 | ✅ |
| calibrar | estudios_edad | 0,0009 | 0,0100 | ✅ |
| calibrar | nacionalidad | 0,0002 | 0,0100 | ✅ |
| calibrar | nacionalidad_edad | 0,0008 | 0,0100 | ✅ |
| calibrar | nacionalidad_top | 0,0002 | 0,0100 | ✅ |
| calibrar | tamano_hogar | 0,0002 | 0,0100 | ✅ |
| calibrar | tipo_hogar | 0,0005 | 0,0100 | ✅ |
| calibrar | urbanizacion | 0,0002 | 0,0100 | ✅ |
| reservar | actividad_edad | 0,0015 | 0,0200 | ✅ |
| reservar | adultos_nacionalidad | 0,0002 | 0,0200 | ✅ |
| reservar | estado_civil_edad | 0,0019 | 0,0200 | ✅ |
| reservar | estudios_sexo_edad | 0,0024 | 0,0200 | ✅ |
| reservar | nacionalidad_top_sexo_edad | 0,0022 | 0,0200 | ✅ |
| reservar | provincia_si_calibra_ccaa | 0,0011 | 0,0200 | ✅ |
| reservar | tamano_municipio | 0,0006 | 0,0200 | ✅ |
| reservar | tipo_hogar_edad4_ref | 0,0011 | 0,0200 | ✅ |

## Prueba del territorio reservado

Galicia (CCAA:12) calibrada sin sus objetivos socioeconómicos, relación con la actividad × sexo y estudios × edad. Esos dos objetivos se comprueban después como reservados, con el umbral de comunidad: máx(1,2 × TVD_ref + 0,002; 0,05).

| Objetivo retirado | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_sexo | 0,0379 | 0,0056 | 0,050 | ✅ |
| estudios_edad | 0,0366 | 0,0079 | 0,050 | ✅ |

El resto de marginales calibradas: 0 fallos de 10.

Sin calibrarlos, la actividad y los estudios se desvían alrededor de 0,04 de la cifra oficial, frente a 0,0017 y 0,0019 en la serie calibrada. Quedan dentro del umbral de comunidad, así que la estructura demográfica y del hogar que aportan los donantes transmite buena parte de la información socioeconómica. Aun así, calibrarlos reduce mucho el error, y por eso se mantienen calibrados.

## Donantes y confianza

- **Comunidades y provincias:** 97,8 % (Melilla) a 100 % de donantes locales. Las unidades no locales vienen de las comunidades parecidas (D-041.2). Kish de los donantes ≥ 1.616 (Ceuta).
- **Lista urbana** (València y 11 municipios de L'Horta): 98,5 % locales, porque los municipios de más de 10.000 habitantes están identificados en el Censo.
- **Lista rural** (226 municipios de Teruel de menos de 2.000 habitantes): 0 % locales por diseño. El Censo no identifica municipios pequeños, así que los donantes son los hogares de su provincia y clase de tamaño (19.813 personas de la misma provincia), más 177 de la misma comunidad y grado de urbanización y 7 de comunidades parecidas. Confianza **baja y reducida**, con el municipio de cada hogar asignado al azar en proporción a la población (`modelada`).

## Anexo por territorio

Una sección por territorio en [`fase_05_anexo.md`](fase_05_anexo.md), con:

- donantes por nivel, Kish y confianza;
- V-MARG;
- cada cruce reservado del nivel propio (TVD, TVD_ref, umbral);
- en las comunidades, la V de Cramér de cada par.

Los CSV de cada comprobación están en `reports/fase_05/`. El ensayo previo de D-042 A está en `reports/fase_05/ensayo_d042.json` (`tools/ensayo_d042.py`).
