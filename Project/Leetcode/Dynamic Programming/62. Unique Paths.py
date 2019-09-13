class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
             return 1
        if m== 0 and n == 0:
            return 0
        dp = [[1] * m for i in range(n)]
        print(dp)
        # for i in range(1, n):
        #     dp[i][0] += dp[i - 1][0]
        # for i in range(1, m):
        #     dp[0][i] += dp[0][i - 1]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(dp)
        return dp[-1][-1]
if __name__ == '__main__':
    S = Solution()
    # a = S.uniquePaths(3, 3)
    # a = S.uniquePaths(4, 3)
    # a = S.uniquePaths(3, 2)
    a = S.uniquePaths(0,0)

    print(a)