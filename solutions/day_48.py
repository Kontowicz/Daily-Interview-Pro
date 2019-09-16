def threeSum(nums):
    set = []

    result = []

    for i, item in enumerate(nums):
        for j, value in enumerate(nums):
            if i <= j:
                continue
            if -(item + value) in set:
                result.append([-(item + value), item, value])
            else:
                set.append(value)
    return result

nums = [1, -2, 1, 0, 5]
print(threeSum(nums))
# [[-2, 1, 1]]