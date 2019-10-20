class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        visited = [False] * len(nums)
        res = []
        def dfs(subset):
            print(subset)
            if len(subset) == len(nums):
                res.append(subset)
            else:
                for i in range(len(nums)):
                    # Key is this line, to avoid Redundant
                    if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                        continue
                    if visited[i] == False:
                        visited[i] = True
                        dfs(subset + [nums[i]])
                        visited[i] = False
        dfs([])
        return res


                # 6% LOL Backtracking by myself
    def permuteUnique1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, nums, [])
        return res
    def dfs1(self, res, nums, subset):
        if not nums and subset not in res:
            res.append(subset)
        for i in range(len(nums)):
            self.dfs(res, nums[:i] + nums[i + 1:], subset + [nums[i]])


if __name__ == '__main__':
    S = Solution()
    test = S.permuteUnique([1,2,1,2])
    # test = S.permuteUnique([0])
    print(test)