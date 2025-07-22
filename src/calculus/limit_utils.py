"""limits module"""
from coverage.debug import simplify

from algebra import substitute
from sympy import limit


def lim(expression: str, point: float, *, side="+") -> float:
    """
    Calculate the limit of an expression as it approaches a point.
    :param side: direction of limit
    :param expression: The expression to evaluate.
    :param point: The point to approach.
    :return: The limit of the expression as it approaches the point.
    """
    # Substitute the point into the expression
    if is_polynomial(expression):
        if point != float('-inf') or point != float('inf'):
            substituted_expression = substitute(expression, {"x": point})
            return float(substituted_expression)
        return point
    else:
        return float(limit(simplify(expression), simplify('x'), point, side))


def is_polynomial(expression: str) -> bool:
    """
    Check if the expression is a polynomial.
    :param expression: The expression to check.
    :return: True if the expression is a polynomial, False otherwise.
    """
    # A check if x is a denominator at any point in the expression

    expression = expression.replace("-", "+")
    terms = expression.split("+")

    for term in terms:
        temp = term.split("/")
        if len(temp) > 1:
            if "x" in temp[1]:
                return False
    return True
