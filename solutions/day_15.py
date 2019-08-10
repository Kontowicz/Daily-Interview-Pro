def findPythagoreanTriplets(array):
    dict = {}
    for item in array:
        dict[item * item] = 0

    for i, i_val in enumerate(array):
        for j, j_val in enumerate(array):
            if j == i:
                continue
            if (i_val * i_val) + (j_val * j_val) in dict:
                return True
    return False


array = [3, 12, 5, 13]
result = findPythagoreanTriplets(array)
print('Result for array: {} is {}.'.format(array, result))
assert result == True
print('Test pass.')

