def remove_dups(nums):
    total_len = len(nums) - 1
    i = 0

    while i < total_len:
        if nums[i] == nums[i+1]:
            del nums[i]
            total_len -= 1
            continue
        i += 1

    return len(nums)



nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
assert remove_dups(nums) == 8
print(remove_dups(nums))
print(nums)
assert nums == [1, 2, 3, 4, 5, 6, 7, 9]
print()
nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
assert remove_dups(nums) == 1
assert nums == [1]
print(nums)
print('Test pass.')