class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        dic = {}
        ls = len(cells)
        if ls <= 1: return cells
        if ls == 2: return [0, 0]
        if N % 14 == 0 and N != 0:
            N = 14
        else:
            N = N % 14
        while N > 0:
            N -= 1
            pre = cells[0]
            cells[0] = 0
            for i in range(1, ls - 1):
                if pre == cells[i + 1]:
                    pre = cells[i]
                    cells[i] = 1
                else:
                    pre = cells[i]
                    cells[i] = 0
            cells[-1] = 0

        return cells

S = Solution()
test = S.prisonAfterNDays([1,0,0,1,0,0,1,0], 18)
test = S.prisonAfterNDays([1,0,0,1,0,0,0,1], 826)
print(test)