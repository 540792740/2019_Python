class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        ls = len(A)
        count = 0
        A.sort()
        temp = A[0]
        for i in range(1, ls):
            if A[i] <= temp:
                temp += 1
                count += temp - A[i]
            else:
                temp = A[i]
        return count
