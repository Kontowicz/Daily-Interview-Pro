def moveZeros(nums):
    counter = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[counter] = nums[i]
            counter += 1

    while counter < len(nums):
        nums[counter] = 0
        counter += 1



nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
moveZeros(nums)
print(nums)
assert nums == [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]