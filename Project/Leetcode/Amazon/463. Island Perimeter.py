class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        self.res = 0
        directions = ((0, 1), (1, 0))

        def dfs(x, y, grid):
            for dx, dy in directions:
                if -1 < x + dx < m and -1 < y + dy < n and grid[x + dx][y + dy] == 1:
                    self.res -= 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.res += 4
                    dfs(i, j, grid)
        return self.res

    # 99%
    def islandPerimeter1(self, grid):
        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]:
                    res += 4
                    if 0 < row < m and grid[row - 1][column]:
                        res -= 2
                    if 0 < column < n and grid[row][column - 1]:
                        res -= 2
        return res

S = Solution()
test = S.islandPerimeter([[1,1],[1,1]])
print(test)