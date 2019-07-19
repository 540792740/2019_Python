class Solution(object):
    def combinationSum(self, candidates, target):
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
                else:
                    dfs(target - candidates[i], i, vlist + [candidates[i]])
        dfs(target,0,[])
        return res



if __name__ == '__main__':
    S = Solution()
    a = S.combinationSum([8,7,4,3],11)
    print(a)