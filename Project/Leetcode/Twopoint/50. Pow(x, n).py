class Solution:
    # recursive, 93%
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 != 0:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n / 2)

        # bit operation 99.83%
        def myPow1(self, x, n):
            if n < 0:
                x = 1 / x
                n = -n
            pow = 1
            while n:
                if n & 1:
                    pow * x
                n >> 1
                x = x * x