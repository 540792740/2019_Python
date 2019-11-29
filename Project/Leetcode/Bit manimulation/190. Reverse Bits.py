
def reverseBits(n):
    res = 0
    for i in range(32):
        res = res << 1
        res |= ((n >> i) & 1)
    print(res)
    return res


reverseBits(10)