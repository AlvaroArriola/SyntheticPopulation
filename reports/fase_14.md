# Fase 14 · Interfaz web

**Estado:** puertas automáticas superadas (`reports/fase_14_puerta.md`). **Pendiente de revisión humana (G14.4).**
**Fecha:** 2026-10-22 · **Decisiones:** D-073, D-075, D-076
**Comando:** `sinpop serve --paquete dist/paquete` y, con el servicio en marcha, `python tools/prueba_interfaz.py http://127.0.0.1:8000 && sinpop validate --phase 14`

## Qué es

Una página (`src/sinpop/servicio/web/`) servida por `sinpop serve`, sin pasos de compilación:

- **Mapa** (Leaflet 1.9.4 con teselas de OpenStreetMap): selector de nivel (España, comunidades, provincias). Se pulsa un territorio para elegirlo. Los territorios con población lista se ven más marcados, y al pasar el ratón se ven los tamaños disponibles.
- **Tamaño:** 10 mil, 50 mil, 100 mil, 500 mil y 1 millón de personas. Un punto verde marca las poblaciones listas.
  - Con los datos originales se puede generar una población nueva desde ahí.
  - En modo paquete, la interfaz avisa de que ese tamaño no está incluido y, al elegir territorio, pasa sola al tamaño disponible.
- **Pregunta:** enunciado, opciones con plantillas habituales y la casilla «Incluir N.S. y N.C.». Mientras se escribe aparecen preguntas parecidas del banco del CIS, que se pueden reutilizar.
- **Resultado:**
  - barras con la estimación y los intervalos del 80 % y del 95 %;
  - la confianza en una cifra grande, con su explicación;
  - pestaña «Lo que piensa la población» / «Como lo mediría el CIS»;
  - tabla de calor por subgrupos (edad, sexo, estudios, comunidad, recuerdo de voto);
  - mapa coloreado por comunidad para la opción que se elija;
  - las preguntas del CIS en que se apoya;
  - el aviso de resultado simulado.
- **«¿Y si ocurre…?» (evento):** muestra el antes y el después con el intervalo del cambio. Sin modelo de lenguaje enseña el antes y explica por qué no hay cambio estimado (D-073).
- **Gasto del LLM** frente al tope, siempre visible arriba. Modo oscuro y diseño para móvil.
- Colores, marcas y accesibilidad siguen la guía de visualización (paleta validada, una escala secuencial de un solo tono, texto en tinta y no en el color de la serie, tabla con valores escritos).

## Pruebas (con el paquete, en una copia limpia del repositorio sin `data/`)

`tools/prueba_interfaz.py` recorre la interfaz con Chromium real:

| ID | Resultado | Evidencia |
| --- | --- | --- |
| G14.1 Extremo a extremo | ✅ | Pregunta sobre España, mapa coloreado, pregunta sobre Madrid (100 000), evento y exploración; 0 errores de JavaScript |
| G14.2 Ninguna cifra sin intervalo ni confianza | ✅ | En el DOM: 7/7 barras con IC 80 % y 95 %, 28/28 celdas con confianza y aviso de simulación en todos los resultados, también en el evento |
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
7. modo oscuro;
8. móvil.

En el contenedor de trabajo las teselas de OpenStreetMap están bloqueadas, por eso las capturas muestran solo los límites del INE. En un equipo con internet se ve el mapa de fondo.

## Paquete portable frente al modo completo

En 40 preguntas del banco: TVD media 0,0000, máxima 0,0002 y la misma confianza (`reports/fase_13/comparacion_paquete.json`, D-076).

## Para la revisión humana (G14.4)

```bash
git clone <repositorio> && cd SyntheticPopulation
pip install -e ".[web]"
sinpop serve --paquete dist/paquete      # http://127.0.0.1:8000
```

Si la apruebas, añade en `DECISIONS.md` una entrada «### Aprobación de F14» con «**Estado:** aprobada».
