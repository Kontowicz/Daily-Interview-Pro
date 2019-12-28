def sqrt(x):
    i = 1
    def binary(x, lower, upper):

        mid = (lower + upper) / 2
        result = mid * mid
        if result == x or (abs(result - x) < 0.0001):
            return round(mid, 3)
        elif result < x:
            return binary(x, mid, upper)
        else:
            return binary(x, lower, mid)

    done = False
    while not done:
        if i * i == x:
            return i
        elif i * i > x:
            return binary(x, i - 1, i)
        i += 1

assert sqrt(5) == 2.236
print(sqrt(5))
print('Test pass.')