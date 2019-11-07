class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        # init directions
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        # init matrix
        matrix = [[0] * n for i in range(n)]

        # init coordinate and directions index
        x = 0
        y = 0
        index = 0

        # Matrix value from 1 to n^2
        for i in range(1, n ** 2 + 1):

            # Value Matrix
            matrix[x][y] = i

            dx, dy = directions[index % 4]

            # Move (x, y) in one direction of the matrix
            if -1 < x + dx < n and -1 < y + dy < n and matrix[x + dx][y + dy] == 0:
                x = x + dx
                y = y + dy

            # At the edge of matrix, change the direction
            else:
                index += 1
                dx, dy = directions[index % 4]
                x = x + dx
                y = y + dy

        return matrix

if __name__ == '__main__':
    S= Solution()
    Test = S.generateMatrix(3)
    print(Test)