def rotate(mat):
    rot = list(zip(*mat[::-1]))
    for i in range(0, len(rot)):
        rot[i] = list(rot[i])

    return rot

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Looks like
# 7 4 1
# 8 5 2
# 9 6 3
assert rotate(mat) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(rotate(mat))
print('Test pass.')