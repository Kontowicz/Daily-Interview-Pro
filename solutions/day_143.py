def find_primes(n):
    bools = [True] * n
    i = 2
    while i < n:
        for j in range(0, n, i):
            if j == i:
                continue
            bools[j] = False
        i += 1

    return [i for i in range(0, len(bools)) if bools[i] == True and i > 1]

assert find_primes(14) == [2, 3, 5, 7, 11, 13]
print(find_primes(14))
print('Test pass.')