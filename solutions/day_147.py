def pascal_triangle_row(n):
    pascal = [[1], [1,1]]
    if n == 1:
        return pascal[1]
    if n == 2:
        return pascal[2]

    for i in range(1, n - 1):
        new_row = []
        for j in range(0, len(pascal[i]) - 1):
            if j == 0:
                new_row.append(1)
            new_row.append(pascal[i][j] + pascal[i][j+1])

        new_row.append(1)
        pascal.append(new_row)

    return pascal[-1]

assert pascal_triangle_row(6) == [1, 5, 10, 10, 5, 1]
print(pascal_triangle_row(6))
print('Test pass.')