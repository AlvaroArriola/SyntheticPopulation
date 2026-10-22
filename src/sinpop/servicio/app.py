"""Servicio de consulta local (F13; `docs/04`; D-075).

Una API HTTP sobre las funciones ya validadas, sin reimplementar ningún método:

- `GET  /api/territorios`  límites de España, comunidades y provincias (INE) y poblaciones listas;
- `GET  /api/poblaciones`  poblaciones generadas y sus capas;
- `POST /api/poblaciones`  genera una población (`synth`) con sus capas de opinión y política;
- `POST /api/preguntas`    predice una pregunta (`predict.salida.predecir_dict`, formato §2.8);
- `POST /api/eventos`      efecto de un evento sobre una pregunta (`predict.evento`);
- `GET  /api/trabajos/{id}` estado y resultado de un trabajo en segundo plano;
- `GET  /api/banco`        preguntas parecidas del banco del CIS y datos de la población (INE…);
- `GET  /api/atributos/{v}` distribución de un dato de la población (D-077);
- `GET  /api/tamano`       asistente de tamaño según el margen deseado (D-079);
- `POST /api/informe`      informe PDF de un resultado (D-078);
- `POST /api/comparar`     la misma pregunta en cada comunidad con su propia población (D-080);
- `GET  /api/llm`          gasto acumulado del modelo de lenguaje frente al tope;
- `GET  /api/ficha/{run}`  ficha de datos de una población.

Los trabajos (generar una población, predecir) usan un solo hilo: son cálculos pesados y en un
equipo normal es mejor encadenarlos que competir por la memoria. Nada de aquí lee la ventana de
evaluación (regla 5) ni devuelve microdatos originales: solo agregados y la población sintética.

Comando: `sinpop serve` (por defecto http://127.0.0.1:8000).
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import threading
import traceback
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from pydantic import BaseModel, Field

from sinpop import POPULATIONS_DIR, REPORTS_DIR

WEB = Path(__file__).parent / "web"
FECHA = "2026-01-01"
TAMANOS = [10_000, 50_000, 100_000, 500_000, 1_000_000]
CAPAS = ["persons.parquet", "opinion.parquet", "politics.parquet"]
# categorías del recuerdo de voto que no son familias de partidos (politics/recuerdo.py)
SITUACIONES_VOTO = [
    ("abstencion", "Abstención"),
    ("blanco", "Voto en blanco"),
    ("nulo", "Voto nulo"),
    ("no_tenia_edad", "No tenía edad para votar"),
    ("sin_derecho_voto", "Sin derecho a voto"),
]

_pool = ThreadPoolExecutor(max_workers=1)
_trabajos: dict[str, dict] = {}
_cerrojo = threading.Lock()


# ---------------------------------------------------------------------------- poblaciones


def run_id(territorio: str, tamano: int, semilla: int = 1) -> str:
    return f"{FECHA}_{territorio.replace(':', '_')}_{tamano}_s{semilla}"


def poblaciones() -> list[dict]:
    from sinpop import paquete as PK

    if PK.activo():  # paquete portable (D-076): solo las poblaciones que trae
        return [json.loads(f.read_text("utf-8")) for f in sorted(PK.ruta("marcos").glob("*.json"))]
    out = []
    for d in sorted(POPULATIONS_DIR.glob(f"{FECHA}_*")):
        meta_f = d / "metadata.json"
        if not meta_f.exists() or not (d / "persons.parquet").exists():
            continue
        meta = json.loads(meta_f.read_text("utf-8"))
        t = meta.get("territorio") or {}
        codigo = t.get("codigo") if isinstance(t, dict) else str(t)
        if not codigo or codigo.startswith("MUNIS"):
            continue
        if d.name != run_id(
            codigo, int(meta.get("tamano_solicitado", 0) or 0), int(meta.get("semilla", 0))
        ):
            continue  # variantes de ensayos (sufijos), no se ofrecen
        out.append(
            {
                "run_id": d.name,
                "territorio": codigo,
                "tamano": meta.get("tamano_obtenido") or meta.get("tamano_solicitado"),
                "tamano_solicitado": meta.get("tamano_solicitado"),
                "semilla": meta.get("semilla"),
                "capas": {c.split(".")[0]: (d / c).exists() for c in CAPAS},
                "lista": all((d / c).exists() for c in CAPAS),
                "ficha": (REPORTS_DIR / d.name / "ficha.md").exists(),
            }
        )
    return out


def _generar(territorio: str, tamano: int, semilla: int, avance) -> dict:
    from sinpop.opinion import run as OR
    from sinpop.politics import run as PR
    from sinpop.synth.poblacion import construir

    rid = run_id(territorio, tamano, semilla)
    d = POPULATIONS_DIR / rid
    if not (d / "persons.parquet").exists():
        avance("Generando la población (calibración a las cifras oficiales)…")
        construir(territorio, tamano, semilla, None)
    if not (d / "opinion.parquet").exists():
        avance("Asignando opinión y valores…")
        OR.construir(rid)
    if not (d / "politics.parquet").exists():
        avance("Asignando la capa política (calibrada a resultados oficiales)…")
        PR.construir(rid)
    return next(p for p in poblaciones() if p["run_id"] == rid)


# ---------------------------------------------------------------------------- trabajos


def _lanzar(tipo: str, funcion, *args) -> str:
    tid = uuid.uuid4().hex[:12]
    with _cerrojo:
        _trabajos[tid] = {
            "id": tid,
            "tipo": tipo,
            "estado": "en_cola",
            "mensaje": "En cola…",
            "creado": dt.datetime.now().isoformat(timespec="seconds"),
        }

    def avance(msg: str) -> None:
        with _cerrojo:
            _trabajos[tid]["mensaje"] = msg

    def ejecutar() -> None:
        with _cerrojo:
            _trabajos[tid]["estado"] = "en_curso"
        try:
            res = funcion(*args, avance)
            with _cerrojo:
                _trabajos[tid] |= {"estado": "hecho", "resultado": res, "mensaje": "Listo"}
        except Exception as e:  # noqa: BLE001 - el error se devuelve a la interfaz
            with _cerrojo:
                _trabajos[tid] |= {
                    "estado": "error",
                    "mensaje": str(e),
                    "traza": traceback.format_exc(limit=3),
                }

    _pool.submit(ejecutar)
    return tid


def _predecir(q: dict, rid: str, avance) -> dict:
    from sinpop.predict import salida as S

    avance("Buscando preguntas parecidas y aplicando el modelo a la población…")
    return S.predecir_dict(q, rid)


def _comparar(q: dict, runs: list[str], avance) -> dict:
    """La misma pregunta sobre la población propia de cada territorio, sin LLM (D-080)."""
    from sinpop.predict import salida as S

    out = {}
    for i, rid in enumerate(runs, 1):
        avance(f"Territorio {i} de {len(runs)}…")
        r = S.predecir_dict(q, rid, permitir_llm=False)
        out[r.get("territorio") or rid] = {
            "run_id": rid,
            "total": r["total"],
            "confianza": r["confianza"]["total"],
        }
    return {"territorios": out, "opciones": q["opciones"]}


def _evento(q: dict, ev: dict, rid: str, avance) -> dict:
    from sinpop.predict import estimador as E
    from sinpop.predict import evento as V
    from sinpop.predict import opciones as O

    avance("Calculando el antes y el efecto del evento…")
    pq = E.Pregunta(
        q["id"],
        q["enunciado"],
        q["opciones"],
        q.get("escala") or O.escala_probable(q["opciones"]),
        ev["fecha"][:7],
        [],
    )
    out = V.predecir_pregunta(
        pq, ev["descripcion"], dt.date.fromisoformat(ev["fecha"]), ev.get("ambito", "ES"), rid
    )
    from sinpop.predict.salida import AVISO

    return {"id": q["id"], "run_id": rid, "resultado_simulado": True, "aviso": AVISO, **out}


def _id_pregunta(enunciado: str, opciones: list[str]) -> str:
    h = hashlib.sha256(json.dumps([enunciado, opciones], ensure_ascii=False).encode()).hexdigest()
    return f"UI-{h[:10]}"


def etiquetas_subgrupos() -> dict:
    """Nombres legibles de los códigos de los subgrupos, leídos de la configuración."""
    from sinpop.config import load_config

    ter = load_config("territories.yaml")
    par = load_config("partidos.yaml")
    return {
        "ccaa": {c.codigo: c.nombre for c in ter.ccaa},  # type: ignore[attr-defined]
        "provincia": {c.codigo: c.nombre for c in ter.provincias},  # type: ignore[attr-defined]
        "recuerdo_voto_generales_familia": {f.id: f.nombre for f in par.familias}  # type: ignore[attr-defined]
        | dict(SITUACIONES_VOTO),
        "sexo": {"hombre": "Hombres", "mujer": "Mujeres"},
        "estudios_3": {
            "hasta_obligatoria": "Hasta obligatoria",
            "secundaria_2a_etapa": "Secundaria 2.ª etapa",
            "superior": "Superior",
        },
        "dimensiones": {
            "edad_4": "Edad",
            "sexo": "Sexo",
            "estudios_3": "Estudios",
            "ccaa": "Comunidad",
            "recuerdo_voto_generales_familia": "Recuerdo de voto 2023",
        },
    }


# ---------------------------------------------------------------------------- aplicación


class PeticionPoblacion(BaseModel):
    territorio: str = Field(pattern=r"^(ES|CCAA:\d{2}|PROV:\d{2})$")
    tamano: int
    semilla: int = 1


class PeticionPregunta(BaseModel):
    run_id: str
    enunciado: str = Field(min_length=3)
    opciones: list[str] = Field(min_length=2)
    escala: str | None = None
    subgrupos: list[str] | None = None
    fecha_referencia: str = "2026-07"


class PeticionComparar(BaseModel):
    enunciado: str = Field(min_length=3)
    opciones: list[str] = Field(min_length=2)
    nivel: str = Field(default="CCAA", pattern=r"^(CCAA|PROV)$")


class PeticionInforme(BaseModel):
    tipo: str = Field(pattern=r"^(pregunta|dato)$")
    datos: dict
    contexto: dict = {}


class PeticionEvento(PeticionPregunta):
    descripcion: str = Field(min_length=3)
    fecha: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    ambito: str = "ES"


def crear_app():
    from fastapi import FastAPI, HTTPException
    from fastapi.responses import FileResponse, PlainTextResponse
    from fastapi.staticfiles import StaticFiles

    app = FastAPI(
        title="sinpop", description="Población sintética de España (resultados simulados)"
    )

    def _comprobar_run(rid: str) -> None:
        p = next((x for x in poblaciones() if x["run_id"] == rid), None)
        if p is None or not p["lista"]:
            raise HTTPException(404, f"la población {rid} no existe o no tiene sus capas")

    @app.get("/api/territorios")
    def territorios():
        return FileResponse(WEB / "territorios.geojson", media_type="application/geo+json")

    @app.get("/api/poblaciones")
    def listar():
        return {"poblaciones": poblaciones(), "tamanos": TAMANOS}

    @app.post("/api/poblaciones")
    def generar(p: PeticionPoblacion):
        if p.tamano not in TAMANOS:
            raise HTTPException(422, f"tamaño no admitido; usa uno de {TAMANOS}")
        from sinpop import paquete as PK

        if PK.activo():
            raise HTTPException(
                409,
                "Con el paquete portable no se pueden generar poblaciones nuevas: hacen falta los "
                "microdatos del Censo. Elige una de las poblaciones incluidas.",
            )
        rid = run_id(p.territorio, p.tamano, p.semilla)
        ya = next((x for x in poblaciones() if x["run_id"] == rid and x["lista"]), None)
        if ya:
            return {"run_id": rid, "trabajo": None, "poblacion": ya}
        return {
            "run_id": rid,
            "trabajo": _lanzar("poblacion", _generar, p.territorio, p.tamano, p.semilla),
        }

    @app.post("/api/preguntas")
    def preguntar(p: PeticionPregunta):
        _comprobar_run(p.run_id)
        q = {
            "id": _id_pregunta(p.enunciado, p.opciones),
            "tipo": "pregunta",
            "enunciado": p.enunciado,
            "opciones": p.opciones,
            "fecha_referencia": p.fecha_referencia,
        }
        if p.escala:
            q["escala"] = p.escala
        if p.subgrupos is not None:
            q["subgrupos"] = p.subgrupos
        return {"trabajo": _lanzar("pregunta", _predecir, q, p.run_id)}

    @app.post("/api/comparar")
    def comparar(p: PeticionComparar):
        """Compara una pregunta entre las comunidades con poblaciones listas (D-080)."""
        runs = sorted(
            x["run_id"]
            for x in poblaciones()
            if x["lista"] and x["territorio"].startswith(p.nivel + ":") and x["semilla"] == 1
        )
        # una población por territorio: la más grande
        por_ter: dict[str, str] = {}
        for x in sorted(poblaciones(), key=lambda x: x["tamano_solicitado"]):
            if x["run_id"] in runs:
                por_ter[x["territorio"]] = x["run_id"]
        if len(por_ter) < 2:
            raise HTTPException(409, "hacen falta al menos dos territorios con población lista")
        q = {
            "id": _id_pregunta(p.enunciado, p.opciones),
            "tipo": "pregunta",
            "enunciado": p.enunciado,
            "opciones": p.opciones,
        }
        return {
            "trabajo": _lanzar("comparar", _comparar, q, list(por_ter.values())),
            "territorios": len(por_ter),
        }

    @app.post("/api/eventos")
    def evento(p: PeticionEvento):
        _comprobar_run(p.run_id)
        q = {
            "id": _id_pregunta(p.enunciado, p.opciones),
            "enunciado": p.enunciado,
            "opciones": p.opciones,
        }
        if p.escala:
            q["escala"] = p.escala
        ev = {"descripcion": p.descripcion, "fecha": p.fecha, "ambito": p.ambito}
        return {"trabajo": _lanzar("evento", _evento, q, ev, p.run_id)}

    @app.get("/api/trabajos/{tid}")
    def trabajo(tid: str):
        with _cerrojo:
            t = _trabajos.get(tid)
            if t is None:
                raise HTTPException(404, "trabajo desconocido")
            return dict(t)

    @app.get("/api/banco")
    def banco(q: str, k: int = 6):
        from sinpop.predict import atributos as AT
        from sinpop.predict import recuperar as R

        if len(q.strip()) < 4:
            return {"preguntas": [], "atributos": []}
        d = R.indice().similares(q, [], min(k, 20))
        return {
            "atributos": AT.buscar(q),
            "preguntas": [
                {
                    "id": r["id"],
                    "fecha": r["fecha"][:7],
                    "enunciado": r["enunciado"],
                    "opciones": r["opciones"],
                    "similitud": round(float(r["similitud"]), 3),
                }
                for r in d.iter_rows(named=True)
            ],
        }

    @app.get("/api/atributos/{variable}")
    def atributo(variable: str, run_id: str):
        """Dato de la población: distribución ponderada de un atributo calibrado con fuentes
        oficiales (D-077). No es una predicción: no lleva modelo de confianza."""
        from sinpop.predict import atributos as AT

        _comprobar_run(run_id)
        if variable not in AT.catalogo():
            raise HTTPException(404, "atributo desconocido")
        from sinpop.predict.salida import AVISO

        return {**AT.distribucion(variable, run_id), "run_id": run_id, "aviso": AVISO}

    @app.get("/api/tamano")
    def tamano(territorio: str, margen: float = 0.01, detalle: str = "grupos"):
        """Asistente de tamaño (D-079): margen de simulación por tamaño y techo de confianza."""
        from sinpop.servicio import tamano as T

        if detalle not in T.DETALLES or not 0.001 <= margen <= 0.2:
            raise HTTPException(422, "detalle o margen fuera de rango")
        return T.recomendar(territorio, margen, detalle, TAMANOS)

    @app.get("/api/etiquetas")
    def etiquetas():
        return etiquetas_subgrupos()

    @app.post("/api/informe")
    def informe(p: PeticionInforme):
        """Informe PDF de un resultado que ya tiene la interfaz (D-078)."""
        from fastapi.responses import Response

        from sinpop.servicio import informe as INF

        pdf = INF.generar(p.tipo, p.datos, p.contexto, etiquetas_subgrupos())
        return Response(
            pdf,
            media_type="application/pdf",
            headers={"Content-Disposition": 'attachment; filename="informe_espana_sintetica.pdf"'},
        )

    @app.get("/api/modo")
    def modo():
        from sinpop import paquete as PK

        return {"paquete": PK.activo()}

    @app.get("/api/llm")
    def llm():
        from sinpop.llm import cliente as C

        c = C._cfg()
        return {
            "activo": c.activo,
            "credenciales": C.credenciales(),
            "gastado_eur": round(C.gasto_total(), 4),
            "tope_total_eur": c.presupuesto.eur_max_total,
        }

    @app.get("/api/ficha/{rid}", response_class=PlainTextResponse)
    def ficha(rid: str):
        from sinpop import paquete as PK

        f = PK.ruta("fichas", f"{rid}.md") if PK.activo() else REPORTS_DIR / rid / "ficha.md"
        if not f.exists():
            raise HTTPException(404, "esta población no tiene ficha de datos")
        return f.read_text("utf-8")

    app.mount("/", StaticFiles(directory=WEB, html=True), name="web")
    return app


def servir(host: str = "127.0.0.1", puerto: int = 8000) -> None:
    import uvicorn

    uvicorn.run(crear_app(), host=host, port=puerto, log_level="info")
