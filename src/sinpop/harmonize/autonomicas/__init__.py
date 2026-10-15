"""Resultados oficiales de las últimas elecciones autonómicas (F2, G2.6; D-023).

Cada comunidad tiene su lector en `ccaa_XX.py`, con la función

    leer(path: Path) -> Resultado

que extrae de la publicación oficial (boletín o acta de la junta electoral) los resultados
por circunscripción y, si la publicación lo trae, el total de la comunidad. Ningún número se
completa ni se deduce fuera del PDF: si un dato no aparece, queda a `None` y se documenta.

Comprobaciones (`Resultado.errores()`), que deben dar una lista vacía:
- por circunscripción: votantes = válidos + nulos; válidos = votos a candidaturas + blancos
  (si la publicación da los válidos o los votos a candidaturas, también se contrastan);
- si hay total publicado: la suma de las circunscripciones reproduce cada cifra del total.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import polars as pl

from sinpop import RAW_DIR

AUTONOMICAS = RAW_DIR / "resultados_autonomicas"


@dataclass
class Circunscripcion:
    codigo: str  # provincia INE (2 cifras); isla o circunscripción: "<prov>-<sufijo>"
    nombre: str
    electores: int | None  # total de electores del acta (incluido CERA si el acta lo incluye)
    votantes: int
    nulos: int
    blancos: int
    votos: dict[str, int]  # candidatura (nombre tal como figura en la publicación) → votos
    escanos: dict[str, int] = field(default_factory=dict)
    validos: int | None = None  # solo si la publicación lo da
    a_candidaturas: int | None = None  # solo si la publicación lo da
    notas: str | None = None

    def errores(self) -> list[str]:
        out = []
        validos = sum(self.votos.values()) + self.blancos
        if self.votantes != validos + self.nulos:
            out.append(
                f"{self.nombre}: votantes {self.votantes} ≠ candidaturas + blancos + nulos "
                f"{validos + self.nulos}"
            )
        if self.validos is not None and self.validos != validos:
            out.append(f"{self.nombre}: válidos publicados {self.validos} ≠ {validos}")
        if self.a_candidaturas is not None and self.a_candidaturas != sum(self.votos.values()):
            out.append(f"{self.nombre}: votos a candidaturas publicados ≠ suma de candidaturas")
        if self.electores is not None and self.votantes > self.electores:
            out.append(f"{self.nombre}: más votantes que electores")
        return out


@dataclass
class Resultado:
    ccaa: str  # código INE de la comunidad (2 cifras)
    eleccion: str  # id de configs/elecciones.yaml
    circunscripciones: list[Circunscripcion]
    total: Circunscripcion | None = None  # total de la comunidad, si la publicación lo da
    notas: list[str] = field(default_factory=list)

    def errores(self) -> list[str]:
        out = [e for c in self.circunscripciones for e in c.errores()]
        if self.total is not None:
            out += self.total.errores()
            cs = self.circunscripciones
            for campo in ("electores", "votantes", "nulos", "blancos"):
                t = getattr(self.total, campo)
                s = sum(getattr(c, campo) or 0 for c in cs)
                if t is not None and t != s:
                    out.append(f"total {campo}: publicado {t} ≠ suma {s}")
            suma: dict[str, int] = {}
            for c in cs:
                for k, v in c.votos.items():
                    suma[k] = suma.get(k, 0) + v
            for k, v in self.total.votos.items():
                if suma.get(k, 0) != v:
                    out.append(f"total {k}: publicado {v} ≠ suma {suma.get(k, 0)}")
        return out

    def frames(self) -> tuple[pl.DataFrame, pl.DataFrame]:
        """(resumen por circunscripción, votos y escaños por circunscripción y candidatura)."""
        res = pl.DataFrame(
            [
                {
                    "eleccion": self.eleccion,
                    "ccaa": self.ccaa,
                    "circunscripcion": c.codigo,
                    "nombre": c.nombre,
                    "electores": c.electores,
                    "votantes": c.votantes,
                    "nulos": c.nulos,
                    "blancos": c.blancos,
                    "validos": sum(c.votos.values()) + c.blancos,
                }
                for c in self.circunscripciones
            ],
            schema_overrides={"electores": pl.Int64},
        )
        vot = pl.DataFrame(
            [
                {
                    "eleccion": self.eleccion,
                    "ccaa": self.ccaa,
                    "circunscripcion": c.codigo,
                    "candidatura": k,
                    "votos": v,
                    "escanos": c.escanos.get(k),
                }
                for c in self.circunscripciones
                for k, v in c.votos.items()
            ],
            schema_overrides={"escanos": pl.Int64},
        )
        return res, vot


# Comunidades cuyos resultados oficiales están incompletos (D-023): no superan G2.6
INCOMPLETAS = {"04": "solo voto CERA; faltan los resultados generales (MANUAL_DOWNLOADS.md)"}


def lector(ccaa: str):
    """Función `leer` del módulo `ccaa_XX`, o None si aún no existe."""
    import importlib

    try:
        return importlib.import_module(f"sinpop.harmonize.autonomicas.ccaa_{ccaa}").leer
    except ModuleNotFoundError:
        return None


def todas() -> dict[str, dict]:
    """Lee las 19 comunidades y devuelve, por comunidad, errores, pendientes y un resumen."""
    out = {}
    for i in range(1, 20):
        c = f"{i:02d}"
        leer = lector(c)
        if leer is None:
            out[c] = {"errores": [], "pendiente": True, "resumen": "sin lector", "resultado": None}
            continue
        r = leer()
        err = r.errores()
        pend = c in INCOMPLETAS
        resumen = f"{len(r.circunscripciones)} circunscripciones"
        if err:
            resumen += f"; {len(err)} errores: {err[0]}"
        if pend:
            resumen += f"; {INCOMPLETAS[c]}"
        out[c] = {"errores": err, "pendiente": pend, "resumen": resumen, "resultado": r}
    return out
