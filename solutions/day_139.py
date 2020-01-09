def closest_nums(nums, k, x):
    diff = [[abs(item - x), item] for item in nums]
    diff.sort(key=lambda x:x[0])
    return [y[1] for y in diff[0:k]]

assert set(closest_nums([1, 3, 7, 8, 9], 3, 5)) == set([7, 3, 8])
print(closest_nums([1, 3, 7, 8, 9], 3, 5))
print('Test pass.')