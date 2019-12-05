'''
DFS
'''


class Solution(object):
    def hasPath(self, maze, start, destination):
        m = len(maze)
        if not m: return False
        n = len(maze[0])
        if not maze[0]: return False
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
        visited = set()
        def helper(maze, position):
            if position == destination: return True
            if (position[0],position[1]) in visited: return False
            visited.add((position[0],position[1]))
            for dx, dy in direction:
                x, y = position[0], position[1]
                while -1 < dx + x < m and -1 < dy + y < n and maze[dx + x][dy + y] == 0:
                    x += dx
                    y += dy
                if helper(maze, [x, y]): return True
            return False
        return helper(maze, start)
if __name__ == '__main__':
    S= Solution()
    test = S.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
    [0,4],[3,2])
    print(test, 'False')

    test = S.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
    [0,4], [4,4])
    print(test, 'True')

    test = S.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
    [0,4], [1,2])
    print(test, 'True')