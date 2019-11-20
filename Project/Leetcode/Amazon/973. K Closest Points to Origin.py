import heapq

class Solution(object):
    # O(NlogN)
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dic = collections.defaultdict(list)
        list_res = []
        res = []
        for i, j in points:
            dic[i**2 + j **2].append([i, j])
            list_res.append(i**2 + j **2)
        list_res.sort()
        for i in range(K):
            if len(res) < K:
                res.extend(dic[list_res[i]])
        return res

    def kClosest1(self, points, K):
        heap = []
        for x, y in points:
            if len(heap) == K:
                heapq.heappushpop(heap, (-(x ** 2 + y ** 2), x, y))
            else:
                heapq.heappush(heap, (-(x ** 2 + y ** 2), x, y))

        return [[x, y] for (_, x, y) in heap]

if __name__ == '__main__':
    S = Solution()
    # test = S.kClosest1([[1,3],[-2,2]], 1)
    test = S.kClosest1([[3,3],[-2,4], [5,-1]], 2)
    print(test)