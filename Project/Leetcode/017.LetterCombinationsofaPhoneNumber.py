class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return[]
        mapping = {'2':['a', 'b', 'c'],
                   '3': ['e', 'd', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        res = []
        self.backtracking(res, '', mapping, digits)
        return res
    def backtracking(self, res, subset, mapping, digits):
        if digits == '':
            res.append(subset)
            return
        for c in mapping[digits[0]]:
            self.backtracking(res, subset + c, mapping,digits[1:])


if __name__ == "__main__":
    S = Solution()
    a = S.letterCombinations('234')
    print(a)