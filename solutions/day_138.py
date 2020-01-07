import math
def closest_points(points, k):
    distance_points = [[math.sqrt((x[0]**2)+(x[1]**2)), x[0], x[1]] for x in points]
    distance_points.sort(key = lambda x: x[0])
    return [(distance_points[i][1], distance_points[i][2]) for i in range(0, k)]

assert set(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2)) == set([(1, 2), (0, 0)])
print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
print('Test pass.')