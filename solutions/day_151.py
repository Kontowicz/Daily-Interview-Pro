def longest_common_prefix(strs):
    min_size = min([len(x) for x in strs])

    strs = [x[:min_size] for x in strs]

    to_return = 0

    for item in zip(*strs):
        if item == None:
            break
        if item.count(item[0]) == len(item):
            to_return += 1
        else:
            break
    if to_return == 0:
        return ''
    return strs[0][0:to_return]

assert longest_common_prefix(['helloworld', 'hellokitty', 'hell']) == 'hell'
assert longest_common_prefix(['daily', 'interview', 'pro']) == ''

print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
print(longest_common_prefix(['daily', 'interview', 'pro']))
print('Test pass.')