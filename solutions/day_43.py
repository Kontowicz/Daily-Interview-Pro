def is_valid(string, k):
    return len(list(set(string))) <= k

def longest_substring_with_k_distinct_characters(s, k):
    start = 0
    end = 1
    max_len = 0
    while end < len(s):
        if is_valid(s[start:end+1], k):
            if max_len < (end + 1 - start):
                max_len = (end + 1 - start)
            end += 1
        else:
            start += 1
    return max_len

assert longest_substring_with_k_distinct_characters('aabcdefff', 3) == 5
assert longest_substring_with_k_distinct_characters('aabacbebebe', 3) == 7
print('Test pass.')