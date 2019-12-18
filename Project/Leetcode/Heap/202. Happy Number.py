class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = set()
        while n:
            if n == 1: return True
            n = sum(int(i) ** 2 for i in str(n))
            if n in dic: return False
            dic.add(n)
            print(n)
