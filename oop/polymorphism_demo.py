#!/usr/bin/env python3
"""
Polymorphism Demo: Demonstrating method overriding in Python.

Classes defined:
- Shape (Base Class)
- Rectangle (Derived Class)
- Circle (Derived Class)
"""
import math

class Shape:
    """
    Base class for all geometric shapes. Defines the common interface
    for calculating area.
    """
    def area(self):
        """
        Calculates the area of the shape. Must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement the 'area()' method.")

class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        """
        Initializes a Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the base class method to calculate the rectangle's area:
        length * width.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        """
        Initializes a Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the base class method to calculate the circle's area:
        π * radius².
        """
        return math.pi * (self.radius ** 2)
