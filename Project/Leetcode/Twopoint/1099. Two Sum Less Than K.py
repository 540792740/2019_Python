class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        Max_res = -1
        l, r = 0, len(A) - 1
        while l < r:
            temp = A[l] + A[r]
            if temp < K and temp > Max_res:
                Max_res = temp
            if temp < K:
                l += 1
            else:
                r -= 1
        return Max_res


if __name__ == '__main__':
    S = Solution()
    # test = S.twoSumLessThanK([34,23,1,24,75,33,54,8], 60)
    test = S.twoSumLessThanK([358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549],1800)
    print(test)