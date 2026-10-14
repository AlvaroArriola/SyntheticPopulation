# 03 · Arquitectura

## 1. Visión general

El sistema es un pipeline por etapas. Cada etapa lee artefactos de la anterior, escribe los suyos con metadatos y se puede validar de forma independiente.

```
 Fuentes oficiales
        │
        ▼
 [1] Ingesta ──────────► data/raw/ + MANIFEST.yaml
        │
        ▼
 [2] Armonización ─────► data/interim/<fuente>.parquet   (variables y códigos comunes)
        │
        ▼
 [3] Objetivos ────────► data/processed/targets/<territorio>.parquet   (cifras oficiales a reproducir)
        │
        ▼
 [4] Síntesis ─────────► población base: personas + hogares + pesos
        │   (donantes ► calibración ► integerización ► muestreo a tamaño N)
        ▼
 [5] Enriquecimiento ──► atributos de renta, salud, uso digital… por emparejamiento
        │
        ▼
 [6] Validación y auditoría de sesgos ──► reports/<run_id>/
        │
        ▼
 [7] Opinión y valores (F8A) ──► opinion.parquet   (rasgos y valores por persona)
        │
        ▼
 [8] Política (F8B) ──► politics.parquet   (recuerdo de voto calibrado, ideología, identidad…)
        │
        ▼
 [9] Dimensión temporal (F8C) ──► trayectorias de rasgos fechadas
        │
        ▼
 [10] Predicción (F9) y confianza (F10) ──► distribución de respuestas + intervalo + confianza
```

Las etapas 1 a 6 forman el **núcleo** (fases 0 a 7). Las etapas 7 a 10 son extensiones y se guardan en ficheros separados unidos por `person_id`, de modo que la población base no depende de ellas (decisión D-005).

## 2. Métodos por etapa

### 2.1 Síntesis de la población (etapa 4)

**Método base recomendado: remuestreo ponderado de donantes con calibración.** Es el estándar en microsimulación espacial y conserva las combinaciones reales.

1. **Selección de donantes.** Hogares completos de los microdatos del Censo 2021 que pertenecen al territorio, o al conjunto jerárquico ampliado si no hay suficientes (ver `02_datos_y_variables.md`, sección 5).
2. **Calibración a nivel de hogar.** Se ajustan los pesos de los hogares donantes para que las personas y los hogares resultantes reproduzcan los objetivos del territorio (edad × sexo, nacionalidad, estudios, actividad, tipo y tamaño de hogar, tamaño de municipio…). Métodos admitidos:
   - **Raking / IPF** (ajuste proporcional iterativo): sencillo y robusto. Requiere controlar la convergencia y los pesos extremos.
   - **Calibración por regresión generalizada con acotación de pesos** (GREG truncado, distancia logit o *raking ratio* acotado): permite limitar la deformación de los pesos.
   - **Calibración integrada persona-hogar:** objetivos a nivel de persona y de hogar a la vez, manteniendo hogares completos.
   La elección se registra en `DECISIONS.md` con una comparación empírica.
3. **Integerización y muestreo a tamaño N.** Convertir pesos en un número entero de copias por hogar mediante un método que minimice el error, como el TRS (*truncate, replicate, sample*) o un muestreo sistemático ordenado. Para tamaños pequeños, muestreo proporcional a los pesos.
4. **Identificadores.** Cada persona sintética recibe un `person_id` y un `household_id` nuevos. Se conserva una referencia interna al donante solo en un fichero de trazabilidad aparte (`lineage.parquet`), útil para auditar la concentración de donantes.

**Métodos alternativos** que pueden compararse si el base no supera las validaciones: redes bayesianas, cópulas, modelos generativos tabulares. Cualquier método generativo debe demostrar que no produce combinaciones imposibles y que conserva los cruces mejor que el método base.

**Modo de sobremuestreo de minorías.** Cuando se pide un mínimo de personas de un grupo, se muestrea más de ese grupo y se asigna a cada persona un `peso` igual a la inversa de su probabilidad de inclusión relativa. Toda estadística agregada usa ese peso. El informe muestra los resultados ponderados.

### 2.2 Población territorial

Se usa **el mismo código** que la nacional, cambiando tres entradas:

- el territorio (por código o lista de municipios);
- los objetivos de calibración de ese territorio;
- el conjunto de donantes (local o jerárquico).

La población territorial **no** se obtiene filtrando la nacional. Así cada territorio tiene el tamaño que se pida y queda ajustado a sus propias cifras.

**Coherencia entre niveles.** Como comprobación, las poblaciones de las 19 comunidades, combinadas con sus pesos poblacionales, deben reproducir la nacional dentro de los umbrales de validación.

### 2.3 Enriquecimiento (etapa 5)

**Emparejamiento estadístico** de cada persona u hogar sintético con un registro de una encuesta (ECV, EPA, TIC-H, EPF, salud), usando las variables comunes armonizadas como llave.

- Emparejamiento por estratos (por ejemplo, CCAA × tramo de edad × sexo) y distancia dentro del estrato, o emparejamiento basado en modelo (predicción y selección aleatoria de un donante con predicción cercana, *predictive mean matching*).
- **Se hereda un bloque coherente de variables del mismo donante** (por ejemplo, todas las de renta y privación juntas) para no romper sus relaciones internas.
- Imputación múltiple opcional (M copias) para medir la incertidumbre que añade el emparejamiento.
- Los universos se respetan: por ejemplo, para mayores de 74 sin cobertura en TIC-H se usa un método documentado (otra fuente, extrapolación por modelo o valor marcado como imputado de baja calidad).
- Cada variable enriquecida lleva una columna `<variable>__calidad` (`observada`, `emparejada`, `modelada`, `extrapolada`).

### 2.4 Opinión y valores (fase 8A)

1. Apilar los microdatos del CIS (y la ESS) anteriores a la fecha de corte en formato largo: encuestado, perfil armonizado, fecha de campo, pregunta, respuesta, peso.
2. Estimar un **modelo de rasgos latentes** (análisis factorial o teoría de respuesta al ítem) con los rasgos de `02_datos_y_variables.md`, sección 3.4.
3. Estimar un **modelo multinivel** que explique esos rasgos por el perfil individual y el contexto territorial (MRP).
4. Asignar a cada persona sintética una **extracción aleatoria** de sus rasgos condicionada a su perfil y su territorio. No la media: la extracción conserva la variabilidad dentro de los grupos.

### 2.5 Política (fase 8B)

El orden importa: primero el comportamiento pasado, anclado en resultados reales; después lo que depende de él.

1. **Universo electoral.** Marcar en cada persona su derecho a voto en cada tipo de elección (nacionalidad, edad en la fecha de la elección).
2. **Modelo de recuerdo de voto.** Modelo multinivel multinomial entrenado con los estudios del CIS (preelectorales, postelectorales y barómetros posteriores a la elección): probabilidad de cada opción (familia de partidos, blanco, nulo, abstención) según perfil individual y contexto territorial. Como contexto se usa el resultado real del municipio o la provincia, que es información muy rica y fiable.
3. **Asignación y calibración.** Asignar a cada persona con derecho a voto una opción por extracción aleatoria de sus probabilidades, y **calibrar** para que la distribución agregada reproduzca el resultado oficial del territorio (por provincia, o por CCAA si la muestra no da para más), abstención incluida. La calibración se hace sobre las probabilidades (ajuste por territorio en escala logit, como en la *postestratificación con restricciones*), no reasignando personas a mano.
4. **Ideología, identidad y resto de variables políticas.** Modelo condicionado al perfil **y al recuerdo de voto asignado**, para que la coherencia entre voto e ideología sea la de los datos reales (no todos los votantes de un partido se colocan igual en la escala).
5. **Rasgos políticos latentes** (`rasgo_izquierda_derecha`, `rasgo_eje_territorial`, `rasgo_desafeccion`, `rasgo_implicacion_politica`) por extracción condicionada.
6. **Elecciones de varios niveles.** El recuerdo de autonómicas y europeas se modela condicionado al de generales, porque están muy correlacionados y así se conserva el voto dual (votar distinto según la elección).

### 2.6 Dimensión temporal (fase 8C)

- Los modelos de 2.4 y 2.5 incluyen **efectos de periodo** (mes o trimestre de campo) y su interacción con los grupos principales (edad, territorio, recuerdo de voto). Así se estima cómo ha evolucionado cada tipo de persona.
- Con esos efectos se generan trayectorias de los rasgos de cada persona sintética, coherentes con su grupo y con la variabilidad observada.
- **Eventos.** `configs/eventos.yaml` lista eventos con fecha. Para cada evento pasado se estima el cambio en los rasgos y en las respuestas de cada grupo (antes y después), lo que forma un **banco de efectos de eventos** que la capa de predicción usa por analogía.

### 2.7 Predicción y confianza (fases 9 y 10)

- **Estimador estadístico:** el LLM traduce una pregunta nueva a parámetros (qué rasgos activa, en qué dirección, umbrales, propensión a NS/NC) apoyándose en preguntas parecidas recuperadas del banco histórico. El modelo estadístico genera la respuesta de cada persona.
- **Estimador de simulación:** el LLM responde en el papel de una submuestra estratificada (unas 1.000 personas) con su perfil y sus rasgos.
- **Eventos:** ante un evento nuevo, el LLM busca eventos análogos en el banco y propone qué rasgos se desplazan y cuánto. El sistema devuelve la distribución **antes** y **después** del evento, y el cambio.
- **Combinación:** pesos aprendidos en validación.
- **Incertidumbre:** la predicción se repite con varias poblaciones o imputaciones (por ejemplo, 20 réplicas) y con variaciones de la traducción del LLM. El resultado incluye un intervalo del 80 % y del 95 % por opción.
- **Confianza:** modelo que predice el error a partir de la similitud con preguntas pasadas, el desacuerdo entre estimadores, la sensibilidad a reformulaciones, la amplitud del intervalo y el tamaño efectivo de datos del subgrupo; entrenado con un *backtest* sobre preguntas históricas.

### 2.8 Formato de preguntas y respuestas

Entrada (`preguntas/<id>.json`):

```json
{
  "id": "Q017",
  "tipo": "pregunta",
  "enunciado": "¿Con qué frecuencia se siente usted sola?",
  "opciones": ["Nunca", "Rara vez", "A veces", "A menudo", "Siempre", "N.S.", "N.C."],
  "escala": "ordinal",
  "poblacion": {"territorio": "ES", "universo": "18+"},
  "fecha_referencia": "2026-10",
  "subgrupos": ["edad_4", "sexo", "estudios_3", "ccaa", "recuerdo_voto_generales_familia"]
}
```

Para un evento, `"tipo": "evento"` y además `"evento": {"descripcion": "…", "fecha": "2026-11-01"}` y la pregunta sobre la que se mide el efecto.

Salida (`predicciones/<id>_<run_id>.json`):

```json
{
  "id": "Q017",
  "run_id": "…",
  "total": {"Nunca": {"p": 0.31, "ic80": [0.28, 0.34], "ic95": [0.26, 0.36]}, "…": {}},
  "por_subgrupo": {"edad_4=65+": {"…": {}}},
  "confianza": {"total": 0.72, "por_subgrupo": {"edad_4=65+": 0.55}},
  "parametros_llm": {"rasgos": ["rasgo_aislamiento_social"], "direccion": "+", "ns_nc": 0.02},
  "preguntas_similares": ["CIS-3450-P12", "CIS-3501-P08"],
  "coste": {"llamadas": 14, "tokens": 52000, "eur": 0.40, "segundos": 95},
  "versiones": {"modelo_llm": "…", "prompts": "prompts@v3", "poblacion": "…"}
}
```

Las cifras del ejemplo son ilustrativas.

### 2.9 Operación de los modelos de lenguaje

- **Modelos declarados** en `configs/llm.yaml` con su fecha de corte de conocimiento. Cambiar de modelo es una decisión registrada y obliga a revalidar.
- **Prompts versionados** en `prompts/` con identificador de versión; cada predicción guarda la versión usada.
- **Salidas estructuradas** validadas por esquema; una salida no válida se reintenta un número limitado de veces y, si sigue fallando, se registra y se usa el estimador estadístico solo.
- **Caché** de llamadas por (modelo, versión de prompt, entrada) para reproducibilidad y coste.
- **Registro** de cada llamada (sin microdatos originales) en `logs/llm/`.
- **Presupuesto** máximo por predicción y por ejecución, configurable.
- **Temperatura y semillas** fijadas cuando el proveedor lo permita; si no, la variabilidad se mide con repeticiones y forma parte de la incertidumbre.

## 3. Estructura del repositorio

```
poblacion-sintetica/
├── README.md
├── CLAUDE.md
├── DECISIONS.md
├── pyproject.toml
├── configs/
│   ├── sources.yaml          # fuentes, ediciones, rutas
│   ├── variables.yaml        # diccionario armonizado y recodificaciones
│   ├── targets.yaml          # qué objetivos se calibran y cuáles se reservan para validar
│   ├── territories.yaml      # definiciones de territorios y jerarquía de donantes
│   ├── territorios/          # territorios definidos por lista de municipios
│   ├── watchlist.yaml        # grupos minoritarios vigilados
│   ├── thresholds.yaml       # umbrales de validación
│   ├── partidos.yaml         # partidos por elección y familias estables
│   ├── elecciones.yaml       # elecciones de referencia y sus fuentes
│   ├── eventos.yaml          # eventos fechados para la dimensión temporal
│   └── llm.yaml              # modelos, fechas de corte, presupuesto
├── prompts/                  # prompts versionados
├── data/                     # fuera de git salvo los manifiestos
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   ├── populations/<run_id>/
│   └── eval/                 # solo lo lee src/sinpop/evaluate/
├── src/sinpop/
│   ├── ingest/
│   ├── harmonize/
│   ├── targets/
│   ├── synth/                # donantes, calibración, integerización, muestreo
│   ├── enrich/
│   ├── validate/
│   ├── audit/                # sesgos y minorías
│   ├── opinion/              # fase 8A
│   ├── politics/             # fase 8B
│   ├── temporal/             # fase 8C
│   ├── predict/              # fase 9
│   ├── confidence/           # fase 10
│   ├── evaluate/             # fase 11
│   └── cli.py
├── preguntas/                # preguntas y eventos de entrada (JSON)
├── predicciones/             # salidas de la capa de predicción (JSON)
├── logs/llm/                 # registro de llamadas a modelos de lenguaje
├── tests/
│   ├── unit/
│   ├── integration/
│   └── test_no_leakage.py
└── reports/
    ├── fase_00.md … fase_12.md (con fase_08a, fase_08b y fase_08c)
    └── <run_id>/
```

## 4. Formatos de salida

### `persons.parquet`

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `person_id` | string | Identificador sintético |
| `household_id` | string | Hogar al que pertenece |
| `peso` | float | Peso de la persona (1 en modo representativo) |
| `es_adulto` | bool | 18+ |
| *variables del diccionario* | según diccionario | Atributos armonizados |
| `<variable>__calidad` | category | Cómo se obtuvo el valor |

### `households.parquet`

`household_id`, `tamano_hogar`, `tipo_hogar`, `tenencia_vivienda`, `renta_hogar_decil`, territorio y contexto.

### `opinion.parquet` y `politics.parquet`

Una fila por persona adulta, unida por `person_id`: rasgos y variables de las secciones 3.4 y 3.5 de `02_datos_y_variables.md`, cada una con su columna `__calidad` y la fecha de referencia de los rasgos.

### `trajectories.parquet`

Rasgos por persona y periodo (formato largo: `person_id`, `periodo`, `rasgo`, `valor`), marcados como `modelada`.

### `metadata.json`

```json
{
  "run_id": "2026-10-14_ES_100000_s42",
  "territorio": {"tipo": "pais", "codigo": "ES"},
  "tamano_solicitado": 100000,
  "tamano_obtenido": 100000,
  "modo": "representativo",
  "semilla": 42,
  "fecha_referencia": "2026-01-01",
  "fuentes": [{"id": "censo2021_personas", "edicion": "...", "sha256": "..."}],
  "objetivos_calibrados": ["edad_5 x sexo", "nacionalidad_grupo", "..."],
  "objetivos_reservados": ["estudios_3 x edad_4", "..."],
  "metodo_calibracion": "...",
  "version_codigo": "git:abcdef1",
  "validacion": {"estado": "superada", "informe": "reports/<run_id>/validacion.md"}
}
```

## 5. Interfaz de línea de comandos

```bash
# Ingesta y preparación
sinpop ingest --source all
sinpop harmonize --source all
sinpop targets --territory ES --date 2026-01-01

# Generación
sinpop build --territory ES --size 100000 --seed 42
sinpop build --territory CCAA:07 --size 20000 --seed 42
sinpop build --territory PROV:42 --size 20000 --seed 42 --oversample "edad_5>=85:2000"
sinpop build --territory MUNIS:configs/territorios/area_valencia.yaml --size 50000 --seed 42

# Validación
sinpop validate --run <run_id>
sinpop validate --phase 4
sinpop audit --run <run_id>          # sesgos y minorías

# Fases posteriores
sinpop opinion --run <run_id>
sinpop politics --run <run_id> --election generales-2023
sinpop temporal --run <run_id> --from 2023-01 --to 2026-06
sinpop predict --run <run_id> --question preguntas/q01.json
sinpop predict --run <run_id> --event preguntas/e01.json
sinpop evaluate --tag <etiqueta_congelada>   # fase 11, una sola vez
```

## 6. Stack recomendado

| Necesidad | Propuesta | Alternativas |
| --- | --- | --- |
| Lenguaje | Python 3.11+ | — |
| Tablas | Polars o pandas, con PyArrow y Parquet | DuckDB para consultas grandes |
| Calibración | Implementación propia testeada de raking y GREG acotado | `samplics`, `ipfn` |
| Modelos estadísticos | statsmodels, scikit-learn | — |
| Modelos multinivel, multinomiales y latentes (F8A–F8C) | PyMC o Bambi | `factor_analyzer`, `girth` para IRT |
| Configuración | YAML con validación por esquema (pydantic) | — |
| Tests | pytest, hypothesis para pruebas por propiedades | — |
| CLI | Typer | Click |
| Informes | Markdown y gráficos en PNG (matplotlib) | — |

## 7. Reproducibilidad

- Un generador aleatorio por ejecución (`numpy.random.default_rng(seed)`), pasado explícitamente a cada función.
- Los ficheros de salida se ordenan de forma determinista antes de escribirse.
- `metadata.json` guarda el hash de cada fichero de salida.
- Un test de integración genera dos veces la misma población y compara los hashes.
