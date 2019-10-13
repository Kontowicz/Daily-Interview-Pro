def compress(chars):
    to_return = []
    prev = chars[0]
    counter = 1

    for char in chars[1::]:
        if prev != char:
            to_return.append(prev)
            if counter > 1:
                to_return.append(str(counter))
            counter = 0

        counter += 1
        prev = char
    to_return.append(prev)
    if counter > 1:
        to_return.append(str(counter))
    return to_return
assert compress(['a', 'a', 'b', 'c', 'c', 'c']) == ['a', '2', 'b', 'c', '3']
print(compress(['a', 'a', 'b', 'c', 'c', 'c']))
print('Test pass.')