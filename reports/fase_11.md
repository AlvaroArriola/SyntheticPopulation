# Fase 11 · Evaluación final sin contaminación

> **Aprobada el 2026-10-23** («Aprobación de F11» en `DECISIONS.md`). Después se corrigieron las escalas (D-089) para el uso del producto. **El resultado oficial de esta evaluación no cambia (0,158)** y no se ha repetido. Con el sistema corregido, el mismo barómetro da 0,078; esa cifra es informativa y está en `reports/validacion.md`. La hipótesis de la línea «Hipótesis pendiente de comprobar» se confirmó: era la lista de opciones del banco, que no tenía los valores intermedios de las escalas con solo los extremos etiquetados.


**Estado:** G11.1 y G11.2 superadas. **Revisión humana (G11.3): aprobada.**
**Fecha:** 2026-10-23 · **Decisiones:** D-086, «Aprobación de F9», D-089
**Código congelado:** etiqueta `f11-congelacion-2026-10-23`, commit `0e40628e`, árbol limpio. La etiqueta queda en local porque el entorno solo deja subir la rama; el commit está en el remoto.
**Comando** (una sola vez; si ya existe `reports/fase_11_evaluacion.json`, se niega a repetirse):

```
git checkout f11-congelacion-2026-10-23
python -m sinpop.evaluate.final --tag f11-congelacion-2026-10-23
sinpop validate --phase 11
```

## Qué se evaluó

- **Ventana:** barómetro del CIS de octubre de 2026 (estudio 3582), posterior al corte de los datos (junio de 2026). Ningún paso anterior lo había leído (regla 5).
- **Preguntas:** 90 evaluables, de ellas 16 políticas y 74 de vida cotidiana. En 18 no había análogas fiables y respondió el LLM anclado; 5 no tenían ninguna análoga alineable.
- **Medida:** TVD entre la distribución predicha (como la mediría el CIS) y la observada ponderada. 0 es perfecto; 0,10 equivale a 10 puntos desplazados en total.

## Resultados

| | Preguntas | Sistema final | B0 (análoga más parecida) | B1 (análogas ponderadas) | B2 (LLM sin anclaje) |
| --- | --- | --- | --- | --- | --- |
| Todas | 90 | **0,158** | 0,190 | 0,189 | 0,262 |
| Políticas | 16 | **0,095** | 0,095 | 0,094 | 0,181 |
| Vida cotidiana | 74 | **0,172** | 0,212 | 0,211 | 0,278 |

- **Subgrupos** (edad, sexo, estudios): sistema 0,196, B1 0,194.
- **Comunidades:** sistema 0,206, B1 0,204.
- **Cobertura de los intervalos:**
  - IC 80 %: 0,57. Por debajo del rango de validación (0,70-0,90): los intervalos son demasiado estrechos.
  - IC 95 %: 0,94, dentro del rango.
- **Preguntas sin precedentes:** el LLM anclado (18 preguntas) da 0,179. En las 13 que también tenían estimador estadístico: 0,177 frente a 0,392. Es lo que más mejora el sistema frente a los baselines.
- **Confianza declarada (F10):**
  - Spearman con el error 0,81, mejor que en validación (0,74);
  - ECE 0,058, por encima del umbral de F10 (0,05): algo sobreconfiada en la franja media;
  - la confianza baja con el tamaño del subgrupo (0,56) y de la comunidad (0,58), como debe.

Detalle por pregunta en `reports/fase_11/preguntas.csv` y de la confianza en `reports/fase_11/confianza.csv`.

## Análisis de errores

**Hipótesis comprobada: el error se concentra en las escalas 1-10 de valoración de ministros y líderes (D-089).**

| | Preguntas | Sistema final | B0 | B1 | B2 | IC 80 % |
| --- | --- | --- | --- | --- | --- | --- |
| Escalas 1-10 (`VALMINIS`, `VALORALIDERES`) | 26 | 0,351 | 0,351 | 0,351 | 0,443 | 0,39 |
| Resto | 64 | **0,080** | 0,118 | 0,118 | 0,187 | 0,73 |

- **Sin las escalas,** el error baja a 0,080 (políticas 0,030, vida cotidiana 0,092) y la cobertura del IC 80 % vuelve a su rango.
- **Las escalas fallan igual con cualquier método** (sistema, B0 y B1 dan lo mismo). Eso apunta a los datos de entrada, no al método, como pide revisar primero CLAUDE.md.
- **Lo mismo pasa en validación,** donde ya se vio la anomalía (D-089). En el estudio 3571 la escala solo tiene etiquetados los extremos. En el 3577 y el 3582 viene completa y el error se dispara.
- **Hipótesis pendiente de comprobar:** las análogas del banco tienen la escala etiquetada de otra forma (solo los extremos, o con valores agrupados) y la alineación de opciones las empareja mal. La corrección propuesta (tratar las escalas 1-10 como numéricas en todo el banco) cambiaría el método. Se decidiría después de esta evaluación, que no se repite.

**Resto de errores grandes:** temas nuevos sin precedente en el banco.
- `P1`, `P2`, `P4`: preguntas de actualidad de octubre.
- `VIVIENDA_*`: un bloque de vivienda con similitud de 0,22-0,28.

Son los casos para los que existe el LLM anclado, que aquí mejora mucho al estadístico (0,18 frente a 0,39).

## Elección posterior a la congelación (tarea 5)

No se ha registrado ninguna estimación antes de una elección posterior a la congelación. Queda como prueba prospectiva, junto con la del modo evento (Aprobación de F9).

## Lectura para la persona responsable

- **Lo que funciona:**
  - preguntas recurrentes y políticas (0,03 sin las escalas);
  - preguntas de actualidad con el LLM anclado (0,18, frente a 0,39 sin él);
  - el orden de la confianza (Spearman 0,81).
- **Lo que no:**
  - las escalas 1-10, por un problema de datos de entrada que ya estaba señalado (D-089);
  - por eso, los intervalos del 80 % estrechos y la confianza algo alta en el conjunto.
- **El coste total del LLM en el proyecto** es de 5,23 € de 15 €.

Si apruebas la evaluación, añade en `DECISIONS.md` una entrada «### Aprobación de F11» con «**Estado:** aprobada». Indica también si se corrigen las escalas (D-089) para el uso del producto. Esta evaluación final no se repetiría.
