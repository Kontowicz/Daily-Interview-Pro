def first_recurring_char(s):
    data = {}
    for character in s:
        if character in data:
            return character
        else:
            data[character] = 1

    return None

assert first_recurring_char('qwertty') == 't'
assert first_recurring_char('qwerty') == None

print(first_recurring_char('qwertty'))
print(first_recurring_char('qwerty'))

print('Test pass.')