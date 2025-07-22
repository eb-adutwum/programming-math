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
