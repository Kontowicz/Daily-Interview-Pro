def findTime(arr, cooldown):
    to_return = []

    i = 0
    while i < len(arr):
        tmp = 0
        while tmp < cooldown and i < len(arr):
            tmp += arr[i]
            i += 1
            to_return.append(1)
        to_return.append(1)

    return sum(to_return)
assert findTime([1, 1, 2, 1], 2) == 7
print(findTime([1, 1, 2, 1], 2))
print('Test pass.')