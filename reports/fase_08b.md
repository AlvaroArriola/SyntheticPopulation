# Fase 08B · Capa política

**Estado:** pendiente de la revisión humana G8B.9. La puerta automática falla en un punto: dos celdas de G8B.2, que se proponen como excepciones (D-067).
**Fecha:** 2026-10-21 · **Versión del código:** ver `reports/fase_08b_validacion.json` (`version_codigo`)
**Comando para reproducir** (tras la cadena de `reports/fase_08a.md`):

```
python tools/descargar_cis.py --solo-fichas --fichas <estudios de seleccion.json> \
  && python -c "from sinpop.opinion import cis, ess; cis.armonizar(); ess.armonizar()" \
  && sinpop targets --territory all \
  && python -c "from sinpop.politics import run; run.construir('2026-01-01_ES_1000000_s1')" \
  && python -m sinpop.validate.fase8b && sinpop validate --phase 8b
```

## Resumen

A cada adulto de la población nacional (840.249 personas) se le asigna en `politics.parquet`, unido por `person_id`:

| Bloque | Variables | Fuente | Método |
| --- | --- | --- | --- |
| Derecho a voto | actual (generales, europeas y municipales potenciales), generales 2023 y última autonómica | Población base | Edad a la fecha de cada elección |
| Voto pasado | recuerdo de generales 2023 (+ NS/NC aparte) | 49 estudios del CIS (200.195 encuestados) | Multinomial calibrado a los resultados oficiales de residentes por provincia y, dentro, por tamaño con la mitad A de los municipios |
| | recuerdo de la última autonómica (+ NS/NC) | Postelectorales autonómicos del CIS (3410, 3446, 3459, 3464, 3541, 3548, 3550 y 3566) | Condicionado al voto de generales; calibrado por circunscripción |
| Ideología | autoubicación 1-10, NS, NC | CIS (estudios con recuerdo de 2023) | Multinomial con perfil, valores y recuerdo |
| | partido más cercano (familias, ninguno, NS, NC) | CIS, 19 estudios de los 12 meses anteriores al corte | Igual |
| Actitudes (ESS) | interés, 7 formas de participación, confianza en 7 instituciones, satisfacción con la democracia | ESS ronda 11 | Emparejamiento conjunto por voto × edad × estudios (`emparejada`) |
| Rasgos latentes | izquierda-derecha, desafección, implicación | ESS ronda 11 | Factorial + extracción condicionada al voto y la ideología |
| | eje territorial | CIS 3409 | Igual, con la autoubicación |

- Ninguna variable política entra en `persons.parquet` ni en `opinion.parquet`, que no cambian (G8B.6).
- Las respuestas NS/NC se mantienen como opciones.
- La intención de voto y la valoración de líderes no son atributos.
- Toda correspondencia de siglas está en `configs/partidos.yaml`.

**Reapertura de F3:**
- Los electores autonómicos de los boletines incluyen el CERA y se descuentan (D-067). Galicia pasa de 44 % a 32 % de abstención de residentes.
- Solo cambia `voto_autonomicas`. La puerta F3 se vuelve a superar.

## Puerta de salida

Ver `reports/fase_08b_puerta.md` (`sinpop validate --phase 8b`).

| ID | Resultado | Valor |
| --- | --- | --- |
| G8B.1 V-POL-RECUERDO | ✅ | 52/52 provincias; TVD máx. 0,026 |
| G8B.2 V-POL-RESERVADA | ❌ (2 excepciones propuestas) | España 6/6 tamaños; comunidad × tamaño 47/49 evaluables. Fuera: Cantabria ≤ 2.000 hab. (TVD 0,063; participación 5,3 puntos) y Navarra 10.001-50.000 (TVD 0,082; 4,4 puntos) |
| G8B.3 V-POL-PERFIL | ✅ | 24/24 (6 electorados × 4 variables) frente al 3420 reponderado; TVD máx. 0,077. Sin reponderar: 14/24 |
| G8B.4 V-POL-COHERENCIA | ✅ | 9/9 electorados: media a ± 0,3 y razón de desviaciones en [0,8; 1,2] |
| G8B.5 V-POL-TRANSFERENCIA | ✅ | 28/28 filas con ≥ 200 casos frente al CIS ajustado por IPF; TVD media 0,027. Sin ajustar: 5/28 |
| G8B.6 Capas | ✅ | 0 columnas políticas en la base y en opinión; sus sha256 no cambian |
| G8B.7 V-POL-SESGO | ✅ | Diversidad 63/63 (razón de entropías mín. 0,94); contrafactual de ideología 9/9 |
| G8B.8 Derecho a voto | ✅ | 0 personas sin derecho con recuerdo (generales: 144.533 sin derecho; autonómicas: 136.913) |
| V-LATENTE (tarea 6) | ✅ | Izquierda-derecha CFI 0,966 / RMSEA 0,064 / omega 0,72; desafección 0,991 / 0,059 / 0,85; implicación 0,971 / 0,066 / 0,75 (conjunto); eje territorial 0,999 / 0,030 / 0,72 |
| G8B.9 Revisión humana | ⏸️ | Pendiente |

**Reproducibilidad:** ver la sección «Reproducibilidad» al final.

## Decisiones que necesitan aprobación (D-067)

1. **G8B.2:** aceptar las dos celdas fuera de umbral como excepciones documentadas; el umbral no cambia.
2. **G8B.3:** reponderar el postelectoral 3420 a edad × sexo × estudios. Su peso solo corrige la comunidad, y su muestra tiene un 48 % de titulados superiores frente al 38 % real.
3. **G8B.5:** ajustar por IPF la tabla cruzada del CIS a los márgenes oficiales. El CIS declara un 10-14 % de abstención autonómica frente al 30-45 % real. Así se compara la relación entre los dos votos, no los márgenes.
4. **G8B.7:** criterio contrafactual de ± 0,3 puntos (no lo fija `docs/06`), con la religiosidad en las celdas de datos. La primera versión, sin religiosidad, dejaba al PP y a Vox 0,30 y 0,39 por debajo: el modelo atenuaba las diferencias, no las exageraba.
5. **Residuos correlacionados declarados a priori** en el factorial: izquierda-derecha (autoubicación–partido votado) y eje territorial (identificación–orgullo).
6. **Implicación:** su ajuste se contrasta con la desafección. Con los tres rasgos de la ESS juntos el CFI baja a 0,88.

Los cambios de los puntos 2 a 4 se hicieron después de ver el primer resultado; D-067 recoge las cifras de antes y de después.

## Limitaciones

- **Comunidades del 28/05/2023:** la relación generales → autonómicas se estima con la intención de voto de generales (3410) y no se valida (no hay datos con los dos recuerdos).
- **Nacionalidad y residencia** son las actuales: quien se nacionalizó o se mudó después de una elección figura con derecho en ella.
- **Votos del CERA:** quedan dentro de los votos autonómicos, así que la abstención de residentes queda algo por debajo de la real.
- **«Otro partido»** del CIS mezcla familias y se asigna a «otros».
- **Encuesta frente a oficiales:** el recuerdo de encuesta está sesgado (sobredeclara participación y voto al ganador). Por eso los márgenes se calibran contra los resultados oficiales y solo las relaciones se comparan contra el CIS.

## Reproducibilidad

Se reporta tras la comprobación de dos construcciones con la misma semilla.
