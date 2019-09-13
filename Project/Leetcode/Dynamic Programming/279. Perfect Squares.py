class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        # n = 1, len(dp) = 2, so that n + 1
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        print(dp)
        return dp[-1]
# [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 4]
# [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3]

if __name__ == '__main__':
    S = Solution()
    a = S.numSquares(12)
    print(a)