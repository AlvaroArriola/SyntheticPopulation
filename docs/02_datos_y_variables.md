# 02 · Datos y variables

**Este es el documento más importante del proyecto.** La fidelidad de la población depende de qué fuentes se usan, para qué y con qué variables. Todo lo demás se construye encima.

> **Aviso para el agente:** las fuentes, ediciones, variables y niveles geográficos de este documento son el plan de partida. Cada uno se **verifica** en la fase 1 contra la documentación oficial vigente (diseño de registro, metodología, cuestionario). Donde este documento dice «verificar», no hay que darlo por cierto. Cualquier diferencia se registra en `DECISIONS.md` y se actualiza este documento.

## 1. Arquitectura de datos por capas

| Capa | Pregunta que responde | Tipo de fuente | Uso |
| --- | --- | --- | --- |
| **A. Verdad de referencia** | ¿Cuánta gente hay de cada tipo en cada territorio? | Registros y censos: Padrón, Censo Anual de Población, Censo 2021 (tablas) | Objetivos de calibración y validación |
| **B. Donantes** | ¿Qué combinaciones reales de atributos existen, persona a persona y hogar a hogar? | Microdatos del Censo 2021 y del Censo Anual | Base de las personas sintéticas |
| **C. Enriquecimiento** | ¿Qué más sabemos de personas con ese perfil (renta, uso digital, salud, actitudes, política)? | Microdatos de encuestas: ECV, EPA, TIC-H, EPF, encuestas de salud, CIS, ESS | Atributos añadidos por emparejamiento o modelo |
| **A-POL. Verdad electoral** | ¿Qué votó realmente cada territorio? | Resultados electorales oficiales y censo electoral | Calibración y validación de la capa política |

Regla de prioridad: **ante un conflicto entre fuentes, manda la de mayor cobertura y calidad para esa variable**: registro o censo antes que encuesta, encuesta grande antes que pequeña, dato más reciente antes que antiguo. Cada conflicto se registra.

## 2. Catálogo de fuentes

### 2.1 Capa A · Verdad de referencia

| Fuente | Organismo | Qué aporta | Nivel geográfico | Notas y verificaciones |
| --- | --- | --- | --- | --- |
| Estadística del Padrón Continuo | INE | Población por edad, sexo y nacionalidad o país de nacimiento | Municipio | Fecha de referencia 1 de enero. Usar la más reciente publicada |
| Censo Anual de Población (tablas y microdatos) | INE | Población por edad, sexo, nacionalidad, estado civil, nivel de estudios, relación con la actividad, ocupación, año de llegada… | Varía según variable (verificar) | Según el INE, el fichero de microdatos **solo con variables demográficas es exhaustivo** (toda la población) y el de **todas las variables censales es una muestra del 10 %**. El INE añadió el grado de urbanización a los ficheros demográficos el 29/04/2026. Ediciones por bloque: estudios y actividad 2021–2024, ocupación 2021–2023, llegada y residencia anterior 2021–2025, estado civil 2021–2024 (verificar las vigentes) |
| Censo de Población y Viviendas 2021 (tablas) | INE | Hogares por tipo y tamaño, viviendas, tenencia, población en establecimientos colectivos | Municipio y sección censal para muchas tablas | Base para estructura de hogares y vivienda |
| Atlas de Distribución de Renta de los Hogares | INE (estadística experimental) | Renta media por persona y hogar, fuentes de ingreso, indicadores de desigualdad | Municipio, distrito y sección censal | Contexto socioeconómico local y calibración de renta. Verificar el último año disponible |
| Indicadores urbanos y grado de urbanización | INE y Eurostat (DEGURBA) | Clasificación rural, intermedio, urbano | Municipio | Usar la clasificación que traen los microdatos censales para no mezclar criterios |

### 2.2 Capa B · Donantes

| Fuente | Qué contiene | Uso | Notas y verificaciones |
| --- | --- | --- | --- |
| Censo 2021, microdatos de personas y hogares | Muestra del **10 % de los hogares**, con todas sus personas. El INE añadió el grado de urbanización el 17/06/2026 | **Donante principal:** conserva la estructura completa del hogar | Verificar: nivel geográfico disponible en el fichero nacional (en el Censo 2011, el fichero nacional suprimía provincia y municipio por confidencialidad y existían ficheros provinciales); cobertura de la **población en establecimientos colectivos** (residencias, que la muestra de hogares podría no incluir) |
| Censo Anual de Población, microdatos de todas las variables (muestra del 10 %) | Variables censales actualizadas | Actualizar la distribución de estudios, actividad y ocupación respecto a 2021 | Verificar si permite reconstruir hogares o solo personas |
| Censo 2021, microdatos de viviendas (muestra del 10 %) | Características de la vivienda | Atributos de vivienda por emparejamiento con el hogar | Muestra independiente de la de hogares |

### 2.3 Capa C · Enriquecimiento

| Fuente | Qué aporta | Universo y notas |
| --- | --- | --- |
| Encuesta de Condiciones de Vida (ECV), INE | Renta del hogar, privación material, dificultades para llegar a fin de mes, tenencia y gastos de vivienda, salud autopercibida | Unos 30.000 hogares (verificar). Desagregación por CCAA |
| Encuesta de Población Activa (EPA), INE | Situación laboral detallada, jornada, temporalidad, teletrabajo, sector | Trimestral, muestra grande. Útil para actualizar el empleo al trimestre de referencia |
| Encuesta TIC en Hogares (TIC-H), INE | Uso de internet, comercio electrónico, competencias digitales, uso de servicios digitales | Núcleo de 16 a 74 años (verificar si las ediciones recientes amplían a mayores de 74). **Los mayores de 74 necesitan tratamiento específico** |
| Encuesta de Presupuestos Familiares (EPF), INE | Gasto del hogar por categorías | Hábitos de consumo y ocio |
| Encuesta Europea de Salud en España / Encuesta Nacional de Salud, INE y Ministerio de Sanidad | Salud, discapacidad, hábitos (tabaco, actividad física), uso de servicios sanitarios | Verificar la edición más reciente con microdatos |
| Encuesta a las personas sin hogar, INE | Población sin hogar | Solo para documentar el hueco y, si es posible, un módulo aparte |
| Barómetros y estudios del CIS | Actitudes, preocupaciones, valores, hábitos, confianza | Unas 4.000 entrevistas al mes (excepto agosto). **Solo para las capas de opinión y política (fases 8A y 8B)** |
| Barómetro Sanitario 2026, CIS y Ministerio de Sanidad | Opinión sobre el sistema sanitario | 7.800 entrevistas en 3 oleadas, al menos 250 por comunidad autónoma (120 en Ceuta y Melilla), con ponderación por comunidad. Útil para validar opinión por territorio |
| European Social Survey (ESS), ronda 11 (2023/24) | Valores humanos (escala de Schwartz), confianza interpersonal e institucional, bienestar | Incluye España. La ronda 12 se espera en 2026: verificar si está publicada |

### 2.4 Fuentes políticas y electorales

La dimensión política combina dos tipos de fuente con papeles distintos: **resultados electorales oficiales** como verdad de referencia y **encuestas** para saber qué tipo de persona vota o piensa qué.

| Fuente | Organismo | Qué aporta | Nivel geográfico | Uso y notas |
| --- | --- | --- | --- | --- |
| Resultados electorales oficiales (generales, autonómicas, municipales, europeas) | Ministerio del Interior (Infoelectoral) y juntas o gobiernos autonómicos | Censo electoral, votantes, abstención, votos en blanco y nulos, votos por candidatura | Mesa, sección censal, municipio, provincia | **Verdad de referencia** para calibrar el recuerdo de voto y validar la capa política por territorio. Generales de referencia: 23 de julio de 2023. Europeas: 9 de junio de 2024. Autonómicas: la más reciente de cada comunidad (verificar) |
| Censo electoral | INE (Oficina del Censo Electoral) | Electores por territorio, incluidos los extranjeros con derecho a voto en municipales y europeas | Municipio y sección | Define el **universo electoral**, distinto de la población residente |
| Barómetros mensuales del CIS | CIS | Recuerdo de voto, intención de voto, voto + simpatía, escala de autoubicación ideológica (1–10), interés por la política, valoración de líderes, cercanía a partidos | CCAA, tamaño de municipio | Principal fuente individual de variables políticas. Unas 4.000 entrevistas al mes |
| Estudios preelectorales y postelectorales del CIS | CIS | Muestras grandes con representatividad provincial o autonómica en periodo electoral; el postelectoral recoge el voto declarado justo después de la elección | Provincia (preelectorales de generales) | Mejor fuente para relacionar perfil y voto con detalle territorial. Verificar los estudios disponibles para 23J 2023 y elecciones posteriores |
| Estudios autonómicos del CIS y de centros autonómicos | CIS, CEO (Cataluña), Euskobarómetro / Sociómetro (País Vasco) y otros | Política y opinión autonómica, identidad territorial | CCAA, provincia | Detalle territorial donde el CIS nacional tiene poca muestra. Verificar condiciones de uso de cada centro |
| ESS, ronda 11 | ESS ERIC | Escala izquierda-derecha (0–10), confianza en instituciones, participación política no electoral, satisfacción con la democracia | NUTS2 | Comparabilidad europea y participación no electoral |
| Series temporales del CIS | CIS | Evolución de indicadores (ideología media, problemas principales, valoración de la situación) | Nacional | Base para la dimensión temporal (sección 8) |

## 3. Diccionario de variables

Cada variable tiene un nivel de prioridad:

- **P0 · Estructural:** define a la persona y se calibra. Si falla, la población no vale.
- **P1 · Esencial:** se añade y se valida con umbrales.
- **P2 · Complementaria:** se añade si la fuente lo permite; se valida, pero no bloquea.
- **P3 · Opinión:** capa de opinión y valores (fase 8A).
- **P3-POL · Política:** capa política (fase 8B).

### 3.1 Persona

| Variable | Prioridad | Categorías armonizadas (propuesta) | Fuente principal | Por qué importa |
| --- | --- | --- | --- | --- |
| `edad` | P0 | Años cumplidos; tramos derivados `edad_5` (quinquenales) y `edad_4` (18–34, 35–49, 50–64, 65+) | Censo / Padrón | Influye en casi todas las actitudes y comportamientos |
| `sexo` | P0 | Hombre, mujer (según registro) | Censo / Padrón | Variable básica de calibración |
| `nacionalidad_grupo` | P0 | Española; española con doble nacionalidad (si se identifica); UE; resto de Europa; África; América Latina; Asia; otros | Censo / Padrón | Diversidad de origen; grupos minoritarios clave |
| `pais_nacimiento_grupo` | P1 | Igual que arriba, por país de nacimiento | Censo / Padrón | Distingue población nacida fuera aunque tenga nacionalidad española |
| `nacionalidad_top` | P1 | Principales nacionalidades individuales (por ejemplo, las 15 más numerosas) más «otras» | Padrón | Evita tratar «extranjeros» como un bloque homogéneo |
| `estado_civil` | P1 | Soltero, casado, viudo, separado o divorciado | Censo Anual | Estructura vital |
| `nivel_estudios` | P0 | Detalle ISCED (CNED-A) y agregado `estudios_3`: hasta obligatoria, secundaria 2ª etapa, superior | Censo Anual | Gran predictor de actitudes, renta y uso digital |
| `relacion_actividad` | P0 | Ocupado; parado; jubilado o pensionista; estudiante; labores del hogar; incapacidad permanente; otra inactividad | Censo Anual / EPA | Situación vital y económica |
| `ocupacion` | P1 | CNO-11 a un dígito (y dos si el tamaño lo permite) | Censo Anual / EPA | Clase social y tipo de trabajo |
| `sector_actividad` | P2 | CNAE-09 por secciones | EPA / Censo | Contexto laboral |
| `situacion_profesional` | P1 | Asalariado público, asalariado privado, autónomo, empresario | EPA / Censo | Estabilidad y perspectiva económica |
| `tipo_jornada` | P2 | Completa, parcial | EPA | Condiciones laborales |
| `teletrabajo` | P2 | Nunca, ocasional, habitual | EPA / TIC-H | Relevante para movilidad y vivienda |
| `anio_llegada_espana` | P2 | Tramos | Censo Anual | Integración y arraigo de población inmigrante |
| `discapacidad_limitacion` | P1 | Sin limitación, limitación moderada, limitación grave (indicador GALI) | ECV / Encuesta de salud | Grupo frecuentemente invisible |
| `salud_autopercibida` | P1 | Muy buena, buena, regular, mala, muy mala | ECV / Encuesta de salud | Bienestar |
| `uso_internet` | P1 | Diario, semanal, menos frecuente, nunca | TIC-H | Brecha digital |
| `competencias_digitales` | P2 | Bajas, básicas, superiores a las básicas | TIC-H | Adopción de tecnología |
| `compra_online` | P2 | Sí/no en los últimos 3 meses | TIC-H | Hábitos de consumo |

### 3.2 Hogar

| Variable | Prioridad | Categorías | Fuente | Por qué importa |
| --- | --- | --- | --- | --- |
| `tipo_hogar` | P0 | Unipersonal; pareja sin hijos; pareja con hijos; monoparental; varias familias o personas no emparentadas; otros | Censo 2021 | Soledad, cuidados, economía doméstica |
| `tamano_hogar` | P0 | 1, 2, 3, 4, 5+ | Censo 2021 | Estructura del hogar |
| `relacion_persona_ref` | P0 | Persona de referencia, pareja, hijo, padre o madre, otro familiar, no familiar | Censo 2021 | Permite reconstruir el hogar completo |
| `n_menores_hogar` | P1 | 0, 1, 2, 3+ | Censo 2021 | Cargas familiares |
| `n_mayores_hogar` | P1 | Número de personas de 65+ y de 80+ | Censo 2021 | Cuidados |
| `tenencia_vivienda` | P1 | Propiedad sin hipoteca, propiedad con hipoteca, alquiler a precio de mercado, alquiler inferior o cesión | Censo 2021 / ECV | Vivienda y coste de vida |
| `renta_hogar_decil` | P1 | Decil de renta equivalente nacional y regional | ECV, calibrada con el Atlas de renta | Gran predictor de actitudes económicas |
| `privacion_material` | P1 | Sí/no (indicador oficial) y número de carencias | ECV | Vulnerabilidad |
| `dificultad_fin_mes` | P2 | Escala de 6 puntos ECV | ECV | Percepción económica |
| `vehiculo_hogar` | P2 | Sí/no | ECV / Censo | Movilidad |

### 3.3 Territorio y entorno

| Variable | Prioridad | Categorías | Fuente | Por qué importa |
| --- | --- | --- | --- | --- |
| `ccaa` | P0 | 19 códigos INE | Censo | Calibración y análisis territorial |
| `provincia` | P0 si está disponible | 52 códigos INE | Censo (verificar en microdatos) | Territorios a medida |
| `tamano_municipio` | P0 | <2.000; 2.000–10.000; 10.000–50.000; 50.000–100.000; 100.000–500.000; >500.000 (alinear con la clasificación de los microdatos) | Censo / Padrón | Ruralidad y servicios |
| `grado_urbanizacion` | P0 | Ciudad, intermedio, rural (DEGURBA) | Microdatos censales | Diferencias urbano-rurales |
| `municipio` | P2 | Código INE | Solo cuando el usuario define el territorio por municipios y la fuente lo permita | Asignación final dentro del territorio |
| `ctx_renta_municipio` | P1 | Renta media por persona del municipio o sección | Atlas de renta | Contexto económico local |
| `ctx_envejecimiento` | P1 | % de 65+ en el municipio | Padrón | Contexto demográfico |
| `ctx_precio_vivienda` | P2 | Índice de precio o alquiler (verificar fuente oficial) | Ministerio de Vivienda / INE | Presión de vivienda |

Las variables `ctx_*` describen el **entorno** de la persona, no a la persona, y se asignan por su municipio o territorio.

### 3.4 Opinión y valores (capa P3, fase 8A)

Variables observadas directamente en las encuestas, que se asignan a cada persona por modelo o emparejamiento:

| Variable | Categorías | Fuente | Por qué importa |
| --- | --- | --- | --- |
| `religiosidad` | Católico practicante, católico no practicante, otra religión, agnóstico, ateo, indiferente | CIS | Predictor clásico de valores y actitudes morales |
| `identidad_territorial` | Escala Linz-Moreno: solo español … solo de su comunidad | CIS, centros autonómicos | Clave en opinión territorial y política autonómica |
| `lengua_habitual` | Castellano, catalán o valenciano, euskera, gallego, otras, bilingüe | CIS, centros autonómicos | Identidad y consumo de medios en comunidades con lengua cooficial |
| `clase_subjetiva` | Alta, media-alta, media, media-baja, baja, obrera | CIS | Percepción de posición social, distinta de la renta |
| `situacion_economica_personal` | Muy buena … muy mala | CIS | Percepción económica |
| `medio_informacion_principal` | Televisión, prensa, radio, redes sociales, otros digitales | CIS | Exposición a información y encuadres |

Rasgos latentes estimados a partir del CIS y la ESS. Propuesta inicial, a confirmar con los datos:

| Rasgo | Descripción |
| --- | --- |
| `rasgo_sensibilidad_precio` | Preocupación por el coste de vida y peso del precio en las decisiones |
| `rasgo_confianza_tecnologia` | Actitud ante la tecnología y la IA |
| `rasgo_preocupacion_ambiental` | Importancia del medio ambiente |
| `rasgo_aislamiento_social` | Soledad y red social |
| `rasgo_confianza_institucional` | Confianza en instituciones y servicios públicos |
| `rasgo_confianza_interpersonal` | Confianza en los demás (ESS) |
| `rasgo_tradicion_apertura` | Eje de valores de Schwartz: conservación frente a apertura (ESS) |
| `estilo_ns_nc` | Propensión a contestar «No sabe / No contesta» |
| `estilo_aquiescencia` | Tendencia a mostrarse de acuerdo |

### 3.5 Política (capa P3-POL, fase 8B)

Las variables políticas describen el **pasado** (qué votó la persona), su **posición estable** (ideología, identidad, interés) y su **disposición presente** (cercanía a partidos, intención). Juntas ayudan a anticipar opiniones futuras, porque muchas actitudes se organizan alrededor de ellas (decisión D-004).

| Variable | Categorías | Fuente | Calibración o validación | Por qué importa |
| --- | --- | --- | --- | --- |
| `derecho_voto_generales` | Sí / no | Nacionalidad y edad (derivada) | Censo electoral | Solo los españoles mayores de edad votan en generales y autonómicas |
| `derecho_voto_europeas` | Sí / no | Nacionalidad española o de otro país de la UE inscrito en el censo (derivada) | Censo electoral | Universo de las europeas |
| `derecho_voto_municipales` | Sí / no | Nacionalidad española, de la UE o de países con acuerdo de reciprocidad (derivada) | Censo electoral | Universo de las municipales |
| `recuerdo_voto_generales` | Partido o familia de partidos de las generales de 2023, blanco, nulo, abstención, no tenía edad, sin derecho a voto, NS/NC | CIS (barómetros, postelectoral) | **Calibrado a los resultados oficiales** por provincia o CCAA, incluida la abstención | Comportamiento pasado observado; el predictor más fuerte de actitudes políticas |
| `recuerdo_voto_autonomicas` | Igual, para las últimas autonómicas de su comunidad | CIS y centros autonómicos | Resultados oficiales autonómicos | Sistemas de partidos propios de cada comunidad |
| `recuerdo_voto_europeas` | Igual, para las europeas de 2024 | CIS | Resultados oficiales | Punto intermedio en el tiempo |
| `ideologia_autoubicacion` | Escala 1 (izquierda) a 10 (derecha) y NS/NC | CIS | Distribución del CIS ponderada | Posición estable; disponible en casi todos los barómetros |
| `ideologia_eje_territorial` | Escala de nacionalismo o centralismo (donde se pregunte) | CIS y centros autonómicos | Distribución por CCAA | Segunda dimensión del sistema de partidos español |
| `cercania_partido` | Partido al que se siente más cercano, ninguno, NS/NC | CIS | Distribución del CIS | Identificación partidista |
| `intencion_voto` | Partido, blanco, nulo, abstención, indeciso, NS/NC | CIS | Solo validación; **no se calibra** | Disposición presente; muy volátil |
| `interes_politica` | Mucho, bastante, poco, nada | CIS, ESS | Distribución | Implicación y probabilidad de opinar |
| `participacion_no_electoral` | Manifestaciones, firmas, contacto con políticos, boicot (sí/no por tipo) | ESS | Distribución | Activismo |
| `confianza_instituciones` | Escalas por institución (gobierno, parlamento, partidos, justicia, UE) | ESS, CIS | Distribución | Desafección |
| `satisfaccion_democracia` | Escala 0–10 | ESS | Distribución | Desafección |
| `valoracion_lideres` | Escala 1–10 por líder | CIS | Solo validación, **no es atributo estable** | Muy dependiente del momento; se usa como pregunta, no como rasgo |

Rasgos latentes políticos que se estiman a partir de lo anterior:

| Rasgo | Descripción |
| --- | --- |
| `rasgo_izquierda_derecha` | Posición en el eje ideológico, estimada con autoubicación, recuerdo de voto y actitudes |
| `rasgo_eje_territorial` | Posición en el eje centralización-autogobierno |
| `rasgo_desafeccion` | Desconfianza en instituciones y partidos, insatisfacción con la democracia |
| `rasgo_implicacion_politica` | Interés, participación y probabilidad de votar |

**Reglas específicas de la capa política:**

1. **Familias de partidos.** Los partidos cambian (coaliciones que se rehacen, partidos que desaparecen o nacen). Se armonizan en `configs/partidos.yaml` con dos niveles: el partido tal como se votó en cada elección y una **familia o bloque estable** (por ejemplo, izquierda estatal, socialdemócrata, centro-derecha estatal, derecha radical, nacionalistas y regionalistas por territorio, otros). Toda tabla de correspondencia entre elecciones se documenta en `DECISIONS.md`.
2. **Universo electoral.** El recuerdo de voto se calibra sobre el **censo electoral residente** del territorio, no sobre toda la población: se excluyen los extranjeros sin derecho a voto y los que no tenían edad. El voto de los residentes en el extranjero (CERA) se descuenta de los resultados de referencia.
3. **Sesgos conocidos del recuerdo de voto.** Las encuestas suelen infrarrepresentar la abstención y sobrerrepresentar el voto al ganador. La calibración a resultados oficiales corrige el agregado; el sesgo residual por perfil se documenta.
4. **Las variables volátiles no son atributos.** La intención de voto y la valoración de líderes cambian mes a mes: se tratan como preguntas que el sistema predice, no como características fijas de la persona.

### 3.6 Variables excluidas

| Variable | Motivo |
| --- | --- |
| Orientación sexual, identidad de género, etnia | No existen en las fuentes oficiales de referencia. No se inventan |
| Afiliación a partidos o sindicatos | Sin fuente de encuesta con muestra suficiente; si aparece en algún estudio, puede añadirse como P2 de la capa política |
| Cualquier variable sin fuente oficial o encuesta de calidad | Principio de «mejor un hueco declarado que un dato inventado» |

## 4. Armonización

1. **Un diccionario único.** `configs/variables.yaml` define cada variable armonizada: nombre, tipo, categorías, y para cada fuente la variable original y la tabla de recodificación. Ningún código de recodificación vive fuera de ese archivo.
2. **Valores especiales.** «No sabe», «No contesta», «No procede» y valores perdidos se mapean a categorías explícitas (`NS`, `NC`, `NP`) o a nulos, **nunca** a valores numéricos de la escala.
3. **Universo.** Cada fuente tiene su universo (16+, 18+, 16–74, hogares privados…). El diccionario registra el universo y el código lo comprueba antes de comparar o unir fuentes.
4. **Pesos.** Cada fuente define su variable de peso. Todo agregado se calcula ponderado.
5. **Clasificaciones.** Estudios en CNED-A/ISCED, ocupación en CNO-11, actividad en CNAE-09, territorio con los códigos INE vigentes en la fecha de referencia. Si dos fuentes usan versiones distintas, se documenta la tabla de correspondencia.
6. **Fecha de referencia.** Cada población declara su fecha de referencia (por defecto, el último 1 de enero con Padrón publicado). Los objetivos de calibración se toman de esa fecha o de la más cercana disponible, y el desfase se documenta por variable.
7. **Variables comunes entre encuestas y población.** La capa de opinión y la política se unen a la población a través de variables que existen en ambas (edad, sexo, CCAA, tamaño de municipio, estudios, actividad, nacionalidad, tipo de hogar si existe). La matriz de cobertura de F1 indica, para cada encuesta, qué variables comunes tiene y con qué codificación. **Cuanto más rica sea la llave común, menos se generaliza.**
8. **Partidos.** Ver `configs/partidos.yaml` y las reglas de la sección 3.5.

## 5. Geografía

Niveles soportados, de mayor a menor fiabilidad:

| Nivel | Calibración disponible | Validación disponible | Confianza esperada |
| --- | --- | --- | --- |
| España | Completa | Muchas fuentes | Alta |
| Comunidad autónoma | Completa en demografía; buena en socioeconomía | Encuestas con muestra por CCAA (ECV, EPA, Barómetro Sanitario) | Media-alta |
| Provincia | Buena en demografía (Padrón, Censo); limitada en socioeconomía | Escasa | Media |
| Municipio o agrupación | Demografía (Padrón); renta (Atlas) | Muy escasa | Baja, declarada |

**Donantes cuando el territorio es pequeño.** Si un territorio no tiene suficientes donantes propios (umbral en `05_validacion.md`), se amplía el conjunto de donantes de forma jerárquica: misma provincia, luego misma comunidad con el mismo grado de urbanización, luego comunidades parecidas. La calibración posterior a las cifras locales corrige la composición. El informe de cada población indica qué proporción de donantes es local.

## 6. Gestión de las fuentes en el repositorio

- `data/raw/<fuente>/<edicion>/`: ficheros originales sin tocar, con su diseño de registro y su documentación.
- `data/raw/MANIFEST.yaml`: para cada fichero, la URL oficial, la fecha de descarga, la edición, el hash SHA-256 y la licencia o condiciones.
- `data/raw/MANUAL_DOWNLOADS.md`: ficheros que requieren descarga manual.
- Los datos brutos **no** se versionan en git. El manifiesto sí.

## 7. Datos de evaluación y contaminación

Para la población sociodemográfica (fases 0 a 7) no hay riesgo de contaminación: se usan los datos más recientes disponibles.

Para la capa de opinión y predicción (fases 8 a 12), los modelos de lenguaje pueden conocer resultados publicados antes de su fecha de corte. Por eso:

- Se fija una **fecha de corte de construcción** (propuesta: 30/06/2026, ajustable a los modelos usados). Solo se usan para construir y ajustar estudios con trabajo de campo anterior.
- Los estudios posteriores se reparten en una **ventana de validación** y una **ventana de evaluación final**, guardadas en `data/eval/` y protegidas por test.
- En la capa política el riesgo es mayor: los modelos de lenguaje han visto muchas estimaciones de voto publicadas. Ninguna estimación de voto anterior al corte se usa como «predicción» en la evaluación.

## 8. Dimensión temporal

Las opiniones cambian con el tiempo, y el proyecto quiere describir opiniones pasadas y anticipar las futuras.

- **No hay datos de panel.** El CIS entrevista a personas distintas cada mes, así que no existe la trayectoria real de una persona. Lo que sí existe es la evolución de **cada tipo de persona** (por cohorte de edad, estudios, territorio, recuerdo de voto) a lo largo de muchos barómetros: un pseudopanel.
- **Datos apilados con fecha.** Todos los microdatos de opinión se apilan con su fecha de campo. Los modelos de las fases 8A y 8B incluyen efectos de periodo, de modo que los rasgos de cada persona se pueden fechar («cómo pensaba este tipo de persona en enero de 2024») y proyectar con su incertidumbre.
- **Historia de cada persona sintética.** Cada persona puede llevar una trayectoria simulada de sus rasgos en el tiempo, coherente con la evolución de su grupo. Se marca siempre como `modelada`: no es la historia de una persona real.
- **Eventos.** Los eventos relevantes (elecciones, crisis, cambios de precios, catástrofes) se registran en `configs/eventos.yaml` con su fecha y descripción. Sirven para estudiar cómo cambiaron las opiniones antes y después de eventos pasados y, por analogía, predecir el efecto de eventos nuevos.
