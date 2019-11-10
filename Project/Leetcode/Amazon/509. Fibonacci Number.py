class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0: return 0
        if N == 1: return 1
        if N == 2: return 1
        res = [0, 1, 1]
        while N >= 2:
            if N == 2: return res[-1]
            res.append(res[len(res) - 1] + res[len(res) - 2])
            N -= 1


