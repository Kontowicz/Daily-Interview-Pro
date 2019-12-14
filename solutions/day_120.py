def rotate_list(nums, k):
    for i in range(0, k+1):

        tmp = nums[len(nums) - 1]
        for j in range(len(nums) - 2, -1, -1):
            nums[j + 1] = nums[j]

        nums[0] = tmp

    return nums

a = [1, 2, 3, 4, 5]
rotate_list(a, 2)
print(a)
# [3, 4, 5, 1, 2]