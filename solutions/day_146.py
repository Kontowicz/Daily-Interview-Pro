def intersection(list1, list2, list3):
    counter = {}
    all = [list1, list2, list3]

    for item in all:
        for num in list(set(item)):
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] = counter[num] + 1

    return [k for k, v in counter.items() if v == 3]

assert set(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5])) == set([4])
print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
print('Test pass.')