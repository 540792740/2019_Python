class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in range(n)]  # Define Matrix of result
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # Direction in spiral order

        x, y = 0, 0  # Coordinate of matrix
        d = 0  # Direction Index

        for i in range(1, n * n + 1):
            matrix[x][y] = i  # Assign value of Matrix[x][y]

            # Steps
            dx, dy = directions[d % 4]
            if -1 < x + dx < n and -1 < y + dy < n and matrix[x + dx][y + dy] == 0:
                x, y = x + dx, y + dy

            # Change the direction at the edge of reach level of spiral
            else:
                d += 1
                dx, dy = directions[d % 4]
                x, y = x + dx, y + dy

        return matrix


if __name__ == '__main__':
    S= Solution()
    Test = S.generateMatrix(3)
    print(Test)