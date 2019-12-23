import re

def convert_to_int(s):
    if not re.match('^[-+]?[1-9]\d*$', s):
        return

    to_return = 0
    negative = 1

    if s[0] == '-':
        negative = -1
        s = s[1::]

    for i in range(0, len(s)):
        to_return += ((ord(s[i])-ord('0')) * (10**(len(s) - i - 1)))

    return to_return * negative
assert (convert_to_int('-105') + 1) == -104
print(convert_to_int('-105') + 1)
print('Test pass.')