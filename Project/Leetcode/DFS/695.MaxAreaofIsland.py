'''
Time: O(m*n)
Space: O(1)

'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        if row == 0 or col == 0:
             return 0
        res = 0

        def dfs(i, j):
            if 0 <= i < row and 0 <=j < col and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res =  max(res, dfs(i,j))
        return res

if __name__ == '__main__':
    S = Solution()
    a = S.maxAreaOfIsland([[1,1,0,0,0],[1,1,1,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    print(a)

