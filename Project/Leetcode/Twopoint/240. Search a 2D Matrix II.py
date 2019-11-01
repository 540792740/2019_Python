class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix) - 1
        if m < 0: return False
        n = len(matrix[0]) - 1
        if n < 0: return False

        for i in range(m + 1):
            while matrix[i][n] >= target and n >= 0:
                print(matrix[i][n])
                if matrix[i][n] == target:
                    return True

                elif matrix[i][n] > target:
                    n -= 1

                else:
                    break
        return False