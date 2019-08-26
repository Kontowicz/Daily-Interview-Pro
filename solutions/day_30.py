def maximum_product_of_three(lst):
    lst.sort()

    return max(lst[0] * lst[1] * lst[-1], lst[-1] * lst[-2] * lst[-3])
array = [-4, -4, 2, 8]
expected_val = 128
result = maximum_product_of_three(array)

assert result  == 128
print('Result for: {} is {}.'.format(array, result))
print('Test pass.')