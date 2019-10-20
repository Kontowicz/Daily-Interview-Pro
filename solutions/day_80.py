def find_continuous_k(list, k):
    start = 0
    end = 1

    while end < len(list):
        s = sum(list[start:end])
        if s == k:
            return list[start:end]
        if s > k:
            start += 1
        if s < k:
            end += 1

assert find_continuous_k([1, 3, 2, 5, 7, 2], 14) == [2, 5, 7]
print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
print('Test pass.')