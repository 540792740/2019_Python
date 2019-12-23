'''
Question:
1.  input, dividend and divisor? negative number or just positive number.
2.  return remainder or result
3.  The range of the result? -2^31 - 2^31 -1?

Solution:
1.  Bit manipulation is good way to solve.
2.  Initial return res, use while loop  dividend >= divisor, keep using
    Subtraction to find the result.
3.  Complexity O(log(n)指数增长除数)
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Initial return res
        self.res = 0
        if dividend == 0: return self.res

        def divide_func(dividend, divisor):
            # when >= ：res += number
            while dividend >= divisor:
                # Initial index, how many bits shifted by divisor(temp)
                temp = divisor
                index = 1
                # Save time way
                while dividend >= temp:
                    dividend -= temp
                    self.res += index
                    temp <<= 1
                    index <<= 1
            return self.res


        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            dividend, divisor = abs(dividend), abs(divisor)
            res = divide_func(dividend, divisor)
            if self.res == 2147483648: return self.res - 1
            return self.res

        if dividend < 0 or divisor < 0:
            dividend, divisor = abs(dividend), abs(divisor)
            return-divide_func(dividend, divisor)