def min_window_to_sort(nums):
    start = 0
    end = 0

    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            start = i
            break

    for i in range(len(nums)-1, 0, -1):
        if nums[i] < nums[i-1]:
            end = i + 1
            break

    return (start, end)

assert min_window_to_sort([2, 4, 7, 5, 6, 8, 9]) == (2, 4)
print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
print('Test pass.')