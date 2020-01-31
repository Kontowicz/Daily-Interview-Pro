def sum_binary(bin1, bin2):
    max_len = max(len(bin1), len(bin2))

    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    to_return = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if bin1[i] == '1' else 0
        r += 1 if bin2[i] == '1' else 0
        to_return = ('1' if r % 2 == 1 else '0') + to_return
        carry = 0 if r < 2 else 1
    if carry != 0:
        to_return = '1' + to_return

    return to_return

assert sum_binary("11101", "1011") == '101000'
print(sum_binary("11101", "1011"))
print('Test pass.')