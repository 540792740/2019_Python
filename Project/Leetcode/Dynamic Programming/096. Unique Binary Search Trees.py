'''
1. recursion, Time Limit Exceed
2. Dynamic Programming

0 --> 1
1 --> 1
2 --> 2
3 --> 5  = 1*2 + 1*1 + 2*1
4 --> 14 = 1*5 + 1*2 + 2*1 + 5*1
'''

class Solution(object):
    # Time Limit Exceed
    def numTrees_1(self, n):
        if n <= 1:
             return 1
        sum = 0
        for i in range(0, n):
            sum += self.numTrees(i) * self.numTrees(n - i - 1)
        return sum

    #DP
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        print(dp)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]

if __name__ == '__main__':
    S = Solution()
    # a = S.numTrees(5)
    a = S.numTrees(3)
    print(a)