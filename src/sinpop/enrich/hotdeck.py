"""Hot-deck aleatorio ponderado por celdas con colapso jerárquico (D-044.1).

Cada receptor recibe un donante sorteado con probabilidad proporcional a su peso entre los
donantes de su celda de llaves. Si la celda tiene menos de `k_min` donantes, se quita la última
llave de la lista y se vuelve a intentar; las llaves `fijas` no se quitan nunca. Una llave con
valor desconocido en el receptor (NC, NS) no se usa para ese receptor. Así se reproduce la
distribución condicionada ponderada de la encuesta y se asignan valores reales de donantes.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import polars as pl

DESCONOCIDOS = ("NC", "NS")


@dataclass
class Asignacion:
    donante: np.ndarray  # fila del donante (índice en `donantes`) para cada receptor
    nivel: np.ndarray  # índice del nivel de colapso usado por cada receptor


def _clave(cols: list[str]) -> pl.Expr:
    if not cols:
        return pl.lit("·")
    return pl.concat_str([pl.col(c).cast(pl.Utf8) for c in cols], separator="|")


def niveles_colapso(llaves: list[str], geografia: list[str | None]) -> list[list[str]]:
    """Secuencia de celdas: con todas las llaves, primero en la geografía más fina y luego en
    las más amplias (`None` = España); después se quita la última llave y se repite."""
    out = []
    for nk in range(len(llaves), -1, -1):
        for g in geografia:
            out.append([*([g] if g else []), *llaves[:nk]])
    return out


def niveles_nucleo(llaves: list[str], geografia: list[str | None], nucleo: int) -> list[list[str]]:
    """Secuencia de celdas que conserva la geografía fina mientras queden las `nucleo` llaves
    más importantes: primero se quitan las llaves secundarias en la comunidad, después se amplía
    la geografía (con todas las llaves y quitando las secundarias), y solo al final se quitan
    llaves del núcleo."""
    out: list[list[str]] = []
    for g in geografia:
        for nk in range(len(llaves), nucleo - 1, -1):
            out.append([*([g] if g else []), *llaves[:nk]])
    for nk in range(nucleo - 1, -1, -1):
        for g in geografia:
            out.append([*([g] if g else []), *llaves[:nk]])
    return out


def celdas(
    receptores: pl.DataFrame,
    donantes: pl.DataFrame,
    niveles: list[list[str]],
    fijas: list[str],
    k_min: int,
) -> tuple[np.ndarray, np.ndarray, pl.DataFrame]:
    """Celda de cada receptor: (id de celda, índice del nivel usado) y la tabla de donantes con
    su celda (`_c`, `_d` = fila original); receptores y donantes comparten los ids de celda.
    `niveles`: listas de llaves de la más fina a la más gruesa; las `fijas` se añaden siempre."""
    todas = list(dict.fromkeys(c for n in niveles for c in n))
    r = receptores.select([*fijas, *todas]).with_row_index("_r")
    d = donantes.select([*fijas, *todas]).with_row_index("_d")
    celda_r = np.full(r.height, -1, dtype=np.int64)
    nivel_r = np.full(r.height, -1, dtype=np.int64)
    trozos = []
    base = 0
    pendientes = r
    for nivel, usadas in enumerate(niveles):
        if pendientes.is_empty():
            break
        # Patrones de llaves desconocidas en el receptor: esas llaves no se usan para él
        desc = [
            pl.col(c).cast(pl.Utf8).is_in(DESCONOCIDOS).alias(f"_x{i}")
            for i, c in enumerate(usadas)
        ]
        pend = pendientes.with_columns(desc) if usadas else pendientes
        patrones = (
            pend.select([f"_x{i}" for i in range(len(usadas))]).unique().rows() if usadas else [()]
        )
        asignados = []
        for pat in sorted(patrones):
            cols = [*fijas, *[c for c, x in zip(usadas, pat, strict=True) if not x]]
            sel = pend
            for i, x in enumerate(pat):
                sel = sel.filter(pl.col(f"_x{i}") == x)
            dc = (
                d.with_columns(_clave(cols).alias("_k"))
                .group_by("_k")
                .agg(pl.col("_d"))
                .filter(pl.col("_d").list.len() >= k_min)
                .sort("_k")
                .with_row_index("_c", offset=base)
            )
            if dc.is_empty():
                continue
            base += dc.height
            j = sel.with_columns(_clave(cols).alias("_k")).join(dc.select("_k", "_c"), on="_k")
            if j.is_empty():
                continue
            ri = j["_r"].to_numpy()
            celda_r[ri] = j["_c"].to_numpy()
            nivel_r[ri] = nivel
            asignados.append(j.select("_r"))
            trozos.append(dc.select("_c", "_d").explode("_d"))
        if asignados:
            hechos = pl.concat(asignados)
            pendientes = pendientes.join(hechos, on="_r", how="anti")
    if (celda_r < 0).any():
        n = int((celda_r < 0).sum())
        raise ValueError(f"{n} receptores sin donantes ni con las llaves fijas {fijas}")
    tabla = pl.concat(trozos) if trozos else pl.DataFrame(schema={"_c": pl.UInt32, "_d": pl.UInt32})
    return (
        celda_r,
        nivel_r,
        tabla.with_columns(pl.col("_c").cast(pl.Int64), pl.col("_d").cast(pl.Int64)),
    )


def muestrear(
    celda_r: np.ndarray, tabla: pl.DataFrame, pesos: np.ndarray, rng: np.random.Generator
) -> np.ndarray:
    """Un donante por receptor, con probabilidad ∝ peso dentro de su celda (búsqueda en la
    suma acumulada de los pesos ordenados por celda)."""
    t = tabla.sort("_c", "_d")
    c = t["_c"].to_numpy()
    dn = t["_d"].to_numpy()
    w = pesos[dn].astype(float)
    if (w < 0).any() or not np.isfinite(w).all():
        raise ValueError("pesos de donantes no válidos")
    acum = np.cumsum(w)
    ini = np.searchsorted(c, np.arange(c.max() + 1), side="left") if len(c) else np.array([])
    fin = np.searchsorted(c, np.arange(c.max() + 1), side="right") if len(c) else np.array([])
    antes = np.where(ini > 0, acum[np.maximum(ini - 1, 0)], 0.0)
    total = acum[fin - 1] - antes
    u = rng.random(len(celda_r))
    objetivo = antes[celda_r] + u * total[celda_r]
    pos = np.searchsorted(acum, objetivo, side="right")
    pos = np.clip(pos, ini[celda_r], fin[celda_r] - 1)
    return dn[pos]


def emparejar(
    receptores: pl.DataFrame,
    donantes: pl.DataFrame,
    niveles: list[list[str]],
    peso: str,
    rng: np.random.Generator,
    fijas: list[str] | None = None,
    k_min: int = 10,
) -> Asignacion:
    fijas = fijas or []
    celda_r, nivel, tabla = celdas(receptores, donantes, niveles, fijas, k_min)
    dn = muestrear(celda_r, tabla, donantes[peso].to_numpy(), rng)
    return Asignacion(donante=dn, nivel=nivel)
