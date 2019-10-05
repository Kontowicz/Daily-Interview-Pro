def chainedWords(words):
    start_letters = {}
    last_letters = {}

    for word in words:
        start = word[0]
        last = word[-1]

        if start not in start_letters:
            start_letters[start] = 1
        else:
            start_letters[start] = start_letters[start] + 1

        if last not in last_letters:
            last_letters[last] = 1
        else:
            last_letters[last] = last_letters[last] + 1

    if last_letters == start_letters:
        return True
    return False

print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
assert chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']) == True

print(chainedWords(['hehehe', 'ababab']))
assert chainedWords(['hehehe', 'ababab']) == False

print('Test pass.')