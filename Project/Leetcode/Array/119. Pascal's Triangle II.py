class Solution:
    # 94%
    def getRow(self, rowIndex):
        pascal = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                pascal[j] += pascal[j - 1]
        return pascal

if __name__ == '__main__':
    S = Solution()
    test = S.getRow(3)
    print(test)
a = [1,2]
a.remove(1)
print(a)