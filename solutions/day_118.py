
lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def makeWords(phone):
    to_return = []
    aval_char = []

    for num in phone:
        aval_char += lettersMaps[int(num)]

    for word in validWords:
        if set(list(word)).issubset(set(aval_char)):
            to_return.append(word)
    return to_return


assert makeWords('364') == ['dog', 'fog']
print(makeWords('364'))
print('Test pass.')