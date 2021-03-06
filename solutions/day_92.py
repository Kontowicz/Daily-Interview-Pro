def convertToTitle(n):
    to_return = []

    while n > 0:
        rem = n % 26
        if rem == 0:
            to_return.append('Z')
            n = ((n // 26) - 1)
        else:
            to_return.append(chr(rem - 1 + ord('A')))
            n = n // 26

    return ''.join(to_return[::-1])

input1 = 1
input2 = 456976
input3 = 28
input4 = 26
input5 = 27
input6 = 28
assert convertToTitle(input1) == 'A'
print(convertToTitle(input1))

assert convertToTitle(input2) == 'YYYZ'
print(convertToTitle(input2))

assert convertToTitle(input3) == 'AB'
print(convertToTitle(input3))
print('Test pass.')

assert convertToTitle(input4) == 'Z'
print(convertToTitle(input4))
print('Test pass.')

assert convertToTitle(input5) == 'AA'
print(convertToTitle(input5))
print('Test pass.')

assert convertToTitle(input6) == 'AB'
print(convertToTitle(input6))
print('Test pass.')