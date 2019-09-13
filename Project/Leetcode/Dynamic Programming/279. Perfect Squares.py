class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        while n % 4 == 0:
            n = n // 4
        print(n)
        # n = 1, len(dp) = 2, so that n + 1
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[-1]

    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        while n % 4 == 0:
            n = n // 4
        if n % 8 == 7:
            return 4
        if int(math.sqrt(n)) ** 2 == n:
            return 1
        i = 1
        while i * i <= n:
            j = math.sqrt(n - i * i)
            if int(j) == j:
                return 2
            i += 1
        return 3

    
if __name__ == '__main__':
    S = Solution()
    a = S.numSquares1(13)
    print(a)