def one_bits(num):
    cnt = 0
    while num != 0:
        cnt += 1
        num = num&(num-1)
    return cnt

assert one_bits(23) == 4

print(one_bits(23))

print('Test pass.')