def longest(array):
    values = [1] * len(array)

    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                values[i] = max(values[i], values[j] + 1)
    return max(values)

print(longest([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
assert longest([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
print('Test pass.')