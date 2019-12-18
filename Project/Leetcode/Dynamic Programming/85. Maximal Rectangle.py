class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        self.res = 0
        for i in range(m):
            for j in range(n):
                dp[j] += 1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for idx, val in enumerate(dp):
                while val < dp[stack[-1]]:
                    h = dp[stack.pop()]
                    self.res = max(self.res, h * (idx - stack[-1]  - 1))
                stack.append(idx)
                print(dp, self.res, stack)
            print()
        return self.res
if __name__ == '__main__':
    S = Solution()
    test = S.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    print(test)