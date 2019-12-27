def missing_ranges(nums, low, high):
    to_return = []
    for i in range(0, len(nums) - 1):
        if nums[i] + 1 != nums[i + 1]:
            to_return.append((nums[i]+ 1, nums[i+1]-1))

    return to_return

assert missing_ranges([1, 3, 5, 10], 1, 10) == [(2, 2), (4, 4), (6, 9)]
print(missing_ranges([1, 3, 5, 10], 1, 10))
print('Test pass.')