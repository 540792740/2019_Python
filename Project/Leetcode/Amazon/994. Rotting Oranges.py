class Solution:

    #   98%
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_ora = []  # Save rotten orange into a list
        fresh_ora = 0  # Save quatity of fresh oranges
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_ora.append((i, j))
                elif grid[i][j] == 1:
                    fresh_ora += 1

        count = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while rotten_ora:
            rotten_new = []
            for x, y in rotten_ora:
                for dx, dy in directions:
                    dx, dy = x + dx, y + dy
                    if -1 < dx < m and -1 < dy < n and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        fresh_ora -= 1
                        rotten_new.append((dx, dy))
            rotten_ora = rotten_new
            count += 1
        print(count)
        if fresh_ora == 0:
            return count
        else:
            return -1

if __name__ == '__main__'