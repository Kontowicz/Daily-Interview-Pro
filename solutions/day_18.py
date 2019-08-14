def findSequence(seq):
    his = {}

    for item in seq:
        if item not in his:
            his[item] = 0
        else:
            his[item] = his[item] + 1

    num = []
    for key, value in his.items():
        num.append(value)

    num.sort(reverse=True)

    begin = 0
    end = 1

    while True:
        if num[begin] == num[end] or\
            num[begin] + 1 == num[end] or\
            num[begin] == num[end] + 1:
            return num[begin] + num[end]

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
assert findSequence([1, 3, 5, 3, 1, 3, 1, 5]) == 4
print('Test pass.')