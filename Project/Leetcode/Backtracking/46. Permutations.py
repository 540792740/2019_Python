class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums,[], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i + 1:], path +[nums[i]], res)
        print(path)

if __name__ == '__main__':
    S = Solution()
    test = S.permute([1,2,3])
    print(test)