# Instrucciones para el agente de código

Este archivo define cómo trabajar en este proyecto. Léelo entero antes de empezar y vuelve a él cuando dudes.

## Antes de escribir código

1. Lee `README.md`, `DECISIONS.md` y `docs/01` a `docs/08` en orden. `docs/02_datos_y_variables.md` y `docs/06_sesgos_y_minorias.md` son los más importantes y no se pueden saltar.
2. Comprueba en qué fase está el proyecto: el último informe en `reports/` y el estado de `DECISIONS.md`.
3. Trabaja **solo en la fase actual**. No adelantes trabajo de fases posteriores salvo que la fase actual lo exija.

## Reglas no negociables

1. **No se avanza de fase sin superar su puerta.** Cada fase de `docs/04_fases.md` tiene criterios de salida. Ejecuta `sinpop validate --phase N`. Si algún criterio falla, arréglalo o documenta por qué no se puede y pide decisión humana. Nunca relajes un umbral sin registrarlo en `DECISIONS.md` y sin aprobación humana.
2. **Nunca inventes códigos ni significados de variables.** Cada variable que leas de un fichero oficial se verifica contra su diseño de registro o su cuestionario original. Si un código no aparece documentado, detente y regístralo como duda en `DECISIONS.md`. Ejemplos típicos de error: tratar «No sabe» (a menudo 8, 98 o 998) o «No contesta» (9, 99 o 999) como valores numéricos; confundir códigos de comunidad autónoma con códigos de provincia; usar códigos de estudios de una clasificación distinta.
3. **Nada de datos inventados.** Si falta un dato, no lo rellenes con suposiciones. Documenta el hueco y propón una fuente o un método.
4. **Usa siempre los pesos de las encuestas.** Las estadísticas descriptivas de microdatos de encuestas (CIS, ECV, EPA, TIC-H, ESS…) se calculan ponderadas. Un resultado sin ponderar se marca explícitamente como tal.
5. **Separación física de los datos de evaluación.** Todo lo que esté en `data/eval/` está prohibido para cualquier paso de construcción o ajuste. Hay un test (`tests/test_no_leakage.py`) que falla si algún módulo fuera de `src/sinpop/evaluate/` lo lee. No lo desactives.
6. **Reproducibilidad.** Toda ejecución recibe una semilla. La misma configuración y la misma semilla deben producir ficheros idénticos (mismo hash). Nada de aleatoriedad sin semilla.
7. **Trazabilidad.** Cada fichero generado lleva metadatos: fuentes y versiones usadas, configuración, semilla, fecha y versión del código.
8. **Datos originales en local y fuentes citadas.** No subas microdatos originales a ningún servicio externo, incluido un modelo de lenguaje: al LLM solo le llegan perfiles sintéticos o agregados. Cita cada fuente según `docs/08_uso_y_licencias.md`.
9. **Capas separadas.** Ninguna variable de opinión ni política entra en `persons.parquet`. Viven en `opinion.parquet` y `politics.parquet`, unidas por `person_id`. Hay un test que lo comprueba.
10. **Reglas de la capa política.**
    - El recuerdo de voto se calibra contra **resultados oficiales**, nunca contra el recuerdo declarado en el CIS.
    - Solo reciben recuerdo de voto las personas con derecho a voto en esa elección.
    - La intención de voto y la valoración de líderes **no** son atributos de la persona.
    - Toda correspondencia entre partidos de distintas elecciones o estudios va en `configs/partidos.yaml` y se documenta en `DECISIONS.md`.
    - «No sabe», «No recuerda» y «No contesta» son respuestas legítimas: se modelan como una opción más, no se eliminan.
    - Aplica las mismas pruebas y el mismo tono a todos los electorados.
11. **Modelos de lenguaje.** Usa solo los modelos de `configs/llm.yaml`. Versiona los prompts en `prompts/`, valida cada salida contra su esquema, usa la caché, registra las llamadas y respeta el presupuesto.

## Forma de trabajar

- **Pequeño y verificable.** Prefiere funciones pequeñas con tests. Cada transformación de datos tiene un test que comprueba al menos: número de filas esperado, ausencia de valores fuera de dominio y conservación de totales ponderados.
- **Primero el informe, luego la conclusión.** Cuando analices un dato, genera la tabla o el gráfico y guárdalo en `reports/`. No resumas resultados de memoria.
- **Registra las decisiones.** Cada elección relevante (método de calibración, recodificación, variable descartada, umbral) va a `DECISIONS.md` con alternativas consideradas, evidencia y fecha.
- **Pide revisión humana** en las puertas marcadas como «revisión humana» en `docs/04_fases.md`. Prepara el informe de fase y detente.
- **Descarga de datos.** Algunas fuentes requieren aceptar condiciones o registrarse (por ejemplo, el CIS o la ESS). Si no puedes descargar un fichero, no busques copias en sitios no oficiales: añade una entrada en `data/raw/MANUAL_DOWNLOADS.md` con la URL oficial y el nombre de fichero esperado, y continúa con lo demás.
- **Datos grandes.** Los microdatos del Censo tienen millones de registros. Lee por columnas y por bloques, usa Parquet y Polars o DuckDB, y no cargues en memoria más de lo necesario.
- **Si la documentación se contradice o se queda corta**, no improvises: registra la duda en `DECISIONS.md` con tu propuesta y, si afecta a una puerta de fase, pide decisión humana.

## Cuando algo no cuadre

Si una validación falla, sigue este orden:

1. Comprueba primero los datos de entrada: códigos, pesos, filtros, universo (por ejemplo, 16+ frente a 18+, hogares frente a personas).
2. Después la armonización.
3. Por último el método.

Muchos fallos aparentes de método son en realidad errores de códigos o de universo.

## Definición de terminado (para cualquier tarea)

- El código tiene tests y pasan.
- La validación de la fase actual se ha ejecutado y su resultado está en `reports/`.
- `DECISIONS.md` está actualizado.
- Se puede reproducir desde cero con un solo comando documentado en el informe.
