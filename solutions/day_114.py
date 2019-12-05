class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"({self.x}, {self.y})"

def closest_points(points, k, p):
    to_return = []
    from math import sqrt
    for point in points:
        to_return.append([sqrt(pow((point.x - p.x), 2) + pow((point.y - p.y), 2)),point])

    to_return.sort(key= lambda x: x[0])
    tmp = []

    for i in range(0, k):
        tmp.append(to_return[i][1])

    return tmp

points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
]

print(closest_points(points, 2, Point(0, 2)))
# [(0, 0), (1, 1)]