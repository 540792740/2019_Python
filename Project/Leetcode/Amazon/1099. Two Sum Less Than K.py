class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
# Two pointer
        def quickSort(A, low, high):
            l = low
            r = high
            if low <= high:
                pivot = A[high]
                while l < r:
                    while l < r and A[l] <= pivot:
                        l += 1
                    A[r] = A[l]

                    while l < r and A[r] >= pivot:
                        r -= 1
                    A[l] = A[r]
                A[l] = pivot
                quickSort(A, low, l - 1)
                quickSort(A, l + 1, high)
        res = -2 ^ 31
        ls = len(A)
        quickSort(A, 0, ls - 1)
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            else:
                res = max(res, A[l] + A[r])
                l += 1
        if res == -2 ^ 31: return -1
        return res
if __name__ == '__main__':
    S = Solution()
    # test = S.twoSumLessThanK([34,23,1,24,75,33,54,8], 60)
    test = S.twoSumLessThanK([358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549],1800)
    print(test)