class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None: return 0
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

if __name__ == '__main__':
    S = Solution()
    a = S.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    # a = S.minPathSum([[1,2,5],[3,2,1]])
    print(a)