from src.geometry import rect, tri, circ
import pytest


def test_rectangle_area_if_int():
    rect = rect(5, 10)
    assert rect.area() == 50


def test_rectangle_perimeter_if_int():
    rect = rect(5, 10)
    assert rect.perimeter() == 30


def test_triangle_area_if_int():
    tri = tri(3, 4, 5)
    assert tri.area() == 6.0


def test_triangle_perimeter_if_int():
    tri = tri(3, 4, 5)
    assert tri.perimeter() == 12


def test_circle_area_if_int():
    circ = circ(7)
    assert circ.area() == 153.93804002589985


def test_circle_circumference_if_int():
    circ = circ(7)
    assert circ.circumference() == 43.982297150257104


def test_rectangle_area_if_float():
    rect = rect(5.5, 10.2)
    assert round(rect.area(), 1) == 56.1


def test_rectangle_perimeter_if_float():
    rect = rect(5.5, 10.2)
    assert round(rect.perimeter(), 1) == 31.4


def test_triangle_area_if_float():
    tri = tri(3.5, 4.5, 5.5)
    assert round(tri.area(), 2) == 7.85


def test_triangle_perimeter_if_float():
    tri = tri(3.5, 4.5, 5.5)
    assert round(tri.perimeter(), 1) == 13.5


def test_circle_area_if_float():
    circ = circ(7.5)
    assert round(circ.area(), 2) == 176.71


def test_circle_circumference_if_float():
    circ = circ(7.5)
    assert round(circ.circumference(), 1) == 47.1


def test_rectangle_area_if_zero():
    temp = "might fail"
    try:
        temp = "fail"
        rect = rect(0, 10)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_rectangle_perimeter_if_zero():
    temp = "might fail"
    try:
        temp = "fail"
        rect = rect(0, 10)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_triangle_area_if_zero():
    temp = "might fail"
    try:
        temp = "fail"
        tri = tri(0, 4, 5)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_triangle_perimeter_if_zero():
    temp = "might fail"
    try:
        temp = "fail"
        tri = tri(0, 4, 5)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_circle_area_if_zero():
    temp = "might fail"
    try:
        temp = "fail"
        circ = circ(0)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_circle_circumference_if_zero():
    temp = "might fail"
    try:
        temp = "fail"
        circ = circ(0)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_rectangle_area_if_negative():
    temp = "might fail"
    try:
        temp = "fail"
        rect = rect(-5, 10)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_rectangle_perimeter_if_negative():
    temp = "might fail"
    try:
        temp = "fail"
        rect = rect(-5, 10)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_triangle_area_if_negative():
    temp = "might fail"
    try:
        temp = "fail"
        tri = tri(-3, 4, 5)
    except ValueError:
        temp = "passed"
    assert temp == "passed"

    # pytest.raises(ValueError, tri._area())


def test_triangle_perimeter_if_negative():
    temp = "might fail"
    try:
        temp = "fail"
        tri = tri(-3, 4, 5)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_circle_area_if_negative():
    temp = "might fail"
    try:
        temp = "fail"
        circ = circ(-7)
    except ValueError:
        temp = "passed"
    assert temp == "passed"


def test_circle_circumference_if_negative():
    temp = "might fail"
    try:
        temp = "fail"
        circ = circ(-7)
    except ValueError:
        temp = "passed"
    assert temp == "passed"
