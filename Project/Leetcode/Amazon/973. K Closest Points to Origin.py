class Solution(object):
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


if __name__ == '__main__':
    S = Solution()
    test = S.kClosest([[1,3],[-2,2]], 1)
    test = S.kClosest([[3,3],[5,-1],[-2,4]], 2)
    print(test)