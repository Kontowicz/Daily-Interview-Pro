def find_anagrams(s, t):
    to_return = []
    t = sorted(t)
    for i in range(0, len(s) - len(t) + 1):
        if sorted(s[i:i+len(t)]) == t:
            to_return.append(i)

    return to_return

assert find_anagrams('acdbacdacb', 'abc') == [3, 7]
print(find_anagrams('acdbacdacb', 'abc'))
print('Test pass.')