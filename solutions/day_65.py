def decodeString(s):
    if '[' not in s:
        return s
    start = 0
    end = 0
    for i in range(0, len(s)):
        if '[' == s[i]:
            start = i
        if s[i] == ']':
            end = i
            break

    new_string = s[0:start-1] + (int(s[start - 1]) * s[start+1:end]) + s[end+1::]
    return decodeString(new_string)

print(decodeString('2[a2[b]c]'))
assert decodeString('2[a2[b]c]') == 'abbcabbc'

print(decodeString('3[abc]'))
assert decodeString('3[abc]') == 'abcabcabc'

print('Test pass.')