

# Bit manipulation
def singleNumber(nums):
    one = 0
    two = 0
    three = 0
    for i in range(0, len(nums)):
        two |= one & nums[i]    # 当新来的为0时，two = two | 0，two不变，当新来的为1时，（当one此时为0，则two = two|0，two不变；当one此时为1时，则two = two | 1，two变为1
        one ^= nums[i]          # 新来的为0，one不变，新来为1时，one是0、1交替改变
        three = one & two       # 当one和two为1是，three为1（此时代表要把one和two清零了）
        one &= ~three           # 把one清0
        two &= ~three           # 把two清0
        print(bin(one)[2:], bin(two)[2:], bin(three)[2:],' ', one, two, three)
    return one
singleNumber([7,3,1,7,3,7,3])

# Easy way
def singleNumber1(self, nums):
    return (sum(set(nums)) * 3 - sum(nums)) // 2

# Using dic
def singleNumber2(self, nums):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
        if dic[i] == 3:
            del dic[i]
    return list(dic)[0]

print(5 & ~0)