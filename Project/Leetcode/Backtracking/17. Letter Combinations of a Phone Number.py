class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9': 'wxyz'
        }
        self.backtracking(mapping, res, digits, '')
        return res
    def backtracking(self, mapping, res, digital, subset):
        if digital == '':
            return res.append(subset)
        for c in mapping[digital[0]]:
            self.backtracking(mapping, res, digital[1:], subset + c)

if __name__ == '__main__':
    S = Solution()
    test = S.letterCombinations('23')
    print(test)


