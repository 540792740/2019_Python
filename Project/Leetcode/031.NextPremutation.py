'''
下一个字典序，先交换，然后reverse。
Code comes from: https://blog.csdn.net/fuxuemingzhu/article/details/82113409
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)

        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    self.swap(nums, i - 1, j)
                    break

    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        for k in range(i, int((i + j) / 2 + 1)):
            self.swap(nums, k, i + j - k)
            print(nums)

    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        n = ls - 1
        # n is index
        while n > 0 and nums[n - 1] >= nums[n]:
            n -= 1
        self.reverse(nums, n, ls - 1)
        for i in range(n, ls):
            if nums[i] > nums[n - 1]:
                self.swap(nums, n - 1, i)
                break
        print(nums)
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, i, j):
        for k in range(i, int((i + j) / 2 + 1)):
            self.swap(nums, k, i + j - k)


if __name__ == '__main__':
    s = Solution()
    # s.nextPermutation([1,5,8,4,7,6,5,3,1])
    # s.nextPermutation([1,2,3])
    # s.nextPermutation([2,3,1])
    s.nextPermutation([5,1,1])
