class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ls = len(matrix)
        res = []
        if ls < 1:
            return
        def dfs(matrix):
            while[] in matrix:
                matrix.remove([])
            if matrix:
                while (matrix[0] != []):
                    res.append(matrix[0].pop(0))
                matrix.pop(0)
                i = 0
                while i < len(matrix):
                    res.append((matrix[i].pop(-1)))
                    i += 1
                i = i - 1

                print(matrix,i)
                while i >= 0 and matrix[i] != []:
                    res.append(matrix[i].pop(-1))

                ls = len(matrix)
                # if matrix != []:
                #     matrix.pop(ls - 1)
                if matrix == []:
                    return

                while ls > 0 and matrix[ls - 2] != []:
                    res.append(matrix[ls - 2].pop(0))
                    ls -= 1
                if matrix == []:
                    return res
                else:
                    dfs(matrix)
        dfs(matrix)
        return res
if __name__ == '__main__':
    S = Solution()
#     a = S.spiralOrder([
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ])
    # a = S.spiralOrder([[1]])
    # a = S.spiralOrder([[3],[2]])
    # a = S.spiralOrder([[1,2],[3,4]])
    a = S.spiralOrder([[2,5,8],[4,0,-1]])
    print(a)
