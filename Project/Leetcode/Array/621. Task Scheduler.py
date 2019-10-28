class Solution:
    def leastInterval(self, tasks, n):
        count = 0
        ls = len(tasks)
        dic = {}
        for i in tasks:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        max_val = max(dic.values())
        for i in dic.values():
            print(i)
        print(dic.values())


if __name__ == '__main__':
    S = Solution()
    test = S.leastInterval(["A","A","A","B","B","B"], 2)
    print(test)