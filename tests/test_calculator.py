import pytest
from app.calculator.repl import CalculatorREPL


def test_show_help(capsys):
    repl = CalculatorREPL()
    repl.show_help()
    captured = capsys.readouterr()
    assert "Commands:" in captured.out


def test_history_empty(capsys):
    repl = CalculatorREPL()
    repl.show_history()
    captured = capsys.readouterr()
    assert "No history available." in captured.out


def test_handle_command_add(capsys):
    repl = CalculatorREPL()
    repl.handle_command("add 1 2")
    captured = capsys.readouterr()
    assert "add 1.0 2.0 = 3.0" in captured.out
    assert repl.history[-1] == "add 1.0 2.0 = 3.0"


def test_invalid_command():
    repl = CalculatorREPL()
    with pytest.raises(ValueError):
        repl.handle_command("add 1")


def test_run_exit(monkeypatch, capsys):
    repl = CalculatorREPL()
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out


def test_run_help(monkeypatch, capsys):
    repl = CalculatorREPL()
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "Commands:" in captured.out


def test_history_with_data(capsys):
    repl = CalculatorREPL()
    repl.handle_command("add 1 1")
    repl.show_history()
    captured = capsys.readouterr()
    assert "add 1.0 1.0 = 2.0" in captured.out


def test_run_history(monkeypatch, capsys):
    repl = CalculatorREPL()
    repl.handle_command("add 5 5")  # Pre-populate history
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "add 5.0 5.0 = 10.0" in captured.out


def test_run_eoferror(monkeypatch, capsys):
    repl = CalculatorREPL()
    # Simulate input raising EOFError
    monkeypatch.setattr("builtins.input", lambda _: (_ for _ in ()).throw(EOFError))
    repl.run()
    captured = capsys.readouterr()
    # No crash, exits cleanly
    assert "Welcome to Calculator!" in captured.out

def test_run_power(monkeypatch, capsys):
    repl = CalculatorREPL()
    inputs = iter(["pow 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "pow 2.0 3.0 = 8.0" in captured.out

def test_run_modulo(monkeypatch, capsys):
    repl = CalculatorREPL()
    inputs = iter(["mod 10 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    repl.run()
    captured = capsys.readouterr()
    assert "mod 10.0 3.0 = 1.0" in captured.out

