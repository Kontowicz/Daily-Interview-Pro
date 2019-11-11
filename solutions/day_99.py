def sort_partially_sorted(nums, k):
    for i in range(0, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key

    return nums
assert sort_partially_sorted([3, 2, 6, 5, 4], 2) == [2, 3, 4, 5, 6]
print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
print('Test pass.')