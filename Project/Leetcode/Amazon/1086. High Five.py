class Solution(object):
    # 95%
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        # init a dic to save all students
        dic = collections.defaultdict(list)
        res = []
        for i, j in items:
            dic[i].append(j)
        for i in range(1, len(dic) + 1):
            res.append([i, sum(sorted(dic[i])[-5:]) / 5])
        return res

if __name__ == '__main__':
    S = Solution()
    test = S.highFive([[1, 60], [1, 65], [1, 87], [1, 91], [1, 92], [1, 100], [2, 76], [2, 77], [2, 93], [2, 97], [2, 100]])
    print(test)
