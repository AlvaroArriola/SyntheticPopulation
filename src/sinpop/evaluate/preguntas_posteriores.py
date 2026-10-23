"""Preguntas de los estudios del CIS posteriores al corte (junio de 2026), con el error obtenido
cuando ya se han evaluado (`reports/preguntas_posteriores_al_corte.md`).

Solo enunciados y opciones, que son el cuestionario público, nunca respuestas. Vive aquí porque
solo `sinpop.evaluate` puede leer `data/eval/` (regla 5). La ventana final (`--final`) se lista
solo después de F11.

Comando: `python -m sinpop.evaluate.preguntas_posteriores [--final]`.
"""

import sys

import polars as pl

from sinpop.evaluate import validacion as V

estudios = dict(V.VALIDACION) | (dict(V.EVALUACION_FINAL) if "--final" in sys.argv else {})
val = pl.read_csv("reports/fase_09/validacion_preguntas.csv", infer_schema_length=None)
llm = pl.read_csv("reports/fase_09/llm_preguntas.csv", infer_schema_length=None)
fin = None
try:
    fin = pl.read_csv("reports/fase_11/preguntas.csv", infer_schema_length=None)
except FileNotFoundError:
    pass
err = {}
for d, col in ((val, "tvd_sistema_cis"), (llm, "tvd_nueva")):
    for r in d.select("id", col).iter_rows():
        if r[1] is not None and r[0] not in err:
            err[r[0]] = (r[1], "LLM anclado" if col == "tvd_nueva" else "análogas")
if fin is not None:
    for r in fin.select("id", "tvd_sistema_final").iter_rows():
        if r[1] is not None:
            err.setdefault(r[0], (r[1], "final"))
out = []
for est, fecha in estudios.items():
    _, _, banco = V._cargar(est, fecha)
    qs = V.preguntas(banco, est, fecha)
    uso = "evaluación final (F11)" if est in V.EVALUACION_FINAL else "validación (F9-F10)"
    out.append(f"\n## Estudio {est} · {fecha[:7]} · {uso} · {len(qs)} preguntas\n")
    out.append("| Pregunta | Opciones | Tipo | Error (TVD) |\n| --- | --- | --- | --- |")
    for q in qs:
        ops = " / ".join(
            o.replace("(NO LEER) ", "") for o in q["opciones"] if o not in ("N.S.", "N.C.")
        )
        e = err.get(q["id"])
        et = f"{e[0]:.3f} ({e[1]})" if e else "—"
        txt = q["enunciado"].replace("|", "/").replace("\n", " ")
        tipo = "política" if q["politica"] else "vida cotidiana"
        out.append(f"| {txt} | {ops.replace('|', '/')} | {tipo} | {et} |")
print("\n".join(out))
