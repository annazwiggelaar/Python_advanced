class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width h, height h"""
        self.corner = posn
        self.width = w
        self.height = h

    def area(self, w, h):
        area = int(w) * int(h)
        return area

    def perimeter(self, w, h):
        i = w * 2 + h * 2
        return i
