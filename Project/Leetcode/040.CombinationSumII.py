class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ls = len(candidates)
        candidates.sort()
        res = []
        def dfs(target, start, vlist):
            if target == 0:
                res.append(vlist)
            for i in range(start, ls):
                if target < candidates[i]:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                else:
                    dfs(target - candidates[i], i + 1, vlist + [candidates[i]])
        dfs(target, 0, [])
        return res


if __name__ == '__main__':
    S = Solution()
    a = S.combinationSum2([4,6,2,8,3,3,5],13)
    a = S.combinationSum2([2,5,2,1,2], 5)
    print(a)