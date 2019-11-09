def fix_brackets(s):
    data = {}

    for x in s:
        if x in data:
            data[x] = data[x] + 1
        else:
            data[x] = 1

    return abs(data['('] - data[')'])

assert fix_brackets('(()()') == 1
print(fix_brackets('(()()'))
print('Test pass.')