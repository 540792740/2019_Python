'''
DFS, keep rows or columns, set it to 0. when find next '1', result + 1
'''

class Solution(object):
    def numIslands(self, grid):

        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0

        res = 0
        m = len(grid)
        n = len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(grid, i ,j):
            for dx, dy in directions:
                if -1 < dx + i < m and -1 < dy + j < n and grid[i + dx][j + dy] == '1':
                    grid[i + dx][j + dy] = '0'
                    dfs(grid, i + dx, j + dy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
                    print(grid)
        return res

    def numIslands1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        if i - 1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j)
        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.dfs(grid, i + 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.dfs(grid, i, j - 1)
        if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1)



if __name__ == "__main__":
    S = Solution()
    a = S.numIslands([["1","1","1","0"],["1","0","1","0"],["1","0","0","0"],["0","0","0","0"]])
    print(a)
    a = S.numIslands1([["1","1","1","0"],["1","0","1","0"],["1","0","0","0"],["0","0","0","0"]])
    print(a)


'''
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1':
                    output += 1
                    self.dfs(grid,i,j)
        return output

    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        if i - 1 >= 0 and grid[i - 1][j] =='1':
            print(grid)
            self.dfs(grid, i-1, j)

        if i + 1 < len(grid) and grid[i+1][j] == '1':
            print(grid)
            self.dfs(grid, i+1, j)


        if j - 1 >=0 and grid[i][j-1] =='1':
            print(grid)
            self.dfs(grid, i, j-1)
        if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
            print(grid)
            self.dfs(grid, i, j + 1)
            '''