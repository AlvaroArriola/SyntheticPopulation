# Fase 13 · Servicio de consulta (API local)

**Estado:** puerta superada (`reports/fase_13_puerta.md`).
**Fecha:** 2026-10-22 · **Decisiones:** D-073, D-075, D-076
**Comando:** `python tools/prueba_f13.py && sinpop validate --phase 13`

## Qué hay

`sinpop serve` levanta un servicio FastAPI en `http://127.0.0.1:8000` (`src/sinpop/servicio/app.py`). Usa las mismas funciones que la CLI (`predict.salida.predecir_dict`, `predict.evento.predecir_pregunta`, `synth`, `opinion`, `politics`), sin reimplementar ningún método.

| Ruta | Para qué |
| --- | --- |
| `GET /api/territorios` | Recintos de las 19 comunidades y las 52 provincias (seccionado del INE 2024, simplificado) |
| `GET /api/poblaciones`, `POST /api/poblaciones` | Poblaciones existentes y generación de una nueva (en cola, una a la vez) |
| `POST /api/preguntas`, `POST /api/eventos` | Predicción de una pregunta o del efecto de un evento (en cola) |
| `GET /api/trabajos/{id}` | Estado y resultado de un trabajo |
| `GET /api/banco` | Preguntas parecidas del banco del CIS |
| `GET /api/etiquetas`, `/api/modo`, `/api/llm`, `/api/ficha/{run}` | Etiquetas, modo (completo o paquete), gasto del LLM y ficha de datos |

- **Predicción por territorio (D-075):** sobre una población de una comunidad o una provincia, el rastrillo usa la composición del CIS de ese territorio. La incertidumbre y la confianza del total salen de lo que se sabe de ese territorio, así que las provincias pequeñas tienen intervalos más anchos.
- **Paquete portable (D-076):** `sinpop serve --paquete dist/paquete` funciona sin microdatos (`docs/guias/uso.md` §7). Probado en una copia limpia del repositorio sin `data/`. Frente al modo completo, en 40 preguntas del banco: TVD media 0,0000, máxima 0,0002 y la misma confianza (`reports/fase_13/comparacion_paquete.json`).

## Puerta

| ID | Resultado | Evidencia |
| --- | --- | --- |
| G13.1 Servicio = CLI | ✅ 4/4 | Q001 y E002 sobre España (1 millón) y Madrid (100 000): JSON idéntico salvo el tiempo (`reports/fase_13/prueba_servicio.json`) |
| G13.2 Formato §2.8 | ✅ 0 fallos | Esquema y coherencia (`salida.validar`), `resultado_simulado`, aviso, IC 80 % y 95 % y confianza en cada respuesta |
| G13.3 Sin microdatos | ✅ | Solo rutas conocidas; `servicio/app.py` no lee `data/raw` ni `data/interim`; el test de fugas sigue pasando |
| G13.4 Presupuesto | ✅ | El servicio no llama al proveedor; todo pasa por `llm.cliente.ejecutar`, que bloquea antes de enviar si se supera el tope |

## Cambios para que servicio y CLI coincidan

La salida del evento por CLI no llevaba `run_id` ni el aviso, y la del servicio sí. Ahora la CLI también los lleva.

## Pendiente

Nada en F13. La interfaz (F14) espera revisión humana (G14.4).
