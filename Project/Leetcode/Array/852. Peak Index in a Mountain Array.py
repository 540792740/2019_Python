class Solution(object):
    # 99%
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ls = len(A)
        if ls == 0: return None
        if ls == 1: return 0
        if ls == 2:
            if A[0] > A[1]: return 0
            else: return 1
        for i in range(1, ls - 1):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                return i