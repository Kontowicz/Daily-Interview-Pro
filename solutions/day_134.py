def swap_bits(num):
    e = num & 0xAAAAAAAA
    o = num & 0x55555555
    e >>= 1
    o <<= 1
    return e | o

assert f"0b{swap_bits(0b10101010101010101010101010101010):032b}" == '0b01010101010101010101010101010101'
print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
print('Test pass.')