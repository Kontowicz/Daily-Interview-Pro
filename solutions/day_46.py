
def sortColors(nums):
    elem = [0] * 3

    for item in nums:
        elem[item] = elem[item] + 1

    return ([0] * elem[0]) + ([1] * elem[1]) + ([2] * elem[2])

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

result = sortColors(nums)
print("After Sort: ")
print(result)
assert result == [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print('Test pass.')