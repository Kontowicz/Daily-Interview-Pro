def shortest_path(file_path):
    path = [x for x in file_path.split('/') if x != '']

    to_return = []

    for item in path:
        if item != '..' and item != '.':
            to_return.append(str(item))
        if item == '..':
            to_return.pop()

    return '/' + '/'.join(to_return)

path = '/Users/Joma/Documents/../Desktop/./../'
assert shortest_path(path) == '/Users/Joma'
print(shortest_path(path))
print('Test pass.')