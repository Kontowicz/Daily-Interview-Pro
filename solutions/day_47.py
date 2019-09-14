def get_first_diff(first_word, second_word):
    min_len = min(len(first_word), len(second_word))

    for i in range(0, min_len):
        if first_word[i] != second_word[i]:
            return [first_word[i], second_word[i]]
    return False

def isSorted(words, order):
    first = 0
    second = 1

    for i in range(1, len(words)):
        first_word = str(words[first])
        second_word = str(words[second])

        first += 1
        second += 1

        if first_word == second_word:
            continue

        a = get_first_diff(first_word, second_word)
        if a == False:
            continue
        a_pos = order.index(a[0])
        b_pos = order.index(a[1])

        if b_pos - a_pos < 0:
            return False

    return True


assert isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba") == False

assert isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba") == True

print('Test pass.')