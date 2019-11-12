import heapq
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            temp = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += temp
            heapq.heappush(sticks, temp)
        return res


if __name__ == '__main__':
    S = Solution()
    test = S.connectSticks([2,4,3])
    print(test)