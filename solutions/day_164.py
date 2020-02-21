def maxNonAdjacentSum(nums):
    small = 0
    big = 0

    for item in nums:
        new_big = max(small, big)

        small = big + item
        big = new_big
    return max(small, big)
  
assert maxNonAdjacentSum([3, 4, 1, 1]) == 5
assert maxNonAdjacentSum([2, 1, 2, 7, 3]) == 9

print(maxNonAdjacentSum([3, 4, 1, 1]))
print(maxNonAdjacentSum([2, 1, 2, 7, 3]))

print('Test pass.')