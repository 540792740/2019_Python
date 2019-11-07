import heapq

class Solution(object):
    # O(NlogN)
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dic = {}
        for x, y in points:
            dic[(x, y)] = x ** 2 + y ** 2

        dic = sorted(dic.items(), key = lambda d : d[1], reverse = False)
        # print(dic[0][1])
        # dic = dic.values.sort()
        # print(dic.values())
        return [dic[i][0] for i in range(K)]

    def kClosest1(self, points, K):
        heap = []
        for x, y in points:
            dist = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
                print(heap)
            else:
                heapq.heappush(heap, (dist, x, y))
                print(heap)
        return [(x, y) for (dist, x, y) in heap]

if __name__ == '__main__':
    S = Solution()
    # test = S.kClosest1([[1,3],[-2,2]], 1)
    test = S.kClosest1([[3,3],[-2,4], [5,-1]], 2)
    print(test)