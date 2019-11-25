class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
            print(bin(a),bin(mask))
        if b > mask:
            return a & mask
        else:
            return a

S = Solution()
# test = S.getSum(-3, 1)
# test = S.getSum(2, -2)
test = S.getSum(-14, 16)
print(test)
'''
-3 --> 1011 = bin: 1101
1101 ^ 0001: 1100, so -100
'''