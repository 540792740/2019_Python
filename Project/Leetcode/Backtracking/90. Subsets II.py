class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        nums.sort()
        self.res = [[]]

        def helper(nums, subset):
            if subset not in self.res:
                self.res.append(subset)
            ls = len(nums)
            for i in range(ls):

                # This line can improve efficient
                if i - 1 >= 0 and nums[i] == nums[i - 1]:
                    continue
                helper(nums[i + 1:], subset + [nums[i]])

        helper(nums, [])
        return self.res

if __name__ == '__main__':
    S = Solution()
    test = S.subsetsWithDup([1,1,1])
    # test = S.subsetsWithDup([1])
    # test = S.subsetsWithDup([0])
    # test = S.subsetsWithDup([])
    print(test)