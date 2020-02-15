def searchMatrix(mat, value):
    for row in mat:
        if row[0] <= value and row[-1] >= value:
            if value in set(row):
                return True

    return False

mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

assert searchMatrix(mat, 4) == False
assert searchMatrix(mat, 10) == True

print(searchMatrix(mat, 4))
print(searchMatrix(mat, 10))

print('Test pass.')