class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        def find_max(A, l, r, target):
            start = l
            while l <= r:
                mid = (l + r) // 2
                if target > A[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            #high >= start, absolutely to make sure there is a value.
            print(r)
            return A[r] #if high >= start else None
        res = -1
        A.sort()
        for i, u in enumerate(A):

            target = K - u
            val = find_max(A, i + 1, len(A) - 1, target)
            if val + u == 1796:
                print((val, u) )
            if val is not None and res < val + u < K:
                res = val + u
        return res


if __name__ == '__main__':
    S = Solution()
    # test = S.twoSumLessThanK([34,23,1,24,75,33,54,8], 60)
    test = S.twoSumLessThanK([358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549],1800)
    print(test)