class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals: return True
        intervals.sort()
        l, r = intervals[0]
        for x, y in intervals[1:]:
            if r > x: return False
            r = y
        return True