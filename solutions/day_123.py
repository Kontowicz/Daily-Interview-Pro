def reverse_words(words):
    begin = 0
    end = len(words) - 1
    while begin != end:
        words[begin], words[end] = words[end], words[begin]

        begin += 1
        end -= 1

    begin = 0
    end_word = 0

    while end_word - 1 < len(words):
        while words[end_word] != ' ':
            end_word += 1
            if end_word == len(words):
                break

        tmp_begin = begin
        tmp_end = (end_word - 1)

        while tmp_begin < tmp_end:
            words[tmp_begin], words[tmp_end] = words[tmp_end], words[tmp_begin]
            tmp_end -= 1
            tmp_begin += 1

        begin = end_word + 1
        end_word += 2

    return words


s = list("can you read this")
print('Orginal: ', end='')
print(''.join(s))

reverse_words(s)
assert ''.join(s) == 'this read you can'
print('Reverse: ', end='')
print(''.join(s))
print('Test pass.')