class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        ls = len(matrix)
        print(ls)
        if ls == 0:
             return False
        j = len(matrix[0]) - 1
        if j == -1:
            return False
        for row in matrix:
            while j >= 0 and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False
if __name__ == '__main__':
    S = Solution()
    a = S.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5)
    a = S.searchMatrix([],0)
    a = S.searchMatrix([[5]],0)
    print(a)