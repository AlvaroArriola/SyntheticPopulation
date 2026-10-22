"""Cliente de modelos de lenguaje con caché, registro, validación y presupuesto (D-071).

- **Caché** (`logs/llm/cache/<clave>.json`, versionada): la clave es el SHA-256 del modelo, el
  prompt (`nombre@versión` y su hash), el esfuerzo, el esquema y el texto enviado. La misma
  petición nunca se paga dos veces, y una ejecución repetida da ficheros idénticos.
- **Registro de gasto** (`logs/llm/gasto.jsonl`, versionado): una línea por llamada pagada, con
  tokens y coste en euros.
- **Presupuesto:** antes de enviar se calcula una cota superior del coste (entrada estimada y
  `max_tokens` completos de salida). Si superaría el tope por ejecución o el total del proyecto
  (`configs/llm.yaml`), no se envía nada (`PresupuestoExcedido`).
- **Validación:** la salida se pide con esquema JSON (`output_config.format`) y se valida otra vez
  aquí, más una comprobación semántica opcional de quien llama. Una salida inválida se reintenta
  `reintentos_salida_invalida` veces; si sigue mal, se devuelve `None` y quien llama usa el
  componente estadístico.
- **Lotes:** con `usar_lotes`, las peticiones van por la Message Batches API (50 % más barata).
- A los modelos solo les llegan enunciados públicos y agregados, nunca microdatos (regla 8).
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

import jsonschema

from sinpop import REPO_ROOT
from sinpop.config import load_config
from sinpop.llm import prompts as P

CARACTERES_POR_TOKEN = 3.0  # cota prudente para estimar la entrada (español, JSON)


class LLMNoDisponible(RuntimeError):
    pass


class PresupuestoExcedido(RuntimeError):
    pass


@dataclass
class Peticion:
    id: str
    tarea: str
    variables: dict[str, str]
    esquema: dict
    validar: Callable[[dict], None] | None = field(default=None, compare=False)


@dataclass
class Respuesta:
    texto: str | None
    entrada: int
    salida: int
    motivo_fin: str | None


class Backend(Protocol):
    def enviar(self, solicitudes: list[dict], lotes: bool) -> dict[str, Respuesta]: ...


def _cfg():
    return load_config("llm.yaml")


def _rutas() -> tuple[Path, Path]:
    c = _cfg()
    cache = REPO_ROOT / c.cache_dir
    return cache, REPO_ROOT / c.logs_dir / "gasto.jsonl"


def credenciales() -> bool:
    return any(os.environ.get(v) for v in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"))


def disponible() -> bool:
    """El LLM se usa solo si está activado en la configuración y hay credenciales."""
    return bool(_cfg().activo and credenciales())


def gasto_total() -> float:
    _, reg = _rutas()
    if not reg.exists():
        return 0.0
    return sum(json.loads(x)["eur"] for x in reg.read_text("utf-8").splitlines() if x.strip())


def _modelo(id_: str):
    return next(m for m in _cfg().modelos if m.id == id_)


def coste_eur(modelo: str, entrada: int, salida: int, lote: bool) -> float:
    c, m = _cfg(), _modelo(modelo)
    if m.precio_usd_mtok is None:
        raise ValueError(f"{modelo}: sin precio declarado en configs/llm.yaml")
    usd = (entrada * m.precio_usd_mtok.entrada + salida * m.precio_usd_mtok.salida) / 1e6
    if lote:
        usd *= c.presupuesto.descuento_lotes
    return usd * c.presupuesto.eur_por_usd


def _solicitud(p: Peticion) -> tuple[dict, str, dict]:
    """Parámetros de la API, clave de caché y metadatos de una petición."""
    t = _cfg().tareas[p.tarea]
    pr = P.cargar(t.prompt)
    sistema, usuario = pr.render(p.variables)
    params = {
        "model": t.modelo,
        "max_tokens": t.max_tokens,
        "system": sistema,
        "messages": [{"role": "user", "content": usuario}],
        "output_config": {
            "effort": t.esfuerzo,
            "format": {"type": "json_schema", "schema": p.esquema},
        },
    }
    meta = {"tarea": p.tarea, "modelo": t.modelo, "prompt": pr.id, "prompt_sha256": pr.sha256}
    clave = hashlib.sha256(
        json.dumps({"params": params, "meta": meta}, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()
    return params, clave, meta


def _cota(params: dict, lote: bool) -> float:
    chars = len(params["system"]) + sum(len(m["content"]) for m in params["messages"])
    chars += len(json.dumps(params["output_config"]))
    return coste_eur(params["model"], int(chars / CARACTERES_POR_TOKEN), params["max_tokens"], lote)


def estimar(peticiones: list[Peticion]) -> dict:
    """Cota superior del coste de las peticiones que no están en caché (no llama a nadie)."""
    cache, _ = _rutas()
    lote = _cfg().presupuesto.usar_lotes
    pend = [s for s in map(_solicitud, peticiones) if not (cache / f"{s[1]}.json").exists()]
    return {
        "peticiones": len(peticiones),
        "en_cache": len(peticiones) - len(pend),
        "a_enviar": len(pend),
        "cota_eur": round(sum(_cota(s[0], lote) for s in pend), 4),
        "gastado_eur": round(gasto_total(), 4),
        "tope_total_eur": _cfg().presupuesto.eur_max_total,
        "tope_ejecucion_eur": _cfg().presupuesto.eur_max_por_ejecucion,
    }


def registro(p: Peticion) -> dict:
    """Llamadas, tokens y euros que ha costado una petición (0 si salió de la caché sin pagar
    en esta copia del registro)."""
    _, reg = _rutas()
    params, clave, meta = _solicitud(p)
    filas = []
    if reg.exists():
        filas = [json.loads(x) for x in reg.read_text("utf-8").splitlines() if x.strip()]
    filas = [f for f in filas if f["clave"] == clave]
    return {
        "llamadas": len(filas),
        "tokens": sum(f["tokens_entrada"] + f["tokens_salida"] for f in filas),
        "eur": round(sum(f["eur"] for f in filas), 6),
        "modelo": params["model"],
        "prompt": meta["prompt"],
    }


def _comprobar(salida: dict, p: Peticion) -> None:
    jsonschema.validate(salida, p.esquema)
    if p.validar is not None:
        p.validar(salida)


def ejecutar(peticiones: list[Peticion], backend: Backend | None = None) -> dict[str, dict | None]:
    """Devuelve la salida validada de cada petición (o None si no se pudo obtener)."""
    c = _cfg()
    if backend is None:
        if not disponible():
            raise LLMNoDisponible("LLM desactivado en configs/llm.yaml o sin credenciales")
        backend = AnthropicBackend()
    cache, registro = _rutas()
    cache.mkdir(parents=True, exist_ok=True)
    registro.parent.mkdir(parents=True, exist_ok=True)
    lote = c.presupuesto.usar_lotes
    out: dict[str, dict | None] = {}
    pendientes: dict[str, tuple[Peticion, dict, str, dict]] = {}
    for p in peticiones:
        params, clave, meta = _solicitud(p)
        f = cache / f"{clave}.json"
        if f.exists():
            out[p.id] = json.loads(f.read_text("utf-8"))["salida"]
        else:
            pendientes[p.id] = (p, params, clave, meta)
    cota = sum(_cota(v[1], lote) for v in pendientes.values())
    if cota > c.presupuesto.eur_max_por_ejecucion:
        raise PresupuestoExcedido(
            f"cota {cota:.2f} € > tope por ejecución {c.presupuesto.eur_max_por_ejecucion} €"
        )
    if gasto_total() + cota > c.presupuesto.eur_max_total:
        raise PresupuestoExcedido(
            f"gastado {gasto_total():.2f} € + cota {cota:.2f} € > tope total "
            f"{c.presupuesto.eur_max_total} €"
        )
    for _intento in range(c.reintentos_salida_invalida + 1):
        if not pendientes:
            break
        resp = backend.enviar([{"custom_id": k, **v[1]} for k, v in pendientes.items()], lote)
        hechos = []
        for k, (p, params, clave, meta) in pendientes.items():
            r = resp.get(k)
            if r is None:
                continue
            eur = coste_eur(params["model"], r.entrada, r.salida, lote)
            salida, error = None, None
            try:
                if r.texto is None:
                    raise ValueError(f"sin texto (motivo de fin: {r.motivo_fin})")
                salida = json.loads(r.texto)
                _comprobar(salida, p)
            except (ValueError, jsonschema.ValidationError) as e:
                salida, error = None, str(e)[:300]
            with registro.open("a", encoding="utf-8") as fh:
                fh.write(
                    json.dumps(
                        {
                            "fecha": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
                            "id": k,
                            "clave": clave,
                            **meta,
                            "lote": lote,
                            "tokens_entrada": r.entrada,
                            "tokens_salida": r.salida,
                            "eur": round(eur, 6),
                            "valida": error is None,
                            "error": error,
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
            if error is None:
                guardado = {"meta": meta, "salida": salida}
                (cache / f"{clave}.json").write_text(
                    json.dumps(guardado, ensure_ascii=False, indent=1, sort_keys=True), "utf-8"
                )
                out[k] = salida
                hechos.append(k)
        for k in hechos:
            pendientes.pop(k)
    for k in pendientes:
        out[k] = None
    return out


def _sin_id(s: dict) -> dict:
    return {k: v for k, v in s.items() if k != "custom_id"}


class AnthropicBackend:
    """Envío real con el SDK oficial de Anthropic (`pip install anthropic`)."""

    ESPERA_S = 30

    def __init__(self) -> None:
        import anthropic

        self.cliente = anthropic.Anthropic()

    @staticmethod
    def _respuesta(msg: Any) -> Respuesta:
        texto = None
        if msg.stop_reason not in ("refusal", "max_tokens"):
            texto = next((b.text for b in msg.content if b.type == "text"), None)
        return Respuesta(texto, msg.usage.input_tokens, msg.usage.output_tokens, msg.stop_reason)

    def enviar(self, solicitudes: list[dict], lotes: bool) -> dict[str, Respuesta]:
        if not lotes:
            out = {}
            for s in solicitudes:
                out[s["custom_id"]] = self._respuesta(self.cliente.messages.create(**_sin_id(s)))
            return out
        peticiones = [{"custom_id": s["custom_id"], "params": _sin_id(s)} for s in solicitudes]
        lote = self.cliente.messages.batches.create(requests=peticiones)
        while self.cliente.messages.batches.retrieve(lote.id).processing_status != "ended":
            time.sleep(self.ESPERA_S)
        out = {}
        for r in self.cliente.messages.batches.results(lote.id):
            if r.result.type == "succeeded":
                out[r.custom_id] = self._respuesta(r.result.message)
        return out


class SimuladoBackend:
    """Backend determinista para tests: `responder(solicitud) -> texto JSON`."""

    def __init__(self, responder: Callable[[dict], str], tokens: tuple[int, int] = (1000, 500)):
        self.responder, self.tokens, self.llamadas = responder, tokens, 0

    def enviar(self, solicitudes: list[dict], lotes: bool) -> dict[str, Respuesta]:
        self.llamadas += len(solicitudes)
        return {
            s["custom_id"]: Respuesta(self.responder(s), *self.tokens, "end_turn")
            for s in solicitudes
        }
