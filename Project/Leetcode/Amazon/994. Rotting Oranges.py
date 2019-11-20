class Solution:
    #   98%
    def orangesRotting(self, grid):
        # DFS
        # Init a list to save all index of rotten oranges
        # Count how many fresh orange, inorder to get result
        rotten_org = []
        fresh_org = 0
        m, n = len(grid), len(grid[0])

        # Save oranges into list and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_org.append((i, j))
                elif grid[i][j] == 1:
                    fresh_org += 1
                else:
                    continue

        # Init directions, res_count
        res_count = 0
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while rotten_org:
            rotten_new = []
            for x, y in rotten_org:
                for dx, dy in directions:
                    if -1 < x + dx < m and -1 < y + dy < n and grid[x + dx][y + dy] == 1:
                        rotten_new.append((x + dx, y + dy))
                        grid[x + dx][y + dy] = 2
                        fresh_org -= 1

            rotten_org = rotten_new
            if rotten_org:  res_count += 1

        if fresh_org == 0: return res_count
        else: return -1

# if __name__ == '__main__'