"""Unit tests for geometry utilities in the profMath project."""

import pytest
from src.geometry import rect, tri, circ


def test_rectangle_area_if_int():
    """
    Test the area of a rectangle with integer sides.
    :return: None
    """
    rect_obj = rect(5, 10)
    assert rect_obj.area() == 50


def test_rectangle_perimeter_if_int():
    """
    Test the perimeter of a rectangle with integer sides.
    :return: None
    """
    rect_obj = rect(5, 10)
    assert rect_obj.perimeter() == 30


def test_triangle_area_if_int():
    """
    Test the area of a triangle with integer sides.
    :return: None
    """
    tri_obj = tri(3, 4, 5)
    assert tri_obj.area() == 6.0


def test_triangle_perimeter_if_int():
    """
    Test the perimeter of a triangle with integer sides.
    :return: None
    """
    tri_obj = tri(3, 4, 5)
    assert tri_obj.perimeter() == 12


def test_circle_area_if_int():
    """
    Test the area of a circle with integer radius.
    :return: None
    """
    circ_obj = circ(7)
    assert circ_obj.area() == 153.93804002589985


def test_circle_circumference_if_int():
    """
    Test the circumference of a circle with integer radius.
    :return: None
    """
    circ_obj = circ(7)
    assert circ_obj.circumference() == 43.982297150257104


def test_rectangle_area_if_float():
    """
    Test the area of a rectangle with float sides.
    :return: None
    """
    rect_obj = rect(5.5, 10.2)
    assert round(rect_obj.area(), 1) == 56.1


def test_rectangle_perimeter_if_float():
    """
    Test the perimeter of a rectangle with float sides.
    :return: None
    """
    rect_obj = rect(5.5, 10.2)
    assert round(rect_obj.perimeter(), 1) == 31.4


def test_triangle_area_if_float():
    """
    Test the area of a triangle with float sides.
    :return: None
    """

    tri_obj = tri(3.5, 4.5, 5.5)
    assert round(tri_obj.area(), 2) == 7.85


def test_triangle_perimeter_if_float():
    """
    Test the perimeter of a triangle with float sides.
    :return: None
    """
    tri_obj = tri(3.5, 4.5, 5.5)
    assert round(tri_obj.perimeter(), 1) == 13.5


def test_circle_area_if_float():
    """
    Test the area of a circle with float radius.
    :return: None
    """
    circ_obj = circ(7.5)
    assert round(circ_obj.area(), 2) == 176.71


def test_circle_circumference_if_float():
    """
    Test the circumference of a circle with float radius.
    :return: None
    """

    circ_obj = circ(7.5)
    assert round(circ_obj.circumference(), 1) == 47.1


def test_rectangle_area_if_zero():
    """
    Test the area of a rectangle with zero sides.
    :return: None
    """

    with pytest.raises(ValueError) as execution_info:
        rect(0, 10)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_rectangle_perimeter_if_zero():
    """
    Test the perimeter of a rectangle with zero sides.
    :return: None
    """

    with pytest.raises(ValueError) as execution_info:
        rect(0, 10)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_triangle_area_if_zero():
    """
    Test the area of a triangle with zero sides.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        tri(0, 4, 5)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_triangle_perimeter_if_zero():
    """
    Test the perimeter of a triangle with zero sides.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        tri(0, 4, 5)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_circle_area_if_zero():
    """
    Test the area of a circle with zero radius.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        circ(0)
    assert str(execution_info.value) == "Radius must be a positive number."


def test_circle_circumference_if_zero():
    """
    Test the circumference of a circle with zero radius.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        circ(0)
    assert str(execution_info.value) == "Radius must be a positive number."


def test_rectangle_area_if_negative():
    """
    Test the area of a rectangle with negative sides.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        rect(-5, 10)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_rectangle_perimeter_if_negative():
    """
    Test the perimeter of a rectangle with negative sides.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        rect(-5, 10)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_triangle_area_if_negative():
    """
    Test the area of a triangle with negative sides.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        tri(-3, 4, 5)
    assert str(execution_info.value) == "Sides must be positive numbers."

    # pytest.raises(ValueError, tri._area())


def test_triangle_perimeter_if_negative():
    """
    Test the perimeter of a triangle with negative sides.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        tri(-3, 4, 5)

    assert str(execution_info.value) == "Sides must be positive numbers."


def test_circle_area_if_negative():
    """
    Test the area of a circle with negative radius.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        circ(-5)

    assert str(execution_info.value) == "Radius must be a positive number."


def test_circle_circumference_if_negative():
    """
    Test the circumference of a circle with negative radius.
    :return: None
    """
    with pytest.raises(ValueError) as execution_info:
        circ(-5)

    assert str(execution_info.value) == "Radius must be a positive number."
