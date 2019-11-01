# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(1) == 0: return 1
        b = [1, n]
        while 1:
            mid = (b[0] + b[1]) // 2
            l = b[0]
            r = b[1]
            if guess(i) == guess(m):
                b = [mid, r]
            else:
                b = [l, mid]
            if guess(r) == 0: return r