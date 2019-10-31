class Solution:
    # 97%
    def divide(self, dividend, divisor):
        if dividend == 0: return 0
        Flag = False
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            Flag = True
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if Flag == False:
            return -res
        else:
            # carefully
            if res == 2147483648: return res - 1
            return res

