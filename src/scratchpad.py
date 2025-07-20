from sympy import symbols, factor, expand, simplify, solve, Eq

from src.algebra import factor, simplify, expand, solve

equations = {"eq1": "v = 1/2 * m * v**2"}
result = solve(variables="v", **equations)

print(result)
