def square_numbers(nums):
    return sorted([x * x for x in nums])

assert square_numbers([-5, -3, -1, 0, 1, 4, 5]) == [0, 1, 1, 9, 16, 25, 25]
print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
print('Test pass.')