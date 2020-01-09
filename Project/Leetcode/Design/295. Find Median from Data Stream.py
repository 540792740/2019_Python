class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, -num))
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            return (float(self.max_heap[0] - self.min_heap[0])) / 2.0
        else:
            return float(self.max_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()