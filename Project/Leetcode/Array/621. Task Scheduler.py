'''
max_val - 1 means last time, there no need to idel
n + 1 means every iterate, there should have n + 1 numbers
'''
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
            if i == max_val:
                count += 1
        return max((max_val - 1) * (n + 1) + count, ls)

if __name__ == '__main__':
    S = Solution()
    test = S.leastInterval(["B","B","B"], 2)
    print(test)