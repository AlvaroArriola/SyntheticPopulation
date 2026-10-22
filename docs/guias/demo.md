# Guía de la demo (15 minutos)

Un recorrido por lo que hace la interfaz, en el orden en que mejor se entiende. Todo funciona sin los microdatos, con el paquete portable (D-076).

## Antes de empezar

```bash
pip install -e ".[web]"
export SINPOP_ANTHROPIC_API_KEY=…            # opcional: preguntas sin precedentes y eventos
sinpop serve --paquete dist/paquete          # http://127.0.0.1:8000
```

- **Clave del modelo de lenguaje:** arriba a la derecha se ve el gasto («LLM 0,93 € de 15,00 €»). Sin clave, la interfaz lo dice y todo lo demás funciona igual.
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

## 2. Exportar (10 s)

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
- El resultado trae la **justificación** del modelo y el coste, unos 0,05 €.
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

## Qué decir si preguntan

- **¿Son personas reales?** No. Es una población sintética de adultos residentes en España, calibrada con el INE (Censo, ECP 2026, EPA), encuestas oficiales y resultados electorales oficiales.
- **¿Qué se manda al modelo de lenguaje?** Solo el enunciado y agregados públicos, nunca microdatos.
- **¿Cuánto acierta?** En 107 preguntas reales de la ventana de validación, el error total medio es de 0,066 (TVD). La confianza está calibrada: ECE 0,028 (`reports/fase_09_puerta.md`, `reports/fase_10_puerta.md`).
- **¿Sustituye a una encuesta?** No. Describe distribuciones de grupo y lo dice en cada resultado (`docs/guias/limites_de_uso.md`).
