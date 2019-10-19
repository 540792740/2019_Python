'''
This line is very very important!!!!!!!!!!!!!!!!!!!!
if target >= candidates[i]:
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        ans = []
        def backtracking(candidates, target, subset):
            if target == 0:
                ans.append(subset)
                return
            for i in range(len(candidates)):
                if target >= candidates[i]:
                    backtracking(candidates[i:], target - candidates[i], subset + [candidates[i]])
        backtracking(candidates, target, [])
        return ans

if __name__ == '__main__':
    S = Solution()
    test = S.combinationSum([2,3,6,7], 7)
    print(test)