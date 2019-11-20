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
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if guess(mid) == 0: return mid
            if guess(l) == guess(mid):
                l = mid + 1
            elif guess(r) == guess(mid):
                r = mid - 1

