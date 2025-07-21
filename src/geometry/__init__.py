"""Geometry module initialization file."""

from .geometry_utils import (
    Rectangle as rect,
    Triangle as tri,
    Circle as circ,
)

__all__ = ["rect", "tri", "circ"]

# print("Geometry module loaded. Available classes: Rectangle, Triangle, Circle.")
