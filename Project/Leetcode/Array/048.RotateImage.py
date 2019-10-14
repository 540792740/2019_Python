'''
0. matrix[i][j] in dic: dic[(j,ls - 1 - i)] =  matrix[i][j]
1. if exist: matrix[i][j] = dic[(i,j)]
2. if not matrix[i][j] = matrix[][]
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

'''

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
                    matrix[i][j] = matrix[ls - 1 - j][i]
                else:
                    dic[(j, ls - 1 - i)] = matrix[i][j]
                    matrix[i][j] = dic[(i,j)]
        print(dic)
        return matrix



if __name__ == '__main__':
    S = Solution()
    a = S.rotate([[1,2,3],[4,5,6],[7,8,9]])
    print(a)