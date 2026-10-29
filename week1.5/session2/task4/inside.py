# Week 1.5, Session 2: Task 4
from geometry import Circle
from geometry import Point
# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
p = Point(1,1)
c1 = Circle(2,Point(0,0))
c2 = Circle(1,Point(5,5))
if p in c1:
    print(f"{p} is in {c1}")
else:
    print(f"{p} is not in {c1}")
if p in c2:
    print(f"{p} is in {c2}")
else:
    print(f"{p} is not in {c2}")