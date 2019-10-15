from itertools import permutations

def largestNum(nums):
    to_return = []
    for item in list(permutations(nums)):
        to_return.append(int("".join([str(x) for x in list(item)])))

    return max(to_return)

assert largestNum([17, 7, 2, 45, 72]) == 77245217
print(largestNum([17, 7, 2, 45, 72]))
print('Test pass.')