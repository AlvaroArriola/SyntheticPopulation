# Fase 01 · Inventario y adquisición de datos

**Estado:** pendiente de revisión humana (G1.4 y G1.5 necesitan decisión)
**Fecha:** 2026-10-14 · **Versión del código:** ver `fase_01_puerta.md`
**Comando para reproducir:** `sinpop ingest --verify && sinpop ingest --inventory && sinpop validate --phase 1` (las descargas se repiten con los comandos `sinpop ingest --source … --url …` / `--ine-table …` registrados en `data/raw/MANIFEST.yaml`, que guarda la URL y el SHA-256 de cada fichero).

## Resumen

Con acceso a la red se han descargado del INE, de forma automática y verificada por SHA-256, **todas las fuentes del núcleo**:
- microdatos del Censo 2021 (personas y viviendas);
- microdatos del Censo Anual (fichero exhaustivo de 2025 y muestras de 2023, 2024 y 2025);
- 25 tablas oficiales (ECP a 01/01/2026 y Censo Anual);
- ECV 2025, EPA 2T2026, TIC-H 2025, Encuesta de Salud de España 2023, EPF 2025 y Encuesta de personas sin hogar 2022;
- Atlas de renta (tablas municipales).

El manifiesto tiene 251 ficheros. Del Atlas de renta falta 1 de 54 tablas provinciales (la 30824), que supera el límite de volumen de la API (se resolverá en F6, donde se usa). Se han resuelto 5 de las 7 verificaciones críticas. Las 2 pendientes afectan solo a las capas de opinión y política. Hay tres puntos que necesitan una decisión:
- la muestra del Censo Anual 2023 difiere en 866 registros (−0,018 %) de la cifra oficial actual;
- el Censo 2021 no declara un número exacto de registros;
- quedan pendientes las fuentes del CIS, de Infoelectoral y de la ESS.

## Puerta de salida

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G1.1 | Fuentes P0 descargadas y con hash verificado | ✅ | 5/5 | 5/5 |
| G1.2 | Diseño de registro o documentación de cada fichero | ✅ | todas | todas |
| G1.3 | Matriz de cobertura sin variables P0 sin fuente | ✅ | 15/15 | 15/15 |
| G1.4 | Registros leídos = declarados | ❌ | 3/4 coinciden; muestra 2023 −866; Censo 2021 sin cifra exacta declarada | igualdad exacta |
| G1.5 | 7 verificaciones críticas resueltas | ❌ | 5/7 (pendientes 6 y 7, solo F8) | 7/7 |
| G1.6 | Revisión humana | ⏸️ | pendiente | aprobación |

Detalle automático: [`fase_01_puerta.md`](fase_01_puerta.md). Inventario completo: [`fase_01_inventario.md`](fase_01_inventario.md).

## Resultados principales

### Fuentes descargadas (núcleo)

| Fuente | Edición | Qué es | Registros / alcance | Peso |
| --- | --- | --- | --- | --- |
| Censo 2021, personas | 2021 | **Donantes**: 10 % de los hogares con todas sus personas | 4.707.186 personas, 1.853.662 hogares | sin peso (factor 10) |
| Censo Anual exhaustivo | 01/01/2025 | Demografía de toda la población | 49.128.297 = población oficial ✅ | — |
| Censo Anual, muestra | 2025 / 2024 / 2023 | 10 % de la población: demografía (2025), estudios, actividad y estado civil (2024), ocupación (2023) | 4,9 M / 4,9 M / 4,8 M | sin peso (factor 10) |
| ECP | 01/01/2026 | Población en viviendas familiares por provincia × sexo × edad × nacionalidad; hogares por tamaño | 14 tablas | — |
| Censo Anual (tablas) | 2021, 2023, 2024, 2025 | Cifras publicadas para reproducir en F2 (estudios, actividad, estado civil, población) | 9 tablas | — |
| ECV | 2025 | Renta, privación, tenencia, salud | 29.369 hogares, 71.398 personas | RB050, PB040, DB090 |
| EPA | 2T2026 | Empleo detallado | 114.021 personas | FACTOREL |
| TIC-H | 2025 | Uso digital, 16+ | 16.938 personas | FACTOR_P |
| ESdE | 2023 | Salud, limitación GALI, 15+ | 21.032 adultos | FACTORADULTO |

### Contraste del Censo 2021 por provincia

Registros × 10 frente a la población oficial de 2021: el cociente va de 0,956 (Palencia) a 1,011 (Melilla). Es lo esperable en una muestra uniforme del 10 % de los hogares que excluye los establecimientos colectivos, más abundantes en provincias envejecidas. La calibración de F4 a la ECP de viviendas familiares corrige esta composición.

### Verificaciones críticas (G1.5)

| # | Verificación | Estado | Resultado |
| --- | --- | --- | --- |
| 1 | Nivel geográfico de los microdatos censales | ✅ | Provincia (52), municipio si tiene 10.000 habitantes o más (si no, tres tamaños) y grado de urbanización. No hace falta el plan alternativo |
| 2 | Establecimientos colectivos | ✅ | No están en la muestra de hogares. Son 386.003 personas (0,78 %) según la ECP 2026 → D-017 |
| 3 | Universo de la TIC-H | ✅ | 16 años o más, sin límite superior (edades 16–104) |
| 4 | Ronda 12 de la ESS | ✅ | No publicada (prevista para enero de 2027): se usa la ronda 11 |
| 5 | Encuesta de salud más reciente | ✅ | Encuesta de Salud de España 2023 (INE) |
| 6 | Fuentes electorales | ⏳ | Infoelectoral corta la conexión desde el entorno; los microdatos del CIS se sirven bajo petición → D-019 |
| 7 | Variables políticas por barómetro | ⏳ | Requiere los cuestionarios y microdatos del CIS → D-019 |

Fuente: [`fase_01_verificaciones.yaml`](fase_01_verificaciones.yaml).

### Matriz de cobertura (variables P0–P2)

`⚠️` = cobertura parcial; la nota está en `configs/variables.yaml`. «CA» = Censo Anual.

| Variable | Prior. | Censo 2021 | CA exh. 2025 | CA muestra | ECP 2026 | ECV 2025 | EPA 2T26 | TIC-H 2025 | ESdE 2023 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `edad` | P0 | `VAREDAD` | `VAREDAD` | `VAREDAD` | `Edad (tablas 59589, 60129)` | `RB082` | `EDAD1` ⚠️ | `EDAD` | `EDADa` |
| `edad_5` | P0 | `VAREDAD` | `VAREDAD` | — | `Edad` | — | — | — | — |
| `edad_4` | P0 | `VAREDAD` | `VAREDAD` | — | `Edad` | — | — | — | — |
| `sexo` | P0 | `SEXO` | `SEXO` | `SEXO` | `Sexo` | `RB090` | `SEXO1` | `SEXO` | `SEXOa` |
| `nacionalidad_grupo` | P0 | `PNACIO` ⚠️ | `PNACIO` | `PNACIO` | `Nacionalidad (española/extranjera, tabla 60129)` ⚠️ | `RB290` | `NAC1, EXREGNA1` | `NACIONALIDAD` | — |
| `pais_nacimiento_grupo` | P1 | `PNACIM` | `PNACIM` | `PNACIM` | — | — | — | — | — |
| `nacionalidad_top` | P1 | `PNACIO` | `PNACIO` | `PNACIO` | — | — | — | — | — |
| `estado_civil` | P1 | `ECIVIL` | — | `ECIVIL` ⚠️ | — | — | — | — | — |
| `nivel_estudios` | P0 | `ESREAL_CNEDA` | — | `ESREAL` ⚠️ | — | `PE041` | `NFORMA` | `NIVELEST` | `NIVEST` |
| `estudios_3` | P0 | `ESREAL_CNEDA` | — | `ESREAL` ⚠️ | — | — | — | — | — |
| `relacion_actividad` | P0 | `RELA` ⚠️ | — | `RELA` ⚠️ | — | `PL032` | `AOI` | `SIT_LAB` | — |
| `ocupacion` | P1 | `OCU63` | — | `CNO` ⚠️ | — | — | `OCUP1` | — | — |
| `sector_actividad` | P2 | `ACT89` | — | `CNAE` ⚠️ | — | — | — | — | — |
| `situacion_profesional` | P1 | `SITU` ⚠️ | — | `SITU` ⚠️ | — | — | `SITU` | — | — |
| `tipo_jornada` | P2 | — | — | — | — | — | `PARCO1` | — | — |
| `teletrabajo` | P2 | — | — | — | — | — | — | `TTRAB_ACTUAL, ULT_TTRAB` | — |
| `anio_llegada_espana` | P2 | `VARANOE` | — | `VARANOE` | — | — | — | — | — |
| `discapacidad_limitacion` | P1 | — | — | — | — | `PH030` | — | — | `C3a` |
| `salud_autopercibida` | P1 | — | — | — | — | `PH010` | — | — | `C1` |
| `uso_internet` | P1 | — | — | — | — | — | — | `ULT_INT, FREC_INT` | — |
| `competencias_digitales` | P2 | — | — | — | — | — | — | `pendiente: indicador derivado de los bloques de habilidades (F2)` | — |
| `compra_online` | P2 | — | — | — | — | — | — | `ULT_COM` | — |
| `tipo_hogar` | P0 | `TIPO_HOG + ESTRUC_HOG + TIPO_NUC` | — | — | — | — | — | — | — |
| `tamano_hogar` | P0 | `TAM_HOG` ⚠️ | — | — | `Tamaño del hogar (tabla 60133)` ⚠️ | — | — | — | — |
| `relacion_persona_ref` | P0 | `NORDEN_CON, NORDEN_PAD, NORDEN_MAD, NORDEN_OPA, FAMILIA, NUCLEO, TIPOPER` ⚠️ | — | — | — | — | — | — | — |
| `n_menores_hogar` | P1 | `VAREDAD (agregado por hogar)` | — | — | — | — | — | — | — |
| `n_mayores_65_hogar` | P1 | `VAREDAD (agregado por hogar)` | — | — | — | — | — | — | — |
| `n_mayores_80_hogar` | P1 | `VAREDAD (agregado por hogar)` | — | — | — | — | — | — | — |
| `tenencia_vivienda` | P1 | `TENEN_VIV` ⚠️ | — | — | — | `HH021` | — | — | — |
| `renta_hogar_decil` | P1 | — | — | — | — | `vhRentaa / HX240 (renta equivalente)` | — | — | — |
| `renta_hogar_decil_ccaa` | P1 | — | — | — | — | `vhRentaa` | — | — | — |
| `privacion_material` | P1 | — | — | — | — | `vrMATSOCDEP / vhMATDEP` | — | — | — |
| `privacion_material_n` | P1 | — | — | — | — | `HD080, HS040–HS090, PD020–PD070…` ⚠️ | — | — | — |
| `dificultad_fin_mes` | P2 | — | — | — | — | `HS120` | — | — | — |
| `vehiculo_hogar` | P2 | — | — | — | — | `HS110` | — | — | — |
| `ccaa` | P0 | `CPRO (derivada)` | `CPRO (derivada)` | `CPRO (derivada)` | `Provincia (derivada)` | `DB040` | `CCAA` | `CCAA` | `CCAA` |
| `provincia` | P0 | `CPRO` | `CPRO` | `CPRO` | `Provincia` | — | `PROV` | — | — |
| `tamano_municipio` | P0 | `CMUN` ⚠️ | `CMUN` ⚠️ | `CMUN` | — | — | — | — | — |
| `grado_urbanizacion` | P0 | `TIPO_MUN_DEGURBA` | `DEGURBA` | `DEGURBA` | — | `DB100` | — | — | — |
| `municipio` | P2 | `CMUN` ⚠️ | `CMUN` ⚠️ | `CMUN` ⚠️ | — | — | — | — | — |
| `ctx_renta_municipio` | P1 | — | — | — | — | — | — | — | — |
| `ctx_envejecimiento` | P1 | — | — | — | — | — | — | — | — |
| `ctx_precio_vivienda` | P2 | — | — | — | — | — | — | — | — |

Ninguna variable P0 queda sin fuente. Algunas variables P1/P2 solo existen en las encuestas: renta, privación, salud, limitación, uso digital, jornada, teletrabajo y vehículo. Se añadirán por emparejamiento en F6.

## Decisiones tomadas

- D-015 · Fecha de referencia 01/01/2026: ECP para los totales y Censo Anual para la estructura; ECP como fuente P0 (propuesta).
- D-016 · Hallazgos en los ficheros: las muestras censales no tienen peso (factor 10); el Parquet de 2024 está desfasado y se usa el TXT; la muestra 2023 difiere en 866 registros; los códigos varían entre fuentes (propuesta).
- D-017 · Población base = residentes en viviendas familiares; los colectivos (0,78 %) se declaran como limitación (propuesta).
- D-018 · Ajustes del diccionario: actividad sin «labores del hogar», situación profesional según el Censo, tenencia en dos pasos, regla de persona de referencia y sin doble nacionalidad (propuesta).
- D-019 · Fuentes del CIS, Infoelectoral y ESS en descarga manual; verificaciones 6 y 7 aplazadas a F8 (propuesta).

## Problemas abiertos y riesgos

- **Desfase temporal:** el tipo de hogar procede de 2021 (el tamaño se calibra con la ECP 2026); estudios y actividad, de 2024; ocupación, de 2023. Se documentará por variable.
- **Sin peso en los donantes:** se trata como una muestra con factor uniforme 10; la calibración de F4 hace el resto.
- **Persona de referencia:** el Censo 2021 no la define y hay que derivarla con una regla (D-018.4); afecta a la regla dura V-REGLAS «una persona de referencia por hogar» y a `tipo_hogar × edad_4` del hogar.
- **Capas F8:** dependen de descargas manuales (CIS, ESS, Infoelectoral).

## Qué necesita revisión humana

1. ¿Se aprueban **D-015 a D-019**? En concreto: la fecha de referencia 01/01/2026, el universo de viviendas familiares y la regla de la persona de referencia.
2. **G1.4:** ¿se acepta la muestra 2023 del Censo Anual con su diferencia de −0,018 %? Solo se usa para la distribución de la ocupación. ¿Se acepta el contraste por cociente para el Censo 2021, cuya documentación no declara una cifra exacta?
3. **G1.5:** ¿se aplazan las verificaciones 6 y 7 (fuentes del CIS y electorales) al inicio de F8A/F8B? No intervienen en la población sociodemográfica.
4. Si se quiere la capa política: descargar a mano los ficheros de `data/raw/MANUAL_DOWNLOADS.md` (Infoelectoral, CIS, ESS) cuando llegue F8.
