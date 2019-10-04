class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i,j):
            if 0 <= i < row and 0 <= j < col and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return 0

        row, col = len(grid), len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))

        return ans
if __name__ == '__main__':
    S = Solution()
    a = S.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    print(a)

