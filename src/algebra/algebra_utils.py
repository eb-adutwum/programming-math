from sympy import symbols, factor, expand, simplify, solve, Eq


def _factorize(expression: str, *, variables: str = "x") -> any:
    expression = _simplify(expression)
    return factor(expression)


def _expand(expression: str, *, variables: str = "x") -> any:
    expression = _simplify(expression)
    return expand(expression)


def _simplify(expression: str, *, variables: str = "x") -> any:
    return simplify(simplify(expression))


def parse_eq(equation: str) -> str:
    if "=" in equation:
        lhs, rhs = equation.split("=")
        return Eq(_simplify(lhs), _simplify(rhs))
    return Eq(_simplify(equation))


def _solve(*, variables: str = "x", **equations) -> any:
    """
    Eq requires (LHS, RHS)
    solve requires expression (=0 by default) or *args of equations and a tuple of variable(s) (to solve simultaneously)
    well for "solve", if you pass in one variable for a multivariate equation, it will perform a change of subject
    """
    equations_map = {k: parse_eq(v) for k, v in equations.items()}

    variables = symbols(str(variables))
    return solve(tuple(equations_map.values()), variables)


def _substitute(expression: str, variables: dict) -> float:
    expr = ""
    for i in range(len(expression)):
        temp = expression[i]
        if temp in variables:
            temp = str(variables[temp])
        expr += temp

    return _simplify(expr)


# print(_substitute("x**2 + y", {"x": 2, "y": 3}))
