# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width or height are not an integer")
        if width <= 0 or height <= 0:
            raise ValueError("width or height is smaller than or equal to 0")
        self.width = width
        self.height = height
    def is_square(self):
        """
        Returns true if the rectangle is a square and false if not
        """
        if self.width == self.height:
            return True
        return False
    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height
    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        return self.width * 2 + self.height * 2

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    