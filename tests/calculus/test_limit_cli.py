"""CLI for calculus operations"""

import subprocess
import sys
from pathlib import Path


entry_script_path = (Path(__file__).resolve().parents[2] / "src" / "calculus" / "__main__.py")


def test_limit_cli():
    """
    Test the limit command in the calculus CLI.
    :return: None
    """

    result = subprocess.run(
        [sys.executable, str(entry_script_path), "lim", "x**2 + 2*x + 1,1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    assert "4.0" in result.stdout

def test_limit_cli_polynomial():
    """
    Test the limit command in the calculus CLI for polynomial expressions.
    :return: None
    """

    result = subprocess.run(
        [sys.executable, str(entry_script_path), "lim", "x**4 + x**2 + 1,0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    assert "1.0" in result.stdout


def test_limit_cli_non_polynomial():
    """
    Test the limit command in the calculus CLI for non-polynomial expressions.
    :return: None
    """

    result = subprocess.run(
        [sys.executable, str(entry_script_path), "lim", "1/x,0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    assert "inf" in result.stdout


def test_limit_cli_negative():
    """
    Test the limit command in the calculus CLI for negative values.
    :return: None
    """

    result = subprocess.run(
        [sys.executable, str(entry_script_path), "lim", "x**2 - 4,-2"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    assert "0.0" in result.stdout

def test_limit_cli_fraction():
    """
    Test the limit command in the calculus CLI for fractional expressions.
    :return: None
    """

    result = subprocess.run(
        [sys.executable, str(entry_script_path), "lim", "x/(x+1),0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    assert "0.0" in result.stdout