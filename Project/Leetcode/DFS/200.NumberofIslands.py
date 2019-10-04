'''
DFS, keep rows or columns, set it to 0. when find next '1', result + 1
'''

class Solution(object):
    def numIslands(self, grid):
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