
# first one is fastest
def hammingWeight(n):
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count

# Easy way
def hammingWeight1(n):
    res = 0
    n = bin(n)[2:]
    for i in n:
        if i == '1': res += 1
    return res
hammingWeight(10001)

# Str function count
def hammingWeight2(n):
    return str(bin(n)).count('1')
