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
- **Estado:** aprobada (humano, 2026-10-14)
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
- **Estado:** aprobada
- **Contexto:** la regla 5 de `CLAUDE.md` prohíbe que cualquier módulo fuera de `src/sinpop/evaluate/` lea los datos de evaluación, pero la tarea 6 de F8A pide «guardar en `data/eval/` los estudios posteriores a la fecha de corte», lo que haría el módulo de opinión.
- **Alternativas consideradas:**
  1. Permitir escrituras desde otros módulos y prohibir solo lecturas (difícil de comprobar de forma estática y fiable).
  2. Toda escritura o lectura de esos datos pasa por funciones de `sinpop.evaluate`; la ingesta y la opinión le entregan los ficheros y nunca conocen la ruta.
- **Evidencia:** `tests/test_no_leakage.py` detecta tanto rutas como importaciones de `sinpop.evaluate` fuera de ese paquete.
- **Decisión:** opción 2. La única definición de la ruta está en `src/sinpop/evaluate/__init__.py`. El reparto de estudios por fecha se hará con un comando de `sinpop.evaluate` (por ejemplo `sinpop evaluate --split`) que se diseñará en F8A.
- **Consecuencias:** ningún otro módulo puede importar `sinpop.evaluate`.
- **Aprobada por:** humano (2026-10-14)

## D-010 · Alcance de la comprobación por hash (V-REPRO)

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Contexto:** RNF-01 exige ficheros idénticos con la misma configuración y semilla, pero `metadata.json` incluye la fecha de ejecución y la versión del código, que cambian entre ejecuciones.
- **Decisión:** V-REPRO compara el SHA-256 de los ficheros de datos (`persons.parquet`, `households.parquet`, `lineage.parquet`, capas). `metadata.json` guarda esos hashes y queda fuera de la comparación.
- **Consecuencias:** el test de integración de F4 compara solo los ficheros de datos.
- **Aprobada por:** humano (2026-10-14)

## D-011 · Interpretación de la puerta G3.4

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Contexto:** G3.4 dice «ninguna variable reservada aparece en la lista de calibración», pero la propuesta de `targets.yaml` reserva cruces (por ejemplo `estudios_3 × sexo × edad_4`) cuyas variables sueltas sí se calibran en otros cruces (`estudios_3 × edad_4`). Leída al pie de la letra, la propuesta de la propia documentación incumpliría la puerta.
- **Decisión:** la comprobación se hace por **objetivo** (cruce exacto de variables): ningún cruce reservado puede estar en la lista de calibración. Lo valida el esquema de `targets.yaml` y un test.
- **Aprobada por:** humano (2026-10-14)

## D-012 · Códigos territoriales y dominios de partida

- **Fecha:** 2026-10-14
- **Fase:** F0
- **Estado:** aprobada
- **Contexto:** `territories.yaml` y `variables.yaml` necesitan dominios para ser válidos en F0.
- **Decisión:** se cargan los códigos INE de las 19 comunidades y ciudades autónomas y de las 52 provincias, y las categorías propuestas en `docs/02`. Las variables cuyo dominio depende de la fuente (`nacionalidad_top`, `nivel_estudios`, `anio_llegada_espana`, recuerdos de voto, escalas del CIS) quedan con `dominio_pendiente`, sin inventar categorías. Todo se verifica en F1/F2 contra la documentación oficial (regla 2).
- **Dudas abiertas:** el tramo superior de `edad_5` (85+ frente a tramos hasta 100+ del Padrón); la variable de privación material severa de la lista de vigilancia no existe aún en el diccionario (el indicador oficial de la ECV se fija en F2); `recuerdo_voto_generales_familia`, usada en `docs/03` como subgrupo, será una variable derivada de la capa política.
- **Aprobada por:** humano (2026-10-14)

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
- **Estado:** aprobada
- **Contexto:** la política de red del entorno en la nube deniega (HTTP 403 en el proxy) `www.ine.es`, `servicios.ine.es`, `www.cis.es`, `infoelectoral.interior.gob.es`, `www.europeansocialsurvey.org`, `ess.sikt.no`, `www.sanidad.gob.es`, `ec.europa.eu`, `ceo.gencat.cat` y `www.ehu.eus`. Sin ellas no se puede descargar ninguna fuente P0.
- **Alternativas consideradas:**
  1. Buscar copias en otros sitios: **prohibido** por `CLAUDE.md` («no busques copias en sitios no oficiales»).
  2. Que la persona responsable añada esos dominios a la red permitida del entorno.
  3. Que la persona responsable descargue los ficheros y los coloque en `data/raw/<fuente>/<edicion>/` (lista en `data/raw/MANUAL_DOWNLOADS.md`).
- **Decisión:** se registran todas las fuentes en `MANUAL_DOWNLOADS.md` y se deja la ingesta preparada para registrar y verificar (SHA-256) cualquier fichero que llegue por la vía 2 o la 3. F1 no puede cerrarse hasta entonces.
- **Aprobada por:** humano (2026-10-14)

## D-015 · Fuentes de referencia y fecha de referencia de la población

- **Fecha:** 2026-10-14
- **Fase:** F1
- **Estado:** aprobada
- **Contexto:** `docs/02` propone el Padrón continuo como verdad de referencia y el último 1 de enero publicado como fecha. El INE publica hoy como cifras oficiales la Estadística Continua de Población (ECP, trimestral, provisional hasta 01/07/2026) y el Censo Anual de Población (definitivo hasta 01/01/2025, con un fichero exhaustivo de microdatos demográficos). Los bloques de estudios, actividad y estado civil del Censo Anual llegan a 2024 y la ocupación a 2023.
- **Alternativas consideradas:**
  1. Fecha 01/01/2025 con el Censo Anual exhaustivo para todo: coherente, pero un año más antigua.
  2. Fecha 01/01/2026 con la ECP para los totales y el Censo Anual para la estructura que la ECP no publica.
  3. Seguir con las tablas del Padrón continuo: el INE las ha integrado en la ECP y el Censo Anual.
- **Evidencia:** `reports/fase_01_inventario.md`; tablas ECP 59589, 59591, 60124–60135 a 01/01/2026; Censo Anual exhaustivo 2025 con 49.128.297 registros (= población oficial).
- **Decisión (propuesta):** opción 2. Fecha de referencia **01/01/2026**.
  - ECP 01/01/2026: población en viviendas familiares por provincia × sexo × grupo de edad × nacionalidad (española/extranjera) (tabla 60129) y hogares por tamaño (1, 2, 3, 4+) por provincia (tabla 60133).
  - Censo Anual 2025 exhaustivo: grupos de nacionalidad y país de nacimiento, nacionalidades principales, grado de urbanización y tamaño de municipio (desfase de 1 año, documentado por variable).
  - Muestra del Censo Anual 2024: estudios, relación con la actividad y estado civil (desfase de 2 años); 2023: ocupación y situación profesional (3 años).
  - Censo 2021: donantes y tipo de hogar (5 años de desfase en el tipo de hogar; se calibra el tamaño con la ECP 2026).
  - El grado de urbanización se toma de los microdatos censales (como pide `docs/02`), no de un fichero aparte. `padron_continuo`, `censo2021_tablas` y `degurba` pasan a P1 en `sources.yaml`; se añade `ecp` como P0.
- **Consecuencias:** `targets.yaml` (F3) usará estas fuentes; la ficha de datos documenta el desfase de cada variable.
- **Aprobada por:** humano (2026-10-15)

## D-016 · Hallazgos en los ficheros oficiales

- **Fecha:** 2026-10-14
- **Fase:** F1
- **Estado:** aprobada
- **Contexto e evidencia:**
  1. Las muestras del Censo 2021 y del Censo Anual **no traen variable de peso**. El INE las describe como el 10 % de los hogares (2021) y el 10 % de la población (Censo Anual). Las muestras 2024 y 2025 tienen exactamente población/10 registros; se usa un factor uniforme de 10 y en F2 se contrasta por provincia.
  2. En el ZIP de la muestra 2024 del Censo Anual, el Parquet y el JSON del diseño están **desfasados** (sin DEGURBA ni residencia hace un año, y con actividad y estudios vacíos), mientras el TXT y el Excel siguen el diseño actualizado de 80 posiciones. Se usa el TXT con el Excel.
  3. La muestra 2023 tiene 4.807.670 registros frente a 4.808.536 (= población oficial 2023 / 10): 866 menos (−0,018 %). Probablemente se extrajo antes de la revisión de la cifra oficial. Solo se usa para la ocupación.
  4. Los códigos difieren entre fuentes: sexo 1/6 (no 1/2); relación con la actividad 1,2,4,5,6,7 en el Censo 2021 y 01–06 en el Censo Anual; `ECIVIL` = 0 «No consta» (4 % en 2024). Todo se recodifica en F2 desde los diccionarios oficiales, nunca por suposición.
- **Decisión (propuesta):** factor uniforme 10 para las muestras censales; TXT + Excel para el Censo Anual; aceptar la muestra 2023 con la discrepancia documentada (G1.4 no se cumple al pie de la letra para ese fichero).
- **Aprobada por:** humano (2026-10-15)

## D-017 · Universo de la población base: viviendas familiares

- **Fecha:** 2026-10-14
- **Fase:** F1
- **Estado:** sustituida por D-021
- **Contexto:** la muestra de hogares del Censo 2021 no incluye establecimientos colectivos. Según la ECP a 01/01/2026, 386.003 residentes (0,78 %) viven en ellos, sobre todo personas mayores.
- **Alternativas consideradas:**
  1. Módulo aparte con personas de colectivos modeladas a partir de tablas por edad y sexo (sin donantes reales: atributos modelados).
  2. Declarar la limitación y calibrar la población base a la población en viviendas familiares de la ECP.
- **Decisión (propuesta):** opción 2 ahora, con la limitación cuantificada por edad en la ficha de datos; la opción 1 queda como mejora posterior si se pide.
- **Aprobada por:** pendiente de humano (revisión G1.6)

## D-018 · Ajustes del diccionario a lo que contienen las fuentes

- **Fecha:** 2026-10-14
- **Fase:** F1
- **Estado:** aprobada
- **Contexto:** varias categorías de `docs/02` no existen en los donantes del Censo 2021.
- **Decisión (propuesta):**
  1. `relacion_actividad`: el Censo no separa «labores del hogar» (va en otra inactividad). Categorías: ocupado, parado, jubilado_pensionista, incapacidad_permanente (pensionista de invalidez), estudiante, otra_inactividad.
  2. `situacion_profesional`: el Censo distingue cuenta propia con/sin asalariados y ajena indefinida/temporal, pero no sector público/privado. Categorías: empresario, autonomo, asalariado_indefinido, asalariado_temporal, otra; el sector público/privado se añade en F6 desde la EPA como variable P2 `sector_publico`.
  3. `tenencia_vivienda`: el Censo solo da propiedad/alquiler/otro; la distinción con/sin hipoteca y el tipo de alquiler se añaden en F6 desde la ECV, condicionadas al régimen censal.
  4. `relacion_persona_ref`: el Censo 2021 no define persona de referencia. Se deriva con una regla fija: miembro de mayor edad entre los cónyuges o progenitores del primer núcleo; si no hay núcleo, la persona adulta de mayor edad. Las relaciones se derivan de los punteros de cónyuge, progenitores y familia.
  5. `nacionalidad_grupo`: la doble nacionalidad no se identifica en ninguna fuente; se elimina la categoría `espanola_doble`.
  6. `tamano_municipio`: para municipios de 10.000 habitantes o más se asigna con la población municipal del Censo Anual exhaustivo; para los menores, con los códigos 991–993.
- **Aprobada por:** humano (2026-10-15)

## D-019 · Fuentes de las capas de opinión y política: descarga manual y verificaciones aplazadas

- **Fecha:** 2026-10-14
- **Fase:** F1
- **Estado:** sustituida por D-021 y D-022
- **Contexto:** Infoelectoral corta la conexión desde el entorno; el CIS sirve sus microdatos bajo petición y limita las peticiones automáticas; la ESS exige registro. Ninguna de estas fuentes interviene en el núcleo (F2–F7).
- **Decisión (propuesta):** registrar estas fuentes en `MANUAL_DOWNLOADS.md` y aplazar las verificaciones críticas 6 y 7 al inicio de F8A/F8B, donde se reabre la parte correspondiente de F1. La puerta G1.5 queda con 5/7 hasta entonces.
- **Aprobada por:** pendiente de humano (revisión G1.6)

## D-020 · Revisión humana parcial de F1 (2026-10-14)

- **Fecha:** 2026-10-14
- **Fase:** F1
- **Estado:** aprobada
- **Decisión del responsable:**
  1. **G1.4 aceptada:** se acepta la muestra 2023 del Censo Anual con su diferencia de −866 registros (−0,018 %) y el contraste por cociente del Censo 2021, cuya documentación no declara una cifra exacta (D-016, puntos 1 y 3).
  2. Se siguen las revisiones humanas tal y como las fija la documentación (no se agrupan).
  3. D-017 (universo) y D-018.4 (persona de referencia) quedan pendientes de aclaración; D-019 (aplazar G1.5 a F8) no se aprueba por ahora.
- **Aprobada por:** humano

## D-021 · Decisiones del responsable sobre colectivos, persona de referencia y fuentes políticas (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F1
- **Estado:** aprobada
- **Decisión del responsable:**
  1. **Establecimientos colectivos (sustituye a D-017): opción B.** La población incluye a los residentes en establecimientos colectivos (386.003 personas a 01/01/2026; el 5,2 % de los de 90 años o más). Se generan en un módulo aparte con las cifras oficiales por provincia, sexo y edad (ECP: población total menos población en viviendas familiares). Sus demás atributos se modelan a partir de personas parecidas y se marcan como `modelada` en `__calidad`; la ficha de datos advierte de su menor fiabilidad. Se implementa en F4/F5 y se audita en F7.
  2. **Persona de referencia (concreta D-018.4): la persona de más edad del hogar.** En caso de empate, la de menor número de orden (`NORDEN`) en el fichero del Censo. Las relaciones (pareja, hijo, padre o madre, otro familiar, no familiar) se derivan de los punteros de cónyuge, progenitores y familia respecto a esa persona.
  3. **G1.5:** no se aplazan las verificaciones 6 y 7 a F8: se completan en F1 con los ficheros aportados y con nuevos intentos en el CIS.
- **Evidencia nueva:**
  - El responsable aporta 52 PDF con los resultados municipales del Congreso del 23/07/2023 publicados por el Ministerio del Interior. Son las hojas del **escrutinio provisional** (sello horario de la noche electoral, 23–24/07/2023). Se han leído los 8.131 municipios sin ningún descuadre interno: válidos = candidatura + blancos; participación = válidos + nulos; suma de candidaturas = votos a candidatura. Censo de residentes: 35.146.062; participación: 24.743.612. No incluyen el voto CERA, que es justo el universo que pide `docs/02` (§3.5, regla 2). Tres ficheros venían con el nombre cambiado (`34.pdf` = Málaga, `48.pdf` = Toledo, `Málaga.pdf` = Melilla); se identifican por su contenido y se guardan con el código INE de provincia.
  - El CIS publica en abierto (CC BY 4.0) los microdatos, cuestionarios y fichas técnicas en la página de cada estudio. Se descargan respetando pausas de 20 s (el buscador del catálogo tiene protección contra robots; las páginas de estudio no).
- **Consecuencias:** las cifras provisionales pueden diferir ligeramente del escrutinio definitivo. G2.6 («totales oficiales sin diferencias») se contrastará contra estos PDF y la diferencia con el definitivo se documentará si se obtiene.
- **Aprobada por:** humano

## D-022 · Elecciones europeas y estudio postelectoral fuera de las fuentes (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F1
- **Estado:** aprobada
- **Contexto:** `docs/02` y `docs/04` (F3, tarea 5) proponen las europeas de 2024 como elección reservada para validar la capa política (V-POL-RESERVADA), y la verificación 6 incluye los estudios postelectorales del CIS.
- **Decisión del responsable:**
  1. **Europeas de 2024 fuera:** no son buen identificador del comportamiento político (participación muy baja y voto a candidaturas que no se presentan a las generales). No se usan ni para construir ni para validar.
  2. **Postelectoral del CIS no necesario:** se usan el preelectoral 3411 y los barómetros posteriores al 23J, que recogen el recuerdo de voto de 2023 (la documentación los admite: `docs/03`, §2.5).
- **Consecuencias:** V-POL-RESERVADA necesita otra validación reservada. Propuesta del agente, para decidir en F3: reservar el detalle municipal de las generales de 2023 (calibrar el recuerdo de voto por provincia y validar contra los municipios, que no se usan para calibrar). `elecciones.yaml` registra esta alternativa en `validacion_reservada`.
- **Aprobada por:** humano (puntos 1 y 2); la alternativa de validación queda propuesta.

## D-023 · Resultados de las últimas elecciones autonómicas (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F1
- **Estado:** aprobada (fuentes aportadas por el responsable)
- **Contexto:** la verificación 6 de F1 pide las últimas autonómicas de cada comunidad, para `recuerdo_voto_autonomicas` (voto dual).
- **Evidencia:** el responsable aporta 18 PDF de boletines oficiales y juntas electorales; las asambleas de Ceuta y Melilla se toman del BOE de resultados de las elecciones locales de 2023, que contiene también otras provincias que no se usan. La fecha de Aragón (08/02/2026) no figura en su PDF y se ha confirmado en el portal oficial del Gobierno de Aragón; los escaños del PDF coinciden con los de ese portal.

  | Comunidad | Fecha | Publicación | Nivel | Voto CERA | Notas |
  | --- | --- | --- | --- | --- | --- |
  | Andalucía | 2026-05-17 | BOJA nº 108, 08/06/2026 (Junta Electoral de Andalucía) | provincia | sí | — |
  | Aragón | 2026-02-08 | Informe de resultados definitivos del Gobierno de Aragón | provincia, comarca y municipio | por verificar | la fecha no figura en el PDF: confirmada en el portal oficial |
  | Asturias, Principado de | 2023-05-28 | BOPA nº 119, 22/06/2023 (Junta Electoral Provincial de Asturias) | circunscripción (Central, Occidental, Oriental) | sí | texto no extraíble: requiere OCR (tesseract, spa) |
  | Balears, Illes | 2023-05-28 | BOIB nº 83, 2023 (Junta Electoral de las Illes Balears) | circunscripción insular | solo CERA | SOLO contiene el voto de los residentes en el extranjero: faltan los resultados generales |
  | Canarias | 2023-05-28 | BOC nº 121, 22/06/2023 (Junta Electoral de Canarias) | circunscripción insular y autonómica | sí | — |
  | Cantabria | 2023-05-28 | BOC extraordinario nº 46, 07/06/2023 (Junta Electoral Provincial de Cantabria) | comunidad (circunscripción única) | sí | — |
  | Castilla y León | 2026-03-15 | BOCyL nº 80, 29/04/2026 (Junta Electoral de Castilla y León) | provincia | sí | — |
  | Castilla-La Mancha | 2023-05-28 | DOCM nº 114, 16/06/2023 (Junta Electoral de Castilla-La Mancha) | provincia | sí | — |
  | Cataluña | 2024-05-12 | DOGC nº 9178, 06/06/2024 (Junta Electoral Central) | provincia | sí | — |
  | Comunitat Valenciana | 2023-05-28 | DOGV nº 9618, 15/06/2023 (Junta Electoral de la Comunitat Valenciana) | provincia | por verificar | — |
  | Extremadura | 2025-12-21 | DOE nº 8, 14/01/2026 (Junta Electoral de Extremadura) | provincia | por verificar | — |
  | Galicia | 2024-02-18 | DOG nº 47, 06/03/2024 (Junta Electoral de Galicia) | provincia | por verificar | — |
  | Madrid, Comunidad de | 2023-05-28 | BOCM nº 136, 09/06/2023 (Junta Electoral Provincial de Madrid) | comunidad (circunscripción única) | por verificar | — |
  | Murcia, Región de | 2023-05-28 | BORM nº 135, 14/06/2023 (Junta Electoral Provincial de Murcia) | comunidad (circunscripción única) | sí | primera página con texto desordenado; el resto se lee |
  | Navarra, Comunidad Foral de | 2023-05-28 | BON nº 147, 14/07/2023 (Resolución 73/2023) | comunidad (circunscripción única) | por verificar | — |
  | País Vasco | 2024-04-21 | BOPV nº 90, 09/05/2024 (Junta Electoral de la CA del País Vasco) | territorio histórico | por verificar | — |
  | Rioja, La | 2023-05-28 | BOR nº 125, 20/06/2023 (Junta Electoral de La Rioja) | comunidad (circunscripción única) | por verificar | — |
  | Ceuta | 2023-05-28 | BOE nº 261, 01/11/2023 (Junta Electoral Central, elecciones locales) | ciudad autónoma | — | Asamblea de Ceuta: elegida en las elecciones locales; el PDF incluye otras provincias que no se usan |
  | Melilla | 2023-05-28 | BOE nº 261, 01/11/2023 (Junta Electoral Central, elecciones locales) | ciudad autónoma | — | Asamblea de Melilla: elegida en las elecciones locales; mismo PDF que Ceuta |

- **Decisión:** se usan como verdad de referencia del recuerdo de voto autonómico, a nivel de circunscripción (provincia, isla o territorio histórico), salvo Aragón, que llega a municipio. Son resultados **definitivos** (actas de las juntas electorales), a diferencia de los de las generales (escrutinio provisional). El voto CERA se descuenta cuando el boletín lo da por separado (`docs/02`, §3.5, regla 2); donde no, se documenta.
- **Huecos:**
  1. **Illes Balears:** el PDF solo contiene el voto CERA; faltan los resultados generales.
  2. **Asturias:** el texto del PDF no es extraíble; se lee por OCR y se valida con la suma de candidaturas igual a votos a candidaturas.
- **Aprobada por:** humano (aporte de las fuentes); el tratamiento de los huecos queda pendiente.

## D-024 · Aprobación de F1 (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F1
- **Estado:** aprobada
- **Decisión:** el responsable aprueba el inventario, la matriz de cobertura, las verificaciones críticas y las decisiones D-015 a D-023 (puerta G1.6). Se inicia F2. Queda abierto el hueco de las autonómicas de Illes Balears (solo voto CERA), que no bloquea.
- **Aprobada por:** humano
