def reshape_matrix(mat, x, y):
    if len(mat) * len(mat) != x * y:
        return None
    else:
        flat_matrix = [item for row in mat for item in row]
        begin = 0
        to_return = []
        for i in range(0, y):
            to_return.append(flat_matrix[begin:begin+x])
            begin += x
        return to_return

print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None