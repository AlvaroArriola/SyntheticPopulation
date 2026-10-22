"""Prompts versionados (`prompts/<nombre>/<versión>.md`) (D-071).

Cada fichero tiene dos secciones, `## sistema` y `## usuario`, con variables `$nombre`
(`string.Template`, para no chocar con las llaves de los ejemplos JSON). El identificador
`nombre@versión` y el SHA-256 del fichero van en la caché y en el registro de cada llamada, así que
cambiar un prompt invalida sus respuestas guardadas.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from string import Template

from sinpop import REPO_ROOT

PROMPTS_DIR = REPO_ROOT / "prompts"


@dataclass(frozen=True)
class Prompt:
    id: str
    sha256: str
    sistema: str
    usuario: str

    def render(self, variables: dict[str, str]) -> tuple[str, str]:
        return (
            Template(self.sistema).substitute(variables),
            Template(self.usuario).substitute(variables),
        )


def cargar(id_: str) -> Prompt:
    nombre, version = id_.split("@")
    ruta = PROMPTS_DIR / nombre / f"{version}.md"
    texto = ruta.read_text("utf-8")
    partes = re.split(r"^## (sistema|usuario)\s*$", texto, flags=re.M)
    secciones = {partes[i]: partes[i + 1].strip() for i in range(1, len(partes) - 1, 2)}
    if set(secciones) != {"sistema", "usuario"}:
        raise ValueError(f"{ruta}: hacen falta las secciones '## sistema' y '## usuario'")
    return Prompt(
        id_,
        hashlib.sha256(texto.encode("utf-8")).hexdigest(),
        secciones["sistema"],
        secciones["usuario"],
    )
