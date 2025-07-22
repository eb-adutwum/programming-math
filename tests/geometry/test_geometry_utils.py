from src.geometry import rect, tri, circ
import pytest


def test_rectangle_area_if_int():
    rect_obj = rect(5, 10)
    assert rect_obj.area() == 50


def test_rectangle_perimeter_if_int():
    rect_obj = rect(5, 10)
    assert rect_obj.perimeter() == 30


def test_triangle_area_if_int():
    tri_obj = tri(3, 4, 5)
    assert tri_obj.area() == 6.0


def test_triangle_perimeter_if_int():
    tri_obj = tri(3, 4, 5)
    assert tri_obj.perimeter() == 12


def test_circle_area_if_int():
    circ_obj = circ(7)
    assert circ_obj.area() == 153.93804002589985


def test_circle_circumference_if_int():
    circ_obj = circ(7)
    assert circ_obj.circumference() == 43.982297150257104


def test_rectangle_area_if_float():
    rect_obj = rect(5.5, 10.2)
    assert round(rect_obj.area(), 1) == 56.1


def test_rectangle_perimeter_if_float():
    rect_obj = rect(5.5, 10.2)
    assert round(rect_obj.perimeter(), 1) == 31.4


def test_triangle_area_if_float():
    tri_obj = tri(3.5, 4.5, 5.5)
    assert round(tri_obj.area(), 2) == 7.85


def test_triangle_perimeter_if_float():
    tri_obj = tri(3.5, 4.5, 5.5)
    assert round(tri_obj.perimeter(), 1) == 13.5


def test_circle_area_if_float():
    circ_obj = circ(7.5)
    assert round(circ_obj.area(), 2) == 176.71


def test_circle_circumference_if_float():
    circ_obj = circ(7.5)
    assert round(circ_obj.circumference(), 1) == 47.1


def test_rectangle_area_if_zero():
    with pytest.raises(ValueError) as execution_info:
        rect(0, 10)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_rectangle_perimeter_if_zero():
    with pytest.raises(ValueError) as execution_info:
        rect(0, 10)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_triangle_area_if_zero():
    with pytest.raises(ValueError) as execution_info:
        tri(0, 4, 5)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_triangle_perimeter_if_zero():
    with pytest.raises(ValueError) as execution_info:
        tri(0, 4, 5)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_circle_area_if_zero():
    with pytest.raises(ValueError) as execution_info:
        circ(0)
    assert str(execution_info.value) == "Radius must be a positive number."


def test_circle_circumference_if_zero():
    with pytest.raises(ValueError) as execution_info:
        circ(0)
    assert str(execution_info.value) == "Radius must be a positive number."


def test_rectangle_area_if_negative():
    with pytest.raises(ValueError) as execution_info:
        rect(-5, 10)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_rectangle_perimeter_if_negative():
    with pytest.raises(ValueError) as execution_info:
        rect(-5, 10)
    assert str(execution_info.value) == "Sides must be positive numbers."


def test_triangle_area_if_negative():
    with pytest.raises(ValueError) as execution_info:
        tri(-3, 4, 5)
    assert str(execution_info.value) == "Sides must be positive numbers."



def test_triangle_perimeter_if_negative():
    with pytest.raises(ValueError) as execution_info:
        tri(-3, 4, 5)

    assert str(execution_info.value) == "Sides must be positive numbers."


def test_circle_area_if_negative():
    with pytest.raises(ValueError) as execution_info:
        circ(-5)

    assert str(execution_info.value) == "Radius must be a positive number."


def test_circle_circumference_if_negative():
    with pytest.raises(ValueError) as execution_info:
        circ(-5)

    assert str(execution_info.value) == "Radius must be a positive number."
