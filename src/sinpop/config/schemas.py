"""Esquemas pydantic de los ficheros de `configs/`.

Cada fichero YAML de configuración tiene un modelo raíz. Los modelos son
estrictos (`extra="forbid"`): una clave desconocida es un error, para que una
errata no se ignore en silencio.
"""

from __future__ import annotations

import datetime as dt
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


# --------------------------------------------------------------------------- sources.yaml

Capa = Literal["A", "B", "C", "A-POL"]


class Source(Strict):
    id: str = Field(pattern=r"^[a-z0-9_]+$")
    nombre: str
    organismo: str
    capa: Capa
    tipo: Literal["microdatos", "tablas", "resultados", "documentacion"]
    url_oficial: str = Field(pattern=r"^https://")
    edicion: str | None = None  # None = pendiente de verificar en F1
    universo: str | None = None
    unidad: (
        Literal["persona", "hogar", "vivienda", "persona_y_hogar", "territorio", "mesa"] | None
    ) = None
    variable_peso: str | None = None
    nivel_geografico: str | None = None
    prioridad: Literal["P0", "P1", "P2", "P3", "P3-POL"]
    descarga: Literal["automatica", "manual", "pendiente"] = "pendiente"
    condiciones: str
    verificar: list[str] = Field(default_factory=list)
    # Si el fichero se documenta a sí mismo (p. ej. cada cifra rotulada en el PDF),
    # aquí se explica; cuenta como documentación para G1.2.
    documentacion_en_fichero: str | None = None


class SourcesConfig(Strict):
    fuentes: list[Source]

    @model_validator(mode="after")
    def _ids_unicos(self) -> SourcesConfig:
        ids = [s.id for s in self.fuentes]
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            raise ValueError(f"ids de fuente duplicados: {sorted(dup)}")
        return self


# --------------------------------------------------------------------------- variables.yaml

Prioridad = Literal["P0", "P1", "P2", "P3", "P3-POL"]
NivelVariable = Literal["persona", "hogar", "territorio", "opinion", "politica"]
TipoVariable = Literal["categorica", "ordinal", "numerica", "booleana", "identificador"]

# Categorías explícitas para los valores especiales (02 · sección 4.2)
ESPECIALES = ("NS", "NC", "NP")


class FuenteVariable(Strict):
    """Correspondencia de una variable armonizada con una fuente concreta (se rellena en F2)."""

    variable_original: str
    universo: str | None = None
    recodificacion: dict[str, str] = Field(default_factory=dict)
    verificado_contra: str | None = None  # diseño de registro / cuestionario usado
    notas: str | None = None  # limitaciones de cobertura detectadas en el inventario (F1)


class Variable(Strict):
    prioridad: Prioridad
    nivel: NivelVariable
    tipo: TipoVariable
    descripcion: str
    categorias: list[str] | None = None
    # Si las categorías dependen de la fuente (p. ej. las 15 nacionalidades más numerosas),
    # se indica aquí en qué fase y de qué documento se fijan. No se inventan.
    dominio_pendiente: str | None = None
    rango: tuple[float, float] | None = None
    fuente_principal: str
    derivada_de: str | None = None
    fuentes: dict[str, FuenteVariable] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _dominio(self) -> Variable:
        if self.tipo in ("categorica", "ordinal") and not (
            self.categorias or self.dominio_pendiente
        ):
            raise ValueError(
                "una variable categórica u ordinal necesita 'categorias' o 'dominio_pendiente'"
            )
        if self.categorias and self.dominio_pendiente:
            raise ValueError("'categorias' y 'dominio_pendiente' son excluyentes")
        if self.categorias and len(set(self.categorias)) != len(self.categorias):
            raise ValueError("categorías duplicadas")
        for f in self.fuentes.values():
            fuera = set(f.recodificacion.values()) - set(self.categorias or []) - set(ESPECIALES)
            if self.categorias and fuera:
                raise ValueError(f"recodificación a valores fuera de dominio: {sorted(fuera)}")
        return self


class VariablesConfig(Strict):
    variables: dict[str, Variable]

    @field_validator("variables")
    @classmethod
    def _nombres(cls, v: dict[str, Variable]) -> dict[str, Variable]:
        import re

        malos = [k for k in v if not re.fullmatch(r"[a-z][a-z0-9_]*", k)]
        if malos:
            raise ValueError(f"nombres de variable no válidos: {malos}")
        return v

    def por_capa(self, *prioridades: str) -> set[str]:
        return {k for k, v in self.variables.items() if v.prioridad in prioridades}


# --------------------------------------------------------------------------- targets.yaml


Universo = Literal[
    "residentes",
    "viviendas_familiares",
    "colectivos",
    "hogares",
    "censo_electoral_residente",  # electores residentes en España (generales, sin CERA)
    "censo_electoral",  # electores de la publicación autonómica (puede incluir el CERA)
]


class Objetivo(Strict):
    id: str
    variables: list[str] = Field(min_length=1)
    unidad: Literal["persona", "hogar"] = "persona"
    universo: Universo = "residentes"
    # Territorios en los que existe: «provincia» (España, CCAA y provincias), «municipios»
    # (territorios por lista de municipios) o «todos»
    ambito: Literal["todos", "provincia", "municipios"] = "todos"
    descripcion: str | None = None
    fuente: str | None = None  # la fuente, edición y fecha de cada cifra van en el fichero
    edicion: str | None = None  # de objetivos (data/processed/targets/), no aquí (D-036)
    fecha_referencia: dt.date | None = None

    @model_validator(mode="after")
    def _unidad_universo(self) -> Objetivo:
        if (self.unidad == "hogar") != (self.universo == "hogares"):
            raise ValueError(f"{self.id}: la unidad hogar va con el universo hogares")
        return self

    @property
    def clave(self) -> tuple[str, ...]:
        return tuple(sorted(self.variables))


class TargetsConfig(Strict):
    fecha_referencia: dt.date
    # Agrupaciones de edad de las tablas oficiales: límites inferiores de cada grupo (el
    # primero es la edad mínima del universo de la tabla; por debajo, un grupo «00-(min-1)»)
    agrupaciones_edad: dict[str, list[int]] = Field(default_factory=dict)
    calibrar: list[Objetivo]
    reservar: list[Objetivo]

    @field_validator("agrupaciones_edad")
    @classmethod
    def _cortes(cls, v: dict[str, list[int]]) -> dict[str, list[int]]:
        for k, c in v.items():
            if not c or c != sorted(set(c)) or c[0] < 1:
                raise ValueError(f"{k}: los cortes deben ser crecientes, sin repetir y > 0")
        return v

    @model_validator(mode="after")
    def _separacion(self) -> TargetsConfig:
        # Un cruce no puede calibrarse y reservarse en los mismos territorios. «provincia»
        # (España, CCAA, provincias) y «municipios» (listas de municipios) no se solapan.
        def solapan(a: str, b: str) -> bool:
            return "todos" in (a, b) or a == b

        comun = {
            c.clave
            for c in self.calibrar
            for r in self.reservar
            if c.clave == r.clave and solapan(c.ambito, r.ambito)
        }
        if comun:
            raise ValueError(f"objetivos a la vez calibrados y reservados: {sorted(comun)}")
        ids = [o.id for o in self.calibrar + self.reservar]
        if len(ids) != len(set(ids)):
            raise ValueError("ids de objetivo duplicados")
        return self


# --------------------------------------------------------------------------- territories.yaml


class CCAA(Strict):
    codigo: str = Field(pattern=r"^\d{2}$")
    nombre: str


class Provincia(Strict):
    codigo: str = Field(pattern=r"^\d{2}$")
    nombre: str
    ccaa: str = Field(pattern=r"^\d{2}$")


NIVELES_DONANTES = (
    "mismo_territorio",
    "misma_provincia",
    "misma_ccaa_mismo_grado_urbanizacion",
    "ccaa_parecidas",
    "espana",
)


class CCAAParecidas(Strict):
    numero: int = Field(gt=0)
    objetivos: list[str] = Field(min_length=1)


class Ampliacion(Strict):
    min_donantes_celda: int = Field(gt=0)
    # Mínimo propio de algunos objetivos (D-051): p. ej. cada nacionalidad, para que un grupo
    # pequeño no salga de unos pocos hogares (V-CONCENTRACION)
    min_donantes_objetivo: dict[str, int] = Field(default_factory=dict)
    razon_max: float = Field(gt=1)
    razon_objetivo: float = Field(gt=1)
    # Razones propias de algunos objetivos (D-051): p. ej. las nacionalidades que han crecido
    # desde 2021 se amplían antes, para no clonar mucho sus pocos hogares donantes
    razon_max_objetivo: dict[str, float] = Field(default_factory=dict)
    razon_objetivo_objetivo: dict[str, float] = Field(default_factory=dict)
    # D-054: las celdas de extranjeros (edad, actividad, nacionalidad × edad) se amplían con
    # estas razones; si el territorio no converge con ellas sin fundir nacionalidades, se
    # calibra sin ellas
    razon_max_extranjeros: dict[str, float] = Field(default_factory=dict)
    razon_objetivo_extranjeros: dict[str, float] = Field(default_factory=dict)


class TerritoriesConfig(Strict):
    fuente_codigos: str
    ccaa: list[CCAA]
    provincias: list[Provincia]
    jerarquia_donantes: list[str] = Field(min_length=1)
    ccaa_parecidas: CCAAParecidas
    ampliacion: Ampliacion
    donantes_min_kish: int = Field(gt=0)

    @field_validator("jerarquia_donantes")
    @classmethod
    def _niveles(cls, v: list[str]) -> list[str]:
        malos = [n for n in v if n not in NIVELES_DONANTES]
        if malos or v[0] != "mismo_territorio":
            raise ValueError(f"jerarquía de donantes no válida: {v}")
        return v

    @model_validator(mode="after")
    def _coherencia(self) -> TerritoriesConfig:
        cc = [c.codigo for c in self.ccaa]
        pr = [p.codigo for p in self.provincias]
        if len(set(cc)) != len(cc) or len(set(pr)) != len(pr):
            raise ValueError("códigos territoriales duplicados")
        huerfanas = [p.codigo for p in self.provincias if p.ccaa not in set(cc)]
        if huerfanas:
            raise ValueError(f"provincias con CCAA inexistente: {huerfanas}")
        return self


# --------------------------------------------------------------------------- watchlist.yaml


class Grupo(Strict):
    id: str = Field(pattern=r"^[a-z0-9_]+$")
    nombre: str
    # Expresiones SQL de Polars sobre las variables de la población (pl.sql_expr)
    definicion: str
    universo: str = "TRUE"
    unidad: Literal["persona", "hogar"] = "persona"
    referencia: str
    recuento_minimo: int | None = Field(default=None, gt=0)
    capa: Literal["base", "enriquecimiento", "opinion", "politica"] = "base"
    medible: bool = True
    motivo: str | None = None


class WatchlistConfig(Strict):
    grupos: list[Grupo]

    @model_validator(mode="after")
    def _ids(self) -> WatchlistConfig:
        ids = [g.id for g in self.grupos]
        if len(ids) != len(set(ids)):
            raise ValueError("ids de grupo duplicados")
        return self


# --------------------------------------------------------------------------- thresholds.yaml

Rango = tuple[float, float]


class _Th(Strict):
    pass


class VMarg(_Th):
    factor_tvd_ref: float = Field(gt=0)
    tolerancia: float = Field(ge=0)
    muestras_ref: int = Field(gt=0)
    percentil_ref: float = Field(gt=0, lt=100)
    # D-056: en la serie de F4, una marginal solo falla si queda fuera en este número de
    # poblaciones o más (azar frente a sesgo, como D-047)
    poblaciones_fallo_min: int = Field(default=1, ge=1)


class ExcepcionCruce(Strict):
    """Cruce reservado cuyo fallo se acepta como limitación documentada de los datos."""

    territorio: str
    objetivo: str
    decision: str
    motivo: str


class VCruce(_Th):
    espana: float
    ccaa: float
    provincia: float
    cramer_v_max_dif: float
    # D-038 A: cuando domina el error de muestreo, el margen de V-MARG sobre TVD_ref.
    factor_tvd_ref: float = 1.0
    tolerancia: float = 0.0
    excepciones: list[ExcepcionCruce] = []
    # D-039 (aprobada): en la serie de poblaciones de la puerta, fallos tolerados por azar en cada
    # población; un cruce que falla en todas las semillas de un tamaño es sesgo y no se tolera.
    proporcion_fallos_max: float = 0.0


class VReglasBlandas(_Th):
    exceso_relativo_max: float


class VPesos(_Th):
    convergencia_max: float
    rango_factor: Rango
    proporcion_en_rango: float
    kish_min_ratio: float


class VSemillas(_Th):
    n_semillas: int
    factor_sd: float
    tamanos_fallo_min: int = 1


class VCoherencia(_Th):
    tvd_marginales: float
    tvd_cruces: float
    factor_tvd_ref: float
    tolerancia: float


class VDonantes(_Th):
    kish_min: int
    locales_alerta: float


class VEnriqMarg(_Th):
    proporcion_celdas_ic95: float
    tvd_nacional: float
    limitaciones: dict[str, str] = {}
    # TVD ajustada máxima propia de una limitación, aprobada por la persona responsable (D-059)
    tvd_ajustada_max: dict[str, float] = {}


class VDelta(_Th):
    max_abs_dif: float


class VEnriqBloque(_Th):
    max_abs_dif: float
    media_abs_dif: float


class VMinorias(_Th):
    ratio: Rango
    recuento_esperado_min: int
    # D-059: fallos de G7.1, G7.3 y G7.4 aceptados como limitación declarada por la persona
    # responsable: grupos (en cualquier población) y nacionalidades fuera de la población de
    # España (territorios con pocos donantes por nacionalidad)
    limitaciones: dict[str, str] = {}
    nacionalidades_territoriales: bool = False
    # Excepciones concretas aprobadas (D-061): "territorio|grupo" → motivo
    excepciones: dict[str, str] = {}


class VTvdMax(_Th):
    tvd_max: float


class VMinoriasPerfil(_Th):
    tvd_max: float
    # Margen de muestreo (D-051): umbral = máx(tvd_max, factor × TVD_ref(n) + tolerancia)
    factor_tvd_ref: float
    tolerancia: float
    muestras_ref: int
    percentil_ref: float


class VDiversidad(_Th):
    ratio_entropia_min: float
    proporcion_grupos: float
    tamano_grupo_min: int
    # Margen de muestreo (D-051): también cumple si la entropía no baja del percentil
    # `percentil_ref` de la de muestras aleatorias simples de tamaño n de la referencia
    muestras_ref: int
    percentil_ref: float


class VConcentracion(_Th):
    top5_max: float
    donantes_distintos_min: int
    divisor_tamano_grupo: int
    # D-051: el top 5 inevitable por el tamaño del grupo (5 × miembros por hogar / tamaño)
    # también es aceptable
    top5_inevitable: bool


class VRareza(_Th):
    metodo_base_max: float
    metodo_generativo_max: float


class VLatente(_Th):
    cfi_min: float
    rmsea_max: float
    omega_min: float


class VDiversidadRasgos(_Th):
    ratio_varianza: Rango


class VPolRecuerdo(_Th):
    factor_tvd_ref: float
    tolerancia: float


class VPolReservada(_Th):
    tvd_espana: float
    tvd_ccaa: float
    error_participacion_max: float


class VPolPerfil(_Th):
    tvd_max: float
    casos_cis_min: int


class VPolCoherencia(_Th):
    error_media_max: float
    ratio_sd: Rango


class VPolTransferencia(_Th):
    tvd_fila_max: float
    casos_fila_min: int


class VPolSesgo(_Th):
    ratio_entropia_min: float


class VTemporalSeries(_Th):
    error_medio_max_pp: float


class VReformulacion(_Th):
    tvd_max: float


class VCobertura(_Th):
    ic80: Rango
    ic95: Rango


class VEvento(_Th):
    proporcion_direccion_correcta: float


class VConfCorr(_Th):
    spearman_min: float


class VConfEce(_Th):
    ece_max: float
    tvd_acierto: float


class VDatos(_Th):
    totales_dif_relativa_max: float
    oficiales_min_por_fuente: int


class VRegresion(_Th):
    empeoramiento_relativo_max: float


class ThresholdsConfig(Strict):
    model_config = ConfigDict(extra="forbid", frozen=True, populate_by_name=True)

    v_datos: VDatos = Field(alias="V-DATOS")
    v_marg: VMarg = Field(alias="V-MARG")
    v_cruce: VCruce = Field(alias="V-CRUCE")
    v_reglas_blandas: VReglasBlandas = Field(alias="V-REGLAS-BLANDAS")
    v_pesos: VPesos = Field(alias="V-PESOS")
    v_semillas: VSemillas = Field(alias="V-SEMILLAS")
    v_coherencia: VCoherencia = Field(alias="V-COHERENCIA")
    v_donantes: VDonantes = Field(alias="V-DONANTES")
    v_enriq_marg: VEnriqMarg = Field(alias="V-ENRIQ-MARG")
    v_enriq_asoc: VDelta = Field(alias="V-ENRIQ-ASOC")
    v_enriq_bloque: VEnriqBloque = Field(alias="V-ENRIQ-BLOQUE")
    v_enriq_holdout: VDelta = Field(alias="V-ENRIQ-HOLDOUT")
    v_minorias: VMinorias = Field(alias="V-MINORIAS")
    v_minorias_perfil: VMinoriasPerfil = Field(alias="V-MINORIAS-PERFIL")
    v_diversidad: VDiversidad = Field(alias="V-DIVERSIDAD")
    v_concentracion: VConcentracion = Field(alias="V-CONCENTRACION")
    v_rareza: VRareza = Field(alias="V-RAREZA")
    v_latente: VLatente = Field(alias="V-LATENTE")
    v_diversidad_rasgos: VDiversidadRasgos = Field(alias="V-DIVERSIDAD-RASGOS")
    v_pol_recuerdo: VPolRecuerdo = Field(alias="V-POL-RECUERDO")
    v_pol_reservada: VPolReservada = Field(alias="V-POL-RESERVADA")
    v_pol_perfil: VPolPerfil = Field(alias="V-POL-PERFIL")
    v_pol_coherencia: VPolCoherencia = Field(alias="V-POL-COHERENCIA")
    v_pol_transferencia: VPolTransferencia = Field(alias="V-POL-TRANSFERENCIA")
    v_pol_sesgo: VPolSesgo = Field(alias="V-POL-SESGO")
    v_temporal_series: VTemporalSeries = Field(alias="V-TEMPORAL-SERIES")
    v_reformulacion: VReformulacion = Field(alias="V-REFORMULACION")
    v_cobertura: VCobertura = Field(alias="V-COBERTURA")
    v_evento: VEvento = Field(alias="V-EVENTO")
    v_conf_corr: VConfCorr = Field(alias="V-CONF-CORR")
    v_conf_ece: VConfEce = Field(alias="V-CONF-ECE")
    v_regresion: VRegresion = Field(alias="V-REGRESION")


# --------------------------------------------------------------------------- partidos.yaml


class Familia(Strict):
    id: str = Field(pattern=r"^[a-z0-9_]+$")
    nombre: str
    desglose_por_territorio: bool = False


class Candidatura(Strict):
    codigo_oficial: str
    codigo_boe: str | None = None  # siglas en el resumen oficial del BOE, si difieren
    nombre: str
    familia: str
    ambito: str | None = None
    codigos_cis: dict[str, list[str]] = Field(default_factory=dict)
    notas: str | None = None


EspecialCIS = Literal[
    "NP",
    "NS",
    "NC",
    "en_blanco",
    "nulo",
    "no_voto_o_ninguno",
    "no_tenia_edad",
    "sin_derecho_voto",
    "mismo_partido",
]


class CodigoCIS(Strict):
    etiqueta: str
    familia: str | None = None
    especial: EspecialCIS | None = None
    notas: str | None = None

    @model_validator(mode="after")
    def _uno(self) -> CodigoCIS:
        if (self.familia is None) == (self.especial is None):
            raise ValueError(f"{self.etiqueta}: indicar familia o especial (solo uno)")
        return self


class EstudioCIS(Strict):
    titulo: str
    variables: list[str] = Field(min_length=1)
    recuerdo_de: str | None = None  # elección a la que se refiere el recuerdo de voto
    codigos: dict[int, CodigoCIS]


class EleccionPartidos(Strict):
    fecha: dt.date
    fuente: str
    candidaturas: list[Candidatura] = Field(default_factory=list)


class PartidosConfig(Strict):
    familias: list[Familia] = Field(min_length=1)
    elecciones: dict[str, EleccionPartidos] = Field(default_factory=dict)
    cis: dict[str, EstudioCIS] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _familias_existen(self) -> PartidosConfig:
        ids = {f.id for f in self.familias}
        for eid, e in self.elecciones.items():
            malas = [c.nombre for c in e.candidaturas if c.familia not in ids]
            if malas:
                raise ValueError(f"{eid}: candidaturas con familia desconocida: {malas}")
            for c in e.candidaturas:
                for est, cods in c.codigos_cis.items():
                    if est not in self.cis:
                        raise ValueError(f"{c.nombre}: estudio CIS no declarado {est}")
                    faltan = [k for k in cods if int(k) not in self.cis[est].codigos]
                    if faltan:
                        raise ValueError(f"{c.nombre}: códigos CIS inexistentes {faltan}")
        for est, d in self.cis.items():
            malas = [k for k, c in d.codigos.items() if c.familia and c.familia not in ids]
            if malas:
                raise ValueError(f"CIS {est}: códigos con familia desconocida: {malas}")
        return self


# --------------------------------------------------------------------------- elecciones.yaml


class Eleccion(Strict):
    id: str = Field(pattern=r"^[a-z0-9_-]+$")
    tipo: Literal["generales", "europeas", "autonomicas", "municipales"]
    fecha: dt.date
    ambito: str
    fuente: str
    uso: Literal["calibrar", "reservar", "pendiente", "excluida"]
    url_oficial: str | None = None
    verificar: list[str] = Field(default_factory=list)


class EleccionesConfig(Strict):
    elecciones: list[Eleccion]
    # Validación reservada alternativa cuando no se reserva ninguna elección completa (D-022)
    validacion_reservada: str | None = None

    @model_validator(mode="after")
    def _una_reservada(self) -> EleccionesConfig:
        ids = [e.id for e in self.elecciones]
        if len(ids) != len(set(ids)):
            raise ValueError("ids de elección duplicados")
        if (
            self.elecciones
            and not any(e.uso == "reservar" for e in self.elecciones)
            and not self.validacion_reservada
        ):
            raise ValueError("debe reservarse al menos una elección para validar (F3, tarea 5)")
        return self


# --------------------------------------------------------------------------- eventos.yaml


class Evento(Strict):
    id: str = Field(pattern=r"^e\d{3,}$")
    fecha: dt.date
    descripcion: str
    tipo: Literal["economico", "social", "politico", "catastrofe", "internacional"]
    ambito: str = Field(pattern=r"^(ES|CCAA:\d{2}|PROV:\d{2})$")
    fuente: str
    indicadores_afectados: list[str] = Field(default_factory=list)


class EventosConfig(Strict):
    eventos: list[Evento] = Field(default_factory=list)


# --------------------------------------------------------------------------- llm.yaml


class ModeloLLM(Strict):
    id: str
    proveedor: str
    fecha_corte_conocimiento: dt.date
    uso: list[Literal["traduccion", "simulacion", "eventos", "embeddings"]]


class Presupuesto(Strict):
    eur_max_por_prediccion: float = Field(gt=0)
    eur_max_por_ejecucion: float = Field(gt=0)
    llamadas_max_por_prediccion: int = Field(gt=0)


class LLMConfig(Strict):
    fecha_corte_construccion: dt.date
    modelos: list[ModeloLLM] = Field(default_factory=list)
    presupuesto: Presupuesto
    reintentos_salida_invalida: int = Field(ge=0, le=5)
    temperatura: float = Field(ge=0, le=2)
    cache_dir: str
    logs_dir: str

    @model_validator(mode="after")
    def _corte(self) -> LLMConfig:
        for m in self.modelos:
            if m.fecha_corte_conocimiento > self.fecha_corte_construccion:
                raise ValueError(
                    f"el modelo {m.id} conoce datos posteriores a la fecha de corte de "
                    "construcción; hay que mover la fecha (D-003)"
                )
        return self


# --------------------------------------------------------------------------- registro

SCHEMAS: dict[str, type[BaseModel]] = {
    "sources.yaml": SourcesConfig,
    "variables.yaml": VariablesConfig,
    "targets.yaml": TargetsConfig,
    "territories.yaml": TerritoriesConfig,
    "watchlist.yaml": WatchlistConfig,
    "thresholds.yaml": ThresholdsConfig,
    "partidos.yaml": PartidosConfig,
    "elecciones.yaml": EleccionesConfig,
    "eventos.yaml": EventosConfig,
    "llm.yaml": LLMConfig,
}
