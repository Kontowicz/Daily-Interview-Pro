def count_invalid_parenthesis(string):
    dict = {}
    for item in string:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] = dict[item] + 1

    return abs(dict['('] - dict[')'])

assert count_invalid_parenthesis("()())()") == 1