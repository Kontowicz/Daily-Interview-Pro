def find_min_max(nums):
    min_nums = 0
    max_nums = 0
    start = 1
    if len(nums) % 2 == 0:
        min_nums = min(nums[0::1])
        max_nums = max(nums[0::1])
        start = 2
    else:
        min_nums = max_nums = nums[0]

    for i in range(start, len(nums) - 1):
        if nums[i] < nums[i+1]:
            min_nums = min(min_nums, nums[i])
            max_nums = max(max_nums, nums[i+1])
        else:
            max_nums = max_nums(max_nums, nums[i])
            min_nums = min(min_nums, nums[i+1])
    return (min_nums, max_nums)
assert find_min_max([3, 5, 1, 2, 4, 8]) == (1,8)
print(find_min_max([3, 5, 1, 2, 4, 8]))
print('Test pass.')