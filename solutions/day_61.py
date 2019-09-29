def getBonuses(performance):
    to_return = []

    for i in range(0, len(performance)):
        bonus = 1
        if i - 1 >= 0:
            if performance[i] > performance[i-1]:
                bonus += 1
        if i + 1 < len(performance):
            if performance[i] > performance[i+1]:
                bonus += 1
        to_return.append(bonus)
    return to_return

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
assert getBonuses([1, 2, 3, 2, 3, 5, 1]) == [1, 2, 3, 1, 2, 3, 1]
print('Test pass.')
# [1, 2, 3, 1, 2, 3, 1]