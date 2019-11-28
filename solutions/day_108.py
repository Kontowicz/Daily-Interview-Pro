def flatten_dictionary(d, parent_key = ''):
    items = []
    for key, value in d.items():
        new_key = ''
        if key == '':
            new_key = key
        else:
            if parent_key != '':
                new_key = parent_key + f'.{key}'
            else:
                new_key = f'{key}'

        if isinstance(value, dict):
            items.extend(flatten_dictionary(value, new_key).items())
        else:
            items.append((new_key, value))

    return dict(items)

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}

print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}