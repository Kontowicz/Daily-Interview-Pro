def max_change(mat):
    to_return = [[0 for x in range(0, len(mat[0]))] for x in range(0, len(mat))]
    to_return[0][0] = mat[0][0]

    for i in range(1, len(mat)):
        to_return[i][0] = to_return[i-1][0] + mat[i][0]

    for i in range(1, len(mat)):
        to_return[0][i] = to_return[0][i-1] + mat[0][i]

    for i in range(1, len(mat)):
        for j in range(1, len(mat[i])):
            to_return[i][j] = max(to_return[i-1][j] + mat[i][j], to_return[i][j-1] + mat[i][j])

    return to_return[len(mat)-1][len(mat[0])-1]
mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

assert max_change(mat) == 13
print(max_change(mat))
print('Test pass.')