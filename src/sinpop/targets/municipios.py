"""Objetivos de territorios definidos por una lista de municipios (F3, tarea 3; D-036).

Fichero de definición (YAML):

    nombre: <texto>
    descripcion: <texto, opcional>
    municipios: ["46250", "46131", ...]   # códigos INE de 5 cifras

Método. Los objetivos de cada provincia a 01/01/2026 (build.provincias) se reparten entre sus
municipios con la estructura municipal más reciente:

- edad × sexo y nacionalidad: Censo Anual exhaustivo 2025. Los municipios de menos de 10.000
  habitantes no están identificados en ese fichero (solo su clase de tamaño por provincia):
  se reparte la clase entre sus municipios en proporción a su población del Padrón 2025.
- estudios (15+) y actividad (16+) por sexo: tablas municipales del Censo Anual 2024 (una por
  provincia); los pensionistas de jubilación y de incapacidad vienen juntos y se separan con la
  proporción de su provincia y sexo. Municipios sin dato (secreto estadístico): cuotas de su
  provincia.
- grado de urbanización: el del municipio en el Censo Anual 2025 (los pequeños, el reparto de
  su clase); tamaño de municipio: el del Padrón 2025.

Así la suma de todos los municipios de una provincia reproduce el objetivo provincial.
Objetivos que solo existen a nivel provincial (no se calculan por municipio): población en
viviendas familiares y en colectivos, hogares por tamaño y tipo, estudios y actividad por
edad, estado civil.
"""

from __future__ import annotations

import json
from pathlib import Path

import polars as pl
import yaml
from pydantic import BaseModel, ConfigDict, Field, field_validator

from sinpop import INTERIM_DIR, RAW_DIR
from sinpop.harmonize.core import edad_5
from sinpop.ingest.ine_tablas import leer
from sinpop.targets import build


def solo_provincia() -> list[str]:
    """Objetivos que solo existen a nivel provincial (ámbito «provincia» en targets.yaml)."""
    from sinpop.config import load_config

    cfg = load_config("targets.yaml")
    return [o.id for o in cfg.calibrar + cfg.reservar if o.ambito == "provincia"]  # type: ignore[attr-defined]


ESTUDIOS_MUN = {
    "Educación primaria e inferior": "hasta_obligatoria",
    "Primera etapa de Educación Secundaria y similar": "hasta_obligatoria",
    "Segunda etapa de Educación Secundaria y Educación Postsecundaria no Superior": (
        "secundaria_2a_etapa"
    ),
    "Educación superior": "superior",
}
ACTIVIDAD_MUN = {
    "Ocupado/a": "ocupado",
    "Parado/a": "parado",
    "Perceptor/a pensión de incapacidad, jubilación, prejubilación": "pensionista",
    "Estudiante": "estudiante",
    "Otra situación de inactividad": "otra_inactividad",
}


class TerritorioMunicipios(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nombre: str
    descripcion: str | None = None
    municipios: list[str] = Field(min_length=1)

    @field_validator("municipios")
    @classmethod
    def _codigos(cls, v: list[str]) -> list[str]:
        malos = [m for m in v if not (len(m) == 5 and m.isdigit())]
        if malos:
            raise ValueError(f"códigos de municipio no válidos: {malos}")
        if len(set(v)) != len(v):
            raise ValueError("municipios repetidos")
        return v


def definicion(path: Path) -> TerritorioMunicipios:
    return TerritorioMunicipios.model_validate(
        yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    )


# --------------------------------------------------------------------------- reparto


def padron() -> pl.DataFrame:
    """Municipios con su población 2025 (Padrón, tabla 29005) y su clase de tamaño."""
    from sinpop.harmonize.censos import poblacion_municipal
    from sinpop.harmonize.core import tamano_por_poblacion

    pm = poblacion_municipal()
    return pm.select(
        pl.concat_str("CPRO", "CMUN").alias("municipio"),
        pl.col("CPRO").alias("provincia"),
        "poblacion",
        pl.Series("tamano_municipio", [tamano_por_poblacion(int(x)) for x in pm["poblacion"]]),
    )


def reparto() -> pl.DataFrame:
    """Peso de cada municipio dentro de su unidad del Censo Anual 2025.

    Columnas: municipio, provincia, unidad (el propio código si el municipio está identificado;
    si no, «<provincia>-<clase>»), w (1 si identificado; si no, su fracción de la población del
    Padrón de su clase en la provincia).
    """
    ex = pl.read_parquet(INTERIM_DIR / "censo_anual_exhaustivo_2025.parquet", columns=["municipio"])
    ident = set(ex["municipio"].drop_nulls().unique().to_list())
    p = padron().with_columns(pl.col("municipio").is_in(list(ident)).alias("ident"))
    no = p.filter(~pl.col("ident")).with_columns(
        pl.concat_str("provincia", pl.lit("-"), "tamano_municipio").alias("unidad"),
        (
            pl.col("poblacion") / pl.col("poblacion").sum().over("provincia", "tamano_municipio")
        ).alias("w"),
    )
    si = p.filter(pl.col("ident")).with_columns(
        pl.col("municipio").alias("unidad"), pl.lit(1.0).alias("w")
    )
    return pl.concat([si, no]).select("municipio", "provincia", "unidad", "w", "tamano_municipio")


def exhaustivo_unidades() -> pl.DataFrame:
    """Censo Anual exhaustivo 2025 por unidad de reparto (municipio identificado o clase)."""
    ex = pl.read_parquet(INTERIM_DIR / "censo_anual_exhaustivo_2025.parquet")
    return ex.with_columns(
        pl.when(pl.col("municipio").is_not_null())
        .then(pl.col("municipio"))
        .otherwise(pl.concat_str("provincia", pl.lit("-"), "tamano_municipio"))
        .alias("unidad")
    )


def repartir(
    obj_prov: pl.DataFrame, estructura: pl.DataFrame, celda: list[str], rep: pl.DataFrame
) -> pl.DataFrame:
    """Reparte las celdas provinciales (`provincia`, *celda, valor) entre municipios.

    `estructura` trae (provincia, unidad, *celda, personas) del Censo Anual 2025. Cada
    municipio recibe valor × (personas de su unidad en la celda / personas de la provincia en
    la celda) × w. Si la celda no tenía nadie en 2025, se reparte con la población total de la
    unidad (sin desagregar).
    """
    k = ["provincia", *celda]
    e = estructura.group_by("provincia", "unidad", *celda).agg(pl.col("personas").sum())
    e = e.with_columns((pl.col("personas") / pl.col("personas").sum().over(k)).alias("q"))
    tot = estructura.group_by("provincia", "unidad").agg(pl.col("personas").sum())
    tot = tot.with_columns(
        (pl.col("personas") / pl.col("personas").sum().over("provincia")).alias("q")
    )
    con = obj_prov.join(e.select(*k, "unidad", "q"), on=k)
    sin = obj_prov.join(e.select(k).unique(), on=k, how="anti").join(
        tot.select("provincia", "unidad", "q"), on="provincia"
    )
    por_unidad = pl.concat([con, sin], how="diagonal_relaxed")
    return (
        por_unidad.join(rep.select("municipio", "unidad", "w"), on="unidad")
        .with_columns((pl.col("valor") * pl.col("q") * pl.col("w")).alias("valor"))
        .select("municipio", "provincia", *celda, "valor")
    )


def ajustar(
    celdas: pl.DataFrame, totales: pl.DataFrame, k: list[str], var: str, iteraciones: int = 50
) -> pl.DataFrame:
    """Ajuste proporcional iterativo (IPF) de (municipio, provincia, *k, var, valor).

    Respeta a la vez los totales provinciales de cada (k, var) —los de `celdas`— y los totales
    de cada (municipio, k) de `totales` (columna `t`), para que todos los objetivos de un
    municipio sumen lo mismo. Ambos márgenes suman lo mismo por (provincia, k), así que el
    ajuste converge.
    """
    col = celdas.group_by("provincia", *k, var).agg(pl.col("valor").sum().alias("c"))
    x = celdas.join(totales, on=["municipio", *k], how="left").join(col, on=["provincia", *k, var])
    x = x.with_columns(pl.col("t").fill_null(0.0))
    for _ in range(iteraciones):
        x = x.with_columns(
            (pl.col("valor") * pl.col("t") / pl.col("valor").sum().over("municipio", *k))
            .fill_nan(0.0)
            .alias("valor")
        )
        x = x.with_columns(
            (pl.col("valor") * pl.col("c") / pl.col("valor").sum().over("provincia", *k, var))
            .fill_nan(0.0)
            .alias("valor")
        )
    return x.select("municipio", "provincia", *k, var, "valor")


def ecp_municipal() -> pl.DataFrame:
    """Residentes a 01/01/2026 por sexo de los municipios que publica la ECP (tabla 79544)."""
    from sinpop.ingest.ine_tablas import leer as leer_ine

    t = leer_ine(RAW_DIR / "ecp/ultimo/tabla_79544_ultimo.json").filter(
        (pl.col("Nacionalidad") == "Total") & pl.col("Sexo").is_in(["Hombres", "Mujeres"])
    )
    return t.select(
        pl.col("Municipios__cod").alias("municipio"),
        pl.col("Sexo").replace_strict({"Hombres": "hombre", "Mujeres": "mujer"}).alias("sexo"),
        pl.col("valor").alias("t_ecp"),
    )


def con_ecp_municipal(por_edad: pl.DataFrame) -> pl.DataFrame:
    """Ajusta el reparto por edad y sexo para que los municipios con cifra oficial de la ECP
    2026 tengan exactamente su total por sexo; el resto de su provincia se reparte entre los
    demás municipios en proporción a lo que ya tenían. Se conservan los totales provinciales
    por sexo y edad (IPF)."""
    t0 = por_edad.group_by("municipio", "provincia", "sexo").agg(pl.col("valor").sum().alias("t0"))
    t = t0.join(ecp_municipal(), on=["municipio", "sexo"], how="left")
    resto = t.group_by("provincia", "sexo").agg(
        (pl.col("t0").sum() - pl.col("t_ecp").fill_null(0).sum()).alias("libre"),
        pl.col("t0").filter(pl.col("t_ecp").is_null()).sum().alias("t0_libre"),
    )
    t = t.join(resto, on=["provincia", "sexo"]).with_columns(
        pl.when(pl.col("t_ecp").is_not_null())
        .then(pl.col("t_ecp"))
        .otherwise(pl.col("t0") * pl.col("libre") / pl.col("t0_libre"))
        .alias("t")
    )
    if t.filter(pl.col("t") < 0).height:
        raise ValueError("la cifra ECP de algún municipio supera el total de su provincia")
    tot = t.select("municipio", "sexo", "t")
    x = por_edad.join(tot, on=["municipio", "sexo"])
    col = por_edad.group_by("provincia", "sexo", "edad").agg(pl.col("valor").sum().alias("c"))
    x = x.join(col, on=["provincia", "sexo", "edad"])
    for _ in range(50):
        x = x.with_columns(
            (pl.col("valor") * pl.col("t") / pl.col("valor").sum().over("municipio", "sexo"))
            .fill_nan(0.0)
            .alias("valor")
        )
        x = x.with_columns(
            (
                pl.col("valor")
                * pl.col("c")
                / pl.col("valor").sum().over("provincia", "sexo", "edad")
            )
            .fill_nan(0.0)
            .alias("valor")
        )
    return x.select(por_edad.columns)


# --------------------------------------------------------------------------- tablas 2024


def _tablas_municipales(tipo: str) -> pl.DataFrame:
    """Recuentos municipales 2024 (municipio, sexo, categoria, valor) de las 52 tablas."""
    nombre = {
        "estudios": "Población de 15 y más años por sexo y nivel de estudios (agrupado)",
        "actividad": "Población de 16 y más años por sexo y relación con la actividad (agrupado)",
    }[tipo]
    dim, mapa = (
        ("Nivel de formación alcanzado", ESTUDIOS_MUN)
        if tipo == "estudios"
        else ("Relación con la actividad", ACTIVIDAD_MUN)
    )
    out = []
    for f in sorted((RAW_DIR / "censo_anual_tablas/ultimo").glob("tabla_*_ultimo.json")):
        if tablas_por_nombre().get(f.stem.split("_")[1]) != nombre:
            continue
        t = leer(f)
        t = t.filter(
            pl.col("Municipios").is_not_null()
            & pl.col("Secciones").is_null()
            & pl.col("Sexo").is_in(["Hombres", "Mujeres"])
            & (pl.col(dim) != "Total")
        )
        sin = set(t[dim].unique().to_list()) - set(mapa)
        if sin:
            raise ValueError(f"{f.name}: categorías sin traducir {sorted(sin)}")
        out.append(
            t.select(
                pl.col("Municipios__cod").alias("municipio"),
                pl.col("Sexo")
                .replace_strict({"Hombres": "hombre", "Mujeres": "mujer"})
                .alias("sexo"),
                pl.col(dim).replace_strict(mapa).alias("categoria"),
                "valor",
            )
        )
    if not out:
        raise FileNotFoundError(f"no hay tablas municipales de {tipo}")
    return pl.concat(out).group_by("municipio", "sexo", "categoria").agg(pl.col("valor").sum())


def tablas_por_nombre() -> dict[str, str]:
    """{id de tabla: nombre} del catálogo del Censo Anual (TABLAS_OPERACION/463)."""
    path = RAW_DIR / "censo_anual_tablas/catalogo/463"
    return {str(x["Id"]): x["Nombre"].strip() for x in json.loads(path.read_text("utf-8"))}


# --------------------------------------------------------------------------- construcción


def construir(path: Path) -> pl.DataFrame:
    from sinpop.harmonize.core import ccaa_de_provincia

    d = definicion(path)
    rep = reparto()
    validos = set(rep["municipio"].to_list())
    malos = [m for m in d.municipios if m not in validos]
    if malos:
        raise ValueError(f"municipios sin población en el Padrón 2025: {malos}")
    provs = sorted({m[:2] for m in d.municipios})
    if not set(provs) <= set(ccaa_de_provincia()):
        raise ValueError("provincia desconocida")
    prov = build.provincias().filter(pl.col("provincia").is_in(provs))
    rep_t = rep.filter(pl.col("provincia").is_in(provs))
    ex = exhaustivo_unidades().filter(pl.col("provincia").is_in(provs))
    mun = d.municipios
    out = []

    cfg = build.load_config("targets.yaml")
    objetivos = {o.id: o for o in cfg.calibrar + cfg.reservar}  # type: ignore[attr-defined]

    def meta(o: str) -> dict:
        ob = objetivos[o]
        uso = "calibrar" if ob in cfg.calibrar else "reservar"  # type: ignore[attr-defined]
        base = {"uso": uso, "unidad": ob.unidad, "universo": ob.universo}
        r = prov.filter(pl.col("objetivo") == o)
        if r.height:
            x = r.row(0, named=True)
            return base | {k: x[k] for k in ("fuente", "edicion", "metodo")}
        return base | {
            "fuente": "censo_anual_tablas: tablas municipales (una por provincia) + ecp: "
            "tabla 59589",
            "edicion": "2024-01-01 (estructura); 2026-01-01 (efectivos)",
            "metodo": "cuotas municipales de 2024 por sexo sobre la población 2026 del municipio",
        }

    def emitir(df: pl.DataFrame, variables: list[str], o: str, extra: str) -> None:
        m = meta(o)
        g = (
            df.filter(pl.col("municipio").is_in(mun))
            .sort(*variables)
            .group_by(*variables, maintain_order=True)
            .agg(pl.col("valor").sum().round(6))
        )
        clave = pl.concat_str(
            [pl.concat_str([pl.lit(f"{v}="), pl.col(v).cast(pl.Utf8)]) for v in variables],
            separator=";",
        )
        out.append(
            g.select(
                pl.lit(f"MUNIS:{path}").alias("territorio"),
                pl.lit(o).alias("objetivo"),
                pl.lit(m["uso"]).alias("uso"),
                pl.lit(m["unidad"]).alias("unidad"),
                pl.lit(m["universo"]).alias("universo"),
                clave.alias("clave"),
                "valor",
                pl.lit(
                    m["fuente"]
                    if o.startswith("voto")
                    else m["fuente"] + " + reparto municipal (D-036)"
                ).alias("fuente"),
                pl.lit(m["edicion"]).alias("edicion"),
                pl.lit(build.FECHA).alias("fecha_referencia"),
                pl.lit(f"{m['metodo']}; {extra}").alias("metodo"),
            )
        )

    reparto_txt = "repartido con el Censo Anual exhaustivo 2025 (pequeños: Padrón 2025)"
    # Edad simple × sexo (de ella salen edad_5 y los umbrales de 15 y 16 años)
    base = build.base_edad().filter(pl.col("provincia").is_in(provs)).rename({"n": "valor"})
    est_edad = ex.select("provincia", "unidad", "sexo", "edad", "personas")
    por_edad = con_ecp_municipal(repartir(base, est_edad, ["sexo", "edad"], rep_t))
    reparto_txt += "; municipios con cifra ECP 2026 (tabla 79544): su total por sexo"
    emitir(
        por_edad.with_columns(edad_5(pl.col("edad"))), ["edad_5", "sexo"], "edad5_sexo", reparto_txt
    )
    # Nacionalidad (grupo y top 15)
    cel = build.nacionalidad_celdas().filter(pl.col("provincia").is_in(provs))
    tot_e5 = (
        por_edad.with_columns(edad_5(pl.col("edad")))
        .group_by("municipio", "sexo", "edad_5")
        .agg(pl.col("valor").sum().alias("t"))
    )
    for var, o in (
        ("nacionalidad_grupo", "nacionalidad"),
        ("nacionalidad_top", "nacionalidad_top"),
    ):
        c = cel.filter(pl.col("variable") == var).rename({"categoria": var}).drop("variable")
        est = ex.select("provincia", "unidad", "sexo", "edad_5", var, "personas")
        r = repartir(c, est, ["sexo", "edad_5", var], rep_t)
        r = ajustar(r, tot_e5, ["sexo", "edad_5"], var)
        if var == "nacionalidad_grupo":
            adultos = build.adultos_nacionalidad(
                r.rename({var: "categoria"}).with_columns(pl.lit(var).alias("variable")),
                clave="municipio",
            )
            emitir(
                adultos, ["nacionalidad_esp_ext", "es_adulto"], "adultos_nacionalidad", reparto_txt
            )
            emitir(
                build.esp_ext(r, var),
                ["nacionalidad_esp_ext", "edad_5"],
                "nacionalidad_edad",
                reparto_txt + "; ajustado (IPF) al total por edad y sexo del municipio",
            )
        emitir(r, [var], o, reparto_txt + "; ajustado (IPF) al total por edad y sexo del municipio")
    # Grado de urbanización y tamaño de municipio
    tot_m = por_edad.group_by("municipio").agg(pl.col("valor").sum())
    deg = (
        ex.group_by("unidad", "grado_urbanizacion")
        .agg(pl.col("personas").sum())
        .with_columns((pl.col("personas") / pl.col("personas").sum().over("unidad")).alias("q"))
    )
    urb = tot_m.join(rep_t.select("municipio", "unidad"), on="municipio").join(deg, on="unidad")
    emitir(
        urb.with_columns((pl.col("valor") * pl.col("q")).alias("valor")),
        ["grado_urbanizacion"],
        "urbanizacion",
        "grado del municipio en el Censo Anual 2025 (pequeños: reparto de su clase)",
    )
    tam = tot_m.join(rep_t.select("municipio", "tamano_municipio"), on="municipio")
    emitir(tam, ["tamano_municipio"], "tamano_municipio", "clase del municipio en el Padrón 2025")
    # Estudios (15+) y actividad (16+) por sexo: tablas municipales 2024
    for tipo, var, o, minimo in (
        ("estudios", "estudios_3", None, 15),
        ("actividad", "relacion_actividad", "actividad_sexo", 16),
    ):
        tab = _tablas_municipales(tipo)
        con_tabla = set(tab["municipio"].str.slice(0, 2).unique().to_list())
        faltan = sorted(set(provs) - con_tabla)
        if faltan:
            raise FileNotFoundError(
                f"falta la tabla municipal de {tipo} del Censo Anual de las provincias {faltan}"
                " (sinpop ingest --source censo_anual_tablas --ine-table <id> --metadata)"
            )
        pob = por_edad.with_columns((pl.col("edad") >= minimo).alias("dentro"))
        np_ = pob.filter(~pl.col("dentro")).group_by("municipio", "sexo").agg(pl.col("valor").sum())
        dentro = (
            pob.filter(pl.col("dentro"))
            .group_by("municipio", "sexo", "provincia")
            .agg(pl.col("valor").sum().alias("n"))
        )
        q = tab.with_columns(
            (pl.col("valor") / pl.col("valor").sum().over("municipio", "sexo")).alias("q")
        )
        con = dentro.join(q.select("municipio", "sexo", "categoria", "q"), on=["municipio", "sexo"])
        # sin dato municipal (secreto estadístico): cuotas de la provincia en la misma tabla
        qp = (
            tab.with_columns(pl.col("municipio").str.slice(0, 2).alias("provincia"))
            .group_by("provincia", "sexo", "categoria")
            .agg(pl.col("valor").sum())
            .with_columns(
                (pl.col("valor") / pl.col("valor").sum().over("provincia", "sexo")).alias("q")
            )
        )
        sin = dentro.join(q.select("municipio").unique(), on="municipio", how="anti").join(
            qp.select("provincia", "sexo", "categoria", "q"), on=["provincia", "sexo"]
        )
        v = pl.concat([con, sin], how="diagonal_relaxed").with_columns(
            (pl.col("n") * pl.col("q")).alias("valor")
        )
        if tipo == "actividad":
            v = _separar_pensionistas(v, prov)
        v = pl.concat(
            [
                v.select("municipio", "sexo", pl.col("categoria").alias(var), "valor"),
                np_.select("municipio", "sexo", pl.lit("NP").alias(var), "valor"),
            ]
        )
        if o:
            emitir(v, [var, "sexo"], o, "cuotas municipales del Censo Anual 2024 por sexo")
        else:
            emitir(
                v,
                [var, "sexo"],
                "estudios_sexo_mun",
                "cuotas municipales del Censo Anual 2024 por sexo",
            )
    # Generales 2023: suma de los municipios de la lista (sin CERA, como el universo)
    from sinpop.targets import electorales as el

    if "48916" in mun:
        raise ValueError(
            "Usansolo (48916) se segregó de Galdakao después de las generales de 2023: su voto "
            "está dentro del de Galdakao (48036) y no se puede separar (D-029)"
        )
    opc, vot = el.generales_municipios()
    sin_dato = sorted(set(mun) - set(opc["municipio"].unique().to_list()))
    if sin_dato:
        raise ValueError(f"municipios sin resultados de las generales 2023: {sin_dato}")
    emitir(
        opc.rename({"opcion": "recuerdo_voto_generales"}),
        ["recuerdo_voto_generales"],
        "voto_generales_2023",
        "suma de los municipios de la lista",
    )
    emitir(
        el.generales_candidaturas(opc, vot),
        ["candidatura_generales_2023"],
        "voto_generales_2023_candidatura",
        "suma de los municipios de la lista",
    )
    res = pl.concat(out).sort("objetivo", "clave")
    return res


def _separar_pensionistas(v: pl.DataFrame, prov: pl.DataFrame) -> pl.DataFrame:
    """Separa «pensionista» en jubilación e incapacidad con la proporción de su provincia y
    sexo en el objetivo provincial `actividad_sexo`."""
    a = (
        prov.filter(pl.col("objetivo") == "actividad_sexo")
        .with_columns(
            pl.col("clave").str.extract(r"relacion_actividad=(\w+)").alias("cat"),
            pl.col("clave").str.extract(r"sexo=(\w+)").alias("sexo"),
        )
        .filter(pl.col("cat").is_in(["jubilado_pensionista", "incapacidad_permanente"]))
    )
    r = a.with_columns(
        (pl.col("valor") / pl.col("valor").sum().over("provincia", "sexo")).alias("r")
    ).select("provincia", "sexo", pl.col("cat"), "r")
    pen = v.filter(pl.col("categoria") == "pensionista").join(r, on=["provincia", "sexo"])
    pen = pen.with_columns(
        (pl.col("valor") * pl.col("r")).alias("valor"), pl.col("cat").alias("categoria")
    )
    return pl.concat(
        [v.filter(pl.col("categoria") != "pensionista"), pen.drop("cat", "r")],
        how="diagonal_relaxed",
    )


def entradas() -> dict[str, str]:
    from sinpop.repro import sha256_file

    out = {}
    for f in sorted((RAW_DIR / "censo_anual_tablas/ultimo").glob("tabla_*_ultimo.json")):
        out[f"raw/censo_anual_tablas/ultimo/{f.name}"] = sha256_file(f)
    return out
