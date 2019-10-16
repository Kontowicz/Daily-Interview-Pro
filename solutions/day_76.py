def findSmallest(nums):
    to_return = 1

    for item in nums:
        if item <= to_return:
            to_return += item
        else:
            break

    return to_return

assert findSmallest([1, 2, 3, 8, 9, 10]) == 7
print(findSmallest([1, 2, 3, 8, 9, 10]))
print('Test pass.')