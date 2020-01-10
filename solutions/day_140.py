def larger_number(nums):
    def get_position(arr, num):
        for i, item in enumerate(arr):
            if item > num:
                return i
        return -1

    to_return = []

    for i, item in enumerate(nums):
        pos = get_position(nums[i::], item)
        if pos == -1:
            to_return.append(-1)
        else:
            to_return.append(pos + i)

    return to_return


assert larger_number([3, 2, 5, 6, 9, 8]) == [2, 2, 3, 4, -1, -1]
print(larger_number([3, 2, 5, 6, 9, 8]))
print('Test pass.')

