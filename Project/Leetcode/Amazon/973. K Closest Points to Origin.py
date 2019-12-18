'''
Question:
1.  Input contains a list of points coordinate and the length of output?
2.  Coordinate of points can be either positive or negative.
3.  Return a list of points coordinate
4.  Distance is (2, 2), sqrt(8)
5.  How to deal with the same distance?

Solution:
1.  Init a dic, key is the distance, value is the coordinate of the point
2.  Sort the dic, return

'''
import heapq

class Solution(object):
    # O(NlogN)
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        #  Init dic, key: distance, value : (x, y)
        dic = {}
        for i, j in points:
            dic[(i, j)] = i ** 2 + j ** 2
        # Sort
        dic = sorted(dic.items(), key=lambda b: b[1], reverse=False)
        return [dic[element][0] for element in range(K)]

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