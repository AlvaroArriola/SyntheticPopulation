# Fase 00 · Preparación del proyecto

**Estado:** superada
**Fecha:** 2026-10-14 · **Versión del código:** git:af9dae0
**Comando para reproducir:** `pip install -e ".[dev]" && sinpop validate --phase 0`

## Resumen

Repositorio creado con la estructura de `docs/03_arquitectura.md` (sección 3), paquete instalable `sinpop`, esquemas pydantic estrictos para las 10 configuraciones, CLI con los 11 comandos documentados y `tests/test_no_leakage.py` con autotests del detector. Las configuraciones de partida recogen literalmente las propuestas de `docs/02`, `docs/04`, `docs/05` y `docs/06`; lo que depende de los datos queda marcado como pendiente de verificar, sin inventar códigos. La puerta F0 se supera (4/4).

## Resumen de objetivo, fases y reglas (lectura inicial)

1. Objetivo: población sintética de adultos (18+) residentes en España, con hogares completos, fiel a datos oficiales, de tamaño variable y construida y calibrada para cualquier territorio (no filtrada de la nacional).
2. Prioridad absoluta: el núcleo F0–F7 (datos, armonización, objetivos, población nacional, territorial, enriquecimiento y auditoría de sesgos y minorías).
3. Extensión F8A–F12 (opinión, política calibrada a resultados oficiales, dimensión temporal, predicción y confianza) solo tras aprobar F7, en ficheros separados unidos por `person_id`.
4. Método base: remuestreo de hogares donantes del Censo 2021 + calibración (raking/GREG acotado) + integerización con semilla.
5. No se avanza sin superar la puerta; las puertas de revisión humana (F1, F2, F4, F5, F7, F8A, F8B, F11, F12) detienen el trabajo.
6. Nunca inventar códigos ni datos; verificar cada variable contra su diseño de registro; NS/NC/NP como categorías explícitas.
7. Todo agregado de encuesta, ponderado. Validar con objetivos reservados, no solo con los calibrados.
8. `data/eval/` solo lo usa `sinpop.evaluate`; reproducibilidad por semilla y hash; trazabilidad en metadatos.
9. Microdatos originales solo en local; al LLM solo llegan perfiles sintéticos o agregados.
10. Umbrales en `configs/thresholds.yaml`: nunca se cambian sin `DECISIONS.md` y aprobación humana.

## Puerta de salida

| ID | Comprobación | Resultado | Valor | Umbral |
| --- | --- | --- | --- | --- |
| G0.1 | `pytest` se ejecuta sin errores | ✅ | 43 tests superados | 0 fallos |
| G0.2 | Las configuraciones pasan la validación de esquema | ✅ | 10/10 | 10/10 |
| G0.3 | `test_no_leakage.py` existe y falla ante una lectura provocada de los datos de evaluación | ✅ | 6 autotests del detector (ruta directa, `Path / "eval"`, ruta Windows, importación de `sinpop.evaluate`, paquete permitido, falsos positivos) | existe y sus autotests pasan |
| G0.4 | `sinpop --help` muestra todos los comandos | ✅ | 11/11 | 11/11 |

Detalle automático: [`fase_00_puerta.md`](fase_00_puerta.md).

## Resultados principales

- `src/sinpop/config/schemas.py`: un esquema por fichero, con reglas de coherencia (objetivos calibrados y reservados disjuntos, familias de partidos existentes, al menos una elección reservada, provincias con CCAA válida, recodificaciones dentro de dominio y NS/NC/NP admitidos como especiales, modelos LLM con fecha de corte anterior a la de construcción).
- `src/sinpop/validate/layers.py`: comprobación de separación de capas (ninguna variable P3/P3-POL ni volátil en la población base), con tests.
- `src/sinpop/repro.py`: generador aleatorio con semilla obligatoria, SHA-256 de ficheros y versión del código.
- `src/sinpop/validate/phases.py`: puertas F0 y F1 ejecutables con `sinpop validate --phase N`.

## Decisiones tomadas

- D-008 · Herramientas (Python, Polars, pydantic, Typer, pytest, Ruff).
- D-009 · Solo `sinpop.evaluate` lee o escribe los datos de evaluación (propuesta; resuelve una contradicción entre la regla 5 y F8A).
- D-010 · V-REPRO compara los ficheros de datos, no `metadata.json` (propuesta).
- D-011 · G3.4 se comprueba por objetivo (cruce), no por variable suelta (propuesta).
- D-012 · Códigos territoriales y dominios de partida, con dominios pendientes donde dependen de la fuente (propuesta).
- D-013 · Umbrales completados con `docs/05`, sin cambiar ninguno.

## Contradicciones y dudas encontradas en la documentación

1. Regla 5 de `CLAUDE.md` frente a F8A tarea 6 (quién escribe en `data/eval/`) → D-009.
2. RNF-01 (hash idéntico) frente a `metadata.json` con fecha → D-010.
3. G3.4 al pie de la letra frente a la propuesta de `targets.yaml` → D-011.
4. La lista de vigilancia usa «privación material severa», que no está en el diccionario; `docs/03` usa `recuerdo_voto_generales_familia` como subgrupo sin definirla → D-012.
5. El tramo superior de `edad_5` no está fijado (85+ frente a tramos del Padrón hasta 100+) → D-012.

## Problemas abiertos y riesgos

- **Bloqueo de red (D-014):** el entorno no puede acceder a las webs del INE, CIS, Ministerio del Interior ni ESS. F1 no puede completarse sin una de las dos vías de `data/raw/MANUAL_DOWNLOADS.md`.

## Qué necesita revisión humana

F0 no requiere revisión humana. Las decisiones D-009 a D-012 y D-014 quedan propuestas para la revisión de F1.
