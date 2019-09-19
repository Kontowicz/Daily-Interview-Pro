from collections import defaultdict

def groupAnagramWords(strs):
    dict = {}

    for word in strs:
        if ''.join(sorted(''.join(set(word)))) not in dict:
            dict[''.join(sorted(''.join(set(word))))] = [word]
        else:
            dict[''.join(sorted(''.join(set(word))))] = dict[''.join(sorted(''.join(set(word))))] + [word]
    to_return = []
    for key, value in dict.items():
        to_return.append(value)

    return to_return
print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]