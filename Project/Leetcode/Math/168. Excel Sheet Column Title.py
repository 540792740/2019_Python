class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        AscII = ord('A')
        # print(AscII, chr(65))
        while n > 0:
            res = chr((n - 1) % 26  + AscII) + res
            # print((n - 1) % 26 + AscII)
            n = (n - 1) // 26
        return res

S = Solution()
test = S.convertToTitle(26)
print(test)
