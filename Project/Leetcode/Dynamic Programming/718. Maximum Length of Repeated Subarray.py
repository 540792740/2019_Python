class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # Init matrix
        matrix = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    matrix[i][j] = matrix[i -1][j - 1] + 1

        return max(max(row) for row in matrix)