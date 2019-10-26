def findDisappearedNumbers(nums):
    data = [False] * max(nums)

    for item in nums:
        data[item - 1] = True

    to_return = []

    for i in range(0, len(data)):
        if not data[i]:
            to_return.append(i+1)
    return to_return

nums = [4, 6, 2, 6, 7, 2, 1]
assert findDisappearedNumbers(nums) == [3, 5]
print(findDisappearedNumbers(nums))
print('Test pass.')