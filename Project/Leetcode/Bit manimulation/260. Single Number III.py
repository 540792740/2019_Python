'''
Solution: https://blog.csdn.net/fuxuemingzhu/article/details/79434100
'''
# Not understand
def singleNumber(self, nums):
    xor = 0
    num1, num2 = 0, 0
    for num in nums:
        xor ^= num
    mask = 1
    while xor & mask == 0:
        mask = mask << 1
    for num in nums:
        if num & mask == 0:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]

# 99% in dic O(n)
def singleNumber(self, nums):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
        if dic[i] == 2:
            del dic[i]
    return list(dic)