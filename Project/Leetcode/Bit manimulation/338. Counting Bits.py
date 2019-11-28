def countBits(num):
    res = []
    index = 0
    while len(res) < num + 1:
        # res.append(str(bin(index)).count('1'))
        res.append(bin(index & 0xffffffff).count('1'))
        index += 1
    print(res)
    return res

countBits(5)

# Good way
def countBits1(num):
    dp = [0, 1]
    while len(dp) < num + 1:
        dp.extend(list(map(lambda x: x + 1, dp)))
    return dp[:num + 1]