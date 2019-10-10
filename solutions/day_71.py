def finonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return finonacci_recursive(n-1) + finonacci_recursive(n - 2)

def fibonacci_iterative(n):
    first = 0
    second = 1

    for i in range(1, n):
        tmp = first + second
        first = second
        second = tmp

    return second


n = 9
assert fibonacci_iterative(n) == 34
assert finonacci_recursive(n) == 34

n = 3
assert fibonacci_iterative(n) == 2
assert finonacci_recursive(n) == 2

n = 7
assert fibonacci_iterative(n) == 13
assert finonacci_recursive(n) == 13

print('Test pass.')

