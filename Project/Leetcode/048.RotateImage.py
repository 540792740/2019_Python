class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ls = len(matrix)
        dic = {}
        for i in range(0, ls):
            for j in range(0, ls):
                if (i,j) not in dic:
                    dic[(j,ls - 1 - i)] = matrix[i][j]
                    matrix[i][j] = matrix[j][ls - 1 - i]
                else:
                    dic[(j, ls - 1 - i)] = matrix[i][j]
                    matrix[i][j] = dic[(i,j)]
        print(dic)
        return matrix



if __name__ == '__main__':
    S = Solution()
    a = S.rotate([[1,2,3],[4,5,6],[7,8,9]])
    print(a)