'''
前三个先写出来，后面的一个一个写。
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
           return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            arr = [1]
            j = 1
            while j < i:
                print(res[i-1][j - 1] + res[i - 1][j])
                arr.insert(j,res[i-1][j - 1] + res[i - 1][j])
                j += 1
                if j == i:
                    arr.insert(j,1)
            res.append(arr)

        return res

if __name__ == '__main__':
    S = Solution()
    a = S.generate(5)
    print(a)