# Registro de decisiones

Formato de cada entrada en `docs/07_plantillas.md`. Las decisiones no se borran: si cambian, se añade una nueva que sustituye a la anterior.

## D-001 · Variables políticas excluidas por defecto

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** sustituida por D-004
- **Decisión original:** voto, ideología, simpatía partidista y valoración de líderes no formaban parte de la población.

## D-002 · Universo de salida 18+, con hogares completos

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Contexto:** la composición del hogar (hijos menores, mayores a cargo) es un atributo clave de cada adulto.
- **Decisión:** se generan hogares completos, incluidos los menores; las consultas y predicciones se hacen sobre personas de 18 años o más.

## D-003 · Fecha de corte de construcción para las capas de opinión y política

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** propuesta
- **Contexto:** los modelos de lenguaje pueden conocer resultados publicados antes de su fecha de corte de conocimiento.
- **Decisión:** solo se usan para construir y ajustar estudios con trabajo de campo anterior al 30/06/2026; los posteriores van a `data/eval/`. La fecha se ajusta en F8A a la fecha de corte de los modelos declarados en `configs/llm.yaml`.

## D-004 · Inclusión de la dimensión política

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Contexto:** las variables políticas (comportamiento electoral pasado, ideología, identidad territorial, implicación, confianza institucional) describen a la persona y ayudan a anticipar sus opiniones, porque muchas actitudes se organizan alrededor de ellas.
- **Alternativas consideradas:**
  1. Excluirlas (D-001): población más simple, pero se pierde uno de los predictores más fuertes de opinión.
  2. Incluirlas solo como rasgos latentes sin partidos: se pierde el anclaje con resultados electorales reales.
  3. Incluirlas completas, calibradas con resultados oficiales.
- **Decisión:** opción 3. Las variables políticas forman una capa propia (P3-POL, fase F8B), con el recuerdo de voto calibrado a resultados electorales oficiales.
- **Consecuencias:** nuevas fuentes (resultados electorales, censo electoral, estudios electorales del CIS), armonización de partidos (`configs/partidos.yaml`) y validaciones específicas (V-POL-*).

## D-005 · Separación de capas y variables volátiles

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Decisión:**
  1. La población sociodemográfica (F4–F7) se valida y aprueba **sin** variables de opinión ni políticas, para que su calidad no dependa de ellas.
  2. Las capas de opinión y política se guardan en ficheros aparte (`opinion.parquet`, `politics.parquet`) y se unen a las personas por `person_id`.
  3. La intención de voto y la valoración de líderes no son atributos de la persona: se predicen como preguntas.

## D-006 · Dimensión temporal por pseudopanel

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Contexto:** no existen datos de panel que sigan a las mismas personas en el tiempo.
- **Decisión:** la evolución de opiniones se modela por tipo de persona (cohorte, perfil, territorio, recuerdo de voto) a partir de barómetros sucesivos apilados con su fecha. Las trayectorias individuales de las personas sintéticas se marcan como `modelada`.

## D-007 · Uso no comercial

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Decisión:** el proyecto es de uso no comercial. Las fuentes se usan según sus condiciones para ese fin (`docs/08_uso_y_licencias.md`).

## D-008 · Herramientas del proyecto (F0)

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Contexto:** F0 pide configurar entorno, linter, formateador y pytest.
- **Alternativas consideradas:**
  1. Stack recomendado en `docs/03` (Python 3.11+, Polars/PyArrow, pydantic, Typer, pytest, hypothesis).
  2. pandas como librería principal.
- **Evidencia:** `docs/03_arquitectura.md`, sección 6.
- **Decisión:** opción 1. Ruff como linter y formateador (línea de 100). Paquete instalable `sinpop` con `src/`. Cada configuración tiene un esquema pydantic estricto (`extra="forbid"`) en `src/sinpop/config/schemas.py`.
- **Consecuencias:** ninguna sobre los datos.
- **Aprobada por:** agente (no requiere aprobación)

## D-009 · Quién escribe en los datos de evaluación (contradicción documental)

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** propuesta
- **Contexto:** la regla 5 de `CLAUDE.md` prohíbe que cualquier módulo fuera de `src/sinpop/evaluate/` lea los datos de evaluación, pero la tarea 6 de F8A pide «guardar en `data/eval/` los estudios posteriores a la fecha de corte», lo que haría el módulo de opinión.
- **Alternativas consideradas:**
  1. Permitir escrituras desde otros módulos y prohibir solo lecturas (difícil de comprobar de forma estática y fiable).
  2. Toda escritura o lectura de esos datos pasa por funciones de `sinpop.evaluate`; la ingesta y la opinión le entregan los ficheros y nunca conocen la ruta.
- **Evidencia:** `tests/test_no_leakage.py` detecta tanto rutas como importaciones de `sinpop.evaluate` fuera de ese paquete.
- **Decisión:** opción 2. La única definición de la ruta está en `src/sinpop/evaluate/__init__.py`. El reparto de estudios por fecha se hará con un comando de `sinpop.evaluate` (por ejemplo `sinpop evaluate --split`) que se diseñará en F8A.
- **Consecuencias:** ningún otro módulo puede importar `sinpop.evaluate`.
- **Aprobada por:** pendiente de humano

## D-010 · Alcance de la comprobación por hash (V-REPRO)

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** propuesta
- **Contexto:** RNF-01 exige ficheros idénticos con la misma configuración y semilla, pero `metadata.json` incluye la fecha de ejecución y la versión del código, que cambian entre ejecuciones.
- **Decisión:** V-REPRO compara el SHA-256 de los ficheros de datos (`persons.parquet`, `households.parquet`, `lineage.parquet`, capas). `metadata.json` guarda esos hashes y queda fuera de la comparación.
- **Consecuencias:** el test de integración de F4 compara solo los ficheros de datos.
- **Aprobada por:** pendiente de humano

## D-011 · Interpretación de la puerta G3.4

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** propuesta
- **Contexto:** G3.4 dice «ninguna variable reservada aparece en la lista de calibración», pero la propuesta de `targets.yaml` reserva cruces (por ejemplo `estudios_3 × sexo × edad_4`) cuyas variables sueltas sí se calibran en otros cruces (`estudios_3 × edad_4`). Leída al pie de la letra, la propuesta de la propia documentación incumpliría la puerta.
- **Decisión:** la comprobación se hace por **objetivo** (cruce exacto de variables): ningún cruce reservado puede estar en la lista de calibración. Lo valida el esquema de `targets.yaml` y un test.
- **Aprobada por:** pendiente de humano

## D-012 · Códigos territoriales y dominios de partida

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** propuesta
- **Contexto:** `territories.yaml` y `variables.yaml` necesitan dominios para ser válidos en F0.
- **Decisión:** se cargan los códigos INE de las 19 comunidades y ciudades autónomas y de las 52 provincias, y las categorías propuestas en `docs/02`. Las variables cuyo dominio depende de la fuente (`nacionalidad_top`, `nivel_estudios`, `anio_llegada_espana`, recuerdos de voto, escalas del CIS) quedan con `dominio_pendiente`, sin inventar categorías. Todo se verifica en F1/F2 contra la documentación oficial (regla 2).
- **Dudas abiertas:** el tramo superior de `edad_5` (85+ frente a tramos hasta 100+ del Padrón); la variable de privación material severa de la lista de vigilancia no existe aún en el diccionario (el indicador oficial de la ECV se fija en F2); `recuerdo_voto_generales_familia`, usada en `docs/03` como subgrupo, será una variable derivada de la capa política.
- **Aprobada por:** pendiente de humano (en la revisión de F1)

## D-013 · Umbrales completados en `thresholds.yaml`

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Contexto:** el extracto de `docs/07` no incluye todos los umbrales de `docs/05`.
- **Decisión:** se completan copiando literalmente `docs/05` (V-DATOS, V-SEMILLAS, V-COHERENCIA, V-ENRIQ-*, V-MINORIAS-PERFIL, V-RAREZA, V-LATENTE, V-DIVERSIDAD-RASGOS, V-POL-SESGO, V-REFORMULACION, V-EVENTO, V-CONF-*, V-REGRESION). V-EVENTO «2 de cada 3» se guarda como 0,6667. Un test comprueba los valores principales contra la documentación. No se ha cambiado ningún umbral.
- **Aprobada por:** agente (transcripción, sin cambio de umbral)

## D-014 · Fuentes oficiales inaccesibles desde el entorno de ejecución

- **Fecha:** 2026-10-14
- **Fase:** F1
- **Estado:** pendiente de decisión humana
- **Contexto:** la política de red del entorno en la nube deniega (HTTP 403 en el proxy) `www.ine.es`, `servicios.ine.es`, `www.cis.es`, `infoelectoral.interior.gob.es` y `www.europeansocialsurvey.org`. Sin ellas no se puede descargar ninguna fuente P0.
- **Alternativas consideradas:**
  1. Buscar copias en otros sitios: **prohibido** por `CLAUDE.md` («no busques copias en sitios no oficiales»).
  2. Que la persona responsable añada esos dominios a la red permitida del entorno.
  3. Que la persona responsable descargue los ficheros y los coloque en `data/raw/<fuente>/<edicion>/` (lista en `data/raw/MANUAL_DOWNLOADS.md`).
- **Decisión:** se registran todas las fuentes en `MANUAL_DOWNLOADS.md` y se deja la ingesta preparada para registrar y verificar (SHA-256) cualquier fichero que llegue por la vía 2 o la 3. F1 no puede cerrarse hasta entonces.
- **Aprobada por:** pendiente de humano
