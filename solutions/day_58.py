def calcAngle(h, m):
    angle = abs(0.5 * ((60 * h) - (11 * m)))
    if angle > 180:
        return 360 - angle
    return angle

assert calcAngle(3, 30) == 75
assert calcAngle(12, 30) == 165
print(calcAngle(3, 30))
print(calcAngle(12, 30))
print('Test pass.')
