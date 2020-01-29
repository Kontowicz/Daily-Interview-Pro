def reverse_integer(num):
    rev = 1
    if num < 0:
        rev = -1
        num *= -1

    reverse = 0
    pow = 1
    while num > 0:
        reverse = (reverse*10) + ((num%10)*pow)
        num = num // 10

    return reverse * rev

assert reverse_integer(135) == 531
assert reverse_integer(-321) == -123

print(reverse_integer(135))
print(reverse_integer(-321))
print('Test pass.')