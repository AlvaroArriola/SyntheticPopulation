"""Comprobaciones de la puerta F3 sobre `data/processed/targets/` (docs/04, G3.1–G3.6)."""

from __future__ import annotations

import polars as pl

from sinpop.targets import run

UMBRAL_TOTAL = 1e-3  # G3.1: < 0,1 %
UMBRAL_COHERENCIA = 1e-6  # G3.2: diferencia relativa entre marginales (solo redondeo)
UMBRAL_DERECHO_VOTO = 0.05  # G3.6: < 5 %


def ficheros() -> dict[str, pl.DataFrame]:
    import json

    meta = json.loads((run.DESTINO / "metadata.json").read_text(encoding="utf-8"))["salidas"]
    return {t: pl.read_parquet(run.DESTINO / i["fichero"]) for t, i in sorted(meta.items())}


def totales_oficiales(territorio: str) -> dict[str, float]:
    """Totales oficiales por universo para ES, CCAA y provincias."""
    from sinpop import INTERIM_DIR
    from sinpop.targets.build import provincias_de

    ps = provincias_de(territorio)
    f = pl.col("provincia").is_in(ps)

    def s(nombre: str, col: str) -> float:
        return float(pl.read_parquet(INTERIM_DIR / f"{nombre}.parquet").filter(f)[col].sum())

    elec = pl.read_parquet(INTERIM_DIR / "elecciones_generales_2023_municipios.parquet")
    return {
        "residentes": s("ecp_total", "personas"),
        "viviendas_familiares": s("ecp_viviendas_familiares", "personas"),
        "colectivos": s("ecp_colectivos", "personas"),
        "hogares": s("ecp_hogares", "hogares"),
        "censo_electoral_residente": float(elec.filter(f)["censo_residentes"].sum()),
    }


def _variables(clave: str) -> list[str]:
    return [p.split("=", 1)[0] for p in clave.split(";")]


def g31_totales(fs: dict[str, pl.DataFrame]) -> list[str]:
    """Cada objetivo suma el total oficial de su universo (< 0,1 %). En los territorios por
    municipios no hay total oficial 2026 para los pequeños: se exige que todos los objetivos de
    residentes sumen lo mismo que `edad5_sexo`."""
    malos = []
    for t, df in fs.items():
        sumas = df.group_by("objetivo", "universo").agg(pl.col("valor").sum())
        if t.startswith("MUNIS:"):
            ref = sumas.filter(pl.col("objetivo") == "edad5_sexo")["valor"].item()
            tot = {"residentes": ref}
        else:
            tot = totales_oficiales(t)
        for o, u, v in sumas.iter_rows():
            if u not in tot:  # censo_electoral autonómico: ver G3.6
                continue
            if abs(v - tot[u]) / tot[u] >= UMBRAL_TOTAL:
                malos.append(f"{t} {o}: {v:,.0f} frente a {tot[u]:,.0f}")
    return malos


def g32_coherencia(fs: dict[str, pl.DataFrame]) -> list[str]:
    """Marginales comunes coherentes: para cada variable que aparece en varios objetivos del
    mismo universo, el reparto por esa variable es el mismo en todos ellos."""
    malos = []
    for t, df in fs.items():
        largo = df.with_columns(pl.col("clave").str.split(";").alias("partes")).explode("partes")
        largo = largo.with_columns(
            pl.col("partes").str.split_exact("=", 1).struct.rename_fields(["var", "cat"])
        ).unnest("partes")
        g = largo.group_by("universo", "objetivo", "var", "cat").agg(pl.col("valor").sum())
        varios = g.group_by("universo", "var").agg(pl.col("objetivo").n_unique().alias("n"))
        varios = varios.filter(pl.col("n") > 1)
        g = g.join(varios.select("universo", "var"), on=["universo", "var"])
        d = g.group_by("universo", "var", "cat").agg(
            ((pl.col("valor").max() - pl.col("valor").min()) / pl.col("valor").max()).alias("d")
        )
        for u, v, c, x in d.filter(pl.col("d") > UMBRAL_COHERENCIA).iter_rows():
            malos.append(f"{t} [{u}] {v}={c}: diferencia relativa {x:.2e}")
    return malos


def g33_ccaa_suman_espana(fs: dict[str, pl.DataFrame]) -> list[str]:
    ccaa = [df for t, df in fs.items() if t.startswith("CCAA:")]
    if "ES" not in fs or len(ccaa) != 19:
        return ["faltan España o alguna de las 19 comunidades"]
    s = pl.concat(ccaa).group_by("objetivo", "clave").agg(pl.col("valor").sum())
    j = s.join(
        fs["ES"].select("objetivo", "clave", pl.col("valor").alias("es")),
        on=["objetivo", "clave"],
        how="full",
        coalesce=True,
    ).fill_null(0.0)
    m = j.filter((pl.col("valor") - pl.col("es")).abs() > 1e-3)
    return [f"{o} {c}: {v} frente a {e}" for o, c, v, e in m.head(10).iter_rows()]


def g35_metadatos(fs: dict[str, pl.DataFrame]) -> list[str]:
    malos = []
    for t, df in fs.items():
        for c in ("fuente", "edicion", "fecha_referencia", "metodo"):
            n = df[c].null_count() + (df[c].cast(pl.Utf8) == "").sum()
            if n:
                malos.append(f"{t}: {n} filas sin {c}")
    return malos


def g36_electorales(fs: dict[str, pl.DataFrame]) -> tuple[list[str], dict[str, float]]:
    """Generales: las opciones suman el censo de residentes (100 %) y el censo es coherente con
    los españoles de 18 y más años de los objetivos (< 5 %, documentado). Autonómicas: cada
    comunidad suma sus electores publicados (o sus votantes en Aragón)."""
    malos, difs = [], {}
    for t, df in fs.items():
        vg = df.filter(pl.col("objetivo") == "voto_generales_2023")["valor"].sum()
        ad = df.filter(
            (pl.col("objetivo") == "adultos_nacionalidad")
            & (pl.col("clave") == "nacionalidad_esp_ext=espanola;es_adulto=si")
        )["valor"].sum()
        if not t.startswith("MUNIS:"):
            censo = totales_oficiales(t)["censo_electoral_residente"]
            if abs(vg - censo) > 1e-3:
                malos.append(f"{t}: las opciones suman {vg:,.0f} y el censo es {censo:,.0f}")
        if ad:
            difs[t] = vg / ad - 1
            if abs(difs[t]) >= UMBRAL_DERECHO_VOTO:
                malos.append(
                    f"{t}: censo de residentes 2023 {vg:,.0f} frente a españoles 18+ "
                    f"2026 {ad:,.0f} ({100 * difs[t]:+.1f} %)"
                )
    return malos, difs
