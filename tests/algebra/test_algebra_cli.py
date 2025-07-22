"""Test cases for the algebra CLI commands."""

import subprocess
import sys
from pathlib import Path


def test_factor_cli():
    """
    Test the factor command in the algebra CLI.
    :return: None
    """
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )

    # Run CLI like: python __main__.py factor x**2-1
    result = subprocess.run(
        [sys.executable, str(script_path), "factor", "x**2 -1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    assert "(x - 1)*(x + 1)" in result.stdout


def test_expand_cli():
    """
    Test the expand command in the algebra CLI.
    :return: None
    """
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )

    result = subprocess.run(
        [sys.executable, str(script_path), "expand", "x**2 - 1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    assert "x**2 - 1" in result.stdout


def test_simplify_cli():
    """
    Test the simplify command in the algebra CLI.
    :return: None
    """
    # path to cli script
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )

    result = subprocess.run(
        [sys.executable, str(script_path), "simplify", "x**2 - 1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    assert "x**2 - 1" in result.stdout


def test_wrong_command_cli():
    """
    Test the CLI with a command that does not exist.
    :return: None
    """
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )

    result = subprocess.run(
        [sys.executable, str(script_path), "nonexistent_command", "x**2 - 1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,  # We expect this to fail
    )

    # using the error code
    assert result.returncode > 0


def test_wrong_arg_position_cli():
    """
    Test the CLI with an incorrect argument position.
    :return: None
    """
    script_path = (
        Path(__file__).resolve().parents[2] / "src" / "algebra" / "__main__.py"
    )
    result = subprocess.run(
        [sys.executable, str(script_path), "x**2 -1", "factor", "extra_arg"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    assert result.returncode > 0
