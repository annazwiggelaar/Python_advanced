from Exercises_ch11.Point import Point
from Exercises_ch11.Rectangle import Rectangle

r = Rectangle(Point(0, 0), 10, 5)
area = r.area()
print(area)

print(r.perimeter())

print(r.flip())

print(r.contains(0, 0))
print(r.contains(3, 3))
print(r.contains(3, 7))
print(r.contains(3, 4.9999))
print(r.contains(-3, -3))
