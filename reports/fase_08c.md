# Fase 08C · Dimensión temporal

**Estado:** puerta automática superada (G8C.1–G8C.3). F8C no tiene revisión humana obligatoria (`docs/04`).
**Fecha:** 2026-10-21 · **Versión del código:** ver `reports/fase_08c_validacion.json` (`version_codigo`)
**Comando para reproducir** (tras la cadena de `reports/fase_08b.md`):

```
python -c "from sinpop.temporal import trayectorias as T, eventos as E; T.construir('2026-01-01_ES_1000000_s1'); E.construir()" \
  && python -m sinpop.validate.fase8c && sinpop validate --phase 8c
```

## Resumen

- **Indicadores** (`configs/temporal.yaml`), mensuales, de enero de 2023 a junio de 2026:
  - situación económica de España y personal;
  - autoubicación en bloques;
  - partido más cercano;
  - mención de vivienda, inmigración, paro, economía y política entre los principales problemas.
  - Fuente: 39 barómetros del CIS (agosto no tiene barómetro).
- **Efectos de periodo** (`src/sinpop/temporal/modelo.py`):
  - Un perfil estático, más un nivel local por mes (paseo aleatorio con ruido, filtro de Kalman) a escala nacional y por grupo de edad, comunidad y voto de 2023.
  - El ruido y la variabilidad del paseo se estiman por máxima verosimilitud.
- **`trajectories.parquet`:** 840.249 adultos × 42 meses (35,3 millones de filas).
  - Cada persona conserva un cuantil fijo por indicador, así que su trayectoria es coherente en el tiempo y su grupo reproduce la evolución observada.
  - Todas las trayectorias son `modelada` (no son la historia de personas reales); las de fuera del universo del CIS, `extrapolada`.
- **Banco de efectos de eventos:**
  - 16 eventos con fecha y fuente oficial o primaria (`configs/eventos.yaml`).
  - Cambio antes/después por indicador, categoría y grupo, con IC 95 %: 3.750 filas en `data/processed/temporal/banco_efectos_eventos.parquet`; la parte nacional está en `reports/fase_08c/banco_efectos_nacional.csv`.

## Puerta de salida

| ID | Resultado | Valor |
| --- | --- | --- |
| G8C.1 V-TEMPORAL | ✅ | Error medio 1,90 puntos frente a 2,29 de la persistencia (870 predicciones de t + 1 a t + 3, 11 orígenes, solo con datos hasta t) |
| G8C.2 V-TEMPORAL-SERIES | ✅ | Diferencia absoluta media 1,57 puntos (umbral 2) en 1.170 mes × categoría |
| G8C.3 Banco de eventos | ✅ | 16/16 eventos con fecha, fuente y efecto con IC 95 % |

**Reproducibilidad:** ver `trajectories_metadata.json` (sha256). Dos construcciones con la misma semilla se comparan en la sección final.

## Resultados por indicador

| Indicador | *Backtest*: modelo / persistencia (pp) | Series: diferencia media con el CIS (pp) |
| --- | --- | --- |
| cercanía a partido | 0,72 / 1,07 | 1,49 |
| economía de España | 1,88 / 2,38 | 1,82 |
| economía personal | 1,09 / 1,88 | 1,49 |
| ideología (bloques) | 0,98 / 1,53 | 2,30 |
| problema: economía | 2,50 / 2,69 | 0,70 |
| problema: inmigración | 3,86 / 4,08 | 1,48 |
| problema: paro | 2,18 / 2,20 | 1,20 |
| problema: política | 4,59 / 5,08 | 1,73 |
| problema: vivienda | 4,61 / 4,44 | 1,30 |

- **Vivienda:** es el único indicador en que la persistencia gana. Tiene una tendencia sostenida (del 3,5 % en enero de 2023 al 42-49 % en 2026) que el paseo aleatorio, sin pendiente, sigue con retraso.
- **Ideología:** su diferencia de series es sobre todo de **composición**. La población está calibrada al voto oficial (D-067), mientras que los encuestados del CIS recuerdan más voto al PSOE (30,9 % frente al 22,1 % oficial) y menos abstención (15,8 % frente al 29,6 %). Por eso la población tiene menos «izquierda» (36 % frente a 43-47 %).
- **Octubre de 2025:** es un barómetro atípico (3,6 puntos de diferencia media) que el nivel suavizado no sigue.

## Limitaciones

- **Grupo de voto:** antes de agosto de 2023 el recuerdo de 2023 no existe. Hasta entonces las trayectorias solo dependen del perfil y del nivel por edad y comunidad.
- **Eventos:** el efecto es el cambio observado, no causal. Los eventos cercanos (e001 y e002) comparten ventanas, y con dos barómetros a cada lado se mezclan con la tendencia.
- **Universo:** el CIS solo entrevista a españoles. Las trayectorias de extranjeros y residentes en colectivos son extrapolaciones.
