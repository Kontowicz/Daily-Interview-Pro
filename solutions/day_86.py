def plusOne(digits):

    digits[-1] += 1
    c = digits[-1]/10
    digits[-1] = digits[-1] % 10

    for i in range(len(digits) - 2, -1, -1):
        if c == 1:
            digits[i] += 1
            c = digits[i] / 10
            digits[i] = digits[i] % 10

    if c == 1:
        digits.insert(0, 1)

    return digits


num = [2, 9, 9]
print(plusOne(num))
# [3, 0, 0]
