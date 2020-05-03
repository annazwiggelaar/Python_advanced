class Point:
    """Create a new Point, at coordinates x, y"""

    def __init__(self, x=0, y=0):
        """Create a new point at x, y"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def distance(self, target):
        """Return the distance between myself and the target"""
        mx = (target.x - self.x) ** 2
        my = (target.y - self.y) ** 2
        result = (mx + my) ** 0.5
        return result

    def reflect_x(self):
        new__y = self.y - (2 * self.y)
        new_point = (self.x, new__y)
        return new_point

    def slope_from_origin(self):
        sx = (self.x - 0)
        sy = (self.y - 0)
        slope = sy / sx
        return slope

    def get_line_to(self, target):
        slope = (target.y - self.y)/(target.x - self.x)
        o = int(slope * target.x)
        if o > 0:
            b = target.y - o
        else:
            b = target.y + o
        return "y =", slope, "x +", b

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def multadd(self, y, z):
        return self * y + z

    def reverse(self):
        (self.x, self. y) = (self.y, self.x)

    def front_and_back(self):
        import copy
        back = copy.copy(self)
        back.reverse()
        print(str(self) + str(back))
