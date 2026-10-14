# 06 · Sesgos, generalizaciones y minorías

El objetivo de este documento es que la población **no simplifique la realidad**: que los grupos pequeños existan en su proporción justa, que se parezcan a sí mismos y no a un tópico, y que dentro de cada grupo haya la misma variedad que en la vida real.

## 1. De dónde vienen los sesgos

| Tipo de sesgo | Cómo aparece | Cómo se evita en este proyecto |
| --- | --- | --- |
| **Cobertura** | Las fuentes no incluyen a ciertas personas: residentes en residencias u otros establecimientos colectivos, personas sin hogar, personas no empadronadas | Verificar la cobertura en F1; tratar los establecimientos colectivos como bloque específico si hay datos; documentar lo que no se puede cubrir |
| **No respuesta de las encuestas** | Ciertos perfiles contestan menos | Usar siempre los pesos oficiales de cada encuesta |
| **Temporal** | Los donantes son de 2021 y la población de referencia, de 2026 | Calibrar a las cifras más recientes; documentar el desfase por variable |
| **Agregación** | Tratar como un único grupo a poblaciones muy distintas, por ejemplo «extranjeros» | Variables con detalle (`nacionalidad_top`, `pais_nacimiento_grupo`) y validación por subgrupo |
| **Reutilización de donantes** | Un grupo pequeño se construye copiando muchas veces a unas pocas personas reales: el grupo se convierte en la caricatura de esas pocas personas | Métrica V-CONCENTRACION; ampliación jerárquica de donantes; sobremuestreo con pesos en lugar de duplicación masiva |
| **Regresión a la media** | Asignar a cada persona el valor medio de su grupo (renta media, opinión media) en lugar de un valor plausible con su variabilidad | Emparejamiento con donantes reales o extracciones aleatorias, nunca medias. Métrica V-DIVERSIDAD |
| **Préstamo geográfico** | Un territorio con pocos datos se construye con personas de otro sitio y hereda sus rasgos | Calibración a cifras locales después del préstamo; contexto territorial (`ctx_*`); porcentaje de donantes locales en el informe |
| **Clasificación** | Las categorías oficiales no recogen ciertas realidades (por ejemplo, el sexo registral es binario) | Documentar la limitación; no inventar categorías sin fuente |
| **Estereotipos del modelo de lenguaje** (F9) | El LLM responde por tópico del grupo en lugar de por los datos | Pruebas contrafactuales y auditoría de justificaciones (sección 5) |
| **Recuerdo de voto** (F8B) | En las encuestas se declara menos abstención y más voto al ganador del que hubo; el voto a algunos partidos se declara menos | Calibración a resultados oficiales; validación de perfiles contra postelectorales, no de totales |
| **Determinismo político** (F8B) | Asumir que todos los votantes de un partido piensan igual o que un perfil sociodemográfico determina el voto | Asignación por probabilidades y extracción aleatoria; validación de la dispersión ideológica dentro de cada electorado |
| **Temporal en lo político** (F8C) | Fijar como identidad algo que cambia (intención de voto, valoración de líderes) | Esas variables se predicen como preguntas, no se asignan como atributos (D-005) |

## 2. Lista de vigilancia

Los grupos vigilados se definen en `configs/watchlist.yaml`. Cada entrada tiene: nombre, definición como expresión sobre las variables, fuente oficial de referencia, proporción esperada por territorio y recuento mínimo deseado.

Lista inicial (ampliable):

| Grupo | Definición | Referencia | Por qué se vigila |
| --- | --- | --- | --- |
| Mayores de 85 | `edad >= 85` | Padrón | Pocos donantes; alta presencia en residencias |
| Mayores que viven solos | `edad >= 65 & tipo_hogar == unipersonal` | Censo 2021 | Soledad; grupo clave en vivienda y cuidados |
| Principales nacionalidades extranjeras, una a una | Las 15 más numerosas según el Padrón | Padrón | Evitar tratar «extranjeros» como un bloque |
| Nacidos fuera con nacionalidad española | `pais_nacimiento_grupo != España & nacionalidad_grupo == española` | Censo Anual | Grupo creciente, a menudo invisible |
| Residentes en Ceuta y Melilla | `ccaa in {18, 19}` | Padrón | Territorios muy pequeños y con perfil propio |
| Residentes en municipios de menos de 2.000 habitantes | `tamano_municipio == <2.000` | Padrón | Ruralidad extrema; pocos donantes en algunas zonas |
| Residentes en islas no capitalinas | Por municipio, si se dispone | Padrón | Insularidad |
| Hogares monoparentales | `tipo_hogar == monoparental` | Censo 2021 | Vulnerabilidad económica |
| Personas con limitación grave | `discapacidad_limitacion == grave` | ECV / encuesta de salud | Grupo frecuentemente invisible |
| Jóvenes que ni estudian ni trabajan | `edad 18–24 & no ocupado & no estudiante` | EPA | Situación vital específica |
| Personas en paro | `relacion_actividad == parado` | EPA | Situación económica |
| Personas sin estudios o con primaria incompleta | `nivel_estudios <= primaria incompleta` | Censo Anual | Brecha educativa y digital |
| Hogares con privación material severa | Indicador oficial ECV | ECV | Pobreza |
| Personas que nunca usan internet | `uso_internet == nunca` | TIC-H | Brecha digital |
| Abstencionistas en las generales | `recuerdo_voto_generales == abstencion` | Resultados oficiales | Suelen faltar en las encuestas y son una cuarta parte o más del electorado |
| Votantes de partidos pequeños y regionalistas | Por familia y territorio en `partidos.yaml` | Resultados oficiales | Pocos casos en el CIS; riesgo de desaparecer o de describirse con datos de otros |
| Residentes sin derecho a voto en generales | `derecho_voto_generales == no` | Padrón y censo electoral | No deben recibir recuerdo de voto; sí tienen opiniones políticas |
| Personas sin ubicación ideológica | `ideologia_autoubicacion == NS/NC` | CIS | Grupo amplio que tiende a desaparecer si se imputa siempre un valor |

### Grupos no observables

Hay grupos que **no se pueden representar con fiabilidad** porque las fuentes oficiales no los identifican o no los cubren. No se inventan. Se documentan en la sección de limitaciones de cada población:

- Personas sin hogar (existe una encuesta específica del INE, pero no se integra en el marco de hogares; se puede tratar como módulo aparte).
- Población no empadronada, incluida parte de la población migrante en situación irregular.
- Grupos étnicos (por ejemplo, la población gitana), orientación sexual e identidad de género: no figuran en las fuentes de referencia.
- Población en establecimientos colectivos, si F1 confirma que la muestra de hogares no la cubre.

## 3. Procedimiento de auditoría (F7)

`sinpop audit --run <run_id>` ejecuta, para la población y cada grupo vigilado:

1. **Representación:** ratio entre proporción sintética y oficial (V-MINORIAS).
2. **Perfil interno:** distribución de edad, sexo, estudios y actividad dentro del grupo frente a la oficial, si existe (V-MINORIAS-PERFIL).
3. **Concentración de donantes:** cuántos hogares donantes distintos generan el grupo y cuánto pesan los cinco más usados (V-CONCENTRACION).
4. **Diversidad interna:** entropía de los atributos dentro del grupo frente a la de los donantes ponderados (V-DIVERSIDAD).
5. **Combinaciones raras:** perfiles que no existen en ningún donante (V-RAREZA).
6. **Calidad de los atributos enriquecidos:** proporción de valores `observada`, `emparejada`, `modelada` y `extrapolada` dentro del grupo. Un grupo con mucha extrapolación se señala.

El informe incluye un **semáforo por grupo**:

- **Verde:** supera todas las comprobaciones.
- **Ámbar:** las supera, pero con más del 50 % de donantes no locales o con más del 30 % de atributos extrapolados.
- **Rojo:** falla alguna comprobación. Bloquea la puerta de F7.

## 4. Medidas correctoras, por orden de preferencia

1. **Revisar datos y armonización.** Muchos fallos son errores de códigos o de universo.
2. **Añadir el grupo a la calibración** si existe una cifra oficial fiable para él.
3. **Ampliar el conjunto de donantes** de forma jerárquica, documentándolo.
4. **Sobremuestrear el grupo con pesos** para tener casos suficientes sin distorsionar los agregados.
5. **Modelar en lugar de copiar** atributos concretos del grupo, con modelos que tomen prestada información de grupos parecidos (modelos multinivel) y marcando el resultado como `modelada`.
6. **Declarar la limitación** si nada de lo anterior es posible con datos.

Nunca se corrige un grupo ajustando a mano sus valores para que «cuadren».

## 5. Estereotipos en la capa de IA (F9)

Cuando el modelo de lenguaje interviene, se añaden tres pruebas:

1. **Prueba contrafactual.** Se toman perfiles idénticos salvo en un atributo (por ejemplo, la nacionalidad, el sexo o el tipo de municipio) y se comparan sus respuestas. La diferencia que produce el LLM se compara con la que producen los datos (modelo estadístico de F8A y F8B). Si el LLM exagera sistemáticamente las diferencias entre grupos, está aplicando un estereotipo.
2. **Homogeneidad.** La variabilidad de las respuestas simuladas dentro de cada grupo se compara con la real. Un LLM que responde casi igual para todo un grupo está generalizando.
3. **Auditoría de justificaciones.** En una muestra de 100 justificaciones, se comprueba que solo se apoyan en atributos que la persona tiene en su ficha y que no recurren a rasgos del grupo que no figuran en ella. Las justificaciones problemáticas se registran y alimentan cambios en los prompts.

## 6. Sesgos en la capa política (F8B)

Las variables políticas son muy predictivas, y por eso mismo muy propensas a convertirse en estereotipos. Pruebas obligatorias:

1. **Diversidad dentro de cada electorado.** Para cada familia de partidos, los atributos no políticos (edad, estudios, renta, territorio, valores) tienen la diversidad que muestran los datos reales. Un electorado sintético más homogéneo que el real indica que el modelo ha simplificado (umbral en V-POL-SESGO).
2. **Dispersión ideológica.** La autoubicación dentro de cada electorado conserva su dispersión real (V-POL-COHERENCIA). Votar a un partido no fija la ideología.
3. **El voto no lo explica todo.** En la capa de predicción se compara la diferencia entre electorados que produce el sistema con la que aparece en los datos reales para preguntas no políticas. Si el sistema exagera la división por voto en temas cotidianos, está polarizando de más.
4. **Prueba contrafactual política.** Dos perfiles iguales salvo en el recuerdo de voto: la diferencia en sus respuestas debe parecerse a la de los datos, no a la del tópico. Se aplica también a la escala ideológica.
5. **Equilibrio en los textos.** Las justificaciones generadas por el LLM para votantes de distintas familias se revisan con el mismo criterio: ningún electorado se describe con más carga negativa o caricatura que otro.
6. **NS/NC como respuesta legítima.** No ubicarse en la escala, no recordar el voto o no tener partido cercano son respuestas reales y frecuentes. No se eliminan ni se imputan siempre: se modelan como una opción más.

## 7. Límites de uso

Cada población y cada informe incluyen esta sección, adaptada:

- La población describe **distribuciones**, no personas. No se debe usar para tomar decisiones sobre individuos reales.
- No sustituye a una encuesta cuando la decisión es crítica o afecta a derechos de las personas.
- No debe usarse para dirigir acciones a grupos vulnerables sin una validación específica para ese grupo.
- Los grupos marcados en ámbar o rojo, y los no observables, no deben analizarse por separado sin advertir de su baja fiabilidad.
- Las estimaciones por provincia o municipio tienen una confianza menor que las nacionales y autonómicas, y así debe comunicarse.
- La capa política describe tendencias de grupo: no permite afirmar qué vota o qué piensa una persona real con un perfil determinado.
