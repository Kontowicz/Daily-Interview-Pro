def products(nums):
    value = 1
    for item in nums:
        value *= item

    to_return = []

    for item in nums:
        to_return.append(value/item)

    return to_return



assert products([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
print('Test pass.')