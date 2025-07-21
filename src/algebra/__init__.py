"""Algebra module initialization file."""

from .algebra_utils import (
    _factorize as factor,
    _simplify as simplify,
    _expand as expand,
    _solve as solve,
    _substitute as substitute,
)

__all__ = ["factor", "simplify", "expand", "solve", "substitute"]

# print("Algebra module loaded. Available functions: factor, simplify, expand, solve, substitute.")
