def findSingle(nums):
    to_return = nums[0]

    for number in nums[1::]:
        to_return ^= number
    return to_return

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
assert findSingle(nums) == 3
print(findSingle(nums))
print('Test pass.')