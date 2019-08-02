def sortNums(nums):
    buckets = [0, 0, 0]

    for item in nums:
        buckets[item - 1] += 1

    to_return = [1] * buckets[0]
    to_return += [2] * buckets[1]
    to_return += [3] * buckets[2]

    return to_return

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
assert sortNums([3, 3, 2, 1, 3, 2, 1]) == [1, 1, 2, 2, 3, 3, 3]
print('Test pass.')