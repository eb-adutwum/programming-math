"""Algebra utilities for symbolic computation using SymPy."""

from sympy import symbols, factor, expand, simplify, solve, Eq


def _factorize(expression: str) -> any:
    expression = _simplify(expression)
    return factor(expression)


def _expand(expression: str) -> any:
    expression = _simplify(expression)
    return expand(expression)


def _simplify(expression: str) -> any:
    return simplify(simplify(expression))


def parse_eq(equation: str) -> str:
    """
    Parses an equation string into a SymPy Eq object.
    :param equation: The equation string to parse.
    :return: Eq - A SymPy Eq object representing the equation.
    """
    if "=" in equation:
        lhs, rhs = equation.split("=")
        return Eq(_simplify(lhs), _simplify(rhs))
    return Eq(_simplify(equation), "")


def _solve(*, variables: str = "x", **equations) -> any:
    """
    Eq requires (LHS, RHS)
    solve requires expression (=0 by default) or *args of equations
    and a tuple of variable(s) (to solve simultaneously)
    well for "solve", if you pass in one variable for a multivariate equation,
    it will perform a change of subject
    """
    equations_map = {k: parse_eq(v) for k, v in equations.items()}

    variables = symbols(str(variables))
    return solve(tuple(equations_map.values()), variables)


def _substitute(expression: str, variables: dict) -> float:
    expr = ""
    for i in range(len(expression)):
        temp = expression[i]
        if temp in variables:
            temp = "(" + str(variables[temp]) + ")"
        expr += temp

    return _simplify(expr)
