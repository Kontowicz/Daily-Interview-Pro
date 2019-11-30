def is_unique(prefix, words):
    cnt = 0
    for item in words:
        if prefix == item[0:len(prefix)]:
            cnt += 1

    return cnt == 1

def shortest_unique_prefix(words):
    to_return = []

    for i in range(0, len(words)):
        for j in range(0, len(words[i])):
            if is_unique(words[i][0:j], words):
                to_return.append(words[i][0:j])
                break

    return to_return

assert shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']) == ['jom', 'joh', 'ja', 't']
print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
print('Test pass.')
