def longest_run(n):
    to_return = 0

    while n:
        n = (n & (n<<1))
        to_return += 1

    return to_return

assert longest_run(242) == 4
print(longest_run(242))
print('Test pass.')