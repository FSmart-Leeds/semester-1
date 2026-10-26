# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        '''
            Sets the coordinates for the point
        '''
        self.x = x
        self.y = y
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def distance_to(self, p2):
        x_dist = self.x - p2.x
        y_dist = self.y - p2.y
        return math.sqrt(x_dist ** 2 + y_dist ** 2)

class Circle:
    """
    A Circle in 2D space.
    """
    def __init__(self, radius, centre ):
        self.centre = centre
        self.radius = radius
    def area(self):
        """
        Returns the Area of the Circle.
        """
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        """
        Returns the Perimeter of the Circle.
        """
        return 2 * self.radius * math.pi
    
# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
