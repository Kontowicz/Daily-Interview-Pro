from itertools import combinations

def fourSum(nums, target):
    to_return = []

    for item in list(set(combinations(nums, 4))):
        if sum(item) == target:
            if sorted(list(item)) not in to_return:
                to_return.append(sorted(list(item)))

    return to_return


print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
#print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])