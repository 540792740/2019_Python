class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        firstRowHasZero = not all(matrix[0])
        print(firstRowHasZero)
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        print(matrix)
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        print(matrix)
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n

if __name__ == '__main__':
    S = Solution()
    test = S.setZeroes([[1,1,1,1],[1,0,1,1],[1,1,1,1],[1,1,1,1]])
    print(test)