def is_shifted(a, b):
    if len(a) != len(b):
        return False

    if b in (a+a):
        return True
    return False

assert is_shifted('abcde', 'cdeab') == True
print(is_shifted('abcde', 'cdeab'))
print('Test pass.')