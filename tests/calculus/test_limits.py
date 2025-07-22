from src.calculus import lim


def test_lim():
    assert lim("x**2 + 2*x + 1", 1) == float(4)


def test_lim_polynomial():
    assert lim("x**4 + x**2 + 1", 0) == float(1)


def test_lim_non_polynomial():
    assert lim("1/x", 0) == float("inf")


def test_lim_negative():
    assert lim("x**2 - 4", -2) == float(0)


def test_lim_fraction():
    assert lim("x/(x+1)", 0) == float(0)

def test_lim_infinity():
    assert lim("1/x", float("inf")) == float(0)

def test_lim_negative_infinity():
    assert lim("1/x", float("-inf")) == float(0)

def test_lim_direction_positive():
    assert lim("1/x", 0, side="+") == float("inf")

def test_lim_direction_negative():
    assert lim("1/x", 0, side="-") == float("-inf")

def test_lim_polynomial_infinity():
    assert lim("x**2 + 2*x + 1", float("inf")) == float("inf")