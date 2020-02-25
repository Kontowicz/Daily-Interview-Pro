def shortest_dist(string, character):
    character_all_pos = [i for i, c in enumerate(string) if c == character]
    to_return = []
    for i, c in enumerate(string):
        if c == character:
            to_return.append(0)
        else:
            tmp = []
            for num in character_all_pos:
                tmp.append(abs(num - i))
            to_return.append(min(tmp))

    return to_return

assert shortest_dist('helloworld', 'l') == [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
print(shortest_dist('helloworld', 'l'))
print('Test pass.')