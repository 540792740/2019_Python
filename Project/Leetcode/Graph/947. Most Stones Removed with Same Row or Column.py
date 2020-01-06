import collections
class Solution:
    def removeStones(self, stones):
        ls = len(stones)
        stones = list(map(tuple, stones))
        dic = {}
        s = set(stones)
        for i, j in stones:
            dic[i] = dic.get(i, []) + [j]
            dic[j] = dic.get(j, []) + [i]

        def dfs(i, j):
            for y in dic[i]:
                if (i, y) not in s: continue
                s.remove((i, y))
                dfs(i, y)
            for x in dic[j]:
                if (x, j) not in s: continue
                s.remove((x, j))
                dfs(x, j)
        res = 0
        for i, j in stones:
            if (i, j) not in s: continue
            s.remove((i, j))
            dfs(i, j)
            res += ls - len(s) - 1
            ls = len(s)
        return res

S = Solution()
test = S.removeStones( [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
print(test)