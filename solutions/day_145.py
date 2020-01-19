def common_characters(strs):
    counter_ch = {}

    for s in strs:
        for character in list(set(s)):
            if character in counter_ch:
                counter_ch[character] += 1
            else:
                counter_ch[character] = 1

    to_return = []
    for key, value in counter_ch.items():
        if value == len(strs):
            to_return.append(key)

    return to_return

assert common_characters(['google', 'facebook', 'youtube']) == ['e', 'o']
print(common_characters(['google', 'facebook', 'youtube']))
print('Test pass.')