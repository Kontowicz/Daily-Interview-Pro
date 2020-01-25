import itertools

def closest_3sum(nums, target):
    to_return = []
    for item in itertools.combinations(nums, 3):
        to_return.append([item, abs(sum(item) - target)])
    to_return.sort(key=lambda x:x[1])
    return to_return[0][0]

assert set(closest_3sum([2, 1, -5, 4], -1)) == set([-5, 1, 2])
print(closest_3sum([2, 1, -5, 4], -1))
print('Test pass.')