# Fase 12 · Empaquetado y documentación final

**Estado:** en curso.
- Lo que no depende del modelo de lenguaje está hecho.
- La ficha de modelo final se escribe tras F11, con sus resultados.
- G12.1 y G12.4 son de revisión humana.

**Fecha:** 2026-10-22 · **Decisiones:** D-071, D-072
**Comando:** `python tools/prueba_actualizacion.py && python -m sinpop.audit.citas && sinpop validate --phase 12`

## Entregables

| Tarea (`docs/04`) | Estado | Dónde |
| --- | --- | --- |
| Ficha de datos | Hecha por población (F4-F7) | `reports/<run_id>/ficha.md` |
| Ficha de modelo | Pendiente de F11 | `reports/ficha_modelo.md` |
| Guía de uso con ejemplos de la CLI | Hecha | `docs/guias/uso.md` |
| Guía de actualización de fuentes, incluida la actualización tras unas elecciones | Hecha y probada (G12.2) | `docs/guias/actualizacion.md` §1-2 |
| Límites de uso | Hechos | `docs/guias/limites_de_uso.md` |
| Actualización mensual (barómetro nuevo, mover el corte) | Hecha | `docs/guias/actualizacion.md` §3 |
| Citas de las fuentes | Generadas | `docs/guias/fuentes_y_citas.md` |

## Puerta de salida

| ID | Resultado | Valor |
| --- | --- | --- |
| G12.1 Una persona ajena genera y valida una población con la guía | ⏸️ | Revisión humana: hace falta alguien ajeno al proyecto |
| G12.2 Prueba de la guía de actualización | ✅ | EPA 2T 2026 → 1T 2026: 0 valores fuera de dominio; 4/4 cifras de la nota de prensa; producción intacta |
| G12.3 Lista de comprobación de `docs/08` | ✅ | 863 ficheros con condiciones; cita para cada fuente; caché del LLM sin microdatos; salidas marcadas como simuladas |
| G12.4 Revisión humana final | ⏸️ | Tras F11 |

## Cambios hechos al empaquetar

- **CLI:** `sinpop politics`, `sinpop temporal` y `sinpop predict` (preguntas y eventos) ya ejecutan las capas validadas. La evaluación final se lanza aislada (`python -m sinpop.evaluate.final`) por la regla 5.
- **EPA:** la edición se lee de `configs/sources.yaml` y las cifras oficiales están por edición. Con la edición en uso, el fichero armonizado es idéntico, byte a byte, al de producción.
- **Fecha de corte:** `tests/unit/test_corte.py` impide mover la fecha de corte en unas capas y no en otras.

## Qué necesita revisión humana

- **G12.1:** que alguien ajeno al proyecto siga `docs/guias/uso.md` en un equipo limpio, genere una población y la valide. Después se registra «### Aprobación de G12.1» en `DECISIONS.md`.
- **El umbral propuesto de la prueba contrafactual del LLM** (V-LLM-ESTEREOTIPO = 1,25, D-071).
