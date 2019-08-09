def countWaysUtil(n, m):
    res = [0 for x in range(n)]  # Creates list res witth all elements 0
    res[0], res[1] = 1, 1

    for i in range(2, n):
        j = 1
        while j <= m and j <= i:
            res[i] = res[i] + res[i - j]
            j = j + 1
    return res[n - 1]


def staircase(n):
    return countWaysUtil(n + 1, 2)

assert staircase(4) == 5

assert  staircase(5) == 8
# 8

print('Test pass.')