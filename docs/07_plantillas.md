# 07 · Plantillas

## 1. `DECISIONS.md`

Una entrada por decisión, en orden cronológico. Las decisiones no se borran: si cambian, se añade una nueva que sustituye a la anterior.

```markdown
## D-0XX · <Título corto>

- **Fecha:** AAAA-MM-DD
- **Fase:** FX
- **Estado:** propuesta | aprobada | sustituida por D-0YY
- **Contexto:** qué problema o duda la motiva.
- **Alternativas consideradas:**
  1. …
  2. …
- **Evidencia:** datos, tablas o pruebas que la justifican (enlace a `reports/…`).
- **Decisión:** qué se hace.
- **Consecuencias:** qué cambia y qué hay que revalidar.
- **Aprobada por:** humano | agente (solo si no requiere aprobación)
```

Las decisiones de partida (D-001 a D-006) ya están en `DECISIONS.md`.

## 2. Informe de fase · `reports/fase_XX.md`

```markdown
# Fase XX · <Nombre>

**Estado:** superada | fallida | pendiente de revisión humana
**Fecha:** AAAA-MM-DD · **Versión del código:** git:<hash>
**Comando para reproducir:** `…`

## Resumen
Tres o cuatro frases: qué se ha hecho y el resultado.

## Puerta de salida
| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| GX.1 | … | ✅ / ❌ | … | … |

## Resultados principales
Tablas y gráficos (enlazados a `reports/<run_id>/`).

## Decisiones tomadas
Lista de D-0XX con una línea cada una.

## Problemas abiertos y riesgos
…

## Qué necesita revisión humana
Preguntas concretas para quien revisa.
```

## 3. Ficha de datos de una población · `reports/<run_id>/ficha.md`

```markdown
# Ficha de datos · <run_id>

## Identificación
- Territorio: …
- Tamaño: … personas, … hogares
- Modo: representativo | sobremuestreo (<grupos>)
- Fecha de referencia: …
- Semilla: … · Versión del código: …

## Fuentes
| Fuente | Edición | Uso (referencia / donantes / enriquecimiento) | Fecha de referencia |
| --- | --- | --- | --- |

## Variables
| Variable | Prioridad | Fuente | Método (observada / emparejada / modelada / extrapolada) | % de valores por método |
| --- | --- | --- | --- | --- |

## Calidad
- Validación: superada | fallida (enlace al informe)
- Donantes locales: …%
- Confianza esperada del territorio: alta | media | baja

## Grupos vigilados
| Grupo | Ratio de representación | Semáforo |
| --- | --- | --- |

## Limitaciones conocidas
- Grupos no observables: …
- Variables con desfase temporal: …
- Otras: …

## Límites de uso
(Sección 7 de `06_sesgos_y_minorias.md`, adaptada.)
```

## 4. `configs/watchlist.yaml` (ejemplo)

```yaml
grupos:
  - id: mayores_85
    nombre: "Personas de 85 años o más"
    definicion: "edad >= 85"
    referencia: padron
    recuento_minimo: 500
  - id: mayores_solos
    nombre: "Personas de 65+ que viven solas"
    definicion: "edad >= 65 and tipo_hogar == 'unipersonal'"
    referencia: censo2021_tablas
    recuento_minimo: 500
  - id: nac_marruecos
    nombre: "Nacionalidad marroquí"
    definicion: "nacionalidad_top == 'MAR'"
    referencia: padron
    recuento_minimo: 300
  - id: abstencion_generales
    nombre: "Abstencionistas en las generales de 2023"
    definicion: "recuerdo_voto_generales == 'abstencion'"
    referencia: infoelectoral
    capa: politica
```

## 5. `configs/thresholds.yaml` (extracto)

```yaml
V-MARG:
  factor_tvd_ref: 1.2
  tolerancia: 0.002
V-CRUCE:
  espana: 0.03
  ccaa: 0.05
  provincia: 0.08
V-PESOS:
  convergencia_max: 0.001
  rango_factor: [0.2, 5.0]
  proporcion_en_rango: 0.99
  kish_min_ratio: 0.30
V-DONANTES:
  kish_min: 200
  locales_alerta: 0.50
V-MINORIAS:
  ratio: [0.9, 1.1]
  recuento_esperado_min: 200
V-DIVERSIDAD:
  ratio_entropia_min: 0.9
  proporcion_grupos: 0.95
  tamano_grupo_min: 100
V-CONCENTRACION:
  top5_max: 0.20
  donantes_distintos_min: 50
V-POL-RECUERDO:
  factor_tvd_ref: 1.2
  tolerancia: 0.005
V-POL-RESERVADA:
  tvd_espana: 0.04
  tvd_ccaa: 0.06
  error_participacion_max: 0.03
V-POL-PERFIL:
  tvd_max: 0.08
  casos_cis_min: 300
V-POL-COHERENCIA:
  error_media_max: 0.3
  ratio_sd: [0.8, 1.2]
V-POL-TRANSFERENCIA:
  tvd_fila_max: 0.10
  casos_fila_min: 200
V-TEMPORAL-SERIES:
  error_medio_max_pp: 2.0
V-COBERTURA:
  ic80: [0.70, 0.90]
  ic95: [0.88, 0.99]
```

## 6. `configs/partidos.yaml` (ejemplo de estructura)

Los códigos y familias concretos se completan en F2 a partir de los resultados oficiales y de los diseños de registro del CIS. Este ejemplo solo muestra la forma.

```yaml
familias:
  - id: izquierda_estatal
    nombre: "Izquierda de ámbito estatal"
  - id: socialdemocrata
    nombre: "Socialdemócrata"
  - id: centro_derecha_estatal
    nombre: "Centro-derecha de ámbito estatal"
  - id: derecha_radical
    nombre: "Derecha radical"
  - id: nacionalista_regionalista
    nombre: "Nacionalistas y regionalistas"
    desglose_por_territorio: true
  - id: otros
    nombre: "Otras candidaturas"

elecciones:
  generales-2023:
    fecha: 2023-07-23
    fuente: infoelectoral
    candidaturas:
      - codigo_oficial: "<código del Ministerio del Interior>"
        nombre: "<candidatura>"
        familia: "<id de familia>"
        codigos_cis:
          "<id estudio CIS>": "<código en la variable de recuerdo>"
        notas: "Coalición formada por …; correspondencia con la elección anterior: …"
```

## 7. `configs/eventos.yaml` (ejemplo de estructura)

```yaml
eventos:
  - id: e001
    fecha: AAAA-MM-DD
    descripcion: "<qué ocurrió>"
    tipo: economico | social | politico | catastrofe | internacional
    ambito: ES | CCAA:XX
    fuente: "<URL oficial o de prensa>"
    indicadores_afectados: ["<pregunta o serie del CIS>"]
```
