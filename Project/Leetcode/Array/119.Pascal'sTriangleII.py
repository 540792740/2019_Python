'''
from Third row, change the value of each row, reverse to add value till final
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        if rowIndex <= 1 :
            return [1] * (rowIndex + 1)
        row = [1,1]
        idx = 2
        while idx <= rowIndex:
            r = list(range(1, idx))
            print(r)
            for i in r[::-1]:
                row[i] = row[i-1] + row[i]
            row.append(1)
            idx += 1
        return row

if __name__ == '__main__':
    S = Solution()
    a = S.getRow(7)
    print(a)