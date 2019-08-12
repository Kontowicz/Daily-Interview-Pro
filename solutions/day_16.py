def min_distance(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if s1[m-1] == s2[n-1]:
        return min_distance(s1, s2, m - 1, n - 1)

    return 1 + min(min_distance(s1, s2, m, n - 1),
                   min_distance(s1, s2, m - 1, n),
                   min_distance(s1, s2, m - 1, n - 1))

def min_distance_fast(s1, s2):
    result = [[ 0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                result[i][j] = j
            if j == 0:
                result[i][j] = i

            if s1[i-1] == s2[j-1]:
                result[i][j] = result[i-1][j-1]
            else:
                result[i][j] = 1 + min(result[i][j-1],
                                   result[i-1][j-1],
                                   result[i-1][j])
    return result[-1][-1]

def distance(s1, s2):
    return min_distance_fast(s1, s2)
    #return min_distance(s1, s2, len(s1), len(s2))

string_1 = 'biting'
string_2 = 'sitting'
expected = 2

result = distance(string_1, string_2)

print('Distance between w1: {} and w2: {} is {}. Expected distance is {}.'.format(string_1, string_2, result, expected))
assert distance(string_1, string_2) == 2
print('Test pass.')