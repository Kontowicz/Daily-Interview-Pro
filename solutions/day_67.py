def jumpToEnd(nums):

    start = 0
    cnt = 0
    while start < len(nums) - 1:
        start += max(nums[start+1:nums[start]])
        cnt += 1

    return cnt

print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
assert jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]) == 2
print('Test pass.')