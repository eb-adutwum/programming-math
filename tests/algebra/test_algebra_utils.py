from sympy import simplify, nsimplify

from src.algebra import factor, simplify, expand, solve, substitute


def assert_equivalent(expr1, expr2):
    assert simplify(expr1 - simplify(expr2)) == 0


def test_factor_diff_two_squares():
    assert_equivalent(factor("x**2 - 4"), "(x - 2)*(x + 2)")
    assert_equivalent(factor("a**2 - b**2"), "(a - b)*(a + b)")


def test_factor_trinomials():
    assert_equivalent(factor("x**2 + 3*x + 2"), "(x + 1)*(x + 2)")
    assert_equivalent(factor("x**2 - 5*x + 6"), "(x - 2)*(x - 3)")
    assert_equivalent(factor("x**2 - 4*x + 4"), "(x - 2)**2")


def test_factor_sum_of_squares():
    assert_equivalent(factor("x**2 + 1"), "x**2 + 1")  # Cannot be factored over reals


def test_factor_cubic_polynomials():
    assert_equivalent(factor("x**3 - 3*x**2 + 3*x - 1"), "(x - 1)**3")


def test_factor_multivariable_polynomials():
    assert_equivalent(
        factor("x**2 + y**2"), "x**2 + y**2"
    )  # Cannot be factored over reals
    assert_equivalent(factor("x**2 - y**2"), "(x - y)*(x + y)")
    assert_equivalent(factor("x**2 + 2*x*y + y**2"), "(x + y)**2")


def test_expand_basic():
    assert_equivalent(expand("(x + 2)*(x + 3)"), "x**2 + 5*x + 6")
    assert_equivalent(expand("(x - 1)*(x + 1)"), "x**2 - 1")


def test_expand_polynomials():
    assert_equivalent(expand("x**2*(x + 1)"), "x**3 + x**2")
    assert_equivalent(expand("(x + 1)**3"), "x**3 + 3*x**2 + 3*x + 1")


def test_expand_multivariable():
    assert_equivalent(expand("(x + y)*(x - y)"), "x**2 - y**2")
    assert_equivalent(expand("(x + y)**2"), "x**2 + 2*x*y + y**2")


def test_simplify_basic():
    assert_equivalent(simplify("x + 2 - 2 + x"), "2*x")
    assert_equivalent(simplify("x**2 - x**2 + 1"), "1")


def test_simplify_rational_expressions():
    assert_equivalent(simplify("x/(x + 1) + 1/(x + 1)"), "1")
    assert_equivalent(simplify("x**2/(x + 1) - x/(x + 1)"), "(x**2 - x)/(x + 1)")


def test_simplify_trigonometric():
    assert_equivalent(simplify("sin(x)**2 + cos(x)**2"), "1")
    assert_equivalent(simplify("tan(x) * cos(x)"), "sin(x)")


def test_solve_linear_equations():
    assert set(solve(variables="x", eq1="2*x + 3 = 7").values()) == {2}
    assert set(solve(variables="x", eq1="x - 5 = 0").values()) == {5}
    assert set(solve(variables="y", eq1="1/3*y + 2 = 0").values()) == {-6}


def test_solve_quadratic_equations():
    def flatten(lst):
        return [item for sublist in lst for item in sublist]

    assert set(flatten(solve(variables="x", eq1="x**2 - 4 = 0"))) == {2, -2}
    assert set(flatten(solve(variables="x", eq1="x**2 + 3*x + 2 = 0"))) == {-1, -2}
    assert set(flatten(solve(variables="x", eq1="x**2 - 5*x + 6 = 0"))) == {2, 3}


def test_solve_system_of_equations():
    equations = {"eq1": "x + y = 5", "eq2": "2*x - y = 1"}
    result = solve(variables="x, y", **equations)
    assert set(result.values()) == {2, 3}

    equations = {"eq1": "x + 2*y = 8", "eq2": "3*x - y = 1"}
    result = solve(variables="x, y", **equations)
    assert set(result.values()) == {nsimplify(23 / 7), nsimplify(10 / 7)}


def test_solve_multivariable_equations():
    equations = {
        "eq1": "x + y + z = 6",
        "eq2": "2*x - y + 3*z = 11",
        "eq3": "x - 2*y + z = 3",
    }
    result = solve(variables="x, y, z", **equations)
    assert set(result.values()) == {2, 1, 3}


def test_solve_change_of_subject():
    equations = {
        "eq1": "x + y = 5",
    }
    result = solve(variables="y", **equations)
    assert_equivalent(result[simplify("y")], "-x + 5")


def test_substitute_basic():
    assert_equivalent(substitute("x + y", {"x": 2, "y": 3}), 5)
    assert_equivalent(substitute("x**2 + y", {"x": 2, "y": 3}), 7)


def test_substitute_polynomial():
    assert_equivalent(substitute("x**2 + 2*x + 1", {"x": 3}), 16)
    assert_equivalent(substitute("x**2 - y", {"x": 4, "y": 5}), 11)


def test_substitute_trigonometric():
    assert_equivalent(substitute("sin(x) + cos(x)", {"x": 0}), 1)
    assert_equivalent(substitute("tan(x) - sin(x)", {"x": 0}), 0)


def test_substitute_rational():
    assert_equivalent(nsimplify(substitute("x/(x + 1)", {"x": 2})), 2 / 3)
    assert_equivalent(nsimplify(substitute("1/(x + y)", {"x": 1, "y": 2})), 1 / 3)
