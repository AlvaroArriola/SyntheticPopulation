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
- **Estado:** aprobada
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
- **Aprobada por:** humano (2026-10-17), con el informe de F6 y D-046 a D-048 (umbral de G6.6 en D-046 C)

## D-045 · Enriquecimiento: estrategia de colapso, tenencia de los hogares extranjeros y llaves estructurales (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F6
- **Estado:** aprobada
- **Contexto:** con el diseño inicial de D-044 (llaves en orden fijo, la comunidad como primera llave, mínimo de 10 donantes por celda), muchas celdas no tenían donantes suficientes y se quitaban llaves importantes. Ejemplo, en Galicia: V de Cramér de renta × nacionalidad 0,29 en la ECV y 0,08 en la población. Se compararon estrategias sobre la población nacional de 1.000.000 de personas (semilla 1), con las métricas de docs/05 §5:

  | Estrategia (1M) | Celdas en IC 95 % (global) | V-ENRIQ-ASOC fuera de 0,05 | V-ENRIQ-BLOQUE máx. / medio | TVD de la tenencia |
  | --- | ---: | ---: | --- | ---: |
  | Llaves primero, k = 5, tenencia del Censo fija | 88,7 % | 1 de 81 | 0,020 / 0,008 | 0,035 |
  | Igual, sin tenencia del Censo | 90,2 % | 0 | 0,019 / 0,008 | 0,005 |
  | Núcleo de 2 llaves, k = 5, sin tenencia | 92,5 % | 2 | 0,016 / 0,007 | 0,007 |
  | **Elegida:** núcleo de 2 llaves, k = 5, tenencia fija salvo en hogares con extranjeros, situación profesional fija | 91,8 % | 0 | 0,020 / 0,007 | 0,012 |

- **Decisiones:**
  1. **Llaves ordenadas por su importancia medida en la propia encuesta.** Se usa la V de Cramér máxima con las variables del bloque. Resultado:
     - **Hogar:** ocupados, estudios más altos, adulto extranjero, 65+, menores, tamaño y grado de urbanización.
     - **Persona ECV:** edad por decenios, relación con la actividad, estudios, quintil de renta, nacionalidad y sexo.
     - **Empleo:** ocupación, nacionalidad, sexo, edad y estudios.
     - **Digital:** edad, relación con la actividad, estudios, nacionalidad y sexo.
  2. **Colapso con núcleo** (`hotdeck.niveles_nucleo`), en este orden:
     1. Se quitan las llaves secundarias manteniendo la comunidad.
     2. Se amplía la geografía, con la zona NUTS-1 (agrupación oficial de Eurostat) y después España.
     3. Solo al final se quitan las 2 llaves del núcleo.
     4. El mínimo es de 5 donantes por celda.
  3. **Tenencia de los hogares con algún adulto extranjero: la decide la ECV 2025, sin la tenencia del Censo como llave.**
     - Los extranjeros de la población son residentes de 2021 reponderados a 2026, y los llegados después de 2021 viven sobre todo de alquiler. Por eso, en la población (Censo 2021) el 47 % de los adultos extranjeros vive en propiedad y el 41 % de alquiler. En la ECV 2025 son el 34 % y el 62 % (con alquiler inferior al de mercado). Entre los españoles, las dos fuentes coinciden: propiedad 81,1 % y 81,5 %.
     - Con la tenencia fija, V de Cramér de tenencia × nacionalidad: 0,31 frente a 0,43 de la ECV (falla). Con la regla elegida: 0,39 (pasa).
     - Los hogares sin extranjeros conservan el régimen de su hogar donante. El 91 % de los hogares tiene una tenencia de la ECV compatible con la del Censo; los demás son hogares con extranjeros.
  4. **Llaves estructurales fijas, que no se quitan nunca:**
     - situación profesional en el empleo: un autónomo o un empresario no puede ser del sector público (con la situación como llave secundaria aparecían autónomos públicos);
     - ser ocupado en el bloque digital: el teletrabajo solo procede para ocupados;
     - tenencia compatible en los hogares sin extranjeros.
     La nacionalidad va en segundo lugar en el empleo, porque el empleo público exige en general la nacionalidad española (V de Cramér de sector público × nacionalidad: 0,09 → 0,13, frente a 0,17).
- **Lo que queda por debajo de los umbrales**, sin solución dentro del enriquecimiento: diferencias de composición entre la población, calibrada a las cifras censales, y las encuestas. Ver `reports/fase_06.md`:
  - Entre los adultos, «otra inactividad»: 19 % en la población y 10 % en las encuestas; ocupados: 49,6 % y 52 %.
  - Estudios hasta la obligatoria: 42 % en la población y 34-38 % en las encuestas.
  - Afectan sobre todo al teletrabajo (su NP son los no ocupados) y a la compra en línea.
- **Aprobada por:** humano (2026-10-17), con el informe de F6

## D-046 · Puerta F6: composición censal y límites del emparejamiento (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F6
- **Estado:** aprobada (A2, B1 y C)
- **Contexto:**
  - `reports/fase_06.md`: G6.2, G6.3, G6.5 y G6.6 se superan; G6.1 y G6.4 no.
  - Además, al revisar el contexto apareció un fallo de síntesis: unidades importadas de otra comunidad iban a provincias sin su grado de urbanización (18 personas de 1.000.000). Ya está corregido en `pesos._ampliar`. Hay que repetir las series F4 y F5, y conviene hacerlo una sola vez, después de esta decisión.
- **A. G6.1 y la composición de la población.**
  - Salud, carencias y variables digitales fallan por la composición, no por el emparejamiento. Ajustando la composición de la encuesta pasan al 97-100 % de celdas.
  - La población tiene menos ocupados (49,6 % frente a 52 %), el doble de «otra inactividad» (19 % frente a 10 %) y más estudios bajos (42 % frente a 34-38 %) que las encuestas de 2025-2026.
  - **A1:** mantener las cifras censales y evaluar G6.1 sobre la población con la composición de la encuesta. Se informa el resultado bruto y se aceptan como limitación los patrones regionales de tenencia, vehículo, jornada y sector público.
  - **A2** (**propuesta**): resolver ahora D-038 C con la opción 2.
    - Calibrar ocupados / parados / inactivos a la EPA del 2T 2026 por comunidad × sexo × edad. Dentro de los inactivos se mantiene el reparto censal (estudiante, jubilado, incapacidad, otra).
    - Así la población describe el mercado de trabajo de 2026, igual que las encuestas con las que se enriquece.
    - Los estudios siguen calibrados al Censo Anual: es la fuente oficial exhaustiva y la diferencia con las encuestas es de definición y respuesta.
    - Hay que rehacer F3 (objetivo `actividad_sexo`), F4, F5 y F6.
    - Después se evalúa G6.1 tal cual. Si solo quedan los patrones regionales, se presentan como limitación.
- **B. G6.4 (variable llave reservada).**
  - Todas las variables quedan mejor que la independencia.
  - Con |Δ| ≤ 0,05 no basta: el emparejamiento solo recupera en parte la asociación con una variable que no es llave. Es la hipótesis de independencia condicional, común a todo emparejamiento estadístico.
  - **B1** (**propuesta**): exigir «mejor que la independencia» (hoy se cumple en las 14 variables; sin los estudios se recupera entre el 19 % y el 98 % de la asociación). Se informa |Δ| con cada llave reservada (sexo, nacionalidad, actividad y estudios) y se documenta que las relaciones con variables que no son llave salen atenuadas.
  - **B2:** buscar un emparejamiento basado en modelo, con más variables comunes.
    - No hay muchas más variables comunes entre la población y las encuestas.
    - La ganancia esperada es pequeña y el coste, alto.
- **C. Umbral de G6.6:** máx(2 %, 2 errores típicos) donde se calibra. Hoy: 52 de 52 provincias dentro.
- **Aprobada por:** humano (2026-10-16): «Me gustan las propuestas… si tienes que volver a ejecutar las fases anteriores hazlo… la población más fehaciente posible a la real, con fecha de corte en junio de 2026».

## D-047 · V-SEMILLAS con cinco semillas: azar frente a sesgo (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F4 (serie repetida con D-046)
- **Estado:** aprobada
- **Contexto:** al repetir la serie F4, G4.5 falla en 1 de 1.220 proporciones.
  - Es la proporción de mujeres de 35-39 años entre los residentes en colectivos, con N = 10.000 (unos 80 residentes en colectivos por población).
  - Su desviación típica entre las 5 semillas es 1,59 veces la de una muestra aleatoria simple; el umbral es 1,5.
  - En los otros tamaños (50.000 a 1.000.000) no falla ninguna proporción. La razón media está entre 0,22 y 0,29.
- **Por qué es azar:** con 5 semillas, la desviación típica se estima con 4 grados de libertad. Para una proporción con la variabilidad de una muestra aleatoria simple, P(s > 1,5 σ) = P(χ²₄ > 9) = 6,1 %. En los colectivos, que se muestrean casi como personas sueltas (el equilibrado apenas reduce su varianza), es esperable que alguna de las 38 celdas supere 1,5 por azar.
- **Propuesta** (como D-039 para V-CRUCE): una proporción solo falla V-SEMILLAS si supera 1,5 en dos o más tamaños de población (sesgo sistemático). El resultado estricto se informa siempre.
- **Alternativa:** más semillas (por ejemplo, 10) solo en N = 10.000. Así baja la probabilidad de falso fallo, pero cuesta otra serie.
- **Aprobada por:** humano (2026-10-17). Aplicada en `thresholds.yaml` y en la puerta.

## D-048 · G6.1 tras calibrar la actividad a la EPA: lo que queda (2026-10-16)

- **Fecha:** 2026-10-16
- **Fase:** F6
- **Estado:** aprobada
- **Contexto:** tras D-046 A2 y la cadena F3-F6 repetida, G6.1 queda así (`reports/fase_06.md`):
  - 92,6 % de las celdas dentro del IC.
  - Por debajo del 90 %: tenencia (65 %), vehículo (81 %), sector público (86 %), jornada (87 %) y teletrabajo (89 %).
  - TVD nacional > 0,02: teletrabajo (0,033) y tenencia (0,020).
  - Con la población reponderada a la composición de cada encuesta (diagnóstico), todas las TVD quedan ≤ 0,019, y el teletrabajo, la salud, las carencias y las variables digitales entran en el IC en el 97-100 % de las celdas.
- **Lectura:**
  1. **Teletrabajo:** es una diferencia de fecha. La población tiene los ocupados del 2T 2026 (54,7 % de los adultos); la TIC-H es de 2025 (52,1 %). La categoría «no procede» de los no ocupados es menor en la población porque la población es más reciente que la encuesta.
  2. **Tenencia, vehículo, jornada y sector público:** son patrones regionales.
     - La tenencia de los hogares sin extranjeros es la del Censo 2021 (exhaustivo) y por comunidad no coincide con la muestra de la ECV 2025.
     - Las otras tres dependen de la comunidad más de lo que recogen las llaves, y la EPA, con su muestra grande, da intervalos estrechos.
     - Es lo que D-046 A2 preveía presentar como limitación.
- **Propuesta:**
  - G6.1 se supera cuando cada variable cumple el umbral, o cuando, con la composición de la encuesta, tiene TVD nacional ≤ 0,02 y su desviación regional está documentada como limitación.
  - Se informan siempre las dos lecturas.
  - Limitaciones declaradas: tenencia, vehículo, jornada y sector público por comunidad; el informe de cada población lo indica.
- **Alternativa:** añadir la comunidad como llave fija en esos bloques. Se perderían asociaciones con las llaves: con la comunidad primero, V-ENRIQ-ASOC tenía entre 6 y 11 fallos (D-045).
- **Aprobada por:** humano (2026-10-17). Aplicada en `thresholds.yaml` y en la puerta.

## D-049 · Correcciones de entrada que destapa la auditoría de F7 (2026-10-17)

- **Fecha:** 2026-10-17
- **Fase:** F7 (corrige F2-F3)
- **Estado:** aprobada por la persona responsable el 2026-10-20 (G7.7, D-059). Son medidas correctoras de docs/06 §4: primero revisar los datos de entrada y, si hay cifra oficial, calibrar el grupo.
- **Contexto:** la primera auditoría de la población nacional (1.000.000, semilla 1) da tres grupos con representación fuera de rango y perfiles de actividad desviados.
  - Jóvenes de 18 a 24 que ni estudian ni trabajan: 26 % frente al 13 % de la ECV 2025.
  - Personas sin estudios: ratio 1,16 frente al Censo Anual 2024.
  - Nacidos fuera con nacionalidad española: ratio 0,81 frente al Censo Anual 2025.
- **Causas, en los datos de entrada:**
  1. **Inactivos del Censo Anual.**
     - La relación con la actividad del Censo Anual 2024 (registros administrativos) clasifica al 23 % de los jóvenes de 20-24 años en «otra situación de inactividad». La ECV y la TIC-H, con situación declarada, los clasifican como estudiantes: el 49-53 % frente al 28 %. «Otra inactividad» es solo el 3 %.
     - El Censo no identifica bien a los estudiantes y su «otra inactividad» (19 % de los adultos) no coincide con ninguna encuesta (10 %).
  2. **Sin estudios:** no se calibraba; solo `estudios_3`. Los donantes de 2021 tienen más personas sin estudios que el Censo Anual 2024: 4,3 % frente a 3,7 %.
  3. **Nacidos fuera:** no se calibraba el país de nacimiento. Desde 2021 ha crecido mucho la adquisición de la nacionalidad española, así que los donantes de 2021 se quedan cortos.
- **Decisiones:**
  1. **La relación con la actividad, entera, de la EPA del 2T 2026.** Ocupados y parados según AOI (OIT). Los inactivos, según su situación autopercibida, con códigos comprobados en `dr_EPA_2026.json`.
     - **Una sola situación por persona.** SIDI1, SIDI2 y SIDI3 son hasta tres respuestas ordenadas por código, no por importancia: en todos los registros SIDI1 es menor que SIDI2. Una primera versión tomaba solo SIDI1 y, por eso, clasificaba como estudiante a todo jubilado que además hace un curso: un 3 % de estudiantes de 65 y más años, frente al 0,07 % del Censo. Se corrige con esta prioridad, la de los registros administrativos del Censo:
       - pensión de jubilación o prejubilación (02) → jubilado_pensionista;
       - incapacidad permanente (04) → incapacidad_permanente;
       - estudiante (01) que cursa enseñanza reglada (CURSR 1 o 2) → estudiante, como el Censo, que cuenta la matrícula en enseñanza reglada;
       - la primera de 03 (labores del hogar), 05 (pensión distinta de la de jubilación: la categoría 5 del Censo es solo «pensionista de jubilación, prejubilación»), 06 y 07 → otra_inactividad;
       - estudiante sin enseñanza reglada → otra_inactividad;
       - 00 y vacío → NC.
     - **Contraste por tramos**, en proporción sobre los inactivos:
       - Entre 35 y 65+ años, la EPA queda cerca del Censo.
       - En los jóvenes, corrige su sesgo: con 16-24 años, «otra inactividad» es el 12,7 % (Censo 26 %, ECV 4 %); con 25-34, estudiante es el 25 % (Censo 12 %, ECV 54 %).
       - Las alternativas comparadas fueron solo SIDI1, otros órdenes de prioridad y sin CURSR. Dan entre 3 y 8 veces más estudiantes de 35-64 años que el Censo, la ECV y la TIC-H.

     El reparto entre provincias y edades quinquenales dentro de cada comunidad × sexo × tramo sigue siendo el del Censo Anual, con la misma contracción de D-046.

     Es la definición declarada de la ECV, la TIC-H y el CIS, de modo que las capas de enriquecimiento, opinión y política comparan lo mismo.

     La actividad se calibra por los tramos de edad de la EPA (`actividad_tramo`: 16-24, 25-34, 35-44, 45-54, 55-64, 65+), que es la resolución a la que la EPA tiene muestra, para que el perfil de edad de los parados y estudiantes sea el de la EPA. El objetivo por tramo se deriva del quinquenal ya reescalado (coherencia G3.2). `actividad_edad` y `actividad_sexo` de ámbito provincial pasan a reservados; la comprobación de esquema de calibrados frente a reservados distingue ahora el ámbito (provincia o municipios).

     En las listas de municipios, las tablas municipales del Censo Anual se llevan a la EPA con el cociente provincial (`actividad_sexo_mun`).
  2. **Nuevo objetivo calibrado `sin_estudios_edad`:** «Sin estudios» (CNED-A nivel 0: analfabetos y primaria incompleta) por edad, de la tabla 66601. Va con la variable derivada `sin_estudios`.
  3. **Nuevo objetivo calibrado `nacimiento_nacionalidad`:** nacido fuera × nacionalidad española/extranjera. Usa la proporción de nacidos fuera de cada provincia × sexo × edad × nacionalidad en el Censo Anual exhaustivo 2025, sobre las celdas de la ECP 2026 (3,07 millones de españoles nacidos fuera, 6,2 %). Va con la variable derivada `nacido_fuera`.
  4. **Categorías de inactividad casi vacías en un tramo.** En la calibración, la categoría de inactividad que pesa menos del 2 % de los inactivos de su tramo (`MIN_INACTIVIDAD`) se funde con «otra inactividad» del mismo tramo.
     - Ejemplos: jubilados de 16-44 años y estudiantes de 65 y más. La EPA tiene algunos y los donantes del Censo casi ninguno, así que la calibración acotada no tiene solución.
     - La persona conserva su categoría, y el total de inactivos del tramo se sigue calibrando.
     - Es el mismo mecanismo que las nacionalidades pequeñas (D-041).
     - Las fusiones quedan en los metadatos de la población (`fusiones`).
  5. **Celdas diminutas sin donantes.** Algunas celdas con objetivo positivo no tienen ningún donante posible ni tras ampliar los donantes. Ejemplo: jubilados de 25-34 años en Ceuta, que salen de la contracción hacia la EPA.
     - Si la celda pesa ≤ 0,1 % de su objetivo (`MAX_SIN_DONANTES`), sale de la calibración.
     - Su valor se reparte, en proporción, entre las demás categorías del mismo cruce (mismo tramo), así que los totales se conservan.
     - Queda registrada en los metadatos de la población (`ceros`, motivo `sin_donantes`).
     - Si es mayor, la construcción se sigue deteniendo.
     - Alternativa descartada: poner a 0 en los objetivos las categorías que el Censo agregado no tiene en la celda. Choca con la muestra de donantes, que sí las tiene (p. ej. jubilados de 16-24), y fuerza ceros que no son reales.
- **Consecuencias:** se rehacen F3-F6 y la auditoría. La prueba del territorio reservado de F5 retira ahora `actividad_tramo` y `estudios_edad`.

## D-050 · Desfase de los donantes de 2021 y comparaciones homogéneas en la auditoría (2026-10-17)

- **Fecha:** 2026-10-17
- **Fase:** F7 (corrige F3, F6 y la lista de vigilancia)
- **Estado:** aprobada por la persona responsable el 2026-10-17. Eligió las cuatro opciones recomendadas. Ratificada en G7.7 (D-059).
- **Contexto:** la cadena F4-F7 repetida tras D-049 deja estos fallos:
  - **G4.2:** estado civil × edad, sistemático a 10.000 personas.
  - **G5.2:** V de Cramér de actividad × sexo.
  - **Auditoría F7:** en rojo los jóvenes ni-ni, el perfil de actividad de los grupos de la ECV y la TIC-H, y el perfil de edad de paraguayos y rumanos.
- **Decisiones:**
  1. **Estado civil × edad pasa a calibrado.**
     - **Por qué falla:** los donantes del Censo 2021 tienen más casados y menos solteros de 35-54 años que el Censo Anual 2024 llevado a la ECP 2026 (−1,2 puntos de solteros y +0,9 de casados). Con 1.000.000 de personas, la TVD es 0,028 frente a un umbral de 0,03. Con 10.000 lo supera por ruido en las 5 semillas.
     - **Consecuencia:** se pierde como cruce de control; quedan 10 reservados.
     - **Alternativa descartada:** declararlo limitación.
  2. **Nuevo objetivo calibrado `nacionalidad_top_edad`:** 15 nacionalidades × 5 grupos de edad, del Censo Anual exhaustivo 2025 sobre los extranjeros de la ECP 2026.
     - **Por qué:** los donantes de 2021 no recogen el rejuvenecimiento de los paraguayos (llegados hace poco) ni el envejecimiento de los rumanos (TVD de 0,088 y 0,084 frente a 0,08).
     - **Celdas pequeñas:** van a otras_extranjeras de la misma edad. Son las celdas de menos de 100 personas y las de las nacionalidades ya fundidas (D-041).
     - **Consecuencia:** el perfil de edad de cada nacionalidad deja de ser un control independiente; el de sexo sigue reservado.
  3. **Actividad calibrada por sexo:** `actividad_tramo` pasa a relación con la actividad × sexo × tramo de edad, que es como la EPA construye el objetivo. Sin el sexo, la asociación actividad × sexo era la del Censo y fallaba G5.2.
     - **Fusiones con otra_inactividad del mismo cruce** (`_fusionar_actividad`). Son reglas basadas en los datos, no una lista de celdas; la persona conserva su categoría y el total del cruce se calibra:
       - **Falta de cobertura.** Una categoría no ocupada cuya proporción en todos los donantes, multiplicada por el factor máximo de la calibración (5), no llega a la del objetivo con un margen de 1,25. Ejemplos: los incapacitados de 65 y más, a los que el Censo, de registros administrativos, cuenta como jubilados, y los parados varones de 65 y más en Andalucía.
       - **Exceso de cobertura.** Si una categoría de inactividad tiene en los donantes del bloque, por el factor mínimo (0,2) y con el mismo margen, más de lo que pide el objetivo, todas las categorías de inactividad del cruce se calibran como un total. Ejemplo: varones de 35-44 en «otra inactividad» en el País Vasco.
       - **Objetivo 0 con donantes.** Las categorías no ocupadas en ese caso. Ejemplo: paradas de 65 y más en Ceuta.
       - **Por qué el margen:** otras restricciones tiran de las mismas unidades.
   2 ter. **Exceso de cobertura en estado civil y en nacionalidad × edad.** Si los donantes del bloque cubren de más una celda (su proporción por 0,2, con margen de 1,25, supera la del objetivo), esa celda se calibra junto con la categoría más numerosa de su cruce.
     - **Cruce:** el tramo de edad en el estado civil; la nacionalidad en nacionalidad × edad.
     - **Ejemplo:** estado civil «no consta» de 35-54 años en Ceuta, mucho más frecuente en los donantes de 2021.
     - **Último recurso:** si un bloque sigue sin converger y hay celdas de nacionalidad × edad fuera de tolerancia, esas nacionalidades se calibran en el bloque solo por su total y se repite, con 5 intentos como máximo (`MAX_SIN_EDAD`). Le ocurre a los marroquíes de Ceuta: los hogares de 2021 traen juntos niños y adultos con una estructura de edad que no casa con la de 2025.
     - Todo queda en las fusiones de la calibración.
   2 bis. **Nacionalidades pequeñas sin edad.** Una nacionalidad con menos de 2.000 personas en el bloque (`MIN_NACIONALIDAD_EDAD`) se calibra solo por su total: todas sus edades van a una celda. Con tan pocos donantes, el total y la edad no se pueden cumplir a la vez dentro de las cotas; ejemplo: ecuatorianos en La Rioja (1.090).
  4. **Atributo nuevo `cursa_formacion`.** Indica si la persona ha cursado estudios reglados o formación no reglada en las cuatro últimas semanas. Sale de CURSR y CURSNR de la EPA 2T 2026 (tabla TCURSR, comprobada en `dr_EPA_2026.json`).
     - Se enriquece en un bloque nuevo, «formación» (F6): EPA, 16+ no ocupados, con la relación con la actividad como llave fija; los ocupados quedan NP.
     - **Jóvenes ni-ni con la definición de Eurostat:** sin empleo y sin educación ni formación. La referencia es la EPA con la misma definición, de 20 a 24 años, porque la EPA no separa a los de 18 y 19; da un 11,5 %.
     - **Antes:** se comparaba con la ECV, cuya situación principal declarada no es la de la EPA (ratio 1,55).
     - **Alternativas descartadas:** referencia de la EPA sin el atributo (no es la tasa oficial) o limitación declarada.
  5. **Perfiles de actividad en tres categorías** (ocupado, parado, inactivo) cuando la referencia es una encuesta (ECV, TIC-H, EPA).
     - **Por qué:** las subcategorías de inactividad de la ECV y la TIC-H (situación principal declarada) no se definen como las de la EPA, de la que sale la población.
     - **TVD con 3 categorías:** limitación grave 0,027, privación severa 0,080 y nunca usa internet 0,008. Con 6 categorías eran 0,107, 0,112 y 0,162.
  6. **Referencia de tipo de hogar × edad de la persona de referencia llevada a 2026.** Aprobado el 2026-10-18.
     - **Por qué:** G4.2 fallaba de forma sistemática con 500.000 y 1.000.000 personas (TVD 0,0304-0,0307 frente a 0,03). La referencia reservada repartía los hogares de 2026 con la edad de la referencia de 2021, sin el envejecimiento posterior, mientras que la población está calibrada a la edad y al estado civil de 2026.
     - **Método de las tasas de jefatura:** la proporción de personas de cada provincia × sexo × edad_5 que son referencia de su hogar en 2021 se aplica a la población en viviendas familiares de la ECP 2026. Da los hogares de 2026 por provincia y edad_4 de la referencia, escalados al total de hogares de la ECP. Como el grupo 15-19 corta los 18 años, las tasas se parten por la edad_4 de la referencia.
     - **Construcción:** la estructura tipo × tamaño × edad del Censo 2021 se ajusta por IPF a dos márgenes: tipo × tamaño calibrado (sin cambios) y esos hogares por edad.
     - **Efecto:** los hogares con referencia de 35-49 años pasan del 26,9 % al 24,0 % y los de 65 y más, del 35,6 % al 37,4 %. Con 1.000.000 de personas la TVD baja de 0,0304 a 0,0134.
     - Sigue reservado y la población no cambia.
     - **Alternativas descartadas:** una excepción documentada, o calibrarlo, que haría heredar a la población la edad de 2021.
  7. **Nuevo objetivo calibrado `actividad_nacionalidad`:** ocupados, parados e inactivos × nacionalidad española/extranjera × tramo de la EPA, por provincia; variable derivada `actividad_3`.
     - **Primera versión, solo ocupados y no ocupados:** corrigió el empleo, pero entre los extranjeros no ocupados seguía habiendo un 17 % de parados frente al 27 % de la EPA.
     - **Por qué:** la actividad se calibraba con la EPA por sexo y tramo, pero no por nacionalidad, y quedaba la de los donantes de 2021. Los extranjeros sintéticos trabajaban entre 8 y 14 puntos menos que en la EPA: de 35-44 años, 67,8 % frente a 75,3 %; de 55-64, 44 % frente a 58 %. Los españoles quedaban algo por encima. Además, por composición, la asociación nacionalidad × formación era más fuerte que en la EPA (fallo de G6.4).
     - **Construcción, coherente por construcción con lo calibrado:**
       - los ocupados y los parados de cada provincia y tramo son los de `actividad_tramo`;
       - los extranjeros, los de `nacionalidad_edad` (el grupo 15-19 se parte con la proporción de 16-19 de la ECP por edad simple);
       - el reparto de ocupados y de parados entre españoles y extranjeros sigue sus tasas de empleo y de paro de la EPA por comunidad × nacionalidad × tramo, contraídas hacia la nacional con 200 personas como en D-046; sin muestra regional, la nacional;
       - los inactivos son el resto.
     - Es una aplicación de D-049 (la actividad, de la EPA), no un umbral nuevo.
  8. **Actividad calibrada con 16-19 y 20-24 años por separado** (`edad_tramo_epa`: 16, 20, 25, 35, 45, 55, 65).
     - **Por qué:** con el tramo 16-24 de una pieza, la actividad del tramo era la de la EPA, pero el reparto entre 16-19 y 20-24 seguía al Censo, que clasifica a muchos estudiantes de 20-24 como «otra inactividad» (el sesgo de D-049). La población de 20-24 tenía un 29,7 % de estudiantes frente al 34,5 % de la EPA, y los jóvenes ni-ni salían con ratio 1,14 (13,1 % frente a 11,5 %), sin que la composición por estudios lo explicara (12,98 % ajustado).
     - Es una aplicación de D-049; la EPA da los dos grupos por separado.
- **Correcciones de código:**
  - **Peso inicial de los donantes importados.** Con pocos donantes locales, cada unidad añadida recibía el objetivo de la celda dividido entre el número mínimo de donantes, sin contar cuántas personas de la celda trae. Ejemplo: 8 hogares chinos de unas 4 personas para 123 chinos en Teruel daban unas 790 personas, y ni con el factor mínimo se bajaba al objetivo. Ahora se divide entre las personas de la celda que traen.
  - **V-MARG.** Una celda fundida en la calibración con objetivo 0 puede tener personas, porque estas conservan su categoría: no cuenta como fuera de dominio, aunque su desviación sigue en la TVD. Ejemplo: paradas de 65 y más en Melilla, que la EPA no tiene por tamaño de muestra.
  - **Tope del peso inicial de una unidad añadida:** 10 veces la mediana del peso de los donantes locales del bloque (`MAX_PESO_IMPORTADA`).
    - **Por qué:** una unidad importada para cubrir una celda con pocos candidatos podía llegar con un peso de 337, frente a 10 de los donantes del Censo, y desbordar otras celdas pequeñas en las que también cae. Ejemplo: un hogar con un parado de 65 y más años en Baleares, en una celda de 47 personas.
    - **Si falta peso:** lo suplen las rondas de reparación, con más donantes.
    - **Exceso de cobertura:** se aplica también a los parados de `actividad_tramo` (con otra_inactividad) y a `actividad_nacionalidad`.
  - **Celdas diminutas.** Las celdas de menos de 100 personas (`MIN_CELDA_NACIONALIDAD`, el umbral de D-041) se calibran junto con la categoría principal de su cruce: la no ocupación en `actividad_tramo` (con otra_inactividad), y `actividad_nacionalidad` y `nacionalidad` (con la más numerosa). Con tan pocas personas, uno o dos hogares importados por otra celda bastan para que no haya solución. Ejemplos: parados varones de 65 y más en Cantabria (22) y nacionalidad «otros» en Ceuta (3).
  - **Donantes de menos en `actividad_nacionalidad`.** Una celda que ni con el factor máximo alcanzaría su objetivo se calibra con la más numerosa del cruce. Ejemplo: parados extranjeros de un tramo en Madrid. En las demás tablas, la falta de donantes la resuelve la importación (D-041).
  - **Último recurso general.** Si un bloque no converge, las celdas fuera de tolerancia de los objetivos secundarios se calibran con su destino y se repite, con hasta 8 intentos.
    - **Objetivos secundarios:** actividad, actividad por nacionalidad, estado civil, sin estudios, nacimiento y nacionalidad.
    - **Nunca:** edad, sexo, tamaño o tipo de hogar, ni españoles/extranjeros por edad.
    - **Destino:** otra_inactividad del cruce en la actividad; otras_extranjeras en la nacionalidad; en el resto, la categoría más numerosa del cruce.
    - **Ejemplo:** en Teruel, varias celdas pequeñas a la vez (sin estudios de 15-19, británicos, estado civil «no consta» de 75 y más) no tenían solución conjunta.
    - Queda en las fusiones de la calibración.
  - **Fusiones encadenadas.** Una clave fundida dos veces (nacionalidad pequeña → otras_extranjeras de una edad → edad más numerosa) va directamente a su destino final.
  - **Memoria.** La tabla de celdas por donante se construye con las fusiones ya aplicadas, sin copia, y se suelta lo del intento anterior. Los candidatos a importar reciben su nivel de la jerarquía sin copiar la tabla por nivel.
  - **Resolución numérica del paso de Newton.** Si la SVD de LAPACK no converge con restricciones redundantes (objetivos que suman lo mismo, como `trabajo_nacionalidad`), se usa QR con pivotaje (`gelsy`), que da la misma solución de mínimos cuadrados.
  - **Exceso de cobertura en `nacionalidad_top`.** La nacionalidad sobrecubierta se funde con otras_extranjeras, como las pequeñas (D-041).
- **Otros cambios sin decisión de método:**
  - La auditoría da «sin referencia» si el territorio no tiene el objetivo del que sale la cifra (listas de municipios); antes se detenía.
  - Ajustes de memoria en la construcción de España, sin efecto en los resultados.
- **Consecuencias:** se rehacen F2 (EPA), F3-F6 y la auditoría.

## D-051 · Márgenes de muestreo en la auditoría de F7 y limitaciones de composición (2026-10-19)

- **Fecha:** 2026-10-19
- **Fase:** F7
- **Estado:** aprobada por la persona responsable el 2026-10-19. Eligió las tres opciones recomendadas.
- **Contexto:** con F4, F5 y F6 superadas, la auditoría de F7 da 25 grupos en verde y 2 en rojo en la población nacional. En los territorios pequeños hay muchos rojos, casi todos en nacionalidades de 40 a 250 personas.
  - Esos rojos vienen de dos criterios que no dependen del tamaño:
    - **Perfil:** TVD ≤ 0,08, con un perfil muy ruidoso con tan pocas personas.
    - **Concentración:** los 5 hogares donantes más usados ≤ 20 %. Con 60 personas en hogares de 3, los 5 mayores ya pesan más del 20 % por fuerza.
  - V-DIVERSIDAD falla en la nacionalidad (93,9 %) y en el país de nacimiento (93,2 %) frente al 95 %. Los grupos que fallan tienen de 100 a 760 personas y casi ningún extranjero.
- **Decisiones:**
  1. **V-MINORIAS-PERFIL con margen de muestreo,** como V-MARG y V-CRUCE (D-038 A): umbral = máx(0,08; 1,2 × TVD_ref(n) + 0,002).
     - TVD_ref(n) es el percentil 95 de la TVD de muestras aleatorias simples de tamaño n de la distribución oficial.
     - n son las personas del grupo con la variable conocida.
  2. **V-CONCENTRACION:** el top 5 cumple si es ≤ máx(20 %, el inevitable). El inevitable es el peso de los 5 hogares sintéticos con más miembros del grupo; cada residente en colectivo cuenta por separado. Se mantiene el mínimo de donantes distintos.
  3. **V-DIVERSIDAD:** un grupo cumple si su entropía es ≥ 0,9 × la de referencia o si no baja del percentil 5 de la entropía de muestras aleatorias simples de su tamaño de la distribución de referencia.
  4. **Limitaciones declaradas en la población nacional,** como en D-048:
     - **Personas que nunca usan internet:** ratio 1,11 frente a la TIC-H 2025; 1,04 si la población se repondera a la composición por edad × estudios de la TIC-H. El Censo Anual 2024, al que se calibran los estudios, tiene más personas con estudios obligatorios o menos que la muestra ponderada de la TIC-H (25-34 años: 27,5 % frente a 15,5 %).
     - **Carencia material y social severa:** la representación está dentro del intervalo de la ECV (ratio 0,95). Solo falla el perfil de actividad (TVD 0,085, con 3 categorías), porque la ECV mide el paro según lo que declara cada persona y la población usa el paro de la OIT de la EPA (D-049).
- **Alternativas descartadas:** solo grupos de 200 o más; subir el mínimo de V-DIVERSIDAD a 500; mantener los criterios y declarar limitaciones; un criterio ajustado por composición para los grupos de encuestas.
- **Medida correctora complementaria** (docs/06 §4, punto 3: ampliar los donantes de forma jerárquica): ampliación propia de `nacionalidad_top`.
  - **Por qué:** muchas nacionalidades han crecido desde 2021 (por ejemplo, argentinos). Sus pocos hogares donantes llegaban al factor máximo y se clonaban 3 o 4 veces; en Aragón, los 5 donantes más usados daban el 34 % de los argentinos.
  - **Regla:** una nacionalidad cuyo objetivo supera 1,5 veces la masa de sus donantes locales se amplía por la jerarquía hasta 1,2; antes, 3,5 y 2,5. Además, cada nacionalidad tiene al menos 30 hogares donantes.
  - **Resultado en la prueba de Aragón con 100.000 personas:** rojos de 8 a 5 y argentinos del 34 % al 23 %.
  - **Alternativa probada y descartada:** 1,2 y 1,0. No mejoraba (6 rojos) y añadía grupos en ámbar por donantes no locales.
  - **Excepción:** la ampliación propia de las nacionalidades no se aplica a las listas de municipios, que ya toman sus donantes de su provincia y clase de municipio. Importar hogares de otras comunidades desbordaba sus celdas de grado de urbanización; en Valencia urbano, la zona intermedia quedaba +49 %.

## D-052 · Error de muestreo de la encuesta de referencia en V-MINORIAS-PERFIL (2026-10-19)

- **Fecha:** 2026-10-19
- **Fase:** F7
- **Estado:** aprobada por la persona responsable el 2026-10-20 (G7.7, D-059).
- **Contexto:**
  - El margen de muestreo de D-051 compara el perfil del grupo sintético (n personas) con el perfil oficial como si este fuera exacto.
  - Eso vale para las fuentes exhaustivas: ECP, Padrón, Censo Anual y objetivos.
  - No vale para los grupos que salen de una encuesta: limitación grave y privación severa (ECV), ni-ni (EPA) y nunca internet (TIC-H).
    - Por comunidad, esos perfiles salen de unas decenas o cientos de entrevistas.
    - Con la población a 100.000 personas, el umbral se quedaba en 0,08, mientras que la propia encuesta varía mucho más de una muestra a otra.
  - Percentil 95 de la TVD entre la encuesta y sus réplicas bootstrap, con 3.000 personas sintéticas:

    | Grupo | Territorio | TVD del perfil |
    | --- | --- | --- |
    | privación severa | La Rioja | 0,15 (sexo) a 0,22 (edad) |
    | privación severa | Andalucía | 0,12 a 0,19 |
    | ni-ni | Madrid | 0,16 a 0,18 |
    | privación severa | España | 0,02 a 0,04 |

  - En la auditoría anterior había 28 poblaciones en rojo por el perfil de la privación severa: todas salvo España quedaban dentro de ese ruido. Con la limitación grave, el ni-ni y nunca internet pasaba lo mismo.
- **Alternativas consideradas:**
  1. Mantener el umbral y declarar la limitación. Se descarta porque el rojo no indicaría un defecto de la población, sino el tamaño de la encuesta.
  2. Usar el tamaño efectivo de Kish de la encuesta. Se descarta porque ignora la agrupación por hogares (la privación es del hogar) y daría un margen demasiado estrecho.
  3. **Elegida:** TVD_ref de dos muestras, como en V-COHERENCIA (D-042 B), con el diseño de la encuesta.
- **Decisión:** si la referencia del perfil es una encuesta, TVD_ref(n) pasa a ser el percentil 95 de la TVD entre:
  - una muestra aleatoria simple de tamaño n del perfil de la encuesta, y
  - una réplica bootstrap de la encuesta: Poisson por hogar en la ECV, por persona en la EPA y la TIC-H, como en el intervalo de la proporción.

  Se hacen 200 réplicas. El umbral sigue siendo máx(0,08; 1,2 × TVD_ref + 0,002). Las referencias exhaustivas no cambian. La representación (ratio o IC 95 % de la encuesta) tampoco cambia.
- **Evidencia:** `tests/unit/test_auditoria.py`; tabla de umbrales en el informe de F7.
- **Consecuencias:**
  - En España el margen apenas cambia: 0,03-0,04, por debajo del mínimo de 0,08. Por eso sigue en rojo el perfil de actividad de la privación severa (0,085), que es la limitación ya declarada en D-051.4.
  - Por comunidad y provincia, el rojo solo salta cuando la diferencia supera lo que la propia encuesta puede distinguir.
- **Aprobada por:** humano (2026-10-20, D-059).

## D-053 · Inclinación de la ECV por comunidad: limitación grave y privación severa (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F6 (detectado en la auditoría de F7)
- **Estado:** aprobada por el agente. Es una mejora del método de enriquecimiento hacia cifras oficiales y no cambia ningún umbral (docs/06 §4, medida 2: llevar el grupo a una cifra oficial fiable).
- **Contexto:**
  - En la auditoría, la limitación grave sale por debajo del IC 95 % de la ECV en varias comunidades:

    | Comunidad | Población | ECV |
    | --- | --- | --- |
    | Castilla y León | 3,9 % | 4,7 % |
    | Murcia | 3,3 % | 4,0 % |
    | Castilla-La Mancha | 4,4 % | 4,8 % |

  - Lo mismo pasa con la privación severa en Cataluña y en Castilla y León.
  - El 99,5 % de las personas encuentra donante en su propia comunidad, así que no es un problema de geografía.
  - **Causa: composición.** Una llave del bloque es la relación con la actividad.
    - En la población viene de la EPA (D-046, D-050).
    - En la ECV es la que declara cada persona.
    - La población tiene menos «incapacidad permanente» que la ECV (Castilla y León: 1,2 % frente a 2,9 % de los de 16+). Ese grupo tiene un 40 % de limitación grave.
  - Con las tasas de la ECV por celda (edad × actividad) y la composición de la población, se reproduce lo que da la población: Castilla y León 4,0 % y Murcia 3,3 %.
  - La prevalencia regional de estos indicadores es la que publica el INE con la ECV, y la población debe reproducirla.
- **Alternativas consideradas:**
  1. Declararlo como limitación, como en D-048. Se descarta porque existe una cifra oficial a la que llevar la población.
  2. Usar como llave la actividad en tres categorías. Se descarta porque no corrige el paro (OIT frente a declarado) y rompe la asociación entre la incapacidad y la limitación (G6.2).
  3. Un λ fijo por comunidad, estimado con la composición de los objetivos (actividad × edad). Se probó y se descarta: la renta, otra llave, no está en esa composición. En privación, el λ de Aragón salía con el signo contrario, y el error residual llegaba a ±0,5 puntos.
  4. **Elegida:** la misma inclinación que la renta con el Atlas (D-044.5), por comunidad y con las celdas reales de los receptores.
- **Decisión:**
  - **Pesos:** en el bloque personal de la ECV, el donante pesa w · exp(λ₁ · [limitación grave] + λ₂ · [privación severa]).
  - **Estimación de los λ:** en cada comunidad del territorio, los λ se calculan con las celdas de emparejamiento de sus receptores de viviendas familiares (el universo de la ECV). Así, la prevalencia esperada de cada indicador es la de la ECV en esa comunidad. Se resuelven por coordenadas, cada λ por bisección.
  - **Sorteo:** después se sortea con esos pesos.
  - **Trazabilidad:** los λ, la prevalencia sin inclinar y la esperada quedan en la metadata del enriquecimiento (`persona_ecv.inclinacion`).
  - **Poblaciones de una provincia o de una lista de municipios:** reciben la prevalencia de su comunidad, que es también la referencia de la auditoría, porque la ECV no es representativa por provincia. Dentro de una población de comunidad o de España, las provincias conservan sus diferencias de composición.
- **Evidencia:**
  - `tests/unit/test_inclinacion_ecv.py` comprueba la prevalencia sin inclinar, que se alcanzan los dos objetivos a la vez y que el denominador no cuenta los valores desconocidos.
  - En la prueba de Ceuta, la limitación grave pasa de ratio 1,27 a 0,98 y la privación severa queda en 1,00.
- **Consecuencias:** cambian las variables del bloque personal de la ECV (salud, limitación y privación) en todas las poblaciones. Se repiten F6 y F7.

## D-054 · Ampliación de donantes de las celdas de extranjeros (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F4-F5 (detectado en la auditoría de F7)
- **Estado:** aprobada por el agente. Es una medida correctora de docs/06 §4, punto 3 (ampliar los donantes de forma jerárquica) y no cambia ningún umbral.
- **Contexto:**
  - Con D-051, la ampliación propia solo miraba el total de cada nacionalidad.
  - La población extranjera ha crecido mucho desde 2021. Sus celdas de edad (`nacionalidad_edad`, `nacionalidad_top_edad`) y de actividad (`actividad_nacionalidad`) superan entre 1,5 y 4 veces la masa de sus donantes locales.
  - Esas celdas no se ampliaban hasta pasar de 3,5, y la calibración subía al factor máximo a los pocos hogares que tenían.
  - Ejemplo en Cantabria: un hogar paraguayo de 5 personas copiado 8 veces da el 18 % de los paraguayos, y los 5 hogares más usados dan el 41 %.
  - En la cadena con D-051 y D-052 seguía habiendo de 3 a 12 nacionalidades en rojo por concentración en la mayoría de comunidades y provincias.
- **Alternativas consideradas:**
  1. Bajar el factor máximo de la calibración para los hogares extranjeros. Se descarta porque compromete la convergencia.
  2. Declarar la limitación. Se descarta porque hay donantes de otras comunidades parecidas que pueden aportar variedad real.
  3. Aplicar esa ampliación a todos los territorios. Se probó y se descarta. En Teruel y Ceuta, los hogares importados desbordan otras celdas, la calibración solo converge fundiendo todas las nacionalidades en el último recurso y se rompe la representación (Marruecos 0,8, Colombia 0,3).
  4. Ampliar solo nacionalidad × edad. Se probó y se descarta porque casi no mejora: Cantabria pasa de 12 a 11 rojos y Aragón de 4 a 3.
  5. **Elegida:** la regla de D-051 (si el objetivo supera 1,5 veces la masa local, se amplía hasta 1,2) se aplica también a `nacionalidad_edad`, `nacionalidad_top_edad` y `actividad_nacionalidad`, con vuelta atrás:
     - si el bloque no converge, o solo converge fundiendo en el último recurso celdas de nacionalidad (`nacionalidad`, `nacionalidad_top`, `nacionalidad_top_edad`) o de actividad (`actividad_tramo`, `actividad_nacionalidad`), se calibra sin esta ampliación;
     - en la primera cadena, Aragón convergía con la ampliación, pero fundiendo inactivos con ocupados de 35-44 años. Se perdía el control de su tasa de actividad, lo que es peor que la concentración que se gana;
     - la metadata de la calibración registra `ampliacion_extranjeros` y las fusiones de último recurso.
- **Prueba en la copia aislada** (concentración de las nacionalidades):

  | Población | Rojos antes | Rojos después | Ampliación aplicada |
  | --- | --- | --- | --- |
  | Aragón | 4 | 1 | sí |
  | Cantabria | 12 | 7 | sí |
  | Teruel | 12 | 12 | no (idéntica a la línea base) |
  | Ceuta | — | — | no |

  - Sube el número de grupos en ámbar por más del 50 % de donantes no locales. Es la señal prevista: se declara, no bloquea.
- **Prueba descartada:** calibrar el total de cada nacionalidad desde 5 personas en lugar de 100, para controlar las nacionalidades diminutas de Ceuta, Melilla y Teruel.
  - En Ceuta no lo resuelve: con pocos o ningún donante, un único hogar ucraniano importado daba 4,2 veces el objetivo.
  - Se mantiene el umbral de 100 y no se abre decisión propia.
- **Consecuencias:** cambian las calibraciones de todos los territorios salvo las listas de municipios, que siguen la excepción de D-051. Se repiten F4-F7.

## D-056 · V-MARG en N = 10.000: un fallo aislado por azar (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F4 (serie repetida con D-053 y D-054)
- **Estado:** aprobada por la persona responsable el 2026-10-20 (D-059). Aplicada en `thresholds.yaml` (`V-MARG.poblaciones_fallo_min`) y en la puerta G4.1.
- **Contexto:** G4.1 falla en 1 de 8.480 comprobaciones.
  - Es el tipo de residencia (vivienda familiar o colectivo) de Navarra en la población de España de 10.000 personas con semilla 1.
  - Navarra tiene allí 139 personas: TVD 0,0208 frente a un umbral de 0,0183, unas 3 personas de diferencia en colectivos.
  - El mismo indicador queda muy por dentro del umbral en las otras 4 semillas de N = 10.000 (TVD de 0,0007 a 0,008) y en las 20 poblaciones de 50.000 a 1.000.000 (TVD ≤ 0,0021, con umbrales de 0,0036 a 0,0098).
  - Detalle en `reports/fase_04/*_v_marg.csv`.
- **Por qué es azar:** el umbral, 1,2 × el percentil 95 de TVD_ref + 0,002, deja una probabilidad pequeña pero no nula de fallo por celda. Con 8.480 comprobaciones, un fallo aislado en la población más pequeña es esperable. El patrón no es sistemático: no se repite en otra semilla ni en otro tamaño.
- **Propuesta** (como D-047 para V-SEMILLAS y D-039 para V-CRUCE): una marginal solo falla V-MARG en la serie de F4 si queda fuera del umbral en dos o más poblaciones de la serie (semillas o tamaños). El resultado estricto se informa siempre.
- **Alternativas:**
  1. Repetir la semilla 1 con otra semilla. Se descarta porque elegir la semilla hasta que pase sería manipular el resultado.
  2. Aceptar el fallo como limitación declarada.
- **Aprobada por:** humano (2026-10-20, D-059).

## D-057 · Tamaño de municipio de los hogares añadidos desde otra provincia (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F4-F7 (detectado en G7.2 tras D-054)
- **Estado:** aprobada por el agente. Corrige un defecto del código y la referencia de una prueba; no cambia ningún umbral.
- **Contexto:**
  - Los hogares añadidos desde otra provincia (ampliación de donantes) no conservan su tamaño de municipio de origen, que puede no existir en el destino.
  - Hasta ahora todos recibían la clase más frecuente entre los donantes locales de su provincia y grado de urbanización.
  - Con más hogares añadidos (D-054), los grupos perdían variedad en este atributo y G7.2 bajaba:

    | Población | Grupos dentro (antes de D-054) | Grupos dentro (con D-054) |
    | --- | --- | --- |
    | España | 99 % | 89 % |
    | Baleares | 100 % | 50 % |
    | Murcia | 100 % | 58 % |

  - Además, la referencia de V-DIVERSIDAD usaba el tamaño de municipio de origen de esos donantes. En Ceuta, con un solo municipio, el ratio salía 0/0 y el atributo fallaba en todas las rondas.
- **Decisión:**
  1. Cada hogar añadido recibe una clase de tamaño de municipio sorteada, con semilla, con la distribución ponderada de los donantes locales de su provincia y grado de urbanización. Se sigue marcando como `modelada`. Es un objetivo reservado (no calibrado), así que la calibración no cambia.
  2. En V-DIVERSIDAD, la entropía de referencia del tamaño de municipio se calcula con los donantes del propio territorio, que son los que conservan su clase. El resto de atributos no cambia.
- **Consecuencias:** se repiten F4-F7. Las calibraciones no cambian, porque `poblacion.py` no forma parte de sus entradas.

## D-058 · Calibrar el sexo de cada nacionalidad principal (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F3-F7 (detectado en la auditoría de F7)
- **Estado:** aprobada por el agente. Medida correctora de docs/06 §4, punto 2: llevar un grupo a una cifra oficial fiable. No cambia ningún umbral.
- **Contexto:**
  - En la población nacional, el perfil por sexo de los paraguayos sale en rojo: 69,3 % de mujeres frente al 61,3 % del Censo Anual exhaustivo 2025 (TVD 0,080).
  - Los hondureños tienen 69,3 % frente a 63,9 %. El resto de nacionalidades principales queda dentro de ±2,4 puntos.
  - La causa son los donantes de 2021, más feminizados que la migración reciente. El sexo dentro de cada nacionalidad no se calibraba: solo estaba en el objetivo reservado `nacionalidad_top_sexo_edad`.
- **Alternativas consideradas:**
  1. Pasar a calibrado todo `nacionalidad_top_sexo_edad`. Se descarta: son 160 celdas por bloque, que no tienen solución en los territorios pequeños, y se perdería el objetivo de validación.
  2. Declarar la limitación. Se descarta porque existe la cifra oficial.
  3. **Elegida:** un objetivo calibrado nuevo, `nacionalidad_top_sexo`, de la misma fuente que `nacionalidad_top_edad`, con las mismas reglas de fusión. Se refactorizan en `_fundir_cruce_nacionalidad`:
     - una nacionalidad con menos de 200 personas en el bloque queda en una sola celda (`sexo=todas`). Es un umbral propio, más bajo que el de la edad (2.000), porque el sexo son 2 celdas y no 5;
     - las nacionalidades fundidas y las celdas de menos de 100 personas pasan a otras_extranjeras del mismo sexo;
     - el último recurso puede soltar el sexo igual que la edad.
- **Evidencia:**
  - `tests/unit/test_fusion_sexo.py`.
  - En la prueba de la copia aislada convergen Aragón, Madrid y Teruel. En Aragón, el perfil por sexo de los paraguayos pasa de una TVD de 0,135 a 0,013.
  - `nacionalidad_top_sexo_edad` sigue reservado para validar.
- **Consecuencias:** cambian los objetivos de F3 y todas las calibraciones. Se repiten F3-F7.
- **Efecto en G6.1 (pendiente de decisión humana):**
  - Con D-058, la tenencia de la vivienda, ya aceptada como limitación regional en D-048, pasa de una TVD de 0,0189 a 0,0206 con la composición de la encuesta. El criterio de aceptación de D-048 es ≤ 0,02, así que G6.1 queda fallida en estricto por 0,0006.
  - La causa: la tenencia de los hogares con algún adulto extranjero sale de la ECV (D-045), y calibrar el sexo de las nacionalidades cambia algo la composición de esos hogares.
  - No se relaja el umbral. Se pide decidir entre:
    1. aceptar la tenencia como limitación con esa TVD;
    2. volver a la versión sin D-058 (commit `b9ec7a2`), que supera G6.1 pero deja el sexo de paraguayos y hondureños desviado (+8 y +5,5 puntos de mujeres).

## D-059 · Revisión humana de F7: decisiones aprobadas (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F7 (G7.7)
- **Estado:** aprobada por la persona responsable el 2026-10-20. Aceptó las recomendaciones del agente («Venga. Adelante»).
- **Decisiones:**
  1. **D-049 y D-050**, aprobadas.
  2. **D-052** (umbral de perfil con el error de muestreo de la encuesta de referencia), aprobada.
  3. **D-056** (un fallo aislado de V-MARG en la serie de F4 es azar si no se repite en otra población), aprobada.
     - Aplicada en `thresholds.yaml` (`V-MARG.poblaciones_fallo_min: 2`) y en G4.1.
     - El resultado estricto se informa siempre.
  4. **Se mantiene D-058** (sexo de las nacionalidades calibrado) y la tenencia de la vivienda se acepta como limitación con su TVD ajustada de 0,0206.
     - Aplicado en `V-ENRIQ-MARG.tvd_ajustada_max` y en G6.1.
  5. **Fallos aceptados como limitación declarada** en G7.1, G7.3 y G7.4. Aplicado en `V-MINORIAS.limitaciones` y `nacionalidades_territoriales`; el estricto se informa siempre.
     - Las nacionalidades minoritarias en las poblaciones de comunidades, provincias y municipios. Causa: muestra del 10 % del Censo 2021; en Ceuta y Melilla, además, la población de prueba es mayor que la real.
     - La carencia material severa (perfil de actividad) y las personas que nunca usan internet (representación), en cualquier población (D-051).
  6. **Propuesta del agente para F5 y siguientes, aceptada:** el tamaño por defecto de la población de un territorio no debe superar su población real. Generar Ceuta o Melilla con 100.000 personas solo multiplica las copias de los donantes. Se aplicará cuando se repita la serie de F5.
- **Lo que no cubre esta aprobación:**
  - Los fallos de G7 fuera de esas categorías: municipios de menos de 2.000 habitantes en Canarias y Madrid, jóvenes ni-ni en seis poblaciones, y nacidos fuera con nacionalidad española y «sin estudios» en Soria.
  - El agente los investiga antes de cerrar F7.

## D-060 · Estudiantes e «otra inactividad» en los cruces fundidos (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F4-F7 (detectado al investigar los fallos de G7 que no cubre D-059)
- **Estado:** aprobada por el agente. Corrige un sesgo de los datos de entrada que la calibración no podía resolver; no cambia ningún umbral.
- **Contexto:**
  - Los jóvenes ni-ni salen por encima de la EPA en varias poblaciones: Madrid 11,7 % frente a 9,1 % (ratio 1,28); también Castilla y León, Valencia urbano y Soria.
  - **Causa:**
    - Entre los inactivos de 20-24 años, el Censo 2021 (enero de 2021, de registros) tiene un 41 % en «otra situación»; la EPA del 2T 2026, un 16 %.
    - Cuando la calibración no puede separar estudiante y «otra inactividad» (D-050), funde las dos categorías del cruce y solo calibra su total.
    - Así, las personas conservan la categoría del Censo: en Madrid, 27,9 % de estudiantes de 20-24 frente al 33,8 % del objetivo, y 12,8 % de «otra inactividad» frente al 6,6 %.
    - El enriquecimiento da «no cursa formación» a casi todos los de «otra inactividad», y eso infla los ni-ni.
  - El Censo no permite reclasificar en origen: todos sus inactivos que cursan estudios (`ESCUR`) ya son estudiantes.
- **Alternativas consideradas:**
  1. Quitar la fusión. Se descarta porque la calibración acotada no tiene solución en esos cruces.
  2. Declarar la limitación. Se descarta porque existe la cifra oficial (EPA).
  3. **Elegida:** reparto posterior a la calibración.
- **Decisión:** en cada bloque y cruce sexo × tramo de edad con estudiante fundido en «otra inactividad», el total de las dos categorías se reparte con las proporciones del objetivo de la EPA.
  - Se mueven personas al azar, con la semilla, de la categoría que sobra a la que falta.
  - Su `relacion_actividad__calidad` pasa a `modelada`.
  - La calibración no cambia (`repartir_inactividad` en `poblacion.py`).
  - Solo se mueve a personas cuyo perfil P0 con la categoría nueva (persona y, en viviendas familiares, persona y hogar) existe en algún donante del Censo. En la primera vuelta sin esta condición, V-RAREZA detectó 110 personas con perfiles sin donante en la población nacional.
- **Evidencia:**
  - `tests/unit/test_repartir_inactividad.py`.
  - Madrid, 100.000 personas: 20-24 con 33,8 % de estudiantes y 6,9 % de «otra inactividad»; ni-ni 8,5 %; 1.132 personas modeladas (1,1 %).
- **Consecuencias:** se repiten F4-F7. Las calibraciones no cambian.

## D-061 · Excepciones concretas aceptadas en G7 (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F7 (G7.7)
- **Estado:** aprobada por la persona responsable el 2026-10-20 («Acepto ambos puntos»).
- **Decisiones:** se aceptan como limitación declarada, solo en estos territorios. Aplicado en `V-MINORIAS.excepciones` y en G7.1-G7.4; el resultado estricto se informa siempre.
  1. **Municipios de menos de 2.000 habitantes en Canarias y Madrid** (CCAA:05, CCAA:13 y PROV:28, que es la misma comunidad uniprovincial).
     - Canarias: 0,75 % de la población frente al 0,47 % del Padrón 2025, unas 6.000 personas. Madrid: 0,77 % frente al 0,68 %.
     - Los donantes traen la clase de tamaño de municipio del Censo 2021, y varios municipios cercanos a 2.000 habitantes han cambiado de clase.
     - Es un objetivo reservado (de validación), no calibrado.
  2. **Soria (PROV:42):**
     - Perfil de edad de los nacidos fuera con nacionalidad española: TVD 0,09 frente a 0,08.
     - Concentración de donantes en «sin estudios».
     - La causa es la misma que la de las nacionalidades en territorios pequeños: con 50.000 personas sobre unos 90.000 habitantes, cada donante se copia unas 5,5 veces.

## D-062 · Últimas excepciones aceptadas en G7 y aprobación de F7 (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F7 (G7.7)
- **Estado:** aprobada por la persona responsable el 2026-10-20 («Apruebo todas las recomendaciones»).
- **Contexto:** con D-060, los fallos de G7 que no cubrían D-059 y D-061 quedan en 7 casos.
- **Decisiones:** se aceptan como limitación declarada, por territorio y grupo, en `V-MINORIAS.excepciones`; el resultado estricto se informa siempre.
  1. **Concentración de donantes de los jóvenes ni-ni** en Soria, Teruel y la lista de municipios rurales de Teruel. Cada donante se copia entre 3,7 y 5,5 veces, la misma causa que las nacionalidades en territorios pequeños.
  2. **Perfil por edad de la limitación grave** en Castilla y León (TVD 0,116 frente a 0,114) y Soria (0,131 frente a 0,113), con la representación en 1,00 y 1,03.
  3. **Perfil por estudios de los jóvenes ni-ni** en Almería: 0,152 frente a 0,143.
  4. **Jóvenes ni-ni en la lista de municipios de Valencia urbano**: 13,3 % frente al 10,4 % de la referencia. La referencia es la EPA de toda la Comunidad Valenciana, que no es representativa por municipio. Se declara expresamente en la ficha.

### Aprobación de F7

- **Estado:** aprobada por la persona responsable el 2026-10-20. Aprueba la población con las limitaciones declaradas (D-059, D-061 y D-062) y las decisiones D-049 a D-062.

## D-063 · Capa de opinión: datos del CIS, armonización y variables de valores (2026-10-20)

- **Fecha:** 2026-10-20
- **Fase:** F8A
- **Estado:** aprobada por el agente (la persona responsable delegó las decisiones de esta noche; los umbrales no se tocan y la puerta G8A.7 queda para revisión humana).
- **Datos:**
  - **Descarga:** la web del CIS limita las peticiones y corta conexiones. `tools/descargar_cis.py` va despacio y guarda en caché las fichas.
    - La paginación del catálogo cae en una comprobación anti-bots, así que los barómetros se leen directamente de su ficha (`/en/surveys/barometro-de-<mes>-<año>`).
    - Los estudios con trabajo de campo desde el 01/07/2026 van a `data/eval/cis/` (regla 5).
  - **Universo:** los barómetros del CIS entrevistan a personas de **nacionalidad española** de 18 años y más (en el 3567, el 100 % de la muestra).
- **Armonización** (`opinion/cis.py`):
  - Todo se recodifica **por la etiqueta** de valor del fichero SPSS, nunca por el código, y una etiqueta no prevista detiene el proceso.
  - El CIS numera las comunidades por orden alfabético (7 = Castilla-La Mancha, 8 = Castilla y León) y el INE al revés.
  - Las clases de tamaño de municipio del CIS cortan en 400.000; la población usa las del Padrón. Se comparan en cinco clases comunes (hasta 2.000, 2.001-10.000, 10.001-50.000, 50.001-100.000 y más de 100.000).
  - Estudios: la «F.P.» sin nivel se precisa con `NIVELESTENTREV` (grado medio → secundaria 2.ª etapa; grado superior → superior).
  - «No sabe» y «No contesta» se conservan como categorías (regla 10).
  - **Clase subjetiva** (`CLASESOCIAL`, respuesta espontánea codificada por el CIS): proletariado → obrera; pobre, infraclase, «los de abajo», excluidos y clase baja → baja. Se añaden «otras» y «no cree en las clases», que son respuestas reales, al dominio de `variables.yaml`.
- **Modelo** (`opinion/valores.py`):
  - Para cada variable, una regresión logística multinomial ponderada con el peso del CIS (normalizado por estudio).
  - Predictores: sexo, grupo de edad, estudios, actividad, comunidad y tamaño de municipio.
  - Se ajusta con los barómetros de los 12 meses anteriores al corte.
  - A cada adulto sintético se le asigna una extracción aleatoria de su distribución predicha, con la semilla (docs/03 §2.4: no la media).
- **Calidad y limitación:**
  - Los extranjeros y los residentes en colectivos, fuera del universo del CIS, reciben la predicción con su perfil y se marcan `extrapolada`; el resto, `modelada`.
  - Limitación declarada: en los extranjeros, el modelo de los españoles infravalora previsiblemente «otra religión», y no hay fuente oficial para corregirlo.
- **Dependencias nuevas:** `pyreadstat`, `scikit-learn` y `statsmodels`. `semopy` no compila en el entorno; el análisis factorial confirmatorio de V-LATENTE se programa con `scipy`.

## D-064 · Capa de opinión: modelo MRP, universos y validación (2026-10-21)

- **Fecha:** 2026-10-21
- **Fase:** F8A
- **Estado:** aprobada por el agente (decisiones delegadas para esta noche; ningún umbral cambia; G8A.7 queda para revisión humana).
- **Datos:** 39 estudios del CIS anteriores al corte (37 barómetros mensuales de enero de 2023 a junio de 2026 y las oleadas del Barómetro Sanitario de noviembre de 2025 y marzo de 2026), 154.838 encuestados. Los tres barómetros posteriores al corte (julio, septiembre y octubre de 2026) están en `data/eval/cis/` y no se leen. No hay ficha de barómetro en junio ni en septiembre de 2023 (tampoco en agosto, que no se hace).
- **Universos:**
  - Los barómetros mensuales solo entrevistan a personas de nacionalidad española: ningún extranjero en los estudios que traen la variable.
  - El Barómetro Sanitario entrevista también a extranjeros (128 y 170 en sus dos oleadas).
  - Los modelos de valores y rasgos se ajustan solo con españoles, porque no llevan la nacionalidad como predictor. Los extranjeros sintéticos siguen marcados `extrapolada` (D-063).
  - En G8A.5 la población sintética que responde son todos los adultos en vivienda familiar, el universo del Sanitario.
- **Modelo (al estilo MRP):**
  - Al modelo aditivo se le añade la interacción comunidad × edad en cuatro grupos.
  - Sin ella, religiosidad quedaba en el 89,5 % de celdas en el IC, por debajo del umbral del 90 %. Los fallos se repartían por todas las categorías: es el efecto de la edad propio de cada comunidad, que el modelo aditivo no recoge.
  - La regularización se elige por validación cruzada (3 particiones fijas, log-verosimilitud ponderada; rejilla C ∈ {0,01; 0,03; 0,1; 0,3; 1}). Así el modelo se encoge hacia efectos simples cuando hay pocos encuestados por celda.
  - Alternativa considerada: un modelo multinivel bayesiano (PyMC). Se descarta por coste y por reproducibilidad bit a bit; la regresión penalizada es su aproximación estándar.
- **Rasgos continuos:**
  - Los residuos reales se sortean dentro de la celda edad × estudios × sexo. Antes se sorteaban por edad × estudios, y la varianza dentro de los grupos por sexo salía 0,78-1,39 frente al CIS.
  - La regularización de la regresión de los rasgos también se elige por validación cruzada (RidgeCV).
- **V-OPINION-CV (G8A.2):**
  - Se toma una versión por pregunta: la lista de opciones que aparece en más estudios. Los problemas codificados cambian de lista con el tiempo y cada lista cuenta como pregunta distinta en el banco.
  - Se excluyen las preguntas políticas (ministros, líderes, voto), las técnicas y las de perfil (nacionalidad, edad, sexo).
- **G8A.5 (Barómetro Sanitario):**
  - La oleada de contraste es la última del Sanitario anterior al corte (marzo de 2026).
  - Cada pregunta se ajusta con los estudios de los 12 meses previos que tienen la misma pregunta (variable, enunciado y opciones).
  - Se informa la TVD por comunidad frente a tres referencias: B0 (distribución nacional previa), B1 (distribución directa previa de la comunidad) y el ruido muestral de la oleada de contraste.
  - Con una sola oleada de ajuste y la interacción sin regularizar, el modelo quedaba peor que B0 (0,085 frente a 0,078). Con la regularización por validación cruzada y los barómetros cuando comparten pregunta, mejora a B0 y a B1.
- **Pesos:** se usa `PESO` (ponderación con ajuste por estudios), normalizado a media 1 por estudio. `PESOCCAA` es la ponderación autonómica sin el ajuste por estudios. Dentro de una comunidad, `PESO` corrige además la composición por estudios.

## D-065 · Rasgos latentes de F8A y huecos de la lista de rasgos (2026-10-21)

- **Fecha:** 2026-10-21
- **Fase:** F8A
- **Estado:** aprobada por el agente (decisiones delegadas; G8A.7 queda para revisión humana).
- **Estudios temáticos descargados** (todos anteriores al corte):
  - 3535, Tendencias sociales V (noviembre de 2025).
  - 3534, Miedos e incertidumbres (noviembre de 2025).
  - 3554, Temores en la sociedad actual (marzo de 2026).
  - 3563, Desinformación y humor (mayo de 2026).
  - Postelectorales autonómicos: 3541 (Extremadura), 3548 (Aragón), 3550 (Castilla y León) y 3566 (Andalucía).
  - 3569, Índice de Confianza del Consumidor de junio de 2026.
- **Estudios descartados o restringidos:**
  - **Índice de Confianza del Consumidor (3569):** no se usa. No lleva el perfil estándar del CIS (sexo y edad están en P19 y P20, no en SEXO y EDAD), y sus ítems son expectativas económicas, no actitudes. Queda descargado para una armonización propia si hace falta.
  - **Postelectorales autonómicos:** entrevistan a una sola comunidad. No entran en los modelos nacionales de valores y rasgos ni en V-OPINION-CV, porque sobrerrepresentarían su comunidad. Se usarán en F8B (recuerdo de voto autonómico, eje territorial).
  - **Peso del estudio 3550:** no trae `PESO` sino `PESO1` («Ponderación con ajuste por Estudios»); se usa ese.
- **Rasgos construidos** (`configs/rasgos.yaml`). Factorial confirmatorio de un factor por rasgo, máxima verosimilitud sobre la correlación de Pearson ponderada:
  - **`rasgo_confianza_institucional`** (3535, P.4, escala 1-10):
    - Ítems: medios de comunicación, Justicia, Constitución, Tribunal Constitucional y organizaciones empresariales. CFI 0,995, RMSEA 0,038, omega 0,80.
    - Con los nueve ítems el modelo de un factor no ajusta (CFI 0,67): partidos, sindicatos, Gobierno y Parlamento forman un factor partidista, que es la desafección de la capa política (F8B).
  - **`rasgo_sensibilidad_precio`** (3554, P.2 y P.2A, miedo de 0 a 10):
    - Ítems: que el trabajo o la pensión no permitan vivir con dignidad, perder el trabajo, no poder pagar la vivienda y una crisis económica. CFI 0,997, RMSEA 0,048, omega 0,82.
    - Es un indicador de la presión del coste de vida; no hay en los estudios disponibles una batería del peso del precio en las decisiones de compra.
  - **`rasgo_aislamiento_social`** (3554):
    - Ítems: temor a la soledad, a no tener a quien amar y a quedarse sin apoyo emocional. Omega 0,74.
    - El ítem «tiene con quién hablar de sus preocupaciones» no carga en el factor (0,04) y se descarta. Es un rasgo de **temor** a la soledad, no una medida de la red social real.
    - Con tres ítems el modelo propio tiene 0 grados de libertad. Su ajuste se contrasta en el factorial conjunto con la sensibilidad al precio: 13 grados de libertad, CFI 0,987, RMSEA 0,049, correlación entre factores 0,58 (rasgos distintos).
- **Huecos (rasgos de la lista de docs/02 §3.4 que no se construyen):**
  - **`rasgo_confianza_tecnologia` y `rasgo_preocupacion_ambiental`:** en los estudios disponibles solo hay ítems sueltos (miedo al control por las nuevas tecnologías, miedo al deterioro ambiental) o expectativas de desarrollo tecnológico, no actitudes. Propuesta: estudios temáticos del CIS sobre inteligencia artificial y sobre medio ambiente anteriores al corte, cuya ficha no se ha podido localizar porque la paginación del catálogo cae en la comprobación anti-bots; o el módulo de cambio climático de la ESS.
  - **`rasgo_confianza_interpersonal` y `rasgo_tradicion_apertura` (ESS):** la ESS requiere registro. Está anotada en `data/raw/MANUAL_DOWNLOADS.md` (ronda 11) y pendiente de descarga manual.
  - **`estilo_aquiescencia`:** necesita baterías equilibradas de acuerdo y desacuerdo con ítems invertidos, que no hay en estos estudios.
  - **`identidad_territorial` y `lengua_habitual`:** los barómetros nacionales de 2023-2026 no preguntan la escala Linz-Moreno ni la lengua, y los postelectorales autonómicos solo cubren cuatro comunidades. Propuesta: estudios autonómicos o de los centros autonómicos (CEO, Euskobarómetro, etc.) para las comunidades con lengua cooficial.
  - **`medio_informacion_principal`:** no está en los barómetros descargados.
  - Ningún hueco se rellena con suposiciones (CLAUDE.md, regla 3).

### Aprobación de F8A

- **Estado:** aprobada por la persona responsable el 2026-10-21. Aprueba la capa de opinión, los tres rasgos construidos y las decisiones D-063 a D-065, incluido que la confianza en partidos, sindicatos, Gobierno y Parlamento pase a `rasgo_desafeccion` (F8B).
- **Encargo adicional:** completar los rasgos y variables de docs/02 §3.4 que quedaron como huecos (D-065) con las fuentes pertinentes, y después pasar a F8B. Se registra en D-066.

## D-066 · Huecos de F8A completados: lengua, medios, identidad, tecnología, ambiente y ESS (2026-10-21)

- **Fecha:** 2026-10-21
- **Fase:** F8A (encargo de la persona responsable al aprobar F8A)
- **Estado:** aprobada por el agente; la excepción de omega de `rasgo_tradicion_apertura`, aprobada por la persona responsable.
- **Fuentes nuevas** (todas anteriores al corte):
  - **INE, ECEPOV 2021:** microdatos públicos, 424.493 personas.
  - **CIS:**
    - 3495, Inteligencia artificial (febrero de 2025);
    - 3511, Audiencias de medios II (mayo de 2025);
    - 3402, Preelectoral municipales y autonómicas 2023;
    - postelectorales de Galicia (3446), País Vasco (3459) y Cataluña (3464) de 2024;
    - estudios de campaña 3442, 3451 y 3456.
  - **ESS ronda 11, edición 4.2:** descargada a mano por la persona responsable.
- **Incidente con la ESS:**
  - El fichero de la ESS se subió al repositorio, que es **público**, en el commit `4ba7b79`. Eso incumplía la regla 8 y las condiciones de la ESS, que prohíben redistribuir los datos.
  - Con la aprobación de la persona responsable, se reescribió el historial de la rama hasta `4d37770` (push forzado) y el fichero queda solo en local, en `data/raw/ess/ESS11/`.
  - GitHub puede conservar una copia en caché del commit huérfano hasta que su soporte la purgue.
- **Corrección de la armonización del CIS:**
  - En muchos estudios la nacionalidad no está en `NACIONALIDAD`, sino en la `P0` de filtro («Nacionalidad de la persona entrevistada»). Ahora se lee de ahí.
  - Los barómetros siguen siendo 100 % españoles, como se suponía en D-063 y D-064.
  - El estudio de Temores (3554) tenía 317 extranjeros que se trataban como españoles; ya se excluyen de sus rasgos.
- **Estudios nacionales:**
  - Para los modelos nacionales se excluyen los preelectorales y postelectorales, aunque cubran varias comunidades.
  - El 3402 entrevista a 12 comunidades con muestras desproporcionadas; se excluye por la misma razón.
- **`lengua_habitual` (ECEPOV 2021):**
  - La lengua más usada **en familia**. Castellano y cooficial empatadas → `bilingue`. Las lenguas se clasifican por su nombre en el fichero.
  - Modelo multinomial con sexo, edad, estudios, actividad, provincia × edad, tamaño de municipio, nacionalidad y país de nacimiento (agrupado con la tabla del Censo 2021: los códigos INE de país coinciden).
  - **Validación:** la ECEPOV es de 2021, y la población adulta nacida fuera de España pasó del 16 % al 21 %. G8A.4 compara con la ECEPOV reponderada a la composición sintética por comunidad × edad × país de nacimiento.
    - Sin reponderar: 78,7 % de celdas en el IC.
    - Reponderada: 91,4 % de celdas en el IC y TVD nacional 0,004.
  - La ECEPOV cubre a todas las nacionalidades: solo los residentes en colectivos son `extrapolada`.
- **`medio_informacion_principal` (CIS 3511):**
  - No se pregunta un medio «principal». Se toma el de mayor frecuencia de uso para informarse (de 5, a diario, a 2, de vez en cuando; mencionado sin frecuencia = 1).
  - Los empates reparten el peso del encuestado.
  - Se añade la categoría `ninguno`.
- **`identidad_territorial` (Linz-Moreno):**
  - Se recodifica por patrón de la etiqueta, independiente del gentilicio.
  - Hay un modelo por comunidad con los encuestados de esa comunidad.
  - Disponible en Andalucía, Aragón, Castilla y León, Cataluña, Galicia y País Vasco, más las que aporte el estudio nacional 3409 (Identidades culturales, nacionales y europeas, 2023) si se completa su descarga.
  - En las comunidades sin datos la variable queda vacía; no se inventa.
- **Rasgos nuevos:**
  - **`rasgo_confianza_tecnologia`** (3495, P.3, asociación 1-10 de los avances tecnológicos con progreso, riqueza, eficacia y bienestar): CFI 0,999, RMSEA 0,020, omega 0,76.
    - La media de «Progreso» reproduce la publicada por el CIS: 7,68 frente a 7,67.
    - La batería de comodidad con la IA del Barómetro Sanitario no ajusta (RMSEA 0,18-0,20).
    - La de beneficios de la IA (3495, P.14) solo la contesta quien conoce la IA.
  - **`rasgo_preocupacion_ambiental`** (3489): preocupación por el cambio climático, importancia de las medidas, más recursos públicos y atribución de la DANA al cambio climático. CFI 0,991, RMSEA 0,059, omega 0,71.
  - **`rasgo_confianza_interpersonal`** (ESS: ppltrst, pplfair, pplhlp): omega 0,70. El factorial conjunto de la ESS da CFI 0,960 y RMSEA 0,045.
  - **`rasgo_tradicion_apertura`** (ESS): polo de conservación de Schwartz (seguridad, conformidad y tradición, 6 ítems). CFI 0,943, RMSEA 0,069, **omega 0,68**.
    - La versión bipolar centrada en la media individual ajusta peor (CFI 0,81).
    - **Excepción aprobada** por la persona responsable (`thresholds.yaml`, `V-LATENTE.excepciones_omega`); el umbral general no cambia.
  - **`estilo_aquiescencia`** (ESS): media de los 21 ítems de valores de Schwartz (MRAT), con al menos 16 respondidos. Es un estilo de respuesta, como `estilo_ns_nc`, y no pasa por el análisis factorial.
  - Los rasgos de la ESS se modelan con sexo, edad, estudios, actividad, comunidad y nacionalidad. La ESS no trae el tamaño de municipio en clases comparables. Los extranjeros son `modelada`, porque la ESS los entrevista.
