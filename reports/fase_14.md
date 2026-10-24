# Fase 14 · Interfaz web

**Estado:** puertas automáticas superadas (`reports/fase_14_puerta.md`). **Pendiente de revisión humana (G14.4).**
**Fecha:** 2026-10-22 · **Decisiones:** D-073, D-075 a D-091
**Comando:** `sinpop serve --paquete dist/paquete` y, con el servicio en marcha, `python tools/prueba_interfaz.py http://127.0.0.1:8000 && sinpop validate --phase 14`

## Qué es

Una página (`src/sinpop/servicio/web/`) servida por `sinpop serve`, sin pasos de compilación. Recorrido de la demo: `docs/guias/demo.md`.

- **Mapa** (Leaflet 1.9.4; desde D-093, cartografía propia con los límites del INE, sin teselas de fondo, y nombres de ciudades opcionales de CARTO, con crédito al pie del panel):
  - selector de nivel (España, comunidades, provincias);
  - Canarias en un recuadro con sus islas;
  - se pulsa un territorio para elegirlo.
- **Tamaño:** de 10 mil a 1 millón de personas, con el asistente «¿Qué tamaño necesito?» según el margen deseado (D-079).
- **«¿Se parece a la población real?»:** la fidelidad de la población frente a las cifras oficiales, de la auditoría de F7 (D-081).
- **Pregunta:**
  - enunciado y opciones propias, escritas una a una o pegadas con «;»;
  - plantillas (acuerdo, valoración, intensidad, responsable, confianza, frecuencia, prioridad);
  - «N.S.» y «N.C.» por defecto (D-085);
  - mientras se escribe aparecen las preguntas parecidas del banco del CIS y, si lo que se pregunta ya es un atributo de la población, el **dato oficial** (INE y otras fuentes, D-077).
- **Resultado:**
  - «En resumen», un texto por reglas a partir de las cifras;
  - barras con intervalos del 80 % y del 95 % y la confianza en una cifra grande;
  - la estimación de la población, con el interruptor «Comparar con el CIS» (D-093);
  - evolución en el tiempo;
  - desglose por comunidades y provincias con el mapa coloreado;
  - grupos ampliados (ideología, voto, religiosidad, clase, tamaño de municipio…), con los más distintos destacados;
  - retratos;
  - cruce con otra pregunta;
  - las preguntas del CIS en que se apoya;
  - el aviso de resultado simulado (D-081, D-083).
- **Preguntas sin precedentes:** con clave, responde el modelo de lenguaje anclado en el banco, con su justificación. Si falla, se muestra la estimación sin él con un aviso (D-085).
- **«¿Y si ocurre…?» (evento):** el cambio esperado por categoría con la explicación del modelo. Sin modelo de lenguaje enseña el antes y explica por qué no hay cambio estimado (D-073).
- **Exportar:** PDF con resumen y gráficos, CSV y JSON (D-078). Las consultas recientes se guardan en el navegador.
- **Comparar comunidades:** cada comunidad con su propia población (D-080).
- **«¿De qué depende la respuesta?»** (D-090): fuerza de cada variable del perfil en cada resultado y en el PDF. El botón «Generar PDF» está arriba del resultado, y el informe tiene páginas nuevas de análisis, método y fuentes.
- **Validación** (`/validacion.html`, D-091): 212 preguntas del CIS posteriores al corte, con lo previsto frente a lo real en total y en ocho variables de grupo, la importancia prevista y real y las fuentes de cada cifra. Resultados en `reports/validacion.md`.
- **Sin gasto del LLM en pantalla,** por decisión de la persona responsable (D-088, en lugar de la tarea 5 de F14). Se consulta en `/api/llm` y el tope se aplica en el servidor.
- **Acabado (D-088):**
  - cabecera fija con «Compartir» (enlace que rellena la pregunta) y «Presentación» (solo mapa y resultado);
  - preguntas de ejemplo para empezar;
  - esqueleto y barra de progreso con el tiempo mientras se calcula;
  - barras que crecen desde el eje y confianza en un anillo con su nivel (alta, media o baja);
  - el mapa vuela al territorio elegido y cambia de color con suavidad;
  - avisos flotantes y atajos de teclado.
  - Todo el movimiento se desactiva si el sistema pide menos animación.
- Solo modo claro (D-081), con diseño para móvil.
- Colores, marcas y accesibilidad siguen la guía de visualización: paleta validada, escala secuencial de un solo tono, texto en tinta y no en el color de la serie, tabla con valores escritos.

## Pruebas (con el paquete, en una copia limpia del repositorio sin `data/`)

`tools/prueba_interfaz.py` recorre la interfaz con Chromium real:

| ID | Resultado | Evidencia |
| --- | --- | --- |
| G14.1 Extremo a extremo | ✅ | Pregunta sobre España, mapa coloreado, pregunta sobre Madrid (100 000), evento y exploración; 0 errores de JavaScript |
| G14.2 Ninguna cifra sin intervalo ni confianza | ✅ | En el DOM: 7/7 barras con IC 80 % y 95 %, 77/77 celdas de subgrupo con confianza y aviso de simulación en todos los resultados, también en el evento |
| G14.3 Accesibilidad | ✅ | axe-core: 0 avisos |
| G14.4 Revisión humana | ⏸️ | Pendiente |

Además: en móvil (390 px) no hay desplazamiento horizontal.

Capturas en `reports/fase_14/`:
1. inicio;
2. sugerencias del banco;
3. resultado;
4. mapa coloreado;
5. comunidad;
6. evento;
8. móvil;
9. dato de la población;
10. asistente de tamaño;
11. validación (previsto frente a real, por grupos).

También se comprueban las opciones propias pegadas con «;» y la plantilla «responsable» (D-085).

Desde D-093 el mapa no usa teselas de fondo, así que las capturas son iguales con y sin internet. Los nombres de ciudades (opcionales) no se han podido comprobar aquí, porque el contenedor bloquea el servidor de CARTO.

## Paquete portable frente al modo completo

En 40 preguntas del banco: TVD media 0,0000, máxima 0,0002 y la misma confianza (`reports/fase_13/comparacion_paquete.json`, D-076).

## Para la revisión humana (G14.4)

```bash
git clone <repositorio> && cd SyntheticPopulation
pip install -e ".[web]"
sinpop serve --paquete dist/paquete      # http://127.0.0.1:8000
```

Si la apruebas, añade en `DECISIONS.md` una entrada «### Aprobación de F14» con «**Estado:** aprobada».
