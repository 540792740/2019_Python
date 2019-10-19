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
if __name__ == '__main__':
    S = Solution()
    test = S.letterCasePermutation("a1b2")
    print(test)