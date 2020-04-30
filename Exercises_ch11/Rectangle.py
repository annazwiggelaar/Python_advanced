class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width h, height h"""
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        i = self.width * 2 + self.height * 2
        return i

    def flip(self):
        h_2 = self.width
        w_2 = self.height
        return w_2, h_2

    def contains(self, w, h):
        if 0 <= w < self.width and 0 <= h < self.height:
            return True
        else:
            return False

