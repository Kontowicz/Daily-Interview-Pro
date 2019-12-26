def pow(x, n):
    if n == 0:
        return 1
    power = pow(x, n//2)
    if n % 2 == 1:
        return x * power * power
    return power * power



assert pow(5, 3) == 125
print(pow(5, 3))
print('Test pass.')