from math import degrees, sqrt, atan


x1 = -5
y1 = 8

x2 = 4
y2 = 6

xd = x2 - x1
yd = y2 -y1

h = round(sqrt((xd**2 + yd**2)), 2)
d = round(degrees((atan((yd) / (xd)))), 2)

print(f"The distance between the two points is {h}units\nAnd the angle from the first point to the second is {d}deg")