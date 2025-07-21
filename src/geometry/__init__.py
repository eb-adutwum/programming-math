"""Geometry module initialization file."""

from .geometry_utils import (
    _Rectangle as Rectangle,
    _Triangle as Triangle,
    _Circle as Circle,
)

__all__ = ["Rectangle", "Triangle", "Circle"]

# print("Geometry module loaded. Available classes: Rectangle, Triangle, Circle.")
