def square_sum(n):
    if n <= 3:
        return n

    to_return = n

    for i in range(1, n + 1):
        tmp = i * i
        if tmp > n:
            break
        else:
            to_return = min(to_return, 1 + square_sum(n - tmp))

    return to_return

assert square_sum(13) == 2
print(square_sum(13))
print('Test pass.')