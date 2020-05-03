from Exercises_ch11.MyTime import MyTime
from Exercises_ch11.Point import Point

print(MyTime(23, 45, 26))

i = MyTime(12, 13, 14)
o = MyTime(3, 25, 56)

print(i.add_time(o))

t1 = MyTime(4, 35, 43)
t2 = MyTime(6, 56, 3)
t3 = MyTime(5, 25, 6)

print(t3.between(t1, t2))

print(t1.after(t2))

print(t3 > t2)

print(t1.increment(-16000))

