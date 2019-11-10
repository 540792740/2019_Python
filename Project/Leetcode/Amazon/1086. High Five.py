class Solution(object):
    # 95%
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        items = sorted(items)
        print(items)
        ls = len(items) - 1
        dic = {}
        count = 0
        i = ls
        while i >= 0:
            if items[i][0] not in dic:
                dic[items[i][0]] = items[i][1]
            else:
                dic[items[i][0]] += items[i][1]
            count += 1
            if count == 5:
                dic[items[i][0]] //= 5
                count = 0
                while i > 0 and items[i][0] == items[i - 1][0]:
                    i -= 1

            i -= 1
        return [[i, dic[i]] for i in dic]

if __name__ == '__main__':
    S = Solution()
    test = S.highFive([[1, 60], [1, 65], [1, 87], [1, 91], [1, 92], [1, 100], [2, 76], [2, 77], [2, 93], [2, 97], [2, 100]])
    print(test)
