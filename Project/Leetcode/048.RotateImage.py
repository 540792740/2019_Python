class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ls = len(matrix)
        dic = matrix.copy()
        for i in range(0, ls):
            for j in range(0, ls):
                dic[j][ls - 1 - i] = matrix[i][j]
        return dic



if __name__ == '__main__':
    S = Solution()
    a = S.rotate([[1,2,3],[4,5,6],[7,8,9]])
    print(a)