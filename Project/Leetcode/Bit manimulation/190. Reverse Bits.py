
def reverseBits(n):
    res = 0
    for i in range(32):
        res = res << 1
        res |= ((n >> i) & 1)
    return res


reverseBits(10)