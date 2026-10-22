# Límites de uso

Esta sección acompaña a cada población, informe y predicción (`docs/06` §7, `docs/08` §2). Si se comparten resultados, se comparte también este texto, adaptado.

## Qué es y qué no es

- **Es una simulación.** La población sintética se construye con datos oficiales (`docs/guias/fuentes_y_citas.md`), pero ninguna persona sintética existe. Las salidas de predicción son resultados simulados, no una encuesta (`resultado_simulado`).
- **Describe distribuciones, no personas.** Una persona sintética es un caso plausible dentro de una distribución. Sus atributos no permiten afirmar nada sobre una persona real con el mismo perfil.

## Usos que no se deben hacer

- Tomar decisiones sobre individuos reales.
- Sustituir a una encuesta cuando la decisión es crítica o afecta a derechos de las personas.
- Dirigir acciones a grupos vulnerables sin una validación específica para ese grupo.
- Afirmar qué vota o qué piensa una persona real con un perfil determinado. La capa política describe tendencias de grupo, calibradas a resultados oficiales.
- Intentar reidentificar a nadie, o cruzar la población con fuentes que lo permitan.

## Cuándo fiarse menos

- **Grupos pequeños.** Los grupos en ámbar o rojo de la auditoría (`reports/fase_07.md` y `reports/<run_id>/`) y los no observables no se analizan por separado sin advertir de su baja fiabilidad.
- **Territorios pequeños.** Las estimaciones por provincia o municipio tienen menos confianza que las nacionales y autonómicas. La confianza de cada territorio está en su informe; los de pocos donantes locales la declaran como reducida (G5.4, G5.5).
- **Predicciones:**
  - Cada una trae su confianza (la probabilidad de que el error sea ≤ 0,10) y sus intervalos. Una confianza baja significa exactamente eso.
  - Las preguntas sin precedentes en el banco y los subgrupos con pocos datos son los casos más débiles (`reports/fase_09.md` y `reports/fase_10.md`).
  - En el modo evento, sin modelo de lenguaje, la predicción no sabe quién gana o pierde con el evento.
- **Opinión y política.** La capa de opinión hereda los sesgos de respuesta de las encuestas usadas (CIS, ESS). La capa política hereda las limitaciones del recuerdo de voto, aunque esté calibrada a resultados oficiales.
- **Fecha de referencia.** Todo describe la situación con datos hasta el 30 de junio de 2026. Lo posterior es predicción, no dato.

## Modelo de lenguaje

- Cuando interviene, las salidas lo dicen (`versiones.modelo_llm`, `parametros_llm`).
- Las pruebas de estereotipos de `docs/06` §5 se informan en `reports/fase_09.md`.
- El modelo no ve microdatos ni personas sintéticas concretas: solo enunciados públicos y agregados.
