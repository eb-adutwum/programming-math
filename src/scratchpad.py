"""Scratchpad for testing and experimenting with code snippets."""

from src.algebra import solve

equations = {"eq1": "v = 1/2 * m * v**2"}
result = solve(variables="v", **equations)

print(result)
