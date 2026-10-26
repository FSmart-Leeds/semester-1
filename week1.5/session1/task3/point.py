# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        '''
            Sets the coordinates for the point
        '''
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    # Add distance_to() method here
    def distance_to(self, p2):
        x_dist = self.x - p2.x
        y_dist = self.y - p2.y

        return math.sqrt(x_dist ** 2 + y_dist ** 2)
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p1 = Point(2.0, 4.5)
p2 = Point(-1.0, 3.0)
print(p1.distance())
print(p2.distance())

print(p1.distance_to(p2))