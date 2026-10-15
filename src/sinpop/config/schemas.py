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


class Objetivo(Strict):
    id: str
    variables: list[str] = Field(min_length=1)
    unidad: Literal["persona", "hogar"] = "persona"
    fuente: str | None = None  # se rellena en F3
    edicion: str | None = None
    fecha_referencia: dt.date | None = None

    @property
    def clave(self) -> tuple[str, ...]:
        return tuple(sorted(self.variables))


class TargetsConfig(Strict):
    fecha_referencia: dt.date
    calibrar: list[Objetivo]
    reservar: list[Objetivo]

    @model_validator(mode="after")
    def _separacion(self) -> TargetsConfig:
        cal = {o.clave for o in self.calibrar}
        res = {o.clave for o in self.reservar}
        comun = cal & res
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


class TerritoriesConfig(Strict):
    fuente_codigos: str
    ccaa: list[CCAA]
    provincias: list[Provincia]
    jerarquia_donantes: list[str] = Field(min_length=1)
    donantes_min_kish: int = Field(gt=0)

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
    definicion: str
    referencia: str
    recuento_minimo: int | None = Field(default=None, gt=0)
    capa: Literal["base", "enriquecimiento", "opinion", "politica"] = "base"
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


class VCruce(_Th):
    espana: float
    ccaa: float
    provincia: float
    cramer_v_max_dif: float


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


class VCoherencia(_Th):
    tvd_marginales: float
    tvd_cruces: float


class VDonantes(_Th):
    kish_min: int
    locales_alerta: float


class VEnriqMarg(_Th):
    proporcion_celdas_ic95: float
    tvd_nacional: float


class VDelta(_Th):
    max_abs_dif: float


class VEnriqBloque(_Th):
    max_abs_dif: float
    media_abs_dif: float


class VMinorias(_Th):
    ratio: Rango
    recuento_esperado_min: int


class VTvdMax(_Th):
    tvd_max: float


class VDiversidad(_Th):
    ratio_entropia_min: float
    proporcion_grupos: float
    tamano_grupo_min: int


class VConcentracion(_Th):
    top5_max: float
    donantes_distintos_min: int
    divisor_tamano_grupo: int


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
    v_minorias_perfil: VTvdMax = Field(alias="V-MINORIAS-PERFIL")
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
