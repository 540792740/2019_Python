class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key = lambda x: x[0])
        print(intervals)
        l, r = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            cl, cr = intervals[i]
            if r < cl:
                res.append([l,r])
                l, r = cl, cr
            else:
                r = max(r, cr)
        res.append([l,r])
        return res

if __name__=='__main__':
    S = Solution()
    a = S.merge([[2,6],[8,10],[1,3],[15,18]])
    print(a)