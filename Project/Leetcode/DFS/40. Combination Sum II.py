class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        ls = len(candidates)
        candidates.sort()

        def dfs(path, l, target):
            for i in range(l, ls):
                if target < candidates[i]: break

                # Cutting leaves, efficient!!
                if i > l and candidates[i] == candidates[i - 1]:
                    continue

                if target - candidates[i] == 0:
                    if path + [candidates[i]] not in res:
                        res.append(path + [candidates[i]])
                    break
                else:
                    dfs(path + [candidates[i]], i + 1, target - candidates[i])

        dfs([], 0, target)
        return res