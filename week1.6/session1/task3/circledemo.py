# Week 1.6, Session 1: Task 3
from shapes import Circle
from point import Point

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
c = Circle(Point(0,0))
c.set_radius(2.5)
print(c)
print(f"{c.area():.3f}")
print(f"{c.perimeter():.3f}")
c.set_position(Point(2,5))
print(c)