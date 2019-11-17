
KAPREKAR_CONSTANT = 6174
import copy

def desc(n):
    digits = []
    while (n > 0):
        dig = n % 10
        if dig != 0:
            digits.append(dig)
        n = n // 10

    digits.sort(reverse=True)

    if len(digits) < 4:
        padding = 4 - len(digits)
        digits = digits + [0] * padding

    to_return = 0
    multiply = 1
    for item in range(0, len(digits) - 1):
        multiply *= 10

    for item in digits:
        to_return += item * multiply
        multiply = multiply // 10
    return to_return

def asc(n):
    digits = []
    while (n > 0):
        dig = n % 10
        if dig != 0:
            digits.append(dig)
        n = n // 10
    digits.sort()

    to_return = 0
    multiply = 1
    for item in range(0, len(digits) - 1):
        multiply *= 10

    for item in digits:
        to_return += item * multiply
        multiply = multiply // 10

    return to_return


def num_kaprekar_iterations(n):
    cnt = 0

    while n != KAPREKAR_CONSTANT:
        cnt += 1
        descending = desc(n)
        ascending = asc(n)
        n = descending - ascending

    return cnt

assert num_kaprekar_iterations(123) == 3
print(num_kaprekar_iterations(123))
print('Test pass.')