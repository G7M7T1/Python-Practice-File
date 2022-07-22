from collections import namedtuple
from math import sqrt

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

line_length_1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(line_length_1)

# or -----------------------------------------------------------------

Point = namedtuple("Point", ["x", "y"])

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

line_length_2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(line_length_2)
