# Guía de la demo (15 minutos)

Un recorrido por lo que hace la interfaz, en el orden en que mejor se entiende. Todo funciona sin los microdatos, con el paquete portable (D-076).

## Antes de empezar

```bash
pip install -e ".[web]"
export SINPOP_ANTHROPIC_API_KEY=…            # opcional: preguntas sin precedentes y eventos
sinpop serve --paquete dist/paquete          # http://127.0.0.1:8000
```

- **Clave del modelo de lenguaje:** la interfaz no enseña el gasto (D-088). El tope de 15 € se sigue aplicando en el servidor y el gasto se consulta en `/api/llm` o en `logs/llm/gasto.jsonl`. Sin clave, los resultados dicen «Estimador sin modelo de lenguaje» y todo lo demás funciona igual.
- **Atajos para la demo:**
  - **Presentación** (arriba a la derecha) deja solo el mapa y el resultado, en grande; se sale con Esc.
  - **Compartir** copia un enlace que, al abrirlo, rellena la misma pregunta, sus opciones y el territorio.
  - **Ctrl + Intro** pregunta y **/** lleva al enunciado.
  - Los botones **«Prueba con»** cargan las preguntas de esta guía.
- **Fondo del mapa:** las teselas de OpenStreetMap necesitan internet. Sin conexión se ven solo los límites del INE.

## 1. Una pregunta que el CIS ya ha hecho (30 s)

1. Con **España** elegida, escribe «¿Cómo calificaría usted la situación económica actual de España?».
2. Mientras escribes salen las preguntas parecidas del banco del CIS. Pulsa la primera para traer sus opciones.
3. Pulsa **Preguntar**.

Qué enseñar:
- **«En resumen»:** el texto se escribe solo a partir de las cifras.
- **Barras con intervalos del 80 % y del 95 %.**
- **La confianza en grande:** es la probabilidad de que el error total sea menor de 10 puntos, medida en preguntas reales.
- **«Lo que piensa la población» frente a «Como lo mediría el CIS»:** la muestra del CIS tiene más votantes del PSOE y menos abstencionistas que la realidad (D-068).
- **Evolución:** cada vez que el CIS hizo la pregunta, hasta la estimación de hoy, con más peso para lo reciente (D-082).
- **Regiones:** el mapa se colorea solo por comunidad. Pasa a «Provincias» para ver el detalle.
- **Grupos:** edad, sexo, estudios, ideología, recuerdo de voto, religiosidad, clase, tamaño de municipio… Las diferencias más grandes llevan una estrella.
- **Retratos:** 24 personas sintéticas con su probabilidad de cada respuesta.
- **«¿Se parece a la población real?»:** el panel de la izquierda explica cómo de fiel es la población a las cifras oficiales (auditoría de F7).

## 1 bis. ¿De qué depende la respuesta? (20 s)

En el mismo resultado, la sección **«¿De qué depende la respuesta?»** ordena las variables del perfil por cuánto separan las respuestas (fuerza η, D-090).

En la economía de España mandan:
- el recuerdo de voto (0,23) y la ideología (0,22);
- después, religiosidad, edad y clase social.

El sexo y el tamaño del municipio apenas influyen. Pasa el ratón por cada barra para ver la mayor diferencia entre grupos.

## 2. Exportar e informe PDF (10 s)

El botón **«Generar PDF»** está arriba a la derecha del resultado. El informe trae:
- el resumen automático;
- la distribución;
- **«¿De qué depende la respuesta?»**, con texto y gráficos;
- los grupos y el mapa;
- **«Evolución y cómo se ha calculado»**, con el método, la fiabilidad medida y las fuentes.

- **PDF:** resumen automático y páginas de gráficos.
- **CSV:** se abre en Excel en español.
- **JSON:** el formato completo.

## 3. Un dato que la población ya sabe (20 s)

Escribe «¿Cuál es su situación laboral actual?». Arriba de las sugerencias sale **«Dato oficial disponible»**.

Al pulsarlo:
- no es una predicción, sino la proporción en la población sintética, calibrada con la EPA y el Censo;
- trae el margen de simulación y la fuente con su variable original (D-077).

## 4. Cruzar dos preguntas (30 s)

En un resultado, abre **«Cruzar con otra pregunta»** y escribe «¿Cómo calificaría usted su situación económica personal en la actualidad?».

Sale cómo responde a la segunda pregunta cada grupo de respuesta a la primera:
- con la relación observada en el estudio del CIS que hizo las dos;
- ajustada a las predicciones de hoy (D-083).

## 5. Una comunidad y la comparación entre comunidades (40 s)

1. Pulsa **Andalucía** en el mapa y repite la pregunta. Usa su propia población y la composición de los encuestados del CIS allí (D-075).
2. Vuelve a España y, en «Regiones», pulsa **«Recalcular cada comunidad con su propia población»**. Usa las 19 poblaciones de 100 000 personas y tarda unos 2 minutos (D-080).

## 6. Una pregunta nueva con tus propias opciones (40 s, con clave)

1. Escribe «¿A quién culpa usted principalmente del problema del acceso a la vivienda en España?».
2. En **Plantillas**, elige «¿A quién culpa? (Gobierno, comunidad…)». También puedes escribir tus opciones y separarlas con «;».
3. Pulsa **Preguntar**.

Qué pasa:
- Como el CIS no ha hecho esa pregunta, responde el modelo de lenguaje, anclado en las preguntas más parecidas del banco (D-071).
- El resultado trae la **justificación** del modelo, que también sale en el PDF.
- Los intervalos son anchos y la confianza baja, porque así lo dice su historial en validación. Es lo honesto.

## 7. «¿Y si ocurre…?» (30 s, con clave)

En la pestaña **«¿Y si ocurre…?»**, describe «El Gobierno aprueba un tope estatal a los precios del alquiler en todas las zonas tensionadas».

Sale:
- el cambio esperado en cada respuesta, en puntos;
- la explicación del modelo;
- el orden de magnitud de eventos parecidos del pasado.

## 8. ¿Qué tamaño necesito? (20 s)

Debajo de los tamaños, «¿Qué tamaño necesito?»:
- recomienda cuántas personas sintéticas hacen falta para el margen que quieras;
- explica que más personas no suben la confianza, porque esta depende de cuántos encuestados reales hay detrás (D-079).

## 9. Validación: ¿acierta? (2 min)

Pulsa **«Validación»** en la cabecera.

1. **Arriba:** las cifras de 211 preguntas reales del CIS posteriores al corte (julio, septiembre y octubre de 2026). El error medio es de 7,9 puntos sin las escalas dudosas, y el 75 % de las preguntas queda por debajo de 10 puntos.
2. **Una que sale bien:** busca «Valoración de la situación económica general» en septiembre, con 3,3 puntos de error.
   - Verás lo previsto (barra azul) frente a lo real (raya negra) con el margen de muestreo de la encuesta.
   - En **«Por grupos»** pulsa Religiosidad: cada grupo, previsto (punto azul) y real (punto negro), dentro del margen del propio grupo.
   - En **«¿De qué depende la respuesta?»** la fuerza prevista y la real casi coinciden.
3. **Una que sale mal:** ordena por «Mayor error primero». Son temas nuevos sin precedente, como la visita del papa o los incendios, y las escalas dudosas, marcadas.
4. **Abajo, «Cómo se ha hecho»:** el error de los subgrupos frente al ruido de muestreo que se esperaría solo por el tamaño de cada grupo.

Cada pregunta enlaza el cuestionario, la ficha técnica y los microdatos oficiales del CIS de los que sale lo real.

## Qué decir si preguntan

- **¿Son personas reales?** No. Es una población sintética de adultos residentes en España, calibrada con el INE (Censo, ECP 2026, EPA), encuestas oficiales y resultados electorales oficiales.
- **¿Qué se manda al modelo de lenguaje?** Solo el enunciado y agregados públicos, nunca microdatos.
- **¿Cuánto acierta?** Está todo en la sección «Validación» y en `reports/validacion.md`. En 211 preguntas reales posteriores al corte:
  - error medio de 7,9 puntos sin las escalas dudosas (11,4 con ellas);
  - mediana de 5,3;
  - error de 3,0 en las preguntas políticas de octubre.
  - Peor en temas nuevos sin precedente.
- **¿Sustituye a una encuesta?** No. Describe distribuciones de grupo y lo dice en cada resultado (`docs/guias/limites_de_uso.md`).
