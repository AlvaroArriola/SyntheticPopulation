"""Señales del modelo de confianza (`03_arquitectura.md` §2.7) (D-070).

Para una predicción y una clave (total o subgrupo):

- **similitud** con el banco: la de la mejor análoga y la media ponderada de las usadas;
- **desacuerdo entre estimadores**: desviación media entre análogas y distancia (TVD) entre el
  sistema y B0 y entre el sistema y B1;
- **amplitud del intervalo**: anchura media del intervalo del 80 %;
- **tamaño efectivo de datos del subgrupo**: encuestados de las análogas en ese subgrupo (el
  subgrupo de una comunidad pequeña o de un grupo de edad escaso tiene menos datos);
- **forma de la pregunta**: número de opciones, escala ordinal, número de análogas, antigüedad de
  la análoga más reciente y si la pregunta ya se hizo igual (recurrente).

La sensibilidad a reformulaciones de §2.7 se mide en F9 (G9.4) y es prácticamente nula, así que
no se incluye.
"""

from __future__ import annotations

import numpy as np

from sinpop.predict import estimador as E


def senales(r: E.Resultado, clave: str = "total") -> dict:
    q, an = r.pregunta, r.analogas
    pesos = np.array([a["peso_analoga"] for a in an])
    sims = np.array([a["similitud"] for a in an])
    mu = r.sistema_cis[clave]
    sd = r.sistema_cis_sd.get(clave, r.sistema_cis_sd["total"])
    cal = E.calibracion()
    i80, _ = E.intervalos(mu / mu.sum(), sd, cal, float(sims[0]))
    n_sub = sum(a.get("n_sub", {}).get(clave, a.get("encuestados", 0)) for a in an)
    b1 = r.b1.get(clave, r.b1["total"])
    return {
        "similitud_max": float(sims[0]),
        "similitud_media": float((sims * pesos).sum() / pesos.sum()),
        "analogas": len(an),
        "desacuerdo_analogas": float(np.mean(sd)),
        "tvd_sistema_b0": float(0.5 * np.abs(r.sistema_cis["total"] - r.b0).sum()),
        "tvd_sistema_b1": float(0.5 * np.abs(mu - b1).sum()),
        "anchura_ic80": float(np.mean(i80[:, 1] - i80[:, 0])),
        "n_datos": float(n_sub),
        "log_n_datos": float(np.log1p(n_sub)),
        "opciones": len(q.opciones),
        "ordinal": int(q.escala == "ordinal"),
        "meses_ultima": float(min(E._meses(a["fecha"], q.fecha_referencia) for a in an)),
        "recurrente": int(
            any(E.O.normalizar(a["enunciado"]) == E.O.normalizar(q.enunciado) for a in an)
        ),
        "es_subgrupo": int(clave != "total"),
    }
