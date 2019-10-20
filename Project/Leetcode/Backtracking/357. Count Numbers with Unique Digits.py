class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        res = 10
        choices = 9
        for i in range(1, n):
            choices = choices * (10 - i)
            res += choices
        return res
