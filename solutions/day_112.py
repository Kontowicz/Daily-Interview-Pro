def paths_through_maze(maze):
    result = []

    for row in maze:
        tmp = []
        for item in row:
            if item == 1:
                tmp.append(0)
            else:
                tmp.append(1)
        result.append(tmp)

    for i in range(1, len(result)):
        for j in range(1, len(result[i])):
            if result[i][j] == 0:
                continue
            else:
                result[i][j] = result[i - 1][j] + result[i][j - 1]

    return result[-1][-1]

matrix = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]

assert paths_through_maze(matrix) == 2
print(paths_through_maze(matrix))
print('Test pass.')
