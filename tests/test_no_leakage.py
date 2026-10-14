"""Separación física de los datos de evaluación (regla 5 de CLAUDE.md).

Ningún módulo de `src/sinpop/` fuera de `src/sinpop/evaluate/` puede hacer referencia
a la carpeta de datos de evaluación. NO DESACTIVAR ESTE TEST.

La comprobación es estática (AST): busca cualquier literal de texto que nombre la
carpeta `eval` como componente de una ruta (`data/eval`, `"eval"` usado en un join,
`Path(...) / "eval"`…) y cualquier importación de `sinpop.evaluate` desde otro paquete,
porque esa importación daría acceso a `EVAL_DIR`.

Los tests `test_detector_*` comprueban el propio detector (puerta G0.3): si se añade
a propósito una lectura de los datos de evaluación desde otro módulo, el test falla.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src" / "sinpop"
ALLOWED = SRC / "evaluate"

_EVAL_SEGMENT = re.compile(r"(^|[/\\])eval([/\\]|$)")


def _violations_in_source(code: str, filename: str) -> list[str]:
    tree = ast.parse(code, filename=filename)
    found: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if _EVAL_SEGMENT.search(node.value):
                found.append(f"{filename}:{node.lineno}: ruta de evaluación {node.value!r}")
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module == "sinpop.evaluate" or node.module.startswith("sinpop.evaluate."):
                found.append(f"{filename}:{node.lineno}: importa {node.module}")
            elif node.module == "sinpop" and any(a.name == "evaluate" for a in node.names):
                found.append(f"{filename}:{node.lineno}: importa sinpop.evaluate")
        elif isinstance(node, ast.Import):
            for a in node.names:
                if a.name == "sinpop.evaluate" or a.name.startswith("sinpop.evaluate."):
                    found.append(f"{filename}:{node.lineno}: importa {a.name}")
    return found


def find_eval_access(src: Path = SRC, allowed: Path = ALLOWED) -> list[str]:
    """Devuelve las referencias a los datos de evaluación fuera del paquete permitido."""
    out: list[str] = []
    for py in sorted(src.rglob("*.py")):
        if allowed in py.parents:
            continue
        out += _violations_in_source(py.read_text(encoding="utf-8"), str(py.relative_to(src)))
    return out


def test_no_module_outside_evaluate_reads_eval_data() -> None:
    violations = find_eval_access()
    assert violations == [], "Fuga de datos de evaluación:\n" + "\n".join(violations)


# --------------------------------------------------------------------- test del propio test


def _make_pkg(tmp_path: Path, files: dict[str, str]) -> Path:
    src = tmp_path / "sinpop"
    for rel, code in files.items():
        p = src / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(code, encoding="utf-8")
    return src


def test_detector_flags_direct_path(tmp_path: Path) -> None:
    src = _make_pkg(
        tmp_path, {"synth/bad.py": 'import polars as pl\npl.read_parquet("data/eval/x.parquet")\n'}
    )
    assert find_eval_access(src, src / "evaluate")


def test_detector_flags_path_join(tmp_path: Path) -> None:
    code = 'from pathlib import Path\nP = Path("data") / "eval" / "cis.parquet"\n'
    src = _make_pkg(tmp_path, {"opinion/bad.py": code})
    assert find_eval_access(src, src / "evaluate")


def test_detector_flags_import_of_evaluate(tmp_path: Path) -> None:
    src = _make_pkg(tmp_path, {"predict/bad.py": "from sinpop.evaluate import EVAL_DIR\n"})
    assert find_eval_access(src, src / "evaluate")
    src2 = _make_pkg(tmp_path / "b", {"predict/bad.py": "from sinpop import evaluate\n"})
    assert find_eval_access(src2, src2 / "evaluate")


def test_detector_flags_windows_path(tmp_path: Path) -> None:
    src = _make_pkg(tmp_path, {"enrich/bad.py": 'X = "data\\\\eval\\\\y.csv"\n'})
    assert find_eval_access(src, src / "evaluate")


def test_detector_allows_evaluate_package(tmp_path: Path) -> None:
    src = _make_pkg(tmp_path, {"evaluate/ok.py": 'P = "data/eval/x.parquet"\n'})
    assert find_eval_access(src, src / "evaluate") == []


def test_detector_ignores_unrelated_words(tmp_path: Path) -> None:
    code = 'x = "evaluation"\ny = "medieval"\nz = "eval_score"\n'
    src = _make_pkg(tmp_path, {"validate/ok.py": code})
    assert find_eval_access(src, src / "evaluate") == []
