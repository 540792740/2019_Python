class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        digits = {str(x) for x in range(0,10)}
        print(digits)
        A = ['']
        for s_digit in S:
            Alpha = []
            if s_digit in digits:
                for a_digit in A:
                    Alpha.append(a_digit + s_digit)
            else:
                for a_digit in A:
                    Alpha.append(a_digit+ s_digit.lower())
                    Alpha.append(a_digit+ s_digit.upper())
            A = Alpha
        return A

    #80% bymyself
    def letterCasePermutation1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        digit = {str(x) for x in range(10)}
        ls = len(S)
        def helper(subset, s, index):

            for i in s:
                if i in digit:
                    subset += i
                    index += 1
                else:
                    helper(subset + i.lower(), s[index + 1:], 0)
                    helper(subset + i.upper(), s[index + 1:], 0)
                    break
            if len(subset) == ls:
                res.append(subset)
                return
        helper('', S, 0)
        return res


if __name__ == '__main__':
    S = Solution()
    test = S.letterCasePermutation1("a1b2")
    print(test)