from src.calculus import lim


def test_lim():
    """Test the limit of a polynomial function."""
    assert lim("x**2 + 2*x + 1", 1) == float(4)


def test_lim_polynomial():
    """Test the limit of a polynomial function at zero."""
    assert lim("x**4 + x**2 + 1", 0) == float(1)


def test_lim_non_polynomial():
    """Test the limit of a rational function at zero"""
    assert lim("1/x", 0) == float("inf")


def test_lim_negative():
    """Test the limit of a polynomial function at a negative point."""
    assert lim("x**2 - 4", -2) == float(0)


def test_lim_fraction():
    """Test the limit of a rational function at zero."""
    assert lim("x/(x+1)", 0) == float(0)


def test_lim_infinity():
    """Test the limit of a rational function as x approaches infinity."""
    assert lim("1/x", float("inf")) == float(0)


def test_lim_negative_infinity():
    """Test the limit of a rational function as x approaches negative infinity."""
    assert lim("1/x", float("-inf")) == float(0)


def test_lim_direction_positive():
    """Test the limit of a rational function as x approaches zero from the positive side."""
    assert lim("1/x", 0, side="+") == float("inf")


def test_lim_direction_negative():
    """Test the limit of a rational function as x approaches zero from the negative side."""
    assert lim("1/x", 0, side="-") == float("-inf")


def test_lim_polynomial_infinity():
    """Test the limit of a polynomial function as x approaches infinity."""
    assert lim("x**2 + 2*x + 1", float("inf")) == float("inf")
