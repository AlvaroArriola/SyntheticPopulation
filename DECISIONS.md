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

## D-025 · Recodificaciones del Censo 2021 y del Censo Anual (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Contexto:** `docs/02` fija las variables P0–P2 y sus categorías, pero algunas tablas de correspondencia dependen de los diccionarios oficiales. Todas las tablas están en `configs/variables.yaml` (generadas por `tools/generar_recodificaciones_censos.py` y `tools/generar_recodificaciones_encuestas.py`), cada una con `verificado_contra` el diseño de registro del INE.
- **Decisiones:**
  1. **Grupos de país** (`nacionalidad_grupo`, `pais_nacimiento_grupo`): UE-27 por nombre del país en los diccionarios del INE (incluido «Otros países de la Unión Europea»); Canadá y EE. UU. van a «otros» porque `docs/02` no prevé un grupo norteamericano; los códigos agregados 5xx, 555 y 966 («otros países» o «apátridas») van a «otros»; el 999 («no consta») no aparece en los ficheros usados.
  2. **Quince nacionalidades principales** (`nacionalidad_top`): las 15 nacionalidades extranjeras con más residentes en el Censo Anual exhaustivo de 2025 (Marruecos, Colombia, Rumanía, Venezuela, Italia, Reino Unido, Perú, China, Ucrania, Honduras, Argentina, Ecuador, Alemania, Francia, Paraguay); el resto, «otras_extranjeras».
  3. **Tipo de hogar** (Censo 2021): clave `TIPO_HOG|TIPO_NUC` del núcleo principal. Unipersonal = 01; pareja sin hijos = 04|1; pareja con hijos = 04|2; monoparental = 04|3 y 04|4; dos o más familias o personas no emparentadas = 02, 07 y 08; el resto (03, 05, 06), «otros».
  4. **Tamaño de municipio:** por la población del Padrón a 01/01/2025 (tabla 29005), no por el tramo que trae cada fichero. Tres municipios (18102, 31258, 36023) tenían más de 10.000 habitantes en 2021 y menos en 2025: se clasifican con la cifra de 2025, coherente con la fecha de referencia (D-015). Los códigos 991–993 (municipios de menos de 10.000 sin identificar) se traducen a sus tramos.
  5. **Edad en grupos de 5 años:** el último grupo de `docs/02` («85+») se parte en «85-89» y «90+» para poder sobrerrepresentar a los muy mayores (`docs/06`); la ECP publica ambos grupos.
  6. **Persona de referencia** (D-021): la de más edad del hogar; a igual edad, el menor NORDEN. Los parentescos se reconstruyen desde NORDEN_CON, NORDEN_PAD, NORDEN_MAD y FAMILIA: pareja, hijo (de la persona de referencia o de su pareja), padre o madre, otro familiar (misma familia) o no familiar.
  7. **Nueva variable `tenencia_censo`:** régimen de tenencia del Censo 2021 (propiedad, alquiler, otro), más pobre que la `tenencia_vivienda` de la ECV; se guarda para el enlace en F6.
  8. **Universos:** relación con la actividad y estudios, NP para menores de 15 (el INE los deja en blanco); estado civil, NP para menores de 16 (el Censo 2021 codifica «soltero» también a los niños); ocupación, sector y situación profesional, NP para quien no está ocupado.
- **Evidencia:** `tests/unit/test_recodificaciones.py` (un test por tabla: destinos dentro del dominio, todos los códigos traducidos y un código inventado detiene el proceso); `reports/fase_02_cifras_oficiales.md`.
- **Aprobada por:** humano (2026-10-15)

## D-026 · Ocupados con ocupación, actividad o situación profesional en blanco (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada con cambio del responsable
- **Contexto:** en la muestra del Censo Anual 2023 hay 4 personas ocupadas con CNO, CNAE y SITU en blanco. El diseño de registro no documenta el blanco para ocupados.
- **Decisión:** se codifican como «NC» (no consta) y no como NP, porque están dentro del universo de la pregunta. No se imputan. La regla se aplica igual al Censo 2021 (`nc_si` en `censos._personales`).
- **Alternativas:** detener la armonización (regla 2 de CLAUDE.md); descartado porque el blanco dentro del universo es, por definición, un dato que no consta y su peso es despreciable (4 de 4,8 millones de registros).
- **Decisión final del responsable:** se **descartan** los 4 registros por su peso despreciable (no se codifican como NC). Implementado en `censos.descartados_d026`, que solo actúa en ficheros que publican la ocupación (muestra 2023); se retira la regla `nc_si`, de modo que un blanco nuevo vuelve a detener la armonización. G2.3 descuenta los descartados (48.076.700 → 48.076.660).
- **Aprobada por:** humano (2026-10-15)

## D-027 · Tolerancias para reproducir cifras oficiales (G2.4) (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Contexto:** G2.4 pide reproducir 3 cifras oficiales por fuente P0 y P1 «dentro de la tolerancia de redondeo de la publicación». Para muestras, la diferencia esperada no es el redondeo sino el error de muestreo.
- **Decisión propuesta:**
  1. Ficheros exhaustivos y tablas: igualdad exacta.
  2. Muestras con factor de elevación conocido (Censo 2021, muestras del Censo Anual): |p̂ − p| ≤ 3 · EE, con EE de una proporción en muestreo aleatorio simple con fracción f = 0,10.
  3. Encuestas con tasas publicadas redondeadas: redondeo de la publicación + 3 · EE.
  4. **Muestra del Censo 2021 (solo viviendas familiares) frente a tablas que incluyen colectivos:** se suma a la tolerancia la cota del sesgo de cobertura, c = proporción del universo que vive en colectivos (|p_fam − p_total| = c · |p_fam − p_col| ≤ c; c ≈ 0,8 %). Con 3 · EE sin esa cota, 11 de 21 cifras quedan fuera (diferencia máxima 0,24 puntos, en ocupados y casados, justo donde más difieren las residencias de mayores); con la cota, las 21 entran. El INE no publica tablas del Censo 2021 limitadas a viviendas familiares en su API (comprobado en las operaciones 8 y 463).
- **Resultado:** 111 cifras de 14 fuentes P0/P1, todas dentro de tolerancia (`reports/fase_02_cifras_oficiales.md`).
- **Aprobada por:** humano (2026-10-15)

## D-028 · Armonización de las encuestas (ECV, EPA, TIC-H, ESdE) (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Decisiones:**
  1. **ECV 2025:** se unen los ficheros R, P, H y D. RB082 = −1 (nacidos en 2025) → edad 0; RB082 tiene tope en 86 años según el diseño. Universo de las preguntas personales: quien no está en el fichero P (menores de 16) → NP; marca `_F = −1` o PL032 = 7 (sin cuestionario) → NC. Variables del hogar: `_F = −2` → NP, `_F = −1` → NC. `vrMATSOCDEP` trae 958 blancos no documentados: NC. Renta equivalente = vhRentaa / HX240; deciles ponderados con RB050 (nacionales y por comunidad).
  2. **EPA 2T2026:** `edad_4` vacía para el grupo de 16 a 19 años, porque la EPA no permite separar a los de 18 y 19; la EPA no distingue tipos de inactividad (se usa `relacion_actividad_3`) ni indefinido/temporal en SITU (categoría «asalariado»).
  3. **TIC-H 2025:** uso de internet = ULT_INT|FREC_INT; teletrabajo = ULT_TTRAB|TTRAB_ACTUAL, con TELETRAB = 6 («el trabajo exige presencia») → «nunca» y no ocupados → NP. Las competencias digitales no se armonizan en F2 (indicador compuesto: se decide en F6).
  4. **ESdE 2023:** NIVEST 01 («no procede, es menor de 10 años»; no puede darse en el fichero de adultos) → NP; 99 → NC.
  5. **Nuevas variables llave:** `nacionalidad_esp_ext`, `relacion_actividad_3` y `sector_publico`; `compra_online`, `privacion_material` y `vehiculo_hogar` pasan a categóricas sí/no; `situacion_profesional` añade «asalariado» para la EPA.
  6. **Denominadores al reproducir cifras:** la ESdE excluye el «no consta» del denominador y la ECV lo incluye, como hace el INE en cada nota de prensa (comprobado con las cifras publicadas).
- **Aprobada por:** humano (2026-10-15)

## D-029 · Generales 2023: código INE de los municipios (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Contexto:** las hojas del Ministerio del Interior identifican el municipio solo por su nombre de 2023.
- **Decisión:** se asigna el código INE comparando con los nombres del Padrón 2025 (tabla 29005), sin tildes ni signos y con el artículo pospuesto. 8.115 municipios se emparejan de forma única. Los 16 que han cambiado de nombre se fijan en `harmonize/elecciones.py` (`RENOMBRADOS`), comprobando que el censo electoral de 2023 es coherente con la población de 2025 (cociente entre 0,53 y 1,09, dentro del rango de los demás municipios: 0,11–1,88; el más bajo, Castell-Platja d'Aro, es un municipio turístico con muchos residentes extranjeros): Alcocer de Planes → Alcosser; Facheca → Fageca; Vall de Gallinera; Bigues i Riells → Bigues i Riells del Fai; Santa María Rivarredonda → Ribarredonda; Higuera → Higuera de Albalat; Herbés → Herbers; Castell-Platja d'Aro → Castell d'Aro, Platja d'Aro i s'Agaró; Masarac → Masarac i Vilarnadal; La Zarza-Perrunal; Candín → Valle de Ancares; Lumbreras → Lumbreras de Cameros; A Rúa de Valdeorras → Rúa, A; La Bisbal de Falset → Bisbal de Montsant, La; Alfarp → Alfarb; Villanueva de Castellón → Castelló.
- **Consecuencia:** Usansolo (48916) se segregó de Galdakao después de las elecciones: su voto de 2023 está dentro del de Galdakao (48036). Los 6 códigos de la tabla 29005 sin población (municipios fusionados o suprimidos) no tienen resultados.
- **G2.6:** los totales oficiales provinciales del Congreso (BOE-A-2023-18907, Junta Electoral Central) no se pueden descargar: `www.boe.es` no está permitido en la red del entorno y el área de descargas de Interior corta la conexión. Se registra en `data/raw/MANUAL_DOWNLOADS.md`. Mientras, solo se comprueba la coherencia interna de cada municipio (0 descuadres en 8.131).
- **Aprobada por:** humano (2026-10-15): «acepto lo que decidas»; con el BOE accesible se completa en D-032

## D-030 · Familias de partidos y códigos del CIS (`partidos.yaml`) (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Contexto:** `docs/02` (§3.5) pide dos niveles: la candidatura votada y una familia estable. G2.7 exige que cada código de partido de cada estudio del CIS usado tenga correspondencia.
- **Criterios (iguales para todos los electorados):**
  1. Partidos estatales: por su posición, si han tenido representación en el Congreso o en el Parlamento Europeo desde 2015; si no, «otros».
  2. Federaciones, marcas territoriales y coaliciones encabezadas por un partido estatal: la familia de ese partido (PSC, PSdeG, PSE, PSIB, PSN → socialdemócrata; Sumar-ECP, Sumar-Compromís, Més-Sumar, Sumar Aragón, En Comú, Más Madrid, Elkarrekin, Por Andalucía → izquierda estatal; PP+Cs → centro-derecha).
  3. Partidos de una sola comunidad, provincia o municipio sin vínculo con un partido estatal: nacionalistas y regionalistas, con desglose por territorio.
  4. 18 siglas de 2023 cuyo nombre completo no se ha podido verificar (sin acceso al BOE) se clasifican por su ámbito con el criterio 3 o, si se presentan en más de una comunidad, como «otros», y quedan marcadas en `notas`.
- **Correspondencias con el CIS:** el barómetro 3567 recoge el recuerdo de las generales de 2023 (RECUVOTOG, RECUERDO) con 12 partidos más «otro partido»; las candidaturas sin código propio se asocian al 8995 («otro partido»). Las federaciones del PSOE comparten el código 1 y las marcas de Sumar el 21. El preelectoral 3411 se usa solo con su catálogo (su recuerdo es de 2019). En 3411 el código 1501 es Na+ (UPN, PP y Cs) en las variables de 2019 y UPN en las de 2023: se asigna a nacionalistas y regionalistas; 1603 es PP+Cs y 912 es Valents.
- **Especiales del CIS:** 0 NP, 8996 en blanco, 9977 nulo, 9993 mismo partido, 9995 no tenía edad, 9996 sin derecho a voto, 9997 no votó / ninguno / no votaría (según la variable), 9998 NS, 9999 NC. Se modelan como opciones legítimas (regla 10 de CLAUDE.md).
- **Resultado:** 72 candidaturas de 2023 (5 izquierda estatal, 6 socialdemócrata, 1 centro-derecha, 1 derecha radical, 44 nacionalistas y regionalistas, 15 otros); 138 códigos en 3567 y 113 en 3411, 0 sin asignar.
- **Aprobada por:** humano (2026-10-15)

## D-031 · Lectura de las autonómicas: descuadres de las publicaciones oficiales y transcripciones (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Contexto:** cada comunidad tiene un lector (`harmonize/autonomicas/ccaa_XX.py`) que extrae de la publicación oficial los resultados por circunscripción y los comprueba: votantes = válidos + nulos, válidos = candidaturas + blancos y, si hay total publicado, suma de circunscripciones = total. Ningún número se deduce: lo que no publica el boletín queda vacío.
- **Resultado:** 15 de 19 comunidades se leen sin ninguna diferencia aritmética (entre ellas Illes Balears, que además está incompleta). Detalle:
  1. **Descuadres en la propia publicación** (comprobados con una segunda extracción del texto; se conservan las cifras publicadas y quedan en `notas`):
     - Andalucía (BOJA nº 108/2026): en Granada los votos de las candidaturas suman 476.345 y el cuadro I publica 476.342 votos a candidaturas (+3); el total de Andalucía arrastra la misma diferencia.
     - Canarias (BOC nº 121/2023): en El Hierro las candidaturas suman 6.218 y el anexo I publica 6.216 votos a candidaturas (+2).
     - Galicia (DOG nº 47/2024): el total de la comunidad publica 100 votos válidos y a candidaturas más que la suma de partidos y provincias.
     - Región de Murcia (BORM nº 135/2023): votantes publicados 694.906; válidos + nulos = 694.855 (+51).
     - Comunitat Valenciana (DOGV nº 9618/2023): el total de electores publicado (2.426.278) es la suma de Castellón y Valencia sin Alicante; se deja vacío y se guarda la cifra impresa en `notas`. Las cifras provinciales cuadran.
  2. **Cifras no publicadas** (se dejan vacías): votantes en Castilla y León (el anexo I no los trae); electores en Aragón (el informe solo da el censo de constitución de mesas).
  3. **Navarra:** el acta del BON nº 147/2023 es una imagen escaneada sin capa de texto y el OCR confunde cifras. Se transcribe a mano, comprobando cada voto con su cifra en letra, la aritmética del acta y los 50 escaños; el número de electores no tiene comprobación independiente. El lector solo funciona con el PDF de huella SHA-256 registrada.
  4. **Asturias:** se lee por OCR, con dos lecturas que deben coincidir y cada voto contrastado con su cifra en letra; si una cifra no es legible, el lector se detiene.
  5. **Illes Balears:** confirmado que el BOIB nº 83/2023 solo trae el escrutinio del CERA (1.566 votantes); faltan los resultados generales (`MANUAL_DOWNLOADS.md`).
  6. **Canarias:** se guardan por separado las 7 islas y la circunscripción autonómica (cada elector vota en ambas); no se suman.
  7. **CERA:** solo La Rioja y Aragón permiten comprobar que el resultado incluye el voto CERA; en el resto la publicación no lo dice (queda anotado por comunidad).
- **Propuesta:** aceptar los descuadres de las publicaciones como diferencias de la fuente (no del lector), usar las cifras por candidatura, que son las que sirven de objetivo, y dar por buena la transcripción de Navarra. G2.6 queda fallida mientras falten los totales oficiales de las generales (BOE) y los resultados generales de Illes Balears.
- **Aprobada por:** humano (2026-10-15), con las revisiones de D-032 (Alicante, Baleares, Navarra, Galicia)

## D-032 · Segunda ronda de F2: BOE de las generales, Baleares, Navarra, Alicante y Galicia (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Contexto:** el responsable da acceso a `www.boe.es`, aporta el BOIB nº 78/2023 (Baleares) y la página de resultados definitivos del Gobierno de Navarra, y pide revisar Alicante y Galicia.
- **Decisiones y hallazgos:**
  1. **Generales 2023, resultado oficial:** se cargan los cuadros I, II y III del Congreso del BOE-A-2023-18907 (Junta Electoral Central, escrutinio general, con voto CERA): 52 provincias, 59 candidaturas, 350 escaños. Todas las comprobaciones cuadran: votantes = válidos + nulos, válidos = candidaturas + blancos, suma de partidos = votos a candidaturas, escaños, y cada columna y cada partido reproducen el «Total estatal» publicado (37.469.458 electores; 24.952.447 votantes). Única errata: el total de Geroa Bai se imprime «9.938.» con un punto final. La corrección BOE-A-2023-19537 solo afecta al Senado. Salidas: `elecciones_generales_2023_provincias` y `_provincias_votos`.
  2. **Detalle municipal:** las hojas de Interior (escrutinio provisional, sin CERA) se mantienen como detalle municipal y como resultado de los **residentes**, que es el universo de la población sintética (regla 2 de `docs/02`, §3.5). Por provincia quedan siempre por debajo del BOE: 2.323.396 electores (el CERA) y 208.835 votantes en total (`elecciones.comparar_provisional_definitivo`). La diferencia mezcla el voto CERA y los cambios del escrutinio definitivo; no se pueden separar sin el escrutinio CERA por provincia.
  3. **Siglas de Interior y del BOE** (`partidos.yaml`, campo `codigo_boe`): las federaciones del PSOE (PSdeG, PSE-EE, PSIB, PSN) van dentro de «PSOE» en el BOE y el PSC aparte; las cuatro marcas de Sumar, dentro de «SUMAR»; JxCAT-JUNTS = JUNTS; Escons en Blanc dentro de Escaños en Blanco; PCTC, PCTG y PCTE/ELAK dentro del PCTE; Asturias Existe-EV dentro de España Vaciada; EVC = EVR («Entre Veïns Catalunya»). Cada enlace se comprueba: la candidatura del BOE tiene fila en todas las provincias donde se presentó la de Interior. Las 18 siglas que no se podían verificar tienen ya su nombre completo del BOE; su familia sigue los criterios aprobados en D-030 (por ámbito).
  4. **Illes Balears:** el BOIB nº 78 (13/06/2023, anuncio 5722) trae las actas de proclamación de las cuatro islas; se leen sin ninguna diferencia (59 escaños). El voto CERA del BOIB nº 83 se conserva aparte (`ccaa_04.leer_cera`). Hueco cerrado.
  5. **Navarra:** la página «Resultados Definitivos» del portal electoral del Gobierno de Navarra (texto extraíble) confirma todas las cifras transcritas del acta del BON, incluidos los electores (334.493 votantes + 184.505 abstenciones = 518.998). `ccaa_15.leer` hace este contraste cada vez y falla si algo no coincide.
  6. **Alicante:** la cifra de Alicante (1.304.381 electores) es correcta y coherente con el resto de su columna; lo erróneo es el total de la Comunitat impreso en el DOGV (2.426.278), que es exactamente Castellón (430.308) + Valencia (1.995.970), es decir, el total sin Alicante. Por eso el total de electores de la comunidad queda vacío y la suma correcta de provincias es 3.730.659. Las demás cifras del total cuadran.
  7. **Galicia:** en el resumen de la comunidad del DOG, los «votos a candidaturas» se imprimen como 1.488.805, cuando la suma de las cuatro provincias es 1.488.705 (608.185 + 186.070 + 176.022 + 518.428) y la de los votos de cada partido también. Es una errata de un dígito (centenas 7 → 8). Los «votos válidos» del total (1.501.857) se calcularon a partir de esa cifra errónea (1.488.805 + 13.052 blancos); con la cifra correcta son 1.501.757, y entonces votantes = válidos + nulos (1.501.757 + 14.187 = 1.515.944) cuadra. Electores, votantes, blancos, nulos y los votos de cada partido no tienen errores.
  8. **Descuadres aceptados (D-031):** se registran con su texto exacto en `autonomicas.ACEPTADOS`; G2.6 no los cuenta como fallo, pero cualquier otro descuadre sí.
- **Para revisar:** seis listas de una sola provincia tienen nombres que no indican un partido regional (PUEDE «Partido Unionista Estado de España», +RDS+ «Referéndum Sistema Dinero», UNIDOS SI, Fuerza Cívica, CCD «Coalición de Centro Democrático», Partido Autónomos; 2.401 votos en total). Por el criterio 3 de D-030 (ámbito) quedan en «nacionalistas y regionalistas»; se pueden pasar a «otros» si el responsable lo prefiere.
- **Decisión del responsable sobre las seis listas:** pasan a «otros» (`A_OTROS` en `tools/generar_partidos.py`). Resultado: 38 nacionalistas y regionalistas, 21 otros.
- **Aprobada por:** humano (2026-10-15)

## D-033 · Celdas vacías y calidad de las variables armonizadas (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Contexto:** en la revisión G2.8 el responsable pregunta por las celdas vacías de las muestras y pide que el tratamiento de datos sea impecable.
- **Diagnóstico** (recuentos agregados, sin abrir registros):
  - Las celdas vacías de las muestras están casi todas en los **campos originales** (12–60 % en las encuestas): preguntas que no se hacen a esa persona (fuera de universo) o variables que esa edición no publica. En lo armonizado pasan a NP. Es correcto.
  - En los **ficheros armonizados** había vacíos en 8 columnas. Siete tienen un motivo legítimo; uno era un **error**: en la EPA, los menores de 16 años tenían `edad_4` vacía en vez de NP. Corregido.
  - Al exigir una condición exacta para cada vacío apareció otra imprecisión: el universo del fichero de adultos de la ECV no es «16 años en la entrevista» (RB082), sino «16 años a 31 de diciembre del año anterior» (RB081, diseño de registro). Se añade `edad_31dic` al fichero armonizado y la condición pasa a ser exacta (10.573 de 10.573).
- **Decisiones:**
  1. **Vacíos documentados** (`checks.NULOS_DOCUMENTADOS`): cada vacío permitido tiene su condición y su motivo:
     - `municipio`: municipios de menos de 10.000 habitantes no identificados por el INE;
     - `peso_16` de la ECV: menores de 16 a 31/12 del año anterior;
     - `edad_4` de la EPA: grupo de 16 a 19 años;
     - electores de Aragón y votantes de Castilla y León: no publicados;
     - escaños: no impresos en la publicación, o candidaturas sin escaño en el BOE.

     G2.1 falla ante cualquier vacío fuera de esa lista o de su condición.
  2. **Informe de calidad** (`reports/fase_02_calidad.md`, con `sinpop harmonize --check`): para cada variable de cada fichero, % ponderado de NP, de vacíos y de NC y NS **sobre su universo**; se señalan las que superan el 5 % de NC + NS.
  3. **Muestras G2.8:** solo muestran los campos originales que lee la armonización, y la guía explica el significado de los vacíos.
  4. **Escaños autonómicos:** se dejan vacíos cuando la publicación no los imprime; no se deducen ceros (no se usan para construir la población).
- **Resultado:** 0 vacíos sin documentar; una sola variable señalada en el informe de calidad (ver D-034).
- **Aprobada por:** humano (2026-10-16)

## D-034 · Encuesta de Salud: el código 99 de NIVEST no es «no contesta» (2026-10-15)

- **Fecha:** 2026-10-15
- **Fase:** F2
- **Estado:** aprobada
- **Contexto:** el informe de calidad señala `estudios_3` de la ESdE 2023, con un 5,6 % ponderado de «no consta» (código 99, «No contesta» según el diseño de registro). Además, el código 03 («Educación primaria incompleta») no aparece en el fichero ni una vez.
- **Evidencia** (todo con agregados ponderados):
  1. El peso del código 99 sube con la edad como el de la primaria incompleta: 0,7 % en la veintena, 15,5 % a los 70, 30,1 % a los 80 y 38,3 % a los 90. Sumando 02 y 99, el perfil por edad sigue al de «analfabetos + primaria incompleta» del Censo Anual 2024, que no tiene ningún «no consta».
  2. La tabla oficial del INE 71335 (ESdE 2023, estado de salud por nivel de estudios, en miles) **no tiene categoría «no consta»**: sus tres niveles suman toda la población de 15 años y más. Los totales por estado de salud se reproducen exactamente con el fichero.
  3. La distribución de salud del nivel «Básico e inferior» solo se reproduce si el 99 está dentro: oficial 16,6 / 46,0 / 27,3 / 8,1 / 2,0 %; con el 99 dentro, 16,6 / 45,8 / 27,4 / 8,2 / 2,0; con el 99 como «no contesta», 18,2 / 47,2 / 26,0 / 6,8 / 1,8.
  4. Nueva cifra de G2.4 (reparto por nivel frente a la tabla 71335): con el 99 como NC el nivel básico queda en 38,1 % frente al 44,6 % oficial (−6,5 puntos: fuera de tolerancia); con el 99 en el básico, 43,7 % (−0,9 puntos, dentro de la tolerancia de 1,08). Queda una diferencia de unas 380.000 personas entre el básico y el intermedio que el fichero público no permite reproducir: el INE clasifica con un detalle de estudios más fino (CNED-14 a dos dígitos, según la metodología) que no se publica.
- **Propuesta:** recodificar NIVEST 99 → `hasta_obligatoria` en `variables.yaml` (fuente `encuesta_salud`), anotando que contradice la etiqueta del diseño y por qué. No afecta a ninguna otra fuente: el informe de calidad no señala ninguna otra variable.
- **Alternativas:** (a) mantener NC, lo que deja fuera del nivel básico a un 30–40 % de los mayores de 80 y sesga cualquier relación entre salud y estudios; (b) no usar los estudios de la ESdE.
- **Aplicada:** NIVEST 99 → `hasta_obligatoria` (`tools/generar_recodificaciones_encuestas.py` → `variables.yaml`, con la nota del motivo). Reparto por nivel frente a la tabla 71335: básico 43,69 % (oficial 44,59), intermedio 23,85 % (23,08), superior 32,46 % (32,33): las tres dentro de tolerancia. El informe de calidad ya no señala ninguna variable.
- **De paso:** los dos generadores de recodificaciones se han hecho idempotentes (ejecutarlos en cualquier orden deja `variables.yaml` igual); el de censos duplicaba «85-89» y reordenaba las categorías de situación profesional al volver a ejecutarse.
- **Aprobada por:** humano (2026-10-16)

## D-035 · Aprobación de F2 (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F2
- **Estado:** aprobada
- **Decisión:** el responsable revisa las muestras de 20 registros por fuente («tiene buena pinta», G2.8) y aprueba D-033 y D-034. Con las decisiones D-025 a D-034 aprobadas y la puerta automática superada (G2.1–G2.7), F2 queda cerrada y se inicia F3.
- **Aprobada por:** humano (2026-10-16)

## D-036 · Objetivos de calibración y validación (F3) (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F3
- **Estado:** aprobada
- **Contexto:** F3 pide, para cualquier territorio, las cifras que la población debe reproducir, separadas en calibradas y reservadas, coherentes entre sí y con fuente, edición y fecha. Las fuentes tienen fechas distintas: ECP a 01/01/2026, Censo Anual 2025 (exhaustivo) y 2024 (estudios, actividad, estado civil), Censo 2021 (tipo de hogar).
- **Decisiones:**
  1. **Fecha y efectivos:** 01/01/2026 (D-015). Los efectivos por provincia × sexo × edad simple son los de la ECP (tabla 59589). Cada variable de estructura se toma de la tabla oficial más reciente que la publica, **como cuotas dentro de la misma celda provincia × sexo × grupo de edad de esa tabla**, aplicadas a los efectivos de 2026. Así todos los objetivos de persona suman lo mismo por provincia, sexo y edad (G3.1, G3.2), y las comunidades y España son sumas de provincias (G3.3). Celdas sin efectivos en la tabla: cuotas nacionales de su sexo y grupo.
  2. **Grupos de edad de cada tabla** (`agrupaciones_edad` de `targets.yaml`): estudios 15-19…80-89, 90+ (tabla 66601); actividad 16-19…65-69, 70+ (67128); estado civil 16-34, 35-54, 55-74, 75+ (76291); urbanización 0-15, 16-64, 65+ (79341). Los objetivos usan esos grupos y no `edad_4`, que ninguna tabla publica (sus límites de 18 y 65 años no coinciden). Los donantes tienen la edad exacta, así que se pueden agrupar igual. Por debajo de la edad mínima, la variable es NP.
  3. **Universos:** residentes (ECP total), viviendas familiares (ECP 60129), colectivos (diferencia de ambas, D-021) y hogares (ECP 60133). La población sintética será hogares más el módulo de colectivos; las variables de estructura se dan para el total de residentes, porque las tablas no separan colectivos.
  4. **Nacionalidad:** española/extranjera de 2026 (viviendas familiares de la ECP 60129, más colectivos con la proporción de extranjeros de su celda en 2025); grupos y 15 principales nacionalidades con las cuotas del Censo Anual exhaustivo 2025 por provincia × sexo × edad_5. No se usan los grupos de la ECP (77019/77023) porque meten a México en «América del Norte» (unas 40.000 personas), mientras que D-025 lo pone en América Latina; el exhaustivo tiene el país exacto y se clasifica con la misma tabla que los donantes. La ECP 2025 y el Censo Anual 2025 coinciden exactamente (49.128.297).
  5. **Hogares:** tamaño (1, 2, 3, 4+) exacto de la ECP 2026; tipo de hogar con las cuotas del Censo 2021 **dentro de cada tamaño** y provincia, para que los hogares unipersonales coincidan con los de tamaño 1. Se declara la variable `tamano_hogar_4`.
  6. **Territorios por municipios** (`configs/territorios/*.yaml`; ejemplo técnico `ejemplo_almeria.yaml`): los objetivos provinciales se reparten entre municipios con la estructura del Censo Anual exhaustivo 2025. Los municipios de menos de 10.000 habitantes no están identificados en él, así que su clase de tamaño se reparte en proporción al Padrón 2025 (el Censo Anual manda en totales, D-015; el Padrón solo reparte). Los 83 municipios con cifra oficial de la ECP 2026 (tabla 79544) reciben exactamente su total por sexo, y el resto de su provincia se reajusta (IPF). Estudios y actividad por sexo salen de las tablas municipales del Censo Anual 2024 (una por provincia); en ellas, los pensionistas de jubilación e incapacidad van juntos y se separan con la proporción de su provincia. La nacionalidad se ajusta (IPF) al total por edad y sexo de cada municipio, para que todos los objetivos del territorio sumen lo mismo. Solo existen a nivel provincial: viviendas familiares y colectivos, hogares, estudios y actividad por edad, estado civil y autonómicas.
     - **Validación del método** antes de usar la ECP municipal: el reparto 2025 → 2026 se comparó con las 83 cifras de la ECP 2026 sin usarlas. Mediana de la diferencia 0,01 %, desviación típica 0,7 %, máximo −2,2 % (Torrevieja).
  7. **Electorales:** generales 2023 por familia, blanco, nulo y abstención sobre el censo electoral de residentes (hojas municipales de Interior, sin CERA), que es el universo de la población. Se calibra por provincia (y territorios superiores) y se **reserva el detalle municipal para validar** (propuesta de D-022, aplicada). Autonómicas por circunscripción, con abstención = electores − válidos − nulos y, en Aragón (sin electores publicados), solo sobre votantes. Las familias de las candidaturas autonómicas se asignan con los criterios de D-030 y D-032 (`tools/familias_autonomicas.py`).
  8. **Reproducibilidad:** sumas ordenadas y valores redondeados a la millonésima, para que el hash de cada fichero no cambie entre ejecuciones.
- **Consecuencias:** `sinpop targets --territory all` escribe `data/processed/targets/` (España, 19 comunidades, 52 provincias); `--territory MUNIS:<yaml>` para listas de municipios.
- **Aprobada por:** humano (2026-10-16)

## D-037 · Familias de las candidaturas autonómicas (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F3
- **Estado:** aprobada
- **Contexto:** los objetivos de las autonómicas (D-036) necesitan la familia de cada una de las 295 candidaturas (236 nombres) de las 19 publicaciones.
- **Decisión:** se aplican los criterios aprobados en D-030 y D-032, con las candidaturas de las generales como precedente (`tools/familias_autonomicas.py`; nombres tal como se imprimen). Resultado: 109 nacionalistas y regionalistas, 82 otros, 35 centro-derecha estatal, 28 izquierda estatal, 22 derecha radical, 19 socialdemócratas.
  - **Diez listas con nombre sin ninguna referencia territorial** pasan a «otros» por la regla de D-032: 100X100 Unidos, Sociedad Unida (Andalucía), Reset-Reinicio Político (Baleares), Hablemos Ahora, Ahora Tú, Movimiento Alternativo Electoral, Contigo Somos Democràcia (Canarias), Aquí Ahora, TÚ patria (Castilla-La Mancha) y Valores (Murcia).
  - **Clasificadas por su ámbito**, con nota de que el nombre no se ha identificado con certeza: Suma Principado, ETXSBC, Más Canarias, Proyecto Alantre, Coalició Units, Eguzkilore, Izan, Ongi Etorri. Todas, menos ETXSBC, tienen nombre con referencia territorial o en lengua cooficial.
  - **Coaliciones de Formentera:** «Sa Unió de Formentera (PP-Compromís)» → centro-derecha estatal (encabezada por el PP); «Gent per Formentera + PSIB» → nacionalistas y regionalistas (encabezada por Gent per Formentera).
  - **Otras asignaciones** basadas en el nombre:
    - el Partido Comunista del Pueblo Andaluz (organización andaluza del PCPE), Izquierda Anticapitalista Revolucionaria y País con Gestores (se presenta en dos comunidades) → otros;
    - Verdes Equo Asturias → izquierda estatal (marca de EQUO).
- **Erratas de los boletines** (se conservan): «PARITDO AUTÓNOMOS», «PODER ANDAlUZ», «CONTIGO SOMOS DEMOCRÁCIA», «PER UN MÓN MES JUST», y «Los Verdes-Ecopacifistas (CENTRO MODERADO)», cuyas siglas no corresponden al nombre.
- **Aprobada por:** humano (2026-10-16)

## D-038 · Síntesis de la población nacional base (F4) (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F4
- **Estado:** aprobada
- **Contexto:** F4 pide comparar al menos dos métodos de calibración, elegir uno con evidencia, integerizar a tamaño N con semilla y validar. Durante el trabajo aparecieron varios problemas de datos que exigen decisiones.
- **Decisiones:**
  1. **Universo de la actividad (16+).** Los microdatos del Censo 2021 y del Censo Anual dan la relación con la actividad desde los 15 años; las tablas oficiales (67128) y la EPA la dan desde los 16, y V-REGLAS prohíbe ocupados menores de 16 (el Censo 2021 tiene 5). En la población, actividad, ocupación, sector y situación profesional son NP por debajo de 16. Se corrige la nota del diccionario («en blanco = menores de 15», comprobado en los ficheros).
  2. **Método de calibración: logit acotado** (Deville-Särndal, factores en [0,2; 5]), resuelto por Newton con mínimos cuadrados (las restricciones son redundantes). Comparación sobre los mismos donantes y objetivos (calibración por comunidades):
     | | Raking | Logit acotado |
     | --- | --- | --- |
     | Factores en [0,2; 5] | 99,90 % (Canarias 98,2 %: incumple V-PESOS) | 100 % en las 19 comunidades |
     | Factor mínimo / máximo | 0,007 / 78 | 0,20 / 5,0 |
     | Kish / n | 0,910 | 0,919 |
     | TVD de los cruces reservados (pesos, antes de integerizar) | prácticamente iguales (diferencias < 0,0015) | |
  3. **España = unión de las 19 comunidades.** Calibrando solo con marginales nacionales, el reparto por provincias (reservado) empeoraba de TVD 0,012 a 0,022; calibrando cada comunidad con sus objetivos y sus donantes queda en 0,006 y la población nacional reproduce también cada comunidad (V-COHERENCIA).
  4. **Nacionalidades individuales calibradas** (`nacionalidad_top` pasa de reservado a calibrado; nuevo reservado `nacionalidad_top_sexo_edad`, perfil por sexo y edad de cada nacionalidad, con la agrupación `edad_nacionalidad` 0-19, 20-34, 35-49, 50-64, 65+). Con solo los 7 grupos calibrados, la composición interna era la de 2021 y las nacionalidades salían muy mal representadas (ratio Colombia 0,71; Ucrania 0,57; Perú 0,74; China 1,38; Ecuador 1,37), lo que haría fallar la auditoría de minorías.
  5. **Ampliación jerárquica de donantes** (docs/02 §5). Una celda calibrada de una comunidad es deficitaria si tiene menos de 5 unidades donantes locales o si su objetivo supera 3,5 veces la masa inicial local (nacionalidades que más han crecido desde 2021: Perú en 5 comunidades, Ucrania en Asturias y la Comunitat Valenciana…). Se añaden unidades de otras comunidades que caen en la celda (orden pseudoaleatorio fijo, mismo grado de urbanización y tamaño de municipio preferentes, sin las que caerían en celdas con objetivo 0), repartidas entre las provincias en proporción al objetivo; pierden el municipio y se marcan como no locales. Proporción de donantes locales: ≥ 99 % en todas las comunidades.
  6. **Fusión de nacionalidades muy pequeñas:** en cada comunidad, las nacionalidades con objetivo < 100 personas se calibran dentro de «otras extranjeras» (p. ej. 7,6 ecuatorianos en Melilla, cuyos dos hogares donantes ya pesan 55). Solo afecta a Ceuta, Melilla y celdas similares; la nacionalidad sigue calibrada por grupos.
  7. **Ceros estructurales:** las celdas con objetivo 0 y sin donantes (estudios superiores a los 15-19 años; zona rural o intermedia en Ceuta y Melilla) salen de la calibración; si tuvieran donantes, la construcción se detiene.
  8. **Colectivos (D-021):** cada celda provincia × sexo × edad_5 con residentes en colectivos recibe n = máx(5, objetivo/10) personas donantes de su provincia, sexo y edad (orden pseudoaleatorio fijo), como unidades individuales. Sus atributos distintos de edad, sexo y territorio se marcan `modelada`; los del hogar son NP y no tienen `household_id`.
  9. **Integerización:** TRS con muestreo sistemático ordenado (bloque, provincia, grado de urbanización, tamaño de municipio, residencia, tipo y tamaño de hogar, nacionalidad y edad de la persona de referencia) seguido de un **equilibrado** (variante de la fase de aterrizaje del método del cubo, Deville y Tillé 2004): intercambios de unidades dentro de la misma comunidad que acercan los recuentos de la muestra a los esperados en las celdas calibradas. Sin equilibrado, el muestreo por hogares (conglomerados) dejaba algunas marginales autonómicas fuera de V-MARG por azar (4 de 200 con 100.000 personas); con él, 0 de 199.
  10. **Interpretaciones de umbrales (pendientes de aprobación):**
      - V-CRUCE, V de Cramér: se aplica al nivel del territorio de la población (España); por comunidad y provincia se informa.
      - V-REGLAS-BLANDAS: la referencia son los donantes con los pesos calibrados. Se informa el resultado estricto (exceso ≤ 10 %) y con margen de muestreo (+ 2 errores típicos de una muestra aleatoria simple de tamaño N), porque con N pequeño un caso muy raro (p. ej. jubilados menores de 50, frecuencia 1,2 por 100.000) supera el 10 % por azar. Las reglas blandas no son puerta en docs/04 (G4.3 solo exige las duras).
  11. **Integerización sin mezclar hogares y colectivos.** El equilibrado solo intercambia unidades del mismo tipo: al permitir cambiar colectivos por hogares, su total se erosionaba (331 frente a 389 esperados con 50.000 personas). V-MARG incluye desde entonces el reparto viviendas familiares / colectivos, implícito en los objetivos.
  12. **Tamaño de municipio de los hogares trasladados** (ampliación de donantes): la clase más frecuente entre los donantes locales de la provincia con el mismo grado de urbanización (`modelada`), en lugar de la del municipio de origen.
- **Decisiones del responsable (G4.8, 2026-10-16): aprobadas A, B, C y D tal como se proponen.** A y B se aplican en `thresholds.yaml` (V-CRUCE: `factor_tvd_ref`, `tolerancia` y `excepciones`):
  - **A. Criterio de V-CRUCE con poblaciones pequeñas.** Cuando TVD_ref(N) supera el umbral fijo del nivel, el umbral es el propio TVD_ref, que es el percentil 95 de muestras aleatorias simples: una muestra aleatoria perfecta lo supera el 5 % de las veces, y el muestreo por hogares (conglomerados) algo más. Así, la puerta no se puede superar al pie de la letra con 25 poblaciones × 511 comprobaciones. Resultado: 207 fallos de 12.775 (137 con N = 10.000, casi todos en provincias de unos cientos de personas; 7 con N ≥ 500.000). **Propuesta:** el mismo margen que V-MARG, máx(1,2 × TVD_ref + 0,002, umbral del nivel) → 71 fallos, y con N ≥ 500.000 solo uno sistemático (B). Alternativa: mantener el umbral y exigirlo solo a partir de un tamaño mínimo por nivel.
  - **B. Tamaño de municipio en Segovia** (único fallo que persiste con N grande: TVD 0,085-0,095 frente a 0,08). Según el Padrón 2025, el 6,6 % de la provincia vive ya en un municipio de 10.001-50.000 habitantes que en 2021 tenía menos de 10.000; los microdatos del Censo no identifican los municipios pequeños, así que no se puede actualizar la clase de esos donantes. Propuesta: aceptarlo como limitación documentada (el tamaño de municipio no se calibra).
  - **C. Fuente de la relación con la actividad.** La población reproduce el objetivo calibrado (Censo Anual a 01/01/2024), pero frente a la EPA del 2T 2026 tiene menos ocupados (47,7 % frente a 52,3 % de los 16+, media de comunidades; Baleares 46,7 % frente a 63,0 %). Causas: fecha (dos años y medio de crecimiento del empleo), estacionalidad (1 de enero frente a segundo trimestre, muy marcada en Baleares) y definición (declarada frente a OIT). Opciones: (1) mantener el Censo Anual, coherente con las definiciones censales y con los demás objetivos de estructura, y documentarlo; (2) calibrar la actividad a la EPA (media anual de 2025 o los cuatro trimestres más recientes), más reciente pero con otra definición y solo para viviendas familiares. Propuesta: (1) en F4 y revisar con el enriquecimiento de F6, que usará la EPA.
  - **D. Sobremuestreo:** el número de miembros del grupo es el esperado, no un mínimo garantizado (9.872 frente a 10.000 pedidos en la prueba, −1,3 %). Propuesta: aceptarlo (la muestra es aleatoria) o, si se prefiere un mínimo estricto, pedir un 3 % más internamente.
- **Riesgos y limitaciones:**
  - El objetivo reservado `tipo_hogar_edad4_ref` usa la estructura de edad de la persona de referencia de 2021; la población, calibrada a la estructura de edad de 2026, tiene personas de referencia mayores (la proporción de adultos de 35-49 años bajó del 28,5 % al 25,4 %). Su TVD nacional (≈ 0,029-0,030) roza el umbral de 0,03 por esa diferencia de fechas.
  - Los inmigrantes llegados después de 2021 se representan con residentes de su misma nacionalidad en 2021 (el perfil de sexo y edad por nacionalidad se valida con `nacionalidad_top_sexo_edad`).
- **Evidencia:** `reports/fase_04.md` y `reports/fase_04_validacion.json`.
- **Aprobada por:** humano (2026-10-16)

## D-039 · V-CRUCE con poblaciones pequeñas: fallos que quedan tras D-038 (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F4
- **Estado:** aprobada (opción 1)
- **Contexto:** con el criterio aprobado en D-038 A y la excepción de Segovia (D-038 B), quedan 59 fallos de V-CRUCE en 12.775 comprobaciones (0,46 %): 43 con N = 10.000, 12 con N = 50.000, 4 con N = 100.000 y ninguno con N ≥ 500.000. Casi todos son provincias y comunidades pequeñas de poblaciones pequeñas que superan por poco el umbral fijo del nivel (0,08 o 0,05), en variables compartidas por todo el hogar (tamaño de municipio, estado civil, nacionalidad); uno es nacional, `tipo_hogar_edad4_ref` con N = 100.000 (0,0305 frente a 0,03), el desfase de fecha del objetivo de 2021 ya documentado. Ningún fallo se repite en las cinco semillas de un mismo tamaño salvo Segovia: son variación de muestreo, no sesgo.
- **Opciones:**
  1. **Separar ruido de sesgo** (propuesta): la puerta exige (a) que ningún cruce falle en las cinco semillas de un mismo tamaño (sesgo sistemático) y (b) que en cada población la proporción de fallos no supere el 5 % de las comprobaciones (lo que cabe esperar por azar con un umbral de percentil 95). Resultado actual: (a) 0 fuera de las excepciones; (b) máximo 2,3 % (N = 10.000).
  2. **Tamaño mínimo:** exigir V-CRUCE solo desde el tamaño mínimo recomendado en `fase_04.md` (100.000 personas para España y comunidades, 500.000 para provincias) e informar el resto. Resultado actual: quedaría el fallo nacional de `tipo_hogar_edad4_ref` con N = 100.000.
  3. **Mantener el criterio actual:** G4.2 no se supera mientras se generen poblaciones de 10.000 a 100.000 personas.
- **Aprobada por:** humano (2026-10-16), opción 1. Se aplica en `thresholds.yaml` (V-CRUCE, `proporcion_fallos_max: 0.05`) y en la puerta G4.2.

## D-040 · Aprobación de F4 (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F4
- **Estado:** aprobada
- **Decisión:** el responsable aprueba el informe `reports/fase_04.md` (G4.8), con D-036, D-038 y D-039 aprobadas. F4 queda cerrada y se empieza F5.
- **Aprobada por:** humano (2026-10-16)

## D-041 · Generador territorial (F5) (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F5
- **Estado:** aprobada
- **Contexto:** F5 pide generar cualquier territorio (comunidad, provincia o lista de municipios) con el mismo código que la nacional, con sus objetivos y sus donantes, y una jerarquía de donantes para territorios con pocos.
- **Decisiones:**
  1. **Jerarquía de donantes configurable** (`territories.yaml`): mismo territorio → misma provincia → misma comunidad con el mismo grado de urbanización → comunidades parecidas → España (último recurso, como en F4, D-038.5). Parámetros de la ampliación (5 unidades por celda; razón 3,5 → 2,5) en el mismo fichero.
  2. **Comunidades parecidas, con los datos:** las 3 más próximas por la TVD media de sus objetivos de estructura de F3 (edad × sexo, 15 nacionalidades, estudios, actividad, urbanización, tipo de hogar). Ejemplos: Ceuta → Melilla, Madrid, Murcia; Asturias → Castilla y León, Galicia, País Vasco.
  3. **Territorios por lista de municipios:** el Censo 2021 identifica los municipios de más de 10.000 habitantes. Sus hogares son donantes locales. Para los demás se usan los hogares sin municipio de su provincia y clase de tamaño (hasta 2.000; 2.001-10.000), con el peso inicial escalado por la parte de la población de esa clase y provincia que son los municipios de la lista (Padrón 2025), como nivel «misma provincia» (no locales). Los colectivos de esas provincias entran escalados por población. Se excluyen los donantes que caerían en categorías sin objetivo en la lista (p. ej. zona intermedia en un territorio rural). A cada hogar sin municipio de la lista se le asigna uno de su provincia y clase, al azar con la semilla y en proporción a la población (`municipio__calidad = modelada`); el tamaño de municipio pasa a ser el del Padrón 2025 del municipio asignado.
  4. **Reparación de la calibración:** si la calibración acotada no llega a la tolerancia de V-PESOS (0,1 %), se añaden donantes de la jerarquía a las celdas que se quedan cortas, sin tomar unidades de las que se pasan, y se recalibra (hasta 3 rondas). Caso real: municipios rurales de Teruel, donde faltaban africanos no marroquíes. Se registra en la ampliación (`motivo: reparacion N`).
  5. **Aceptación de la calibración:** la tolerancia es la de V-PESOS (0,1 %); la desviación alcanzada se guarda en el diagnóstico.
  6. **V-CRUCE por territorio:** el nivel del propio territorio usa el umbral de su tipo (comunidad 0,05; provincia y lista de municipios 0,08).
  7. **Informe de cada población** (`metadata.json`, `donantes`): proporción local, personas por nivel de la jerarquía, tamaño efectivo de Kish de los hogares donantes usados, confianza esperada (docs/02 §5: España alta, comunidad media-alta, provincia media, municipios baja) y «confianza reducida» si la proporción local es < 50 %.
  8. **Territorios de ejemplo por municipios** (`tools/generar_territorios_ejemplo.py`, códigos tomados del Padrón, no escritos a mano): urbano, València y 11 municipios de L'Horta (selección técnica); rural, los 226 municipios de Teruel de menos de 2.000 habitantes.
  9. **Prueba del territorio reservado:** Galicia calibrada sin actividad ni estudios, que se comprueban como reservados con el umbral de comunidad.
- **Consecuencias:** la calibración nacional también sigue la nueva jerarquía (las importaciones de Ceuta, Melilla y otras celdas deficitarias salen de las comunidades parecidas antes que de toda España).
- **Aprobada por:** humano (2026-10-16), con el informe de F5 (D-043)

## D-042 · Puerta F5: tres fallos y sus propuestas (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F5
- **Estado:** aprobada (el responsable delega la elección de la estrategia)
- **Contexto:** la serie F5 (19 comunidades, 10 provincias, 2 listas de municipios, España a 1M, semilla 1; `reports/fase_05.md`) supera G5.1, G5.4 y G5.5. G5.2 y G5.3 fallan por tres motivos. Ninguno se corrige sin decisión, porque A cambia los objetivos calibrados y B y C tocan umbrales.
- **A. Nacionalidad por edad (G5.2, V de Cramér).**
  - **Fallo:** en 7 comunidades (02, 07, 08, 15, 16, 18 y 19), la V de Cramér de `nacionalidad_esp_ext × es_adulto` se aleja de la oficial más de 0,03.
  - **Es un sesgo sistemático, no azar:** las 19 comunidades tienen demasiados menores extranjeros y algo pocos adultos extranjeros. Por ejemplo, los menores son extranjeros en un 20,9 % en Cataluña frente al 17,3 % oficial, y en un 4,9 % en Ceuta frente al 2,5 %. Por edad quinquenal, el exceso se concentra en los 0-4 años: ×1,46 en Cataluña y Madrid, ×2,5 en Ceuta.
  - **Causa:** solo se calibra el total de cada nacionalidad, no su edad. Para llegar a los extranjeros de 2026, la calibración pondera hacia arriba hogares extranjeros de 2021 con sus hijos, mientras que el crecimiento real desde 2021 ha sido sobre todo de adultos jóvenes. En Ceuta, además, los donantes de 2021 tienen el doble de niños extranjeros (9,6 %) que la ECP 2026 (3,8 %).
  - **No es un error de datos:** comprobados la nacionalidad y la edad de los donantes del Censo 2021 y el universo del objetivo (residentes; ECP 2026 tabla 60129 más colectivos).
  - **Propuesta:** nuevo objetivo calibrado `nacionalidad_edad`, española/extranjera × edad quinquenal (ECP 2026, residentes; las mismas celdas oficiales que ya alimentan `nacionalidad` y `adultos_nacionalidad`).
  - **Ensayo** (`tools/ensayo_d042.py`, `reports/fase_05/ensayo_d042.json`; el objetivo se añade en memoria, sin tocar configuración ni objetivos):

    | Comunidad | V oficial | V de la serie | V con el nuevo objetivo |
    | --- | ---: | ---: | ---: |
    | Cataluña | 0,018 | 0,023 | 0,023 |
    | Madrid | 0,016 | 0,001 | 0,018 |
    | Ceuta | 0,087 | 0,040 | 0,090 |
    | Melilla | 0,107 | 0,049 | 0,111 |

    En las cuatro comunidades del ensayo: V-MARG 0 fallos de 12, el resto de V-CRUCE sin cambios y Kish de los donantes casi igual (Ceuta 1.719 → 1.626).
  - **Coste:** `adultos_nacionalidad` deja de ser una prueba independiente, porque queda casi implícita en lo calibrado; solo el corte 15-17 / 18-19 queda sin calibrar. Seguiría como comprobación del censo de españoles adultos (G3.6). La prueba de minorías por edad sigue en `nacionalidad_top_sexo_edad`: las 15 nacionalidades una a una, por sexo y edad, que sigue reservada.
  - **Alternativa:** dejarlo como limitación documentada (pero afecta a una minoría y a los menores).
  - **Si se aprueba:** se rehacen los objetivos (F3, G3.4 incluido) y la serie F4 y F5.
- **B. V-COHERENCIA de los residentes en colectivos (G5.3).**
  - **Fallo:** `edad5_sexo_colectivos` da TVD 0,0107 frente al umbral fijo de 0,01. Las otras 17 comparaciones están entre 0,0001 y 0,0025.
  - **Causa:** la comparación cuenta 16.377 colectivos en las 19 poblaciones autonómicas y 7.790 en la nacional. Simulando dos muestras aleatorias de esos tamaños (300 réplicas), la TVD esperada por puro azar es 0,037 (p95 0,045). El 0,0107 observado es mucho mejor que el azar gracias al equilibrado. Con pesos (antes de integerizar), España es por construcción la unión de las comunidades (D-038.3), así que la coherencia es exacta.
  - **Propuesta:** el mismo margen de muestreo que V-MARG y V-CRUCE (D-038 A), umbral = máx(0,01, 1,2 × TVD_ref + 0,002), con un TVD_ref de dos muestras.
  - **Alternativa:** exigir 0,01 solo en los universos de más de 100.000 personas en las dos poblaciones e informar el resto.
- **C. Ceuta, `tipo_hogar_edad4_ref` (G5.2).**
  - **Fallo:** TVD 0,0518 frente a 0,05 a nivel de comunidad. Es 1 fallo de 12 comprobaciones (8,3 %), por encima del 5 % por población de D-039.
  - **No es azar:** a N = 50.000 como provincia da lo mismo (0,0519, que pasa con el umbral de provincia, 0,08), y TVD_ref es 0,013.
  - **Causa:** es el desfase de fecha ya documentado en D-038. El objetivo reservado usa la estructura de edad de la persona de referencia del Censo 2021, y la población está calibrada a la edad de 2026. Todos los territorios tienen la misma diferencia, de 0,02 a 0,05 (Canarias 0,046; Las Palmas 0,049), y Ceuta es la única que cruza el umbral.
  - **Propuesta:** excepción documentada como la de Segovia (D-038 B), en `thresholds.yaml` para CCAA:18 / PROV:51 en `tipo_hogar_edad4_ref`.
  - **Alternativa:** que F3 busque una fuente oficial más reciente de hogares por tipo y edad de la persona de referencia y, si no la hay, cambiar este cruce a «referencia 2021, informativo».
- **Otros resultados que no requieren decisión** (ya corregidos, sin cambiar el método):
  - España se calibra componiendo, un bloque cada vez, las calibraciones de sus comunidades. Es el mismo cálculo, pero de otro modo no cabía en memoria a 1M.
  - En la prueba del territorio reservado, V-MARG del resto excluía mal los objetivos retirados.
- **Decisión del responsable (2026-10-16):** «Elige la estrategia que consideres óptima para cada problema… nos interesan los datos de los mayores de 18 años… cíñete a la estrategia de las instrucciones». Elección:
  - **A: calibrar `nacionalidad_edad`.** El motivo pesa sobre todo en los adultos, no en los menores. En la serie, los extranjeros adultos quedaban entre un 0 % y un 8 % por debajo de la cifra oficial (Ceuta −7,6 %, Melilla −7,1 %, Baleares −5,7 %, Cataluña −3,6 %). Eso infla el universo con derecho a voto (españoles de 18 o más años) y deja corta una minoría adulta (docs/06). La calibración usa celdas oficiales de la ECP 2026, es la estrategia de docs/03 §2.1 (calibrar a objetivos oficiales del territorio, nacionalidad incluida) y el ensayo no pierde tamaño efectivo. Se calibra la edad quinquenal completa, menores incluidos, porque son las celdas oficiales y su coste es nulo. Los menores solo están en la población como miembros de los hogares de los adultos.
  - **B: margen de muestreo en V-COHERENCIA**, como en D-038 A (`thresholds.yaml`: `factor_tvd_ref` 1,2 y `tolerancia` 0,002; TVD_ref de dos muestras en `metrics.tvd_ref_dos`). Solo cambia el umbral de los colectivos (0,0555); las demás comparaciones siguen con el umbral fijo, porque su TVD_ref es menor que 0,01.
  - **C: excepción documentada** para Ceuta (`thresholds.yaml`, como Segovia). Se buscó una fuente más reciente en el INE (API Tempus, 16/10/2026): de las 78 tablas de la Estadística Continua de Población, las de hogares solo dan el tamaño (60131-60136); de las 988 del Censo de Población (anual), ninguna es de hogares. La única fuente de tipo de hogar por edad de la persona de referencia sigue siendo el Censo 2021.
- **Consecuencias:** se rehacen los objetivos de F3 (`sinpop targets --territory all` y las listas de municipios), la serie F4 (que valida también el nuevo objetivo) y la serie F5.
- **Resultado** (serie F5 repetida, `reports/fase_05.md`): G5.1-G5.5 superadas.
  - Extranjeros adultos a ±0,8 % de la cifra oficial en las 19 comunidades (antes, entre 0 % y −8 %).
  - V de Cramér de nacionalidad × mayoría de edad a ±0,006 de la oficial.
  - V-COHERENCIA de los colectivos: 0,0086.
  - Puerta F4 repetida: superada.
- **Aprobada por:** humano (2026-10-16), por delegación

## D-043 · Aprobación de F5 (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F5
- **Estado:** aprobada
- **Decisión:** el responsable aprueba el informe `reports/fase_05.md` (G5.6), con D-041 y D-042 aprobadas. F5 queda cerrada y se empieza F6.
- **Aprobada por:** humano (2026-10-16)

## D-044 · Diseño del enriquecimiento (F6) (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F6
- **Estado:** en vigor (F6 no tiene puerta de revisión humana; se presenta en `reports/fase_06.md` y se revisa en F7)
- **Contexto:** F6 añade las variables P1 y P2 que no están en los donantes censales, sin tocar las P0 (G6.5). Inventario de fuentes armonizadas (D-028):
  - ECV 2025: 29.369 hogares y 60.825 personas de 16 o más años; renta del año anterior.
  - EPA del 2T 2026: ocupados.
  - TIC-H 2025: 16 o más años, sin límite superior de edad, así que no hay hueco de mayores de 74.
  - Encuesta de Salud (ESdE) 2023.
  - Atlas de renta 2023: municipio, provincia y España.
- **Decisiones:**
  1. **Método: hot-deck aleatorio ponderado por celdas, con colapso jerárquico** (docs/03 §2.3, opción «por estratos»).
     - Cada persona u hogar sintético recibe un donante de la encuesta, sorteado con probabilidad proporcional al peso de la encuesta entre los donantes de su celda de llaves.
     - Si la celda tiene menos de 10 donantes, se quita la llave menos importante y se repite. El orden de colapso es fijo y se registra el nivel usado.
     - Así se reproduce la distribución condicionada ponderada de la encuesta: es lo que comprueban V-ENRIQ-MARG y V-ENRIQ-ASOC. Se asignan valores reales de donantes, nunca medias (docs/06, regresión a la media).
     - Es determinista con la semilla de la población.
  2. **Bloques heredados del mismo donante y llaves:**

     | Bloque | Fuente | Unidad | Variables | Llaves, en orden de colapso inverso (la primera es la última que se quita) |
     | --- | --- | --- | --- | --- |
     | Hogar | ECV | hogar familiar | renta equivalente, `renta_hogar_decil`, `renta_hogar_decil_ccaa`, `tenencia_vivienda`, `dificultad_fin_mes`, `vehiculo_hogar` | comunidad; tenencia del Censo (compatible, ver 3); tamaño del hogar; ocupados del hogar (0, 1, 2+); estudios más altos de los adultos; menores (sí/no); 65+ (sí/no); algún adulto extranjero; grado de urbanización |
     | Persona ECV | ECV | persona 16+ | `salud_autopercibida`, `discapacidad_limitacion`, `privacion_material`, `privacion_material_n` | comunidad; sexo; edad quinquenal; relación con la actividad; estudios; decil de renta del hogar (ya asignado); nacionalidad |
     | Empleo | EPA | ocupado 16+ | `tipo_jornada`, `sector_publico` | comunidad; sexo; edad; ocupación (CNO-11 a 1 dígito); situación profesional (empresario / autónomo / asalariado); estudios; nacionalidad |
     | Digital | TIC-H | persona 16+ | `uso_internet`, `compra_online`, `teletrabajo` | comunidad; sexo; edad quinquenal; relación con la actividad; estudios; nacionalidad |

     El bloque de persona de la ECV se empareja después del de hogar y usa el decil asignado como llave, para conservar la relación renta-salud. La privación va en la persona porque el indicador oficial (`vrMATSOCDEP`) es personal: combina carencias del hogar y propias.
  3. **Tenencia compatible con el Censo.**
     - Correspondencias (códigos comprobados: Censo T_REGTE; ECV HH021, TH021H):
       - propiedad ↔ ECV 1 y 2;
       - alquiler ↔ ECV 3 y 4;
       - otro ↔ ECV 4 y 5.
     - El 4 («alquiler a precio inferior al de mercado») cabe en «alquiler» o en «otro» del Censo, que incluye la vivienda cedida a bajo precio.
     - Así `tenencia_vivienda` (ECV) nunca contradice `tenencia_censo`.
  4. **Universos.** Variables de persona: menores de 16 → NP. Bloque de empleo: no ocupados → NP. Bloque de hogar: los residentes en colectivos → NP, porque la ECV y la TIC-H solo cubren viviendas familiares (`__calidad = observada` con valor NP por universo).
  5. **Renta y Atlas (tarea 4).** La renta de la ECV (renta disponible de 2024) y el Atlas (renta neta de 2023, de fuentes tributarias) no miden lo mismo en nivel, así que no se reescala ningún valor.
     - El Atlas da el **nivel relativo** de cada provincia (y de cada municipio identificado en las listas de municipios) dentro de su comunidad, con la media de la renta por unidad de consumo.
     - El objetivo es: media sintética de la provincia = media ECV de la comunidad × (Atlas provincia / Atlas comunidad).
     - Se alcanza **inclinando el sorteo** de donantes dentro de la provincia, con probabilidad ∝ peso × exp(λ · renta) y un λ resuelto para cada provincia. Se conservan los valores reales y el bloque completo.
     - Las comunidades uniprovinciales no se inclinan.
     - Umbral propuesto para G6.6, pendiente de confirmar: |error relativo| ≤ 2 % donde se calibró; donde no, se informa.
  6. **Contexto (P1).**
     - `ctx_renta_municipio`: renta neta media por persona del Atlas 2023 del municipio. Si el municipio no está identificado, la media de su provincia y clase de tamaño, ponderada por población (`modelada`).
     - `ctx_envejecimiento`: proporción de 65+ del municipio, con la misma regla y fuente oficial municipal.
     - `ctx_precio_vivienda` (P2): sin fuente oficial descargada; hueco documentado.
  7. **Huecos declarados (P2, no bloquean):**
     - `competencias_digitales`: la TIC-H 2025 no trae el indicador derivado; construirlo exige la metodología de Eurostat (DSI), que se deja documentada para una ronda posterior.
     - Consumo (EPF): sin variable en el diccionario.
  8. **Implementación.**
     - El enriquecimiento es la etapa 5 de `construir`, con su propia semilla derivada de la de la población. Escribe las columnas en `persons.parquet` y `households.parquet` con `__calidad = emparejada` (o `modelada` en el contexto imputado por clase) y la metadata de fuentes y nivel de colapso.
     - G6.5 lo comprueba un test: las columnas P0 son idénticas con y sin enriquecimiento.
  9. **Validación** (docs/05 §5):
     - V-ENRIQ-MARG: intervalo de confianza del 95 % de la encuesta por bootstrap de registros ponderados, por CCAA × edad_4.
     - V-ENRIQ-ASOC: V de Cramér con cada llave.
     - V-ENRIQ-BLOQUE: V de Cramér o Spearman entre las variables de cada bloque.
     - V-ENRIQ-HOLDOUT: emparejar sin estudios y comprobar que se recupera su asociación.
     - La salud se triangula además con la ESdE 2023.
- **Alternativas consideradas:**
  - *Predictive mean matching*: necesita un modelo por variable y rompe los bloques si se aplica variable a variable.
  - Vecino más próximo por distancia: tiende a concentrar donantes y a reducir la varianza.
  - Reescalar la renta al Atlas: mezcla definiciones distintas.
- **Aprobada por:** pendiente del informe de F6 (el umbral de G6.6 necesita confirmación humana)
