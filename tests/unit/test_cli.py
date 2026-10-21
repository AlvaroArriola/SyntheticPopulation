"""CLI (puerta G0.4) y puerta F0."""

from __future__ import annotations

from typer.testing import CliRunner

from sinpop.cli import COMMANDS, app
from sinpop.validate import phases


def test_help_lists_all_commands() -> None:
    out = CliRunner().invoke(app, ["--help"], terminal_width=200)
    assert out.exit_code == 0
    for c in COMMANDS:
        assert c in out.output


def test_documented_commands_are_registered() -> None:
    names = {c.name or c.callback.__name__ for c in app.registered_commands}
    assert set(COMMANDS) <= names


def test_pending_commands_exit_with_code_2() -> None:
    # Los territorios por municipios se generan en F5.
    r = CliRunner().invoke(
        app, ["build", "--territory", "MUNIS:configs/territorios/ejemplo_almeria.yaml"]
    )
    assert r.exit_code == 2
    r = CliRunner().invoke(app, ["politics", "--run", "x"])
    assert r.exit_code == 2


def test_opinion_sin_poblacion_falla_con_mensaje() -> None:
    r = CliRunner().invoke(app, ["opinion", "--run", "no_existe"])
    assert r.exit_code == 1


def test_audit_sin_poblacion_falla_con_mensaje() -> None:
    r = CliRunner().invoke(app, ["audit", "--run", "no_existe"])
    assert r.exit_code == 1


def test_gate_f0_checks_pass_without_recursion(monkeypatch) -> None:
    monkeypatch.setenv(phases._IN_GATE_ENV, "1")
    checks = {c.id: c for c in phases.run_checks(0)}
    assert set(checks) == {"G0.1", "G0.2", "G0.3", "G0.4"}
    assert checks["G0.1"].ok is None  # anidado: no se relanza pytest
    assert checks["G0.2"].ok and checks["G0.3"].ok and checks["G0.4"].ok


def test_gate_f1_has_all_checks_and_human_review() -> None:
    checks = {c.id: c for c in phases.run_checks(1)}
    assert set(checks) == {f"G1.{i}" for i in range(1, 7)}
    assert checks["G1.6"].ok is None  # revisión humana: nunca automática
