# Week 1.5, Session 1: Task 4
from geometry import Circle
from geometry import Point
# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

x = input("insert x value as floating point: ")
y = input("insert y value as floating point: ")
p = Point(x,y)
c = Circle(3, p)
print(round(c.area(),4))
print(round(c.perimeter(),4))