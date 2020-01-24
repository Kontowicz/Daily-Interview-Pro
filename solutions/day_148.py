def transpose(mat):
    return [list(row) for row in zip(*mat)]

mat = [
    [1, 2, 3],
    [4, 5, 6],
]

assert transpose(mat) == [[1, 4], [2, 5], [3, 6]]
print(transpose(mat))
print('Test pass.')