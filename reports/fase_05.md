# Fase 05 · Generador territorial

**Estado:** en revisión humana (G5.6). La puerta falla en G5.2 y G5.3; propuestas en D-042.
**Fecha:** 2026-10-16 · **Versión del código:** ver `fase_05_puerta.md`
**Comando para reproducir:**

```bash
sinpop targets --territory all              # objetivos (F3)
python tools/generar_territorios_ejemplo.py # listas de municipios de ejemplo (desde el Padrón)
python -m sinpop.validate.fase5             # 31 territorios, España a 1M, coherencia, reservado y anexo
sinpop validate --phase 5                   # reports/fase_05_puerta.md
python tools/ensayo_d042.py                 # ensayo de la propuesta D-042 A
sinpop build --territory PROV:44 --size 20000 --seed 7   # un territorio cualquiera
```

Si falta memoria, la serie se puede partir en varios procesos con `--reanudar`. Las poblaciones son deterministas con la semilla.

## Resumen

El generador produce cualquier territorio con el mismo código que la población nacional. Los territorios pueden ser una comunidad, una provincia o una lista de municipios. Cada territorio se genera con sus objetivos de F3, sus donantes y la jerarquía de donantes de `territories.yaml` (D-041). Cada población informa en `metadata.json` de:

- la proporción de donantes locales;
- las personas por nivel de la jerarquía;
- el tamaño efectivo de Kish de los donantes;
- su confianza esperada.

| Puerta | Criterio | Resultado | |
| --- | --- | --- | --- |
| G5.1 | V-MARG y reglas duras en todos los territorios | 0 fallos en 330 marginales de 31 territorios; 0 violaciones | ✅ |
| G5.2 | Cruces reservados por comunidad (V-CRUCE, V de Cramér) | V-CRUCE: 1 fallo, Ceuta `tipo_hogar_edad4_ref` (0,0518 frente a 0,05). V de Cramér: 7 comunidades fuera en nacionalidad × mayoría de edad | ❌ (D-042 A y C) |
| G5.3 | V-COHERENCIA (19 comunidades frente a España a 1M) | 17 de 18 comparaciones dentro (máx. 0,0025). Colectivos por edad y sexo: 0,0107 frente a 0,01 | ❌ (D-042 B) |
| G5.4 | V-DONANTES | Kish mínimo 1.292 (≥ 200). Proporción local informada; confianza reducida solo en Teruel rural | ✅ |
| G5.5 | Ceuta, Melilla y 2 provincias de menos de 150.000 habitantes | Ceuta, Melilla, Soria y Teruel generadas, con su confianza | ✅ |
| G5.6 | Revisión humana | pendiente | ⏸️ |

## Lo que hay que decidir (D-042)

1. **A · Nacionalidad por edad.** Es un sesgo real que afecta a una minoría. Las 19 comunidades tienen demasiados niños extranjeros, sobre todo de 0 a 4 años: ×1,46 en Cataluña y Madrid y ×2,5 en Ceuta. Además tienen algo pocos adultos extranjeros. La causa es que solo se calibra el total de cada nacionalidad, y los hogares extranjeros de 2021 vienen con sus hijos.
   - **Propuesta:** calibrar española/extranjera × edad quinquenal (ECP 2026).
   - **Ensayo:** la V de Cramér pasa a coincidir con la oficial en ±0,004 en Cataluña, Madrid, Ceuta y Melilla, sin otros cambios.
   - **Si se aprueba:** se rehacen los objetivos y las series F4 y F5.
2. **B · Coherencia de los colectivos.** El 0,0107 está muy por debajo de lo que daría el azar con estos tamaños (0,037 de media). Con pesos, la coherencia es exacta. Se propone el mismo margen de muestreo que V-MARG.
3. **C · Ceuta, tipo de hogar por edad de la persona de referencia.** Es el desfase 2021–2026 del objetivo reservado, ya documentado en D-038: el mismo sesgo aparece en todos los territorios y Ceuta es la única que cruza el umbral. Se propone una excepción documentada, como la de Segovia, o buscar una fuente más reciente en F3.

## Tabla resumen por territorio

Semilla 1. Comunidades con 100.000 personas, provincias con 50.000 y listas de municipios con 20.000. V-CRUCE cuenta todos los niveles; en las comunidades, el nivel propio usa el umbral 0,05, las provincias 0,08 y España 0,03 (D-041.6). «Cramér fuera» solo se exige en las comunidades.

| Territorio | Residentes | N pedido / obtenido | V-MARG | V-CRUCE | Cramér fuera | Reglas duras | Local | Kish donantes | Confianza |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| CCAA:01 | 8.751.219 | 100.000 / 99.994 | 0/11 | 0/64 | 0 | 0 | 99,8 % | 30.461 | media-alta |
| CCAA:02 | 1.382.035 | 100.000 / 100.004 | 0/11 | 0/29 | 1 | 0 | 100,0 % | 27.588 | media-alta |
| CCAA:03 | 1.021.627 | 100.000 / 100.015 | 0/11 | 0/14 | 0 | 0 | 99,6 % | 25.696 | media-alta |
| CCAA:04 | 1.260.336 | 100.000 / 100.024 | 0/11 | 0/14 | 0 | 0 | 100,0 % | 21.381 | media-alta |
| CCAA:05 | 2.276.245 | 100.000 / 100.012 | 0/11 | 0/22 | 0 | 0 | 100,0 % | 27.643 | media-alta |
| CCAA:06 | 597.088 | 100.000 / 99.995 | 0/11 | 0/14 | 0 | 0 | 100,0 % | 15.376 | media-alta |
| CCAA:07 | 2.419.181 | 100.000 / 100.004 | 0/11 | 0/71 | 1 | 0 | 99,7 % | 32.120 | media-alta |
| CCAA:08 | 2.155.201 | 100.000 / 99.972 | 0/11 | 0/43 | 1 | 0 | 100,0 % | 28.614 | media-alta |
| CCAA:09 | 8.202.041 | 100.000 / 100.008 | 0/11 | 0/36 | 0 | 0 | 100,0 % | 29.889 | media-alta |
| CCAA:10 | 5.529.081 | 100.000 / 99.991 | 0/11 | 0/29 | 0 | 0 | 100,0 % | 30.522 | media-alta |
| CCAA:11 | 1.055.386 | 100.000 / 100.014 | 0/11 | 0/22 | 0 | 0 | 99,9 % | 27.522 | media-alta |
| CCAA:12 | 2.728.430 | 100.000 / 100.048 | 0/11 | 0/36 | 0 | 0 | 99,7 % | 31.098 | media-alta |
| CCAA:13 | 7.168.876 | 100.000 / 100.021 | 0/11 | 0/14 | 0 | 0 | 100,0 % | 29.367 | media-alta |
| CCAA:14 | 1.605.913 | 100.000 / 100.024 | 0/11 | 0/14 | 0 | 0 | 100,0 % | 26.661 | media-alta |
| CCAA:15 | 690.044 | 100.000 / 100.028 | 0/11 | 0/14 | 1 | 0 | 100,0 % | 16.126 | media-alta |
| CCAA:16 | 2.253.019 | 100.000 / 100.022 | 0/11 | 0/29 | 1 | 0 | 100,0 % | 31.763 | media-alta |
| CCAA:17 | 329.550 | 100.000 / 100.003 | 0/11 | 0/14 | 0 | 0 | 99,9 % | 8.495 | media-alta |
| CCAA:18 | 84.196 | 100.000 / 99.999 | 0/11 | 1/12 | 1 | 0 | 99,8 % | 1.719 | media-alta |
| CCAA:19 | 86.908 | 100.000 / 99.995 | 0/11 | 0/12 | 1 | 0 | 97,8 % | 1.901 | media-alta |
| PROV:28 | 7.168.876 | 50.000 / 50.011 | 0/11 | 0/7 | — | 0 | 100,0 % | 14.750 | media |
| PROV:08 | 6.008.837 | 50.000 / 50.015 | 0/11 | 0/7 | — | 0 | 100,0 % | 15.002 | media |
| PROV:42 | 90.824 | 50.000 / 49.992 | 0/11 | 0/7 | — | 0 | 99,1 % | 2.286 | media |
| PROV:44 | 137.173 | 50.000 / 49.993 | 0/11 | 0/7 | — | 0 | 98,3 % | 3.461 | media |
| PROV:04 | 782.945 | 50.000 / 50.022 | 0/11 | 0/7 | — | 0 | 99,6 % | 13.119 | media |
| PROV:35 | 1.181.260 | 50.000 / 50.006 | 0/11 | 0/7 | — | 0 | 100,0 % | 13.706 | media |
| PROV:20 | 735.369 | 50.000 / 49.996 | 0/11 | 0/7 | — | 0 | 100,0 % | 14.361 | media |
| PROV:32 | 306.524 | 50.000 / 49.978 | 0/11 | 0/7 | — | 0 | 98,8 % | 8.229 | media |
| PROV:51 | 84.196 | 50.000 / 49.978 | 0/11 | 0/6 | — | 0 | 99,8 % | 1.711 | media |
| PROV:52 | 86.908 | 50.000 / 49.993 | 0/11 | 0/6 | — | 0 | 97,8 % | 1.891 | media |
| MUNIS:ejemplo_valencia_urbano | 1.273.589 | 20.000 / 19.992 | 0/6 | 0/2 | — | 0 | 98,4 % | 6.124 | baja |
| MUNIS:ejemplo_teruel_rural | 53.706 | 20.000 / 19.998 | 0/5 | 0/1 | — | 0 | 0,0 % | 1.292 | baja (reducida) |

Ceuta y Melilla se generan con 100.000 personas, más que sus residentes (84.196 y 86.908). La integerización (TRS) replica las unidades calibradas, así que hay hogares donantes repetidos. Es una prueba de estrés del método; en el uso normal, N es menor que los residentes.

## Prueba de coherencia entre niveles (V-COHERENCIA)

Las 19 poblaciones autonómicas, cada persona con peso = residentes de su comunidad / tamaño, frente a España con 1.000.000 de personas (`2026-01-01_ES_1000000_s1`). Umbrales: TVD ≤ 0,01 en las calibradas y ≤ 0,02 en las reservadas.

| Uso | Objetivo | TVD | |
| --- | --- | ---: | --- |
| calibrar | actividad_sexo | 0,0010 | ✅ |
| calibrar | edad5_sexo | 0,0012 | ✅ |
| calibrar | edad5_sexo_colectivos | 0,0107 | ❌ |
| calibrar | edad5_sexo_familiares | 0,0012 | ✅ |
| calibrar | estudios_edad | 0,0012 | ✅ |
| calibrar | nacionalidad | 0,0001 | ✅ |
| calibrar | nacionalidad_top | 0,0002 | ✅ |
| calibrar | tamano_hogar | 0,0002 | ✅ |
| calibrar | tipo_hogar | 0,0004 | ✅ |
| calibrar | urbanizacion | 0,0001 | ✅ |
| reservar | actividad_edad | 0,0022 | ✅ |
| reservar | adultos_nacionalidad | 0,0002 | ✅ |
| reservar | estado_civil_edad | 0,0013 | ✅ |
| reservar | estudios_sexo_edad | 0,0025 | ✅ |
| reservar | nacionalidad_top_sexo_edad | 0,0020 | ✅ |
| reservar | provincia_si_calibra_ccaa | 0,0010 | ✅ |
| reservar | tamano_municipio | 0,0005 | ✅ |
| reservar | tipo_hogar_edad4_ref | 0,0011 | ✅ |

## Prueba del territorio reservado

Galicia (CCAA:12) calibrada sin sus objetivos socioeconómicos, relación con la actividad × sexo y estudios × edad (`excluir`). Esos dos objetivos se comprueban después como reservados, con el umbral de comunidad: máx(1,2 × TVD_ref + 0,002; 0,05).

| Objetivo retirado | TVD | TVD_ref | Umbral | |
| --- | ---: | ---: | ---: | --- |
| actividad_sexo | 0,0371 | 0,0056 | 0,050 | ✅ |
| estudios_edad | 0,0395 | 0,0077 | 0,050 | ✅ |

El resto de marginales calibradas: 0 fallos de 9.

Sin calibrarlos, la actividad y los estudios se desvían alrededor de 0,04 de la cifra oficial, frente a 0,0013 y 0,0020 en la serie calibrada. Quedan dentro del umbral de comunidad, así que la estructura demográfica y del hogar que aportan los donantes ya transmite buena parte de la información socioeconómica. Aun así, calibrarlos reduce el error unas 20 veces, y por eso se mantienen calibrados.

## Donantes y confianza

- **Comunidades y provincias:** 97,8 % (Melilla) a 100 % de donantes locales. Las unidades no locales vienen de las comunidades parecidas (D-041.2). Kish de los donantes ≥ 1.711 (Ceuta).
- **Lista urbana** (València y 11 municipios de L'Horta): 98,4 % locales, porque los municipios de más de 10.000 habitantes están identificados en el Censo.
- **Lista rural** (226 municipios de Teruel de menos de 2.000 habitantes): 0 % locales por diseño. El Censo no identifica municipios pequeños, así que los donantes son los hogares de su provincia y clase de tamaño (misma provincia), más 157 personas de la misma comunidad y grado de urbanización. Tras una ronda de reparación (D-041.4), V-MARG da 0 fallos de 5. Confianza **baja y reducida**, con el municipio de cada hogar asignado al azar en proporción a la población (`modelada`).

## Cambios de código en esta ronda

- `src/sinpop/validate/fase5.py`: serie F5, reanudable (`--reanudar`), y anexo (`--anexo`).
- `src/sinpop/synth/poblacion.py`: España se calibra componiendo las calibraciones de sus comunidades, un bloque cada vez (mismo cálculo; memoria). `construir` suelta los donantes tras ponderar cuando los ha cargado él.
- `tools/ensayo_d042.py`: ensayo de D-042 A.

## Anexo por territorio

Una sección por territorio en [`fase_05_anexo.md`](fase_05_anexo.md), con:

- donantes por nivel, Kish y confianza;
- V-MARG;
- cada cruce reservado del nivel propio (TVD, TVD_ref, umbral);
- en las comunidades, la V de Cramér de cada par.

Los CSV de cada comprobación están en `reports/fase_05/`.
