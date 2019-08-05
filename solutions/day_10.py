def check(lst):
    counter = 0

    for i in range(0, len(lst) - 2):
        if counter > 1:
            return False
        if lst[i] > lst[i + 1]:
            counter += 1

    return counter <= 1

assert check([13, 4, 7]) == True
assert check([5,1,3,2,5]) == False
print('Test pass.')
