'''
70%
'''

class Solution(object):
    def addStrings(self, num1, num2):
        res = ''
        carry = 0
        a = len(num1) - 1
        b = len(num2) - 1
        while a >= 0 or b >= 0 or carry == 1:
            carry += int(num1[a]) if a >= 0 else 0
            carry += int(num2[b]) if b >= 0 else 0
            res = str(carry % 10) + res
            print(res)
            a = a - 1
            b = b - 1
            carry = carry // 10
        return res

    # 90%
    def addStrings1(self, num1, num2):
        return str(int(str(int(num1)+int(num2))))



if __name__ == '__main__':
    S = Solution()
    a = S.addStrings("230", "32")
    print(a)