import subprocess
import sys
from pathlib import Path


def test_factor_cli():
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )

    # Run CLI like: python __main__.py factor x**2-1
    result = subprocess.run(
        [sys.executable, str(script_path), "factor", "x**2 -1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert "(x - 1)*(x + 1)" in result.stdout


def test_expand_cli():
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )

    result = subprocess.run(
        [sys.executable, str(script_path), "expand", "x**2 - 1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert "x**2 - 1" in result.stdout


def test_simplify_cli():
    # Path to your CLI script
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )

    result = subprocess.run(
        [sys.executable, str(script_path), "simplify", "x**2 - 1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert "x**2 - 1" in result.stdout


def test_wrong_command_cli():
    # Path to the cli script
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )

    result = subprocess.run(
        [sys.executable, str(script_path), "nonexistent_command", "x**2 - 1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # using the error code
    assert result.returncode > 0


def test_wrong_arg_position_cli():
    # Path to the script
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )
    result = subprocess.run(
        [sys.executable, str(script_path), "x**2 -1", "factor", "extra_arg"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert result.returncode > 0
