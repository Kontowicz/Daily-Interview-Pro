from itertools import combinations

def sum_combinations(nums, target):
    nums = [x for x in nums if x <= target]
    to_return = []

    for i in range(1, len(nums)):
        for item in list(set(combinations(nums, i))):
            if sum(item) == target:
                if sorted(list(item)) not in to_return:
                    to_return.append(sorted(list(item)))

    return to_return

print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]