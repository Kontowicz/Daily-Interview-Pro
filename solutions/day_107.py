def has_character_map(str1, str2):
    if len(str1) != len(str2):
        return False
    data = {}
    for i in range(0, len(str1)):
        if str1[i] not in data:
            data[str1[i]] = str2[i]
        else:
            if data[str1[i]] != str2[i]:
                return False
    return True

assert has_character_map('abc', 'def') == True
print(has_character_map('abc', 'def'))
assert has_character_map('aac', 'def') == False
print(has_character_map('aac', 'def'))
print('Test pass.')
