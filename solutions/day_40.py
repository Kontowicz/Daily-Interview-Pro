
def first_missing_positive(nums):
    tmp = []
    for item in list(set(nums)):
        if item >= 0:
            tmp.append(item)

    return int((((len(tmp) + 2) / 2)*(len(tmp)+1)) - sum(tmp))

print(first_missing_positive([3, 4, -1, 1]))
