def find_num(nums, target):

    if nums[0] > target or nums[-1] < target:
        return (-1, -1)

    lower_boud = -1
    upper_bound = -1

    for i in range(0, len(nums)):
        if nums[i] == target:
            lower_boud = i
            upper_bound = i
        while nums[upper_bound] == target:
            upper_bound += 1
        upper_bound -= 1
        break

    return (lower_boud, upper_bound)

assert find_num([1, 1, 3, 5, 7], 1) == (0, 1)
assert find_num([1, 2, 3, 4], 5) == (-1, -1)

print(find_num([1, 1, 3, 5, 7], 1))
print(find_num([1, 2, 3, 4], 5))
print('Test pass.')