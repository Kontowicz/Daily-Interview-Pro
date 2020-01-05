def base_2(n):
    to_return = []
    while n > 0:
        to_return.append(str(n%2))
        n = n // 2

    return ''.join(to_return[::-1])

assert base_2(123) == '1111011'
print(base_2(123))
print('Test pass.')