'''
Important: Backtracking, there should be nums[i + 1:] !! remember!
'''

class Solution(object):
    def subsets(self, nums):
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            temp = []
            for j in range(len(nums)):
                print(i & 1 << j)
                if i & 1 << j:
                    temp.append(nums[j])
            print(temp, i)
            res.append(temp)
        return res

    def subsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res
    def dfs(self, nums, res, subset):
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], res, subset + [nums[i]])
        res.append(subset)
if __name__ == '__main__':
    S = Solution()
    test = S.subsets([1, 2, 3])
    print(test)
    print(1 << 1)