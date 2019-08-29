'''
XII:    X left, I right: X + I + I = 10 + 1 + 1 = 12
IX:     I left, X right: I < X  So:X - I = 10 - 1 = 9
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        retInt = 0
        localMax = 0
        RomanDict = {"I": 1, "V": 5, "X": 10, "L": 50,"C": 100, "D":500, "M": 1000}

        for c in reversed(s):
            val = RomanDict[c]
            if localMax <= val:
                retInt += val
                localMax = val
            else:
                retInt -= val

        return retInt


if __name__ == "__main__":
    S = Solution()
    a = S.romanToInt("III")
    print(a)