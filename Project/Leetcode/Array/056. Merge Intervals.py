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


if __name__=='__main__':
    S = Solution()
    a = S.merge([[2,6],[8,10],[1,3],[15,18]])
    print(a)