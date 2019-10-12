def romanToInt(s):
    values = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    to_return = 0
    prev = 0
    for i in range(0, len(s)):
        value = values[s[i]]
        to_return += value
        if value>prev:
            to_return -= (2*prev)
        prev = value

    return to_return


n = 'MCMX'
assert romanToInt(n) == 1910
print(romanToInt(n))

n = 'IV'
assert romanToInt(n) == 4
print(romanToInt(n))

n = 'XL'
assert romanToInt(n) == 40
print(romanToInt(n))

n = 'XC'
assert romanToInt(n) == 90
print(romanToInt(n))

n = 'CD'
assert romanToInt(n) == 400
print(romanToInt(n))

n = 'CM'
assert romanToInt(n) == 900
print(romanToInt(n))
print('Test pass.')