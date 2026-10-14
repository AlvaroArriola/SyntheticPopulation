# 08 · Uso y licencias

El proyecto es de **uso no comercial** (decisión D-007). Este documento recoge lo poco que hay que tener en cuenta sobre las condiciones de uso de los datos y los principios básicos de trabajo con ellos.

## 1. Condiciones de uso de las fuentes

| Fuente | Condición principal | Qué hacemos |
| --- | --- | --- |
| INE (Censo, Padrón, ECV, EPA, TIC-H, EPF, Atlas de renta…) | Citar al INE como fuente del dato primario; los resultados derivados son responsabilidad de quien los elabora | Citar la fuente en cada informe y ficha de datos |
| CIS | Citar el número de estudio y al CIS como fuente | El banco de preguntas y los informes guardan el número de estudio de cada pregunta |
| ESS | Uso gratuito para fines no comerciales, previo registro; citar la ronda y la edición | Registrar la cita exacta de cada edición descargada |
| Ministerio del Interior (resultados electorales) | Datos públicos; citar la fuente | Citar la elección y la fuente |
| Centros autonómicos (CEO, Sociómetro y otros) | Varían según el centro | Revisar en F1 y registrar en `MANIFEST.yaml` |

Las condiciones de cada fichero se registran en `data/raw/MANIFEST.yaml`.

## 2. Principios de trabajo con los datos

1. **Los microdatos originales se quedan en local.** No se suben a servicios externos ni se envían a modelos de lenguaje. Al LLM solo llegan perfiles sintéticos o agregados.
2. **No se intenta reidentificar a nadie.** Los microdatos oficiales están anonimizados y se usan así: no se cruzan con fuentes que permitan identificar personas.
3. **Lo sintético se presenta como sintético.** Los informes y salidas indican que se trata de una simulación basada en datos reales, no de una encuesta ni de datos de personas concretas.
4. **La población describe grupos, no personas.** Una persona sintética es un caso plausible dentro de una distribución; sus atributos no permiten afirmar nada sobre una persona real con el mismo perfil.

## 3. Lista de comprobación (F12)

- [ ] Cada fuente tiene su cita y sus condiciones registradas en `MANIFEST.yaml`.
- [ ] Los informes y fichas de datos citan las fuentes usadas.
- [ ] Ningún microdato original ha salido del entorno local ni se ha enviado a un modelo de lenguaje (comprobado en los registros de `logs/llm/`).
- [ ] Las salidas indican que son resultados simulados.
