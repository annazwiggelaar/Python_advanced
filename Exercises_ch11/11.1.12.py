class Point:
    """Create a new Point, at coordinates x, y"""

    def __init__(self, x=0, y=0):
        """Create a new point at x, y"""
        self.x = x
        self.y = y

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


class SMS_store:
    """Create new SMS store"""

    my_inbox = SMS_store()


    def __init__(self, has_been_viewed, from_number, time_arrived, text_of_SMS):
        self.has_been_viewed = has_been_viewed
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):

    def message_count(self):
        count = len()




p = Point(3, 4)
q = Point(5, 12)
r = p.distance(q)
print(r)

z = Point(3, 4).reflect_x()
print(z)

i = Point(4, -10).slope_from_origin()
print(i)

print(Point(4, 11).get_line_to(Point(6, 15)))
