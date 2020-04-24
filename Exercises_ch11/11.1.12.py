from Exercises_ch11.Point import Point

distance = Point()

p = Point(3, 4)
q = Point(5, 12)
r = p.distance(q)
print(r)

z = Point(3, 4).reflect_x()
print(z)

print(Point(4, 10).slope_from_origin())

print(Point(4, 11).get_line_to(Point(6, 15)))
