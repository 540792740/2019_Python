import heapq
class Solution(object):
    def lastStoneWeight(self, A):
        """
        :type stones: List[int]
        :rtype: int
        """
        pq = [-x for x in A]
        heapq.heapify(pq)
        print(pq)
        for i in range(len(A) - 1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            print(x, y)
            heapq.heappush(pq, -abs(x - y))
            print(pq)
        return -pq[0]


if __name__ == '__main__':
    S = Solution()
    test = S.lastStoneWeight([2,7,4,1,8,1])
    print(test)