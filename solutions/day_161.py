def maxNonAdjacentSum(nums):
    to_return = []

    for i in range(0, len(nums) - 1):
        tmp = nums[i+2::]
        if tmp != []:
            to_return.append(nums[i] + max(tmp))

    return max(to_return)

assert maxNonAdjacentSum([3, 4, 1, 1]) == 5
assert maxNonAdjacentSum([2, 1, 2, 7, 3]) == 9

print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# 9
# max sum is 2 (index 0) + 7 (index 3)
print('Test pass.')