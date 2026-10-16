# Fase 03 · Objetivos de calibración por territorio

**Estado:** superada (F3 no tiene revisión humana en su puerta; sus decisiones D-036 y D-037 se revisan con F4)
**Fecha:** 2026-10-16 · **Versión del código:** ver `fase_03_puerta.md`
**Comando para reproducir:**

```bash
sinpop harmonize --source all                    # entradas (F2)
sinpop targets --territory all                   # España, 19 comunidades y 52 provincias
sinpop targets --territory MUNIS:configs/territorios/ejemplo_almeria.yaml
sinpop validate --phase 3                        # reports/fase_03_puerta.md
```

## Resumen

Para cualquier territorio (España, comunidad, provincia o lista de municipios) hay ya un fichero con las cifras oficiales que la población debe reproducir a 01/01/2026. Cada cifra lleva su fuente, edición, fecha y método, y va separada en **calibrar** y **reservar para validar**.
- **Efectivos:** salen de la ECP 2026 (provincia × sexo × edad simple).
- **Estructura** (estudios, actividad, estado civil, urbanización, nacionalidad, tipo de hogar): sale de las tablas oficiales más recientes, como cuotas dentro de la misma celda de provincia, sexo y edad. Así todos los objetivos suman exactamente lo mismo.
- **Elecciones:** hay objetivos de las generales de 2023 (familia, blanco, nulo y abstención sobre el censo de residentes) y de las últimas autonómicas.

Las seis comprobaciones de la puerta se superan. Los ficheros son reproducibles: varias ejecuciones dan el mismo hash.

## Puerta de salida

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G3.1 | Las marginales suman el total oficial | ✅ | 73 territorios; 0 fuera de umbral | < 0,1 % |
| G3.2 | Marginales coherentes entre cruces | ✅ | 0 incoherencias | diferencia relativa < 1e-6 |
| G3.3 | Las 19 comunidades suman España | ✅ | 0 celdas distintas | < 0,001 personas |
| G3.4 | Ningún objetivo reservado se calibra (test automático) | ✅ | 12 calibrados, 10 reservados | 0 |
| G3.5 | Cada objetivo registra fuente, edición y fecha | ✅ | 0 filas sin metadatos | 0 |
| G3.6 | Electorales al 100 % y coherentes con el derecho a voto | ✅ | España −1,46 %; máximo Guadalajara −4,02 % | 100 % y < 5 % |

Detalle automático: [`fase_03_puerta.md`](fase_03_puerta.md).

## Resultados principales

### Objetivos (`configs/targets.yaml`)

| Uso | Objetivo | Variables | Fuente de la estructura |
| --- | --- | --- | --- |
| Calibrar | `edad5_sexo` (+ viviendas familiares y colectivos) | edad_5 × sexo | ECP 59589 y 60129 (2026), exactos |
| Calibrar | `nacionalidad` | nacionalidad_grupo | ECP 2026 (española/extranjera) + Censo Anual exhaustivo 2025 (grupos) |
| Calibrar | `estudios_edad` | estudios_3 × edad (grupos de la tabla) | Censo Anual 2024, tabla 66601 |
| Calibrar | `actividad_sexo` | relacion_actividad × sexo | Censo Anual 2024, tabla 67128 |
| Calibrar | `urbanizacion` | grado_urbanizacion | Censo Anual 2025, tabla 79341 |
| Calibrar | `tamano_hogar`, `tipo_hogar` | tamano_hogar_4; tipo × tamaño | ECP 60133 (2026); Censo 2021 dentro de cada tamaño |
| Calibrar | `voto_generales_2023`, `voto_autonomicas` | familia, blanco, nulo, abstención | Interior (residentes); boletines autonómicos |
| Reservar | `estudios_sexo_edad`, `actividad_edad`, `estado_civil_edad` | con sexo o edad de la tabla | Censo Anual 2024 |
| Reservar | `tipo_hogar_edad4_ref`, `nacionalidad_top`, `tamano_municipio`, `adultos_nacionalidad`, provincias | — | Censo 2021; exhaustivo 2025; Padrón 2025 |
| Reservar | `voto_generales_2023_municipio`, `voto_generales_2023_candidatura` | detalle municipal y por candidatura | Interior (D-022) |

En los territorios por municipios, `estudios_sexo_mun` (tablas municipales 2024) sustituye a `estudios_edad`. Los objetivos que solo existen por provincia (viviendas familiares, colectivos, hogares, estudios y actividad por edad, estado civil y autonómicas) se indican con `ambito: provincia`.

### España, 01/01/2026

- 49.596.376 residentes: 49.210.373 en viviendas familiares y 386.003 en colectivos.
- 19.762.059 hogares.
- 7,19 millones de extranjeros (6,91 millones en 2025).

Generales 2023 sobre el censo de residentes (35.146.062):

| Opción | % |
| --- | ---: |
| Abstención | 29,60 |
| Centro-derecha estatal | 23,02 |
| Socialdemócrata | 22,08 |
| Derecha radical | 8,63 |
| Izquierda estatal | 8,58 |
| Nacionalistas y regionalistas | 5,92 |
| Otros | 0,86 |
| Nulo | 0,74 |
| Blanco | 0,57 |

Censo electoral de residentes (2023) frente a españoles de 18 y más años de los objetivos (2026), por comunidad: entre −3,1 % (Illes Balears) y +0,9 % (Extremadura); España −1,46 %. La diferencia se explica por los casi tres años entre ambas fechas y por la diferencia entre censo electoral y padrón.

### Territorios por municipios

Método (D-036): los objetivos provinciales se reparten con la estructura municipal del Censo Anual exhaustivo 2025.
- Los municipios pequeños se reparten desde su clase de tamaño con el Padrón 2025.
- Los 83 municipios con cifra oficial de la ECP 2026 reciben su total por sexo exacto.
- La suma de todos los municipios de una provincia reproduce el objetivo provincial.
- Antes de incorporar la ECP municipal, el reparto se validó contra esas 83 cifras, sin usarlas: mediana de la diferencia 0,01 %, desviación típica 0,7 %, máximo −2,2 %.

Ejemplo técnico (`ejemplo_almeria.yaml`, cuatro municipios): 412.081 residentes, y los 9 objetivos suman lo mismo.

## Decisiones tomadas

- D-036 · Objetivos de calibración y validación (fuentes, cuotas, universos, municipios, electorales).
- D-037 · Familias de las 295 candidaturas autonómicas.

## Problemas abiertos y riesgos

1. **Tablas municipales:** se están descargando las 104 tablas municipales del Censo Anual (estudios y actividad, una por provincia). Hasta que estén todas, un territorio por municipios de una provincia sin su tabla se detiene con un mensaje que dice qué falta. Las dos tablas nacionales (66592 y 66594) superan el límite de volumen de la API y no hacen falta.
2. **Desfases de fecha** (documentados en cada cifra): la estructura de estudios, actividad y estado civil es de 2024; la de urbanización y nacionalidad, de 2025; la del tipo de hogar, de 2021.
3. **Electorales:** las autonómicas pueden incluir el voto CERA (la mayoría de publicaciones no lo dice) y Aragón no publica electores, así que su objetivo va sobre votantes, sin abstención.

## Qué necesita revisión humana

Nada bloquea F3. D-036 y D-037 se presentarán con la revisión de F4.
