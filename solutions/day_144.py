def to_hex(n):
    number_map = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    to_return = []
    while n > 0:
        to_return.append(number_map[n%16])
        n = n // 16

    return ''.join(to_return[::-1])

assert to_hex(123) == '7B'
print(to_hex(123))
print('Test pass.')