"""Recuperación de preguntas parecidas del banco (F9, tarea 1) (D-069).

Sin modelo de lenguaje ni *embeddings* neuronales (el entorno no puede descargar modelos y el
coste debe ser cero): representación TF-IDF del enunciado y de las opciones con n-gramas de
caracteres (3 a 5, robustos a flexiones y a pequeños cambios de redacción) y de palabras (1 y 2),
y similitud del coseno. Las preguntas del CIS usan fórmulas muy repetidas, lo que favorece este
método; unos *embeddings* multilingües locales serían la mejora natural si se pueden instalar.
"""

from __future__ import annotations

from functools import cache

import numpy as np
import polars as pl
import scipy.sparse as sp

from sinpop.predict import banco as B
from sinpop.predict import opciones as O


def texto(enunciado: str, opciones: list[str]) -> str:
    ops = " | ".join(O.normalizar(o) for o in O.sustantivas(opciones))
    return f"{O.normalizar(enunciado)} || {ops}"


class Indice:
    def __init__(self, preguntas: pl.DataFrame) -> None:
        from sklearn.feature_extraction.text import TfidfVectorizer

        self.preguntas = preguntas
        docs = [texto(e, o) for e, o in preguntas.select("enunciado", "opciones").iter_rows()]
        self.vc = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)
        self.vw = TfidfVectorizer(analyzer="word", ngram_range=(1, 2), sublinear_tf=True)
        self.x = self._unir(self.vc.fit_transform(docs), self.vw.fit_transform(docs))

    @staticmethod
    def _unir(a: sp.spmatrix, b: sp.spmatrix) -> sp.csr_matrix:
        x = sp.hstack([a, b], format="csr")
        n = np.sqrt(np.asarray(x.multiply(x).sum(axis=1)).ravel())
        n[n == 0] = 1.0
        return sp.diags(1.0 / n) @ x

    def similares(
        self, enunciado: str, opciones: list[str], k: int = 20, excluir: pl.Expr | None = None
    ) -> pl.DataFrame:
        q = texto(enunciado, opciones)
        v = self._unir(self.vc.transform([q]), self.vw.transform([q]))
        s = np.asarray((self.x @ v.T).todense()).ravel()
        d = self.preguntas.with_columns(pl.Series("similitud", s))
        if excluir is not None:
            d = d.filter(~excluir)
        return d.sort(["similitud", "id"], descending=[True, False]).head(k)


@cache
def indice() -> Indice:
    return Indice(B.preguntas())
