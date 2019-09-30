import copy
def findRange(nums):
    orginal = copy.deepcopy(nums)
    nums.sort()

    start = -1
    stop = -2

    for i in range(0, len(nums)):
        if orginal[i] != nums[i]:
            if start == -1:
                start = i
            else:
                stop = i

    return (start, stop)

print(findRange([1, 7, 9, 5, 7, 8, 10]))
assert findRange([1, 7, 9, 5, 7, 8, 10]) == (1, 5)
print('Test pass.')
# (1, 5)