import collections
def hammingDistance(x, y):
    res = 0
    for num in bin(x ^ y)[2:]:
        if num == '1':
            res += 1
    return res

def hammingDistance1(x, y):
    return (bin(x ^ y).count('1'))


hammingDistance(1,4)