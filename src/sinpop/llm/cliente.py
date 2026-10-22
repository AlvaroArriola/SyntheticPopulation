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
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

import jsonschema

from sinpop import REPO_ROOT
from sinpop.config import load_config
from sinpop.llm import prompts as P
from sinpop.llm import validadores as VAL

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
    spec: dict | None = None  # comprobación semántica (llm/validadores.py)


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


# Variable propia del proyecto: si la clave se guardara como ANTHROPIC_API_KEY, la usarían también
# otras herramientas del entorno (por ejemplo, el propio agente de código) y gastarían de ella.
VARIABLE_CLAVE = "SINPOP_ANTHROPIC_API_KEY"


def _clave() -> str | None:
    return os.environ.get(VARIABLE_CLAVE) or os.environ.get("ANTHROPIC_API_KEY")


def credenciales() -> bool:
    return bool(_clave())


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


# por debajo de este número de peticiones no se usa la API de lotes: un lote puede tardar horas y
# una consulta desde la interfaz tiene que responder en segundos (D-084)
MIN_LOTE = 10


def _usar_lote(n: int) -> bool:
    return _cfg().presupuesto.usar_lotes and n >= MIN_LOTE


def _cota(params: dict, lote: bool) -> float:
    chars = len(params["system"]) + sum(len(m["content"]) for m in params["messages"])
    chars += len(json.dumps(params["output_config"]))
    return coste_eur(params["model"], int(chars / CARACTERES_POR_TOKEN), params["max_tokens"], lote)


def estimar(peticiones: list[Peticion]) -> dict:
    """Cota superior del coste de las peticiones que no están en caché (no llama a nadie)."""
    cache, _ = _rutas()
    pend = [s for s in map(_solicitud, peticiones) if not (cache / f"{s[1]}.json").exists()]
    lote = _usar_lote(len(pend))
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


def _comprobar(salida: dict, esquema: dict, spec: dict | None) -> None:
    jsonschema.validate(salida, esquema)
    v = VAL.construir(spec)
    if v is not None:
        v(salida)


def _valida(salida: dict, esquema: dict, spec: dict | None) -> bool:
    try:
        _comprobar(salida, esquema, spec)
    except (ValueError, KeyError, jsonschema.ValidationError):
        return False
    return True


def _pendiente(p: Peticion) -> dict:
    params, clave, meta = _solicitud(p)
    return {
        "id": p.id,
        "clave": clave,
        "meta": meta,
        "params": params,
        "esquema": p.esquema,
        "spec": p.spec,
    }


def _de_cache(pend: dict) -> dict | None:
    cache, _ = _rutas()
    f = cache / f"{pend['clave']}.json"
    if not f.exists():
        return None
    salida = json.loads(f.read_text("utf-8"))["salida"]
    return salida if _valida(salida, pend["esquema"], pend["spec"]) else None


def _comprobar_presupuesto(pendientes: list[dict], lote: bool) -> None:
    c = _cfg()
    cota = sum(_cota(x["params"], lote) for x in pendientes)
    if cota > c.presupuesto.eur_max_por_ejecucion:
        raise PresupuestoExcedido(
            f"cota {cota:.2f} € > tope por ejecución {c.presupuesto.eur_max_por_ejecucion} €"
        )
    if gasto_total() + cota > c.presupuesto.eur_max_total:
        raise PresupuestoExcedido(
            f"gastado {gasto_total():.2f} € + cota {cota:.2f} € > tope total "
            f"{c.presupuesto.eur_max_total} €"
        )


def _enviar(pendientes: list[dict], backend: Backend) -> dict[str, dict | None]:
    """Envía, valida, registra el gasto y guarda en caché; reintenta las salidas inválidas."""
    c = _cfg()
    cache, registro = _rutas()
    cache.mkdir(parents=True, exist_ok=True)
    registro.parent.mkdir(parents=True, exist_ok=True)
    lote = _usar_lote(len(pendientes))
    _comprobar_presupuesto(pendientes, lote)
    out: dict[str, dict | None] = {}
    quedan = {x["id"]: x for x in pendientes}
    for _intento in range(c.reintentos_salida_invalida + 1):
        if not quedan:
            break
        resp = backend.enviar([{"custom_id": k, **v["params"]} for k, v in quedan.items()], lote)
        hechos = []
        for k, x in quedan.items():
            r = resp.get(k)
            if r is None:
                continue
            eur = coste_eur(x["params"]["model"], r.entrada, r.salida, lote)
            salida, error = None, None
            try:
                if r.texto is None:
                    raise ValueError(f"sin texto (motivo de fin: {r.motivo_fin})")
                salida = json.loads(r.texto)
                _comprobar(salida, x["esquema"], x["spec"])
            except (ValueError, KeyError, jsonschema.ValidationError) as e:
                salida, error = None, str(e)[:300]
            with registro.open("a", encoding="utf-8") as fh:
                fh.write(
                    json.dumps(
                        {
                            "fecha": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
                            "id": k,
                            "clave": x["clave"],
                            **x["meta"],
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
                guardado = {"meta": x["meta"], "salida": salida}
                (cache / f"{x['clave']}.json").write_text(
                    json.dumps(guardado, ensure_ascii=False, indent=1, sort_keys=True), "utf-8"
                )
                out[k] = salida
                hechos.append(k)
        for k in hechos:
            quedan.pop(k)
    for k in quedan:
        out[k] = None
    return out


def ejecutar(peticiones: list[Peticion], backend: Backend | None = None) -> dict[str, dict | None]:
    """Devuelve la salida validada de cada petición (o None si no se pudo obtener). Lo que ya
    está en caché no necesita credenciales ni gasta nada."""
    out: dict[str, dict | None] = {}
    pendientes = []
    for p in peticiones:
        x = _pendiente(p)
        salida = _de_cache(x)
        if salida is not None:
            out[p.id] = salida
        else:
            pendientes.append(x)
    if not pendientes:
        return out
    if backend is None:
        if not disponible():
            raise LLMNoDisponible(
                f"{len(pendientes)} peticiones sin respuesta en caché, y el LLM está desactivado "
                "o sin credenciales (o expórtalas: exportar())"
            )
        backend = AnthropicBackend()
    return out | _enviar(pendientes, backend)


# ------------------------------------------------ envío desde otra sesión (D-074)

PENDIENTES_DIR = REPO_ROOT / "logs" / "llm" / "pendientes"


def exportar(peticiones: list[Peticion], nombre: str) -> dict:
    """Escribe las peticiones sin respuesta en caché en `logs/llm/pendientes/<nombre>.jsonl`,
    para enviarlas desde un entorno que tenga la clave (`enviar_pendientes`). Solo contienen lo
    que vería el modelo: enunciados públicos y agregados (regla 8)."""
    pend = [x for x in map(_pendiente, peticiones) if _de_cache(x) is None]
    PENDIENTES_DIR.mkdir(parents=True, exist_ok=True)
    ruta = PENDIENTES_DIR / f"{nombre}.jsonl"
    ruta.write_text(
        "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in pend), "utf-8"
    )
    lote = _usar_lote(len(pend))
    return {
        "fichero": str(ruta.relative_to(REPO_ROOT) if ruta.is_relative_to(REPO_ROOT) else ruta),
        "peticiones": len(pend),
        "cota_eur": round(sum(_cota(x["params"], lote) for x in pend), 4),
    }


def _leer_pendientes(nombre: str) -> list[dict]:
    ruta = PENDIENTES_DIR / f"{nombre}.jsonl"
    return [json.loads(x) for x in ruta.read_text("utf-8").splitlines() if x.strip()]


def enviar_pendientes(nombre: str, backend: Backend | None = None) -> dict:
    """Envía un fichero de peticiones exportado (con los mismos topes de presupuesto)."""
    pend = [x for x in _leer_pendientes(nombre) if _de_cache(x) is None]
    if not pend:
        return {"enviadas": 0, "validas": 0, "gastado_total_eur": round(gasto_total(), 4)}
    if backend is None:
        if not credenciales():
            raise LLMNoDisponible(f"falta la clave en {VARIABLE_CLAVE}")
        backend = AnthropicBackend()
    out = _enviar(pend, backend)
    return {
        "enviadas": len(pend),
        "validas": sum(v is not None for v in out.values()),
        "gastado_total_eur": round(gasto_total(), 4),
    }


def _sin_id(s: dict) -> dict:
    return {k: v for k, v in s.items() if k != "custom_id"}


class AnthropicBackend:
    """Envío real con el SDK oficial de Anthropic (`pip install anthropic`)."""

    ESPERA_S = 30
    CONCURRENCIA = 8

    def __init__(self) -> None:
        import anthropic

        self.cliente = anthropic.Anthropic(api_key=_clave())

    @staticmethod
    def _respuesta(msg: Any) -> Respuesta:
        texto = None
        if msg.stop_reason not in ("refusal", "max_tokens"):
            texto = next((b.text for b in msg.content if b.type == "text"), None)
        return Respuesta(texto, msg.usage.input_tokens, msg.usage.output_tokens, msg.stop_reason)

    def enviar(self, solicitudes: list[dict], lotes: bool) -> dict[str, Respuesta]:
        if not lotes:  # directas, varias a la vez (D-085): una evaluación son ~150 llamadas
            from concurrent.futures import ThreadPoolExecutor

            def una(s: dict) -> Respuesta:
                return self._respuesta(self.cliente.messages.create(**_sin_id(s)))

            with ThreadPoolExecutor(self.CONCURRENCIA) as ex:
                res = list(ex.map(una, solicitudes))
            return {s["custom_id"]: r for s, r in zip(solicitudes, res, strict=True)}
        # la API de lotes solo admite identificadores [a-zA-Z0-9_-]{1,64}: se numeran y se
        # traducen de vuelta a los nuestros
        ids = {f"r{i}": s["custom_id"] for i, s in enumerate(solicitudes)}
        peticiones = [
            {"custom_id": f"r{i}", "params": _sin_id(s)} for i, s in enumerate(solicitudes)
        ]
        lote = self.cliente.messages.batches.create(requests=peticiones)
        while self.cliente.messages.batches.retrieve(lote.id).processing_status != "ended":
            time.sleep(self.ESPERA_S)
        out = {}
        for r in self.cliente.messages.batches.results(lote.id):
            if r.result.type == "succeeded":
                out[ids[r.custom_id]] = self._respuesta(r.result.message)
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


if __name__ == "__main__":
    import argparse

    a = argparse.ArgumentParser(description="Envío de peticiones exportadas (D-074)")
    a.add_argument("--enviar", help="nombre del fichero de logs/llm/pendientes/ (sin .jsonl)")
    a.add_argument("--estimar", help="cota del coste de un fichero exportado, sin enviar nada")
    args = a.parse_args()
    if args.estimar:
        pend = [x for x in _leer_pendientes(args.estimar) if _de_cache(x) is None]
        lote = _usar_lote(len(pend))
        print(
            json.dumps(
                {
                    "peticiones": len(pend),
                    "cota_eur": round(sum(_cota(x["params"], lote) for x in pend), 4),
                    "gastado_eur": round(gasto_total(), 4),
                    "tope_total_eur": _cfg().presupuesto.eur_max_total,
                },
                ensure_ascii=False,
            )
        )
    elif args.enviar:
        print(json.dumps(enviar_pendientes(args.enviar), ensure_ascii=False))
