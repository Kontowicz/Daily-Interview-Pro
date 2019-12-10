import sys

def make_change(coins, n):
    if n == 0:
        return 0

    to_return = 0

    while n > 0:
        if not n - max(coins) < 0:
            n -= max(coins)
            to_return += 1
        else:
            coins.remove(max(coins))

    return to_return

assert make_change([1, 5, 10, 25], 36) == 3
print(make_change([1, 5, 10, 25], 36))
print('Test pass.')