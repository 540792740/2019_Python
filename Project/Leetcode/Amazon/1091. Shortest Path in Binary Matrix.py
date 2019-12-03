import collections

# Since i use BFS, the worst case is to traverse all matrix, so the complexity is N times N
# O(N ^ 2)
def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
    queue = collections.deque([(0, 0, 1)])
    while queue:
        x, y, steps = queue.popleft()
        if x == n - 1 and y == n - 1: return steps
        for dx, dy in direction:
            dx, dy = x + dx, y + dy
            if -1 < dx < n and -1 < dy < n and grid[dx][dy] == 0:
                grid[dx][dy] = 1
                queue.append((dx, dy, steps + 1))
    return -1

shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])